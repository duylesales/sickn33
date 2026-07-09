import os
import re

dir_path = "2026/july-2026"
inventory_path = "content_inventory.md"

# 1. Get files 38 to 60
files = [f for f in os.listdir(dir_path) if re.match(r'^(3[8-9]|[4-5][0-9]|60)-.*\.md$', f) and not f.endswith('-social.md')]
files.sort(key=lambda x: int(x.split('-')[0]))

# 2. Extract metadata and generate rows
rows = []
for idx, f in enumerate(files, start=38):
    path = os.path.join(dir_path, f)
    with open(path, 'r') as file:
        content = file.read()
    
    title_match = re.search(r'^Title:\s*"(.*?)"', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""
    
    keywords_match = re.search(r'^Keywords:\s*(.*?)$', content, re.MULTILINE)
    keywords = keywords_match.group(1) if keywords_match else ""
    
    stage_match = re.search(r'^Buyer Stage:\s*(.*?)$', content, re.MULTILINE)
    stage = stage_match.group(1) if stage_match else ""
    
    parts = content.split('</script>')
    snippet = ""
    if len(parts) > 1:
        after_script = parts[1].strip()
        paragraphs = after_script.split('\n\n')
        for p in paragraphs:
            if p.strip() and not p.startswith('#'):
                snippet = p.strip().replace('\n', ' ')
                if len(snippet) > 100:
                    snippet = snippet[:100] + "..."
                break
                
    article_link = f"[{f}](./{dir_path}/{f})"
    social_file = f.replace('.md', '-social.md')
    social_link = f"[{social_file}](./{dir_path}/{social_file})"
    
    row = f"| {idx} | {title} | {keywords} | {stage} | {article_link} | | {snippet} | {social_link} | |"
    rows.append(row)

# 3. Update inventory
with open(inventory_path, "r") as f:
    lines = f.readlines()

insert_idx = -1
for i, line in enumerate(lines):
    if line.startswith("| 37 |"):
        insert_idx = i + 1
        break

if insert_idx != -1:
    lines = lines[:insert_idx] + [r + '\n' for r in rows] + lines[insert_idx:]
    with open(inventory_path, "w") as f:
        f.writelines(lines)
    print(f"Successfully added {len(rows)} rows starting after row 37.")
else:
    print("Could not find row 37")
