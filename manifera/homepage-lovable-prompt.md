# Manifera.com: New Homepage Prompt for Lovable (EN only)

> Cách dùng: dán **Prompt 1 (Main build)** vào Lovable trước. Khi bản đầu chạy ổn, dán lần lượt **Prompt 2 → 6** (mỗi lần một prompt, kiểm tra kết quả rồi mới dán tiếp). Mọi câu chữ, số liệu, logo khách hàng và lời chứng thực trong prompt đều lấy từ www.manifera.com (trang chủ và trang Contact, kiểm tra lại ngày 20/11/2026). Không thêm số liệu hay cam kết nào khác.
>
> Asset cần tải lên Lovable (kéo thả vào chat), xem danh sách đầy đủ ở mục "Ảnh cần chuẩn bị" cuối file: logo màu `https://www.manifera.com/wp-content/uploads/2021/04/Logo@4x.png`, logo trắng `https://www.manifera.com/wp-content/themes/manifera3/public/images/footer/manifera-logo-white.png`, logo khách hàng và đối tác, logo giải thưởng UNDP và IMDA, ảnh CEO Herre Roelevink, ảnh thật của team và văn phòng Amsterdam / Hồ Chí Minh, ảnh chụp màn hình sản phẩm đã làm cho khách hàng.

---

## Prompt 1: Main build

