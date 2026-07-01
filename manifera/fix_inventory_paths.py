import os
import re

files_to_update = [
    '/Users/duyle/sickn33/manifera/content_inventory.md',
    '/Users/duyle/sickn33/manifera/content_inventory_2027.md'
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace occurrences like:
    # ](./july-2026/... -> ](./2026/july-2026/...
    # ](./august-2027/... -> ](./2027/august-2027/...
    
    # regex pattern to match standard markdown relative links to these folders
    # match: ](./month-year/
    # replace with: ](./year/month-year/
    
    def replacer(match):
        month = match.group(1)
        year = match.group(2)
        return f"](./{year}/{month}-{year}/"

    # Pattern: \]\(\.\/([a-z]+)-(2026|2027)\/
    new_content = re.sub(r'\]\(\.\/([a-z]+)-(2026|2027)\/', replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Moved folders and updated markdown files successfully.")
