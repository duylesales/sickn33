import os
import re

MONTHS = [
    "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026"
]
BASE_DIR = "/Users/duyle/sickn33/manifera"

def rename_in_dir(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    
    # Sort files based on the integer prefix
    def get_prefix(filename):
        match = re.match(r'^(\d+)-', filename)
        return int(match.group(1)) if match else 9999
        
    files.sort(key=get_prefix)
    
    renamed_count = 0
    for i, filename in enumerate(files, start=1):
        # Remove old prefix
        new_name_base = re.sub(r'^\d+-', '', filename)
        new_name = f"{i:02d}-{new_name_base}"
        
        if new_name != filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            renamed_count += 1
            
    print(f"[{os.path.basename(directory)}] Renamed {renamed_count} files. Now ordered from 01 to {len(files)}.")

def main():
    for month in MONTHS:
        month_dir = os.path.join(BASE_DIR, month)
        if os.path.exists(month_dir):
            rename_in_dir(month_dir)

if __name__ == "__main__":
    main()