```
Build a single-page, English-only marketing homepage for Manifera (www.manifera.com), a Dutch-managed software development company with its headquarters in Amsterdam and an engineering hub in Ho Chi Minh City, Vietnam. The page has ONE job: turn B2B visitors (CTOs, VPs of Engineering, founders and COOs of European SMEs) into enquiries through Manifera's contact form. Every design decision should serve that goal.

Tech: React + Vite + TypeScript + Tailwind + shadcn/ui, lucide-react icons, framer-motion for subtle animation. One route ("/") plus a "/thank-you" route. Mobile-first, fully responsive. No lorem ipsum: use the exact copy below.

=== DESIGN SYSTEM: white canvas, cosmic-black type, logo blue and logo magenta ===
The page is LIGHT: a clean white background with generous whitespace. The brand is expressed through three colours only: cosmic black and the two colours of the Manifera logo. Define these as CSS variables in index.css and map them in tailwind.config:
- --white:      #FFFFFF  (main page background)
- --mist:       #F5F6FA  (very light alternating section background, use sparingly)
- --cosmic:     #05060F  (COSMIC BLACK: headings, primary text, footer, and at most two dark contrast bands)
- --logo-navy:  #0F0F3C  (the navy of the logo wordmark, used only inside dark bands and gradients)
- --blue:       #1E5CC8  (LOGO BLUE, primary brand colour: buttons, links, icons, key highlights)
- --magenta:    #CD37A5  (LOGO MAGENTA, accent colour)
- --body:       #3D4257  (body text on white)   --muted: #6B7086 (captions)   --line: #E6E8F0 (borders)
Colour ratio: about 70% white and mist, 15% cosmic black, 10% blue, 5% magenta. Measured contrast: blue on white 6.1:1 (fine for text and buttons), white on blue 6.1:1, magenta on white 4.5:1 (large text and decoration only), body #3D4257 on white 9.9:1.
Signature detail taken from the logo: a thin blue-to-magenta gradient (#1E5CC8 → #CD37A5). Use it only for small accents: the underline under one highlighted word in the hero H1, a 3px top border on featured cards, the "WINNER" award badges, the active state of the mobile menu, and small eyebrow dots before section labels.
Magenta rules: never use magenta for buttons, body text, large fills or small text on white (contrast is too low). Large headline words and decorative elements only. Blue always dominates magenta.
Dark bands: use cosmic black (#05060F) with a subtle radial logo-navy glow for exactly three moments: the trust band under the hero, the awards band and the footer. Everything else is white or mist. On cosmic black all text is white (or white at 70% for captions); logo blue is used there only for icons and large numbers, because blue on cosmic black is too low-contrast for body text.
Typography: "Space Grotesk" for headings in cosmic black (tight letter-spacing, H1 56-72px desktop / 38-44px mobile), "Inter" for body in --body colour (17-18px, line-height 1.65). Max text width 680px.
Buttons: Primary is solid #1E5CC8 with white text, rounded-xl, an arrow icon, and a slightly darker blue plus soft shadow on hover. Secondary is a white button with a 1px cosmic-black/15% border and cosmic-black text. Minimum height 48px.
Cards: white, 1px --line border, rounded-2xl, soft shadow (0 8px 30px rgba(5,6,15,0.06)). On hover lift 2px and the border turns blue at 40% opacity.
Accessibility: WCAG AA contrast, visible focus rings (#1E5CC8), respect prefers-reduced-motion, semantic landmarks, descriptive alt text on every image.

=== IMAGERY: persuasive, real, specific ===
Photos are the main persuasion tool on this page, so treat them as first-class content:
- Prefer the REAL photos I upload: Manifera engineers at work in Ho Chi Minh City, the Amsterdam office on Herengracht, CEO Herre Roelevink, client logos, award logos, and screenshots of products Manifera built for clients.
- Every photo must show real work: engineers pairing at a screen, a sprint review with a European client on a video call, a whiteboard architecture session, mobile apps being tested on real devices. Natural light, warm and consistent colour grade, people in focus, no cheesy stock poses, no "laptop alone on a desk" shots, no abstract sci-fi graphics.
- For atmosphere images where I have not uploaded a photo (office spaces, code-review scenes, device testing), you may generate realistic photos that follow this art direction. NEVER generate faces for named people, client logos, award logos or product screenshots. If one of those is missing, show a neat neutral placeholder (mist background, small label "Photo: <what belongs here>") so it is obvious what to replace.
- Combine photos with proof: overlay small white "proof cards" on key photos (a client quote with its logo, a stat, an award badge). This is what makes the images convincing.
- Treatment: rounded-2xl corners, soft shadow, object-cover, explicit width and height, WebP, lazy-load below the fold.

=== HEADER: recreate the existing manifera.com header 1:1, do not redesign ===
Sticky white header with a 1px --line bottom border once the page scrolls. Colour logo on the left. Navigation, keeping these exact labels and links:
- Our Services (dropdown): Offshore Software Development Teams → https://www.manifera.com/services/offshore-software-development/ · Custom Made Solutions → https://www.manifera.com/services/custom-software-development/ · Mobile app development → https://www.manifera.com/services/mobile-app-development/ · Web app development → https://www.manifera.com/services/web-app-develop/ · Webshop/eCommerce Developments → https://www.manifera.com/services/webshop-development/ · Migration to NL/Euro Cloud → https://www.manifera.com/services/migration-to-nl-euro-cloud-en/
- Portfolio → https://www.manifera.com/portfolio/
- About Us (dropdown): About Us · Our Way Of Working · Setting Up Your Team · Technologies · Careers (link each to its existing manifera.com page)
- Blog → https://www.manifera.com/blog/
- Contact → https://www.manifera.com/contact-us/
Only addition: on the right, a compact primary button "Contact us" that scrolls to #contact. Mobile: a hamburger opening a full-screen white sheet with the same items and the button at the bottom.

=== PAGE SECTIONS (in this order) ===

1) HERO (id="hero"). White background, two columns on desktop.
Left:
- Eyebrow with a small gradient dot: "Dutch management · Vietnamese engineering · Since 2014"
- H1: "Your dedicated <span class=gradient-underline>remote</span> software development team"
- Sub: "Scale up your software development capacity in a flexible and cost-effective way, with experienced engineers managed from Amsterdam."
- CTAs: Primary "Contact us" (scrolls to #contact); Secondary "See our work" (scrolls to #work).
- Micro line under the buttons: "We will contact you within one working day."
Right: a large real team photo (engineers collaborating at a screen), rounded-2xl, with three floating white proof cards overlapping its edges:
  a) Top-left: Vodafone logo + "It was efficient and productive to work with the Manifera project team." (Rizvi Amith, Vodafone)
  b) Bottom-left: "160 applications delivered"
  c) Right edge: magenta-to-blue "WINNER" badge + "United Nations UNDP Pacific-ASEAN Financial Innovation Challenge"
On mobile the photo goes under the text and the proof cards stack below it.

TRUST BAND (directly under the hero, cosmic black band #1 with a faint navy glow): 4 counters that count up once on view: "160 Applications" · "120 Global clients" · "30 Experts and growing" · "Since 2014". Below them a grayscale client-logo marquee (white logos on black; colour on hover) with the label "Some of our clients and partners": Vodafone, Statler, Kilimo, MO Batteries, CFLW, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham, BLCC.

2) WHAT CAN WE HELP YOU WITH? (id="needs"). White. Four large tiles in a grid, each with a small photo or icon, a 1-line outcome and an arrow. Each tile links to its existing service page (no forms, no selectors):
- "Extend my development team" → Offshore Software Development Teams page: "Your dedicated team of experienced software developers."
- "Build my product" → Custom Made Solutions page: "From UI/UX design via development to deployment, service and maintenance."
- "Build a web or mobile app" → Web app development page: "React / Node, Laravel / PHP, Magento, native and hybrid mobile apps."
- "Move to a Dutch or European cloud" → Migration to NL/Euro Cloud page: "We bring your applications and data to a Dutch/European cloud."

3) SERVICES (id="services"). Mist background. Title: "Everything you need to ship, under one roof." A bento grid; the two large cards carry real photos:
- Large card with photo (team in a sprint meeting): "01 Dedicated Remote Teams": "Providing you with your dedicated team of experienced software developers. Increasing your development capacity in a flexible and cost-effective way with our team of highly skilled and motivated engineers." CTA "Help me grow".
- Large card with photo (whiteboard architecture session): "02 Custom-made solutions": "Creating and developing your software application, based on your requirements and ideas to fulfil your specific business needs. From UI/UX design, via development all the way to deployment and service and maintenance, we take care of the whole cycle." CTA "Build my product".
- Small cards: "Mobile App Development" (native and hybrid apps) · "Web App Development" (React / Node, Laravel / PHP) · "Webshop & eCommerce" (Magento) · "Migration to NL / Euro Cloud" · "DevOps" (keep your SaaS or software system operational and up to date).
"Help me grow" and "Build my product" scroll to #contact; the small cards link to their existing manifera.com service URLs (same as the header).

4) AI (id="ai"). White. Two columns: left text, right a photo of a developer reviewing AI-assisted code on a large screen. Title: "AI and how it helps you".
- "AI-assisted development": "Our experienced software developers use AI during development to speed up delivery significantly, while our long software development experience keeps the quality of our deliverables high. We use AI in alignment with our clients, and on request we use local AI models, so no information ends up in public AI models (LLMs)."
- "AI solutions": "We also build AI into web and mobile applications as part of the solution for your business case, to make your internal and external processes even more efficient."
CTA: "Share your business case" (scrolls to #contact).

5) WHY MANIFERA (id="why"). Mist background. Title: "Why European teams choose Manifera." Left: a split photo, Amsterdam canal office on top and the Ho Chi Minh City engineering office below, each with a small location label. Right: four differentiators with blue icons:
- "Dutch management, Vietnamese engineering": Amsterdam headquarters, engineering hub in Ho Chi Minh City, office in Singapore.
- "Flexible and cost-effective": scale your development capacity up or down as your roadmap changes.
- "An international fusion of many cultures": teams used to working with clients in Europe, Asia and the Pacific.
- "Award-winning": Winner of the United Nations UNDP Pacific-ASEAN Financial Innovation Challenge and of Singapore IMDA's Open Innovation Platform.
CTA row under it: "Looking for a reliable partner?" plus the primary button "Contact us".

6) HOW IT WORKS (id="process"). White. A horizontal 4-step timeline (vertical on mobile), each step with a small numbered gradient dot:
1. "Contact us": Fill in the contact form; we contact you within one working day.
2. "Intro meeting": We learn your goals, your technology stack and your timeline.
3. "Your team": We propose the team composition and approach that fit your project.
4. "Start and scale": Development starts, and your team grows with your needs.
CTA: "Start with step 1" (scrolls to #contact).

7) CASE STUDIES (id="work"). Mist background. Title: "Results our clients talk about." Three large cards. On top of each, a product screenshot shown inside a clean browser or phone frame (placeholder if I have not uploaded the screenshot), then the client logo, a 1-line result and the link "Read the story":
- Vodafone Fiji: "Built and launched the online marketplace vitikart.com.fj on Magento with Vodafone Fiji's cloud architecture."
- MO Batteries: "Delivered the front end of a fleet-management platform, built in parallel with the client's own back-end team."
- Client registration system: "Up and running within a few weeks, and live before the planned date."
Link "See all work" → https://www.manifera.com/portfolio/

8) YOUR USE CASE (id="use-cases"). White. Title: "Looking for…" Four cards phrased as the visitor's situation:
- "…extra software developer(s) for a few months, around 20 to 40 hours per week."
- "…a project team to develop your bespoke web or mobile application."
- "…your team of software developers for the long run, with or without quality engineers and a project manager."
- "…DevOps engineer(s) to keep your SaaS or software system operational and up to date."
CTA under the cards: "Talk to us about your use case!" (scrolls to #contact).

9) TESTIMONIALS (id="testimonials"). Mist background. Carousel of large white quote cards, each with the client's company logo (no generated faces), name and role:
- Rizvi Amith, Manager Digital Business, Vodafone: "It was efficient and productive to work with the Manifera project team, and their technical skills in eCommerce development and software development showed!"
- Paul Booij, Co-founder and CTO, MO Batteries: "The technical discussions were of high quality and truly collaborative to create the best back-end/front-end interaction. It felt as if the Manifera developers were our own employees."
- Maarten Diepenmaat, Co-founder, Statler: "Working with Manifera feels like having our own in-house development team."
- Arnold Tijdens, Founder and CEO, Kilimo: "Timelines were met according to plan and the team is highly knowledgeable. I can highly recommend working with Manifera!"
- Berend van Geffen, Director: "We were very positively surprised by the proactive approach, the intuitive UI/UX design and the speed of development by the Manifera team. We went live as planned, before the planned date!"

10) AWARDS (id="awards"). Cosmic black band #2. Two award cards with the real UNDP and IMDA logos on white tiles and a small gradient "WINNER" label: "Winner of the United Nations UNDP Pacific-ASEAN Financial Innovation Challenge" · "Winner of Singapore's IMDA, Infocomm Media Development Authority, Open Innovation Platform".

11) FAQ (id="faq"). White. shadcn Accordion with 6 questions:
- "What engagement models do you offer?" → A dedicated remote team for the long run, a project team for your bespoke web or mobile application, extra developers for a few months at around 20 to 40 hours per week, or DevOps engineers to keep your system running.
- "Where are your developers based?" → Our engineering hub is in Ho Chi Minh City, Vietnam, with management from our Amsterdam headquarters and an office in Singapore.
- "Which technologies do you work with?" → React / Node, Laravel / PHP, Magento, native and hybrid mobile apps, and DevOps.
- "Can you use AI without our data reaching public AI models?" → Yes. We use AI in alignment with our clients, and on request we use local AI models, so no information ends up in public AI models (LLMs).
- "Can you move our application to a Dutch or European cloud?" → Yes. We bring your applications and data to a Dutch/European cloud provider; see our Migration to NL/Euro Cloud service.
- "How do we get started?" → Fill in the contact form below and we will contact you within one working day.
Add FAQPage JSON-LD for these questions in index.html.

12) CONTACT (id="contact"). This is Manifera's OWN contact form, the same as on https://www.manifera.com/contact-us/. Keep it simple and do not turn it into a quiz, wizard, chip selector, price estimator or multi-step form.
White background with a soft blue glow behind the form card. Two columns:
Left:
- H2: "Looking for a reliable partner?"
- Copy: "Let's explore how we can help you in a trustworthy and long-term way! Feel free to fill in the contact form for more information or a question, and we will contact you within one working day."
- A small portrait card with the real photo of CEO Herre Roelevink and the line "Herre Roelevink, Founder & CEO".
- "Our contact information", three small blocks:
  NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam, The Netherlands · +31 619 70 10 01
  VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City, Vietnam · +84 28 66522286
  SINGAPORE: 100 Tras Street #16-01, Singapore 079027 · +65 9853 2842
  Phone numbers are tel: links.
Right: a white form card titled "Contact Form" (react-hook-form + zod) with exactly these fields:
- Name (required, placeholder "Name")
- Email (required, valid email, placeholder "Email")
- Message (required textarea, placeholder "Type your message...")
- A simple human check like the current site: "What is 4 + 3?" with a small number input (random numbers per page load), plus a hidden honeypot field.
- Submit button, full width, primary blue: "Send"
- Under the button, small muted text: "By sending this form you agree to our Privacy Policy." (link to https://www.manifera.com/privacy-policy/)
Inline validation, a loading state, and no page reload. On success, navigate to /thank-you.

=== FOOTER: recreate the existing manifera.com footer 1:1, do not redesign ===
Cosmic black (#05060F) with the white logo. Four columns:
- OUR SERVICES: Offshore Software Development Teams · Custom Software Development · Web Shops / eCommerce
- ABOUT US: About Our Company · Our way of working · Setting up your team · Technologies · Careers
- CONTACT INFO: NETHERLANDS: Herengracht 420, 1017 BZ Amsterdam, the Netherlands. SINGAPORE: 100 Tras Street #16-01, 100 AM, Singapore 079027. VIETNAM: Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward, Ho Chi Minh City.
- Contact us at: Contact Form (→ https://www.manifera.com/contact-us/), LinkedIn and Facebook icons, call icon.
Bottom bar: Privacy Policy · Terms and Conditions · "Copyright © 2026 – Manifera Software Development Pte. Ltd."
All links go to the existing manifera.com URLs.

=== CONVERSION RULES (apply everywhere) ===
- A primary CTA must be visible at most every 2 sections. All primary CTAs scroll to #contact; none sends the visitor away to another site.
- Put proof (a logo row, a quote or a number) next to every CTA block.
- On mobile, show a sticky bottom bar after scrolling past the hero: "Contact us" (primary, scrolls to #contact) and a call icon (tel:+31619701001). Hide it while the contact form is in view.
- No dark patterns: no fake countdowns, no fake "X people viewing", no pop-up on page load. One polite exit-intent banner on desktop only, shown once per session: "Looking for a reliable partner? Let's talk." with a button that scrolls to #contact.
- Do not add promises, numbers or client names beyond the copy in this prompt.

=== PERFORMANCE & SEO ===
- LCP under 2.5s: the hero photo is the LCP element, so preload it, serve WebP at the right size and never lazy-load it. No autoplay video, no heavy 3D. Lazy-load every image below the fold.
- One H1 only (the hero), then a logical H2/H3 order.
- Title: "Manifera | Dedicated Software Teams, Amsterdam & Vietnam". Meta description: "Scale up your software development capacity in a flexible and cost-effective way, with a dedicated team managed from Amsterdam. Since 2014." Add Open Graph tags with a 1200x630 share image (hero photo + logo).
- Add Organization JSON-LD: name, URL, logo, foundingDate 2014, founder Herre Roelevink, the three addresses with their phone numbers, and sameAs links to the Manifera LinkedIn and Facebook pages.
```

