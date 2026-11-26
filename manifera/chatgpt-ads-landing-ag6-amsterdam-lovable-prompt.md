# ChatGPT Ads Landing Page AG6 (Netherlands local, Amsterdam): Prompt for Lovable (EN only, 1 page)

> **Cách dùng:** dán **Prompt 1** vào một project Lovable mới. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 5**.
> **Ad group:** [`chatgpt_ads_plan_manifera.md`](./chatgpt_ads_plan_manifera.md) chưa có AG6. Mình lấy **AG6 Netherlands Local** trong [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) §3 (persona A và C ở Hà Lan; câu hỏi kiểu "software development company in Amsterdam", "software companies in the Netherlands"). Chỉ nhắm **Netherlands**.
> **Nguồn câu chữ:** trang chủ, Offshore teams, Setting Up Your Team, Migration to NL/Euro Cloud (đọc lại ngày 26/11/2026). Trang vẫn viết **tiếng Anh**, vì manifera.com chỉ có tiếng Anh.
> ⚠️ **Không dùng:** "Dutch contracts", "euro invoicing", "EU data hosting" (§8.1 của `paid_ads_plan.md` gợi ý nhưng không có trên site; pháp nhân trên site lại là Manifera Software Development **Pte. Ltd.**, công ty Singapore).

---

## Ý tưởng chính (cho bạn, không dán vào Lovable)

| # | Ý tưởng | Vì sao hiệu quả |
|---|---|---|
| 1 | **Dãy nhà kênh đào Amsterdam** (SVG) ở hero: căn số **420** sáng đèn từng ô cửa, có thuyền trôi trên kênh. Chạm vào căn 420 thì cửa mở ra, hiện thẻ giới thiệu team | Người Hà Lan nhận ra ngay hình ảnh quen thuộc. Địa chỉ Herengracht 420 là lợi thế không ai sao chép được |
| 2 | **Thanh cuộn hình con kênh**: một chiếc thuyền nhỏ chạy theo tiến độ cuộn trang và cập bến ở căn "420" | Chi tiết vui, nhắc người xem rằng cuối trang là đích đến |
| 3 | **Bản đồ Hà Lan bấm được**: chọn thành phố thì ghim rơi xuống, một đường vẽ về Herengracht 420 kèm "X km from our office" (Amsterdam thì hiện "Practically neighbours") | Cá nhân hóa ngay từ bước đầu, đồng thời thu được vị trí để chấm lead |
| 4 | **Thẻ hẹn kiểu gạch men Delft** (viền hoa văn màu xanh thương hiệu) cập nhật trực tiếp: FROM thành phố → TO Herengracht 420 | Dễ nhớ, đậm chất Hà Lan |
| 5 | **"Meet your team in person"**: một thành viên trong team có thể làm việc tại văn phòng khách hàng một thời gian (câu này có trên trang Setting Up Your Team) | Trả lời nỗi lo "team ở xa" theo cách rất hợp với khách địa phương |

---

## Prompt 1: Main build

