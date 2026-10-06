# 🚀 Landing page `/ai-app-into-production` — Content brief + Lovable prompt

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-into-production` (hiện **404**)
> **Design reference:** `https://launchstudio.eu/` (NL) và `https://launchstudio.eu/en/` (EN)
> **Token đã trích trực tiếp từ** `wp-content/themes/launchstudio/style.css`

---

## 1. ⚠️ Đọc phần này trước khi build

Ba vấn đề cần quyết định trước, không phải sau.

### ① Luận điểm của trang này có ~0 lượt tìm kiếm

Theo `volume_analysis_results.md` (chính dữ liệu Keyword Planner của bạn): 27 keyword diễn đạt đúng luận điểm "làm nốt prototype AI" (`to production`, `naar productie`, `production ready`, `afmaken`, `live zetten`) có **tổng 10 lượt/tháng**. 26/27 bằng 0.

**Hệ quả:** đừng build trang này như một trang SEO. Nếu mục tiêu là organic traffic, nó sẽ thất bại — không phải vì làm sai, mà vì không có cầu.

### ② Trang chủ EN đã nói đúng luận điểm này

```
launchstudio.eu/en/   H1: "You built it with AI. We get it launch-ready."
                      H2: "You're stuck between prototype and production"
```

Nếu trang mới lặp lại thông điệp đó, hai trang sẽ **ăn thịt nhau** trong mắt Google, và không trang nào thắng.

### ③ URL nằm sai namespace ngôn ngữ

| URL | Ngôn ngữ |
|---|---|
| `launchstudio.eu/` | 🇳🇱 Tiếng Hà Lan |
| `launchstudio.eu/en/` | 🇬🇧 Tiếng Anh |
| `launchstudio.eu/ai-app-into-production` | ⚠️ Slug tiếng Anh trong namespace tiếng Hà Lan |

**Đề xuất:** dùng `launchstudio.eu/en/ai-app-into-production` cho bản EN, và nếu cần bản NL thì `launchstudio.eu/ai-app-naar-productie`. Gắn hreflang chéo giữa hai bản. Để slug tiếng Anh ở root sẽ làm hỏng cấu trúc hreflang hiện có.

---

## 2. ✅ Vậy trang này nên làm gì?

Ba việc — không có việc nào là "xếp hạng Google".

### Việc 1 — Landing page dành riêng cho ads (đo lường sạch)

Đây chính là thủ thuật trong `conversion_attribution_setup.md` §6: một URL **không có link nào trỏ tới từ menu, sitemap hay nội dung**. Mọi form submit từ URL đó chắc chắn đến từ ads — miễn nhiễm Safari ITP và cookie consent.

Nhận traffic từ campaign **B1-Lovable, B2-Bolt, B3-Replit** (530 lượt/tháng nhánh EN). Đây là người đã *dùng công cụ cụ thể* và chạm tường — khác với `app laten maken` (480/tháng, NL) là người muốn xây mới.

> 🔴 **Đừng dẫn traffic `app laten maken` vào đây.** Thông điệp lệch hoàn toàn: họ chưa có app nào để "đưa lên production". Giữ traffic đó ở trang NL hiện tại.

### Việc 2 — Tài sản GEO (và đây là lý do mạnh nhất)

Volume Google bằng 0 **không** có nghĩa là không ai cần. Nó có nghĩa là **người ta không diễn đạt vấn đề này bằng keyword**.

Vấn đề "tôi build bằng Lovable, giờ không biết đưa lên production thế nào" là loại vấn đề người ta **kể bằng cả câu cho ChatGPT**, không gõ 3 từ vào Google:

> *"I built an app with Lovable but I'm not sure it's secure enough to launch — what do I need to check?"*

Truy vấn đó không tồn tại trong Keyword Planner nhưng tồn tại rất nhiều trong LLM. Và LLM trích dẫn **nội dung có thực chất kỹ thuật**, không trích dẫn trang bán hàng.

**Đó là định vị đúng của trang này: trang có thực chất kỹ thuật nhất trên site.** Trang chủ là lời chào hàng; trang này là nội dung thật.

### Việc 3 — Tài sản bán hàng

Một URL để gửi cho prospect sau cuộc gọi đầu. Ở deal size của launchstudio, một trang làm xong việc sàng lọc giá trị hơn nhiều so với lượng truy cập nó mang lại.

