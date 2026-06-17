import os
import glob

BASE_DIR = "/Users/duyle/sickn33/manifera"
MONTH_DIRS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026", "january-2027"
]

def main():
    inventory_path = os.path.join(BASE_DIR, "content_inventory.md")
    with open(inventory_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    in_table = False
    current_month_dir = ""
    row_idx = 1
    
    # Pre-fetch sorted social files for each month
    month_files = {}
    for month in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month)
        if os.path.exists(full_dir_path):
            files = sorted(glob.glob(os.path.join(full_dir_path, "*-social.md")))
            month_files[month] = [os.path.basename(f) for f in files]
    
    for i, line in enumerate(lines):
        if "## Tháng:" in line:
            month_str = line.split("## Tháng:")[1].strip()
            # Convert "July 2026" to "july-2026"
            current_month_dir = month_str.replace(" ", "-").lower()
            new_lines.append(line)
        elif "| Tiêu đề (Title)" in line:
            in_table = True
            row_idx = 1
            new_lines.append("| Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn | Tóm lược | Bài Social Media |\n")
        elif in_table and line.startswith("|---") or (in_table and line.startswith("| ---")):
            new_lines.append("|---|---|---|---|---|\n")
        elif in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            # parts has empty string at 0 and end, so parts[1] is Title, parts[2] is Keywords, parts[3] is Giai doan, parts[4] is Tom luoc
            if len(parts) >= 5:
                title = parts[1]
                kw = parts[2]
                stage = parts[3]
                summary = parts[4]
                
                # Fetch corresponding social link by row_idx
                social_link_str = ""
                if current_month_dir in month_files and row_idx - 1 < len(month_files[current_month_dir]):
                    social_filename = month_files[current_month_dir][row_idx - 1]
                    social_link_str = f"[{social_filename}](./{current_month_dir}/{social_filename})"
                
                new_lines.append(f"| {title} | {kw} | {stage} | {summary} | {social_link_str} |\n")
                row_idx += 1
            else:
                new_lines.append(line)
        elif in_table and line.strip() == "":
            in_table = False
            new_lines.append(line)
        else:
            new_lines.append(line)
            
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
        
    print("Fixed content_inventory.md columns and links.")

if __name__ == "__main__":
    main()