```
Build a ONE-PAGE, English-only landing page for Manifera, a software development company with headquarters at Herengracht 420 in Amsterdam, an engineering hub in Ho Chi Minh City (Vietnam) and an office in Singapore. Visitors are in the Netherlands and arrive from ads inside ChatGPT after asking something like "Which software development companies are there in Amsterdam?" or "Software company in the Netherlands to build our platform?". They are founders, CTOs and IT managers of Dutch companies. The page has ONE job: get them to complete a playful "Plan a first conversation" brief that ends in the contact form.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react, framer-motion, canvas-confetti (lazy-loaded). ONE route only ("/"); success appears in place. Mobile-first (375px first). Use the exact copy below. Do not invent numbers, promises, client names or prices. Never claim Dutch contracts, euro invoicing or a Dutch legal entity.

=== DESIGN SYSTEM (same as manifera.com) ===
CSS variables in index.css, mapped in tailwind.config:
--white #FFFFFF · --mist #F5F6FA · --cosmic #05060F · --logo-navy #0F0F3C · --blue #1E5CC8 · --magenta #CD37A5 · --body #3D4257 · --muted #6B7086 · --line #E6E8F0 · plus --canal #DCE7F7 (very light blue for water, illustration only) and --brick #F3E9E1 (warm light tone for facades, illustration only).
Ratio about 70% white/mist, 15% cosmic, 10% blue, 5% magenta. Magenta never on buttons, body text or small text on white.
Signature: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5) for small accents only: one underlined word in the H1, the progress bar, the "420" window glow, the stamp.
Fonts: "Space Grotesk" headings (H1 40-44px mobile / 60-68px desktop), "Inter" body (17px, line-height 1.6).
Buttons: primary solid blue, white text, rounded-xl, arrow icon, min height 52px on mobile. Secondary white with a 1px cosmic/15% border.
Cards: white, 1px --line border, rounded-2xl, shadow 0 8px 30px rgba(5,6,15,0.06).
Illustration style: flat, thin cosmic outlines (1.5px), brand blue accents, no gradients except the 420 glow. Never clip-art, never stock photos of windmills or tulips.
Accessibility: WCAG AA, blue focus rings, semantic landmarks, every choice is a real <button> with aria-pressed, full keyboard support (the map has a list fallback), and every animation has a static version under prefers-reduced-motion.

=== HEADER (minimal, no navigation) ===
Sticky white header, 1px --line border after scrolling. Colour logo left (not a link). Right: primary button "Plan a first conversation" (short "Let's talk" under 380px) → #brief.
CANAL PROGRESS BAR: instead of a plain progress bar, the bottom edge of the header is a thin light-blue "canal" line; a tiny boat icon (12px) moves along it with scroll progress and docks at a tiny "420" canal-house icon at the right end when the visitor reaches #brief. Under reduced motion, a plain gradient bar.

=== SECTION 1: HERO (id="hero") ===
Desktop: text left, illustration right. Mobile: text first, illustration under it (cropped to three houses with 420 in the middle).
Left:
- Eyebrow with gradient dot: "Herengracht 420 · Amsterdam · Since 2014"
- H1: "Your software development company on the <gradient-underline>Herengracht</gradient-underline>."
- Sub: "Dutch management in Amsterdam, engineering in Ho Chi Minh City. Custom software, dedicated teams and migration to a Dutch cloud, for companies across the Netherlands."
- Primary CTA "Plan a first conversation" → #brief. Secondary link "See our work" → #work.
- Micro line: "About 60 seconds. We will contact you within one working day."
Right: the CANAL HOUSE SCENE, the signature moment (SVG). A row of six narrow Amsterdam canal-house facades with different gables (step gable, neck gable, bell gable, spout gable), tall windows, a canal in front with soft ripples, a bridge railing at one end and two parked bikes. One house carries the number "420" on its door and a tiny Manifera mark on the gable.
Animation on load: the windows of house 420 light up one by one (warm glow with a subtle gradient) over 1.5s; a small canal boat drifts slowly from left to right (loop every 20s); the water ripples gently.
Interaction: house 420 has a pointer cursor and a "Tap 420" hint chip. On tap or Enter its double door swings open and a small card pops out: "Inside: Manifera HQ. Dutch management, engineering hub in Ho Chi Minh City, office in Singapore." with the button "Plan a first conversation". Tapping elsewhere closes it.
Under reduced motion: house 420 is lit, no boat movement, the door card opens without animation.

=== SECTION 2: PROOF BAND (cosmic black, faint navy glow) ===
Counters that count up once: "160" Applications · "120" Global clients · "30" Experts and growing · "2014" Since. Slow grayscale logo marquee "Some of our clients and partners": TNO, Statler, Kilimo, MO Batteries, CFLW, Upkeepa, Hestec, Loggix, Vodafone, ADB DutchCham (uploaded logos only, otherwise names in white text). Pause on hover and under reduced motion.

=== SECTION 3: PLAN A FIRST CONVERSATION (id="brief"), the core of the page ===
Mist background. Title: "Plan a first conversation". Sub: "Four taps and a short form. We will take it from there."
Desktop: builder left (60%), live MEETING TILE preview right (40%, sticky). Mobile: builder full width, the tile as a compact strip above the buttons that expands on tap.
Progress bar with dots: "You" · "Need" · "Meet" · "Start" · "Send". Save selections in localStorage and restore with the toast "Welcome back, your plan is saved". Quiet link: "Prefer to just write to us? Skip to the form".

STEP 1 "Where is your company?"
A simplified SVG map of the Netherlands (clean outline, provinces not needed) with tappable city pins: Amsterdam, Amstelveen, Haarlem, Zaanstad, Hilversum, Utrecht, Leiden, Den Haag, Rotterdam, Eindhoven, Groningen; plus two buttons under the map: "Elsewhere in the Netherlands" and "Outside the Netherlands". A visually simple list of the same options is shown for keyboard and screen-reader users.
Tapping a pin: the pin drops with a bounce, a dotted line draws from it to a "Herengracht 420" pin, and a label appears with the straight-line distance (haversine from hard-coded coordinates; Herengracht 420 = 52.3667, 4.8890):
- under 5 km: "Practically neighbours."
- 5 to 40 km: "{X} km from our office. A short trip."
- over 40 km: "{X} km from our office, or one video call away."
Auto-advance 900ms after the label appears.

STEP 2 "What do you need?" (single select, auto-advance):
"A new platform or product" · "A dedicated team" · "Migration to a Dutch cloud" · "A web or mobile app" · "Something else".

STEP 3 "How would you like to meet first?" (single select, auto-advance):
"Video call" · "At our office on the Herengracht" · "Phone call".

STEP 4 "When would you like to start?" (pills, auto-advance): "As soon as possible" · "Within 3 months" · "In 3 to 6 months" · "Just exploring for now".

STEP 5 "Where should we reach you?" (react-hook-form + zod):
- Name (required) · Work email (required; for free email domains show "A work email helps us prepare the conversation", but allow it) · Company (required) · City (pre-filled from step 1, editable) · Phone (optional, only shown when "Phone call" was chosen) · Anything else we should know? (optional textarea, placeholder "Your product, your team, a link, anything that helps.") · How did you hear about us? (ChatGPT, Google, LinkedIn, Recommendation, Other; pre-select ChatGPT when utm_source=chatgpt) · Human check "What is 4 + 3?" (random) + hidden honeypot.
- Full-width submit: "Send my plan"
- Muted text: "We will contact you within one working day. By sending this form you agree to our Privacy Policy." (https://www.manifera.com/privacy-policy/, new tab)

THE MEETING TILE (preview card): a square card styled like a Delft tile: white with a thin brand-blue ornamental border and small corner flourishes drawn in SVG (blue only, no other colours). Inside, rows that fill in live with a soft flip: FROM {city} · TO Herengracht 420, Amsterdam · ABOUT {need} · HOW {meeting} · WHEN {start}. A mini route line at the bottom shows the distance from step 1.

SUCCESS STATE (in place): the tile moves to the centre, a gradient stamp "PLAN RECEIVED" lands on it, the little boat in the header docks at 420 with a tiny bounce, one short blue/magenta confetti burst (none under reduced motion).
H3 "Dank je wel, {first name}. Your plan is with us."
"We will contact you within one working day. Prefer to talk now? Call our Amsterdam office: +31 619 70 10 01" (tel: link). Clear the saved plan.

=== SECTION 4: DUTCH MANAGEMENT, VIETNAMESE ENGINEERING (id="team") ===
White. Title: "Dutch management. Vietnamese engineering. One team."
Left: two stacked photos (uploaded): the Amsterdam office on the Herengracht with the label "Amsterdam · HQ and management", and the Ho Chi Minh City office with "Ho Chi Minh City · Engineering hub". Overlay a small portrait card: real photo of Herre Roelevink, "Herre Roelevink, Founder & CEO".
Right:
- LIVE CLOCKS: Amsterdam and Ho Chi Minh City (Intl.DateTimeFormat, Europe/Amsterdam and Asia/Ho_Chi_Minh, updating every second), with the line "Ho Chi Minh City is {difference} hours ahead. Your team starts its day while Amsterdam is still asleep, and your morning is shared time for calls and reviews." (difference calculated: 6 in winter, 5 in summer).
- Three short points with blue icons:
  "English, every day": "Our software developers are very experienced and well versed in English speaking and writing."
  "Daily rhythm": "Daily or weekly standups and regular demos, with a release every 2 to 4 weeks."
  "Meet your team in person": "If you like, one of your team members can work at your office for a period, then share what they learned with the rest of the team."
Button: "Plan a first conversation".

=== SECTION 5: WHAT WE DO FOR DUTCH COMPANIES (id="services") ===
Mist background. Title: "What can we build for you?" Four tiles; tapping a tile expands it with one more line and a button "Add to my plan" (sets step 2 and scrolls to #brief):
- "Dedicated remote teams": "Your own dedicated team of experienced software developers, working as an extended team of your company." More: "Start from one engineer and scale up or down."
- "Custom-made solutions": "From UI/UX design, via development, all the way to deployment and service and maintenance." More: "Agile Scrum, with a release every 2 to 4 weeks."
- "Web and mobile apps": "Laravel / PHP, React / Node, Ruby on Rails, Python / Django, native and hybrid mobile apps." More: "Integrations like Mollie, PayPal, Xero and Intercom."
- "Migration to a Dutch cloud": "We bring your applications and data to a Dutch cloud provider, together with our partner Bitscloud." More: "From analysis to management."

=== SECTION 6: WORK AND WORDS (id="work") ===
White. Title: "Results our clients talk about."
A video card placeholder: "See a Manifera team in action for our client CFLW Cyber Strategies" (I will upload the video; until then show a poster placeholder with a play icon; never autoplay).
Two case cards (screenshot in a frame, placeholder if missing):
- MO Batteries: "Delivered the front end of a fleet-management platform, built in parallel with the client's own back-end team."
- Vodafone Fiji: "Built and launched the online marketplace vitikart.com.fj on Magento with Vodafone Fiji's cloud architecture."
Swipeable testimonial cards (company logos, no generated faces, no autoplay):
- "Working with Manifera feels like having our own in-house development team." Maarten Diepenmaat, Co-founder, Statler
- "It felt as if the Manifera developers were our own employees." Paul Booij, Co-founder and CTO, MO Batteries
- "Timelines were met according to plan and the team is highly knowledgeable. I can highly recommend working with Manifera!" Arnold Tijdens, Founder and CEO, Kilimo

=== SECTION 7: FIND US (id="visit") ===
Mist background. A wide card: a simple SVG mini-map of the Amsterdam canal ring (stylised arcs of the Singel, Herengracht, Keizersgracht and Prinsengracht) with a pulsing pin on the Herengracht. Next to it: "Herengracht 420, 1017 BZ Amsterdam" · "+31 619 70 10 01" (tel: link) · a secondary button "Open in Maps" (https://www.google.com/maps/search/?api=1&query=Herengracht+420+Amsterdam, new tab). Do not embed Google Maps (no third-party cookies).

=== SECTION 8: FAQ (id="faq") ===
White, shadcn Accordion, plus FAQPage JSON-LD in index.html:
- "Where are you based?" → Our headquarters are at Herengracht 420, 1017 BZ Amsterdam. Our engineering hub is in Ho Chi Minh City, Vietnam, and we have an office in Singapore.
- "Can we meet in person?" → Tell us in your plan how you would like to meet first. If you like, one of your team members can also work at your office for a period.
- "Do your developers work in English?" → Yes. Our software developers are very experienced and well versed in English speaking and writing.
- "Can our data stay in the Netherlands?" → Yes. With our Migration to NL/Euro Cloud service we bring your applications and data to a Dutch cloud provider.
- "Can you work alongside our own developers?" → Yes. Our engineers can work closely together with your own team, or independently on a complete project for your company.
- "How do we get started?" → Plan a first conversation above. We will contact you within one working day.

=== SECTION 9: FINAL CTA (cosmic black band with a faint canal-house silhouette row along the bottom) ===
H2: "Coffee on the Herengracht, or a video call?" Sub: "Tell us what you are building. We will contact you within one working day."
Button "Plan a first conversation", or "Finish your plan (step X of 5)" when a saved plan exists. Next to it: "Or call Amsterdam: +31 619 70 10 01".

=== FOOTER (minimal, cosmic black) ===
White logo. NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam · +31 619 70 10 01 · VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City · +84 28 66522286 · SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842 (tel: links). Links (new tab): "manifera.com", "Privacy Policy". "Copyright © 2026 Manifera Software Development Pte. Ltd."

=== CONVERSION RULES ===
- Every primary CTA scrolls to #brief. Only footer, privacy and "Open in Maps" links leave the page (new tab).
- Mobile sticky bottom bar after the hero: "Your plan · step X of 5" (or "Takes about 60 seconds") + "Continue" / "Start", and a call icon (tel:+31619701001). Hidden while #brief is in view.
- Desktop only, once per session: exit-intent card bottom right: "Your plan is saved. Finish it in under a minute?" (or "Leaving already? Plan a first conversation in about 60 seconds."). Never on mobile, never on load.
- No fake countdowns, no fake "people viewing", no autoplay video, no sound.
- Never "cheap", "low cost" or "best"; never "Dutch contracts", "euro invoicing" or "Dutch company" as a legal claim. No em dashes. No ChatGPT or OpenAI branding. English only (the one Dutch phrase allowed is "Dank je wel" in the success message).

=== PERFORMANCE & SEO ===
- LCP under 2.0s on mobile: the hero is text plus an inline SVG; photos only below the fold, lazy-loaded, WebP.
- Prerender "/" at build time so all text is in the initial HTML; otherwise add a <noscript> block in index.html with the H1, sub, the address, the team section text, the four services and the FAQ.
- One H1. Title: "Manifera | Software Development Company in Amsterdam". Meta description: "Software partner at Herengracht 420, Amsterdam, with engineering in Ho Chi Minh City. 160 applications built since 2014. Plan a first conversation."
- Open Graph 1200x630 image (canal houses with 420 lit + logo). Organization and LocalBusiness JSON-LD for the Amsterdam office (name, url, logo, foundingDate 2014, address Herengracht 420, 1017 BZ Amsterdam, NL, geo 52.3667/4.8890, telephone +31619701001), plus the other two offices as Organization addresses.
- robots.txt allows all crawlers, including GPTBot, OAI-SearchBot and ChatGPT-User. Canonical without query parameters. No noindex.
```

