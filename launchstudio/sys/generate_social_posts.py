import os
import glob
import time
import google.generativeai as genai

# ---------------------------------------------------------------------------
# Setup & Configuration
# ---------------------------------------------------------------------------
# Make sure to run: pip install google-generativeai
# And set your API key: export GEMINI_API_KEY="your-api-key-here"

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Run: export GEMINI_API_KEY='your-api-key-here'")
    exit(1)

genai.configure(api_key=API_KEY)
# We use gemini-1.5-flash as it is fast and cheap, but you can change to 'gemini-1.5-pro'
model = genai.GenerativeModel('gemini-1.5-flash')

BASE_DIR = "/Users/duyle/sickn33/launchstudio"
INVENTORY_FILE = os.path.join(BASE_DIR, "content_inventory.md")
PROCESSED_LOG = os.path.join(BASE_DIR, "processed_social_posts.log")

MONTH_DIRS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026", "january-2027"
]

# The prompt instructions for the AI
SYSTEM_PROMPT = """
You are an expert social media manager. I will provide you with the markdown content of a blog post.
Your job is to read it and write a short, punchy, engaging social media post (optimized for LinkedIn or X) in English.
Keep it under 150 words. Include relevant emojis and a few hashtags. 
End the post with "[Link]" to act as a placeholder for the article URL.
Return ONLY the text of the social media post, nothing else.
"""

def get_processed_files():
    """Read the log file to see which articles have already been processed to avoid duplicates."""
    if not os.path.exists(PROCESSED_LOG):
        return set()
    with open(PROCESSED_LOG, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def mark_as_processed(filepath):
    """Log the file as processed."""
    with open(PROCESSED_LOG, "a", encoding="utf-8") as f:
        f.write(f"{filepath}\n")

def append_to_inventory(month, title, relative_path, social_post):
    """Append the generated row to content_inventory.md."""
    # Clean up the social post to be table-friendly (replace newlines with <br>)
    clean_post = social_post.strip().replace("\n", "<br>")
    
    # We escape pipe characters just in case the AI generated them
    clean_post = clean_post.replace("|", "\|")
    
    row = f"| {month.replace('-', ' ').title()} | {title} | [{os.path.basename(relative_path)}](./{relative_path}) | {clean_post} |\n"
    
    with open(INVENTORY_FILE, "a", encoding="utf-8") as f:
        f.write(row)

def extract_title(content):
    """Extract the title from the markdown frontmatter or H1."""
    for line in content.split("\n"):
        if line.startswith("Title:"):
            return line.replace("Title:", "").strip()
        if line.startswith("# "):
            return line.replace("# ", "").strip()
    return "Unknown Title"

def main():
    processed_files = get_processed_files()
    
    print(f"Found {len(processed_files)} already processed files.")
    print("Starting generation...")
    
    # Ensure the table header exists in the inventory if we are starting fresh
    if len(processed_files) == 0:
        with open(INVENTORY_FILE, "a", encoding="utf-8") as f:
            f.write("\n## Bảng Social Media Posts (LinkedIn / X)\n\n")
            f.write("| Tháng | Tiêu đề gốc | Đường dẫn | Bài Social Media (LinkedIn / X Post) |\n")
            f.write("|---|---|---|---|\n")

    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if not os.path.exists(full_dir_path):
            continue
            
        md_files = sorted(glob.glob(os.path.join(full_dir_path, "*.md")))
        
        for file_path in md_files:
            relative_path = f"{month_dir}/{os.path.basename(file_path)}"
            
            if relative_path in processed_files:
                continue # Skip already processed files
                
            print(f"Processing: {relative_path}...")
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            title = extract_title(content)
            
            try:
                # Call Gemini API
                response = model.generate_content(
                    f"{SYSTEM_PROMPT}\n\nHere is the article:\n{content}"
                )
                social_post = response.text
                
                # Append to inventory
                append_to_inventory(month_dir, title, relative_path, social_post)
                
                # Log as processed
                mark_as_processed(relative_path)
                print(f"  -> Success!")
                
                # Sleep to avoid hitting API rate limits
                time.sleep(3) 
                
            except Exception as e:
                print(f"  -> Error processing {relative_path}: {e}")
                print("Waiting 10 seconds before retrying...")
                time.sleep(10)

if __name__ == "__main__":
    main()
