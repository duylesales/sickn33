import os
import glob
import re

BASE_DIR = "/Users/duyle/sickn33/launchstudio"
MONTH_DIRS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026", "january-2027"
]

def format_post(content):
    content = content.strip()
    
    # If it already has multiple line breaks, skip it
    if content.count('\n\n') >= 2:
        return content
        
    # Script format
    if " | " in content:
        parts = content.split(" | ", 1)
        hook = parts[0]
        rest = parts[1]
        
        cta_index = rest.rfind("Discover more strategies")
        if cta_index != -1:
            snippet = rest[:cta_index].strip()
            cta_and_tags = rest[cta_index:].strip()
            
            tag_index = cta_and_tags.rfind("[Link]")
            if tag_index != -1:
                cta = cta_and_tags[:tag_index + 6].strip()
                tags = cta_and_tags[tag_index + 6:].strip()
                
                # Split snippet sentences
                snippet = snippet.replace(". ", ".\n\n")
                
                return f"{hook}\n\n{snippet}\n\n{cta}\n\n{tags}"
                
    # LLM format
    else:
        # Extract tags
        tag_match = re.search(r'(#\w+(?:\s+#\w+)*)$', content)
        tags = ""
        if tag_match:
            tags = tag_match.group(1).strip()
            content = content[:tag_match.start()].strip()
            
        # Extract CTA ending in [Link]
        # Match from the last sentence that contains [Link]
        cta_match = re.search(r'([^\.\!\?]+\[Link\])$', content)
        cta = ""
        if cta_match:
            cta = cta_match.group(1).strip()
            content = content[:cta_match.start()].strip()
            
        # Break remaining content into sentences
        sentences = []
        # split by punctuation keeping the punctuation
        raw_sentences = re.split(r'(?<=[.!?])\s+', content)
        for s in raw_sentences:
            if s.strip():
                sentences.append(s.strip())
                
        result = ""
        if sentences:
            result = sentences[0] # Hook
            if len(sentences) > 1:
                result += "\n\n" + "\n\n".join(sentences[1:])
        else:
            result = content
            
        if cta:
            result += f"\n\n{cta}"
        if tags:
            result += f"\n\n{tags}"
            
        return result

    return content

def main():
    count = 0
    for month_dir in MONTH_DIRS:
        full_dir_path = os.path.join(BASE_DIR, month_dir)
        if os.path.exists(full_dir_path):
            social_files = glob.glob(os.path.join(full_dir_path, "*-social.md"))
            for file_path in social_files:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = format_post(content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content + "\n")
                    count += 1

    print(f"Successfully formatted {count} social post files.")

if __name__ == "__main__":
    main()
