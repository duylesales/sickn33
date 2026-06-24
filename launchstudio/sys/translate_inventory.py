import os
import time
from deep_translator import GoogleTranslator

# Input and output file
filepath = 'content_inventory.md'
output_filepath = 'content_inventory.md'

# Cache to avoid redundant API calls
translation_cache = {}

translator = GoogleTranslator(source='auto', target='nl')

def translate_text(text):
    text = text.strip()
    if not text:
        return text
    if text in translation_cache:
        return translation_cache[text]
    
    try:
        translated = translator.translate(text)
        translation_cache[text] = translated
        # small delay to prevent rate limit
        time.sleep(0.1)
        return translated
    except Exception as e:
        print(f"Error translating '{text[:20]}...': {e}")
        time.sleep(2) # longer delay if rate limited
        try:
            translated = translator.translate(text)
            translation_cache[text] = translated
            return translated
        except:
            return text # fallback to original

def process_file():
    print("Reading file...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    
    in_table = False
    
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and 'Tiêu đề' in line:
            # Header row
            # Original: | No. | Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn | Bài viết | Tóm lược | Ước tính views/tháng | Bài Social Media |
            new_lines.append("| No. | Tiêu đề (Title) | Tiêu đề (Title) - Dutch | Từ khóa (Keywords) | Từ khóa (Keywords) - Dutch | Giai đoạn | Giai đoạn - Dutch | Bài viết | Tóm lược | Tóm lược - Dutch | Ước tính views/tháng | Bài Social Media |\n")
            in_table = True
            continue
            
        if in_table and line.strip().startswith('|---'):
            # Separator row
            new_lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|\n")
            continue
            
        if in_table and line.strip().startswith('|'):
            # Data row
            parts = line.strip('\n').split('|')
            # parts has empty first and last elements because of leading/trailing |
            # e.g., ['', ' 1 ', ' Title ', ' Keywords ', ' Stage ', ' Article ', ' Summary ', ' Views ', ' Social ', '']
            if len(parts) >= 9:
                no = parts[1]
                title = parts[2]
                keywords = parts[3]
                stage = parts[4]
                article = parts[5]
                summary = parts[6]
                views = parts[7]
                social = parts[8]
                
                print(f"Translating row {no.strip()}...")
                title_nl = translate_text(title)
                keywords_nl = translate_text(keywords)
                stage_nl = translate_text(stage)
                summary_nl = translate_text(summary)
                
                new_row = f"|{no}|{title}| {title_nl} |{keywords}| {keywords_nl} |{stage}| {stage_nl} |{article}|{summary}| {summary_nl} |{views}|{social}|\n"
                new_lines.append(new_row)
            else:
                new_lines.append(line)
        else:
            in_table = False
            new_lines.append(line)
            
    print("Writing updated file...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print("Done!")

if __name__ == "__main__":
    process_file()
