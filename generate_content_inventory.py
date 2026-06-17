import os
import glob
import re

BASE_DIR = "/Users/duyle/sickn33/manifera"
OUTPUT_FILE = os.path.join(BASE_DIR, "content_inventory.md")

MONTHS = [
    "july-2026", "august-2026", "september-2026", 
    "october-2026", "november-2026", "december-2026"
]

def extract_frontmatter_and_summary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    title = ""
    keywords = ""
    buyer_stage = ""
    summary = ""
    
    # Extract Frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm_content = fm_match.group(1)
        
        t_match = re.search(r'^Title:\s*"?([^"\n]+)"?', fm_content, re.MULTILINE)
        if t_match:
            title = t_match.group(1)
            
        k_match = re.search(r'^Keywords:\s*"?([^"\n]+)"?', fm_content, re.MULTILINE)
        if k_match:
            keywords = k_match.group(1)
            
        b_match = re.search(r'^Buyer Stage:\s*"?([^"\n]+)"?', fm_content, re.MULTILINE)
        if b_match:
            buyer_stage = b_match.group(1)
            
    # Extract Summary (first paragraph after title)
    content_without_fm = re.sub(r'^---\n.*?\n---\n*', '', content, flags=re.DOTALL)
    
    # Strip script tags
    content_without_scripts = re.sub(r'<script.*?</script>', '', content_without_fm, flags=re.DOTALL)
    
    # Find first text paragraph
    lines = content_without_scripts.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('<'):
            summary = line[:100] + "..." if len(line) > 100 else line
            break
            
    return title, keywords, buyer_stage, summary

def main():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write("# 📚 Bảng Tổng Hợp Content Manifera (Theo Tháng)\n\n")
        out.write("Danh sách dưới đây liệt kê toàn bộ 360 bài viết đã được tạo tự động, bao gồm thông tin về tiêu đề, từ khóa, giai đoạn mua hàng (Buyer Stage), và tóm tắt nội dung.\n\n")
        
        for month in MONTHS:
            month_dir = os.path.join(BASE_DIR, month)
            if not os.path.exists(month_dir):
                continue
                
            out.write(f"## Tháng: {month.replace('-', ' ').title()}\n\n")
            out.write("| Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn | Tóm lược |\n")
            out.write("|---|---|---|---|\n")
            
            # Get and sort files
            files = glob.glob(os.path.join(month_dir, "*.md"))
            def get_prefix(filename):
                base = os.path.basename(filename)
                match = re.match(r'^(\d+)-', base)
                return int(match.group(1)) if match else 9999
            files.sort(key=get_prefix)
            
            for file_path in files:
                title, keywords, buyer_stage, summary = extract_frontmatter_and_summary(file_path)
                
                # Clean up for markdown table
                title = title.replace('|', '-')
                keywords = keywords.replace('|', '-')
                buyer_stage = buyer_stage.replace('|', '-')
                summary = summary.replace('|', '-')
                
                out.write(f"| {title} | {keywords} | {buyer_stage} | {summary} |\n")
                
            out.write("\n")
            
    print(f"✅ Đã tạo thành công bảng tổng hợp tại: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
