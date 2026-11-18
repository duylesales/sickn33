#!/usr/bin/env python3
"""
upload_to_wordpress.py
----------------------
Standardized, WAF-safe WordPress upload utility for Manifera & LaunchStudio.
Automatically parses markdown articles, cleans/sanitizes HTML to avoid WAF blocks,
uploads featured images, auto-refreshes OAuth tokens, configures Yoast SEO metadata,
and creates/updates draft posts.
"""

import os
import sys
import re
import json
import html
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Token configuration path
TOKENS_FILE = os.path.expanduser("~/.gemini/antigravity/mcp_oauth_tokens.json")

SITE_ENDPOINTS = {
    "manifera": "https://www.manifera.com/wp-json/easy-mcp-ai/v1/mcp",
    "launchstudio": "https://launchstudio.eu/wp-json/easy-mcp-ai/v1/mcp"
}

# Default Company Geolocation (Shared by Manifera & LaunchStudio HQ)
DEFAULT_COMPANY_LATITUDE = 52.366841
DEFAULT_COMPANY_LONGITUDE = 4.887593
DEFAULT_COMPANY_CITY = "Amsterdam"
DEFAULT_COMPANY_ADDRESS = "Herengracht 420, 1017 BZ Amsterdam, Netherlands"

DUTCH_CITIES_COORDS = {
    "alkmaar": (52.6324, 4.7534),
    "amsterdam": (52.366841, 4.887593),
    "haarlem": (52.3874, 4.6462),
    "zaanstad": (52.4420, 4.8292),
    "hilversum": (52.2292, 5.1669),
    "rotterdam": (51.9244, 4.4777),
    "den haag": (52.0705, 4.3007),
    "the hague": (52.0705, 4.3007),
    "leiden": (52.1601, 4.4970),
    "delft": (52.0116, 4.3571),
    "dordrecht": (51.8133, 4.6901),
    "utrecht": (52.0907, 5.1214),
    "amersfoort": (52.1561, 5.3878),
    "nieuwegein": (52.0292, 5.0805),
    "veenendaal": (52.0256, 5.5556),
    "zeist": (52.0917, 5.2333),
    "nijmegen": (51.8426, 5.8596),
    "arnhem": (51.9851, 5.8987),
    "apeldoorn": (52.2112, 5.9699),
    "ede": (52.0442, 5.6667),
    "doetinchem": (51.9650, 6.2883),
    "eindhoven": (51.4416, 5.4697),
    "tilburg": (51.5555, 5.0913),
    "breda": (51.5719, 4.7683),
    "den bosch": (51.6978, 5.3037),
    "'s-hertogenbosch": (51.6978, 5.3037),
    "helmond": (51.4817, 5.6611),
    "maastricht": (50.8514, 5.6910),
    "venlo": (51.3700, 6.1724),
    "sittard": (50.9983, 5.8697),
    "sittard-geleen": (50.9983, 5.8697),
    "heerlen": (50.8882, 5.9795),
    "roermond": (51.1942, 5.9875),
    "enschede": (52.2215, 6.8937),
    "zwolle": (52.5168, 6.0830),
    "deventer": (52.2550, 6.1625),
    "almelo": (52.3567, 6.6625),
    "hengelo": (52.2658, 6.7931),
    "almere": (52.3508, 5.2647),
    "lelystad": (52.5185, 5.4714),
    "dronten": (52.5250, 5.7194),
    "zeewolde": (52.3306, 5.5417),
    "emmeloord": (52.7108, 5.7486),
    "groningen": (53.2194, 6.5665),
    "veendam": (53.1067, 6.8744),
    "winschoten": (53.1433, 7.0347),
    "delfzijl": (53.3347, 6.9242),
    "hoogezand": (53.1611, 6.7583),
    "leeuwarden": (53.2012, 5.7999),
    "sneek": (53.0333, 5.6600),
    "drachten": (53.1058, 6.0983),
    "heerenveen": (52.9569, 5.9256),
    "harlingen": (53.1742, 5.4267),
    "assen": (52.9967, 6.5625),
    "emmen": (52.7792, 6.9069),
    "hoogeveen": (52.7283, 6.4764),
    "meppel": (52.6958, 6.1944),
    "coevorden": (52.6617, 6.7417),
    "middelburg": (51.4988, 3.6103),
    "vlissingen": (51.4425, 3.5736),
    "goes": (51.5042, 3.8889),
    "terneuzen": (51.3303, 3.8272),
    "zierikzee": (51.6497, 3.9167)
}

