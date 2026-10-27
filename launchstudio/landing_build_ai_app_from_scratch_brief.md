# 🧱 Landing page "Build AI app from scratch" (NL + EN): content brief + Lovable prompt

> **Ngày:** 22/10/2026 · **Ngôn ngữ trang:** 🇳🇱 Tiếng Hà Lan (mặc định) + 🇬🇧 Tiếng Anh, chuyển bằng nút `EN | NL` trên header
> **Keyword EN:** `build ai app from scratch` · `build an app with ai` (30) · `build ai app` · `ai app development`
> **Keyword NL:** `ai-app laten bouwen` · `app laten maken` (480) · `app laten bouwen` (140) · `mvp laten maken` (50)
> **Nguồn:** `landing_pages_roadmap.md` §1, §3 · `launchstudio_info.md` §2–4, §6 · header/footer lấy trực tiếp từ HTML + `style.css` của launchstudio.eu (22/10/2026) · testimonial Jasper lấy nguyên văn từ trang chủ NL/EN
> **Giới hạn:** tối đa 5 section nội dung (header và footer không tính)

---

## 1. ⚠️ Ba điều cần biết trước khi build

### ① Trang này mở rộng định vị, nên phải nói rõ ai làm gì

Mọi trang trước đều kể chuyện **"giữ nguyên frontend, không build lại"**. Trang này ngược lại: khách **chưa có gì ngoài ý tưởng**, LaunchStudio làm **toàn bộ phần kỹ thuật**, từ UX/UI tới frontend, backend, AI, thanh toán, bảo mật và hosting.

Để hai thông điệp không đá nhau:
- Hero chia vai rõ ràng: **"Jij brengt het idee" / "Wij bouwen de rest"**.
- Cuối S2 có một dòng cho người **đã có prototype**, dẫn về trang chủ (luồng launch-ready). Đây đúng là cơ chế phân luồng `Heb je al iets gebouwd?` mà roadmap §1③ đề xuất, chỉ gọn hơn.

### ② Song ngữ: một file, hai URL

launchstudio.eu dùng hai URL riêng (`/` = NL, `/en/` = EN), và nút `EN | NL` trên header là **link** sang URL kia. Prompt yêu cầu Lovable làm như sau:
- Toàn bộ chữ (kể cả nhãn trong hình SVG, `<title>`, meta description, FAQ schema) nằm trong **một từ điển `COPY = {nl:{…}, en:{…}}`**.
- Ngôn ngữ xác định theo thứ tự: `?lang=` → đường dẫn bắt đầu bằng `/en/` → mặc định `nl`.
- Trên `launchstudio.eu`, nút `EN | NL` chuyển sang URL tương ứng (giữ nguyên query string). Trên bản preview của Lovable, nút đổi ngôn ngữ tại chỗ.
- HTML tĩnh chứa sẵn bản NL, nên trang vẫn chạy khi không có JS.

**URL đề xuất:**

| | URL | hreflang |
|---|---|---|
| NL | `launchstudio.eu/ai-app-laten-bouwen/` | `nl-NL` + `x-default` |
| EN | `launchstudio.eu/en/build-ai-app-from-scratch/` | `en` |

> ⚠️ Roadmap §3 đã xếp **`/app-laten-maken` (630/tháng)** là trang P1 riêng. Trang này nhắm *AI-app*, không thay thế trang đó. Nếu sau này làm `/app-laten-maken` thì hai trang phải link chéo, và H1 phải khác nhau để không ăn thịt từ khoá của nhau.

### ③ Header và footer: dựng lại 1:1 từ site thật

Khác với 5 brief trước (footer chỉ một dòng), lần này prompt mô tả **chính xác** header và footer của launchstudio.eu: logo SVG, menu 6 mục, nút chuyển ngôn ngữ, nút `Gratis offerte`, menu mobile dưới 960px, footer 2 tầng với logo Manifera, thanh promo dưới đáy. Toàn bộ CSS lấy từ `style.css` của theme.

> 🔴 Nếu template WordPress dùng để dán trang **đã tự in header/footer của theme**, hãy xoá header/footer trong file Lovable (hoặc dùng template trống), nếu không trang sẽ có hai header.

---

## 2. 🎨 Phong cách: "Bản vẽ thành sản phẩm" (the build stack)

**Một hình minh hoạ cho cả trang:** một chồng 6 lớp xếp dần từ dưới lên, mỗi lớp là một phần việc LaunchStudio làm. Bên trái là thẻ **"Jouw idee"** (bóng đèn, của khách), bên trên cùng là cửa sổ trình duyệt `jouwapp.nl` gắn nhãn **Live**.

```
            ┌──────────────── jouwapp.nl ── ● Live ┐
            └──────────────────────────────────────┘
                          ▲
   ┌─────────┐   ┌── 01 UX/UI-ontwerp ───────────┐
   │ 💡 Jouw │   ├── 02 Frontend ────────────────┤
   │  idee   │ ⇢ ├── 03 Backend & database ──────┤
   └─────────┘   ├── 04 AI-functies ─────────────┤
                 ├── 05 Accounts & betalingen ───┤
                 └── 06 Beveiliging & hosting ───┘
```

| Vị trí | Trạng thái |
|---|---|
| **S1 Hero** | Animation chạy một lần: ý tưởng toả một đường chấm → 6 lớp trượt vào từ dưới lên → cửa sổ app hiện ra → chấm `Live` xanh nhấp nháy nhẹ |
| **S2** | Số thứ tự 01–06 của 6 thẻ **trùng với 6 lớp** trong hình hero → người đọc thấy ngay "mỗi lớp là một phần việc" |
| **S5 CTA cuối** | Bản thu nhỏ, tĩnh, chồng lớp đã hoàn chỉnh |

