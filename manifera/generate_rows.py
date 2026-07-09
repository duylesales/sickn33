import os
import re

dir_path = "2026/july-2026"
files = [f for f in os.listdir(dir_path) if re.match(r'^(2[0-9]|3[0-7])-.*\.md$', f) and not f.endswith('-social.md')]
files.sort(key=lambda x: int(x.split('-')[0]))

rows = []
for idx, f in enumerate(files, start=20):
    path = os.path.join(dir_path, f)
    with open(path, 'r') as file:
        content = file.read()
    
    title_match = re.search(r'^Title:\s*"(.*?)"', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""
    
    keywords_match = re.search(r'^Keywords:\s*(.*?)$', content, re.MULTILINE)
    keywords = keywords_match.group(1) if keywords_match else ""
    
    stage_match = re.search(r'^Buyer Stage:\s*(.*?)$', content, re.MULTILINE)
    stage = stage_match.group(1) if stage_match else ""
    
    # Snippet: first paragraph after </script>
    parts = content.split('</script>')
    snippet = ""
    if len(parts) > 1:
        # get the text after the first </script>
        after_script = parts[1].strip()
        paragraphs = after_script.split('\n\n')
        for p in paragraphs:
            if p.strip() and not p.startswith('#'):
                snippet = p.strip().replace('\n', ' ')
                # Truncate to ~100 chars
                if len(snippet) > 100:
                    snippet = snippet[:100] + "..."
                break
                
    article_link = f"[{f}](./{dir_path}/{f})"
    social_file = f.replace('.md', '-social.md')
    social_link = f"[{social_file}](./{dir_path}/{social_file})"
    
    row = f"| {idx} | {title} | {keywords} | {stage} | {article_link} | | {snippet} | {social_link} | |"
    rows.append(row)

for r in rows:
    print(r)
