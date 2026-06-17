import os
import glob
import re

BASE_DIR = "/Users/duyle/sickn33/manifera"
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
        # Support both '## Content' and '## Nội dung'
        if "## Content" in line or "## Nội dung" in line:
            start_idx = i + 1
            break
    
    snippet_lines = []
    for line in lines[start_idx:]:
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("<"):
            snippet_lines.append(line)
            if len(" ".join(snippet_lines)) > 300:
                break
    
    full_snippet = " ".join(snippet_lines)
    sentences = full_snippet.split(". ")
    if len(sentences) > 2:
        return ". ".join(sentences[:2]) + "."
    return full_snippet

def generate_social_post(title, snippet):
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "model" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower or "sql" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "cost" in title_lower or "roi" in title_lower: emoji = "💸"
    elif "security" in title_lower or "quality" in title_lower or "qa" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "growth" in title_lower or "devops" in title_lower: emoji = "📈"
    elif "offshore" in title_lower or "team" in title_lower or "cto" in title_lower: emoji = "👨‍💻"
    elif "app" in title_lower or "mobile" in title_lower: emoji = "📱"
    
    snippet_sentences = snippet.replace(". ", ".\n\n")
    
    post = f"{emoji} {title}\n\n{snippet_sentences}\n\nDiscover more strategies for scaling your tech teams: [Link]\n\n#SoftwareDevelopment #TechLeadership #Manifera"
    return post

def main():
    # Phase 1: Generate social post files
    count = 0
    title_to_social = {}
    
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            md_files = glob.glob(os.path.join(full_dir_path, "*.md"))
            for f in md_files:
                if f.endswith("-social.md"): continue
                
                with open(f, "r", encoding="utf-8") as file_obj:
                    content = file_obj.read()
                    
                title = extract_title(content)
                snippet = extract_snippet(content)
                social_content = generate_social_post(title, snippet)
                
                rel_path = f"{month_dir}/{os.path.basename(f)}"
                social_rel_path = rel_path[:-3] + "-social.md"
                
                # Write social post file
                abs_social_path = os.path.join(BASE_DIR, social_rel_path)
                with open(abs_social_path, "w", encoding="utf-8") as out_f:
                    out_f.write(social_content + "\n")
                    
                title_to_social[title.strip()] = social_rel_path
                count += 1
                
    print(f"Generated {count} social post files.")

    # Phase 2: Update content_inventory.md
    inventory_path = os.path.join(BASE_DIR, "content_inventory.md")
    with open(inventory_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        if "| Tiêu đề (Title)" in line:
            in_table = True
            new_lines.append(line.rstrip('\n') + " | Bài Social Media |\n")
        elif in_table and line.startswith("|---") or (in_table and line.startswith("| ---")):
            # Update the separator
            new_lines.append(line.rstrip('\n') + " --- |\n")
        elif in_table and line.startswith("|"):
            parts = line.split("|")
            if len(parts) >= 3:
                title = parts[1].strip()
                social_link = title_to_social.get(title, "")
                if social_link:
                    basename = os.path.basename(social_link)
                    social_link_str = f"[{basename}](./{social_link})"
                else:
                    social_link_str = ""
                    
                # Format properly with spacing
                new_lines.append(line.rstrip('\n') + f" {social_link_str} |\n")
            else:
                new_lines.append(line)
        elif in_table and line.strip() == "":
            in_table = False
            new_lines.append(line)
        else:
            new_lines.append(line)
            
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
        
    print(f"Updated content_inventory.md with {len(title_to_social)} links.")

if __name__ == "__main__":
    main()