> 💡 **Khác biệt hoá so với trang chủ, tránh ăn thịt nhau:**
> **Trang chủ** = "chúng tôi làm việc đó" (pitch, ngắn, cảm xúc).
> **Trang này** = "đây chính xác là những gì phải làm, và đây là cách tự kiểm tra" (sâu, kỹ thuật, có checklist tự dùng được).
>
> Trang này **phải dám cho đi kiến thức thật**. Đó vừa là điều kiện để LLM trích dẫn, vừa là thứ khiến prospect tin.

---

## 3. 🎨 Design system — token chính xác từ theme

Copy nguyên khối này vào Lovable. Đây là giá trị thật trong `style.css`, không phải phỏng đoán.

```css
:root{
  /* màu */
  --navy:#0B1D35;   /* text chính + heading */
  --bg:#F8FAFE;     /* nền trang (trắng hơi xanh) */
  --white:#FFF;     /* nền card */
  --ok:#0D9668;     /* xanh - pass/thành công */
  --red:#DC2626;    /* đỏ - fail/rủi ro */
  --amb:#D97706;    /* hổ phách - cảnh báo */
  --gs:#2F80ED;     /* gradient start - xanh dương */
  --ge:#14B8A6;     /* gradient end - teal */
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);

  /* thang chữ */
  --text:#0B1D35;   /* chính */
  --ts:#384860;     /* phụ */
  --tm:#64748B;     /* mờ */
  --tf:#94A3B8;     /* rất mờ */

  /* viền */
  --bd:#E2E8F0;     /* viền thường */
  --bs:#EEF2F7;     /* viền nhạt / surface */

  /* font */
  --fh:'Satoshi',system-ui,sans-serif;        /* HEADING */
  --fb:'Inter',system-ui,sans-serif;          /* BODY */
  --fa:'Instrument Serif',Georgia,serif;      /* ACCENT (nhấn, in nghiêng) */

  /* bán kính */
  --r:12px; --rs:10px; --rp:999px; --rl:20px; --rx:24px;

  /* shadow - nhiều lớp, rất nhẹ */
  --ss:0 0 0 1px rgba(0,0,0,.03),0 2px 4px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04);
  --sm:0 0 0 1px rgba(0,0,0,.02),0 4px 8px rgba(0,0,0,.03),0 16px 32px rgba(0,0,0,.06);
  --sl:0 0 0 1px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04),0 24px 48px rgba(0,0,0,.08);

  /* chuyển động */
  --t:.28s; --ease:cubic-bezier(.22,1,.36,1);
}
```

### Nạp font — ⚠️ Satoshi KHÔNG có trên Google Fonts

```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
```

Satoshi lấy từ **Fontshare** (api.fontshare.com). Lovable mặc định hay dùng Google Fonts — nếu không nêu rõ, nó sẽ fallback sang Inter cho heading và **trang sẽ trông lệch ngay lập tức**.

### Typography và spacing đúng theo theme

| Phần tử | Giá trị |
|---|---|
| `h1` | `--fh`, 700, `clamp(34px,4.2vw,52px)`, line-height **1.08**, letter-spacing **−1.5px**, navy |
| `h2` | `--fh`, 700, `clamp(28px,3.5vw,44px)`, line-height **1.12**, letter-spacing **−0.8px**, navy |
| `body` | `--fb`, 16px, line-height **1.65**, `-webkit-font-smoothing:antialiased` |
| Body nhỏ | 14px, `--tm`, line-height 1.7 |
| Caption | 12–12.5px, `--tf`/`--tm` |
| Section padding | **100px 0** desktop · **72px 0** mobile |
| Hero padding | **72px 0 56px** desktop · **56px 0 40px** mobile |
| Card | `padding:20–24px`, `border:1px solid var(--bd)`, `border-radius:var(--rl)` (20px) |
| Card hover | `border-color:rgba(37,99,235,.15)`, `box-shadow:var(--ss)` |
| Button hover | `translateY(-2px)`, `box-shadow:0 14px 34px rgba(47,128,237,.22),0 6px 14px rgba(11,29,53,.1)` |
| Icon trong button | hover → `translateX(2px)`, transition `.2s` |