**Khác các trang trước:** vibe-coding (khung chat tối) · into-production (bảng đếm ngược) · security (thấu kính X-ray) · integrations (dây dẫn pastel) · prototype-to-production NL (cầu kéo) → trang này: **chồng lớp xếp hình, nền trắng, sạch**.

---

## 3. 📝 Cấu trúc: 5 section

| # | Section | Vai trò | Thông điệp (NL / EN) |
|---|---|---|---|
| — | **Header** | Giữ nguyên site | Logo · Proces · Schatting · Pakketten · Cases & FAQ · Contact · Inzichten · `EN|NL` · Gratis offerte |
| S1 | **Hero: từ ý tưởng tới sản phẩm hoàn chỉnh** | 🪝 Định vị | `Je AI-app laten bouwen vanaf nul. Van idee tot live product.` / `Your AI app, built from scratch. From idea to live product.` + khối "Jij brengt / Wij bouwen" |
| S2 | Wat we bouwen | Phạm vi full-stack | 6 thẻ = 6 lớp: UX/UI · Frontend · Backend & database · AI · Accounts & betalingen · Beveiliging & hosting |
| S3 | Werkwijze | Quy trình | Idee & scope → Eerst het ontwerp → Bouwen met wekelijkse demo → Live en van jou |
| S4 | Waarom LaunchStudio + FAQ | Bằng chứng + GEO | 11+ · 160+ · 100% · testimonial Jasper · 5 câu FAQ có schema |
| S5 | **Final CTA** | 🎯 | `Jij hebt het idee. Wij bouwen het.` / `You have the idea. We'll build it.` |
| — | **Footer** + thanh promo | Giữ nguyên site | Launch Studio · door Manifera · 6 link · © 2026 · tagline |

Không có bảng giá. Câu hỏi giá trong FAQ dẫn sang calculator trên trang chủ (`/#calculator`), nên không phải bịa con số.

---

## 4. 🤖 Prompt cho Lovable.dev

> Dán nguyên khối. Hướng dẫn viết bằng tiếng Anh (Lovable hiểu tốt hơn), **toàn bộ nội dung trang có đủ hai bản NL và EN**.

