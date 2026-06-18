import os
import requests
from io import BytesIO
from PIL import Image

# ==========================================
# 🔑 ĐIỀN API KEY CỦA BẠN VÀO ĐÂY
# ==========================================
PEXELS_API_KEY = "dZMenvKPw6yI6j6s0wACheowGhY6w2A3vfXLZCeqp1k1KUGT1c35aXtw"
PIXABAY_API_KEY = "56345592-e67f9aa666cf196cb4ffa4bef"
UNSPLASH_API_KEY = "ĐIỀN_MÃ_API_UNSPLASH_CỦA_BẠN_VÀO_ĐÂY"
FREEPIK_API_KEY = "ĐIỀN_MÃ_API_FREEPIK_CỦA_BẠN_VÀO_ĐÂY"

def crop_to_16_9(img):
    """Tự động crop và resize ảnh về đúng tỷ lệ 16:9 (1600x900)"""
    width, height = img.size
    target_ratio = 16 / 9
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        # Ảnh bị bè ngang -> Cắt bớt chiều ngang
        new_width = int(height * target_ratio)
        left = (width - new_width) / 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        # Ảnh bị cao -> Cắt bớt chiều dọc
        new_height = int(width / target_ratio)
        top = (height - new_height) / 2
        img = img.crop((0, top, width, top + new_height))
        
    img.thumbnail((1600, 900), Image.Resampling.LANCZOS)
    return img.convert("RGB")

def download_from_pexels(query, output_path):
    if not PEXELS_API_KEY or "ĐIỀN" in PEXELS_API_KEY:
        print("Lỗi: Chưa có API Key của Pexels!")
        return False
        
    print(f"[Pexels] Đang tìm kiếm ảnh: '{query}'...")
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    headers = {"Authorization": PEXELS_API_KEY}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("photos"):
            img_url = data["photos"][0]["src"]["original"]
            print(f"[Pexels] Đang tải ảnh từ: {img_url}")
            
            img_resp = requests.get(img_url)
            img = Image.open(BytesIO(img_resp.content))
            img = crop_to_16_9(img)
            img.save(output_path, "JPEG", quality=90)
            print(f"[Pexels] ✅ Tải và cắt ảnh thành công: {output_path}")
            return True
    else:
        print(f"[Pexels] Lỗi API: {response.text}")
    return False

def download_from_pixabay(query, output_path):
    if not PIXABAY_API_KEY or "ĐIỀN" in PIXABAY_API_KEY:
        print("Lỗi: Chưa có API Key của Pixabay!")
        return False
        
    print(f"[Pixabay] Đang tìm kiếm ảnh: '{query}'...")
    # Pixabay yêu cầu khoảng trắng đổi thành dấu +
    formatted_query = query.replace(' ', '+')
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={formatted_query}&image_type=photo&per_page=3"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("hits"):
            img_url = data["hits"][0]["largeImageURL"]
            print(f"[Pixabay] Đang tải ảnh từ: {img_url}")
            
            img_resp = requests.get(img_url)
            img = Image.open(BytesIO(img_resp.content))
            img = crop_to_16_9(img)
            img.save(output_path, "JPEG", quality=90)
            print(f"[Pixabay] ✅ Tải và cắt ảnh thành công: {output_path}")
            return True
    else:
        print(f"[Pixabay] Lỗi API: {response.text}")
    return False

def download_from_unsplash(query, output_path):
    if not UNSPLASH_API_KEY or "ĐIỀN" in UNSPLASH_API_KEY:
        print("Lỗi: Chưa có API Key của Unsplash!")
        return False
        
    print(f"[Unsplash] Đang tìm kiếm ảnh: '{query}'...")
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page=1"
    headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            img_url = data["results"][0]["urls"]["raw"]
            print(f"[Unsplash] Đang tải ảnh từ: {img_url}")
            
            img_resp = requests.get(img_url)
            img = Image.open(BytesIO(img_resp.content))
            img = crop_to_16_9(img)
            img.save(output_path, "JPEG", quality=90)
            print(f"[Unsplash] ✅ Tải và cắt ảnh thành công: {output_path}")
            return True
    else:
        print(f"[Unsplash] Lỗi API: {response.text}")
    return False

def download_from_freepik(query, output_path):
    if not FREEPIK_API_KEY or "ĐIỀN" in FREEPIK_API_KEY:
        print("Lỗi: Chưa có API Key của Freepik!")
        return False
        
    print(f"[Freepik] Đang tìm kiếm ảnh: '{query}'...")
    url = f"https://api.freepik.com/v1/resources?q={query}&limit=1"
    headers = {"x-freepik-api-key": FREEPIK_API_KEY}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("data"):
            img_url = data["data"][0]["image"]["source"]["url"]
            print(f"[Freepik] Đang tải ảnh từ: {img_url}")
            
            img_resp = requests.get(img_url)
            img = Image.open(BytesIO(img_resp.content))
            img = crop_to_16_9(img)
            img.save(output_path, "JPEG", quality=90)
            print(f"[Freepik] ✅ Tải và cắt ảnh thành công: {output_path}")
            return True
    else:
        print(f"[Freepik] Lỗi API: {response.text}")
    return False

if __name__ == "__main__":
    # Thay đổi thông tin tìm kiếm ở đây
    search_keyword = "business people meeting laptop professional"
    output_file = "/Users/duyle/sickn33/manifera/july-2026/01-how-to-scale-software-development-team-thumbnail.jpg"
    
    # Kịch bản sẽ ưu tiên thử Pexels trước, nếu lỗi hoặc không có Key sẽ thử qua Pixabay, Unsplash, Freepik
    if not download_from_pexels(search_keyword, output_file):
        if not download_from_pixabay(search_keyword, output_file):
            if not download_from_unsplash(search_keyword, output_file):
                download_from_freepik(search_keyword, output_file)