**Đặc trưng thị giác cần giữ:** nền sáng `#F8FAFE`, card trắng viền mảng xám-xanh, shadow rất nhẹ nhiều lớp (không bao giờ shadow đậm), letter-spacing âm ở heading, gradient xanh→teal chỉ dùng cho điểm nhấn (button chính, số liệu, badge) — **không dùng gradient làm nền section lớn**.

---

## 4. 📝 Cấu trúc nội dung — 9 section

Thứ tự theo logic bán hàng: nhận diện vấn đề → cho đi kiến thức → chứng minh → chuyển đổi.

### S1 — Hero
- **Eyebrow:** `FOR LOVABLE · BOLT · REPLIT · CURSOR · V0 BUILDERS`
- **H1:** `Your AI app works. That doesn't mean it's ready to launch.`
- **Sub:** `Lovable, Bolt and Replit get you to a working prototype fast. The gap between "it works on my screen" and "real users can't break it" is six specific things — and none of them are in the prompt.`
- **CTA chính:** `Get a free production-readiness audit` → form
- **CTA phụ:** `See the 6-point checklist ↓` → anchor S3
- **Trust strip:** `Working code stays · No full rebuild · Fixed scope, fixed price`

> 💡 Cố tình nêu tên công cụ ngay ở eyebrow. Đó là thứ giúp LLM biết trang này nói về Lovable/Bolt/Replit — và là thứ phân biệt trang này với trang chủ.

### S2 — Nhận diện vấn đề (3 cột)

| Dấu hiệu | Giải thích |
|---|---|
| **It demos fine** | Nó chạy đẹp khi bạn tự bấm. Nó chưa gặp người dùng cố tình bấm sai. |
| **The keys are in the code** | API key hardcoded trong file frontend. Ai mở DevTools cũng thấy. |
| **Nothing tells you when it breaks** | Không log, không alert. Người dùng đầu tiên gặp lỗi cũng là người báo lỗi cho bạn. |

### S3 — ⭐ Trọng tâm: framework 6 điểm

Đây là section quan trọng nhất của trang. Lấy nguyên từ `extra-1/02-weekend-framework-six-things-prototype-launch.md`.

Mỗi điểm là một card có: số thứ tự, tiêu đề, *"Vì sao AI tool bỏ qua"*, và **một cách tự kiểm tra**.

| # | Điểm | Cách tự kiểm (đưa thật vào trang) |
|---|---|---|
| 1 | **Secrets & environment variables** | Mở DevTools → Sources → tìm `sk_`, `api_key`. Thấy gì là có vấn đề. |
| 2 | **Structured error handling** | Ngắt mạng giữa lúc submit form. App báo lỗi rõ hay treo trắng? |
| 3 | **Auth & authorization ở tầng API** | Copy URL của user A, mở bằng tài khoản user B. Có chặn không? |
| 4 | **CI pipeline chặn deploy lỗi** | Push một commit cố tình lỗi. Có bị chặn trước khi lên production? |
| 5 | **Test coverage cho 3–5 flow quan trọng** | Liệt kê flow làm bạn mất khách nếu vỡ. Có test nào cho chúng? |
| 6 | **Observability cơ bản** | App lỗi lúc 3 giờ sáng. Sáng ra bạn có biết không? |

> 🔴 **Phải cho đi thật.** Nếu mỗi card chỉ nói "cái này quan trọng, liên hệ chúng tôi", trang mất toàn bộ giá trị GEO và prospect không tin. Cách tự kiểm phải là thứ người đọc làm được ngay trong 5 phút.

### S4 — Widget tự chấm điểm (tương tác)

Theo đúng mô hình "Launch Readiness Checklist" đã có trên trang chủ, nhưng phiên bản kỹ thuật hơn: 6 câu hỏi yes/no → điểm 0–6 → kết quả theo mức:

| Điểm | Kết quả | Màu |
|---:|---|---|
| 5–6 | `Close. One or two gaps to close.` | `--ok` |
| 3–4 | `Halfway. The risky half is usually what's left.` | `--amb` |
| 0–2 | `Not launch-ready. Good news: this is a known list, not a mystery.` | `--red` |

Sau khi có điểm → CTA: `Get these items fixed →`. Điểm được đưa vào hidden field của form.

