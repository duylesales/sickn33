import os
import re

def main():
    inventory_path = "/Users/duyle/sickn33/launchstudio/content_inventory.md"
    
    with open(inventory_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    def replace_link(match):
        full_path = match.group(1)
        basename = os.path.basename(full_path)
        return f"[{basename}](./{full_path})"
        
    # Replace [Link](./path/to/file) with [file](./path/to/file)
    new_content = re.sub(r'\[Link\]\(\./([^)]+)\)', replace_link, content)
    
    if new_content != content:
        with open(inventory_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated links in content_inventory.md.")
    else:
        print("No links found to update.")

if __name__ == "__main__":
    main()
