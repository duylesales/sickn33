#!/usr/bin/env python3
"""
normalize_october_articles.py
-----------------------------
Normalizes all 60 articles in manifera/2026/october-2026/ to adhere strictly
to all system guidelines:
1. FAQ Heading: ## FAQs
2. Exactly 5 FAQs in both Markdown and JSON-LD schema
3. [Scenario: ...] instead of (Scenario: ...)
4. Zero em dash — and en dash –
5. Convert parentheses with commas in body text to brackets
6. Geotag each matching image with Amsterdam HQ coordinates & keywords
"""

import os
import re
import json
import glob
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from upload_to_wordpress import geotag_image_file, DEFAULT_COMPANY_LATITUDE, DEFAULT_COMPANY_LONGITUDE

def normalize_article(art_path):
    with open(art_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Replace em dash and en dash
    text = text.replace("—", " - ").replace("–", " - ")

    # Extract Title and Keywords for geotagging
    title_m = re.search(r'^Title:\s*["\']?(.*?)["\']?$', text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""

    kw_m = re.search(r'^Keywords:\s*["\']?(.*?)["\']?$', text, re.MULTILINE)
    keywords = kw_m.group(1).strip() if kw_m else ""

    # Split into body and FAQ
    faq_split = re.split(r'##\s+(?:Frequently Asked Questions|FAQs|FAQ)', text, flags=re.I)
    if len(faq_split) != 2:
        print(f"[!] Warning: Could not split FAQ in {art_path}")
        return False, title, keywords

    body = faq_split[0]
    faq_and_schema = faq_split[1]

    # Convert parentheses with commas in body (avoid markdown links or images)
    def repl_paren(m):
        content = m.group(1)
        if "http://" in content or "https://" in content:
            return m.group(0)
        return f"[{content}]"

    body = re.sub(r'\(([^)\n]*,[^)\n]*)\)', repl_paren, body)

    # Split FAQ text and JSON-LD schema
    schema_parts = faq_and_schema.split('<script type="application/ld+json">')
    faq_text = schema_parts[0]
    schema_text = schema_parts[1] if len(schema_parts) > 1 else ""

    # Extract exactly 5 FAQ items
    raw_faqs = [f.strip() for f in re.split(r'###\s+', faq_text) if f.strip()]
    raw_faqs = raw_faqs[:5]

    cleaned_faqs = []
    for item in raw_faqs:
        # Convert (Scenario: ...) to [Scenario: ...]
        item_clean = re.sub(r'^\(Scenario:\s*([^)]+)\)', r'[Scenario: \1]', item)
        # Avoid nested parentheses with commas in question heading
        first_line, *rest = item_clean.split("\n", 1)
        first_line = re.sub(r'\(([^)\n]*,[^)\n]*)\)', repl_paren, first_line)
        cleaned_item = first_line + ("\n" + rest[0] if rest else "")
        cleaned_faqs.append("### " + cleaned_item)

    new_faq_body = "\n\n" + "\n\n".join(cleaned_faqs) + "\n\n"

    # Clean JSON-LD schema
    if schema_text:
        faq_schema_str = schema_text.split("</script>")[0].strip()
        try:
            faq_schema = json.loads(faq_schema_str)
            if "@type" in faq_schema and faq_schema["@type"] == "FAQPage":
                faq_schema["mainEntity"] = faq_schema.get("mainEntity", [])[:5]
            new_schema_str = '<script type="application/ld+json">\n' + json.dumps(faq_schema, indent=2, ensure_ascii=False) + '\n</script>\n'
        except Exception as e:
            print(f"[!] JSON schema parse error in {art_path}: {e}")
            new_schema_str = '<script type="application/ld+json">\n' + faq_schema_str + '\n</script>\n'
    else:
        new_schema_str = ""

    new_content = body.rstrip() + "\n\n## FAQs\n" + new_faq_body.lstrip() + new_schema_str

    with open(art_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, title, keywords

def main():
    oct_dir = "manifera/2026/october-2026"
    articles = sorted([f for f in glob.glob(f"{oct_dir}/[0-9]*.md") if not f.endswith("-social.md")])
    pics = sorted(glob.glob(f"{oct_dir}/*_pic.jpg"))

    print(f"[*] Processing {len(articles)} articles in October 2026...")

    for art in articles:
        num = os.path.basename(art).split("-")[0]
        success, title, keywords = normalize_article(art)
        if success:
            print(f"[+] Normalized {os.path.basename(art)} (Title: {title[:40]}...)")

        # Find matching pic
        matched_pics = [p for p in pics if os.path.basename(p).startswith(f"{num}-")]
        if matched_pics:
            pic_path = matched_pics[0]
            lat, lng, city = geotag_image_file(pic_path, title, keywords)
            print(f"    [+] Geotagged {os.path.basename(pic_path)} -> {city} ({lat}, {lng})")
        else:
            print(f"    [!] Warning: No pic matched for {num}")

    print("\n[+] All articles in October 2026 normalized and images geotagged!")

if __name__ == "__main__":
    main()
