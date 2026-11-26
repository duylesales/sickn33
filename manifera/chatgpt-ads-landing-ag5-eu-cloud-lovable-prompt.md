# ChatGPT Ads Landing Page AG5 (Migration to a Dutch/European cloud): Prompt for Lovable (EN only, 1 page)

> **Cách dùng:** dán **Prompt 1** vào một project Lovable mới. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 5**.
> **Ad group:** AG5 "cloud migration" trong §11 của [`chatgpt_ads_plan_manifera.md`](./chatgpt_ads_plan_manifera.md) (persona D: IT Director, CTO hoặc chủ doanh nghiệp SME đang host trên Azure hoặc trên cloud ngoài EU).
> **Nguồn câu chữ:** trang [Migration to NL/Euro Cloud](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) (đọc lại ngày 26/11/2026): hợp tác Manifera × Bitscloud, kinh nghiệm của Sven van den Burg, "From analysis to management", "completely unburdened or keep control", đối tác Microsoft, TransIP, Leaseweb.
> ⚠️ **Không dùng:** "zero downtime", "100% GDPR compliant", "ISO…/NEN…" (câu trên site còn dở dang), và case HealthTech trong `case_studies.md` (không có tên khách, lại thuộc nhóm ngành sức khỏe bị hạn chế quảng cáo ở EU).

---

## Ý tưởng chính (cho bạn, không dán vào Lovable)

| # | Ý tưởng | Vì sao hiệu quả |
|---|---|---|
| 1 | **Bản đồ "hành trình dữ liệu"** ở hero: các gói dữ liệu bay theo vòng cung từ cloud hiện tại (ví dụ ở Mỹ) về một data center ở Hà Lan, đến nơi thì khóa lại | Vẽ ra đúng câu hỏi trong đầu người xem: dữ liệu của tôi đang nằm ở đâu |
| 2 | **"Moving day for your data"**: mỗi thứ cần chuyển (web app, database, file…) thành một thùng các-tông có nhãn, rơi vào thùng container. Xe tải chạy dần theo tiến độ | Biến một chủ đề khô khan thành chuyện "chuyển nhà" dễ hiểu. Đồng thời thu được hạ tầng hiện tại, quy mô, ưu tiên và thời điểm |
| 3 | **Công tắc "Completely unburdened ⇄ In control"** | Dựa trên câu có thật về "flexible management models". Người xem chọn luôn và lựa chọn được thêm vào brief |
| 4 | **Thẻ "United forces"** Manifera + Bitscloud, dấu "+" nhấp nháy | Kinh nghiệm Azure và Microsoft của Bitscloud là bằng chứng mạnh nhất của dịch vụ này |
| 5 | **Câu FAQ "Is this legal advice?"** | Giữ trang ở nhóm "IT services", tránh bị xếp vào nhóm dịch vụ pháp lý bị hạn chế quảng cáo ở EU |

---

## Prompt 1: Main build