def deg_to_dms(deg):
    d = int(deg)
    m = int((deg - d) * 60)
    s = round((deg - d - m/60) * 3600, 4)
    return (d, m, s)

def geotag_image_file(image_path, title, keywords_str, target_city=None):
    """
    Embeds GPS coordinates, Keywords, Title, and Description into EXIF & PNG metadata
    using Pillow. Defaults to Amsterdam HQ (52.366841, 4.887593) unless a specific
    city is detected or passed.
    """
    if not image_path or not os.path.isfile(image_path):
        return DEFAULT_COMPANY_LATITUDE, DEFAULT_COMPANY_LONGITUDE, DEFAULT_COMPANY_CITY

    try:
        from PIL import Image, ExifTags
        from PIL.PngImagePlugin import PngInfo
    except ImportError:
        print("[!] Pillow (PIL) not available, skipping local image geotagging.")
        return DEFAULT_COMPANY_LATITUDE, DEFAULT_COMPANY_LONGITUDE, DEFAULT_COMPANY_CITY

    lat = DEFAULT_COMPANY_LATITUDE
    lng = DEFAULT_COMPANY_LONGITUDE
    city = DEFAULT_COMPANY_CITY

    search_text = f"{target_city or ''} {title} {keywords_str} {os.path.basename(image_path)}".lower()
    for c_name, (c_lat, c_lng) in DUTCH_CITIES_COORDS.items():
        if re.search(r"\b" + re.escape(c_name) + r"\b", search_text):
            lat = c_lat
            lng = c_lng
            city = c_name.title()
            break

    try:
        img = Image.open(image_path)
        ext = os.path.splitext(image_path)[1].lower()
        lat_dms = deg_to_dms(lat)
        lng_dms = deg_to_dms(lng)

        exif = img.getexif()
        exif[0x010E] = f"{title} - {city}, Netherlands"
        if keywords_str:
            exif[0x9c9e] = keywords_str.replace(", ", "; ").encode("utf-16le")
        exif[0x9c9b] = title.encode("utf-16le")

        gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
        gps_ifd[1] = "N" if lat >= 0 else "S"
        gps_ifd[2] = lat_dms
        gps_ifd[3] = "E" if lng >= 0 else "W"
        gps_ifd[4] = lng_dms

        if ext == ".png":
            png_info = PngInfo()
            png_info.add_text("Title", title)
            png_info.add_text("Description", f"{title} - {city}, Netherlands")
            if keywords_str:
                png_info.add_text("Keywords", keywords_str)
            png_info.add_text("Location", f"{city}, Netherlands")
            png_info.add_text("GPSLatitude", f"{lat} N")
            png_info.add_text("GPSLongitude", f"{lng} E")
            png_info.add_text("Author", "LaunchStudio / Manifera")
            png_info.add_text("Copyright", "LaunchStudio / Manifera")
            img.save(image_path, format="PNG", exif=exif, pnginfo=png_info)
        elif ext in [".jpg", ".jpeg"]:
            img.save(image_path, format="JPEG", exif=exif, quality=95)

        print(f"[+] Successfully geotagged image {os.path.basename(image_path)} -> {city} ({lat}, {lng})")
        return lat, lng, city
    except Exception as e:
        print(f"[!] Warning: Could not geotag image: {e}")
        return lat, lng, city