---

## Prompt 2: Contact form backend

```
Connect the contact form to Lovable Cloud (Supabase).
1. Create a table "contact_requests" with these columns: id (uuid), created_at, name, email, message, page_url, referrer, utm_source, utm_medium, utm_campaign, utm_term, utm_content.
2. On first page load, capture the UTM parameters and the referrer, keep them in sessionStorage, and attach them to the submission.
3. Enable RLS: anonymous users may INSERT only. No public SELECT, UPDATE or DELETE.
4. Add an edge function that emails each new request to the sales inbox (put the address in a secret called SALES_EMAIL, never in client code) in a readable layout. Add an optional WEBHOOK_URL secret: if it is set, also POST the request as JSON to it, so we can forward it to WordPress/Contact Form 7 or a CRM later.
5. Spam protection: check the honeypot and the math answer server-side, and rate-limit by IP in the edge function (max 5 submissions per hour).
6. Show friendly error states. If saving fails, keep the user's input and offer the button "Try again".
```

## Prompt 3: Tracking

```
Add conversion tracking that works with Google Tag Manager.
- Load GTM with a container ID from an env variable VITE_GTM_ID (do not hardcode it).
- Push dataLayer events: cta_click {cta_text, section}, service_tile_click {service, section}, form_start {form_id: "contact"} (first field focus), form_submit {form_id: "contact"}, phone_click {office}, exit_intent_shown, exit_intent_click.
- The /thank-you page fires generate_lead once (guard against reloads).
- Add a simple cookie consent banner (Accept / Reject) that respects GDPR. Only load GTM after the visitor clicks Accept.
```

