# ChatGPT Ads Landing Page AG3 (AI-powered SaaS product engineering): Prompt for Lovable (EN only, 1 page)

> **Cách dùng:** dán **Prompt 1** vào một project Lovable mới. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 5**, mỗi lần một prompt.
> **Ad group:** AG3 trong [`chatgpt_ads_plan_manifera.md`](./chatgpt_ads_plan_manifera.md) §5 (persona C: founder hoặc product lead của công ty SaaS, 5-200 nhân viên). Trang này thay cho `/services/web-app-develop/` (trang đó không có chữ SaaS hay AI nào).
> **Nguồn câu chữ:** trang chủ, trang Offshore teams, Web app development, Our Way of Working trên manifera.com (đọc lại ngày 26/11/2026). Không thêm số liệu hay lời hứa nào khác.

---

## Ý tưởng chính (cho bạn, không dán vào Lovable)

| # | Ý tưởng | Vì sao hiệu quả |
|---|---|---|
| 1 | **Thanh kéo "Prototype ⇄ Product"** ở hero: bên trái là bản prototype nguệch ngoạc với giấy nhớ ("TODO: login", "API key in the code?"), kéo sang phải thành dashboard SaaS hoàn chỉnh | Founder có prototype AI nhìn thấy ngay chính sản phẩm của mình. Kéo tay nên người xem phải tương tác ngay giây đầu |
| 2 | **"Stack your SaaS"**: chọn tính năng, mỗi khối rơi xuống và xếp chồng thành "tòa tháp sản phẩm", có cắm cờ tên công ty | Vui như xếp hình. Đồng thời thu được giai đoạn sản phẩm, tính năng, lựa chọn mô hình AI, thời điểm bắt đầu |
| 3 | **Thẻ code "AI viết, kỹ sư duyệt"**: dòng code AI hiện mờ, một reviewer sửa lại rồi đóng dấu "Reviewed by an experienced engineer" | Trả lời nỗi lo về chất lượng code AI bằng đúng câu có trên site |
| 4 | **Công tắc "Local model ⇄ Public model"**: dữ liệu ở trong hộp hoặc bay ra cloud | Biến cam kết dùng local model thành hình ảnh dễ nhớ |
| 5 | **Đường release vẽ theo cuộn trang** (v0.1, v0.2…) | Minh họa "release mỗi 2-4 tuần" có trên site |

---

## Prompt 1: Main build

