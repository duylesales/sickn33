#!/usr/bin/env python3
"""
batch_upload_september.py
-------------------------
Uploads remaining articles in manifera/2026/september-2026/ (articles 03 to 60)
to WordPress (manifera.com) with full WAF safety, geotagged banners, Yoast SEO,
inventory updating (marking ✅ in column 6 only), and diary logging.
"""

import os
import sys
import re
import glob
import time
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__)))
from upload_to_wordpress import (
    upload_post,
    parse_markdown_article,
    slugify_full_title,
    DEFAULT_COMPANY_LATITUDE,
    DEFAULT_COMPANY_LONGITUDE
)

SEPT_DIR = "manifera/2026/september-2026"
INVENTORY_FILE = "manifera/content_inventory.md"
DIARY_FILE = "manifera/diary.md"

def update_inventory_stt(stt_num):
    if not os.path.isfile(INVENTORY_FILE):
        return False
    with open(INVENTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_sep = False
    updated = False
    for i, line in enumerate(lines):
        if "## Tháng: September 2026" in line:
            in_sep = True
            continue
        if in_sep and line.startswith("## Tháng:"):
            break
        if in_sep and line.strip().startswith("|") and not line.strip().startswith("| STT") and not line.strip().startswith("| ---"):
            parts = line.split("|")
            if len(parts) >= 8:
                try:
                    cur_stt = int(parts[1].strip())
                    if cur_stt == stt_num:
                        # parts[6] is column "Đã Post lên"
                        parts[6] = " ✅             "
                        lines[i] = "|".join(parts)
                        updated = True
                        break
                except ValueError:
                    pass

    if updated:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)
    return updated

def add_diary_entry(stt_num, art_rel, title, slug, post_id, media_id, focus_kw):
    if not os.path.isfile(DIARY_FILE):
        return False
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    entry = f"""
- **Đăng tải bài viết {stt_num:02d} (tháng 9/2026) lên website Manifera qua upload_to_wordpress.py**:
  - **Bài viết**: [`{art_rel}`](./{art_rel})
  - **Tiêu đề**: *{title}*
  - **Slug**: `{slug}`
  - **Pre-flight check**: Kiểm tra slug và tiêu đề với `status=any`. Không trùng lặp trên manifera.com.
  - **Chuẩn hóa nội dung**:
    - Tiêu đề FAQ: Chuẩn hóa `## FAQs`.
    - Số lượng FAQ: Chuẩn hóa đúng 5 FAQs theo quy định hệ thống.
    - Thẻ tình huống FAQ: Chuẩn hóa `[Scenario: ...]` theo quy định hệ thống.
    - Đảm bảo 0 em dash `—` và 0 en dash `–`.
  - **Thao tác kỹ thuật**:
    - Ảnh đại diện: Geotag tọa độ HQ Amsterdam (`52.366841, 4.887593`) kèm Title và Keywords vào metadata EXIF.
    - Upload media qua GitHub Raw URL: Attachment ID `{media_id}`.
    - Tạo bài viết: Post ID `{post_id}`, trạng thái Bản nháp (Draft), tự động gắn tags từ keywords.
    - Yoast SEO: Focus Keyword `{focus_kw}`, Meta Description được đồng bộ đầy đủ.
    - Post Meta: Tọa độ địa lý Amsterdam (`geo_latitude: 52.366841`, `geo_longitude: 4.887593`, `geo_city: Amsterdam`, `geo_address: Herengracht 420, 1017 BZ Amsterdam, Netherlands`).
  - **Trạng thái**: Bản nháp (Draft) tại https://www.manifera.com/?p={post_id}. Đã đánh dấu ✅ ở cột "Đã Post lên" trong `manifera/content_inventory.md`.
"""

    # Insert under the first "#### Ngày 27"
    target = "#### Ngày 27\n"
    if target in content:
        content = content.replace(target, target + entry, 1)
        with open(DIARY_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def git_commit_push(msg):
    try:
        subprocess.run(["git", "add", INVENTORY_FILE, DIARY_FILE], check=True)
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"[+] Git committed and pushed: {msg}")
    except Exception as e:
        print(f"[!] Warning: Git commit/push failed: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--end", type=int, default=60)
    args = parser.parse_args()

    articles = sorted([f for f in glob.glob(f"{SEPT_DIR}/[0-9]*.md") if not f.endswith("-social.md")])
    pics = sorted(glob.glob(f"{SEPT_DIR}/*_pic.jpg"))

    print(f"[*] Starting batch upload for September 2026: Articles {args.start} to {args.end}")

    uploaded_count = 0
    for art in articles:
        num = int(os.path.basename(art).split("-")[0])
        if num < args.start or num > args.end:
            continue

        matched_pics = [p for p in pics if os.path.basename(p).startswith(f"{num:02d}-")]
        pic_path = matched_pics[0] if matched_pics else None

        print(f"\n==================================================")
        print(f"[*] Processing Article #{num:02d}: {os.path.basename(art)}")
        print(f"==================================================")

        meta, _ = parse_markdown_article(art)
        title = meta.get("title", "")
        slug = slugify_full_title(title)
        focus_kw = meta.get("focus_kw", "")

        try:
            res = upload_post(
                article_path=art,
                image_path=pic_path,
                site="manifera",
                status="draft"
            )
            post_id = res.get("id")
            media_id = res.get("featured_media", "")

            print(f"[+] Post successfully uploaded! ID: {post_id}, Media ID: {media_id}")

            # Update inventory and diary
            update_inventory_stt(num)
            art_rel = os.path.relpath(art, os.getcwd()).replace("\\", "/")
            add_diary_entry(num, art_rel, title, slug, post_id, media_id, focus_kw)

            uploaded_count += 1

            # Commit periodically every 5 posts
            if uploaded_count % 5 == 0:
                git_commit_push(f"docs(manifera): record upload progress up to article {num:02d}")

            # Sleep to prevent WAF rate limits
            time.sleep(4)

        except Exception as e:
            if "already exists" in str(e).lower() or "aborting upload" in str(e).lower():
                print(f"[*] Article #{num:02d} already exists on site. Marking inventory...")
                update_inventory_stt(num)
            else:
                print(f"[!] Error uploading article #{num:02d}: {e}")
                time.sleep(8)

    # Final git commit and push
    git_commit_push(f"docs(manifera): complete batch upload for September 2026 (articles {args.start} to {args.end})")
    print(f"\n[+] Batch upload completed! Total newly uploaded: {uploaded_count} articles.")

if __name__ == "__main__":
    main()