## Prompt 4: Thank-you page

```
Create the /thank-you page in the same white style, with the header and footer included.
- H1: "Thank you, we received your message."
- Copy: "We will contact you within one working day."
- A small row of proof under it: the client-logo strip from the homepage and one testimonial card.
- Secondary actions: "Explore our portfolio" (→ https://www.manifera.com/portfolio/), "Read the blog" (→ https://www.manifera.com/blog/), "Back to the homepage".
- noindex meta tag.
```

## Prompt 5: Polish & motion

```
Polish pass:
- Subtle framer-motion reveal (fade up 12px, 0.4s, stagger 0.06) for section headings, cards and photos. Disable it when prefers-reduced-motion is set.
- Card hover: lift by 2px, the border turns blue (#1E5CC8) at 40% opacity.
- Hero: the floating proof cards drift by 2-4px in a slow 8-10s loop; static when prefers-reduced-motion is set.
- Check every colour pair against WCAG AA on white and on cosmic black, and fix any that fail. Magenta must never be used for small text on white.
- Check the colour balance: the page reads as white with cosmic-black type, blue is the clear brand colour, magenta covers no more than about 5% of the visual area. Replace any extra magenta with blue.
- Check every image: real photos where uploaded, no generated faces for named people, no stock-looking poses, consistent colour grade, correct alt text.
- Test at 360px, 768px, 1280px and 1536px widths. Make sure there is no horizontal scroll and that every button has a tap target of at least 44px.
```