---

## Prompt 2: Form backend

```
Connect the form to Lovable Cloud (Supabase).
1. Table "ad_leads": id (uuid), created_at, landing (text, always "ag6-amsterdam"), name, work_email, company, city, phone, message, heard_from, brief (jsonb: city_pin, distance_km, need, meeting, start_when), page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref, user_agent, is_free_email (bool).
2. On first load, read utm_* and oppref from the URL, keep them in sessionStorage (first touch wins) and attach them to the submission. Never drop oppref.
3. RLS: anonymous INSERT only. No public SELECT, UPDATE or DELETE.
4. Edge function on insert: email the lead to the secret SALES_EMAIL. Subject: "New ChatGPT Ads lead (Amsterdam): {company}, {city} · {need} · meet by {meeting} · start {start_when}". Body: all fields in a readable table. Optional secret WEBHOOK_URL: also POST the lead as JSON.
5. Server-side spam checks: honeypot, math answer, rate limit 5 per IP per hour.
6. On error keep all input, show "Something went wrong. Try again" with retry and the Amsterdam phone number.
```

## Prompt 3: Tracking and cookie consent

```
Add GDPR-compliant tracking.
1. Small cookie banner: "We use cookies to measure our ads and improve this page." "Accept" and "Reject" with equal weight; "Cookie settings" link in the footer. Self-host the fonts so nothing third-party loads before Accept.
2. GA4 G-ZGH74C8BL4 via gtag.js with Consent Mode v2 (default denied, granted on Accept).
3. src/lib/openaiPixel.ts with init() and trackLead(); marked spot for the official OpenAI Ads pixel snippet. Load only after Accept. After Accept, store oppref in first-party cookie "mf_oppref" (30 days, SameSite=Lax, Secure).
4. Events (gtag + dataLayer):
   - form_submit_contact (PRIMARY, only after a successful save, once): landing, city_pin, need, meeting, start_when. Also call openaiPixel.trackLead().
   - phone_call_click {office}, email_click, maps_click
   - brief_start, city_pick {city, distance_km}, brief_step {step}, brief_skip_to_form
   - house_420_open, service_tile_open {service}, cta_click {cta_text, section}, exit_intent_shown, exit_intent_click, scroll_depth 50/90
5. Never send names, emails, phone numbers or company names to GA4 or the pixel.
```

