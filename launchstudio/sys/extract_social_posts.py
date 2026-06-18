import os
import re

def main():
    inventory_path = "/Users/duyle/sickn33/launchstudio/content_inventory.md"
    with open(inventory_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the bounds of the first table and the second table
    first_table_start = -1
    first_table_end = -1
    second_table_start = -1
    
    for i, line in enumerate(lines):
        if "| Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn |" in line:
            first_table_start = i
        elif first_table_start != -1 and first_table_end == -1 and line.strip() == "":
            first_table_end = i
            
        if "| Tháng | Tiêu đề gốc | Đường dẫn | Bài Social Media" in line:
            second_table_start = i

    if first_table_end == -1 and first_table_start != -1:
        # Table might go to the end before the next section
        for i in range(first_table_start + 2, len(lines)):
            if not lines[i].startswith("|"):
                first_table_end = i
                break

    # Extract posts from the second table
    title_to_social_link = {}
    
    # Process the second table to extract files
    # The second table rows start at second_table_start + 2
    row_count = 0
    second_table_rows_to_keep = []
    
    for i in range(second_table_start, len(lines)):
        line = lines[i]
        if not line.startswith("|"):
            continue
            
        if i == second_table_start or i == second_table_start + 1:
            second_table_rows_to_keep.append(line)
            continue
            
        # Parse the row
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5:
            # parts[0] is empty (before first |)
            # parts[1] is Month
            # parts[2] is Tiêu đề gốc
            # parts[3] is Đường dẫn
            # parts[4] is Social Post
            
            title = parts[2]
            path_md = parts[3] # e.g. [01-what-is-ai.md](./july-2026/01-what-is-ai.md)
            social_content = parts[4]
            
            # Extract the actual relative path
            path_match = re.search(r'\((.*?)\)', path_md)
            if path_match:
                rel_path = path_match.group(1)
                
                # Make the social filename
                if rel_path.endswith('.md'):
                    social_rel_path = rel_path[:-3] + "-social.md"
                else:
                    social_rel_path = rel_path + "-social.md"
                    
                title_to_social_link[title] = social_rel_path
                
                # Write the social file
                abs_path = os.path.join(os.path.dirname(inventory_path), social_rel_path.lstrip('./'))
                # Ensure dir exists
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                with open(abs_path, "w", encoding="utf-8") as sf:
                    sf.write(social_content + "\n")
                    
            row_count += 1
            # We want to keep the first 5 rows (01 to 05)
            # Wait, the instruction says delete from "06-cursor..." onwards.
            # So keep the first 5 rows.
            if row_count <= 5:
                second_table_rows_to_keep.append(line)

    # Now update the first table
    new_lines = []
    for i, line in enumerate(lines):
        if first_table_start <= i < first_table_end:
            if i == first_table_start:
                new_line = line.rstrip('\n') + " Bài Social Media |\n"
                new_lines.append(new_line)
            elif i == first_table_start + 1:
                new_line = line.rstrip('\n') + "---|\n"
                new_lines.append(new_line)
            else:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 3:
                    title = parts[1]
                    social_link = title_to_social_link.get(title, "")
                    if social_link:
                        social_link_str = f"[Social Post]({social_link})"
                    else:
                        social_link_str = ""
                        
                    new_line = line.rstrip('\n') + f" {social_link_str} |\n"
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
        elif i >= second_table_start:
            # We skip appending original lines for the second table
            pass
        else:
            new_lines.append(line)
            
    # Append the truncated second table
    new_lines.extend(second_table_rows_to_keep)
    
    # Write back to content_inventory.md
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Extracted {row_count} social posts and updated {inventory_path}.")

if __name__ == "__main__":
    main()