```
Build a ONE-PAGE, English-only landing page for Manifera's "Migration to NL/Euro Cloud" service. Manifera is a software development company with headquarters in Amsterdam, an engineering hub in Ho Chi Minh City and an office in Singapore; this service is delivered in partnership with Bitscloud. Visitors arrive from ads inside ChatGPT after asking something like "How do we move our applications from a US cloud to a European cloud?" or "Can we host our Azure apps in a Dutch data center?". They are IT managers, CTOs and owners of small and medium-sized businesses in the Netherlands, Belgium and Germany. The page has ONE job: get them to complete a playful "Plan your move" brief that ends in the contact form.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react, framer-motion, canvas-confetti (lazy-loaded). ONE route only ("/"); success appears in place. Mobile-first (375px first). Use the exact copy below. Do not invent numbers, certifications, guarantees, client names or prices. Never claim "zero downtime" or "100% compliant".

=== DESIGN SYSTEM (same as manifera.com) ===
CSS variables in index.css, mapped in tailwind.config:
--white #FFFFFF · --mist #F5F6FA · --cosmic #05060F · --logo-navy #0F0F3C · --blue #1E5CC8 · --magenta #CD37A5 · --body #3D4257 · --muted #6B7086 · --line #E6E8F0.
Ratio about 70% white/mist, 15% cosmic, 10% blue, 5% magenta. Magenta never on buttons, body text or small text on white.
Signature: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5) for small accents only: one underlined word in the H1, the progress bar, the data-packet trail, the stamp.
Fonts: "Space Grotesk" headings (H1 40-44px mobile / 60-68px desktop), "Inter" body (17px, line-height 1.6).
Buttons: primary solid blue, white text, rounded-xl, arrow icon, min height 52px on mobile. Secondary white with a 1px cosmic/15% border.
Cards: white, 1px --line border, rounded-2xl, shadow 0 8px 30px rgba(5,6,15,0.06).
Accessibility: WCAG AA, blue focus rings, semantic landmarks, every choice is a real <button> with aria-pressed, full keyboard support, and every animation has a static version under prefers-reduced-motion.

=== HEADER (minimal, no navigation) ===
Sticky white header, 1px --line border after scrolling. Colour Manifera logo left (not a link), and next to it a small muted "in partnership with Bitscloud" (Bitscloud logo if uploaded). Right: primary button "Plan my move" → #brief. 3px gradient scroll-progress bar on the bottom edge.

=== SECTION 1: HERO (id="hero") ===
Two columns on desktop, stacked on mobile (text first).
Left:
- Eyebrow with gradient dot: "Migration to NL / Euro Cloud · Manifera × Bitscloud"
- H1: "Bring your applications and data <gradient-underline>home</gradient-underline> to a Dutch cloud."
- Sub: "From analysis to management, your Dutch and European migration partner. Your applications and data in a Dutch data center, with a cloud provider that follows the GDPR."
- Primary CTA "Plan my move" → #brief. Secondary link "How a migration works" → #how.
- Micro line: "About 60 seconds. We will contact you within one working day."
Right: the DATA JOURNEY, the signature moment. A card with a minimal dotted world map (SVG, no map library). Origin pin on the US east coast labelled "Your current cloud"; destination pin in the Netherlands labelled "Dutch data center". Along a curved arc, small rounded squares (icons: app, database, file) travel from origin to destination in a steady stream (one every 700ms, 2.4s per trip). On arrival each packet gets a tiny padlock and slots into a small server-rack icon that slowly fills. A caption under the map: "Applications and data, in the Netherlands." When the visitor picks a region in step 1 of the brief, the origin pin moves there (for example "An EU region of a non-European provider" moves it to Ireland, "Our own servers" turns it into a building icon). Under reduced motion: a static arc with three packets already at the destination.

=== SECTION 2: PROOF BAND (cosmic black, faint navy glow) ===
Counters that count up once: "160" Applications · "120" Global clients · "2014" Since · "15+" Years of Azure and Microsoft experience at Bitscloud. Under them a logo row labelled "Partners": Microsoft, TransIP, Leaseweb, Bitscloud (uploaded logos only, otherwise names in white text). No marquee here, just a calm row.

=== SECTION 3: PLAN YOUR MOVE (id="brief"), the core of the page ===
Mist background. Title: "Moving day for your data". Sub: "Tell us what runs where today. We take it from there."
Desktop: builder left (60%), live MOVING CRATE preview right (40%, sticky). Mobile: builder full width, the crate as a compact strip above the buttons that expands on tap.
Progress bar with dots: "Today" · "Pack" · "Priorities" · "Start" · "Send". Save selections in localStorage and restore with the toast "Welcome back, your moving plan is saved". Quiet link: "Prefer to just write to us? Skip to the form".

STEP 1 "Where do your applications run today?"
Cards (single select): "Microsoft Azure" · "Amazon Web Services" · "Google Cloud" · "Another cloud or hosting provider" · "Our own servers (on-premise)" · "Not sure".
Then region pills (single select, auto-advance): "Outside the EU, for example the US" · "An EU region of a non-European provider" · "Already with a European provider" · "Don't know".

STEP 2 "What needs to move?"
Chips (multi select, lucide icons): Web applications · Databases · File storage and documents · Microsoft applications · Internal tools · Websites or webshops · "Everything, or not sure".
Pills "How many applications?": "1 to 3" · "4 to 10" · "More than 10" · "Not sure".
FUN DETAIL: each selected chip becomes a labelled cardboard box (warm beige with a blue label and the icon) that drops into the open crate in the preview with a bounce; a strip of tape slides across it. Deselecting lifts the box out. Counter: "4 boxes packed".

STEP 3 "What matters most?" (choose up to two; a third tap gently shakes the cards and shows "Pick your top two"):
"Data in a Dutch data center" · "Working with a GDPR-compliant provider" · "Being completely unburdened" · "Keeping control in our own hands" · "Clear advice before we decide".

STEP 4 "When would you like to move?" (pills, auto-advance): "As soon as possible" · "Within 3 months" · "In 3 to 6 months" · "First an analysis, then we decide".

STEP 5 "Where should we send your moving plan?" (react-hook-form + zod):
- Name (required) · Work email (required; for free email domains show "A work email helps us prepare the analysis", but allow it) · Company (required) · Your role (optional select: IT manager, CTO, Owner or director, Other) · Country (required select: Netherlands, Belgium, Germany, Other EU/EEA country, United Kingdom, Switzerland, Other) · Anything else we should know? (optional textarea, placeholder "Your current setup, deadlines, contracts that end, anything that helps.") · How did you hear about us? (ChatGPT, Google, LinkedIn, Recommendation, Other; pre-select ChatGPT when utm_source=chatgpt) · Human check "What is 4 + 3?" (random) + hidden honeypot.
- Full-width submit: "Send my moving plan"
- Muted text: "We will contact you within one working day. By sending this form you agree to our Privacy Policy." (https://www.manifera.com/privacy-policy/, new tab)

THE MOVING CRATE (preview card): an open crate with the packed boxes; above it a route line "FROM {provider}, {region}" → "TO Dutch data center" with a small truck icon that moves along the line as the progress grows; rows below fill in live: APPLICATIONS · PRIORITIES · MANAGEMENT (from section 4, if chosen) · MOVE.

SUCCESS STATE (in place): the crate lid closes, tape seals it, a gradient sticker "PLAN RECEIVED" lands on the side, the truck drives to the NL pin; one short blue/magenta confetti burst (none under reduced motion).
H3 "Thank you, {first name}. Your moving plan is with us."
"We will contact you within one working day. Prefer to talk now? Call our Amsterdam office: +31 619 70 10 01" (tel: link). Clear the saved plan.

=== SECTION 4: UNBURDENED OR IN CONTROL? (id="manage") ===
White. Title: "Hands off, or hands on? Both work."
A large toggle switch with two labels: "Completely unburdened" ⇄ "Control in your own hands". Next to it an illustration of a four-layer stack (Applications · Data · Hosting · Monitoring):
- Unburdened: all four layers are blue with a small Manifera mark; caption "We take care of it, from analysis to management."
- In control: layers turn white with a cosmic outline and your-team icons; a thin blue "support" line runs alongside; caption "You keep control, we support where you need us."
The layers animate between states (400ms). Copy under it: "Thanks to our flexible management models, we offer customized solutions whether you want to be completely unburdened or prefer to keep control in your own hands."
Button: "Add this to my moving plan" (saves the choice to the brief and scrolls to #brief).

=== SECTION 5: HOW A MIGRATION WORKS (id="how") ===
Mist background. Title: "From analysis to management." Four steps placed along a curved route (the same arc style as the hero, drawn with scroll) from a "Today" pin to an "NL" pin; each step lights up when the line reaches it:
1. "Analysis": "With an independent view, we perform a thorough analysis of your applications, data and hosting."
2. "Advice": "Clear advice that fits your situation, before you commit to anything."
3. "Migration": "We bring your applications and data to a Dutch or European cloud provider, and guide you through every step."
4. "Management": "After the move, we keep your applications operational, as hands-off or hands-on as you want."
Line under it: "We have experience with cloud migrations from American to European environments." Button "Plan my move".

=== SECTION 6: UNITED FORCES (id="partners") ===
White. Title: "United forces." Two cards side by side joined by a "+" circle that pulses softly (static under reduced motion):
- Manifera: "Over 10 years of experience in building software applications, and in making and keeping them operational on various hosting platforms." Small facts: "Amsterdam HQ · 160 applications · Since 2014".
- Bitscloud: "With Sven van den Burg, among others, who has more than 15 years of experience as an Azure and Microsoft specialist at companies such as Rabobank, ProRail and the Dutch railways. Bitscloud knows the ins and outs of Microsoft applications and how to host them efficiently and securely."
Below: a "Who we help" card: "Are you a small or medium-sized business that hosts applications or stores data in Azure? Then we can help you migrate them to a Dutch cloud. We already help many customers with Azure hosting and migration questions."
Partner logos row: Microsoft, TransIP, Leaseweb (uploaded only).

=== SECTION 7: WHY A DUTCH DATA CENTER (id="why") ===
Mist background. Three flip cards (tap to flip; static stacked under reduced motion):
- Front "Where is our data, really?" → Back "Your applications and data, trusted in a Dutch data center."
- Front "What about GDPR?" → Back "We work with Dutch and European cloud providers that comply with the GDPR rules."
- Front "Who helps us after the move?" → Back "Local support and in-depth knowledge of European regulations and compliance requirements, from analysis to management."

=== SECTION 8: FAQ (id="faq") ===
White, shadcn Accordion, plus FAQPage JSON-LD in index.html:
- "We are on Azure. Can you help?" → Yes. We help many customers with Azure hosting and migration questions, together with our partner Bitscloud.
- "Have you done migrations from American to European environments?" → Yes. We have experience with cloud migrations from American to European environments and guide organizations through every step.
- "Which cloud providers do you migrate to?" → Dutch and European cloud providers. Our partners include TransIP and Leaseweb. We advise on the provider that fits your situation.
- "Do we have to hand over control?" → No. You can be completely unburdened, or keep control in your own hands with our support.
- "Is this legal advice about GDPR?" → No. We handle the technical analysis, advice, migration and management. For legal questions about GDPR, involve your legal adviser or data protection officer.
- "How do we get started?" → Send your moving plan above. We will contact you within one working day.

=== SECTION 9: FINAL CTA (cosmic black band) ===
H2: "Ready to bring your data home?" Sub: "Tell us what runs where today. We will contact you within one working day."
Button "Plan my move", or "Finish your moving plan (step X of 5)" when a saved plan exists. Next to it: "Or call Amsterdam: +31 619 70 10 01".

=== FOOTER (minimal, cosmic black) ===
White logo + "in partnership with Bitscloud". NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam · +31 619 70 10 01 · VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City · +84 28 66522286 · SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842 (tel: links). Links (new tab): "manifera.com", "Privacy Policy". "Copyright © 2026 Manifera Software Development Pte. Ltd."

=== CONVERSION RULES ===
- Every primary CTA scrolls to #brief. Only footer and privacy links leave the page (new tab).
- Mobile sticky bottom bar after the hero: "Your moving plan · step X of 5" (or "Takes about 60 seconds") + "Continue" / "Start". Hidden while #brief is in view.
- Desktop only, once per session: exit-intent card bottom right: "Your moving plan is saved. Finish it in under a minute?" (or "Leaving already? Plan your move in about 60 seconds."). Never on mobile, never on load.
- No fake countdowns, no fake "people viewing", no autoplay video, no sound. No fear-based copy about fines or data breaches.
- Never "cheap", "low cost" or "best"; never "zero downtime", "100% compliant", certification names or legal guarantees. No em dashes. No ChatGPT or OpenAI branding.

=== PERFORMANCE & SEO ===
- LCP under 2.0s on mobile: the hero is text plus an SVG map. Lazy-load below the fold.
- Prerender "/" at build time so all text is in the initial HTML; otherwise add a <noscript> block in index.html with the H1, sub, the four migration steps, the United forces text and the FAQ.
- One H1. Title: "Manifera | Migration to a Dutch or European Cloud". Meta description: "We bring your applications and data to a Dutch cloud provider. From analysis to management, together with Bitscloud. Plan your move in 60 seconds."
- Open Graph 1200x630 image (data-journey map + logo). Organization JSON-LD (name, url, logo, foundingDate 2014, three addresses with phones).
- robots.txt allows all crawlers, including GPTBot, OAI-SearchBot and ChatGPT-User. Canonical without query parameters. No noindex.
```