```
Build a single, self-contained, BILINGUAL (Dutch + English) landing page as ONE static
`index.html` file: all CSS in one inline <style> block, all JS in one inline <script>
block. No React, no build step, no router, no external dependencies except the three
font links below and one image URL (the Manifera logo). It will be pasted into a
WordPress page template, so it must work standalone.

WHAT THIS PAGE IS
LaunchStudio (by Manifera, 11+ years of software engineering, 160+ projects delivered)
builds complete AI apps FROM SCRATCH. The client brings only the IDEA. LaunchStudio does
EVERYTHING technical: product and UX/UI design, frontend, backend and database, AI
features, accounts and payments, security, hosting and launch. The result is a finished,
live product on the client's own domain; the code is 100% the client's.
Audience: non-technical founders in the Netherlands/EU who have an idea but nothing
built yet. Tone: calm, confident, warm, plain language, no hype, no jargon walls.
The page has EXACTLY: header, 5 content sections, footer, promo bar. No pricing section,
no form; every CTA links out.

=== LANGUAGES (critical) ===
- Every visible string (including SVG labels, button text, aria-labels, the visually
  hidden illustration description, <title>, meta description and the FAQPage JSON-LD)
  lives in ONE JS dictionary: const COPY = { nl: {...}, en: {...} }. Elements carry
  data-i18n="key" (or data-i18n-html="key" when the value contains inline markup such
  as <span class="gd">).
- The static HTML is rendered in DUTCH (<html lang="nl">) so the page works without JS.
- Language detection order: ?lang=nl|en in the URL → else pathname starts with "/en/"
  → else "nl".
- const PAGE_URL = { nl: "https://launchstudio.eu/ai-app-laten-bouwen/",
                     en: "https://launchstudio.eu/en/build-ai-app-from-scratch/" };
- The header EN | NL toggle: if location.hostname === "launchstudio.eu", navigate to
  PAGE_URL[lang] keeping the current query string; otherwise (preview) switch the
  language in place without reload and set ?lang= via history.replaceState.
- Switching language also: sets <html lang>, document.title, meta description, swaps
  every header/footer link href to that language's URL (see HEADER/FOOTER), swaps the
  FAQ JSON-LD, moves the .active class on the toggle, and keeps the scroll position.
- In <head>: <link rel="alternate" hreflang="nl-NL" href="{PAGE_URL.nl}">,
  <link rel="alternate" hreflang="en" href="{PAGE_URL.en}">,
  <link rel="alternate" hreflang="x-default" href="{PAGE_URL.nl}">, and a canonical
  pointing to the current language's PAGE_URL.
- Dutch headings use Dutch sentence case. English headings use sentence case too.
- Title NL: "AI-app laten bouwen vanaf nul | Launch Studio"
  Title EN: "Build your AI app from scratch | Launch Studio"
  Meta NL: "Jij brengt het idee, wij bouwen de complete AI-app: UX/UI, frontend,
  backend, AI, betalingen, beveiliging en hosting. Vaste prijs, code van jou."
  Meta EN: "You bring the idea, we build the complete AI app: UX/UI, frontend,
  backend, AI, payments, security and hosting. Fixed price, your code."

=== BRAND — KEEP EXACTLY (copied from launchstudio.eu style.css) ===
:root{--navy:#0B1D35;--bg:#F8FAFE;--white:#FFF;--ok:#0D9668;--red:#DC2626;
--amb:#D97706;--gs:#2F80ED;--ge:#14B8A6;
--grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);--text:#0B1D35;--ts:#384860;
--tm:#64748B;--tf:#94A3B8;--bd:#E2E8F0;--bs:#EEF2F7;
--fh:'Satoshi',system-ui,sans-serif;--fb:'Inter',system-ui,sans-serif;
--fa:'Instrument Serif',Georgia,serif;--r:12px;--rs:10px;--rp:999px;--rl:20px;
--rx:24px;
--ss:0 0 0 1px rgba(0,0,0,.03),0 2px 4px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04);
--sm:0 0 0 1px rgba(0,0,0,.02),0 4px 8px rgba(0,0,0,.03),0 16px 32px rgba(0,0,0,.06);
--sl:0 0 0 1px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04),0 24px 48px rgba(0,0,0,.08);
--t:.28s;--ease:cubic-bezier(.22,1,.36,1)}
.w{max-width:1120px;margin:0 auto;padding:0 40px}  (20px under 640px)
.gd = gradient text: background:var(--grd); -webkit-background-clip:text;
  -webkit-text-fill-color:transparent; background-clip:text.
Body: var(--fb), var(--ts), background var(--bg). Links have no underline.

FONTS — exactly these three, never substitute. Satoshi is from Fontshare:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">

SHARED ARROW ICON — put once at the top of <body> in a hidden <svg>, reuse via <use>:
<symbol id="ia" viewBox="0 0 14 14"><path d="M3 7h8M7.5 3.5l3.5 3.5-3.5 3.5"
stroke="currentColor" stroke-width="1.7" stroke-linecap="round"
stroke-linejoin="round" fill="none"/></symbol>

BUTTONS (site exact):
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--grd);color:#fff;
font-family:var(--fh);font-size:15px;font-weight:600;padding:14px 32px;
border-radius:16px;box-shadow:0 8px 24px rgba(47,128,237,.18),0 3px 6px rgba(11,29,53,.08);
transition:all var(--t) var(--ease);border:none;cursor:pointer}
.btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(47,128,237,.22),
0 6px 14px rgba(11,29,53,.1)} .btn svg{width:12px;height:12px;transition:transform .2s}
.btn:hover svg{transform:translateX(2px)}
Secondary .b2: same size and radius, background var(--white), color var(--navy),
1px solid var(--bd), box-shadow var(--ss); hover border-color var(--gs).

=== HEADER — REPLICATE launchstudio.eu EXACTLY ===
Markup (keep class names and structure):
<nav class="nav" id="mainNav">
 <div class="ni">
  <a class="nav-logo" href="{home}">
   <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
    <defs><linearGradient id="lg1" x1="0" y1="32" x2="32" y2="0"
     gradientUnits="userSpaceOnUse"><stop stop-color="#2563EB"/>
     <stop offset="1" stop-color="#14B8A6"/></linearGradient></defs>
    <rect x="1" y="8" width="22" height="22" rx="4" stroke="url(#lg1)"
     stroke-width="2" fill="none"/>
    <path d="M7 17l4 4-4 4" stroke="#0B1D35" stroke-width="2" stroke-linecap="round"
     stroke-linejoin="round"/>
    <path d="M15 24h4" stroke="#0B1D35" stroke-width="2" stroke-linecap="round"/>
    <path d="M19 2l11 0 0 11" stroke="url(#lg1)" stroke-width="2.2"
     stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M30 2L18 14" stroke="url(#lg1)" stroke-width="2.2" stroke-linecap="round"/>
   </svg>
   <div><div class="lt">Launch Studio</div><div class="lby">{door|by} Manifera</div></div>
  </a>
  <button class="nav-toggle" id="navToggle" aria-controls="mainNavPanel"
   aria-expanded="false"> 3 lines + <span class="sr-only">Toggle navigation</span></button>
  <div class="nav-menu" id="mainNavPanel">
   <ul class="nl2"> 6 links (below) </ul>
   <div class="nr">
    <div class="ltg"><a class="lbtn" id="langEN">EN</a><a class="lbtn" id="langNL">NL</a></div>
    <a class="btn" href="{contact}">{Gratis offerte|Free quote} <svg><use href="#ia"/></svg></a>
   </div>
  </div>
 </div>
 <button class="nav-backdrop" id="navBackdrop" aria-label="Close navigation"></button>
</nav>

Header links per language:
 NL: Launch Studio logo → https://launchstudio.eu/
     Proces → https://launchstudio.eu/#process
     Schatting → https://launchstudio.eu/#calculator
     Pakketten → https://launchstudio.eu/#packages
     Cases & FAQ → https://launchstudio.eu/#proof
     Contact → https://launchstudio.eu/#contact
     Inzichten → https://launchstudio.eu/nl/inzichten/
     Button "Gratis offerte" → https://launchstudio.eu/#contact
 EN: logo → https://launchstudio.eu/en/
     Process → https://launchstudio.eu/en/#process
     Estimate → https://launchstudio.eu/en/#calculator
     Packages → https://launchstudio.eu/en/#packages
     Cases & FAQ → https://launchstudio.eu/en/#proof
     Contact → https://launchstudio.eu/en/#contact
     Insights → https://launchstudio.eu/insights/
     Button "Free quote" → https://launchstudio.eu/en/#contact

Header CSS (site exact):
.nav{position:sticky;top:0;z-index:200;background:rgba(248,250,254,.72);
backdrop-filter:blur(20px) saturate(1.2);-webkit-backdrop-filter:blur(20px) saturate(1.2);
border-bottom:1px solid rgba(226,232,240,.6);transition:background .3s,box-shadow .3s}
.nav.scrolled{background:rgba(248,250,254,.92);box-shadow:0 1px 0 rgba(0,0,0,.04),
0 4px 16px rgba(0,0,0,.04)}
.nav::after{content:'';position:absolute;bottom:-2px;left:0;right:0;height:2px;
background:var(--grd);opacity:0;transition:opacity .3s} .nav.scrolled::after{opacity:1}
.ni{display:flex;align-items:center;justify-content:space-between;gap:16px;height:72px;
max-width:1120px;margin:0 auto;padding:0 40px;position:relative;z-index:2}
.nav-logo{display:flex;align-items:center;gap:11px}
.lt{font-family:var(--fh);font-weight:700;font-size:19px;letter-spacing:-.4px;color:var(--navy)}
.lby{font-size:11px;font-weight:500;color:var(--tf);letter-spacing:.03em}
.nav-menu{display:flex;align-items:center;gap:22px;margin-left:auto}
.nl2{display:flex;align-items:center;gap:22px;list-style:none;margin:0;padding:0}
.nl2 a{font-size:13.5px;font-weight:500;color:var(--tm);transition:color var(--t);position:relative}
.nl2 a::after{content:'';position:absolute;bottom:-3px;left:0;width:0;height:1.5px;
background:var(--grd);transition:width .3s var(--ease)}
.nl2 a:hover{color:var(--navy)} .nl2 a:hover::after{width:100%}
.nr{display:flex;align-items:center;gap:14px}
.nav-toggle{display:none;align-items:center;justify-content:center;width:44px;height:44px;
border-radius:var(--rs);border:1px solid var(--bd);background:rgba(255,255,255,.75);
color:var(--navy);box-shadow:0 1px 2px rgba(11,29,53,.04)}
.nav-toggle-lines{width:18px;height:12px;display:inline-flex;flex-direction:column;
justify-content:space-between}
.nav-toggle-lines span{display:block;width:100%;height:2px;border-radius:999px;
background:currentColor;transition:transform .25s var(--ease),opacity .2s var(--ease)}
.nav.open .nav-toggle-lines span:nth-child(1){transform:translateY(5px) rotate(45deg)}
.nav.open .nav-toggle-lines span:nth-child(2){opacity:0}
.nav.open .nav-toggle-lines span:nth-child(3){transform:translateY(-5px) rotate(-45deg)}
.nav-backdrop{display:none;position:fixed;inset:0;border:0;background:rgba(11,29,53,.18);
backdrop-filter:blur(2px);opacity:0;visibility:hidden;pointer-events:none;z-index:1}
.nav.open .nav-backdrop{opacity:1;visibility:visible;pointer-events:auto}
.ltg{display:flex;background:rgba(11,29,53,.05);border:1px solid var(--bd);
border-radius:var(--rp);overflow:hidden;height:34px}
.lbtn{font-family:var(--fh);font-size:12px;font-weight:600;color:var(--tm);padding:0 13px;
height:100%;display:flex;align-items:center;transition:all var(--t);cursor:pointer}
.lbtn.active{background:var(--white);color:var(--navy);box-shadow:0 0 0 1px rgba(0,0,0,.03),
0 1px 2px rgba(0,0,0,.04)}
The header's "Gratis offerte" .btn is smaller: padding 10px 20px, font-size 13.5px.
@media(max-width:960px){ .nav-menu becomes a dropdown panel: position:absolute;
top:calc(100% - 1px);left:0;right:0;display:grid;gap:18px;padding:18px 40px 22px;
background:rgba(248,250,254,.98);border-bottom:1px solid rgba(226,232,240,.85);
box-shadow:0 24px 40px rgba(11,29,53,.08);opacity:0;visibility:hidden;
transform:translateY(-8px);pointer-events:none; .nav.open .nav-menu → visible, no
transform; .nav-toggle displayed; .nl2 vertical, gap 14px, links 15px var(--navy);
.nr full width, space-between, padding-top 18px, border-top 1px solid var(--bd);
.nav.open .nav-backdrop display:block }
@media(max-width:640px){ .ni and .nav-menu side padding 20px; .nr stacks vertically
(gap 12px, stretch); .ltg full width with both .lbtn flex:1 centred; header .btn full
width centred }
JS: add .scrolled to .nav when scrollY > 8. Toggle button and backdrop toggle .open on
.nav, body.nav-open (overflow:hidden) and aria-expanded; Escape and any menu link click
close it.

=== FOOTER — REPLICATE launchstudio.eu EXACTLY ===
<footer><div class="w">
 <div class="frow">
  <div>
   <div class="fbr">Launch Studio</div>
   <div class="fby">{Meer dan 11 jaar productie-ervaring | 11+ years of production experience}</div>
   <div class="fby-author"><span>{door|by}</span>
    <a href="https://www.manifera.com/?utm_source=launchstudio&utm_medium=logo-footer"
     target="_blank" rel="noopener noreferrer">
     <img src="https://launchstudio.eu/wp-content/uploads/2026/08/manifera-logo.webp"
      alt="Manifera Logo" class="fby-logo"></a></div>
  </div>
  <div class="fls"> 6 links (below) </div>
 </div>
 <div class="fbt"><span class="fcop">© 2026 LaunchStudio</span>
  <span class="ftag">{tagline}</span></div>
</div></footer>
Footer links:
 NL: Inzichten → https://launchstudio.eu/inzichten · Pakketten → https://launchstudio.eu/#packages
     · Veelgestelde vragen → https://launchstudio.eu/#proof · Contact →
     https://launchstudio.eu/#contact · Privacybeleid → https://launchstudio.eu/privacybeleid
     · Algemene voorwaarden → https://launchstudio.eu/algemene-voorwaarden
     Tagline: "Van prototype naar productie. Snel, veilig, van jou."
 EN: Insights → https://launchstudio.eu/en/insights · Packages → https://launchstudio.eu/en/#packages
     · FAQ → https://launchstudio.eu/en/#proof · Contact → https://launchstudio.eu/en/#contact
     · Privacy Policy → https://launchstudio.eu/en/privacy-policy · Terms & Conditions →
     https://launchstudio.eu/en/terms-and-conditions
     Tagline: "From prototype to production. Fast, secure, yours."
Footer CSS (site exact):
footer{padding:48px 0 36px;border-top:2px solid transparent;border-image:var(--grd) 1}
.frow{display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;
gap:24px;margin-bottom:32px}
.fbr{font-family:var(--fh);font-weight:700;font-size:18px;color:var(--navy)}
.fby{font-size:11px;color:var(--tf);margin-top:3px}
.fby-author{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--tf);margin-top:4px}
.fby-author .fby-logo{height:25px;width:auto}
.fls{display:flex;gap:24px;flex-wrap:wrap} .fls a{font-size:13px;color:var(--tm)}
.fls a:hover{color:var(--navy)}
.fbt{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;
border-top:1px solid var(--bd);padding-top:24px}
.fcop{font-size:12px;color:var(--tf)} .ftag{font-size:12px;color:var(--tf);font-style:italic}
@media(max-width:640px){footer{padding-bottom:72px}}

PROMO BAR (site exact, after the footer):
<div class="promo" id="promoBar"><div class="w"><div class="pi">
 <span class="ptx">{Er zijn deze maand nog 2 plekken beschikbaar. | 2 spots remaining this month}</span>
 <a class="pbtn" data-cta>{Gratis offerte|Free quote} <svg width="11" height="11"><use href="#ia"/></svg></a>
 <span class="px" id="promoClose" role="button" aria-label="Sluiten / Close">&times;</span>
</div></div></div>
.promo{position:fixed;bottom:-100px;left:0;right:0;z-index:190;background:var(--navy);
padding:12px 0;transition:bottom .5s var(--ease);box-shadow:0 -4px 24px rgba(0,0,0,.15)}
.promo.show{bottom:0}
.pi{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap}
.ptx{color:rgba(255,255,255,.65);font-size:13.5px}
.pbtn{display:inline-flex;align-items:center;gap:6px;background:var(--grd);color:#fff;
font-family:var(--fh);font-size:12.5px;font-weight:600;padding:8px 18px;border-radius:var(--rs)}
.px{color:rgba(255,255,255,.3);font-size:18px;cursor:pointer;padding:4px 8px;line-height:1}
.px:hover{color:#fff}
JS: show (.show) after the user scrolls past 35% of the page; hide while S5 is in view;
close button hides it for the session (sessionStorage in try/catch).

=== PAGE STYLE ("from blueprint to product") ===
- White and var(--bg) backgrounds only, except the S5 card which is var(--navy). No
  background grids, no glassmorphism outside the header, no monospace font.
- Typography (site style): h1 var(--fh) 700, clamp(38px,5vw,60px), line-height 1.06,
  letter-spacing -1.8px, var(--navy) · h2 var(--fh) 700, clamp(28px,3.4vw,42px),
  line-height 1.12, letter-spacing -1px · h3 var(--fh) 700, 18px · body 16.5px/1.7.
- Section eyebrow (site hero style): inline-flex, gap 8px, 11px, weight 700,
  letter-spacing .06em, uppercase, var(--gs), with a 7px gradient dot (.hdot) before it.
- Cards: white, 1px solid var(--bd), radius var(--rl), box-shadow var(--ss); hover:
  border-color rgba(47,128,237,.3), box-shadow var(--sm), translateY(-2px).
- var(--fa) italic for at most two phrases on the page (the testimonial and one word
  in S4's H2 are fine).
- Sections: padding 104px 0 desktop, 72px 0 mobile. Gentle 400ms fade-up as each block
  enters view (IntersectionObserver). Only the hero illustration is truly animated.

ILLUSTRATION — "THE BUILD STACK" (inline SVG, flat vector, used in S1 and S5):
- Left: a white card "Jouw idee / Your idea" (radius 16, 1px var(--bd)) with a simple
  lightbulb icon in gradient stroke and two short grey "handwritten note" lines.
- A dotted gradient line flows from the idea card into the stack.
- Centre/right: SIX horizontal layers stacked bottom-up, each a white rounded bar
  (radius 12, 1px var(--bd), small 2px gradient left edge), with a 10px var(--fh) 700
  number in var(--gs) and a 12px var(--fh) 600 var(--navy) label:
    01 UX/UI-ontwerp / UX/UI design          (top)
    02 Frontend / Frontend
    03 Backend & database / Backend & database
    04 AI-functies / AI features
    05 Accounts & betalingen / Accounts & payments
    06 Beveiliging & hosting / Security & hosting   (bottom)
  Each layer has one tiny line-icon on its right (pen, layout, server, sparkle, card,
  shield), 1.6px var(--navy) stroke.
- On top of the stack: a browser window (rounded, 3 grey dots, address pill
  "jouwapp.nl" / "yourapp.com") with a minimal app screen inside (a header bar, two
  cards, a chat bubble hinting at AI) and a pill "● Live" in var(--ok).
- Labels in the SVG come from COPY (data-i18n), min 11px, never clipped in either
  language (EN labels are longer: size the bars for the longer string).
- S1 animation (once, when in view): idea card fades in (300ms) → dotted line draws
  (stroke-dashoffset, 600ms) → layers slide up and fade in from 06 to 01, 140ms apart
  → browser window drops in (400ms) → "Live" dot then pulses softly every 2.4s forever.
  Hover/focus on a layer highlights it (border var(--gs)) and highlights the S2 card
  with the same number if visible. prefers-reduced-motion: final state, no pulse.

=== SECTIONS, IN ORDER (exactly five) ===

S1 HERO — FROM NOTHING TO FINISHED PRODUCT. Background var(--bg). CSS grid 1.05fr 1fr,
gap 56px, vertically centred: copy LEFT, build-stack illustration RIGHT. Mobile: copy,
then illustration full width.
- Eyebrow: NL "Voor founders met een idee" · EN "For founders with an idea"
- H1 (data-i18n-html):
  NL 'Je AI-app laten bouwen vanaf nul. <span class="gd">Van idee tot live product.</span>'
  EN 'Your AI app, built from scratch. <span class="gd">From idea to live product.</span>'
- Lead, 18px, max 540px:
  NL "Jij brengt het idee. Wij doen de rest: UX/UI-ontwerp, frontend, backend,
  database, AI-functies, betalingen, beveiliging en hosting. Eén team, één vaste prijs,
  en een app die vanaf dag één klaar is voor echte gebruikers."
  EN "You bring the idea. We do everything else: UX/UI design, frontend, backend,
  database, AI features, payments, security and hosting. One team, one fixed price, and
  an app that's ready for real users from day one."
- ROLE SPLIT — two compact side-by-side boxes (stack under 520px), radius var(--r):
  Box 1, white, 1px var(--bd): title with a small lightbulb icon
    NL "Jij brengt" · EN "You bring"
    items (small grey dots): NL "Het idee" · "Je kennis van je klanten" · "Je feedback
    op elk ontwerp" — EN "The idea" · "Knowledge of your customers" · "Your feedback on
    every design"
  Box 2, background rgba(47,128,237,.06), 1px solid rgba(47,128,237,.25): title with a
  small gradient check icon
    NL "Wij bouwen" · EN "We build"
    one line, var(--navy) 600: NL "Alles wat technisch is, van eerste schets tot live
    app." EN "Everything technical, from first sketch to live app."
- Buttons: primary .btn NL "Vraag een gratis offerte aan" / EN "Get a free quote"
  (data-cta) · secondary .b2 NL "Bekijk wat we bouwen" / EN "See what we build"
  (href #wat-we-bouwen).
- Trust row, 13.5px var(--tm), small gradient check icons, separated by dots:
  NL "Vaste prijs vooraf" · "Code 100% van jou" · "11+ jaar engineering via Manifera"
  EN "Fixed price upfront" · "100% your code" · "11+ years of engineering via Manifera"
- Visually hidden description of the illustration:
  NL "Illustratie: jouw idee wordt laag voor laag een complete app: ontwerp, frontend,
  backend, AI, betalingen en beveiliging, tot hij live staat."
  EN "Illustration: your idea becomes a complete app layer by layer: design, frontend,
  backend, AI, payments and security, until it's live."

S2 WHAT WE BUILD — id="wat-we-bouwen". Background white.
- Eyebrow: NL "Wat we bouwen" · EN "What we build"
- H2: NL "Alles wat je app nodig heeft. Door één team."
      EN "Everything your app needs. Built by one team."
- Sub, max 640px: NL "Geen losse freelancers voor design, frontend en backend die
  elkaar nooit gesproken hebben. Eén team dat het hele product bouwt en ervoor instaat."
  EN "No separate freelancers for design, frontend and backend who've never spoken to
  each other. One team that builds the whole product and stands behind it."
- SIX cards, 3x2 grid (2 columns under 960px, 1 under 640px). Each card: number
  01–06 (var(--fh) 700 13px var(--gs)) + the same line-icon as its layer, h3, one
  paragraph 15px, then a row of small chips (12px, var(--bs) background, var(--tm),
  radius var(--rp), padding 4px 10px). Each card has data-layer="01".."06".
  01 NL "Product & UX/UI-ontwerp" — "We vertalen je idee naar gebruikersflows,
     wireframes en een klikbaar ontwerp dat je goedkeurt voordat er één regel code
     wordt geschreven." chips: "User flows" "Wireframes" "Figma"
     EN "Product & UX/UI design" — "We turn your idea into user flows, wireframes and a
     clickable design you approve before a single line of code is written."
     chips: "User flows" "Wireframes" "Figma"
  02 NL "Frontend" — "Snelle, responsive schermen die op elke telefoon en laptop
     werken, en toegankelijk zijn voor iedereen." chips "React" "Next.js" "React Native"
     EN "Frontend" — "Fast, responsive screens that work on every phone and laptop, and
     are accessible to everyone." chips same
  03 NL "Backend & database" — "De logica, API's en data achter je app: veilig
     opgeslagen, goed gestructureerd en klaar om te groeien." chips "Node.js" "Python"
     "PostgreSQL" "Supabase"
     EN "Backend & database" — "The logic, APIs and data behind your app: stored
     safely, well structured and ready to grow." chips same
  04 NL "AI-functies" — "Het slimme deel van je app: een assistent die vragen
     beantwoordt, zoeken in je eigen documenten, samenvatten en automatiseren. Met de
     kosten en privacy onder controle." chips "LLM's" "RAG" "Automatisering"
     EN "AI features" — "The smart part of your app: an assistant that answers
     questions, search across your own documents, summarising and automation. With
     costs and privacy under control." chips "LLMs" "RAG" "Automation"
  05 NL "Accounts, betalingen & koppelingen" — "Inloggen, gebruikersrollen,
     abonnementen, betalen met iDEAL en koppelingen met de tools die je al gebruikt."
     chips "Stripe" "Mollie" "iDEAL" "E-mail"
     EN "Accounts, payments & integrations" — "Login, user roles, subscriptions,
     payments with iDEAL and connections to the tools you already use."
     chips "Stripe" "Mollie" "iDEAL" "Email"
  06 NL "Beveiliging, hosting & lancering" — "Veilig vanaf de eerste dag, automatisch
     getest en uitgerold, met back-ups en monitoring. Live op je eigen domein."
     chips "CI/CD" "Monitoring" "Vercel" "AWS" "Azure"
     EN "Security, hosting & launch" — "Secure from day one, automatically tested and
     deployed, with backups and monitoring. Live on your own domain." chips same
- Below the grid, one centred line, 15px var(--tm), on a var(--bg) pill with 1px
  var(--bd) border:
  NL "Al iets gebouwd met Lovable, Bolt of Cursor? Dan beginnen we niet opnieuw."
     + link "Maak je prototype launch-ready →" → https://launchstudio.eu/
  EN "Already built something with Lovable, Bolt or Cursor? Then we don't start over."
     + link "Make your prototype launch-ready →" → https://launchstudio.eu/en/
  (link in var(--gs) 600; carry the attribution params; add from=scratch-page)

S3 HOW IT WORKS — id="werkwijze". Background var(--bg).
- Eyebrow: NL "Werkwijze" · EN "How it works"
- H2: NL "Van idee naar live app in vier stappen."
      EN "From idea to live app in four steps."
- Four steps in a row (2x2 under 960px, 1 column under 640px), connected on desktop
  by a 2px line that fills with var(--grd) from left to right as the section scrolls
  into view (once; static and full under reduced motion). Each step: a 44px white
  circle with 1px var(--bd) and the number in gradient text, h3, one paragraph.
  1 NL "Idee en scope" — "In een kennismaking van 15 minuten vertel je wat je wilt
    bouwen, in gewone taal. Daarna krijg je een vaste scope, planning en prijs op
    papier."
    EN "Idea and scope" — "In a 15-minute intro call you tell us what you want to
    build, in plain language. Then you get a fixed scope, timeline and price in
    writing."
  2 NL "Eerst het ontwerp" — "Je ziet en klikt door je app voordat we gaan bouwen. Pas
    als jij tevreden bent, schrijven we code."
    EN "Design first" — "You see and click through your app before we build it. We
    only write code once you're happy."
  3 NL "Bouwen, met elke week een demo" — "Je volgt de voortgang in een werkende
    versie, niet in statusrapporten."
    EN "Build, with a demo every week" — "You follow progress in a working version, not
    in status reports."
  4 NL "Live en van jou" — "Getest en live op je eigen domein, met 48 uur support na de
    lancering. Code, repo en accounts staan op jouw naam."
    EN "Live and yours" — "Tested and live on your own domain, with 48 hours of support
    after launch. Code, repo and accounts are in your name."
- Under the steps, centred: secondary .b2 NL "Plan een kennismaking van 15 minuten"
  / EN "Book a 15-minute intro call" (data-cta, adds type=call).

S4 WHY LAUNCHSTUDIO + FAQ — id="waarom". Background white.
- Eyebrow: NL "Waarom LaunchStudio" · EN "Why LaunchStudio"
- H2 (data-i18n-html): NL 'Gebouwd met AI-snelheid. Afgemaakt door
  <em>engineers</em>.' · EN 'Built at AI speed. Finished by <em>engineers</em>.'
  (em = var(--fa) italic, weight 400, gradient text)
- Stats row, three items, number var(--fh) 700 48px gradient text, label 14px var(--tm):
  "11+" NL "jaar engineering via Manifera" / EN "years of engineering via Manifera"
  "160+" NL "projecten opgeleverd" / EN "projects delivered"
  "100%" NL "van de code is van jou" / EN "of the code is yours"
- Three short points in a row (stack on mobile), each with a small gradient icon, h3
  and one line:
  NL "Sneller dan een bureau" — "AI waar het tijd bespaart, engineers waar het ertoe
     doet. Weken, geen maanden."
  EN "Faster than an agency" — "AI where it saves time, engineers where it matters.
     Weeks, not months."
  NL "Eén vaste prijs" — "Geen uurtje-factuurtje. Je weet vooraf wat het kost."
  EN "One fixed price" — "No hourly billing. You know the cost upfront."
  NL "Geen lock-in" — "Je code, je data, je accounts. Elke ontwikkelaar kan er later
     mee verder."
  EN "No lock-in" — "Your code, your data, your accounts. Any developer can pick it up
     later."
- One testimonial card, max 760px centred: quote in var(--fa) italic 22px var(--navy),
  then "Jasper" 600 and role 14px var(--tm):
  NL „Als SaaS-oprichter wil je snel en tegen lage kosten testen en lanceren. Ik lever
     mijn ideeën aan, zij bouwen het uit. Het kost me slechts 20% van wat ik normaal
     gesproken aan ontwikkeltijd zou uitgeven." — "Jasper · Founder, Wisey (EdTech)"
  EN "As a SaaS founder, you want to test and ship fast, at a low cost. I deliver my
     ideas, they build it out. It costs me just 20% of what I'd normally spend on dev
     hours." — "Jasper · Founder, Wisey (EdTech)"
  <!-- VERIFY: on launchstudio.eu the quote says "ideeën aan in code" / "ideas in
  code". Shortened here on purpose; confirm with Jasper before publishing. -->
- FAQ, h3 NL "Veelgestelde vragen" / EN "Frequently asked questions", max 780px,
  <details>/<summary> accordion, plus icon rotating 45°, 1px var(--bd) separators.
  FAQPage JSON-LD in <script type="application/ld+json" id="faq-ld"> regenerated from
  COPY on every language switch.
  1 NL "Moet ik technisch zijn om een app te laten bouwen?" — "Nee. Jij kent je klanten
    en je idee, wij vertalen dat naar een werkend product. Jij beslist over elk
    ontwerp, wij nemen de techniek voor onze rekening."
    EN "Do I need to be technical to have an app built?" — "No. You know your customers
    and your idea; we turn that into a working product. You decide on every design, we
    take care of the technology."
  2 NL "Wat kost het om een AI-app te laten maken?" — "Dat hangt af van wat je app moet
    kunnen. Na de kennismaking krijg je een vaste prijs op papier. Een eerste schatting
    maak je in twee minuten met onze calculator." ("calculator" links to
    https://launchstudio.eu/#calculator)
    EN "How much does it cost to build an AI app?" — "It depends on what your app needs
    to do. After the intro call you get a fixed price in writing. You can get a first
    estimate in two minutes with our calculator." (→ https://launchstudio.eu/en/#calculator)
  3 NL "Hoe lang duurt het om een MVP te bouwen?" — "Meestal enkele weken, geen
    maanden. De precieze planning staat in je offerte, voordat we beginnen."
    EN "How long does it take to build an MVP?" — "Usually a few weeks, not months. The
    exact timeline is in your quote, before we start."
  4 NL "Van wie zijn het idee en de code?" — "Van jou. Altijd. Op verzoek tekenen we
    vooraf een NDA, en code, repo, domein en accounts staan op jouw naam."
    EN "Who owns the idea and the code?" — "You do. Always. On request we sign an NDA
    upfront, and the code, repo, domain and accounts are in your name."
  5 NL "Ik heb al een prototype. Moet alles opnieuw?" — "Nee. Dan maken we af wat je
    hebt in plaats van opnieuw te beginnen: beveiliging, betalingen, hosting en wat er
    verder nodig is om live te gaan."
    EN "I already have a prototype. Do we start over?" — "No. We finish what you have
    instead of starting over: security, payments, hosting and whatever else it takes
    to go live."
- Do NOT add client logos, certification badges or award seals.

S5 FINAL CTA — id="start". Background var(--bg); inside .w a card with background
var(--navy), radius var(--rx), padding 64px 48px (40px 24px mobile), CSS grid 1.2fr 1fr:
copy LEFT, a small STATIC version of the build stack RIGHT (complete, "Live" pill
green, white strokes at 85% opacity on navy, labels in #C3CEDF). Mobile: copy only, hide
the illustration under 640px.
- H2 (data-i18n-html), white: NL 'Jij hebt het idee. <span class="gd">Wij bouwen het.</span>'
  EN 'You have the idea. <span class="gd">We'll build it.</span>'
- Sub, 17px, #C3CEDF: NL "Vertel ons wat je wilt bouwen. We reageren binnen 1 werkdag
  om een gratis gesprek van 15 minuten in te plannen."
  EN "Tell us what you want to build. We reply within 1 working day to schedule a free
  15-minute call."
- Buttons: primary .btn NL "Vraag een gratis offerte aan" / EN "Get a free quote"
  (data-cta) · secondary: transparent, 1px solid rgba(255,255,255,.25), white text,
  NL "Plan 15 minuten kennismaking" / EN "Book a 15-minute intro" (data-cta, type=call).
- Small line 13px #94A3B8: NL "Geen verplichtingen. Je idee blijft van jou."
  EN "No obligations. Your idea stays yours."

=== JS (vanilla, small) ===
- const CTA_URL = { nl: "https://launchstudio.eu/#contact",
                    en: "https://launchstudio.eu/en/#contact" };
  // REPLACE with the real request/booking pages when they exist
  Every [data-cta] gets href = CTA_URL[lang] with query params inserted BEFORE the hash.
- Attribution: copy gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content from location.search onto every data-cta link, plus
  landing=build-ai-app-from-scratch, lang={nl|en}, and per-button params (type=call).
- i18n render function, language detection and toggle exactly as in LANGUAGES.
- Header scroll/open logic, promo bar logic, fade-up observer, hero animation (run once,
  pause the Live pulse when off-screen or tab hidden), layer ↔ card highlight, S3
  progress line.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML: exactly one <h1>, each section <section aria-labelledby>, <button> for
  actions, <a> for links. Illustrations aria-hidden with the visually hidden
  description in the current language.
- No horizontal scroll at 360px in either language; check the longest EN and NL
  strings (e.g. "Accounts, betalingen & koppelingen") wrap cleanly.
- Contrast at least 4.5:1 (including #C3CEDF on navy). Visible focus rings: 2px solid
  var(--ge), 3px offset.
- prefers-reduced-motion: no animations, every illustration in its final state.
- One HTML file, inline CSS and JS; only the three font links and the Manifera logo
  image are external.
```

