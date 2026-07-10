# Workspace Rules & Guidelines

## Content Generation Guidelines
- **FAQ Requirement:** All generated articles (whether for blogs, long-form content, or whitepapers) MUST include exactly **5 FAQ questions**. Never generate fewer than 5 FAQs.
- **JSON-LD Schema:** The 5 FAQs must also be properly formatted and included in a JSON-LD `<script type="application/ld+json">` block for SEO (as a `FAQPage` schema) at the bottom of the file.

## Image Generation Guidelines
- **Non-Repetitive Layouts (Diversity):** When generating multiple images in a series, NEVER reuse the same structural layout or visual template (e.g., "Person A on left, glowing object in center, Person B on right" or "Bad on left, fix in center, Good on right"). You MUST invent vastly diverse compositions and perspectives (macro, wide-angle, over-the-shoulder, architectural) to avoid boring repetition.
- **Literal and Grounded (No Abstract Metaphors):** Because these are hyper-realistic images for enterprise business articles, avoid confusing abstract art, sci-fi concepts, or overly complex visual metaphors. The imagery must be immediately understandable and grounded in real-world, high-end professional tech environments (e.g., a modern data center, an executive boardroom, a realistic code review session, architectural tech spaces). Diversity comes from changing the real-world scene and camera angle, NOT from making the concept weirder.
- **Never Use Pollinations:** Under no circumstances should any agent use the `pollinations.ai` API for image generation. It produces low-quality, distorted outputs for professional use cases. If the native image generation tool or configured skill fails due to quota limits, inform the user and request a different API key (e.g., OpenAI or Midjourney) or ask them to wait.