### S5 — "Production-ready không có nghĩa là build lại"

Phản bác nỗi sợ lớn nhất. Nguồn: `extra-1/32-production-ready-doesnt-mean-rebuilt-debunking-common-fear.md`.

Dạng so sánh 2 cột: **What we keep** (UI, logic nghiệp vụ, schema, công sức đã bỏ ra) vs **What we add** (secret management, API auth, CI, test, observability, error handling).

### S6 — Quy trình 3 bước

Giữ đúng nhịp "3 steps to going live" của trang chủ để thống nhất: **Audit (free, 48h)** → **Fixed-scope plan** → **Launch**.

### S7 — Giá minh bạch

Dùng lại `.cmp-card` của theme, 3 cột, cột giữa `hl` (highlight, viền `--gs`). Lấy mức giá đúng từ trang chủ — **không tự đặt số mới**.

### S8 — Social proof

Testimonial + số liệu. Dùng gradient `--grd` cho con số.

### S9 — Form liên hệ

| Trường | Ghi chú |
|---|---|
| Name, Email | bắt buộc |
| **Which tool did you build with?** | select: Lovable / Bolt / Replit / Cursor / v0 / Other — **dữ liệu phân loại cực giá trị** |
| **Repo or live URL** | optional |
| What's blocking you? | textarea |
| **Budget range** | select, bắt buộc — sàng lọc (xem `conversion_attribution_setup.md` §4) |
| 🔒 hidden | `click_id`, `click_type`, `landing`, `source`, `readiness_score` |

---

## 5. 🤖 Prompt cho Lovable.dev

> Paste nguyên khối dưới đây. Viết bằng tiếng Anh vì Lovable xử lý tiếng Anh tốt hơn đáng kể.

