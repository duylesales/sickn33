import os
import glob

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
        line = line.strip()
        if line and not line.startswith("#"):
            snippet_lines.append(line)
            if len(" ".join(snippet_lines)) > 300:
                break
    
    full_snippet = " ".join(snippet_lines)
    # Get first 2-3 sentences
    sentences = full_snippet.split(". ")
    if len(sentences) > 2:
        return ". ".join(sentences[:2]) + "."
    return full_snippet

def generate_social_post(title, snippet):
    # Emojis based on keywords
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "model" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower or "sql" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "pricing" in title_lower or "cost" in title_lower or "margin" in title_lower: emoji = "💸"
    elif "security" in title_lower or "privacy" in title_lower or "auth" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "growth" in title_lower or "seo" in title_lower: emoji = "📈"
    elif "startup" in title_lower or "founder" in title_lower or "vc" in title_lower: emoji = "💡"
    
    post = f"{emoji} {title} | {snippet} Discover more strategies for your startup journey: [Link] #B2B #SaaS #AI"
    # remove newlines
    post = post.replace("\n", " ")
    return post

def main():
    all_files = []
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            md_files = sorted(glob.glob(os.path.join(full_dir_path, "*.md")))
            for f in md_files:
                all_files.append((month_dir, f))
                
    # Skip the 75 files we've already done
    # 0-4 (5), Batch0 (15), Batch1 (15), Batch2 (40) = 75
    remaining_files = all_files[75:]
    print(f"Remaining files to process: {len(remaining_files)}")
    
    output_lines = []
    for month_dir, file_path in remaining_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        title = extract_title(content)
        snippet = extract_snippet(content)
        social_post = generate_social_post(title, snippet)
        
        relative_path = f"./{month_dir}/{os.path.basename(file_path)}"
        month_formatted = month_dir.replace("-", " ").title()
        
        row = f"| {month_formatted} | {title} | [{os.path.basename(file_path)}]({relative_path}) | {social_post} |"
        output_lines.append(row)
        
    with open("batch_all.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")
        
    print(f"Successfully generated {len(output_lines)} rows to batch_all.md")

if __name__ == "__main__":
    main()
