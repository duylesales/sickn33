# Manifera.com: New Homepage Prompt for Lovable (EN only)

> Cách dùng: dán **Prompt 1 (Main build)** vào Lovable trước. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 6** (mỗi lần một prompt, kiểm tra kết quả rồi mới dán tiếp). Mọi số liệu, logo khách hàng và lời chứng thực trong prompt đều lấy từ trang www.manifera.com hiện tại (kiểm tra ngày 19/11/2026). Không thêm số liệu nào khác.
>
> Asset cần tải lên Lovable (kéo thả vào chat): logo màu `https://www.manifera.com/wp-content/uploads/2021/04/Logo@4x.png`, logo trắng `https://www.manifera.com/wp-content/themes/manifera3/public/images/footer/manifera-logo-white.png`, logo khách hàng (Vodafone, Statler, Kilimo, CFLW, MO Batteries…), ảnh thật của team/văn phòng Amsterdam và Hồ Chí Minh, ảnh CEO Herre Roelevink.

---

## Prompt 1: Main build

```
Build a single-page, English-only marketing homepage for Manifera (www.manifera.com), a Dutch-managed software development company with an engineering hub in Ho Chi Minh City, Vietnam. The page has ONE job: turn B2B visitors (CTOs, VPs of Engineering, founders and COOs of European SMEs) into leads via form submissions and booked calls. Every design decision should serve conversion.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react icons, framer-motion for subtle animation. One route ("/") plus a "/thank-you" route. Mobile-first, fully responsive. No lorem ipsum: use the exact copy below.

=== DESIGN SYSTEM ===
Theme: "deep space". The page is dark, premium and calm, lit by Manifera's logo blue. Define these as CSS variables in index.css and map them in tailwind.config:
- --space-950: #05060F  (main page background, "cosmic black")
- --space-900: #0A0B1A  (alternating section background)
- --space-800: #11132A  (cards, form panels)
- --navy:      #080838  (logo navy, used in gradients and deep panels)
- --blue-600:  #1E5CC8  (PRIMARY brand blue: buttons, links, key highlights)
- --blue-400:  #4C8DFF  (lighter blue for text and icons on dark, glows, hover)
- --magenta:   #D12882  (logo magenta: ACCENT ONLY)
- --text:      #F5F7FF  (headings)   --muted: #A9B0C7 (body)   --line: rgba(255,255,255,0.08) (borders)
Colour ratio: about 75% cosmic black and navy, 20% blue, at most 5% magenta. Use magenta only for tiny details: one highlighted word in the hero, the small "WINNER" award badge, a hover underline, a single dot in a status indicator. Never use magenta for buttons, large areas or body text. Blue clearly dominates over magenta.
Atmosphere: a very subtle starfield or noise texture on the darkest sections; soft radial blue glows (#1E5CC8 at 15-25% opacity) behind the hero and the final CTA; thin 1px borders (--line); cards with a faint top-edge highlight; a gradient from navy to blue (#080838 → #1E5CC8) for primary panels. Keep it restrained: no neon overload and no busy particles that hurt performance.
Typography: "Space Grotesk" for headings (tight letter-spacing, H1 56-72px desktop / 38-44px mobile), "Inter" for body (17-18px, line-height 1.65). Max text width 680px.
Buttons: Primary is solid #1E5CC8 with white text, rounded-xl, an arrow icon and a soft blue glow on hover. Secondary is a ghost button with a 1px white/15% border. Minimum height 48px.
Accessibility: WCAG AA contrast, visible focus rings (#4C8DFF), respect prefers-reduced-motion, semantic landmarks, alt text on every image.

=== HEADER: recreate the existing manifera.com header 1:1, do not redesign ===
Sticky header. Logo on the left (uploaded colour logo; use the white logo when the header sits on dark). Navigation, keeping these exact labels and links:
- Our Services (dropdown): Offshore Software Development Teams → https://www.manifera.com/services/offshore-software-development/ · Custom Made Solutions → https://www.manifera.com/services/custom-software-development/ · Mobile app development → https://www.manifera.com/services/mobile-app-development/ · Web app development → https://www.manifera.com/services/web-app-develop/ · Webshop/eCommerce Developments → https://www.manifera.com/services/webshop-development/ · Migration to NL/Euro Cloud → https://www.manifera.com/services/migration-to-nl-euro-cloud-en/
- Portfolio → https://www.manifera.com/portfolio/
- About Us (dropdown): About Us · Our Way Of Working · Setting Up Your Team · Technologies · Careers (link each to its existing manifera.com page)
- Blog → https://www.manifera.com/blog/
- Contact → https://www.manifera.com/contact-us/
Only addition: on the right, a compact primary button "Get a proposal" that scrolls to #lead-form. Mobile: a hamburger opening a full-screen sheet with the same items and the button at the bottom.

=== PAGE SECTIONS (in this order) ===

1) HERO (id="hero"). Two columns on desktop.
Left:
- Eyebrow chip: "Dutch management · Vietnamese engineering · Since 2014"
- H1: "Your dedicated software team, <span class=magenta-underline>live</span> in weeks, not months."
- Sub: "Scale your development capacity with senior engineers managed from Amsterdam. Flexible, cost-effective and GDPR-ready. AI-assisted delivery, without compromising on quality."
- CTAs: Primary "Get a team proposal in 48 hours" (scrolls to #lead-form); Secondary "Book a 30-min call" (opens the booking dialog from section 12).
- Micro-trust line under the buttons: "No commitment · Reply within 1 business day · NDA on request"
Right: a glassy "Quick start" card (--space-800, blue glow) with a 2-step mini form. Step 1: "What do you need?" as 4 large selectable chips: "Extra developers" / "Build a product" / "Modernise legacy" / "Add AI". Step 2: Name, Work email, then the button "Send". It submits to the same leads table (see Prompt 2) with source="hero".
Below the hero, full width: a "trust bar" with 4 animated counters (count up once on view): "160 Applications delivered" · "120 Global clients" · "30+ Experts and growing" · "Since 2014". Then a grayscale client-logo marquee (Vodafone, Statler, Kilimo, CFLW, MO Batteries and the other uploaded logos) with the label "Trusted by teams in Europe, Asia and the Pacific".

2) INTENT SELECTOR (id="needs"). Title: "What can we help you with?" Four large clickable tiles in a grid, each with an icon, a 1-line outcome and an arrow:
- "Add developers to my team": "Senior engineers who join your sprints in 2-4 weeks."
- "Build my product": "From UI/UX to launch, maintenance included."
- "Modernise a legacy system": "Migrate without downtime, including to NL/EU cloud."
- "Add AI to my software": "AI features and AI-assisted development, local models on request."
Clicking a tile scrolls to #lead-form and pre-selects that need in the form.

3) SERVICES (id="services"). Title: "Everything you need to ship, under one roof." A 3x2 bento grid with one larger feature card:
- Large card: "Dedicated Remote Teams": "Your own team of experienced developers, QA and project management, working as an extension of your company." CTA "Help me grow".
- "Custom Software Development": "Built around your requirements, from UI/UX design via development to deployment, service and maintenance." CTA "Build my product".
- "Mobile App Development": "Native and hybrid apps for iOS and Android."
- "Web App Development": "React / Node, Laravel / PHP and modern web stacks."
- "Webshop & eCommerce": "Magento and custom commerce platforms."
- "Migration to NL / Euro Cloud": "Move to GDPR-compliant European cloud infrastructure."
Each card links to its existing manifera.com service URL (same as the header).

4) AI STRIP (id="ai"). Navy-to-blue gradient panel. Title: "AI-assisted development, with senior engineers in control." Two columns:
- "AI-assisted development": "Our developers use AI to speed up delivery, while long-standing engineering experience keeps quality high. On request we use local AI models, so your code and data never reach public LLMs."
- "AI inside your product": "We build AI into web and mobile applications to automate processes and unlock new efficiencies."
CTA: "Discuss your AI use case".

5) WHY MANIFERA (id="why"). Title: "Why European teams choose Manifera." Four differentiators in cards with icons:
- "Dutch management × Vietnamese mastery": European project governance with an Amsterdam HQ, plus a Ho Chi Minh City engineering hub.
- "Scale up or down in 2-4 weeks": Dedicated team, project-based or staff augmentation.
- "Fluent English, real overlap": Developers who write and speak English, with working hours that overlap with Europe.
- "Award-winning": Winner of the United Nations UNDP Pacific-ASEAN Financial Innovation Challenge and of Singapore IMDA's Open Innovation Platform.
Mid-page CTA row under the cards: "Ready to meet your future team?" plus the primary button.

6) HOW IT WORKS (id="process"). A horizontal 4-step timeline (vertical on mobile):
1. "Intro call (30 min)": We learn your goals, stack and timeline.
2. "Proposal in 48 hours": Team composition, approach and cost.
3. "Meet & select your team": You interview and approve every engineer.
4. "First sprint in 2-4 weeks": Onboarding, kick-off, and you are shipping.
CTA: "Start with step 1" (opens the booking dialog).

7) CASE STUDIES (id="work"). Title: "Results our clients talk about." Three large cards with an image on top, client logo, a 1-line challenge, a 1-line result, and the link "Read the story":
- Vodafone Fiji: "Built and launched the online marketplace vitikart.com.fj on Magento with Vodafone's cloud architecture."
- MO Batteries: "Delivered the front end of a fleet-management platform, built in parallel with the client's back-end team."
- Client registration system: "Went live before the planned date, a few weeks after kick-off."
Link "See all work" → https://www.manifera.com/portfolio/

8) USE CASES (id="use-cases"). Title: "Looking for…" Four cards, each phrased as the visitor's situation, each with a small CTA "This is me" (pre-selects the form):
- "…extra software developer(s) for a few months, 20-40 hours per week."
- "…a project team to develop your bespoke web or mobile application."
- "…your own team of software developers for the long run, with or without QA engineers and a project manager."
- "…DevOps engineer(s) to keep your SaaS or software system operational and up to date."

9) TESTIMONIALS (id="testimonials"). Carousel with large quote marks and names, plus a short version of each real quote:
- Rizvi Amith, Manager Digital Business, Vodafone: "It was efficient and productive to work with the Manifera project team, and their technical skills in eCommerce and software development showed."
- Paul Booij, Co-founder & CTO, MO Batteries: "The technical discussions were of high quality and truly collaborative. It felt as if the Manifera developers were our own employees."
- Vincent Koster, IT Manager: "They do more than just build the application; they also give helpful advice and support on related processes. Professional, skilled and very engaged."
- Berend van Geffen, Director: "We were very positively surprised by the proactive approach, the intuitive UI/UX design and the speed of development. We went live before the planned date."

10) AWARDS (id="awards"). A slim band with two award badges (small magenta "WINNER" label): United Nations UNDP Pacific-ASEAN Financial Innovation Challenge · Singapore IMDA Open Innovation Platform.

11) FAQ (id="faq"). shadcn Accordion, 6 objection-handling questions:
- "How fast can my team start?" → Usually 2-4 weeks from the intro call to the first sprint.
- "Do I interview the developers?" → Yes, you approve every engineer before they join.
- "How do you protect my IP and data?" → NDA on request, IP belongs to you, GDPR-compliant processes, and local AI models on request.
- "What engagement models do you offer?" → Dedicated team, project-based delivery, or staff augmentation.
- "What about time zones and communication?" → Fluent English and European overlap hours, with project management from Amsterdam.
- "What does it cost?" → It depends on team size and seniority; you get a transparent proposal within 48 hours.
Add FAQPage JSON-LD for these questions in index.html.

12) FINAL CTA + LEAD FORM (id="lead-form"). The strongest visual moment on the page: a big radial blue glow over cosmic black. Two columns.
Left: H2 "Let’s build your team." Copy: "Tell us what you need. You’ll get a tailored proposal within 48 hours, with no obligation." Then a list of 3 checkmarks (Reply within 1 business day · NDA on request · Dutch point of contact), a small portrait card of CEO Herre Roelevink with the line "You’ll speak directly with our Amsterdam team.", and the three office addresses (from the footer) in small muted text.
Right: the main form card (react-hook-form + zod):
- "What do you need?" (select, required): Extra developers / Build a product / Modernise legacy / Add AI / Something else
- Full name (required) · Work email (required, valid email) · Company (required)
- Team size or budget (optional select): 1-2 developers / 3-5 / 6+ / Not sure yet
- Message (optional textarea, placeholder "Briefly describe your project or stack")
- GDPR consent checkbox (required): "I agree to Manifera processing my data to respond to my request. See our Privacy Policy." (link to https://www.manifera.com/privacy-policy/)
- Submit button, full width: "Get my proposal →"
Inline validation, a loading state, and no page reload. On success, navigate to /thank-you. Below the button, the micro-copy: "We never share your details."
Also add a secondary option under the form: "Prefer to talk? Book a 30-min call" which opens a shadcn Dialog with a simple booking request form (name, email, preferred day and time window). Leave a clearly marked placeholder where a Calendly or Google Calendar embed can be added later.

=== FOOTER: recreate the existing manifera.com footer 1:1, do not redesign ===
Dark (#05060F) with the white logo. Four columns:
- OUR SERVICES: Offshore Software Development Teams · Custom Software Development · Web Shops / eCommerce
- ABOUT US: About Our Company · Our way of working · Setting up your team · Technologies · Careers
- CONTACT INFO: NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam, the Netherlands. SINGAPORE: 100 Tras Street #16-01, 100 AM, Singapore 079027. VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City.
- Contact us at: Contact Form (→ https://www.manifera.com/contact-us/)
Bottom bar: Privacy Policy · Terms and Conditions · "Copyright © 2026 – Manifera Software Development Pte. Ltd."
All links go to the existing manifera.com URLs.

=== CONVERSION RULES (apply everywhere) ===
- A primary CTA must be visible at most every 2 sections. All primary CTAs lead to #lead-form or the booking dialog, and none sends the visitor away to another site.
- On mobile, show a sticky bottom bar after scrolling past the hero: "Get a proposal" (primary) and a call icon. Hide it while the lead form is in view.
- Put social proof (logos, quotes, numbers) right next to every CTA block.
- Pre-selecting: any tile or card with an intent (sections 2, 3, 8) passes that intent into the form via state or a URL hash.
- No dark patterns: no fake countdowns, no fake "X people viewing", no pop-up on page load. One polite exit-intent banner on desktop only, shown once per session: "Get a free team proposal in 48 hours" + CTA.

=== PERFORMANCE & SEO ===
- LCP under 2.5s: no autoplay video and no heavy 3D. The starfield is CSS-only or a tiny canvas that stops when off-screen. Lazy-load images below the fold and serve WebP.
- One H1 only, then a logical H2/H3 order. Title: "Manifera | Dedicated Software Development Teams | Amsterdam & Vietnam". Meta description: "Scale your development capacity with a dedicated team of senior engineers, managed from Amsterdam. Proposal within 48 hours. Since 2014." Add Open Graph tags.
- Add Organization JSON-LD (name, URL, logo, three addresses).
```

