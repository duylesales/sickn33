# ChatGPT Ads Landing Page (AG0): Prompt for Lovable (EN only, 1 page)

> **Cách dùng:** dán **Prompt 1** vào Lovable trước. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 5**, mỗi lần một prompt, kiểm tra xong rồi mới dán tiếp.
> **AG0 là gì:** một landing page duy nhất cho cả chiến dịch `mf-chatgpt-eu-test400`. Cả 3 ad group (AG1 vendor selection, AG2 dedicated team, AG3 AI SaaS) đều trỏ về đây. Tiêu đề và bước đầu của Team Builder tự đổi theo tham số `?ag=` để khớp với câu người dùng vừa hỏi ChatGPT. Không có tham số thì trang hiện bản chung (AG0).
> **Nguồn câu chữ:** mọi con số, lời chứng thực và cam kết đều lấy từ [`chatgpt_ads_plan_manifera.md`](./chatgpt_ads_plan_manifera.md) §3 và [`homepage-lovable-prompt.md`](./homepage-lovable-prompt.md) (đã kiểm tra trên manifera.com ngày 20-25/11/2026). Không thêm số liệu hay lời hứa nào khác.

---

## Ý tưởng chính (tóm tắt cho bạn, không dán vào Lovable)

| # | Ý tưởng | Vì sao hiệu quả với traffic từ ChatGPT |
|---|---|---|
| 1 | **Hero dạng hội thoại**: câu hỏi người dùng vừa hỏi ChatGPT tự gõ ra trong một khung chat, sau đó Manifera "trả lời" bằng một thẻ có số liệu thật | Nối tiếp đúng cuộc trò chuyện họ đang có, nên không bị hụt hẫng. Câu hỏi đổi theo từng ad group |
| 2 | **Team Builder + "Team Pass"**: 3 bước chạm-là-chọn (bạn đang làm gì → ghép team bằng cách bấm vai trò, avatar "nảy" vào bàn → khi nào bắt đầu). Bên cạnh là một **thẻ lên máy bay AMS ⇄ SGN** cập nhật trực tiếp theo lựa chọn | Biến form dài thành trò chơi, người dùng đầu tư công sức nên muốn gửi đi. Bước 4 mới là form liên hệ (chỉ 4 trường). Đồng thời thu đủ dữ liệu để chấm "qualified lead" (cỡ team, thời điểm bắt đầu, quốc gia) |
| 3 | **Đồng hồ sống Amsterdam ⇄ Hồ Chí Minh** với vòng cung chấm chạy và vùng giờ trùng nhau | Trả lời nỗi lo số 1 về offshore (lệch giờ) bằng dữ liệu thật thay vì lời hứa |
| 4 | **Thẻ lật "Bạn đang lo điều gì?"** | Chạm để lật, mặt sau là bằng chứng (địa chỉ Amsterdam, quote khách hàng, số dự án) |
| 5 | **Đường vẽ theo cuộn trang** nối 4 bước "How it works" | Giữ mắt người đọc đi xuống, kết thúc ở nút CTA |
| 6 | **Thanh dính trên mobile hiển thị tiến độ** "Team brief 2/4 · Continue", lưu lựa chọn khi rời trang | Kéo người đã bắt đầu quay lại hoàn tất |
| 7 | **Khoảnh khắc thành công**: dấu "BRIEF RECEIVED" đóng lên Team Pass + confetti màu logo | Kết thúc vui, đáng nhớ, và là nơi bắn event chuyển đổi |

Không dùng: đếm ngược giả, "X người đang xem", popup khi vừa vào trang, bảng tính giá (không có giá đã kiểm chứng).

---

## Prompt 1: Main build