## Prompt 6: QA checklist

```
Run a final QA and fix the issues:
- Every header and footer link matches the existing manifera.com URLs exactly.
- Every primary CTA scrolls to #contact; service tiles and small service cards open the correct manifera.com service page.
- The contact form has exactly Name, Email, Message, the math check and the "Send" button; it validates, saves to contact_requests with the UTM fields, triggers the email and redirects to /thank-you.
- Lighthouse mobile: Performance 90+, Accessibility 95+, Best Practices 95+, SEO 100. Report the scores and fix the biggest issues.
- No placeholder text left except clearly labelled photo placeholders, no lorem ipsum, and no invented statistics, promises or client names beyond the ones provided.
```

---

## Ghi chú cho bạn (không dán vào Lovable)

### Những gì đã đổi so với bản trước
- **Màu**: nền trắng thay cho nền tối "deep space". Màu thương hiệu chỉ còn **đen vũ trụ `#05060F`** (tiêu đề, chữ, footer, 2 dải tối) và **2 màu thật của logo**, đo trực tiếp từ file `Logo@4x.png`: xanh **`#1E5CC8`** (màu chính) và hồng tím **`#CD37A5`** (điểm nhấn). Navy của chữ logo là **`#0F0F3C`**. Bản trước ghi navy `#080838` và magenta `#D12882`, không khớp logo nên đã sửa. Điểm nhấn đặc trưng là dải gradient xanh → hồng tím lấy từ logo, chỉ dùng cho chi tiết nhỏ.
- **Hình ảnh**: thêm phần "IMAGERY" quy định ảnh thật, cảnh làm việc thật, kèm các "proof card" (lời khách hàng + logo, con số, giải thưởng) đặt chồng lên ảnh. Hero giờ dùng ảnh team thay cho form. Mục Services, AI, Why, Case studies đều có ảnh hoặc ảnh chụp màn hình sản phẩm. Không cho Lovable tạo mặt người có tên, logo hay ảnh sản phẩm giả; thiếu ảnh thì hiện ô placeholder có ghi chú.
- **Form**: bỏ hết kiểu form của LaunchStudio, gồm:
  - form "Quick start" chọn chip 2 bước ở hero
  - ô chọn "What do you need?"
  - ô "Team size or budget"
  - truyền nhu cầu đã chọn vào form (pre-select)
  - booking dialog
  - câu cam kết kiểu "reply within 1 day"

  Thay vào đó dùng đúng form liên hệ hiện có của Manifera: **Name / Email / Message ("Type your message...") + câu hỏi tính nhẩm + nút "Send"**, tiêu đề "Looking for a reliable partner?" và câu "we will contact you within one working day" lấy nguyên từ trang Contact. Bảng dữ liệu đổi tên thành `contact_requests`, chỉ lưu đúng các trường đó.