---

## Prompt 2: Lead capture backend

```
Connect all forms to Lovable Cloud (Supabase).
1. Create a table "leads" with these columns: id (uuid), created_at, source (text: "hero" | "lead-form" | "booking" | "exit-intent"), need (text), full_name, work_email, company, team_size, message, preferred_time, consent (boolean), page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content.
2. On first page load, capture the UTM parameters and the referrer, keep them in sessionStorage, and attach them to every submission.
3. Enable RLS: anonymous users may INSERT only. No public SELECT, UPDATE or DELETE.
4. Add an edge function that emails each new lead to the sales inbox (put the address in a secret called SALES_EMAIL, never in client code) with all the fields in a readable layout. Add an optional WEBHOOK_URL secret: if it is set, also POST the lead as JSON to it, so we can forward leads to WordPress/Contact Form 7 or a CRM later.
5. Add basic spam protection: a hidden honeypot field plus rate limiting by IP in the edge function (max 5 submissions per hour).
6. Show friendly error states. If saving fails, keep the user's input and offer the button "Try again".
```

## Prompt 3: Tracking

```
Add conversion tracking that works with Google Tag Manager.
- Load GTM with a container ID from an env variable VITE_GTM_ID (do not hardcode it).
- Push dataLayer events: cta_click {cta_text, section}, intent_select {need, section}, form_start {form_id} (first field focus), form_submit {form_id, need, team_size}, booking_open, booking_submit, exit_intent_shown, exit_intent_click.
- The /thank-you page fires generate_lead once (guard against reloads).
- Add a simple cookie consent banner (Accept / Reject) that respects GDPR. Only load GTM after the visitor clicks Accept.
```

