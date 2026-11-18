# Workspace Rules & Guidelines

## Content Generation Guidelines
- **FAQ Requirement & Heading:** All generated articles (whether for blogs, long-form content, or whitepapers) MUST include exactly **5 FAQ questions**. Never generate fewer than 5 FAQs. The section heading must ALWAYS use the abbreviation **"FAQs"** (or **"FAQ"**), NEVER write out in full ("Frequently Asked Questions").
- **JSON-LD Schema:** The 5 FAQs must also be properly formatted and included in a JSON-LD `<script type="application/ld+json">` block for SEO (as a `FAQPage` schema) at the bottom of the file.
- **No Em Dash (All Projects - Mandatory):** In every article across all folders/projects (launchstudio, manifera, onlyaijobs and any new project), including Dutch versions, social posts, FAQs and JSON-LD, use ONLY the short hyphen `-`. NEVER use the em dash `—`. Write `word - word` (with spaces), never `word—word` or `word — word`.

## Image Generation Guidelines
- **Adjacent Style & Angle Contrast (Strict Sequencing Rule - Mandatory):** Two consecutive/adjacent images in a series MUST NEVER share the same layout style, camera angle, framing, or focal distance. If image N is a macro/tactile close-up, image N+1 must be an architectural wide shot or over-the-shoulder action shot. If image N is an interior room, image N+1 must be an in-transit/outdoor/industrial scene. Always alternate and starkly contrast consecutive images.
- **Strict Ban on "Device on Desk" Formula:** NEVER default to the lazy template of "a laptop or tablet lying on a desk/table/counter with props scattered around it". Actively rotate across distinct visual archetypes:
  1. *Architectural Wide-Angle*: Deep focal length showing an entire facility/depot/data center (no desk in foreground), wall-mounted status displays, natural daylight, architectural volume.
  2. *Over-the-Shoulder / Human in Active Motion*: Shot over the shoulder of an engineer/operator standing and actively manipulating equipment (rack cabinet, server cabling, handheld diagnostic scanner, vehicle diagnostics).
  3. *First-Person POV / Walking Perspective*: Moving through a facility, looking through a vehicle windshield, walking down warehouse aisles between high-bay racks.
  4. *Macro / Extreme Close-up*: Detailed focus on hands terminating fiber/cables, physical security token (YubiKey), calibration gauge, hardware connector.
  5. *Low-Angle Upward / High-Angle Mezzanine*: Camera positioned low looking up at structural steel, industrial conduit, or high-angle looking down from an industrial catwalk/balcony.
  6. *Non-Desk / In-Transit Environments*: Inside delivery vehicle cargo hold, server corridor, electrical plant room, stage lighting booth, construction bay.
- **Literal and Grounded (No Abstract Metaphors):** Because these are hyper-realistic images for enterprise business articles, avoid confusing abstract art, sci-fi concepts, or overly complex visual metaphors. The imagery must be immediately understandable and grounded in real-world, high-end professional tech environments (e.g., a modern data center, an executive boardroom, a realistic code review session, architectural tech spaces). Diversity comes from changing the real-world scene and camera angle, NOT from making the concept weirder.
- **Core Technical Focus (Do NOT Base on Anecdotal Real Examples):** Imagery MUST directly represent the core technical, architectural, operational, or business subject matter of the article itself (e.g., live database schema migration pipelines, edge computing network boundaries, DNS routing infrastructure, session token authentication, transactional email delivery telemetry), rather than being tethered to the anecdotal small business or local founder case study in "Real Example" (e.g., padel club, cafe, bakery, pet clinic). The visual narrative must reflect the true software engineering and enterprise infrastructure domain of the article.
- **Never Use Pollinations:** Under no circumstances should any agent use the `pollinations.ai` API for image generation. It produces low-quality, distorted outputs for professional use cases. If the native image generation tool or configured skill fails due to quota limits, inform the user and request a different API key (e.g., OpenAI or Midjourney) or ask them to wait.

## Default Company Geolocation & Image Metadata Guidelines (Manifera & LaunchStudio)
- **Default Company Location (Applies to both Manifera & LaunchStudio):**
  - **Latitude:** `52.366841`
  - **Longitude:** `4.887593`
  - **Address:** Herengracht 420, 1017 BZ Amsterdam, Netherlands
