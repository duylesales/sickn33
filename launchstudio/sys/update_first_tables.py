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

def build_mapping():
    mapping = {}
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            md_files = glob.glob(os.path.join(full_dir_path, "*.md"))
            for f in md_files:
                # skip the -social.md files
                if f.endswith("-social.md"):
                    continue
                with open(f, "r", encoding="utf-8") as file_obj:
                    content = file_obj.read()
                title = extract_title(content)
                rel_path = f"{month_dir}/{os.path.basename(f)}"
                social_rel_path = rel_path[:-3] + "-social.md"
                mapping[title.strip()] = social_rel_path
    return mapping

def main():
    title_to_social = build_mapping()
    inventory_path = "/Users/duyle/sickn33/launchstudio/content_inventory.md"
    
    with open(inventory_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        # Header of first tables
        if "| Tiêu đề (Title) | Từ khóa (Keywords) |" in line:
            in_table = True
            new_lines.append(line.rstrip('\n') + " Bài Social Media |\n")
        elif in_table and line.startswith("|---|"):
            new_lines.append(line.rstrip('\n') + "---|\n")
        elif in_table and line.startswith("|"):
            parts = line.split("|")
            if len(parts) >= 3:
                title = parts[1].strip()
                social_link = title_to_social.get(title, "")
                if social_link:
                    # check if the social file exists
                    abs_social_path = os.path.join(BASE_DIR, social_link)
                    if os.path.exists(abs_social_path):
                        social_link_str = f"[Link](./{social_link})"
                    else:
                        social_link_str = ""
                else:
                    social_link_str = ""
                    
                new_lines.append(line.rstrip('\n') + f" {social_link_str} |\n")
            else:
                new_lines.append(line)
        elif in_table and line.strip() == "":
            in_table = False
            new_lines.append(line)
        else:
            # Not in one of the first tables, just append
            new_lines.append(line)
            
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
        
    print("Successfully updated tables.")

if __name__ == "__main__":
    main()