---

## 5. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Người Hà Lan bản xứ đọc lại toàn bộ copy NL** | Nhất là: `Je AI-app laten bouwen vanaf nul`, `Gebouwd met AI-snelheid. Afgemaakt door engineers`, `Geen uurtje-factuurtje` |
| 2 | 🔴 **Xác nhận các cam kết quy trình mới** | Trang hứa thêm 3 điều **chưa có trên site**: *klikbaar ontwerp vóór code*, *wekelijkse demo*, *NDA op verzoek*. Nếu team không làm đúng như vậy, sửa hoặc xoá trước khi publish |
| 3 | 🔴 **Xác nhận "enkele weken" / "weken, geen maanden"** cho dự án làm từ đầu | Con số 1–3 tuần trên site là cho gói launch-ready, **không** áp cho build mới. Mình cố ý không ghi số tuần cụ thể |
| 4 | Xác nhận câu trích của Jasper | Prompt đã rút gọn "ideeën aan **in code**" thành "ideeën aan" để khớp trang này. Hoặc xin phép Jasper, hoặc dùng lại nguyên văn |
| 5 | **Chốt URL + hreflang** | `/ai-app-laten-bouwen/` ↔ `/en/build-ai-app-from-scratch/`. Sửa `PAGE_URL` nếu đổi |
| 6 | 🔴 **Header/footer trùng** | Nếu template WP đã in header/footer của theme thì xoá phần đó khỏi file Lovable (xem §1③) |
| 7 | Thay `CTA_URL` khi có trang `/audit-aanvragen` / `/request-audit` | Roadmap §2 (P0). Kiểm tra `gclid`, `utm_*`, `lang`, `type` có đi theo |
| 8 | Test chuyển ngôn ngữ | Trên preview: đổi tại chỗ. Trên launchstudio.eu: nhảy sang URL kia, giữ query. Kiểm `<title>`, meta, FAQ schema đổi theo |
| 9 | Test mobile 360px cả hai ngôn ngữ | Nhãn tiếng Anh trong hình chồng lớp dài hơn, không được bị cắt |
| 10 | Index cả hai bản | FAQ có `FAQPage` schema, phục vụ GEO NL + EN |