## Prompt 4: Motion and polish

```
Polish pass:
- Section reveals: fade up 12px, 0.4s, stagger 0.06, once. Only the signature moments move more (420 windows, boat, door, canal progress boat, map pin and route, tile flips, stamp).
- Keep the SVG scene light: under 40 KB, no filters except one soft glow on the 420 windows; pause the boat loop when the hero is out of view.
- Map: pins have 44px invisible tap areas even though they look small; the route line draws in 600ms.
- Primary buttons: subtle magnetic effect on desktop (max 4px), press scale 0.98.
- Under prefers-reduced-motion: static scene, no boat, no pin bounce, no confetti.
- WCAG AA everywhere. Test at 360, 390, 768, 1280, 1536px and a 390x700 in-app browser viewport. No horizontal scroll, keyboard never covers the active field.
```

## Prompt 5: QA checklist

```
Final QA, fix what fails:
- House 420 opens and closes by tap, click and keyboard.
- The header boat follows scroll and docks at 420 at #brief and again on success.
- Every city pin shows the right distance band (Amsterdam = "Practically neighbours", Rotterdam about 57 km, Groningen about 147 km); the list fallback works with keyboard and screen reader.
- The phone field only appears for "Phone call"; city pre-fills from the map.
- Saved plan survives a reload; "Skip to the form" works; "Add to my plan" on service tiles sets step 2.
- A test lead saves to ad_leads with UTM fields and oppref, sends the email, shows the stamp, fires form_submit_contact once and clears the saved plan.
- Consent rejected: no GA4 or pixel calls and no third-party requests. Accepted: both fire.
- Page source contains the full text (prerender or noscript); LocalBusiness JSON-LD validates.
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100.
- No invented numbers, promises or legal claims; no "cheap", "low cost", "best", "Dutch contracts", "euro invoicing"; no em dashes; no ChatGPT or OpenAI branding.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

- **Link quảng cáo** (ví dụ `amsterdam.manifera.com`): `https://amsterdam.manifera.com/?utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-nl-local&utm_content=ag6-a`. Campaign chỉ nhắm **Netherlands**.
- ⚠️ **Cần xác nhận với ban lãnh đạo:**
  1. Khách có thể đến gặp ở văn phòng Herengracht 420 không? Nếu không, bỏ lựa chọn "At our office on the Herengracht" ở bước 3 và đổi tiêu đề cuối trang.
  2. Đồng ý cho dùng logo khách hàng (TNO, Statler, Kilimo, MO Batteries, CFLW…) và video CFLW trong quảng cáo trả tiền.
- **Đánh số ad group:** plan ChatGPT và plan Google đánh số AG khác nhau (bên Google: AG4 = Mobile, AG5 = Cost, AG6 = NL Local). Bộ file này theo plan ChatGPT cho AG3-5, còn AG6 lấy từ plan Google. Nếu bạn muốn AG6 là chủ đề khác (ví dụ Mobile app), báo mình để viết lại.
- **Ảnh cần tải lên:** ảnh văn phòng Herengracht (bên ngoài và bên trong), ảnh văn phòng Hồ Chí Minh, chân dung Herre Roelevink (bản lớn hơn 400px), logo khách hàng, video CFLW, ảnh chụp màn hình MO Batteries và vitikart.com.fj.
