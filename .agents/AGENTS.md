# Workspace Rules & Guidelines

## Content Generation Guidelines
- **FAQ Requirement:** All generated articles (whether for blogs, long-form content, or whitepapers) MUST include exactly **5 FAQ questions**. Never generate fewer than 5 FAQs.
- **JSON-LD Schema:** The 5 FAQs must also be properly formatted and included in a JSON-LD `<script type="application/ld+json">` block for SEO (as a `FAQPage` schema) at the bottom of the file.

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
- **Never Use Pollinations:** Under no circumstances should any agent use the `pollinations.ai` API for image generation. It produces low-quality, distorted outputs for professional use cases. If the native image generation tool or configured skill fails due to quota limits, inform the user and request a different API key (e.g., OpenAI or Midjourney) or ask them to wait.
