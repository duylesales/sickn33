#!/usr/bin/env python3
"""
generate_realistic_banners.py - High-End Hyper-Realistic Banner Generator for LaunchStudio
Generates 16:9 documentary editorial photographs (1024x576 PNG) for LaunchStudio articles.

Strict Design & Aesthetic Rules:
1. Photorealistic documentary style (35mm/50mm lens, natural daylight, subtle film grain).
2. Zero AI artifacts: No deformed hands, extra fingers, floating items, or fake CGI gloss.
3. Realistic screen orientation: All displays angled obliquely (30-45 deg) or in soft bokeh,
   showing dark-mode code/dashboards in proper upright orientation (never mirrored/reversed).
4. Strict ban on "device on desk" formula (no flat laptops on desks with coffee mugs).
5. Strict adjacent style & angle contrast (N vs N+1 alternation).
6. Automatic center-crop to 1024x576 PNG and EXIF/PNG geotagging (Amsterdam HQ 52.366841, 4.887593).
"""

import os
import sys
import json
import urllib.request
import urllib.error
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from manifera.sys.upload_to_wordpress import geotag_image_file, DEFAULT_COMPANY_LATITUDE, DEFAULT_COMPANY_LONGITUDE

ARTICLES_EXTRA14_89_100 = [
    {
        "num": 89,
        "slug": "89-stripe-checkout-vs-payment-links-vs-embedded-payments",
        "title": "Stripe Checkout vs Payment Links vs Embedded Payments",
        "keywords": "stripe checkout vs payment links, stripe payment element, stripe integration options, which stripe integration, LaunchStudio, Manifera",
        "archetype": "Over-the-Shoulder / Candid Pair Review",
        "prompt": (
            "Authentic European documentary photography, shot on 50mm prime lens, natural morning daylight, subtle film grain. "
            "Shot over the shoulder of a Dutch backend engineer standing beside a seated colleague in a bright Amsterdam canal-house software studio with tall multi-pane windows and white-washed brick. "
            "They are testing payment integration: an upright matte monitor angled 35 degrees displays dark-mode webhook telemetry logs in soft focus, and a handheld contactless payment reader is being held naturally by one of the engineers. "
            "Zero CGI gloss, natural skin textures, candid posture. No laptop lying flat on a desk, no reversed screens, no floating items, no fake gibberish text. 16:9 aspect ratio."
        )
    },
    {
        "num": 90,
        "slug": "90-launchstudio-vs-doing-production-yourself-with-ai",
        "title": "LaunchStudio vs Doing Production Yourself With AI",
        "keywords": "diy production ai app, launch ai app yourself, launchstudio vs diy, do it yourself security ai app, LaunchStudio, Manifera",
        "archetype": "High-Angle Mezzanine View",
        "prompt": (
            "Authentic European architectural documentary photography, shot on 28mm wide-angle lens, f/4, natural overcast daylight. "
            "High-angle view looking down from an industrial black steel mezzanine catwalk inside a converted software operations warehouse in Rotterdam. "
            "Below on polished concrete floors, a software architect and security auditor stand beside a standing-height maple workbench reviewing CI/CD deployment pipeline stages on an upright angled monitor showing clean dark-mode deployment checks. "
            "Exposed steel roof trusses, high crittall glass windows. No laptops lying flat on desks, no reversed screens, zero AI plastic gloss. 16:9 aspect ratio."
        )
    },
    {
        "num": 91,
        "slug": "91-launchstudio-vs-a-dutch-development-agency",
        "title": "LaunchStudio vs a Dutch Development Agency",
        "keywords": "launchstudio vs agency, app laten bouwen bureau, dutch software agency vs launch partner, agency vs fixed price launch, LaunchStudio, Manifera",
        "archetype": "Architectural Wide-Angle",
        "prompt": (
            "Authentic documentary editorial photograph, shot on 24mm wide lens, natural northern European daylight. "
            "Wide-angle view inside a modern minimalist glass-and-concrete tech incubator in Utrecht. "
            "In the midground, a founder and technical partner sit in leather chairs across a low birch table discussing legal and technical project specifications, holding clean paper contract folders. "
            "Floor-to-ceiling glass windows reveal a quiet canal and green trees outside. Soaring concrete ceilings, clean architectural lines, zero clutter, no laptops on desks. 16:9 aspect ratio."
        )
    },
    {
        "num": 92,
        "slug": "92-vercel-and-supabase-vs-aws-for-an-early-saas",
        "title": "Vercel and Supabase vs AWS for an Early-Stage SaaS",
        "keywords": "vercel supabase vs aws, managed platform vs aws startup, aws for ai-built app, saas infrastructure choice, LaunchStudio, Manifera",
        "archetype": "Tactile Macro / Candid Human Hands",
        "prompt": (
            "Tactile macro documentary photography, shot on 50mm lens at f/2.2, crisp side morning daylight, rich natural textures. "
            "Close-up on a cloud infrastructure architect's hands holding a dark anodized aluminum security hardware key beside a minimalist mechanical keyboard on a solid walnut workbench in Delft. "
            "In the soft blurred bokeh background, an upright matte monitor angled 40 degrees displays cloud architecture routing diagrams in soft focus. "
            "Realistic skin details, authentic mechanical switches, no floating objects, no reversed screens, no CGI sheen. 16:9 aspect ratio."
        )
    },
    {
        "num": 93,
        "slug": "93-rebuild-vs-refactor-an-ai-built-app",
        "title": "Rebuild vs Refactor an AI-Built App: A Decision Matrix",
        "keywords": "rebuild vs refactor ai app, rewrite lovable app, refactor ai generated code, when to rebuild app, LaunchStudio, Manifera",
        "archetype": "First-Person POV / Walking Perspective",
        "prompt": (
            "Documentary photography from a first-person walking perspective, shot on 35mm lens, natural daylight. "
            "Walking through an open industrial steel-framed glass doorway into an Eindhoven software engineering lab. "
            "Through the open doorway, two senior developers stand actively conversing beside an upright vertical code-review screen displaying a git dependency tree in soft focus. "
            "Herringbone wood floor, minimalist timber acoustic wall slats, candid European engineering atmosphere, no desk clutter, no reversed text. 16:9 aspect ratio."
        )
    },
    {
        "num": 94,
        "slug": "94-single-tenant-vs-multi-tenant-for-b2b-saas",
        "title": "Single-Tenant vs Multi-Tenant for a B2B SaaS Founder",
        "keywords": "single tenant vs multi tenant, multi-tenant saas supabase, dedicated instance saas, b2b saas architecture founders, LaunchStudio, Manifera",
        "archetype": "Low-Angle Upward Architectural",
        "prompt": (
            "Low-angle upward documentary photograph, shot on 24mm lens at f/4, diffused daylight from high clerestory windows. "
            "Looking up from floor level inside a historic vaulted warehouse tech studio in Haarlem with exposed timber roof trusses and matte black electrical conduit. "
            "In the midground, two database architects stand at a high standing-height maple table discussing database tenant isolation, looking up at a wall-mounted matte display showing multi-tenant PostgreSQL connection pools. "
            "Strong architectural volume, warm bricks, zero CGI gloss, no laptop lying flat on a desk. 16:9 aspect ratio."
        )
    },
    {
        "num": 95,
        "slug": "95-build-vs-buy-for-saas-features-auth-billing-email",
        "title": "Build vs Buy for SaaS Features: Auth, Billing, Email and More",
        "keywords": "build vs buy saas features, saas billing build or buy, auth service vs custom, ai-built saas components, LaunchStudio, Manifera",
        "archetype": "Over-the-Shoulder / Code Review",
        "prompt": (
            "Authentic European documentary photography, shot on 50mm lens at f/2.5, soft diffused natural northern daylight. "
            "Shot over the shoulder of a lead engineer in a dark knitted sweater pointing with a pencil at an upright widescreen monitor angled 45 degrees, showing clean dark-mode API gateway architecture in soft focus. "
            "Beside them, a founder in a linen shirt listens attentively in a quiet Leiden software incubator with whitewashed brick walls and arched windows. "
            "Zero artificial sheen, natural human posture, no reversed screens, no loose cables. 16:9 aspect ratio."
        )
    },
    {
        "num": 96,
        "slug": "96-prototype-vs-mvp-vs-production-app",
        "title": "Prototype vs MVP vs Production App: What's the Difference?",
        "keywords": "prototype vs mvp, mvp vs production app, ai prototype definition, production ready meaning, LaunchStudio, Manifera",
        "archetype": "High-Angle Mezzanine View",
        "prompt": (
            "Authentic documentary photography, shot on 35mm lens, f/4, crisp morning sunlight. "
            "High-angle view looking down from an open timber mezzanine staircase into a sunlit double-height canal-house studio on Herengracht in Amsterdam. "
            "Below on wide herringbone oak floors, three tech team members sit around a solid oak table reviewing architectural roadmap diagrams. "
            "Arched multi-pane windows looking onto the canal, lush indoor fiddle-leaf fig, clean Scandinavian-Dutch aesthetic, no clutter, no laptops flat on desks. 16:9 aspect ratio."
        )
    },
    {
        "num": 97,
        "slug": "97-mollie-vs-stripe-for-subscriptions-in-the-netherlands",
        "title": "Mollie vs Stripe for Subscriptions in the Netherlands",
        "keywords": "mollie vs stripe subscriptions, stripe billing vs mollie subscriptions, dutch saas recurring payments, ideal subscription provider, LaunchStudio, Manifera",
        "archetype": "Tactile Macro / Hands in Motion",
        "prompt": (
            "Tactile macro documentary photography, shot on 50mm lens at f/2.0, natural side lighting from a tall window, subtle grain. "
            "Focus on a fintech software developer's hands holding an NFC payment testing card just above a matte black payment terminal on a solid ash workbench in Groningen. "
            "In the blurred bokeh background, an angled laptop display shows recurring SEPA subscription webhook telemetry in soft focus. "
            "Authentic tactile details, real wood grain, no floating objects, no reversed logos. 16:9 aspect ratio."
        )
    },
    {
        "num": 98,
        "slug": "98-magic-links-vs-passwords-vs-social-login",
        "title": "Magic Links vs Passwords vs Social Login: Choosing Sign-In for Your App",
        "keywords": "magic links vs passwords, social login vs password, passwordless login saas, supabase login options, LaunchStudio, Manifera",
        "archetype": "Architectural Wide-Angle",
        "prompt": (
            "Architectural wide-angle documentary shot, 24mm lens, clean morning daylight. "
            "Inside a tranquil, light-filled software studio in Arnhem with steel-framed glass doors leading to an inner garden courtyard. "
            "In the center of the room, a UX researcher and an authentication engineer sit at a custom timber standing island, reviewing mobile authentication user journeys on a test phone held in hand. "
            "Tall plants, natural oak flooring, minimalist Dutch design, zero fake AI elements, no clutter. 16:9 aspect ratio."
        )
    },
    {
        "num": 99,
        "slug": "99-lovable-cloud-vs-your-own-supabase-which-to-start-with",
        "title": "Lovable Cloud vs Your Own Supabase: Which Should You Start With?",
        "keywords": "lovable cloud vs supabase, lovable cloud or own supabase, lovable backend choice, connect supabase lovable, LaunchStudio, Manifera",
        "archetype": "First-Person POV / Walking Perspective",
        "prompt": (
            "First-person POV documentary perspective, shot on 35mm lens, natural overcast daylight. "
            "Walking into a modern brick-and-glass tech studio in Delft. "
            "Ahead, a cloud architect stands at a high consultation table gesturing naturally toward an upright matte monitor angled 30 degrees showing database connection pool telemetry in soft focus. "
            "Warm hardwood floors, brick walls, realistic candid posture, no reversed text, no CGI gloss. 16:9 aspect ratio."
        )
    },
    {
        "num": 100,
        "slug": "100-lovable-vs-retool-for-internal-tools",
        "title": "Lovable vs Retool for Internal Tools",
        "keywords": "lovable vs retool, internal tool builder, retool alternative ai, build internal tool with ai, LaunchStudio, Manifera",
        "archetype": "Low-Angle Upward Architectural",
        "prompt": (
            "Low-angle upward documentary photograph, shot on 28mm lens at f/3.5, industrial studio lighting combined with soft daylight. "
            "Looking up inside an Eindhoven engineering hub with exposed ceiling ventilation pipes and timber acoustic slats. "
            "In the midground, an operations architect and product manager stand beside an elevated display station reviewing role-based permission hierarchies on an upright display. "
            "Clean professional atmosphere, candid posture, zero AI artifacts, no flat laptops on desks. 16:9 aspect ratio."
        )
    }
]