---

## Prompt 2: Form backend

```
Connect the form to Lovable Cloud (Supabase).
1. Table "ad_leads": id (uuid), created_at, landing (text, always "ag5-eu-cloud"), name, work_email, company, role, country, message, heard_from, brief (jsonb: provider, region, items[], app_count, priorities[], management), start_when, page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref, user_agent, is_free_email (bool).
2. On first load, read utm_* and oppref from the URL, keep them in sessionStorage (first touch wins) and attach them to the submission. Never drop oppref.
3. RLS: anonymous INSERT only. No public SELECT, UPDATE or DELETE.
4. Edge function on insert: email the lead to the secret SALES_EMAIL and, if set, to a second secret PARTNER_EMAIL (for Bitscloud). Subject: "New ChatGPT Ads lead (EU cloud): {company} ({country}) · {provider}, {region} · {app_count} apps · {start_when}". Body: all fields in a readable table. Optional secret WEBHOOK_URL: also POST the lead as JSON.
5. Server-side spam checks: honeypot, math answer, rate limit 5 per IP per hour.
6. On error keep all input, show "Something went wrong. Try again" with retry and the Amsterdam phone number.
```

## Prompt 3: Tracking and cookie consent

```
Add GDPR-compliant tracking (this page is about data protection, so it must be exemplary).
1. Small cookie banner: "We use cookies to measure our ads and improve this page." "Accept" and "Reject" with equal weight; "Cookie settings" link in the footer. No cookies or third-party requests at all before Accept, including fonts: self-host Space Grotesk and Inter.
2. GA4 G-ZGH74C8BL4 via gtag.js with Consent Mode v2 (default denied, granted on Accept).
3. src/lib/openaiPixel.ts with init() and trackLead(); marked spot for the official OpenAI Ads pixel snippet. Load only after Accept. After Accept, store oppref in first-party cookie "mf_oppref" (30 days, SameSite=Lax, Secure).
4. Events (gtag + dataLayer):
   - form_submit_contact (PRIMARY, only after a successful save, once): landing, provider, region, app_count, start_when, country. Also call openaiPixel.trackLead().
   - phone_call_click {office}, email_click
   - brief_start, brief_step {step}, brief_skip_to_form
   - management_toggle {state}, why_card_flip {card}, cta_click {cta_text, section}, exit_intent_shown, exit_intent_click, scroll_depth 50/90
5. Never send names, emails or company names to GA4 or the pixel.
```