```
Build a ONE-PAGE, English-only landing page for Manifera, a software development company with headquarters in Amsterdam, an engineering hub in Ho Chi Minh City (Vietnam) and an office in Singapore. Visitors arrive from ads inside ChatGPT, mostly on mobile, right after asking an AI assistant something like "Which company can build our platform?". The page has ONE job: get them to complete a short, playful "Team Brief" that ends in the contact form. Everything on the page serves that goal.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react icons, framer-motion for animation, canvas-confetti for the success moment. ONE route only ("/"). No other pages, no thank-you route: the success state appears in place. Mobile-first (design at 375px first), fully responsive. No lorem ipsum: use the exact copy below. Do not invent numbers, promises, client names or prices.

=== DESIGN SYSTEM (same as manifera.com) ===
CSS variables in index.css, mapped in tailwind.config:
--white #FFFFFF (main background) · --mist #F5F6FA (alternate sections) · --cosmic #05060F (headings, text, dark bands) · --logo-navy #0F0F3C (glows inside dark bands) · --blue #1E5CC8 (primary: buttons, links, icons) · --magenta #CD37A5 (accent, large or decorative only) · --body #3D4257 · --muted #6B7086 · --line #E6E8F0.
Ratio: about 70% white/mist, 15% cosmic, 10% blue, 5% magenta. Magenta never on buttons, body text or small text on white.
Signature: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5) for small accents only: the underline under one word in the H1, the Team Builder progress bar, avatar rings, the "BRIEF RECEIVED" stamp.
Fonts: "Space Grotesk" for headings (H1 40-44px mobile / 60-68px desktop, tight tracking), "Inter" for body (17px, line-height 1.6).
Buttons: primary solid blue, white text, rounded-xl, arrow icon, min height 52px on mobile. Secondary white with 1px cosmic/15% border.
Cards: white, 1px --line border, rounded-2xl, soft shadow 0 8px 30px rgba(5,6,15,0.06).
Accessibility: WCAG AA, visible blue focus rings, semantic landmarks, every interactive choice is a real <button> with aria-pressed, full keyboard support, and every animation has a static version under prefers-reduced-motion.

=== MESSAGE MATCH: one page, four variants ===
Read the variant from the URL: ?ag=vendor | team | saas. If missing, also accept utm_content starting with "ag1" (vendor), "ag2" (team) or "ag3" (saas). Otherwise use "default". Store the variant in state; it changes the hero question, H1, sub-headline and the pre-selected first step of the Team Builder. Keep the rest of the page identical.

| variant | Chat question (typed in the hero) | H1 (gradient underline on the word in [brackets]) | Sub-headline | Builder step 1 pre-selected |
| default | "Which software development company can build our platform?" | "The software [partner] you were asking about." | "A dedicated engineering team in Ho Chi Minh City, managed from Amsterdam. 160 applications built since 2014." | none |
| vendor | "How do I choose a software development company for our platform?" | "Your platform, built by a [team] managed from Amsterdam." | "Custom web, mobile and business software for SMEs and enterprises. 120 global clients since 2014." | "A new platform or product" |
| team | "Offshore or nearshore: which is safer for a Dutch company?" | "A dedicated dev team, without the [hiring] delays." | "Your own engineers in Ho Chi Minh City, governance in Amsterdam. Scale up as your roadmap grows." | "Extra capacity for my team" |
| saas | "Which company can build our AI-powered SaaS product?" | "From AI prototype to a [SaaS product] your customers use." | "A dedicated product engineering team for your SaaS, managed from Amsterdam. On request we use local AI models, so your data stays out of public LLMs." | "An AI-powered SaaS product" |

=== HEADER (minimal, no navigation: this is an ad landing page) ===
Sticky white header, 1px --line bottom border after scrolling. Colour Manifera logo on the left (not a link). On the right a compact primary button "Talk to our team" that scrolls to #brief. A 3px scroll-progress bar runs along the bottom edge of the header in the blue-to-magenta gradient.

=== SECTION 1: HERO (id="hero") ===
White, two columns on desktop, stacked on mobile (text first, chat card second).
Left:
- Eyebrow with a small gradient dot: "Software development · Amsterdam · Ho Chi Minh City · Singapore · Since 2014"
- H1 and sub-headline from the variant table.
- Primary CTA "Build your team brief" (scrolls to #brief). Secondary text link "See how it works" (scrolls to #how).
- Micro line: "About 60 seconds. We will contact you within one working day."
Right: the CHAT CARD, the signature moment of the page. A clean, neutral chat window (white card, rounded-2xl, soft shadow, small grey header label "The question you probably just asked"). Do NOT use the ChatGPT or OpenAI name, logo, colours or interface; keep it generic.
Animation sequence (plays once when the page loads, about 4 seconds total):
 1. A user bubble on the right types out the variant's chat question letter by letter (35ms per character) with a blinking caret.
 2. A reply bubble on the left shows three "typing" dots for 900ms.
 3. The dots morph into a reply card from "Manifera" (small logo mark) that reveals three lines one by one, each with a blue check icon:
    "A dedicated engineering team, managed from Amsterdam"
    "160 applications delivered for 120 global clients"
    "We will contact you within one working day"
 4. Under the lines, a small blue button inside the card: "Build your team brief" (scrolls to #brief), which pulses softly once.
A small "Replay" icon button in the card header replays the sequence. Under prefers-reduced-motion show the final state immediately.
Behind the card, a very soft radial blue glow that follows the cursor slowly on desktop (disabled on touch devices and under reduced motion).

=== SECTION 2: PROOF BAND (cosmic black band with a faint logo-navy radial glow) ===
Four counters that count up once when they enter the viewport (1.2s, ease-out): "160" Applications · "120" Global clients · "30" Experts and growing · "2014" Since. Under them a slow grayscale logo marquee (white logos on black, colour on hover, pauses on hover and under reduced motion) labelled "Some of our clients and partners": Vodafone, Statler, Kilimo, MO Batteries, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham. Use only the logo files I upload; if a logo is missing, show the company name in white text instead.

=== SECTION 3: TEAM BRIEF BUILDER (id="brief"), the core of the page ===
Mist background. Title: "Build your team brief". Sub: "Three taps to tell us what you need. Then we take it from there."
Layout: desktop = builder on the left (60%), live TEAM PASS preview on the right (40%, sticky while scrolling inside the section). Mobile = builder full width, with the Team Pass shown as a compact bar above the step buttons that expands on tap.
A progress bar on top (gradient) with 4 labelled dots: "Project" · "Team" · "Start" · "Send". Steps slide horizontally (framer-motion, 250ms). "Back" link on steps 2-4. Selections are saved in localStorage so a visitor who leaves and returns continues where they stopped (show "Welcome back, your brief is saved" toast in that case).

STEP 1 "What are you building?" Four large tappable cards with an icon, title and one line (single select, auto-advance 300ms after the tap):
- "A new platform or product": "Web, mobile or business software, from design to deployment."
- "Extra capacity for my team": "Dedicated engineers who join your roadmap."
- "An AI-powered SaaS product": "A SaaS platform, or AI features added to the one you have."
- "Something else": "Tell us in your own words at the end."
Pre-select from the variant (the card shows a small "Suggested" tag), but the visitor can change it.

STEP 2 "Who do you need on the team?" A grid of role chips (multi select), each with a lucide icon: Frontend developer · Backend developer · Mobile developer · UI/UX designer · QA engineer · Project manager · DevOps engineer · AI integration engineer.
Each chip has a small "−  1  +" stepper once selected (0-6 per role). Pre-fill a sensible starting team based on step 1 (for example "A new platform": 1 frontend, 1 backend, 1 UI/UX, 1 QA, 1 project manager; "Extra capacity": 2 backend, 1 frontend; "AI-powered SaaS": 1 frontend, 2 backend, 1 AI integration, 1 QA). Also a "Not sure yet, advise me" toggle that clears the roles and sets team = "Manifera to advise".
FUN DETAIL: every time a role is added, an abstract avatar token (a circle with the role icon and a gradient ring, NO human faces) pops onto a "team table" illustration with a spring animation; removing it makes the token shrink away. A big rolling number shows the team size: "Your team: 5 people".
Continue button: "Looks good".

STEP 3 "When would you like to start?" Pills (single select, auto-advance): "As soon as possible" · "Within 3 months" · "In 3 to 6 months" · "Just exploring for now".

STEP 4 "Where should we send your team brief?" (this is the contact form, react-hook-form + zod):
- Name (required)
- Work email (required, valid email; if the domain is gmail/hotmail/outlook/yahoo/icloud show a friendly hint "A work email helps us prepare for the call", but still allow it)
- Company (required)
- Country (required select: Netherlands, Belgium, Germany, Other EU/EEA country, United Kingdom, Switzerland, Other)
- Anything else we should know? (optional textarea, placeholder "Your product, your stack, a link, anything that helps.")
- How did you hear about us? (select: ChatGPT, Google, LinkedIn, Recommendation, Other). Pre-select "ChatGPT" when utm_source=chatgpt.
- Human check: "What is 4 + 3?" (random numbers per load) plus a hidden honeypot field.
- Submit button, full width: "Send my team brief"
- Under it, small muted text: "We will contact you within one working day. By sending this form you agree to our Privacy Policy." (link to https://www.manifera.com/privacy-policy/, opens in a new tab)
Also offer a quiet escape under the step 1 title: link "Prefer to just write to us? Skip to the form" which jumps straight to step 4 with project = "Something else" and team = "Manifera to advise".

THE TEAM PASS (live preview): a white card designed like a boarding pass, with a perforated divider and a decorative barcode.
- Top: "TEAM PASS" · "AMS ⇄ SGN" (Amsterdam ⇄ Ho Chi Minh City), with a tiny plane icon that moves along a dotted line as the progress grows.
- Fields that fill in live with a soft flip animation: PROJECT (step 1) · CREW (avatar tokens + total) · START (step 3) · PASSENGER (company name, typed live from the form) · MANAGED FROM "Amsterdam".
- Each completed step adds a small check to the pass.

SUCCESS STATE (in place, no page change): the builder slides away, the Team Pass moves to the centre and a rotated gradient stamp "BRIEF RECEIVED" lands on it (scale 1.4 → 1, slight rotation, 400ms), followed by one short confetti burst in blue and magenta (skip confetti under reduced motion). Copy under it:
H3 "Thank you, {first name}. Your team brief is with us."
"We will contact you within one working day. Prefer to talk now? Call our Amsterdam office: +31 619 70 10 01" (tel: link).
Secondary links: "See our portfolio" (https://www.manifera.com/portfolio/, new tab).
Clear the localStorage brief after a successful send.

=== SECTION 4: TWO CITIES, ONE TEAM (id="cities") ===
White. Title: "Two cities, one team." A minimal dotted world-map strip (SVG, no external map library) with two pins, Amsterdam and Ho Chi Minh City, joined by an arc along which a small glowing dot travels every few seconds (static under reduced motion). Under each pin a LIVE clock (Intl.DateTimeFormat with Europe/Amsterdam and Asia/Ho_Chi_Minh, updating every second) and the label "HQ and management" / "Engineering hub". A small third chip: "Singapore office".
A 24-hour bar below shows the Amsterdam working day (09:00-18:00) and the Ho Chi Minh City working day (09:00-18:00) converted to the visitor's local time, with the overlap highlighted in gradient and labelled "Shared hours". Calculate the time difference dynamically (6 hours in winter, 5 in summer).
Copy: "Ho Chi Minh City is {difference} hours ahead of Amsterdam. Your team starts its day while Amsterdam is still asleep, and your morning is shared time for calls and reviews."
Next to it, one real team photo (uploaded by me) with a small white proof card overlay: "Herengracht 420, Amsterdam" and the Amsterdam office photo if available.

=== SECTION 5: HOW IT WORKS (id="how") ===
Mist background. Title: "From question to team in four steps." Four steps connected by an SVG line that DRAWS ITSELF as the visitor scrolls (path length tied to scroll progress, framer-motion useScroll). Each step's numbered gradient dot lights up when the line reaches it:
1. "Send your team brief": "Three taps and a short form. We contact you within one working day."
2. "Intro meeting": "We learn your goals, your technology stack and your timeline."
3. "Your team": "We propose the team composition and approach that fit your project."
4. "Start and scale": "Development starts, and your team grows with your needs."
CTA at the end of the line: "Start with step 1" (scrolls to #brief).

=== SECTION 6: WHAT USUALLY WORRIES TEAMS (id="worries") ===
White. Title: "Worried about working with a remote team? Tap a card." Four flip cards (3D flip on tap/click/Enter, flip back on second tap; under reduced motion show front and back stacked):
- Front "Will the time difference slow us down?" → Back "Ho Chi Minh City is a few hours ahead. Work moves on before your day starts, and your mornings are shared hours."
- Front "Who is accountable?" → Back "Management sits in our Amsterdam headquarters at Herengracht 420. You always have a European point of contact."
- Front "Will it feel like our own team?" → Back "\"It felt as if the Manifera developers were our own employees.\" Paul Booij, Co-founder and CTO, MO Batteries"
- Front "Can you show real work?" → Back "160 applications for 120 global clients since 2014. See two of them below."
Below the cards: primary button "Build your team brief".

=== SECTION 7: AI, BUT SAFE (id="ai") ===
Mist background. For variant "saas" move this section directly after the proof band (before the builder) so the visitor sees it first.
Title: "AI and how it helps you." Two cards:
- "AI-assisted development": "Our experienced software developers use AI during development to speed up delivery, while our long software development experience keeps the quality high. We use AI in alignment with our clients, and on request we use local AI models, so no information ends up in public AI models (LLMs)."
- "AI solutions": "We also build AI into web and mobile applications as part of the solution for your business case, to make your internal and external processes more efficient."
CTA: "Add an AI engineer to your brief" (scrolls to #brief, opens step 2 and adds one "AI integration engineer").

=== SECTION 8: WORK AND WORDS (id="work") ===
White. Title: "Results our clients talk about."
Two case cards, each with a product screenshot in a phone or browser frame (placeholder if I have not uploaded it), the client logo and one line:
- Vodafone Fiji: "Built and launched the online marketplace vitikart.com.fj on Magento with Vodafone Fiji's cloud architecture."
- MO Batteries: "Delivered the front end of a fleet-management platform, built in parallel with the client's own back-end team."
Then a swipeable testimonial carousel (drag on mobile, arrows on desktop, autoplay off), large quote cards with the company logo, no generated faces:
- "It was efficient and productive to work with the Manifera project team, and their technical skills in eCommerce development and software development showed!" Rizvi Amith, Manager Digital Business, Vodafone
- "Working with Manifera feels like having our own in-house development team." Maarten Diepenmaat, Co-founder, Statler
- "Timelines were met according to plan and the team is highly knowledgeable. I can highly recommend working with Manifera!" Arnold Tijdens, Founder and CEO, Kilimo
Link "See all work" → https://www.manifera.com/portfolio/ (new tab).

=== SECTION 9: FAQ (id="faq") ===
Mist background. shadcn Accordion:
- "What engagement models do you offer?" → A dedicated remote team for the long run, a project team for your bespoke web or mobile application, extra developers for a few months at around 20 to 40 hours per week, or DevOps engineers to keep your system running.
- "Where are your developers based?" → Our engineering hub is in Ho Chi Minh City, Vietnam, with management from our Amsterdam headquarters and an office in Singapore.
- "Which technologies do you work with?" → React / Node, Laravel / PHP, Magento, native and hybrid mobile apps, and DevOps.
- "Can you build AI into our SaaS without our data reaching public AI models?" → Yes. We use AI in alignment with our clients, and on request we use local AI models, so no information ends up in public AI models (LLMs).
- "How do we get started?" → Send your team brief above and we will contact you within one working day.
Add FAQPage JSON-LD for these questions in index.html.

=== SECTION 10: FINAL CTA (cosmic black band) ===
H2: "Your team is one brief away." Sub: "Tell us what you are building. We will contact you within one working day."
Button: "Build your team brief", or "Finish your team brief (step X of 4)" if a saved brief exists. Next to it: "Or call Amsterdam: +31 619 70 10 01" (tel: link).

=== FOOTER (minimal, cosmic black) ===
White logo. Three office blocks:
NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam · +31 619 70 10 01
VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City · +84 28 66522286
SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842
Phone numbers are tel: links. Links: "manifera.com" (https://www.manifera.com/), Privacy Policy (https://www.manifera.com/privacy-policy/), both in a new tab. Bottom line: "Copyright © 2026 Manifera Software Development Pte. Ltd."

=== CONVERSION RULES ===
- Every primary CTA scrolls to #brief. Nothing sends the visitor away except the footer, portfolio and privacy links (new tab).
- Mobile sticky bottom bar after the hero: left shows progress "Team brief · step X of 4" (or "Takes about 60 seconds" before the visitor starts), right a primary button "Continue" / "Start". Hide it while #brief is in view.
- Desktop only, once per session: a polite exit-intent card sliding in from the bottom right: "Your team brief is saved. Finish it in under a minute?" (or "Leaving already? Build your team brief in about 60 seconds." if not started), with one button and a close icon. Never on mobile, never on load.
- No fake countdowns, no fake "people viewing", no autoplay video, no sound.
- Never use the words "cheap", "low cost" or "best". No em dashes in any copy.

=== PERFORMANCE & SEO ===
- The hero is text plus the CSS chat card, so LCP must stay under 2.0s on mobile. Lazy-load every image below the fold, WebP, explicit width and height. Keep the JS bundle small: lazy-load canvas-confetti and the testimonial carousel.
- IMPORTANT: ChatGPT reads the landing page to decide ad placement and its crawler may not run JavaScript. Prerender the "/" route at build time (default variant) so the full text of every section is in the initial HTML. If prerendering is not possible, add a <noscript> block in index.html with the H1, sub-headline, the four how-it-works steps, the AI section and the FAQ as plain text.
- One H1 only, then a logical H2/H3 order.
- Title: "Manifera | Your Dedicated Software Team, Managed from Amsterdam" (adjust to stay under 60 characters). Meta description: "A dedicated engineering team in Ho Chi Minh City, managed from Amsterdam. 160 applications built since 2014. Build your team brief in 60 seconds."
- Open Graph tags with a 1200x630 share image (Team Pass visual + logo).
- Organization JSON-LD: name, url https://www.manifera.com, logo, foundingDate 2014, the three addresses with phone numbers.
- robots.txt allows all crawlers (including GPTBot, OAI-SearchBot and ChatGPT-User). Canonical = the page URL without query parameters. Do not add noindex.
```