```
Build a single, self-contained landing page as ONE static `index.html` file with all CSS
in one inline <style> block and all JS in one inline <script> block. No React, no build
step, no router, no external dependencies except the three font links below. This page
will be pasted into a WordPress page template, so it must work as a standalone HTML file.

=== DESIGN SYSTEM — USE THESE EXACT VALUES, DO NOT SUBSTITUTE ===

:root{
  --navy:#0B1D35; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --r:12px; --rs:10px; --rp:999px; --rl:20px; --rx:24px;
  --ss:0 0 0 1px rgba(0,0,0,.03),0 2px 4px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04);
  --sm:0 0 0 1px rgba(0,0,0,.02),0 4px 8px rgba(0,0,0,.03),0 16px 32px rgba(0,0,0,.06);
  --sl:0 0 0 1px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04),0 24px 48px rgba(0,0,0,.08);
  --t:.28s; --ease:cubic-bezier(.22,1,.36,1);
}

FONTS — load exactly these three. Satoshi is from Fontshare, NOT Google Fonts.
Do not replace Satoshi with a Google font:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">

TYPOGRAPHY — exact:
- body: var(--fb), 16px, line-height 1.65, color var(--text), background var(--bg),
  -webkit-font-smoothing:antialiased
- h1: var(--fh), weight 700, clamp(34px,4.2vw,52px), line-height 1.08,
  letter-spacing -1.5px, color var(--navy)
- h2: var(--fh), weight 700, clamp(28px,3.5vw,44px), line-height 1.12,
  letter-spacing -0.8px, color var(--navy)
- h3: var(--fh), weight 600, 20px, letter-spacing -0.3px
- small text: 14px, color var(--tm), line-height 1.7
- captions: 12.5px, color var(--tf)

LAYOUT:
- max content width 1140px, centered, 20px side padding, 16px on mobile
- section padding: 100px 0 desktop, 72px 0 under 768px
- hero padding: 72px 0 56px desktop, 56px 0 40px mobile
- cards: background var(--white), padding 24px, border 1px solid var(--bd),
  border-radius var(--rl), box-shadow var(--ss)
- card hover: border-color rgba(37,99,235,.15), box-shadow var(--sm),
  transition all var(--t) var(--ease)
- primary button: background var(--grd), white text, border-radius var(--rp),
  padding 14px 28px, font var(--fh) weight 600
- primary button hover: translateY(-2px),
  box-shadow 0 14px 34px rgba(47,128,237,.22), 0 6px 14px rgba(11,29,53,.1)
- secondary button: transparent bg, 1px solid var(--bd), color var(--navy),
  border-radius var(--rp)
- arrow/icon inside buttons: translateX(2px) on hover, transition .2s

VISUAL CHARACTER — critical to match the existing site:
- Light, airy, clinical. Background is the near-white blue #F8FAFE, never pure white
  for the page, never dark mode.
- Shadows are ALWAYS soft and multi-layered. Never a single heavy shadow.
- Headings use tight NEGATIVE letter-spacing. This is the signature of the brand.
- The blue-to-teal gradient is an ACCENT only: primary buttons, big stat numbers,
  small badges. NEVER a full-width section background, never behind body text.
- Use Instrument Serif (var(--fa)) in italic very sparingly — one or two emphasis
  phrases in headings maximum.
- Generous whitespace. Do not compress sections.
- No stock photos. No illustrations of robots. No emoji in the UI.
  Use simple inline SVG icons with 1.5px stroke, currentColor, 20x20.

=== PAGE CONTENT — 9 SECTIONS IN THIS ORDER ===

S1 HERO (left-aligned text, max 760px wide, not centered)
- Eyebrow, uppercase, 12px, letter-spacing 1.2px, color var(--gs):
  "FOR LOVABLE · BOLT · REPLIT · CURSOR · V0 BUILDERS"
- H1: "Your AI app works. That doesn't mean it's ready to launch."
- Sub (18px, var(--ts), max 620px): "Lovable, Bolt and Replit get you to a working
  prototype fast. The gap between 'it works on my screen' and 'real users can't break
  it' is six specific things — and none of them are in the prompt."
- Two buttons side by side: primary "Get a free production-readiness audit"
  (anchor #audit), secondary "See the 6-point checklist" (anchor #checklist)
- Below buttons, a thin row of three items separated by middots, 13px var(--tm):
  "Your working code stays" · "No full rebuild" · "Fixed scope, fixed price"

S2 PROBLEM — 3 cards in a row (stack on mobile)
Each card: a small SVG icon in a 40x40 rounded square with background var(--bs),
an h3, and 2 sentences of body text.
1. "It demos fine" — "It behaves when you click through it yourself. It has never met
   a user who clicks the wrong thing on purpose."
2. "The keys are in the code" — "API keys hardcoded into frontend files. Anyone who
   opens DevTools can read them, and they will."
3. "Nothing tells you when it breaks" — "No logs, no alerts. Your first user to hit an
   error is also your error reporting system."

S3 THE SIX-POINT FRAMEWORK — id="checklist". THE MOST IMPORTANT SECTION.
H2: "What 'production-ready' actually means"
Sub: "Six items, in this order. The order matters more than the list — each one makes
the next one safer to do."
Then 6 cards in a 2-column grid (1 column on mobile). Each card has:
- A large number (var(--fh), 800, 26px) with the gradient as text fill
- h3 title
- One paragraph: why AI coding tools skip it
- A visually distinct "Check it yourself" block: background var(--bs),
  border-radius var(--rs), padding 14px, 13.5px monospace-ish, label
  "CHECK IT YOURSELF" in 11px uppercase letter-spacing 1px color var(--tf)

1. Secrets and environment variables
   Why skipped: "The tool needs the key to make the demo work, so it puts the key
   where the demo can reach it — the frontend."
   Check: "Open DevTools → Sources → search for 'sk_' or 'api_key'. If anything
   comes up, it is public."

2. Structured error handling for external calls
   Why skipped: "Prompts describe the happy path. Nobody prompts for 'what if Stripe
   times out'."
   Check: "Turn off your wifi mid-way through submitting a form. Does the app explain
   what happened, or go blank?"

3. Authentication and authorization at the API level
   Why skipped: "Hiding a button in the UI looks like access control. The API
   underneath usually still answers anyone who asks."
   Check: "Copy a URL while logged in as user A. Open it logged in as user B.
   Are you blocked?"

4. A CI pipeline that blocks bad deploys
   Why skipped: "The tool deploys on every change. That is a feature while you build
   and a liability once you have users."
   Check: "Push a commit you know is broken. Does anything stop it reaching
   production?"

5. Test coverage for the handful of flows that actually matter
   Why skipped: "Full test suites are slow to write, so they get skipped entirely —
   when 3 to 5 tests would cover the real risk."
   Check: "Write down the flows that lose you a customer if they break. Sign-up,
   payment, data export. Is there a single test for any of them?"

6. Basic observability
   Why skipped: "Logging feels like something to add later. Later is usually after
   the first outage you found out about from a customer."
   Check: "Your app throws an error at 3am. Do you know about it before your
   users tell you?"

S4 SELF-SCORE WIDGET — interactive, vanilla JS
H2: "Score your own app"
Sub: "Six yes/no questions. Takes two minutes. No email required."
Six toggle rows, one per framework item, each with a short question and
Yes / No buttons (pill-shaped, selected state uses var(--grd)).
Live score display: a large number "X / 6" using the gradient as text fill.
Result message below, which changes with the score:
- 5-6 → color var(--ok): "Close. One or two gaps left to close."
- 3-4 → color var(--amb): "Halfway. The risky half is usually what's left."
- 0-2 → color var(--red): "Not launch-ready yet. The good news: this is a known
  list, not a mystery."
Below the result, a primary button "Get these items fixed" that scrolls to #audit
AND writes the score into the form's hidden input named "readiness_score".

S5 "PRODUCTION-READY DOES NOT MEAN REBUILT"
H2: "Production-ready doesn't mean rebuilt"
Sub: "The most common fear, and the most common misunderstanding. We are not
throwing away what you built."
Two columns side by side, equal width:
- Left card, border-left 3px solid var(--ok), heading "What stays":
  Your UI and design · Your business logic · Your database schema ·
  Your product decisions · The weeks you already spent
- Right card, border-left 3px solid var(--gs), heading "What gets added":
  Secret management · API-level authorization · Error handling on external calls ·
  A CI pipeline · Tests on critical flows · Logging and alerts
Each item as a row with a small check or plus SVG icon.

S6 PROCESS — 3 steps, horizontal on desktop with a thin connecting line
H2: "How it works"
1. "Free audit, 48 hours" — "Send us the repo or the live URL. You get a written
   report against the six points above. No call required, no obligation."
2. "Fixed-scope plan" — "You see exactly what gets done, what it costs and how long
   it takes, before anything starts."
3. "Launch" — "We close the gaps, you ship. Your code, your repo, your accounts —
   you own all of it."

S7 PRICING — 3 cards, middle one highlighted
Use placeholder labels "TIER_1 / TIER_2 / TIER_3" and "€—" for prices, with an HTML
comment <!-- REPLACE with pricing from launchstudio.eu/en/ --> above the block.
Middle card: background var(--white), border-color var(--gs),
box-shadow 0 0 0 1px var(--gs), var(--sm), plus a small pill badge
"MOST CHOSEN" using var(--grd).

S8 SOCIAL PROOF
H2: "What others experience"
A row of three stat blocks — big number using the gradient as text fill,
label below in 13px var(--tm). Use placeholders "—" with an HTML comment
<!-- REPLACE with real figures -->.
Below, two testimonial cards: quote in var(--fa) italic 18px, then name and role
in 13px var(--tm).

S9 CONTACT FORM — id="audit"
H2: "Describe your project. We handle the rest."
Sub: "Send the repo or the URL. You get the audit back in 48 hours."
Form fields, stacked, max-width 620px:
- Name (text, required)
- Email (email, required)
- "Which tool did you build with?" (select, required): Lovable, Bolt, Replit,
  Cursor, v0, Other
- "Repo or live URL" (url, optional)
- "What's blocking you?" (textarea, 4 rows)
- "Budget range" (select, required): "Under €5k", "€5k–15k", "€15k–40k",
  "€40k+", "Not sure yet"
- Five hidden inputs, named exactly: click_id, click_type, landing, source,
  readiness_score
- Submit button, primary style, full width: "Request free audit"
Inputs: background var(--white), border 1px solid var(--bd),
border-radius var(--rs), padding 13px 16px, font var(--fb) 15px.
Focus state: border-color var(--gs), box-shadow 0 0 0 3px rgba(47,128,237,.1),
no default outline.

Add this script at the end to populate the hidden fields from a cookie named
ls_click (read it defensively inside try/catch, and set source to 'organic_or_other'
when no click id is present).

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML: one <h1>, section elements, <label> bound to every input.
- Fully responsive. Single breakpoint at 768px is enough. No horizontal scroll at
  360px width.
- Accessible: visible focus rings on all interactive elements, aria-live on the
  score result, 4.5:1 contrast minimum for body text.
- Respect prefers-reduced-motion: disable transforms and transitions inside it.
- No dark mode. The page is light only, matching the existing site.
- Self-contained: one HTML file, inline CSS and JS, only the three font links
  as external resources.
```

