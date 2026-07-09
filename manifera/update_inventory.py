import os
import re

directory = "/Users/duyle/sickn33/manifera/2026/october-2026"
files = sorted([f for f in os.listdir(directory) if f.endswith('.md') and not f.endswith('-social.md')])

def get_frontmatter_value(content, key):
    match = re.search(r'^' + key + r':\s*(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else ""

def get_first_paragraph(content):
    parts = content.split('</script>')
    if len(parts) > 1:
        text_after_script = parts[1].strip()
        paragraphs = text_after_script.split('\n\n')
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('#') and not p.startswith('##'):
                return p[:100] + "..." if len(p) > 100 else p
    return ""

rows = []
for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    title = get_frontmatter_value(content, 'Title')
    title = title.strip('"')
    keywords = get_frontmatter_value(content, 'Keywords')
    buyer_stage = get_frontmatter_value(content, 'Buyer Stage')
    format = get_frontmatter_value(content, 'Content Format')
    
    # Extract number from filename
    match = re.search(r'^(\d+)-', file)
    num = match.group(1) if match else "00"
    
    social_file = file.replace('.md', '-social.md')
    intro = get_first_paragraph(content).replace('\n', ' ')
    
    row = f"| {num}  | {title} | {keywords}, Manifera | {buyer_stage} / {format} | [{file}](./2026/october-2026/{file}) | | {intro} | [{social_file}](./2026/october-2026/{social_file}) | |"
    rows.append(row)

with open('/Users/duyle/sickn33/manifera/content_inventory.md', 'a') as f:
    f.write("\n")
    for row in rows:
        f.write(row + "\n")

print(f"Added {len(rows)} rows to content_inventory.md")