```
Build a ONE-PAGE, English-only landing page for Manifera, a software development company with headquarters in Amsterdam, an engineering hub in Ho Chi Minh City (Vietnam) and an office in Singapore. Visitors arrive from ads inside ChatGPT, mostly on mobile, after asking something like "Which company can build our AI-powered SaaS product?" or "How do I turn our AI prototype into a real product?". They are SaaS founders and product leads at companies of 5 to 200 people. The page has ONE job: get them to complete a playful "Stack your SaaS" brief that ends in the contact form.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react icons, framer-motion, canvas-confetti (lazy-loaded). ONE route only ("/"). No other pages, no thank-you route: success appears in place. Mobile-first (design at 375px first). Use the exact copy below. Do not invent numbers, promises, client names or prices.

=== DESIGN SYSTEM (same as manifera.com) ===
CSS variables in index.css, mapped in tailwind.config:
--white #FFFFFF · --mist #F5F6FA · --cosmic #05060F · --logo-navy #0F0F3C · --blue #1E5CC8 · --magenta #CD37A5 · --body #3D4257 · --muted #6B7086 · --line #E6E8F0.
Ratio about 70% white/mist, 15% cosmic, 10% blue, 5% magenta. Magenta never on buttons, body text or small text on white.
Signature: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5) for small accents only: one underlined word in the H1, the builder progress bar, the stamp, small eyebrow dots.
Fonts: "Space Grotesk" headings (H1 40-44px mobile / 60-68px desktop, tight tracking), "Inter" body (17px, line-height 1.6).
Buttons: primary solid blue, white text, rounded-xl, arrow icon, min height 52px on mobile. Secondary white with a 1px cosmic/15% border.
Cards: white, 1px --line border, rounded-2xl, shadow 0 8px 30px rgba(5,6,15,0.06).
Accessibility: WCAG AA, visible blue focus rings, semantic landmarks, every choice is a real <button> with aria-pressed, full keyboard support, and every animation has a static version under prefers-reduced-motion.

=== HEADER (minimal, no navigation) ===
Sticky white header, 1px --line border after scrolling. Colour Manifera logo left (not a link). Right: compact primary button "Talk to our team" → #brief. A 3px gradient scroll-progress bar along the header's bottom edge.

=== SECTION 1: HERO (id="hero") ===
Two columns on desktop, stacked on mobile (text first).
Left:
- Eyebrow with gradient dot: "SaaS product engineering · Managed from Amsterdam · Since 2014"
- H1: "From AI <gradient-underline>prototype</gradient-underline> to a SaaS product your customers use."
- Sub: "A dedicated product engineering team for your SaaS, managed from Amsterdam. We build AI into your product, and on request we use local AI models, so your data stays out of public LLMs."
- Primary CTA "Stack your SaaS" → #brief. Secondary text link "See how we build" → #build.
- Micro line: "About 60 seconds. We will contact you within one working day."
Right: the PROTOTYPE ⇄ PRODUCT SLIDER, the signature moment. A card (rounded-2xl, 4:3) containing two layered UI mock-ups built in HTML/SVG (no images):
- Left layer "Prototype": a sketchy wireframe in pencil grey with rough, hand-drawn borders and 4 yellow sticky notes, slightly rotated: "TODO: login", "API key in the code?", "Works on my laptop", "Billing… later".
- Right layer "Product": a clean SaaS dashboard in brand colours (sidebar, chart, user table, an "Ask AI" box) with 4 small labels that pop in as they are revealed: "Accounts and roles", "Subscriptions and billing", "AI assistant", "Tests and monitoring".
- A vertical drag handle (blue circle with ⇄ icon) splits the layers. On load it slides once 50% → 25% → 75% → 50% to invite dragging, with a small chip "Drag me". Keyboard: arrow keys move it. Under reduced motion it stays at 50%.
- Labels above the card corners: "Your prototype" (left), "Your product" (right).

=== SECTION 2: PROOF BAND (cosmic black with a faint logo-navy radial glow) ===
Four counters that count up once on view: "160" Applications · "120" Global clients · "30" Experts and growing · "2014" Since. Below, a slow grayscale logo marquee labelled "Some of our clients and partners": Vodafone, Statler, Kilimo, MO Batteries, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham. Use only logos I upload; otherwise show the name in white text. Pause on hover and under reduced motion.

=== SECTION 3: STACK YOUR SAAS (id="brief"), the core of the page ===
Mist background. Title: "Stack your SaaS". Sub: "Pick what your product needs and watch it grow. Send it to us when it looks right."
Desktop: builder left (60%), live PRODUCT TOWER preview right (40%, sticky inside the section). Mobile: builder full width, the tower as a compact strip above the step buttons that expands on tap.
Gradient progress bar with 5 labelled dots: "Stage" · "Features" · "AI and team" · "Start" · "Send". Steps slide horizontally (250ms). "Back" link on steps 2-5. Save selections in localStorage and restore them with a toast "Welcome back, your stack is saved".
Under the title a quiet link: "Prefer to just write to us? Skip to the form" → jumps to step 5.

STEP 1 "Where are you now?" (single select, auto-advance after 300ms):
- "An idea and a plan"
- "An AI prototype or MVP"
- "A live SaaS, adding AI"
- "A live SaaS, need more engineers"

STEP 2 "What does your product need?" Feature blocks (multi select, each with a lucide icon):
Accounts, roles and permissions · Multi-tenant workspaces · Subscriptions and billing · AI assistant or copilot · AI on your documents or data · Integrations (Mollie, PayPal, Xero, Intercom, MailChimp and more) · Admin dashboard and reporting · Mobile app (native or hybrid) · DevOps, hosting and monitoring.
Plus a toggle "Not sure yet, advise me".
Pre-select from step 1: idea → accounts, admin dashboard, subscriptions; prototype → accounts, subscriptions, DevOps; live adding AI → AI assistant, AI on your data; need engineers → nothing (show hint "Pick the areas your new engineers will work on").
FUN DETAIL: each selected block drops into the tower preview from above with a little gravity bounce and stacks on the others (framer-motion spring, stiffness 500, damping 22). Deselecting pops the block out and the tower settles. A counter reads "Your stack: 6 building blocks". When the company name is typed in step 5, a small flag with that name appears on top of the tower.

STEP 3 "AI and team" (two rows of single-select cards on one screen):
Row A "How should AI handle your data?": "Local AI models: data stays out of public LLMs" · "Public AI models are fine" · "Not sure, advise me".
Row B "How should we work with you?": "Alongside our own developers" · "As our complete product team" · "Not sure yet".
Continue button: "Looks good".

STEP 4 "When would you like to start?" (pills, auto-advance): "As soon as possible" · "Within 3 months" · "In 3 to 6 months" · "Just exploring for now".

STEP 5 "Where should we send your stack?" (react-hook-form + zod):
- Name (required)
- Work email (required, valid; for gmail/hotmail/outlook/yahoo/icloud show the hint "A work email helps us prepare for the call", but allow it)
- Company (required)
- Country (required select: Netherlands, Belgium, Germany, Other EU/EEA country, United Kingdom, Switzerland, Other)
- Link to your prototype or product (optional URL)
- Anything else we should know? (optional textarea, placeholder "Your users, your stack, the AI feature you have in mind.")
- How did you hear about us? (select: ChatGPT, Google, LinkedIn, Recommendation, Other; pre-select ChatGPT when utm_source=chatgpt)
- Human check "What is 4 + 3?" (random numbers per load) plus a hidden honeypot
- Full-width submit: "Send my SaaS stack"
- Small muted text: "We will contact you within one working day. By sending this form you agree to our Privacy Policy." (https://www.manifera.com/privacy-policy/, new tab)

THE PRODUCT TOWER (preview card): the stacked blocks, and under them four rows that fill in live with a soft flip: STAGE · AI DATA · TEAM SETUP · START. At the bottom a small strip "A release every 2 to 4 weeks" with a row of tiny release dots (decorative).

SUCCESS STATE (in place): the builder slides away, the tower moves to the centre, the flag on top waves once, a gradient stamp "STACK RECEIVED" lands on the card (scale 1.4 → 1, slight rotation), then one short confetti burst in blue and magenta (none under reduced motion).
H3 "Thank you, {first name}. Your SaaS stack is with us."
"We will contact you within one working day. Prefer to talk now? Call our Amsterdam office: +31 619 70 10 01" (tel: link). Clear the saved stack.

=== SECTION 4: AI, REVIEWED BY ENGINEERS (id="ai") ===
White. Title: "AI speeds us up. Engineers sign it off."
Left: an animated CODE CARD (dark cosmic card, monospace): a few lines of code; a new line types itself in faint grey "ghost text" (the AI suggestion), then a small reviewer token slides in, two characters get struck through and replaced, and a blue badge appears: "Reviewed by an experienced engineer". Loops every 8 seconds while in view; static final frame under reduced motion.
Right, three blocks:
- "AI-assisted development": "We use AI in various steps of the development cycle, assisting our experienced engineers with user stories, requirements, code and test cases. Every AI-generated deliverable is reviewed by an experienced software engineer."
- "Your data, your choice": an interactive switch "Local models ⇄ Public models". Local: small data dots circle inside a box labelled "Your environment". Public: the dots travel out to a cloud labelled "Public AI model". Caption: "We use local or public models, depending on your wishes. On request we use local AI models, so no information ends up in public AI models (LLMs)."
- "AI in your product": "We build AI into web and mobile applications as part of the solution for your business case, to make your internal and external processes more efficient."
CTA: "Add AI to my stack" → #brief, opens step 2 and selects "AI assistant or copilot".

=== SECTION 5: HOW WE BUILD (id="build") ===
Mist background. Title: "How your SaaS gets built." A horizontal "release track" (vertical on mobile) drawn by an SVG line that grows with scroll (framer-motion useScroll). Small version markers "v0.1", "v0.2", "v0.3", "v1.0" pop up along the line as decoration. Four steps light up when the line reaches them:
1. "Your first ideas and requirements": "We take it from your first wishes and briefing, via development, all the way to a smooth roll-out."
2. "Plan and budget estimation": "Based on the information you share, we prepare a plan and a budget estimation."
3. "A release every 2 to 4 weeks": "Agile Scrum with sprints, daily or weekly standups and regular demos. Each release adds functionality."
4. "Live, then growing": "After going live we support you with Service and Maintenance and DevOps, and keep adding features."
Callout card under the track: "Want to test the collaboration first? A pilot project is possible." + button "Stack your SaaS".

=== SECTION 6: WHAT WE BUILD WITH (id="stack") ===
White. Title: "Technologies we build with." Rounded chips that float very gently (2px, slow) and lean towards the cursor on desktop:
Languages and frameworks: React / Node · Laravel / PHP · Ruby on Rails · Python / Django · React Native · Swift · Kotlin.
Cloud: Amazon Web Services · Microsoft Azure · Google Cloud.
Integrations: Mollie · PayPal · Xero · Intercom · MailChimp.
Line under the chips: "Start from one engineer and scale up or down: developers, test engineers, DevOps, and a Project Manager or Scrum Master when you need one."

=== SECTION 7: WORK AND WORDS (id="work") ===
Mist background. Title: "Teams that felt like their own."
Two case cards with a screenshot in a browser or phone frame (placeholder if not uploaded), client logo and one line:
- MO Batteries: "Delivered the front end of a fleet-management platform, built in parallel with the client's own back-end team."
- Vodafone Fiji: "Built and launched the online marketplace vitikart.com.fj on Magento with Vodafone Fiji's cloud architecture."
Swipeable testimonial carousel (no autoplay, company logos, no generated faces):
- "The technical discussions were of high quality and truly collaborative to create the best back-end/front-end interaction. It felt as if the Manifera developers were our own employees." Paul Booij, Co-founder and CTO, MO Batteries
- "Working with Manifera feels like having our own in-house development team." Maarten Diepenmaat, Co-founder, Statler
- "We were very positively surprised by the proactive approach, the intuitive UI/UX design and the speed of development by the Manifera team. We went live as planned, before the planned date!" Berend van Geffen, Director

=== SECTION 8: FAQ (id="faq") ===
White, shadcn Accordion, plus FAQPage JSON-LD in index.html:
- "Can you work alongside our own developers?" → Yes. Our engineers can work on a project closely together with your own team, or independently on a complete project for your company.
- "Which AI models do you use?" → Local or public models, depending on your wishes. On request we use local AI models, so no information ends up in public AI models (LLMs).
- "How often will we see progress?" → We work Agile Scrum and deliver a release every 2 to 4 weeks, each time adding functionality, with regular demos.
- "Can we start small?" → Yes. You can start with one engineer and scale up or down, and a pilot project is possible first.
- "How is our IP protected?" → We take IP protection and data security seriously: we sign an NDA and follow the GDPR.
- "How do we get started?" → Send your SaaS stack above and we will contact you within one working day.

=== SECTION 9: FINAL CTA (cosmic black band) ===
H2: "Ready to turn the prototype into a product?" Sub: "Tell us what you are building. We will contact you within one working day."
Button "Stack your SaaS", or "Finish your stack (step X of 5)" when a saved stack exists. Next to it: "Or call Amsterdam: +31 619 70 10 01".

=== FOOTER (minimal, cosmic black) ===
White logo. NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam · +31 619 70 10 01 · VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City · +84 28 66522286 · SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842. Phone numbers are tel: links. Links (new tab): "manifera.com", "Privacy Policy" (https://www.manifera.com/privacy-policy/). "Copyright © 2026 Manifera Software Development Pte. Ltd."

=== CONVERSION RULES ===
- Every primary CTA scrolls to #brief. Only the footer and privacy links leave the page (new tab).
- Mobile sticky bottom bar after the hero: "Your stack · step X of 5" (or "Takes about 60 seconds") + button "Continue" / "Start". Hidden while #brief is in view.
- Desktop only, once per session: a polite exit-intent card bottom right: "Your SaaS stack is saved. Finish it in under a minute?" (or "Leaving already? Stack your SaaS in about 60 seconds."), one button and a close icon. Never on mobile, never on load.
- No fake countdowns, no fake "people viewing", no autoplay video, no sound.
- Never use "cheap", "low cost" or "best" in our own copy (client quotes stay word for word). No em dashes in any copy. No ChatGPT or OpenAI branding.

=== PERFORMANCE & SEO ===
- LCP under 2.0s on mobile: the hero is text plus HTML/SVG mock-ups, no large images. Lazy-load everything below the fold.
- ChatGPT reads the landing page to decide ad placement and may not run JavaScript: prerender "/" at build time so all text is in the initial HTML. If that is not possible, add a <noscript> block in index.html with the H1, sub-headline, the AI section, the four build steps and the FAQ as plain text.
- One H1. Title: "Manifera | AI-Powered SaaS Product Engineering Team". Meta description: "From AI prototype to a SaaS product your customers use. A dedicated product engineering team, managed from Amsterdam. 160 applications since 2014."
- Open Graph 1200x630 image (prototype/product split visual + logo). Organization JSON-LD (name, url https://www.manifera.com, logo, foundingDate 2014, three addresses with phones).
- robots.txt allows all crawlers, including GPTBot, OAI-SearchBot and ChatGPT-User. Canonical without query parameters. No noindex.
```

