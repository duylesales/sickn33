import os
import glob

BASE_DIR = "/Users/duyle/sickn33/launchstudio"
MONTH_DIRS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026", "january-2027"
]

def main():
    count = 0
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            social_files = glob.glob(os.path.join(full_dir_path, "*-social.md"))
            for file_path in social_files:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Replace HTML breaks with actual markdown newlines
                new_content = content.replace("<br><br>", "\n\n")
                new_content = new_content.replace("<br>", "\n")
                new_content = new_content.replace("<br/>", "\n")
                new_content = new_content.replace("<br />", "\n")
                
                # Make sure there are no other weird HTML artifacts if possible,
                # but primarily focus on the <br> tags.
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1

    print(f"Successfully fixed formatting in {count} files.")

if __name__ == "__main__":
    main()
