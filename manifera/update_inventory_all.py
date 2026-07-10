import os
import re

def get_frontmatter_value(content, key):
    pattern = r'^' + key.replace(' ', r'[ _]') + r':\s*(.+)$'
    match = re.search(pattern, content, re.MULTILINE | re.IGNORECASE)
    if match:
        val = match.group(1).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        return val
    return ""

def get_first_paragraph(content):
    content_no_frontmatter = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
    content_no_script = re.sub(r'<script.*?</script>', '', content_no_frontmatter, flags=re.DOTALL)
    paragraphs = content_no_script.split('\n\n')
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('#') and not p.startswith('##') and not p.startswith('<'):
            p = p.replace('\n', ' ')
            return p[:100] + "..." if len(p) > 100 else p
    return ""

def process_month(month_dir, month_name, start_stt):
    directory = f"/Users/duyle/sickn33/manifera/2026/{month_dir}"
    files = sorted([f for f in os.listdir(directory) if f.endswith('.md') and not f.endswith('-social.md')],
                   key=lambda x: int(re.search(r'^(\d+)', x).group(1)) if re.search(r'^(\d+)', x) else 999)
    
    rows = []
    rows.append(f"\n## Tháng: {month_name} 2026\n")
    rows.append("| STT | Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn (Buyer Stage) | Bài viết (Article) | Đã Post lên | Đoạn trích (Snippet) | Bài Social Media | Đã Post lên |")
    rows.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    current_stt = start_stt
    for file in files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = get_frontmatter_value(content, 'Title')
        keywords = get_frontmatter_value(content, 'Keywords')
        if "Manifera" not in keywords and keywords:
            keywords += ", Manifera"
            
        buyer_stage = get_frontmatter_value(content, 'Buyer Stage')
        format_val = get_frontmatter_value(content, 'Content Format')
        
        if format_val:
            buyer_stage = f"{buyer_stage} / {format_val}"
            
        social_file = file.replace('.md', '-social.md')
        intro = get_first_paragraph(content)
        
        row = f"| {current_stt} | {title} | {keywords} | {buyer_stage} | [{file}](./2026/{month_dir}/{file}) | | {intro} | [{social_file}](./2026/{month_dir}/{social_file}) | |"
        rows.append(row)
        current_stt += 1
    
    return rows, current_stt

months = [
    ('september-2026', 'September'),
    ('october-2026', 'October'),
    ('november-2026', 'November'),
    ('december-2026', 'December')
]

stt = 61
all_rows = []

for m_dir, m_name in months:
    rows, stt = process_month(m_dir, m_name, stt)
    all_rows.extend(rows)

with open('/Users/duyle/sickn33/manifera/content_inventory.md', 'a', encoding='utf-8') as f:
    for row in all_rows:
        f.write(row + "\n")

print("Generated full inventory for Sep to Dec successfully.")
