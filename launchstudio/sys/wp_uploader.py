import os
import glob
import json
import base64
import urllib.request
import urllib.error

# ==========================================
# 🛠️ CẤU HÌNH WORDPRESS CỦA BẠN
# ==========================================
WP_URL = "https://yourdomain.com" # Thay bằng URL website WordPress của bạn
WP_USERNAME = "your_username"       # Username tài khoản Admin
WP_APP_PASSWORD = "your_app_password" # WordPress Application Password (KHÔNG PHẢI mật khẩu đăng nhập bình thường)
# Xem cách tạo App Password tại: https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/

# Trạng thái bài đăng: 'publish' (đăng ngay), 'draft' (lưu nháp), 'private'
POST_STATUS = "draft" 

# ==========================================

API_URL = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts"
CREDENTIALS = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
TOKEN = base64.b64encode(CREDENTIALS.encode()).decode('utf-8')

def extract_frontmatter(content):
    """Trích xuất Front Matter và trả về metadata cùng phần nội dung chính."""
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return {}, content

    metadata = {}
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
        if ':' in lines[i]:
            key, val = lines[i].split(':', 1)
            metadata[key.strip()] = val.strip().strip('"').strip("'")
            
    if end_idx == -1:
        return {}, content
        
    main_content = '\n'.join(lines[end_idx+1:]).strip()
    return metadata, main_content

def markdown_to_html_basic(text):
    """
    Chuyển đổi Markdown cơ bản sang HTML để WordPress hiển thị tốt hơn.
    Lưu ý: WordPress Gutenberg tự động xử lý nhiều Markdown, nhưng HTML sẽ an toàn hơn.
    (Trong môi trường thực tế, có thể cài thư viện 'markdown' của python: pip install markdown)
    Ở đây dùng một bộ parse siêu cơ bản.
    """
    try:
        import markdown
        return markdown.markdown(text)
    except ImportError:
        # Nếu chưa cài thư viện markdown, trả về raw text bọc trong pre/code hoặc xử lý cơ bản
        # Khuyên dùng: pip install markdown
        print("💡 Gợi ý: Chạy `pip install markdown` để nội dung format đẹp hơn.")
        # Xử lý cơ bản ngắt dòng
        html = ""
        for p in text.split('\n\n'):
            if p.startswith('#'):
                # Bỏ qua xử lý header phức tạp, để nguyên Markdown vì WP đôi khi tự parse
                html += f"<p>{p}</p>\n"
            else:
                html += f"<p>{p}</p>\n"
        return html

def create_wp_post(title, content, tags_text=""):
    """Gửi HTTP POST request tới WordPress REST API."""
    
    # Chuẩn bị dữ liệu
    post_data = {
        "title": title,
        "content": content,
        "status": POST_STATUS,
        # Nếu muốn thêm custom fields/meta data (như Buyer Stage), bạn có thể cấu hình meta parameters ở đây.
    }
    
    data = json.dumps(post_data).encode('utf-8')
    
    req = urllib.request.Request(API_URL, data=data)
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Basic {TOKEN}")
    
    try:
        response = urllib.request.urlopen(req)
        resp_data = json.loads(response.read().decode('utf-8'))
        return True, resp_data.get('id'), resp_data.get('link')
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        return False, e.code, err_msg
    except Exception as e:
        return False, "Error", str(e)

def process_directory(base_dir):
    """Duyệt qua tất cả các thư mục tháng và up bài lên WordPress."""
    md_files = glob.glob(os.path.join(base_dir, '**/*.md'), recursive=True)
    print(f"🔍 Tìm thấy {len(md_files)} file Markdown.")
    
    success_count = 0
    fail_count = 0
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            meta, md_content = extract_frontmatter(content)
            
            # Ưu tiên lấy Title từ Front Matter, nếu không có thì lấy tên file
            title = meta.get('Title', os.path.basename(file_path).replace('.md', '').replace('-', ' ').title())
            keywords = meta.get('Keywords', '')
            buyer_stage = meta.get('Buyer Stage', '')
            
            # Chuyển đổi Markdown sang HTML
            html_content = markdown_to_html_basic(md_content)
            
            # Nếu có Buyer Stage, nối vào đầu/cuối content như một tag ẩn hoặc block
            if buyer_stage:
                html_content += f'<p style="display:none;" data-buyer-stage="{buyer_stage}"></p>'
            
            print(f"⏳ Đang tải lên: {title}...", end=" ")
            
            success, post_id, info = create_wp_post(title, html_content, keywords)
            
            if success:
                print(f"✅ Thành công! (ID: {post_id})")
                success_count += 1
            else:
                print(f"❌ Lỗi: {info}")
                fail_count += 1
                
        except Exception as e:
            print(f"❌ Lỗi xử lý file {file_path}: {e}")
            fail_count += 1
            
    print("\n" + "="*40)
    print("🎉 KẾT QUẢ ĐĂNG BÀI")
    print(f"✅ Thành công: {success_count}/{len(md_files)}")
    print(f"❌ Thất bại: {fail_count}/{len(md_files)}")
    print("="*40)

if __name__ == "__main__":
    import sys
    # Chỉ định thư mục gốc chứa các tháng (july-2026, august-2026,...)
    target_dir = "/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/sickn33/launchstudio"
    
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        
    print("🚀 BẮT ĐẦU PUSH BÀI LÊN WORDPRESS")
    print("⚠️ Lưu ý: Đảm bảo bạn đã thay đổi WP_URL, WP_USERNAME và WP_APP_PASSWORD trong file script!")
    
    process_directory(target_dir)
