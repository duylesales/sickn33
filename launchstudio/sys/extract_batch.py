import os
import glob
import json
import sys

BASE_DIR = "/Users/duyle/sickn33/launchstudio"
MONTH_DIRS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026", "january-2027"
]

def extract_title(content):
    for line in content.split("\n"):
        if line.startswith("Title:"):
            return line.replace("Title:", "").strip()
        if line.startswith("# "):
            return line.replace("# ", "").strip()
    return "Unknown Title"

def extract_snippet(content):
    lines = content.split("\n")
    start_idx = 0
    for i, line in enumerate(lines):
        if "## Nội dung" in line:
            start_idx = i + 1
            break
    
    snippet_lines = []
    for line in lines[start_idx:]:
        if line.strip() and not line.startswith("#"):
            snippet_lines.append(line.strip())
            if len(" ".join(snippet_lines)) > 800:
                break
    return " ".join(snippet_lines)[:800]

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
        
    start_idx = int(sys.argv[1])
    batch_size = int(sys.argv[2])
    
    all_files = []
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            md_files = sorted(glob.glob(os.path.join(full_dir_path, "*.md")))
            for f in md_files:
                all_files.append((month_dir, f))
                
    batch_files = all_files[start_idx : start_idx + batch_size]
    
    results = []
    for month_dir, file_path in batch_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        title = extract_title(content)
        snippet = extract_snippet(content)
        relative_path = f"{month_dir}/{os.path.basename(file_path)}"
        
        results.append({
            "month": month_dir.replace("-", " ").title(),
            "title": title,
            "path": relative_path,
            "snippet": snippet
        })
        
    out_data = {"data": results}
    with open("batch.json", "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
