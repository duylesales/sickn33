# ChatGPT Ads Landing Page AG4 (Cost and engagement models): Prompt for Lovable (EN only, 1 page)

> **Cách dùng:** dán **Prompt 1** vào một project Lovable mới. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 5**.
> **Ad group:** AG4 "cost/models" trong §11 của [`chatgpt_ads_plan_manifera.md`](./chatgpt_ads_plan_manifera.md) (giai đoạn mở rộng). Người xem là founder, CTO hoặc người giữ ngân sách, vừa hỏi ChatGPT kiểu "How much does a development team cost?" hoặc "Fixed price or time and materials?".
> **Nguồn câu chữ:** 4 mô hình hợp tác (kèm ưu và nhược điểm), quy trình 5 bước, pilot project và NDA đều lấy nguyên từ trang [Our Way Of Working](https://www.manifera.com/about-us/our-way-of-working/). Danh sách "những gì Manifera lo cho bạn" lấy từ trang Offshore teams và Setting Up Your Team (đọc lại ngày 26/11/2026).
> ⚠️ **Trang không có bảng giá**, vì manifera.com chưa công bố giá nào. Thay vào đó, trang hứa đúng điều có trên site: "we prepare a plan and a budget estimation".

---

## Ý tưởng chính (cho bạn, không dán vào Lovable)

| # | Ý tưởng | Vì sao hiệu quả |
|---|---|---|
| 1 | **Bộ bài 4 mô hình** được chia ra ở hero, kèm một lá úp "Your match?" | Ngay giây đầu đã cho thấy có 4 lựa chọn, và tò mò muốn lật lá úp |
| 2 | **Model Matcher**: 5 câu hỏi dạng thẻ quẹt (Yes / Not sure / No), bên cạnh là **4 thanh điểm "đua"** đổi thứ hạng sau mỗi câu trả lời | Người hỏi giá thật ra đang chưa biết chọn mô hình nào. Trò chơi trả lời câu đó rồi dẫn thẳng sang "Get my plan and budget estimation" |
| 3 | **Núm xoay giờ Vouchers** 80 / 120 / 160 giờ | Con số duy nhất có trên site, biến nó thành thứ có thể "vặn" |
| 4 | **Tảng băng chìm**: cuộn xuống thì mực nước hạ, lộ ra những việc Manifera lo (tìm người, thiết bị, quản lý chung, môi trường dev, scale…) | Nói về "chi phí ẩn" mà không cần đưa ra con số nào |
| 5 | **FAQ thẳng thắn "Why is there no price list?"** | Người xem cảm thấy được tôn trọng thay vì bị né câu hỏi |

---

## Prompt 1: Main build

```
Build a ONE-PAGE, English-only landing page for Manifera, a software development company with headquarters in Amsterdam, an engineering hub in Ho Chi Minh City (Vietnam) and an office in Singapore. Visitors arrive from ads inside ChatGPT, mostly on mobile, after asking something like "How much does a dedicated development team cost?" or "Fixed price or time and materials for our software project?". They are founders, CTOs and budget owners. This page does NOT show prices. Its ONE job: help them find the right engagement model through a playful matcher, then request a plan and budget estimation through the contact form.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react, framer-motion, canvas-confetti (lazy-loaded). ONE route only ("/"); success appears in place. Mobile-first (375px first). Use the exact copy below. Do not invent numbers, prices, promises or client names.

=== DESIGN SYSTEM (same as manifera.com) ===
CSS variables in index.css, mapped in tailwind.config:
--white #FFFFFF · --mist #F5F6FA · --cosmic #05060F · --logo-navy #0F0F3C · --blue #1E5CC8 · --magenta #CD37A5 · --body #3D4257 · --muted #6B7086 · --line #E6E8F0.
Ratio about 70% white/mist, 15% cosmic, 10% blue, 5% magenta. Magenta never on buttons, body text or small text on white.
Signature: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5) for small accents only: one underlined word in the H1, the progress bar, the winning match bar, the stamp.
Fonts: "Space Grotesk" headings (H1 40-44px mobile / 60-68px desktop), "Inter" body (17px, line-height 1.6).
Buttons: primary solid blue, white text, rounded-xl, arrow icon, min height 52px on mobile. Secondary white with a 1px cosmic/15% border.
Cards: white, 1px --line border, rounded-2xl, shadow 0 8px 30px rgba(5,6,15,0.06).
Accessibility: WCAG AA, blue focus rings, semantic landmarks, every choice is a real <button> with aria-pressed, full keyboard support (swipe gestures always have button equivalents), and every animation has a static version under prefers-reduced-motion.

=== HEADER (minimal, no navigation) ===
Sticky white header, 1px --line border after scrolling. Colour logo left (not a link). Right: primary button "Find my model" → #brief. 3px gradient scroll-progress bar on the bottom edge.

=== SECTION 1: HERO (id="hero") ===
Two columns on desktop, stacked on mobile (text first).
Left:
- Eyebrow with gradient dot: "Engagement models · Plan and budget estimation · Since 2014"
- H1: "What will your software team <gradient-underline>cost</gradient-underline>? Start with the right model."
- Sub: "Four ways to work with Manifera, each with honest pros and cons. Answer five quick questions, see which model fits, and we prepare a plan and a budget estimation for your project."
- Primary CTA "Find my model" → #brief. Secondary link "Compare the four models" → #models.
- Micro line: "About 60 seconds. We will contact you within one working day."
Right: THE DECK, the signature moment. Four model cards (white, rounded-2xl, each with an icon, the model name and a tiny tagline) are dealt onto a soft mist "table" on load (stagger 120ms, slight random rotation -6° to 6°), ending fanned out like a hand of cards:
- "Dedicated team" · "Your own extended team"
- "Vouchers" · "Hours per month, paid upfront"
- "Time and materials" · "Pay for real hours spent"
- "Fixed price" · "Budget and planning fixed"
In the centre lies a fifth card face-down with a gradient back and a "?" labelled "Your match?". Hover or tap lifts any card 8px. Tapping the face-down card scrolls to #brief. After the matcher is finished, this card flips to show the winning model. Under reduced motion the cards are shown static, already fanned.

=== SECTION 2: PROOF BAND (cosmic black, faint navy glow) ===
Counters that count up once: "160" Applications · "120" Global clients · "30" Experts and growing · "2014" Since. Slow grayscale logo marquee "Some of our clients and partners": Vodafone, Statler, Kilimo, MO Batteries, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham (uploaded logos only, otherwise names in white text).

=== SECTION 3: MODEL MATCHER (id="brief"), the core of the page ===
Mist background. Title: "Find your model in five questions". Sub: "No right or wrong answers. Every answer moves the bars."
Desktop: question cards left (55%), live MATCH BARS right (45%, sticky). Mobile: question card full width, a compact version of the bars above it.
Progress bar with dots: "Questions" · "Your match" · "Your project" · "Send". Save progress in localStorage and restore with the toast "Welcome back, your answers are saved". Quiet link under the title: "Prefer to just write to us? Skip to the form".

PART A: FIVE SWIPE CARDS. One card at a time, stacked with the next card peeking behind it. Each card has three big buttons: "Yes" · "Not sure" · "No". On touch you can also swipe right = Yes, left = No, up = Not sure; the card flies off in that direction with a slight rotation, and the next one moves up. Questions:
Q1 "Will there be a steady flow of work for your team for months?"
Q2 "Are your requirements clear and unlikely to change much?"
Q3 "Do you want the budget fixed before we start?"
Q4 "Do you want to manage the developers' daily work yourself?"
Q5 "Can you predict roughly how many development hours you need each month?"
SCORING (points for Yes / points for No; "Not sure" gives half of both):
Q1: Yes → Dedicated +3, Vouchers +1 · No → Time and materials +1, Fixed price +2
Q2: Yes → Fixed price +3, Vouchers +1 · No → Time and materials +3, Dedicated +1
Q3: Yes → Fixed price +3, Vouchers +1 · No → Time and materials +2, Dedicated +1
Q4: Yes → Dedicated +3, Vouchers +1 · No → Fixed price +1, Time and materials +1
Q5: Yes → Vouchers +3, Dedicated +1 · No → Time and materials +2, Fixed price +1
Match % per model = its score divided by its maximum possible score, rounded.
MATCH BARS: four horizontal bars with the model name and the %; after every answer the bars animate to their new width and RE-SORT with a smooth layout animation (framer-motion layout), so the leader rises to the top like a race. The leading bar uses the gradient; the others are blue at 25%.

PART B: YOUR MATCH. A result card expands with the winning model, a short "Best when…" line, its pros (+) and cons (−) from the #models section, and a secondary line with the runner-up: "Close second: {model} ({x}%)". Under it, small text: "As a flexible company, we can deviate from these models. Tell us your ideas about engagement." Confetti-free here; just the face-down card in the hero flips to the winner. Button: "Get my plan and budget estimation".

PART C: YOUR PROJECT (one screen):
- "What are you building?" cards: "A new platform or product" · "Extra capacity for my team" · "A web or mobile app" · "Something else"
- "How many people do you expect to need?" pills: "1" · "2 to 3" · "4 to 6" · "7 or more" · "Not sure"
- "When would you like to start?" pills: "As soon as possible" · "Within 3 months" · "In 3 to 6 months" · "Just exploring for now"
- Toggle: "I'd like to start with a pilot project"

PART D: SEND (react-hook-form + zod):
- Name (required) · Work email (required; for free email domains show "A work email helps us prepare your estimation", but allow it) · Company (required) · Country (required select: Netherlands, Belgium, Germany, Other EU/EEA country, United Kingdom, Switzerland, Other) · Anything else we should know? (optional textarea, placeholder "Scope, deadline, budget range, anything that helps.") · How did you hear about us? (ChatGPT, Google, LinkedIn, Recommendation, Other; pre-select ChatGPT when utm_source=chatgpt) · Human check "What is 4 + 3?" (random) + hidden honeypot.
- Full-width submit: "Request my plan and budget estimation"
- Muted text: "Based on your information we prepare a plan and a budget estimation. We will contact you within one working day. By sending this form you agree to our Privacy Policy." (https://www.manifera.com/privacy-policy/, new tab)

SUCCESS STATE (in place): the result card moves to the centre, a gradient stamp "REQUEST RECEIVED" lands on it, one short blue/magenta confetti burst (none under reduced motion).
H3 "Thank you, {first name}. We are on it."
"We will contact you within one working day to talk through your plan and budget estimation. Prefer to talk now? Call Amsterdam: +31 619 70 10 01" (tel: link). Clear the saved answers.

=== SECTION 4: COMPARE THE FOUR MODELS (id="models") ===
White. Title: "Four ways to work together." Desktop: four columns; mobile: segmented tabs with swipe. If the matcher is finished, the winning column gets a small gradient label "Your match". Use this exact copy:
1. "Offshore Software Development Team": "We set up a dedicated software development team for your projects at our offices. We take care of the general management of the team and provide the necessary equipment and tools. You and your team take care of the daily technical management of the team members."
   + "Your fixed and own dedicated team of experienced software developers, working as an extended team of your company."
   − "Enough work for the team needs to be available continuously to make this efficient, although flexible up and down scaling is provided."
   Best when: "there is continuous work for the team."
2. "Vouchers": "Vouchers for a set number of development hours per month: 80, 120 or 160 hours. Vouchers are paid upfront before the start of each month."
   + "The hours are committed by Manifera for the month they are purchased."
   − "It is not always possible to know how many hours you will need per month."
   Best when: "you can plan your hours per month."
   INTERACTIVE HOURS DIAL inside this column: a circular dial with three stops (80 · 120 · 160). Tap or drag to switch; the arc fills with the gradient and the centre number rolls to the new value. Caption: "{h} development hours per month." Under 160 add: "Roughly one developer full-time for a month."
3. "Time and Materials": "The budget is based on the development effort actually spent and 'materials' costs, like software libraries. During the quotation stage we provide an indicative expected budget based on your ideas and requirements."
   + "You only pay for the real hours spent and the materials used."
   − "Even with an indicative budget, the budget actually needed can be significantly different."
   Best when: "your requirements are not fully clear yet."
4. "Fixed Price Project": "Based on your ideas and requirements we provide a budget estimate and a planning. Both stay fixed as long as the requirements do not change significantly. The budget is paid in parts, linked to agreed milestones."
   + "The budget risk is out of your hands: the price is as agreed."
   − "This normally comes with a higher price, to cater for unforeseen activities."
   Best when: "the scope is clear and budget certainty matters most."
Button under the columns: "Find my model" → #brief.

=== SECTION 5: THE ICEBERG (id="included") ===
Mist background. Title: "With a dedicated team, this is what you don't have to arrange."
An SVG iceberg in a calm sea. Above the waterline a small label: "Your developers". As the visitor scrolls through the section, the water level drops (scroll-linked), revealing seven labelled items under the surface one by one, each with a blue check:
- "Finding the right developers, through our network if needed"
- "Equipment and tools"
- "General management of the team"
- "A development environment set up to match yours"
- "Training and briefings on your business and way of working"
- "Scaling up or down, from one engineer to many"
- "Test engineers, DevOps, a Project Manager or Scrum Master when you need them"
Side note card: "If you like, one of your team members can work at your office for a period, then share what they learned with the rest of the team."
Under reduced motion: the iceberg is static and the list is shown in full.

=== SECTION 6: HOW IT WORKS (id="how") ===
White. Title: "From first message to first release." Five steps on an SVG line that draws itself with scroll; each numbered gradient dot lights up when reached:
1. "Contact us": "Share your ideas or project details. We contact you within one working day."
2. "Consultation and discussion": "Based on what you share, we prepare a plan and a budget estimation."
3. "Contract": "Together we draw up a contract with the overall terms, prices and project schedule."
4. "Realization": "Agile Scrum, with a release every 2 to 4 weeks, each time adding functionality."
5. "Deployment, support and maintenance": "Once your software is live, we provide Service and Maintenance and add features as your business changes."
Callout: "Want to test us first? A pilot project is possible." + button "Find my model".

=== SECTION 7: WORDS (id="work") ===
Mist background. Title: "Plans that held." Swipeable testimonial cards (company logos, no generated faces, no autoplay):
- "Timelines were met according to plan and the team is highly knowledgeable. I can highly recommend working with Manifera!" Arnold Tijdens, Founder and CEO, Kilimo
- "We were very positively surprised by the proactive approach, the intuitive UI/UX design and the speed of development by the Manifera team. We went live as planned, before the planned date!" Berend van Geffen, Director
- "Working with Manifera feels like having our own in-house development team." Maarten Diepenmaat, Co-founder, Statler

=== SECTION 8: FAQ (id="faq") ===
White, shadcn Accordion, plus FAQPage JSON-LD in index.html:
- "Why is there no price list on this page?" → Because team size, seniority, duration and scope decide the budget. Share your brief and we prepare a plan and a budget estimation for your situation.
- "Can we combine or change models?" → Yes. As a flexible company we can deviate from these models. Tell us your ideas about engagement and we are happy to discuss them.
- "How do vouchers work?" → You buy 80, 120 or 160 development hours per month, paid upfront before the start of each month. Manifera commits those hours for that month.
- "Can we try your services before signing a contract?" → Yes. We can start with a pilot project first.
- "Is our project information protected?" → Yes. We offer to sign a Non-Disclosure Agreement (NDA), and we follow the GDPR.
- "How do we get started?" → Find your model above and send your request. We will contact you within one working day.

=== SECTION 9: FINAL CTA (cosmic black band) ===
H2: "Know your model? Let's make the budget concrete." Sub: "Send your answers and we prepare a plan and a budget estimation."
Button "Find my model", or "Finish your request (step X of 4)" when saved answers exist. Next to it: "Or call Amsterdam: +31 619 70 10 01".

=== FOOTER (minimal, cosmic black) ===
White logo. NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam · +31 619 70 10 01 · VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City · +84 28 66522286 · SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842 (tel: links). Links (new tab): "manifera.com", "Privacy Policy". "Copyright © 2026 Manifera Software Development Pte. Ltd."

=== CONVERSION RULES ===
- Every primary CTA scrolls to #brief. Only footer and privacy links leave the page (new tab).
- Mobile sticky bottom bar after the hero: "Your match · question X of 5" (or "Takes about 60 seconds") + "Continue" / "Start". Hidden while #brief is in view.
- Desktop only, once per session: exit-intent card bottom right: "Your answers are saved. See your match in under a minute?" (or "Leaving already? Find your model in five questions."). Never on mobile, never on load.
- No fake countdowns, no fake "people viewing", no autoplay video, no sound.
- Never "cheap", "low cost", "best", "affordable" or any price or saving percentage. No em dashes. No ChatGPT or OpenAI branding.

=== PERFORMANCE & SEO ===
- LCP under 2.0s on mobile: the hero is text plus CSS cards. Lazy-load below the fold.
- Prerender "/" at build time so all text (including the four model descriptions and FAQ) is in the initial HTML; otherwise add a <noscript> block in index.html with the H1, sub, the four models with pros and cons, the five steps and the FAQ.
- One H1. Title: "Manifera | Software Team Cost and Engagement Models". Meta description: "Dedicated team, vouchers, time and materials or fixed price? Find the model that fits your project and get a plan and budget estimation."
- Open Graph 1200x630 image (the fanned card deck + logo). Organization JSON-LD (name, url, logo, foundingDate 2014, three addresses with phones).
- robots.txt allows all crawlers, including GPTBot, OAI-SearchBot and ChatGPT-User. Canonical without query parameters. No noindex.
```

---

## Prompt 2: Form backend

```
Connect the form to Lovable Cloud (Supabase).
1. Table "ad_leads": id (uuid), created_at, landing (text, always "ag4-cost-models"), name, work_email, company, country, message, heard_from, brief (jsonb: answers {q1..q5: yes|unsure|no}, scores {dedicated, vouchers, tm, fixed}, winner, runner_up, project_type, team_size, pilot bool), start_when, page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content, oppref, user_agent, is_free_email (bool).
2. On first load, read utm_* and oppref from the URL, keep them in sessionStorage (first touch wins) and attach them to the submission. Never drop oppref.
3. RLS: anonymous INSERT only. No public SELECT, UPDATE or DELETE.
4. Edge function on insert: email the lead to the secret SALES_EMAIL. Subject: "New ChatGPT Ads lead (cost/models): {company} ({country}) · match {winner} · team {team_size} · start {start_when}". Body: all fields in a readable table, including the five answers and the match %. Optional secret WEBHOOK_URL: also POST the lead as JSON.
5. Server-side spam checks: honeypot, math answer, rate limit 5 per IP per hour.
6. On error keep all input, show "Something went wrong. Try again" with retry and the Amsterdam phone number.
```

## Prompt 3: Tracking and cookie consent

```
Add GDPR-compliant tracking.
1. Small cookie banner: "We use cookies to measure our ads and improve this page." "Accept" and "Reject" with equal weight; "Cookie settings" link in the footer.
2. GA4 G-ZGH74C8BL4 via gtag.js with Consent Mode v2 (default denied, granted on Accept).
3. src/lib/openaiPixel.ts with init() and trackLead(); marked spot for the official OpenAI Ads pixel snippet. Load only after Accept. After Accept, store oppref in first-party cookie "mf_oppref" (30 days, SameSite=Lax, Secure).
4. Events (gtag + dataLayer):
   - form_submit_contact (PRIMARY, only after a successful save, once): landing, winner, team_size, start_when, pilot, country. Also call openaiPixel.trackLead().
   - phone_call_click {office}, email_click
   - brief_start, matcher_answer {q, answer}, matcher_complete {winner}, brief_step {step}, brief_skip_to_form
   - hours_dial_change {hours}, model_tab_view {model}, cta_click {cta_text, section}, exit_intent_shown, exit_intent_click, scroll_depth 50/90
5. Never send names, emails or company names to GA4 or the pixel.
```

## Prompt 4: Motion and polish

```
Polish pass:
- Section reveals: fade up 12px, 0.4s, stagger 0.06, once. Only the signature moments move more (deal, swipe cards, bar race, hours dial, iceberg, step line, stamp).
- Swipe cards: follow the finger with rotation proportional to drag distance; release beyond 100px commits the answer, otherwise spring back. Never block vertical page scroll when the drag is mostly vertical, except on the card itself.
- Bar race: 500ms width animation, layout re-sort 400ms, numbers roll.
- Primary buttons: subtle magnetic effect on desktop (max 4px), press scale 0.98.
- Under prefers-reduced-motion: no deal animation, no card fly-off (just swap), no water movement, no confetti.
- WCAG AA everywhere. Test at 360, 390, 768, 1280, 1536px and a 390x700 in-app browser viewport. Tap targets at least 44px, no horizontal scroll, keyboard never covers the active field.
```

## Prompt 5: QA checklist

```
Final QA, fix what fails:
- Scoring: all "Yes" → Dedicated or Fixed price leads as defined; all "No" → Time and materials leads; check that "Not sure" gives half points. Bars re-sort correctly after every answer.
- The hero face-down card flips to the winner after the matcher; #models shows the "Your match" label.
- Hours dial works by tap, drag and keyboard.
- Saved answers survive a reload; "Skip to the form" works.
- A test lead saves to ad_leads with answers, scores, UTM fields and oppref, sends the email, shows the stamp, fires form_submit_contact once and clears the saved answers.
- Consent rejected: no GA4 or pixel calls. Accepted: both fire.
- Page source contains the full text (prerender or noscript).
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100.
- No prices, savings percentages, invented numbers or promises; no "cheap", "low cost", "best", "affordable"; no em dashes; no ChatGPT or OpenAI branding.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

- **Link quảng cáo** (ví dụ `pricing.manifera.com`): `https://pricing.manifera.com/?utm_source=chatgpt&utm_medium=cpc&utm_campaign=mf-chatgpt-cost-eu&utm_content=ag4-a`.
- **Rủi ro lớn nhất:** [`paid_ads_plan.md`](./paid_ads_plan.md) §8.2 cảnh báo "a cost page without prices converts worse than no page at all". Trang này giảm rủi ro đó bằng Model Matcher, nhưng không thay được giá thật. Nếu ban lãnh đạo duyệt được **khoảng giá tham khảo** (theo tháng, theo cơ cấu seniority), bạn báo mình để thêm một mục "Indicative monthly team rates" vào Prompt 1. Đó là thay đổi có lợi nhất cho AG4.
- **Câu chữ trên site đã cũ:** trang Our Way Of Working ghi "headquarter in Singapore" và "around 50 clients". Prompt không dùng hai câu này (trang chủ ghi Amsterdam và 120 clients). Nên sửa trang đó cho khớp.
- **NDA và pilot project** đều có trên trang Our Way Of Working, nên được dùng. §3 của plan cần sửa dòng "NDA on request".
- **Chưa có context hints và mẫu quảng cáo AG4** trong plan. Mình có thể viết thêm nếu bạn cần.