---

## Prompt 2: Form backend

```
Connect the Team Brief form to Lovable Cloud (Supabase).
1. Create a table "ad_leads" with: id (uuid), created_at, name, work_email, company, country, message, heard_from, project_type, roles (jsonb, e.g. {"backend":2,"frontend":1}), team_size (int, null when "Manifera to advise"), team_advise (bool), start_when, variant (default|vendor|team|saas), page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref, user_agent, is_free_email (bool).
2. On first page load, read utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref and ag from the URL and keep them in sessionStorage (first-touch wins within the session). Attach them to the submission. Never drop the oppref parameter.
3. Enable RLS: anonymous users may INSERT only. No public SELECT, UPDATE or DELETE.
4. Edge function on insert: email the lead to the sales inbox (address in a secret SALES_EMAIL, never in client code). Subject: "New ChatGPT Ads lead: {company} ({country}) · team {team_size} · start {start_when}". Body: every field in a readable table, plus the roles as a list. Optional secret WEBHOOK_URL: if set, also POST the lead as JSON there (for the CRM).
5. Spam protection server-side: honeypot, math answer, and rate-limit by IP (max 5 submissions per hour).
6. Friendly error state: keep everything the visitor entered and show "Something went wrong. Try again" with a retry button, plus the Amsterdam phone number as a fallback.
```

