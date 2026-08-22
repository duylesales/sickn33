import sys
import os
from PIL import Image

def crop_and_resize(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            print(f"Error: Input file {input_path} does not exist.")
            return False
            
        img = Image.open(input_path)
        width, height = img.size
        target_ratio = 16 / 9
        current_ratio = width / height
        
        if current_ratio > target_ratio:
            # Too wide -> crop horizontal sides
            new_width = int(height * target_ratio)
            left = (width - new_width) // 2
            img = img.crop((left, 0, left + new_width, height))
        else:
            # Too tall -> crop vertical sides (takes middle part)
            new_height = int(width / target_ratio)
            top = (height - new_height) // 2
            img = img.crop((0, top, width, top + new_height))
            
        # Resize to exactly 1365x768
        img = img.resize((1365, 768), Image.Resampling.LANCZOS)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save as JPEG with high quality
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=95)
        print(f"Successfully cropped, resized, and saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python crop_to_16_9.py <input_path> <output_path>")
        sys.exit(1)
    crop_and_resize(sys.argv[1], sys.argv[2])
