import os
import re

inventory_path = "content_inventory.md"

def generate_rows(dir_path, start_idx, end_idx):
    files = [f for f in os.listdir(dir_path) if re.match(r'^\d+-.*\.md$', f) and not f.endswith('-social.md')]
    # Filter files within range
    filtered = []
    for f in files:
        idx = int(f.split('-')[0])
        if start_idx <= idx <= end_idx:
            filtered.append((idx, f))
    
    filtered.sort(key=lambda x: x[0])
    
    rows = []
    for idx, f in filtered:
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
    return rows

# Generate August rows 9 to 60
august_rows = generate_rows("2026/august-2026", 9, 60)

# Generate September rows 1 to 60
september_rows = generate_rows("2026/september-2026", 1, 60)

with open(inventory_path, "r") as f:
    lines = f.readlines()

# Find end of August table
# Look for line with "| 8   |" or "| 8 |"
aug_insert_idx = -1
for i in range(len(lines)-1, -1, -1):
    if "| 8   |" in lines[i] or "| 8 |" in lines[i]:
        aug_insert_idx = i + 1
        break

if aug_insert_idx != -1:
    lines = lines[:aug_insert_idx] + [r + '\n' for r in august_rows] + lines[aug_insert_idx:]

# Append September
sep_header = [
    "\n## Tháng: September 2026\n\n",
    "| STT | Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn (Buyer Stage) | Bài viết (Article) | Đã Post lên | Đoạn trích (Snippet) | Bài Social Media | Đã Post lên |\n",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
]
lines.extend(sep_header)
lines.extend([r + '\n' for r in september_rows])

with open(inventory_path, "w") as f:
    f.writelines(lines)

print(f"Added {len(august_rows)} rows to August.")
print(f"Added {len(september_rows)} rows to September.")