---

## Prompt 2: Form backend

```
Connect the form to Lovable Cloud (Supabase).
1. Table "ad_leads": id (uuid), created_at, landing (text, always "ag3-ai-saas"), name, work_email, company, country, product_url, message, heard_from, brief (jsonb: stage, features[], ai_data, team_setup, advise_features bool), start_when, page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref, user_agent, is_free_email (bool).
2. On first load, read utm_source, utm_medium, utm_campaign, utm_term, utm_content and oppref from the URL and keep them in sessionStorage (first touch wins). Attach them to the submission. Never drop oppref.
3. RLS: anonymous users may INSERT only. No public SELECT, UPDATE or DELETE.
4. Edge function on insert: email the lead to the secret SALES_EMAIL (never in client code). Subject: "New ChatGPT Ads lead (AI SaaS): {company} ({country}) · {stage} · start {start_when}". Body: every field in a readable table, features as a list. Optional secret WEBHOOK_URL: also POST the lead as JSON there (CRM).
5. Server-side spam checks: honeypot, math answer, rate limit 5 per IP per hour.
6. On error keep all input, show "Something went wrong. Try again" with a retry button and the Amsterdam phone number.
```

## Prompt 3: Tracking and cookie consent

```
Add GDPR-compliant tracking.
1. Small cookie banner at the bottom: "We use cookies to measure our ads and improve this page." Buttons "Accept" and "Reject" with equal weight, plus a "Cookie settings" link in the footer.
2. GA4 G-ZGH74C8BL4 via gtag.js with Consent Mode v2 (default denied, granted on Accept).
3. src/lib/openaiPixel.ts with init() and trackLead(); a clearly marked spot for the official OpenAI Ads pixel snippet from Ads Manager → Conversions. Load only after Accept. After Accept, also store oppref in a first-party cookie "mf_oppref" (30 days, SameSite=Lax, Secure).
4. Events (gtag + dataLayer):
   - form_submit_contact (PRIMARY, only after a successful save, once): landing, stage, feature_count, ai_data, start_when, country. Also call openaiPixel.trackLead().
   - phone_call_click {office}, email_click
   - brief_start, brief_step {step}, brief_skip_to_form
   - slider_drag (first drag of the hero slider), ai_switch_toggle {state}, cta_click {cta_text, section}, exit_intent_shown, exit_intent_click, scroll_depth 50/90
5. Never send names, emails or company names to GA4 or the pixel.
```