- **Bỏ các câu không có trên site** (bản trước tự thêm vào):
  - "2-4 weeks"
  - "Proposal in 48 hours"
  - "30+" (site ghi "30 Experts and growing")
  - "Fluent English, real overlap"
  - "GDPR-ready"
  - "NDA on request"
  - "You interview and approve every engineer"

  FAQ chỉ trả lời bằng thông tin có trên site. Thêm 2 lời chứng thực có thật trên site (Statler, Kilimo) và số điện thoại 3 văn phòng từ trang Contact.
- **SEO**: title rút còn 56 ký tự. Hero chỉ có một H1 đúng nội dung (khắc phục lỗi H1 trong audit ngày 19/11).

### Ảnh cần chuẩn bị (tải lên Lovable)
| Vị trí | Ảnh | Hiện có trên site? |
|---|---|---|
| Hero | Ảnh thật team Manifera đang làm việc cùng nhau trước màn hình (ngang, ≥ 1600px) | Chưa. Ảnh team trên site hiện tại (`section3-1.webp`, `section3-2.1.webp`) trông giống ảnh stock, nên chụp ảnh thật |
| Logo khách hàng/đối tác | Vodafone, Statler, Kilimo, MO Batteries, CFLW, TNO, Upkeepa, Hestec, Loggix, EuroCham Singapore, ADB DutchCham, BLCC | Có, trong `/wp-content/uploads/2026/10/` và `/2022/11/` |
| Services | Ảnh sprint meeting, ảnh buổi vẽ kiến trúc trên bảng trắng | Chưa |
| AI | Ảnh developer review code trên màn hình lớn | Chưa |
| Why Manifera | Ảnh văn phòng Amsterdam (Herengracht) và văn phòng Hồ Chí Minh | Chưa |
| Case studies | Ảnh chụp màn hình vitikart.com.fj, giao diện MO Batteries, hệ thống client registration (cần khách đồng ý) | Chưa |
| Awards | Logo UNDP và IMDA | Có: `section7-1.webp`, `section7-2.webp` (nên dùng bản độ phân giải cao hơn) |
| Contact | Chân dung CEO Herre Roelevink | Có: `/wp-content/uploads/2020/09/Herre-3-400x400-1.jpg` (400px, nên có bản lớn hơn) |