- **Image Geotagging & Metadata Protocol (Mandatory for all images):**
  - Every featured image or article illustration for both Manifera and LaunchStudio MUST be geotagged with GPS metadata before upload.
  - For general articles or when no specific local city is targeted, ALWAYS use the company headquarters coordinates: Latitude `52.366841`, Longitude `4.887593`.
  - For local campaign articles (e.g., `extra-5-local` targeting specific Dutch cities), use the targeted city coordinates, or fallback to the company HQ coordinates (`52.366841`, `4.887593`).
  - Embed the article's `Keywords` into image EXIF (`XPKeywords`) and PNG text chunks (`Keywords`).
  - Embed the article's `Title` and `Description` into image EXIF (`XPTitle`, `ImageDescription`) and PNG metadata.

## WordPress Publishing & Easy MCP AI Guidelines (Manifera & LaunchStudio)
To avoid Web Application Firewall (WAF/Wordfence/ModSecurity) `403 Forbidden` errors and optimize execution speed when publishing or drafting posts:
- **Strict Ban on `<script>` in Post Content:** NEVER send `<script type="application/ld+json">` or inline `<script>` tags in the WordPress REST API post payload. The server firewall treats them as XSS injection vectors and blocks requests with 403 Forbidden.
- **FAQ Heading Abbreviation:** Always use the abbreviated heading `<h3>FAQs</h3>` (or `<h2>FAQs</h2>`). Never write out the full phrase "Frequently Asked Questions" in post content or headings.
- **Native Semantic HTML5 for FAQ Accordions:** Format all 5 FAQs using semantic HTML5 elements (`<details><summary>`) styled with the scoped `.faq-accordion` stylesheet (which adds `+` and `−` indicators):
  ```html
  <style>
    .faq-accordion { max-width: 100%; margin: 20px auto; font-family: inherit; }
    .faq-accordion details { border-bottom: 1px solid #eaeaea; padding: 15px 0; }
    .faq-accordion summary { cursor: pointer; list-style: none; display: flex; align-items: center; justify-content: space-between; outline: none; }
    .faq-accordion summary::-webkit-details-marker { display: none; }
    .faq-accordion summary h3 { margin: 0; font-size: 1.2em; font-weight: 600; color: #1a1a1a; padding-right: 20px; }
    .faq-accordion summary::after { content: '+'; font-size: 1.5em; color: #0073aa; font-weight: bold; transition: transform 0.2s ease; }
    .faq-accordion details[open] summary::after { content: '−'; }
    .faq-accordion .faq-answer { padding-top: 15px; color: #444; line-height: 1.6; font-size: 1em; }
    .faq-accordion .faq-answer p { margin: 0; }
  </style>
  <div class="faq-accordion">
    <details>
      <summary><h3 style="margin: 0; font-size: 1.2em; font-weight: 600; color: #1a1a1a;">[Scenario: Persona description] Question text?</h3></summary>
      <div class="faq-answer">
        <p>Answer text.</p>
      </div>
    </details>
  </div>
  ```
- **Square Brackets for Scenario Labels & Parentheses Sanitization:** Use square brackets `[Scenario: ...]` instead of parentheses `(Scenario: ...)` in FAQ question headings. Additionally, avoid parentheses containing multiple comma-separated items (e.g. `(item1, item2, item3)`) in body text or headings - convert them to square brackets `[...]` or dashes `- ... -` to prevent triggering SQL function regex detection (`\w+\s*\([^)]*,[^)]*\)`).
- **WAF Sensitive Keyword Replacements:** Replace `real-time` with `instant` or `cloud`, replace `by the time` with `when` (prevents time-based SQLi regex `BY ... TIME`), replace contractions like `what's` with `what is`, and avoid combinations like `basic forms, no real-time` (replace with `simple inputs, static workflows`) which trigger SQLi/command injection filters.
- **WAF Cooldown & Rate Limiting:** If a 403 Forbidden is returned, pause for 3 to 5 seconds before retrying to allow the firewall's temporary IP cooldown window to clear.
- **OAuth Token Auto-Refresh:** OAuth tokens expire after 3600 seconds. Tools must automatically refresh using `refresh_token` and `token_url` from `~/.gemini/antigravity/mcp_oauth_tokens.json` when receiving a 401 Unauthorized.
- **Media Upload Protocol:** Always upload featured images via `wp_upload_media_from_url` using the public raw GitHub repository URL (`https://raw.githubusercontent.com/...`) after git push, avoiding base64 encoding/decoding overhead.
- **Table Styling:** Always wrap tables in `<div style="overflow-x: hidden; max-width: 100%; margin-bottom: 20px;">` with `<table style="width: 100%; table-layout: fixed; border-collapse: collapse; border: 2px solid #1a1a1a; font-family: inherit; word-wrap: break-word;">` and `#f8f9fa` header background.
- **Automated Upload Tooling:** Use the standardized script `manifera/sys/upload_to_wordpress.py` for automated one-click drafting and publishing with built-in WAF sanitization and Yoast SEO integration.