## Prompt 4: Motion and polish

```
Polish pass:
- Section reveals: fade up 12px, 0.4s, stagger 0.06, once. Only the signature moments move more (hero slider, falling blocks, code card, AI switch, release track, stamp, confetti).
- Hero slider: smooth on touch (pointer events, no page scroll while dragging horizontally), 60fps, handle at least 44px.
- Primary buttons: subtle magnetic effect on desktop (max 4px), press scale 0.98.
- Under prefers-reduced-motion: no auto-slide, no falling blocks (blocks appear in place), no typing, no marquee, no confetti.
- WCAG AA on every colour pair. Test at 360, 390, 768, 1280 and 1536px and in a 390x700 in-app browser viewport. No horizontal scroll, tap targets at least 44px, the keyboard never covers the active field.
```

## Prompt 5: QA checklist

```
Final QA, fix what fails:
- The hero slider works with mouse, touch and keyboard, and the auto-slide plays once.
- Step 1 pre-selects the right features; blocks stack and unstack; the company name flag appears; the stack survives a reload; "Skip to the form" works.
- "Add AI to my stack" opens step 2 with the AI assistant selected.
- A test lead saves to ad_leads with UTM fields and oppref, sends the email, shows the stamp, fires form_submit_contact once and clears the saved stack.
- Consent rejected: GA4 and pixel send nothing. Accepted: both fire.
- Page source contains the full text (prerender or noscript).
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100.
- No invented numbers, promises, client names or prices; no "cheap", "low cost", "best" outside client quotes; no em dashes; no ChatGPT or OpenAI branding.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

- **Link quảng cáo** (ví dụ domain `saas.manifera.com`): `https://saas.manifera.com/?utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-saas-eu&utm_content=ag3-a`. Đổi `-a` thành `-b`, `-c` cho từng mẫu quảng cáo.
- **Trùng với AG0:** trang AG0 có biến thể `?ag=saas`. Chọn 1 trong 2 cho AG3. Trang riêng này sâu hơn nên phù hợp hơn khi AG3 nhận ≥ 35% ngân sách (§11 của plan).
- **NDA:** §3 của plan ghi "NDA on request" không có trên site. Thực ra trang Offshore teams có câu "signing an NDA and following the GDPR", nên FAQ dùng đúng câu đó. Nên sửa lại §3.
- **Không dùng** [`case_studies.md`](./case_studies.md): các case trong đó không có tên khách và các con số (45%, 0% turnover…) không có trên site.
- **Ảnh cần tải lên:** logo màu và trắng, logo khách hàng, ảnh chụp màn hình MO Batteries và vitikart.com.fj (cần khách đồng ý).
