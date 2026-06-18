import os
import requests
from io import BytesIO
from PIL import Image
from duckduckgo_search import DDGS

def get_thumbnail(query, output_path):
    print(f"Searching images for: {query}")
    results = DDGS().images(query, max_results=10)
    
    for result in results:
        img_url = result['image']
        print(f"Trying to download: {img_url}")
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
            response = requests.get(img_url, headers=headers, timeout=10)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                
                # Check resolution - skip tiny images
                width, height = img.size
                if width < 800 or height < 450:
                    print(f"Skipping {img_url} (too small: {width}x{height})")
                    continue
                
                # Crop to 16:9
                target_ratio = 16 / 9
                current_ratio = width / height
                
                if current_ratio > target_ratio:
                    # Too wide
                    new_width = int(height * target_ratio)
                    left = (width - new_width) / 2
                    img = img.crop((left, 0, left + new_width, height))
                else:
                    # Too tall
                    new_height = int(width / target_ratio)
                    top = (height - new_height) / 2
                    img = img.crop((0, top, width, top + new_height))
                
                # Resize nicely to a standard 16:9 resolution like 1280x720 if it's large enough
                img.thumbnail((1280, 720), Image.Resampling.LANCZOS)
                
                img = img.convert("RGB")
                img.save(output_path, "JPEG", quality=90)
                print(f"Success! Saved cropped 16:9 thumbnail to {output_path}")
                return True
        except Exception as e:
            print(f"Failed to download or process {img_url}: {e}")
            
    print("Could not find or download a valid image.")
    return False

if __name__ == "__main__":
    output_file = "/Users/duyle/sickn33/manifera/july-2026/01-how-to-scale-software-development-team-thumbnail.jpg"
    success = get_thumbnail("modern software development team office collaboration tech startup stock photo high quality", output_file)
    if success:
        print("DONE")