## Prompt 3: Tracking and cookie consent

```
Add GDPR-compliant tracking.
1. Cookie consent banner (bottom, small, not blocking the page): "We use cookies to measure our ads and improve this page." Buttons "Accept" and "Reject" with equal visual weight, plus a "Cookie settings" link in the footer to change the choice later.
2. Google Analytics 4 with measurement ID G-ZGH74C8BL4 via gtag.js, using Consent Mode v2: default all denied, update to granted on Accept.
3. OpenAI Ads pixel: create src/lib/openaiPixel.ts with init() and trackLead(value?) functions. Leave a clearly marked spot where I will paste the official pixel snippet from OpenAI Ads Manager → Conversions. Load it only after Accept. When consent is given, also store oppref in a first-party cookie "mf_oppref" (30 days, SameSite=Lax, Secure).
4. Events (send to GA4 via gtag and to the dataLayer):
   - form_submit_contact (PRIMARY, fire ONLY after the lead is saved successfully, once per brief): params variant, project_type, team_size, start_when, country. Also call openaiPixel.trackLead() at this moment.
   - phone_call_click {office: nl|vn|sg} on every tel: link
   - email_click on every mailto: link
   - brief_start (first tap in the builder), brief_step {step: 1-4}, brief_skip_to_form
   - cta_click {cta_text, section}
   - chat_replay, worry_card_flip {card}, exit_intent_shown, exit_intent_click
   - scroll_depth at 50% and 90%
5. Do not send names, emails or company names to GA4 or the pixel.
```