Nếu chưa có ảnh thật, Lovable sẽ tạo ảnh không khí văn phòng/làm việc theo mô tả, còn ảnh người có tên, logo và ảnh sản phẩm sẽ hiện ô placeholder để thay sau.

### Lưu ý khác
- **Số liệu**: con số "9 Years in Operation" trên trang chủ hiện tại đã cũ (Manifera thành lập năm 2014 theo `manifera_info.md`). Prompt dùng "Since 2014". Các con số 160 / 120 / 30 lấy nguyên từ trang chủ, nên kiểm tra lại trước khi đưa lên.
- **Lời chứng thực**: là trích đoạn nguyên văn từ trang chủ và trang Contact, chỉ cắt ngắn.
- **Header/Footer**: Lovable không dùng chung được theme WordPress `manifera3`, nên prompt yêu cầu dựng lại y hệt (cùng menu, link, địa chỉ). Nếu sau này đưa trang lên WordPress thật, phần nội dung giữa header và footer cần chuyển thành template của theme, còn form nối vào Contact Form 7 (site đang dùng CF7 kèm captcha tính nhẩm, GA4 và GTM).
- **Bố cục tham khảo**:
  - Hero một CTA chính + Case Studies + "Let's Talk" (gojilabs).
  - Khối "The Unico Difference" (unicoconnect).
  - Ô chọn nhu cầu (sucuri), nhưng ở đây chỉ dẫn sang trang dịch vụ.
  - Lưới "featured competencies" (instinctools).
  - "Why trust" (eleks).