## Prompt 4: Thank-you page

```
Create the /thank-you page in the same deep-space style, with the header and footer included.
- H1: "Thanks, your request is in."
- Copy: "A member of our Amsterdam team will reply within 1 business day with next steps."
- A 3-step "What happens next" list: We review your request → You receive a tailored proposal within 48 hours → Intro call to meet your future team.
- Secondary actions: "Book your intro call now" (opens the booking dialog), "Explore our portfolio" (→ https://www.manifera.com/portfolio/), "Read the blog" (→ https://www.manifera.com/blog/).
- noindex meta tag.
```

## Prompt 5: Polish & motion

```
Polish pass:
- Subtle framer-motion reveal (fade up 12px, 0.4s, stagger 0.06) for section headings and cards. Disable it when prefers-reduced-motion is set.
- Card hover: lift by 2px, the border brightens to blue-400 at 40% opacity, plus a soft inner glow.
- Hero: a slow, barely noticeable drift on the background glow (an 8-12s loop).
- Check every colour pair against WCAG AA and fix any that fail.
- Check that magenta covers no more than about 5% of the visual area. If it is used anywhere beyond the allowed accents, replace it with blue.
- Test at 360px, 768px, 1280px and 1536px widths. Make sure there is no horizontal scroll and that every button has a tap target of at least 44px.
```