## Prompt 4: Motion and polish

```
Polish pass:
- Section reveals: fade up 12px, 0.4s, stagger 0.06, once per element. Nothing moves more than that except the signature moments (chat card, avatar pops, Team Pass, scroll-drawn line, stamp and confetti).
- Primary buttons: subtle "magnetic" effect on desktop (moves max 4px towards the cursor), a short press-down scale (0.98) on tap.
- Team Builder: tap feedback on every card and chip within 100ms; avatar tokens use a spring (stiffness 400, damping 20); the team-size number rolls like an odometer.
- Under prefers-reduced-motion: no typing animation, no marquee, no travelling dot, no confetti, no magnetic buttons; show the final states.
- Check every colour pair for WCAG AA. Magenta never as small text on white.
- Test at 360px, 390px, 768px, 1280px and 1536px. No horizontal scroll. Every tap target at least 44px. The builder must be fully usable with one thumb on a 360px screen, and the on-screen keyboard must not cover the active form field.
- Test inside an in-app browser size (390x700) because ChatGPT opens links in an in-app browser.
```

## Prompt 5: QA checklist

```
Run a final QA and fix the issues:
- ?ag=vendor, ?ag=team, ?ag=saas, utm_content=ag1-a / ag2-b / ag3-c and no parameter each show the correct question, H1, sub-headline and pre-selected step 1. ?ag=saas moves the AI section up.
- The chat card plays once, Replay works, reduced motion shows the final state.
- The builder saves progress in localStorage, restores it with the "Welcome back" toast, "Skip to the form" works, and the Team Pass updates live.
- A test submission saves to ad_leads with all UTM fields and oppref, sends the email, shows the success stamp, fires form_submit_contact exactly once and clears the saved brief.
- With consent rejected, GA4 and the OpenAI pixel send nothing; with consent accepted, both fire.
- View the page source: the full text of the page is present in the initial HTML (prerender or noscript).
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100. Report the scores and fix the biggest issues.
- No invented numbers, promises, client names or prices; no "cheap", "low cost", "best"; no em dashes; no ChatGPT or OpenAI branding on the page.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

### Link quảng cáo cho từng ad group
Cả 3 ad group dùng chung 1 trang. Chỉ khác tham số `ag` và UTM (theo quy ước ở §4 của plan):

| AG | Final URL (ví dụ với domain `go.manifera.com`) |
|---|---|
| AG1 | `https://go.manifera.com/?ag=vendor&utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-vendor-eu&utm_content=ag1-a` |
| AG2 | `https://go.manifera.com/?ag=team&utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-team-eu&utm_content=ag2-a` |
| AG3 | `https://go.manifera.com/?ag=saas&utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-saas-eu&utm_content=ag3-a` |

