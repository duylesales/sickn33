import os
import time
import re
from deep_translator import GoogleTranslator

# Config
inventory_file = 'content_inventory.md'
translator = GoogleTranslator(source='auto', target='nl')

def chunk_text(text, max_length=4000):
    """Split text into chunks by double newline (paragraphs) without exceeding max_length."""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 > max_length:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = p
        else:
            if current_chunk:
                current_chunk += "\n\n" + p
            else:
                current_chunk = p
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def translate_file(filepath):
    """Read a markdown file, translate it in chunks, and save as _dutch.md"""
    print(f"  -> Translating file: {filepath}")
    
    # If the file doesn't exist, skip
    if not os.path.exists(filepath):
        print(f"     [ERROR] File {filepath} not found.")
        return None
        
    base, ext = os.path.splitext(filepath)
    output_filepath = f"{base}_dutch{ext}"
    
    # Check if already translated (resume capability)
    if os.path.exists(output_filepath):
        print(f"     [SKIP] {output_filepath} already exists.")
        return output_filepath

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    chunks = chunk_text(text)
    translated_chunks = []
    
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue
        try:
            translated = translator.translate(chunk)
            translated_chunks.append(translated)
            time.sleep(0.5) # Prevent rate limit
        except Exception as e:
            print(f"     [ERROR] Translating chunk {i}: {e}")
            time.sleep(5) # Wait longer and retry once
            try:
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
            except Exception as e2:
                print(f"     [FATAL] Failed chunk {i}: {e2}")
                translated_chunks.append(chunk) # Fallback to original
                
    translated_text = "\n\n".join(translated_chunks)
    
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(translated_text)
        
    print(f"     [SUCCESS] Saved to {output_filepath}")
    return output_filepath

def update_inventory():
    print("Reading inventory...")
    with open(inventory_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and 'Tiêu đề' in line:
            # Header row
            new_lines.append("| No. | Tiêu đề (Title) | Tiêu đề (Title) - Dutch | Từ khóa (Keywords) | Từ khóa (Keywords) - Dutch | Giai đoạn | Giai đoạn - Dutch | Bài viết | Bài viết - Dutch | Tóm lược | Tóm lược - Dutch | Ước tính views/tháng | Bài Social Media | Bài Social Media - Dutch |\n")
            in_table = True
            continue
            
        if in_table and line.strip().startswith('|---'):
            # Separator row
            new_lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
            continue
            
        if in_table and line.strip().startswith('|'):
            # Data row
            parts = line.strip('\n').split('|')
            if len(parts) == 14: # 12 columns
                no = parts[1]
                article_cell = parts[8].strip()
                social_cell = parts[12].strip()
                summary_cell = parts[9]
                summary_d_cell = parts[10]
                views_cell = parts[11]
                article_raw = parts[8]
                social_raw = parts[12]
            elif len(parts) == 16: # 14 columns
                no = parts[1]
                article_cell = parts[8].strip()
                social_cell = parts[13].strip()
                summary_cell = parts[10]
                summary_d_cell = parts[11]
                views_cell = parts[12]
                article_raw = parts[8]
                social_raw = parts[13]
            else:
                new_lines.append(line)
                continue
                
            article_match = re.search(r'\[(.*?)\]\((.*?)\)', article_cell)
            social_match = re.search(r'\[(.*?)\]\((.*?)\)', social_cell)
            
            article_dutch_cell = parts[9].strip() if len(parts) == 16 else " "
            social_dutch_cell = parts[14].strip() if len(parts) == 16 else " "
            
            print(f"\nProcessing row {no.strip()}...")
            
            if article_match:
                article_text = article_match.group(1)
                article_link = article_match.group(2)
                translated_path = translate_file(article_link)
                if translated_path:
                    base, ext = os.path.splitext(article_text)
                    article_dutch_cell = f"[{base}_dutch{ext}]({translated_path})"
                    
            if social_match:
                social_text = social_match.group(1)
                social_link = social_match.group(2)
                translated_path = translate_file(social_link)
                if translated_path:
                    base, ext = os.path.splitext(social_text)
                    social_dutch_cell = f"[{base}_dutch{ext}]({translated_path})"
                    
            new_row = f"|{parts[1]}|{parts[2]}|{parts[3]}|{parts[4]}|{parts[5]}|{parts[6]}|{parts[7]}|{article_raw}| {article_dutch_cell} |{summary_cell}|{summary_d_cell}|{views_cell}|{social_raw}| {social_dutch_cell} |\n"
            
            # Escape $ signs to prevent markdown table rendering issues
            new_row = new_row.replace('$', '\\$').replace('\\\\$', '\\$')
            
            new_lines.append(new_row)
            
            # Periodically save inventory so progress is not lost if script terminates
            if int(no.strip()) % 5 == 0:
                with open(inventory_file, 'w', encoding='utf-8') as temp_f:
                    temp_f.writelines(new_lines + lines[i+1:])
                    
        else:
            in_table = False
            new_lines.append(line)
            
    print("\nWriting updated inventory...")
    with open(inventory_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print("Done!")

if __name__ == "__main__":
    update_inventory()