def get_auth_token(site_key="manifera"):
    endpoint = SITE_ENDPOINTS.get(site_key, site_key)
    if not os.path.exists(TOKENS_FILE):
        raise FileNotFoundError(f"MCP tokens file not found: {TOKENS_FILE}")
    with open(TOKENS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if endpoint not in data:
        raise KeyError(f"Endpoint {endpoint} not found in {TOKENS_FILE}")
    return data[endpoint]["token"]["access_token"], endpoint

def refresh_oauth_token(site_key="manifera"):
    endpoint = SITE_ENDPOINTS.get(site_key, site_key)
    with open(TOKENS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if endpoint not in data:
        raise KeyError(f"Endpoint {endpoint} not found in {TOKENS_FILE}")

    entry = data[endpoint]
    refresh_token = entry.get("token", {}).get("refresh_token")
    client_id = entry.get("client_id")
    token_url = entry.get("token_url")

    if not refresh_token or not token_url:
        raise RuntimeError("No refresh token or token_url available.")

    req_data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id
    }
    import subprocess
    cmd = [
        "curl", "-s", "-X", "POST",
        token_url,
        "-H", "Content-Type: application/json",
        "-d", json.dumps(req_data)
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    new_token_data = json.loads(proc.stdout)
    new_access = new_token_data.get("access_token", new_token_data.get("token"))
    entry["token"]["access_token"] = new_access
    if "refresh_token" in new_token_data:
        entry["token"]["refresh_token"] = new_token_data["refresh_token"]
    with open(TOKENS_FILE, "w", encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=2)
    print("[+] OAuth token successfully refreshed!")
    return new_access

def call_mcp(endpoint, token, tool_name, arguments, site_key="manifera"):
    req_data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    import subprocess
    cmd = [
        "curl", "-s",
        "-w", "\n%{http_code}",
        endpoint,
        "-H", f"Authorization: Bearer {token}",
        "-H", "Content-Type: application/json",
        "--data-binary", "@-"
    ]
    proc = subprocess.run(cmd, input=json.dumps(req_data), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Curl failed with code {proc.returncode}: {proc.stderr}")

    out_lines = proc.stdout.strip().split("\n")
    http_code = 0
    if out_lines:
        try:
            http_code = int(out_lines[-1])
            body = "\n".join(out_lines[:-1])
        except ValueError:
            body = proc.stdout

    if http_code == 401 or "401" in proc.stdout or "Unauthorized" in proc.stdout or "invalid_token" in proc.stdout:
        print("[!] Token expired (401). Refreshing token and retrying...")
        new_token = refresh_oauth_token(site_key)
        return call_mcp(endpoint, new_token, tool_name, arguments, site_key)

    try:
        res = json.loads(body)
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON response from MCP (HTTP {http_code}): {body[:300]}")

    if "error" in res:
        err = res["error"]
        if isinstance(err, dict) and err.get("code") in [401, -32001]:
            print("[!] Token error. Refreshing token and retrying...")
            new_token = refresh_oauth_token(site_key)
            return call_mcp(endpoint, new_token, tool_name, arguments, site_key)
        raise RuntimeError(f"MCP Error: {res['error']}")

    content_items = res.get("result", {}).get("content", [])
    if content_items and content_items[0].get("type") == "text":
        try:
            return json.loads(content_items[0]["text"])
        except json.JSONDecodeError:
            return content_items[0]["text"]
    return res.get("result", {})

def parse_markdown_article(md_text):
    meta = {}
    content = md_text

    # Extract frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", md_text, re.DOTALL)
    if fm_match:
        fm_lines = fm_match.group(1).split("\n")
        content = fm_match.group(2)
        for line in fm_lines:
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")

    # Extract description from JSON-LD inside article if not in frontmatter
    desc_match = re.search(r'"description":\s*"([^"]+)"', md_text)
    if desc_match and "description" not in meta:
        meta["description"] = desc_match.group(1)

    # Extract first H1 as title if not in frontmatter
    if "title" not in meta:
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if h1_match:
            meta["title"] = h1_match.group(1).strip()

    # Remove H1 and any raw <script> or <style> tags from content
    content = re.sub(r"^#\s+.*$\n*", "", content, flags=re.MULTILINE)
    content = re.sub(r"<script.*?</script>", "", content, flags=re.DOTALL)
    content = re.sub(r"<style.*?</style>", "", content, flags=re.DOTALL)

    return meta, content.strip()

def sanitize_waf_patterns(text):
    """
    Sanitizes common textual patterns that trigger ModSecurity / WAF false positives.
    Guarantees markdown links, code blocks, and inline code are protected.
    """
    # 1. No em dash rule
    text = text.replace("—", " - ")

    # 2. Normalize scenario tags in FAQ: change (Scenario: ...) to [Scenario: ...]
    text = re.sub(r"\(\s*Scenario:\s*([^)]+)\)", r"[Scenario: \1]", text)

    # 3. Prevent form injection signature & multi-item lists inside parentheses
    text = text.replace("basic forms, no real-time features", "simple inputs, static workflows")
    text = text.replace("without real-time features", "static content only")
    text = text.replace("no real-time features or payment processing", "static content and no payment gateways")
    text = text.replace("no real-time features", "static content and basic workflows")
    text = text.replace("no real-time", "static content")
    text = text.replace("basic forms", "simple inputs")

    # 4. Prevent system/time attack signature in tables & paragraphs
    text = text.replace("Real-time sync", "Instant data sync")
    text = text.replace("real-time sync", "instant data sync")
    text = text.replace("real-time backend", "cloud backend")
    text = re.sub(r"\breal[\s\-]time\b", "instant", text, flags=re.IGNORECASE)
    text = re.sub(r"\breal\s+time\b", "actual hours", text, flags=re.IGNORECASE)
    # 'by the time' triggers Blind SQLi / time-based injection regex (BY ... TIME)
    text = re.sub(r"\bby\s+the\s+time\b", "when", text, flags=re.IGNORECASE)
    text = text.replace('"save time"', "accelerate delivery")
    text = text.replace("pay for that time later", "pay for that shortcut later")

    # 5. Prevent contraction SQLi pattern in headings and body
    text = re.sub(r"\bwhat's\b", "what is", text, flags=re.IGNORECASE)

    # 6. Replace multi-argument parentheses containing commas with brackets to avoid SQL function regex
    # Protect URLs inside markdown links [text](url) first so paren_to_brackets cannot mangle URLs
    links_protected = []
    def link_protect_repl(m):
        idx = len(links_protected)
        links_protected.append(m.group(0))
        return f"__LINK_PROTECTED_{idx}__"
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_protect_repl, text)

    # Protect Cost & Timeline parentheses from being converted to brackets
    cost_protected = []
    def cost_protect_repl(m):
        idx = len(cost_protected)
        cost_protected.append(m.group(0))
        return f"__COST_PROTECTED_{idx}__"
    text = re.sub(r"\*\*(?:Cost & Timeline|Kosten & Doorlooptijd):\*\*[^\n]+", cost_protect_repl, text, flags=re.IGNORECASE)

    def paren_to_brackets(match):
        inner = match.group(1)
        if "," in inner:
            return f"[{inner}]"
        return match.group(0)
    text = re.sub(r"\(([^()]{10,})\)", paren_to_brackets, text)

    # Restore protected Cost & Timeline
    for idx, cp in enumerate(cost_protected):
        text = text.replace(f"__COST_PROTECTED_{idx}__", cp)

    # Restore protected links
    for idx, lk in enumerate(links_protected):
        text = text.replace(f"__LINK_PROTECTED_{idx}__", lk)

    return text

def markdown_to_clean_html(content, site="manifera"):
    # 1. Protect fenced code blocks first
    code_blocks = []
    def code_block_repl(m):
        idx = len(code_blocks)
        lang = m.group(1) or ""
        code = m.group(2)
        escaped_code = html.escape(code)
        code_html = (
            f'<pre style="background: #2d3748; color: #f7fafc; padding: 16px; border-radius: 6px; '
            f'overflow-x: auto; font-family: monospace; font-size: 0.9em; line-height: 1.5; margin: 20px 0;">'
            f'<code>{escaped_code}</code></pre>'
        )
        code_blocks.append(code_html)
        return f"\n\n__CODE_BLOCK_PLACEHOLDER_{idx}__\n\n"

    content = re.sub(r"```([a-zA-Z0-9_-]*)\n(.*?)\n```", code_block_repl, content, flags=re.DOTALL)

    # 2. Sanitize WAF patterns on content outside code blocks
    content = sanitize_waf_patterns(content)

    # 3. Normalize headings followed directly by text without a blank line
    content = re.sub(r"(^|\n)(#{1,6}\s+[^\n]+)\n([^\n#\s])", r"\1\2\n\n\3", content)

    # 4. Helper for formatting inline elements (inline code, links, bold, italics, sanitizing tags)
    def format_inline(text):
        if not text:
            return ""

        # Inline code: `code`
        code_spans = []
        def inline_code_repl(m):
            idx = len(code_spans)
            code_text = html.escape(m.group(1))
            code_html = (
                f'<code style="background-color: #f1f1f1; padding: 2px 6px; border-radius: 4px; '
                f'font-family: monospace; font-size: 0.9em; color: #c7254e;">{code_text}</code>'
            )
            code_spans.append(code_html)
            return f"__INLINE_CODE_{idx}__"

        text = re.sub(r"`([^`]+)`", inline_code_repl, text)

        # Markdown links: [text](url)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

        # Bold: **text**
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)

        # Italics: *text* (negative lookbehind/lookahead to avoid matching inside bold)
        text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

        # Sanitize unknown XML/HTML tags (like <View>, <TouchableOpacity>) that are outside code
        allowed_tags = r"(?:/?(?:a|strong|em|code|p|ul|ol|li|blockquote|footer|table|thead|tbody|tr|th|td|div|details|summary|h2|h3|h4|pre|hr|span|br)(?:\s+[^>]*?)?>)"
        def tag_repl(m):
            full = m.group(0)
            if re.match(r"^<" + allowed_tags + r"$", full):
                return full
            return html.escape(full)
        text = re.sub(r"<[^>]+>", tag_repl, text)

        # Restore inline code spans
        for idx, span in enumerate(code_spans):
            text = text.replace(f"__INLINE_CODE_{idx}__", span)

        return text

    # Split into body and FAQ section
    faq_split = re.split(r"(?:##|###)\s+(?:Frequently Asked Questions|FAQs|FAQ|Veelgestelde [Vv]ragen)", content, flags=re.IGNORECASE)
    body_md = faq_split[0]
    faq_md = faq_split[1] if len(faq_split) > 1 else ""

    html_parts = []

    # Process Body Blocks
    paragraphs = body_md.strip().split("\n\n")
    in_article_case = False

    for p in paragraphs:
        p = p.strip()
        if not p:
            continue

        # Discard horizontal dividers (avoids WordPress auto-converting '---' into an em dash '—')
        if p in ["---", "***", "___"] or re.match(r"^[-*_]{3,}$", p):
            if in_article_case:
                html_parts.append("</div>")
                in_article_case = False
            continue

        # Check for Real example / Echt voorbeeld / Praktijkvoorbeeld section (LaunchStudio styled card)
        is_case_match = re.match(r"^##\s+(Real example|Echt voorbeeld|Praktijkvoorbeeld)", p, re.IGNORECASE)
        if is_case_match:
            if in_article_case:
                html_parts.append("</div>")
            case_type = is_case_match.group(1).strip()
            case_label = "Real example" if "real" in case_type.lower() else "Echt voorbeeld"
            html_parts.append(f'<div class="article-case">\n<div class="case-label">{case_label}</div>')
            in_article_case = True
            continue

        # Fenced Code Block Placeholder
        if p.startswith("__CODE_BLOCK_PLACEHOLDER_"):
            m_idx = re.search(r"\d+", p)
            if m_idx:
                idx = int(m_idx.group())
                if idx < len(code_blocks):
                    html_parts.append(code_blocks[idx])
            continue

        # Headings
        if p.startswith("## "):
            if in_article_case:
                html_parts.append("</div>")
                in_article_case = False
            html_parts.append(f"<h2>{format_inline(p[3:].strip())}</h2>")
        elif p.startswith("### "):
            html_parts.append(f"<h3>{format_inline(p[4:].strip())}</h3>")
        elif p.startswith("#### "):
            html_parts.append(f"<h4>{format_inline(p[5:].strip())}</h4>")

        # Blockquote
        elif p.startswith(">"):
            quote_lines = [l.lstrip(">").strip() for l in p.split("\n")]
            q_text = " ".join([l for l in quote_lines if not l.startswith("-") and not l.startswith("**")])
            q_author = " ".join([l.lstrip("-").strip() for l in quote_lines if l.startswith("-") or l.startswith("**")])
            q_text = q_text.strip().strip('"').strip("'").strip("*").strip('"').strip("'").strip()
            q_author = re.sub(r"^\*\*(.*?)\*\*$", r"\1", q_author).strip("-").strip()

            if in_article_case or site == "launchstudio":
                bq_html = (
                    f'<blockquote>\n'
                    f'  <p><em>"{format_inline(q_text)}"</em></p>\n'
                    f'  <ul>\n'
                    f'    <li><strong>{format_inline(q_author)}</strong></li>\n'
                    f'  </ul>\n'
                    f'</blockquote>'
                )
            else:
                bq_html = (
                    f'<blockquote style="border-left: 4px solid #0073aa; margin: 20px 0; padding: 15px 20px; background-color: #f8f9fa; font-style: italic;">\n'
                    f'  <p style="margin-bottom: 8px;">"{format_inline(q_text)}"</p>\n'
                    f'  <footer style="font-weight: 600; font-style: normal; color: #1a1a1a;">- {format_inline(q_author)}</footer>\n'
                    f'</blockquote>'
                )
            html_parts.append(bq_html)

        # Markdown Table
        elif "|" in p and ("|---" in p or "| ---" in p):
            table_lines = [l.strip() for l in p.split("\n") if l.strip() and l.replace("|", "").replace("-", "").replace(":", "").strip() != ""]
            header_cols = [c.strip() for c in table_lines[0].strip("|").split("|")]
            table_html = [
                '<div style="overflow-x: hidden; max-width: 100%; margin-bottom: 20px;">',
                '  <table style="width: 100%; table-layout: fixed; border-collapse: collapse; border: 2px solid #1a1a1a; font-family: inherit; word-wrap: break-word;">',
                '    <thead style="background-color: #f8f9fa;">',
                '      <tr>'
            ]
            col_width = int(100 / len(header_cols))
            for c in header_cols:
                table_html.append(f'        <th style="width: {col_width}%; border: 1px solid #eaeaea; border-bottom: 2px solid #1a1a1a; padding: 15px 10px; text-align: left; font-size: 1.1em;">{format_inline(c)}</th>')
            table_html.extend(['      </tr>', '    </thead>', '    <tbody>'])
            for r_line in table_lines[1:]:
                if re.match(r"^\|?[\s\-:]+\|?$", r_line):
                    continue
                cols = [c.strip() for c in r_line.strip("|").split("|")]
                table_html.append('      <tr>')
                for c in cols:
                    table_html.append(f'        <td style="border: 1px solid #eaeaea; padding: 12px 10px;">{format_inline(c)}</td>')
                table_html.append('      </tr>')
            table_html.extend(['    </tbody>', '  </table>', '</div>'])
            html_parts.append("\n".join(table_html))

        # Ordered List
        elif re.match(r"^\d+\.\s+", p):
            items = []
            current_item = []
            for line in p.split("\n"):
                if re.match(r"^\d+\.\s+", line):
                    if current_item:
                        items.append(" ".join(current_item))
                    current_item = [re.sub(r"^\d+\.\s+", "", line)]
                else:
                    current_item.append(line.strip())
            if current_item:
                items.append(" ".join(current_item))
            ol_html = ['<ol style="margin-bottom: 20px; padding-left: 25px; line-height: 1.7;">']
            for item in items:
                ol_html.append(f'  <li style="margin-bottom: 10px;">{format_inline(item)}</li>')
            ol_html.append('</ol>')
            html_parts.append("\n".join(ol_html))

        # Bullet / Unordered List
        elif p.startswith(("- ", "* ")):
            items = []
            current_item = []
            for line in p.split("\n"):
                if re.match(r"^[-*]\s+", line):
                    if current_item:
                        items.append(" ".join(current_item))
                    current_item = [re.sub(r"^[-*]\s+", "", line)]
                else:
                    current_item.append(line.strip())
            if current_item:
                items.append(" ".join(current_item))
            ul_html = ['<ul style="margin-bottom: 20px; padding-left: 25px; line-height: 1.7;">']
            for item in items:
                ul_html.append(f'  <li style="margin-bottom: 8px;">{format_inline(item)}</li>')
            ul_html.append('</ul>')
            html_parts.append("\n".join(ul_html))

        # Cost & Timeline inside article-case card
        elif in_article_case and (p.startswith("**Cost & Timeline:**") or p.startswith("**Kosten & Doorlooptijd:**") or p.startswith("**Cost &") or p.startswith("**Kosten &")):
            html_parts.append(f"<p>{format_inline(p)}</p>\n</div>")
            in_article_case = False

        # Standard Paragraph
        else:
            html_parts.append(f"<p>{format_inline(p)}</p>")

    if in_article_case:
        html_parts.append("</div>")

    # Process FAQ Accordion
    if faq_md.strip():
        faq_style = (
            '<style>\n'
            '  /* Modern FAQ Accordion */\n'
            '  .faq-accordion {\n'
            '    max-width: 100%;\n'
            '    margin: 20px auto;\n'
            '    font-family: inherit;\n'
            '  }\n'
            '  .faq-accordion details {\n'
            '    border-bottom: 1px solid #eaeaea;\n'
            '    padding: 15px 0;\n'
            '  }\n'
            '  .faq-accordion summary {\n'
            '    cursor: pointer;\n'
            '    list-style: none;\n'
            '    display: flex;\n'
            '    align-items: center;\n'
            '    justify-content: space-between;\n'
            '    outline: none;\n'
            '  }\n'
            '  .faq-accordion summary::-webkit-details-marker {\n'
            '    display: none;\n'
            '  }\n'
            '  .faq-accordion summary h3 {\n'
            '    margin: 0;\n'
            '    font-size: 1.2em;\n'
            '    font-weight: 600;\n'
            '    color: #1a1a1a;\n'
            '    padding-right: 20px;\n'
            '  }\n'
            '  .faq-accordion summary::after {\n'
            '    content: "+";\n'
            '    font-size: 1.5em;\n'
            '    color: #0073aa;\n'
            '    font-weight: bold;\n'
            '    transition: transform 0.2s ease;\n'
            '  }\n'
            '  .faq-accordion details[open] summary::after {\n'
            '    content: "−";\n'
            '  }\n'
            '  .faq-accordion .faq-answer {\n'
            '    padding-top: 15px;\n'
            '    color: #444;\n'
            '    line-height: 1.6;\n'
            '    font-size: 1em;\n'
            '  }\n'
            '  .faq-accordion .faq-answer p {\n'
            '    margin: 0;\n'
            '  }\n'
            '</style>'
        )
        html_parts.append(faq_style)
        html_parts.append("<h3>FAQs</h3>")
        html_parts.append('<div class="faq-accordion">')

        faq_blocks = re.split(r"###\s+", faq_md)
        for block in faq_blocks:
            if not block.strip():
                continue
            lines = block.strip().split("\n", 1)
            q_text = format_inline(lines[0].strip())
            a_text = format_inline(lines[1].strip() if len(lines) > 1 else "")
            a_text = a_text.replace("\n\n", "</p><p>")

            accordion_item = (
                '  <details>\n'
                f'    <summary><h3 style="margin: 0; font-size: 1.2em; font-weight: 600; color: #1a1a1a;">{q_text}</h3></summary>\n'
                '    <div class="faq-answer">\n'
                f'      <p>{a_text}</p>\n'
                '    </div>\n'
                '  </details>'
            )
            html_parts.append(accordion_item)

        html_parts.append("</div>")

    final_html = "\n\n".join(html_parts)
    return final_html

def upload_post(article_path, image_path=None, media_id=None, post_id=None, site="manifera", status="draft", categories=None, tags=None):
    token, endpoint = get_auth_token(site)
    print(f"[*] Connecting to {site} ({endpoint})...")

    with open(article_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    meta, content_md = parse_markdown_article(md_text)
    title = meta.get("title") or meta.get("Title") or meta.get("Titel") or os.path.basename(article_path).replace(".md", "")
    slug = meta.get("slug") or meta.get("Slug") or os.path.basename(article_path).replace("-dutch.md", "").replace(".md", "").split("-", 1)[-1]
    raw_keywords = meta.get("keywords") or meta.get("Keywords") or meta.get("Trefwoorden") or ""
    focus_kw = raw_keywords.split(",")[0].strip() if raw_keywords else ""
    metadesc = meta.get("description") or meta.get("Description") or meta.get("Beschrijving") or ""

    print(f"[*] Title: {title}")
    print(f"[*] Slug: {slug}")
    print(f"[*] Focus Keyword: {focus_kw}")

    clean_html = markdown_to_clean_html(content_md, site=site)

    # 1. Geotag local image file with GPS & Keywords metadata before upload
    geo_lat, geo_lng, geo_city = DEFAULT_COMPANY_LATITUDE, DEFAULT_COMPANY_LONGITUDE, DEFAULT_COMPANY_CITY
    if image_path and os.path.isfile(image_path):
        res_lat, res_lng, res_city = geotag_image_file(image_path, title, raw_keywords)
        if res_lat is not None:
            geo_lat, geo_lng, geo_city = res_lat, res_lng, res_city

    # 2. Handle image upload if provided
    featured_media_id = media_id
    if image_path and not featured_media_id:
        img_title = title
        if image_path.startswith("http://") or image_path.startswith("https://"):
            img_url = image_path
        else:
            repo_rel = os.path.relpath(image_path, os.getcwd()).replace("\\", "/")
            img_url = f"https://raw.githubusercontent.com/duylesales/sickn33/main/{repo_rel}"

        ext = os.path.splitext(image_path)[1] or ".jpg"
        print(f"[*] Uploading banner from: {img_url}")
        media_res = call_mcp(endpoint, token, "wp_upload_media_from_url", {
            "url": img_url,
            "title": img_title,
            "alt_text": img_title,
            "filename": f"{slug}{ext}"
        }, site_key=site)
        featured_media_id = media_res.get("id")
        print(f"[+] Media uploaded successfully! Attachment ID: {featured_media_id}")
    elif featured_media_id:
        print(f"[*] Using existing featured media ID: {featured_media_id}")

    # Prepare post payload
    payload = {
        "title": title,
        "slug": slug,
        "status": status,
        "comment_status": "closed",
        "content": clean_html,
        "meta": {
            "_yoast_wpseo_focuskw": focus_kw,
            "_yoast_wpseo_metadesc": metadesc
        }
    }

    if featured_media_id:
        payload["featured_media"] = featured_media_id

    if categories:
        payload["categories"] = [int(c.strip()) for c in str(categories).split(",") if c.strip().isdigit()]

    # Assign tags (explicit IDs or auto-extracted from keywords)
    if tags:
        payload["tags"] = [int(t.strip()) for t in str(tags).split(",") if t.strip().isdigit()]
    elif raw_keywords:
        kw_tags = [k.strip() for k in raw_keywords.split(",") if k.strip()]
        if kw_tags:
            payload["tag_names"] = kw_tags
            print(f"[*] Auto-assigned tag names from keywords: {kw_tags}")

    if post_id:
        print(f"[*] Updating existing post ID: {post_id} (status: {status})...")
        payload["post_id"] = post_id
        post_res = call_mcp(endpoint, token, "wp_update_post", payload, site_key=site)
        final_id = post_id
    else:
        print(f"[*] Creating post (status: {status})...")
        post_res = call_mcp(endpoint, token, "wp_create_post", payload, site_key=site)
        final_id = post_res.get("id")

    # Save geolocation metadata to post
    if final_id and geo_lat and geo_lng:
        try:
            geo_address = DEFAULT_COMPANY_ADDRESS if geo_city == "Amsterdam" else f"{geo_city}, Netherlands"
            call_mcp(endpoint, token, "wp_update_post_meta", {
                "post_id": final_id,
                "meta": {
                    "geo_latitude": str(geo_lat),
                    "geo_longitude": str(geo_lng),
                    "geo_city": geo_city,
                    "geo_address": geo_address
                }
            }, site_key=site)
            print(f"[+] Assigned Geo Coordinates ({geo_lat}, {geo_lng}) - {geo_city} to post ID {final_id}")
        except Exception as e:
            print(f"[!] Warning: Could not save geo meta: {e}")

    # Handle Polylang language assignment on LaunchStudio
    if site == "launchstudio" and final_id:
        target_lang = "nl" if article_path.lower().endswith(("-dutch.md", "-nl.md")) or "/dutch/" in article_path.lower() else "en"
        try:
            call_mcp(endpoint, token, "wp_add_post_terms", {
                "post_id": final_id,
                "taxonomy": "language",
                "terms": [target_lang],
                "append": False
            }, site_key=site)
            print(f"[+] Assigned Polylang language '{target_lang}' (append=False) to post ID {final_id}")
        except Exception as e:
            print(f"[!] Warning: Could not assign language term: {e}")

    post_link = post_res.get("link")

    print(f"\n[+] SUCCESS! Post saved successfully!")
    print(f"    Post ID: {final_id}")
    print(f"    Status:  {post_res.get('status', status)}")
    print(f"    Link:    {post_link}")
    return post_res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload Markdown article to WordPress via Easy MCP AI")
    parser.add_argument("--article", required=True, help="Path to markdown article file")
    parser.add_argument("--image", help="Path to image file or public image URL")
    parser.add_argument("--media-id", type=int, help="Existing WordPress media attachment ID")
    parser.add_argument("--post-id", type=int, help="Update existing WordPress post ID instead of creating new")
    parser.add_argument("--site", default="manifera", choices=["manifera", "launchstudio"], help="Target site")
    parser.add_argument("--status", default="draft", help="Post status (default: draft)")
    parser.add_argument("--categories", help="Comma-separated category IDs (e.g. 12,25)")
    parser.add_argument("--tags", help="Comma-separated tag IDs (e.g. 99,2595)")

    args = parser.parse_args()
    upload_post(
        article_path=args.article,
        image_path=args.image,
        media_id=args.media_id,
        post_id=args.post_id,
        site=args.site,
        status=args.status,
        categories=args.categories,
        tags=args.tags
    )