Đổi `utm_content` thành `-b`, `-c` cho từng mẫu quảng cáo. `oppref` do OpenAI tự gắn thêm vào.

### Việc cần làm ngoài Lovable
- **Domain:** gắn trang vào subdomain của Manifera (ví dụ `go.manifera.com` hoặc `team.manifera.com`) qua DNS, không dùng `*.lovable.app`. Người dùng sẽ tin hơn, và trang được ChatGPT xem là của manifera.com. Link quảng cáo phải trỏ thẳng tới URL cuối cùng để `oppref` không bị mất qua redirect.
- **Pixel OpenAI:** lấy snippet trong Ads Manager → Conversions rồi dán vào chỗ Lovable chừa sẵn (Prompt 3). Gửi 1 lead thử trước 19/12, đúng như checklist §4.
- **Consent:** ở EU, ai bấm "Reject" thì pixel không đếm được. Vì vậy số chuyển đổi trong Ads Manager sẽ thấp hơn thực tế. Mỗi lead vẫn được lưu kèm UTM và `oppref` trong bảng `ad_leads`, nên hãy đối chiếu lead bằng bảng này (đúng phương án dự phòng "đếm lead thủ công" ở §14).
- **Ảnh cần tải lên Lovable:** logo màu và logo trắng, logo khách hàng (Vodafone, Statler, Kilimo, MO Batteries, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham), 1 ảnh team thật, ảnh văn phòng Amsterdam (nếu có), ảnh chụp màn hình vitikart.com.fj và MO Batteries. Danh sách đường dẫn có trong [`homepage-lovable-prompt.md`](./homepage-lovable-prompt.md) mục "Ảnh cần chuẩn bị".

### Khác với prompt trang chủ
- Prompt trang chủ cố ý **không** dùng quiz hay form nhiều bước để giữ đúng form liên hệ của manifera.com. Landing page quảng cáo thì cần quiz, vì 2 lý do: (1) bạn muốn trang vui, giữ chân người xem; (2) plan cần các trường "team size", "start date", "country", "How did you hear about us" để chấm lead đạt chuẩn (§2, §4). Vẫn có link "Skip to the form" cho người không muốn chơi.
- Không có menu và không có trang /thank-you: trang chỉ có 1 lối ra là gửi brief.

### Cần cập nhật trong plan (nếu bạn đồng ý)
- §4 bảng Landing pages và §5 cột Landing page: thay 3 trang dịch vụ WordPress bằng trang AG0 này.
- §4 mục AG3 "không có trang SaaS/AI": trang này giải quyết luôn, vì biến thể `?ag=saas` có nội dung SaaS/AI và đưa mục AI lên đầu.
- §4 Tracking: sự kiện `form_submit_contact` bắn khi lưu lead thành công (thay cho `wpcf7mailsent` của Contact Form 7). Bỏ `portfolio_view` vì trang không có portfolio riêng.