---

## 6. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | Thay giá thật từ `launchstudio.eu/en/` | Lovable để placeholder `€—` |
| 2 | Thay số liệu social proof thật | Đừng để placeholder lên production |
| 3 | Chuyển vào WordPress | Lưu thành page template trong theme `launchstudio`, hoặc dán vào Custom HTML block |
| 4 | **Quyết định URL** | Đề xuất `/en/ai-app-into-production` + hreflang. Xem §1③ |
| 5 | **Quyết định index hay noindex** | Nếu dùng *chỉ* cho ads → `noindex`, đo lường sạch. Nếu muốn giá trị GEO → **index**, và phải đảm bảo nội dung thật sâu hơn trang chủ |
| 6 | Gắn middleware cookie `ls_click` | Code ở `conversion_attribution_setup.md` §2② |
| 7 | Nối form vào CRM + conversion action `Qualified Lead` | `conversion_attribution_setup.md` §4 |
| 8 | Thêm schema `FAQPage` + `HowTo` | 6 điểm framework là `HowTo` rất tự nhiên — tăng khả năng được LLM trích |
| 9 | Internal link từ 60 bài `extra-1` về trang này | Đây là cách trang có authority mà không cần search volume |
| 10 | Nếu `noindex`: gỡ khỏi sitemap và menu | Nếu không thủ thuật đo lường ở §2 mất tác dụng |