## Prompt 4: Motion and polish

```
Polish pass:
- Section reveals: fade up 12px, 0.4s, stagger 0.06, once. Only the signature moments move more (data journey, boxes, truck, management stack, route line, crate closing).
- Data journey: use requestAnimationFrame or CSS offset-path; pause when the hero is out of view to save battery.
- Boxes: spring drop (stiffness 450, damping 20), tape strip 250ms.
- Primary buttons: subtle magnetic effect on desktop (max 4px), press scale 0.98.
- Under prefers-reduced-motion: static map, boxes appear in place, no truck movement, no confetti.
- WCAG AA everywhere. Test at 360, 390, 768, 1280, 1536px and a 390x700 in-app browser viewport. Tap targets at least 44px, no horizontal scroll, keyboard never covers the active field.
```

## Prompt 5: QA checklist

```
Final QA, fix what fails:
- Choosing a provider and region in step 1 moves the origin pin in the hero map and updates the crate route.
- Boxes pack and unpack; "pick your top two" works; the management toggle choice appears in the crate and in the saved lead.
- Saved plan survives a reload; "Skip to the form" works.
- A test lead saves to ad_leads with UTM fields and oppref, emails SALES_EMAIL (and PARTNER_EMAIL if set), shows the closing crate, fires form_submit_contact once and clears the saved plan.
- Before Accept, the network tab shows no third-party requests (no Google Fonts, no GA4, no pixel).
- Page source contains the full text (prerender or noscript).
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100.
- No "zero downtime", "100% compliant", certification names, invented numbers, prices or promises; no "cheap", "low cost", "best"; no em dashes; no ChatGPT or OpenAI branding.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

- **Link quảng cáo** (ví dụ `eu-cloud.manifera.com`): `https://eu-cloud.manifera.com/?utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-cloud-eu&utm_content=ag5-a`.
- **Bitscloud:** nên xin Bitscloud xác nhận trước khi chạy. Trang nêu tên Sven van den Burg và tên các công ty anh ấy từng làm (Rabobank, ProRail, Dutch railways). Các tên này có trên manifera.com, nhưng đưa vào quảng cáo trả tiền thì nên được đồng ý. Có thể thêm email của Bitscloud vào secret `PARTNER_EMAIL` để họ nhận lead cùng lúc.
- **Số "15+"** ở dải proof lấy từ câu "more than 15 years of experience" trên site, là kinh nghiệm của Sven tại Bitscloud, không phải của Manifera. Nếu thấy dễ gây hiểu nhầm thì thay bằng "30 Experts and growing".
- **Trang trên site còn câu chưa viết xong:** "complies with ISO…, NEN…". Nên sửa hoặc xóa trên manifera.com, vì ChatGPT cũng đọc trang đó.
- **Ngành hạn chế:** ở EU, ChatGPT Ads hạn chế dịch vụ pháp lý (§1 của plan). Vì vậy trang nói về GDPR như một yêu cầu kỹ thuật, và có câu FAQ "not legal advice".
- **Ảnh cần tải lên:** logo Manifera, logo Bitscloud, Microsoft, TransIP, Leaseweb (có sẵn trên trang migration, thư mục `/wp-content/uploads/2025/05/` và `/2026/05/`).