## Prompt 6: QA checklist

```
Run a final QA and fix the issues:
- Every header and footer link matches the existing manifera.com URLs exactly.
- Every CTA either scrolls to #lead-form with the right pre-selected need or opens the booking dialog.
- All forms validate, save to the leads table with the UTM fields, trigger the email, and redirect to /thank-you.
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100. Report the scores and fix the biggest issues.
- No placeholder text, no lorem ipsum, and no invented statistics or client names beyond the ones provided.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

- **Số liệu "9 Years in Operation"** trên trang chủ hiện tại đã cũ (Manifera thành lập năm 2014 theo `manifera_info.md`). Prompt dùng "Since 2014" để không bị lỗi thời. Hãy kiểm tra lại các con số 160 / 120 / 30+ trước khi đưa lên.
- **Lời chứng thực** trong prompt là bản rút gọn từ lời gốc trên trang chủ. Nếu muốn giữ nguyên văn thì thay bằng bản gốc.
- **Header/Footer**: Lovable không dùng chung được theme WordPress `manifera3`, nên prompt yêu cầu dựng lại y hệt (cùng menu, link, địa chỉ). Nếu sau này muốn đưa trang lên WordPress thật, cần chuyển phần nội dung giữa header và footer thành template của theme, còn form thì nối vào Contact Form 7 (website đang dùng CF7, GA4 và GTM).
- **Bố cục tham khảo**: Hero một CTA chính + Case Studies + "Let's Talk" (gojilabs). Hai CTA "Talk to an Expert / Hire" + khối "The Unico Difference" (unicoconnect). Các ô chọn nhu cầu Fix/Scan/Protect/Boost → "What can we help you with?" (sucuri). Lưới "featured competencies" (instinctools). "Why trust" + form cuối trang "Share your goal" (eleks).