def crop_and_resize(img, target_width=1024, target_height=576):
    width, height = img.size
    target_ratio = target_width / target_height
    current_ratio = width / height

    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        img = img.crop((0, top, width, top + new_height))

    return img.resize((target_width, target_height), Image.Resampling.LANCZOS)

def generate_with_gemini(api_key, prompt, output_path):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key={api_key}"
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9",
            "outputOptions": {"mimeType": "image/png"}
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    import base64
    from io import BytesIO
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        b64_str = data["predictions"][0]["bytesBase64Encoded"]
        raw_bytes = base64.b64decode(b64_str)
        img = Image.open(BytesIO(raw_bytes))
        return img

def generate_with_openai(api_key, prompt, output_path):
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1792x1024",
        "response_format": "b64_json",
        "quality": "standard"
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    )
    import base64
    from io import BytesIO
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        b64_str = data["data"][0]["b64_json"]
        raw_bytes = base64.b64decode(b64_str)
        img = Image.open(BytesIO(raw_bytes))
        return img

def process_and_save_image(raw_img, article_info, base_dir):
    slug = article_info["slug"]
    title = article_info["title"]
    keywords = article_info["keywords"]
    output_path = os.path.join(base_dir, f"{slug}_pic.png")

    # 1. Crop & resize to 1024x576
    final_img = crop_and_resize(raw_img, 1024, 576)
    final_img = final_img.convert("RGB")
    final_img.save(output_path, "PNG", optimize=True)
    print(f"[OK] Saved cropped 1024x576 PNG: {output_path}")

    # 2. Geotag & embed metadata
    lat, lon, city = geotag_image_file(output_path, title, keywords)
    print(f"[OK] Geotagged with {city} ({lat}, {lon}) and embedded keywords.")
    return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate realistic banners for articles 89-100")
    parser.add_argument("--provider", choices=["gemini", "openai"], default=None, help="Image provider")
    parser.add_argument("--api-key", default=None, help="API key for selected provider")
    parser.add_argument("--article", type=int, default=None, help="Generate for single article number (e.g. 89)")
    parser.add_argument("--list-prompts", action="store_true", help="Print all planned prompts and archetypes")
    args = parser.parse_args()

    if args.list_prompts:
        print(f"Total articles planned: {len(ARTICLES_EXTRA14_89_100)}")
        for art in ARTICLES_EXTRA14_89_100:
            print(f"Article {art['num']}: {art['title']}")
            print(f"  Archetype: {art['archetype']}")
            print(f"  Prompt: {art['prompt']}\n")
        sys.exit(0)

    base_dir = "launchstudio/2026-extra/extra-14-addation"
    provider = args.provider
    api_key = args.api_key

    if not provider:
        if os.environ.get("OPENAI_API_KEY"):
            provider = "openai"
            api_key = os.environ.get("OPENAI_API_KEY")
        elif os.environ.get("GEMINI_API_KEY"):
            provider = "gemini"
            api_key = os.environ.get("GEMINI_API_KEY")

    if not provider or not api_key:
        print("Error: No provider/API key provided or found in environment.")
        print("Please supply --provider [gemini|openai] --api-key <KEY> or set OPENAI_API_KEY / GEMINI_API_KEY.")
        sys.exit(1)

    targets = ARTICLES_EXTRA14_89_100
    if args.article:
        targets = [a for a in targets if a["num"] == args.article]
        if not targets:
            print(f"Article {args.article} not found in planned list.")
            sys.exit(1)

    print(f"Starting generation with provider '{provider}' for {len(targets)} articles...")
    for art in targets:
        print(f"\n--- Generating for Article {art['num']}: {art['title']} ---")
        try:
            if provider == "gemini":
                img = generate_with_gemini(api_key, art["prompt"], "")
            elif provider == "openai":
                img = generate_with_openai(api_key, art["prompt"], "")
            process_and_save_image(img, art, base_dir)
        except Exception as e:
            print(f"[ERROR] Failed to generate for Article {art['num']}: {e}")
            break
