import os
import glob
import re

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
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "model" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower or "sql" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "pricing" in title_lower or "cost" in title_lower or "margin" in title_lower: emoji = "💸"
    elif "security" in title_lower or "privacy" in title_lower or "auth" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "growth" in title_lower or "seo" in title_lower: emoji = "📈"
    elif "startup" in title_lower or "founder" in title_lower or "vc" in title_lower: emoji = "💡"
    
    # Split snippet into paragraphs
    snippet_sentences = snippet.replace(". ", ".\n\n")
    
    post = f"{emoji} {title}\n\n{snippet_sentences}\n\nDiscover more strategies for your startup journey: [Link]\n\n#B2B #SaaS #AI"
    return post

def main():
    count = 0
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            social_files = glob.glob(os.path.join(full_dir_path, "*-social.md"))
            for file_path in social_files:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Check if it is truncated (e.g., lacks hashtags or is very short)
                if "#B2B" not in content and "#SaaS" not in content and len(content) < 150:
                    # Regenerate
                    orig_md_path = file_path.replace("-social.md", ".md")
                    if os.path.exists(orig_md_path):
                        with open(orig_md_path, "r", encoding="utf-8") as orig_f:
                            orig_content = orig_f.read()
                            
                        title = extract_title(orig_content)
                        snippet = extract_snippet(orig_content)
                        new_social = generate_social_post(title, snippet)
                        
                        with open(file_path, "w", encoding="utf-8") as out_f:
                            out_f.write(new_social + "\n")
                        count += 1

    print(f"Successfully regenerated {count} truncated social post files.")

if __name__ == "__main__":
    main()
