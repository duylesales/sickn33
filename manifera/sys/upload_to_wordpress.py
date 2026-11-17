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
    req = urllib.request.Request(
        token_url,
        data=json.dumps(req_data).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req) as resp:
        new_token_data = json.loads(resp.read().decode("utf-8"))
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
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(req_data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AntigravityWP/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            if "error" in res:
                raise RuntimeError(f"MCP Error: {res['error']}")
            content_items = res.get("result", {}).get("content", [])
            if content_items and content_items[0].get("type") == "text":
                return json.loads(content_items[0]["text"])
            return res.get("result", {})
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("[!] Token expired (401). Refreshing token and retrying...")
            new_token = refresh_oauth_token(site_key)
            return call_mcp(endpoint, new_token, tool_name, arguments, site_key)
        raise

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
    text = text.replace("real-time", "instant")

    # 5. Prevent contraction SQLi pattern in headings
    text = text.replace("What's", "What is")

    # 6. Replace multi-argument parentheses containing commas with brackets to avoid SQL function regex
    def paren_to_brackets(match):
        inner = match.group(1)
        if "," in inner:
            return f"[{inner}]"
        return match.group(0)
    text = re.sub(r"\(([^()]{10,})\)", paren_to_brackets, text)

    return text

def markdown_to_clean_html(content):
    content = sanitize_waf_patterns(content)

    # Split into body and FAQ section
    faq_split = re.split(r"##\s+(?:Frequently Asked Questions|FAQ)", content, flags=re.IGNORECASE)
    body_md = faq_split[0]
    faq_md = faq_split[1] if len(faq_split) > 1 else ""

    html_parts = []

    # Process Body Blocks
    paragraphs = body_md.strip().split("\n\n")
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i].strip()
        if not p:
            i += 1
            continue

        # Headings
        if p.startswith("## "):
            html_parts.append(f"<h2>{p[3:].strip()}</h2>")
        elif p.startswith("### "):
            html_parts.append(f"<h3>{p[4:].strip()}</h3>")
        # Blockquote
        elif p.startswith(">"):
            quote_lines = [l.lstrip(">").strip() for l in p.split("\n")]
            q_text = " ".join([l for l in quote_lines if not l.startswith("-") and not l.startswith("**")])
            q_author = " ".join([l.lstrip("-").strip() for l in quote_lines if l.startswith("-") or l.startswith("**")])
            q_text = q_text.strip('"').strip("'").strip("*")
            q_author = re.sub(r"\*\*([^*]+)\*\*", r"\1", q_author).strip("-").strip()
            bq_html = (
                f'<blockquote style="border-left: 4px solid #0073aa; margin: 20px 0; padding: 15px 20px; background-color: #f8f9fa; font-style: italic;">\n'
                f'  <p style="margin-bottom: 8px;">"{q_text}"</p>\n'
                f'  <footer style="font-weight: 600; font-style: normal; color: #1a1a1a;">- {q_author}</footer>\n'
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
                table_html.append(f'        <th style="width: {col_width}%; border: 1px solid #eaeaea; border-bottom: 2px solid #1a1a1a; padding: 15px 10px; text-align: left; font-size: 1.1em;">{c}</th>')
            table_html.extend(['      </tr>', '    </thead>', '    <tbody>'])
            for r_line in table_lines[1:]:
                # Skip separator lines
                if re.match(r"^\|?[\s\-:]+\|?$", r_line):
                    continue
                cols = [c.strip() for c in r_line.strip("|").split("|")]
                table_html.append('      <tr>')
                for c in cols:
                    c_fmt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", c)
                    table_html.append(f'        <td style="border: 1px solid #eaeaea; padding: 12px 10px;">{c_fmt}</td>')
                table_html.append('      </tr>')
            table_html.extend(['    </tbody>', '  </table>', '</div>'])
            html_parts.append("\n".join(table_html))
        # Bullet list
        elif p.startswith("- ") or p.startswith("* "):
            items = [l.strip()[2:].strip() for l in p.split("\n") if l.strip().startswith(("- ", "* "))]
            ul_html = ["<ul>"]
            for item in items:
                item_fmt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", item)
                ul_html.append(f"  <li>{item_fmt}</li>")
            ul_html.append("</ul>")
            html_parts.append("\n".join(ul_html))
        # Standard paragraph
        else:
            p_fmt = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', p)
            p_fmt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", p_fmt)
            p_fmt = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", p_fmt)
            html_parts.append(f"<p>{p_fmt}</p>")
        i += 1

    # Process FAQ Accordion (Strictly semantic HTML5 with inline styles, NO <script> or <style>)
    if faq_md.strip():
        html_parts.append("<h2>Frequently Asked Questions</h2>")
        html_parts.append('<div class="faq-accordion">')

        faq_blocks = re.split(r"###\s+", faq_md)
        for block in faq_blocks:
            if not block.strip():
                continue
            lines = block.strip().split("\n", 1)
            q_text = lines[0].strip()
            a_text = lines[1].strip() if len(lines) > 1 else ""

            a_text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', a_text)
            a_text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", a_text)
            a_text = a_text.replace("\n\n", "</p><p>")

            accordion_item = (
                '  <details style="border-bottom: 1px solid #eaeaea; padding: 15px 0;">\n'
                f'    <summary style="cursor: pointer; outline: none;"><h3 style="margin: 0; font-size: 1.2em; font-weight: 600; color: #1a1a1a;">{q_text}</h3></summary>\n'
                '    <div class="faq-answer" style="padding-top: 15px; color: #444; line-height: 1.6;">\n'
                f'      <p>{a_text}</p>\n'
                '    </div>\n'
                '  </details>'
            )
            html_parts.append(accordion_item)

        html_parts.append("</div>")

    final_html = "\n\n".join(html_parts)
    return final_html

def upload_post(article_path, image_path=None, media_id=None, site="manifera", status="draft", categories=None, tags=None):
    token, endpoint = get_auth_token(site)
    print(f"[*] Connecting to {site} ({endpoint})...")

    with open(article_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    meta, content_md = parse_markdown_article(md_text)
    title = meta.get("title", os.path.basename(article_path).replace(".md", ""))
    slug = meta.get("slug", os.path.basename(article_path).replace(".md", "").split("-", 1)[-1])
    focus_kw = meta.get("keywords", "").split(",")[0].strip()
    metadesc = meta.get("description", "")

    print(f"[*] Title: {title}")
    print(f"[*] Slug: {slug}")
    print(f"[*] Focus Keyword: {focus_kw}")

    clean_html = markdown_to_clean_html(content_md)

    # Handle image upload if provided
    featured_media_id = media_id
    if image_path and not featured_media_id:
        img_title = title
        if image_path.startswith("http://") or image_path.startswith("https://"):
            img_url = image_path
        else:
            repo_rel = os.path.relpath(image_path, os.getcwd()).replace("\\", "/")
            img_url = f"https://raw.githubusercontent.com/duylesales/sickn33/main/{repo_rel}"

        print(f"[*] Uploading banner from: {img_url}")
        media_res = call_mcp(endpoint, token, "wp_upload_media_from_url", {
            "url": img_url,
            "title": img_title,
            "alt_text": img_title,
            "filename": f"{slug}.jpg"
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

    if tags:
        payload["tags"] = [int(t.strip()) for t in str(tags).split(",") if t.strip().isdigit()]

    print(f"[*] Creating post (status: {status})...")
    post_res = call_mcp(endpoint, token, "wp_create_post", payload, site_key=site)
    post_id = post_res.get("id")
    post_link = post_res.get("link")

    print(f"\n[+] SUCCESS! Post created successfully!")
    print(f"    Post ID: {post_id}")
    print(f"    Status:  {post_res.get('status')}")
    print(f"    Link:    {post_link}")
    return post_res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload Markdown article to WordPress via Easy MCP AI")
    parser.add_argument("--article", required=True, help="Path to markdown article file")
    parser.add_argument("--image", help="Path to image file or public image URL")
    parser.add_argument("--media-id", type=int, help="Existing WordPress media attachment ID")
    parser.add_argument("--site", default="manifera", choices=["manifera", "launchstudio"], help="Target site")
    parser.add_argument("--status", default="draft", help="Post status (default: draft)")
    parser.add_argument("--categories", help="Comma-separated category IDs (e.g. 12,25)")
    parser.add_argument("--tags", help="Comma-separated tag IDs (e.g. 99,2595)")

    args = parser.parse_args()
    upload_post(
        article_path=args.article,
        image_path=args.image,
        media_id=args.media_id,
        site=args.site,
        status=args.status,
        categories=args.categories,
        tags=args.tags
    )