> 🔴 **Mục 5 là quyết định quan trọng nhất và hai lựa chọn loại trừ nhau.**
>
> **`noindex`** → đo lường ads sạch tuyệt đối, nhưng mất toàn bộ giá trị GEO.
> **`index`** → có thể được LLM trích dẫn, nhưng mất khả năng nói "mọi form từ URL này là từ ads".
>
> **Đề xuất của tôi: chọn `index`.** Lý do: giá trị GEO của trang này lớn hơn giá trị đo lường, vì bạn vẫn đo được bằng `gclid` trong hidden field (đã có ở §9), chỉ là không tuyệt đối. Còn giá trị GEO thì không có cách nào khác để có. Nếu cần một trang đo sạch cho ads, tạo thêm một bản `noindex` riêng ở URL khác — rẻ hơn nhiều so với việc hy sinh GEO.

---

## 7. Nguồn nội dung có sẵn trong repo

Không cần viết lại từ đầu. Trang này là bản tổng hợp của:

| Section | Nguồn |
|---|---|
| S3 framework 6 điểm | `extra-1/02-weekend-framework-six-things-prototype-launch.md` |
| S2 vấn đề | `extra-1/03-why-ai-code-looks-done-not-safe-to-ship.md` · `extra-1/18-why-it-works-on-my-machine-isnt-production-ready.md` |
| S3 điểm 1 | `extra-1/04-hardcoded-secrets-problem-nobody-notices.md` |
| S3 điểm 2 | `extra-1/06-structured-error-handling-what-ai-coding-tool-skipped.md` |
| S3 điểm 3 | `extra-1/07-authentication-looks-done-demo-api-level.md` |
| S3 điểm 4 | `extra-1/08-lovable-prototype-needs-ci-pipeline-before-launch.md` |
| S3 điểm 5 | `extra-1/09-three-to-five-user-flows-worth-testing-before-you-ship.md` |
| S3 điểm 6 | `extra-1/10-observability-production-step-vibe-coders-forget.md` |
| S4 widget | `extra-1/45-production-readiness-score-grade-your-own-ai-built-app.md` |
| S5 không build lại | `extra-1/32-production-ready-doesnt-mean-rebuilt-debunking-common-fear.md` |
| S7 giá | `extra-1/38-diy-vs-freelancer-vs-launchstudio-cost-timeline-comparison.md` |
