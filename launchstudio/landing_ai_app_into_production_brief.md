# 🚀 Landing page `/ai-app-into-production` — Content brief + Lovable prompt (v2: Pre-flight / Launch Control)

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-into-production` (hiện **404**)
> **Thương hiệu:** giữ màu, font, gradient của `launchstudio.eu` · **Phong cách:** mới hoàn toàn, không bám theo trang hiện tại
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

## 3. 🎨 Thương hiệu giữ nguyên, phong cách đổi hoàn toàn

### Giữ (nhận diện thương hiệu)

```css
:root{
  --navy:#0B1D35; --navy-2:#102A4C; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --fm:'JetBrains Mono',ui-monospace,monospace;
}
```

- Bảng màu navy + gradient xanh→teal · font Satoshi / Inter / Instrument Serif · letter-spacing âm ở heading
- ⚠️ Satoshi lấy từ **Fontshare**, không có trên Google Fonts. Prompt đã ghi rõ để Lovable không tự thay font.

### Đổi (phong cách tự do) — concept **"Pre-flight / Launch Control"**

"Into production" = **phóng**. Cả trang là một buổi kiểm tra trước khi phóng tên lửa:

| Yếu tố | Site hiện tại | Trang này |
|---|---|---|
| Ẩn dụ | Không có | **Đếm ngược phóng tên lửa**: hero dừng ở `HOLD`, CTA cuối trang đếm tiếp tới `LIFTOFF` |
| Bố cục | Card nhẹ, thoáng | **Editorial mạnh**: chữ rất to, số thứ tự khổng lồ `01/06`, đường kẻ mảnh như bảng điều khiển |
| Hình ảnh | Icon SVG | **Bảng Launch Control** (card navy trên nền sáng), đèn trạng thái, thanh tiến độ bị kẹt ở 80% |
| Tương tác | Widget tách riêng | **Checklist 6 điểm vừa là nội dung vừa là bộ tự chấm điểm** → ra kết luận GO / NO-GO → CTA |
| Chi tiết | — | Thanh "Launch readiness" dính trên cùng, lấp đầy theo tiến độ cuộn trang |

> 💡 **Khác trang `/ai-app-vibe-coding`:** trang đó dùng hero tối toàn màn và khung chat AI. Trang này hero **sáng**, chữ editorial to, chỉ có **một khối navy** (bảng Launch Control). Hai trang nhìn là biết cùng thương hiệu nhưng không giống nhau.

---

## 4. 📝 Cấu trúc nội dung v2 — Pain → Solution → bổ trợ → CTA

**Bỏ theo yêu cầu:** bảng giá, form. Mọi CTA trỏ ra trang liên hệ/đặt lịch, có mang theo `gclid`/`utm_*` và điểm tự chấm.
**Giữ lại có chủ đích:** 6 cách tự kiểm tra (mỗi cách 1 dòng). Theo §2, đây là thứ làm nên giá trị GEO của trang. Bỏ đi thì trang chỉ là bản sao trang chủ.

| # | Section | Vai trò | Thông điệp |
|---|---|---|---|
| S1 | **Hero + Launch Control** | 🪝 Hook | `Your app is 6 checks away from launch.` Đếm ngược T−10 → dừng ở **HOLD** |
| S2 | **Stuck at 80%** | 😬 Pain | Thanh tiến độ Idea ✓ → Prototype ✓ → **[kẹt]** → Launch + 3 sự thật ngắn |
| S3 | **6-point pre-flight** | ✅ Solution + tương tác | Mỗi điểm: vì sao AI bỏ qua · tự kiểm thế nào · Yes/No → ra GO/NO-GO |
| S4 | Not a rebuild | Bổ trợ | Giữ gì / thêm gì |
| S5 | Flight plan | Bổ trợ | 3 bước: free audit 48h → fixed-scope plan → launch |
| S6 | Proof | Bổ trợ | Placeholder số liệu + testimonial |
| S7 | FAQ | Bổ trợ | 3 câu |
| S8 | **Liftoff CTA** | 🎯 Chốt | Đếm ngược tiếp `3 · 2 · 1` → `Let's get you cleared for launch.` |

### Vì sao cách này thuyết phục và đẩy CTA

1. **H1 đưa ra một con số cụ thể và hữu hạn.** "6 checks away" biến nỗi lo mơ hồ thành một danh sách làm được, khác với "app chưa sẵn sàng" chung chung.
2. **Đếm ngược dừng ở HOLD tạo cảm giác dở dang.** Người đọc muốn thấy nó chạy tiếp, và chỉ ở CTA cuối trang nó mới chạy tiếp.
3. **Tự chấm điểm cá nhân hoá CTA.** Sau khi trả lời 6 câu, nút đổi chữ theo kết quả (`Fix my 4 failed checks`). Đây là CTA chuyển đổi mạnh nhất trang.
4. **Có 3 điểm CTA:** hero → sau kết quả chấm điểm → cuối trang. Không nhồi thêm.

---

## 5. 🤖 Prompt cho Lovable.dev (v2)

> Paste nguyên khối. Viết bằng tiếng Anh vì Lovable xử lý tiếng Anh tốt hơn.

```
Build a single, self-contained landing page as ONE static `index.html` file: all CSS in
one inline <style> block, all JS in one inline <script> block. No React, no build step,
no router, no external dependencies except the four font links below. It will be pasted
into a WordPress page template, so it must work standalone.

WHAT THIS PAGE IS
LaunchStudio takes apps built with AI coding tools (Lovable, Bolt, Replit, Cursor, v0)
and makes them production-ready without rebuilding them. Audience: a founder whose app
works but who is stuck before launch. The whole page uses ONE metaphor: a rocket
PRE-FLIGHT CHECK. Launch is on HOLD until six checks pass. Story arc: PAIN, then
SOLUTION (the six checks, interactive), then short supporting sections, then a final
LIFTOFF call to action. Copy is short, confident and specific. Never mock the reader
for using AI tools. There is NO pricing and NO form on this page; every CTA links out.

=== BRAND — KEEP EXACTLY ===
:root{
  --navy:#0B1D35; --navy-2:#102A4C; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --on-dark:#E6EDF7; --on-dark-m:#A3B3CA; --line-dark:rgba(255,255,255,.09);
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --fm:'JetBrains Mono',ui-monospace,monospace;
  --rp:999px; --rs:10px; --rl:20px; --rx:28px;
  --t:.3s; --ease:cubic-bezier(.22,1,.36,1);
}
FONTS — exactly these. Satoshi is from Fontshare, NOT Google Fonts. Never substitute:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

=== STYLE — "LAUNCH CONTROL EDITORIAL" (this is a NEW style, do not make it look like a
generic SaaS template) ===
- Page background var(--bg). Bold editorial typography: very large Satoshi headings
  with tight negative letter-spacing, generous whitespace, thin 1px hairline rules
  (var(--bd)) separating blocks like a control panel.
- h1: var(--fh) 900, clamp(44px,7vw,92px), line-height .98, letter-spacing -3px
- h2: var(--fh) 700, clamp(32px,4.5vw,56px), line-height 1.04, letter-spacing -1.5px
- h3: var(--fh) 700, 21px, letter-spacing -0.4px
- body: var(--fb) 16px/1.65, color var(--ts)
- Labels, counters, status text: var(--fm), 12px, uppercase, letter-spacing 1.5px.
  Every section starts with a mono label like "[ 01 — STATUS ]".
- Huge outline numbers ("01" to "06") in Satoshi 900, 120px, transparent fill with a
  1.5px var(--bd) text stroke, sitting behind content as decoration.
- Exactly TWO dark navy blocks on the page: the hero Launch Control panel and the final
  Liftoff band. Everything else is light. This contrast is the signature.
- Status colours are semantic: var(--red) = fail/hold, var(--amb) = warning,
  var(--ok) = pass/go. Gradient is the brand accent: primary buttons, gradient text on
  1–2 key words, the progress bar fill.
- var(--fa) italic for at most 3 emphasis words on the page.
- All visuals built in HTML/CSS/SVG. NO stock photos, NO cartoon rockets, NO robots, NO
  emoji. A rocket is only ever implied by words and a minimal 1.5px line icon.
- Primary button: var(--grd), white, radius var(--rp), padding 16px 30px, var(--fh) 700,
  with a right arrow that slides 3px on hover; hover lifts 2px with
  box-shadow 0 16px 36px rgba(47,128,237,.3).
- Secondary button: transparent, 1px solid var(--navy), color var(--navy), radius
  var(--rp); hover fills var(--navy) with white text.
- Max width 1180px, 20px side padding (16px under 768px). Sections 120px 0 desktop,
  76px 0 mobile.

STICKY TOP BAR (global): a 56px bar, white at 85% with backdrop blur, bottom hairline.
Left: "LaunchStudio" wordmark in var(--fh) 700. Centre (hidden on mobile): mono label
"LAUNCH READINESS" and a 160px progress bar that fills with var(--grd) as the user
scrolls the page. Right: small primary button "Free pre-flight" (data-cta).

=== SECTIONS, IN ORDER ===

S1 HERO — light background, two columns (copy 55% left, Launch Control panel right),
stacked on mobile with copy first.
Left:
- Mono label: "[ FOR LOVABLE · BOLT · REPLIT · CURSOR · V0 ]"
- H1: 'Your app is <span class=grad>6 checks</span> away from launch.'
- Sub, 19px var(--ts), max 520px: "It works on your screen. Real users need it to
  survive. We run the pre-flight, fix what fails, and get you live — without
  rebuilding what you made."
- Buttons: primary "Book my free pre-flight check" (data-cta), secondary "Run the
  checks yourself" (href #preflight).
- Mono micro-row, var(--tm): "✓ Code stays yours   ✓ No full rebuild   ✓ Audit in 48h"
  (draw the ticks as inline SVG, not characters).

Right — LAUNCH CONTROL PANEL (the hook): a navy card (var(--navy), radius var(--rx),
1px var(--line-dark) border, faint 32px grid pattern inside, large soft shadow).
- Top row in var(--fm): "LAUNCH CONTROL" left, "my-app.lovable.app" right in
  var(--on-dark-m).
- A big mono countdown, 64px, var(--on-dark): animates T-10, T-09 … down to T-04
  (one step every 450ms), then FREEZES and swaps to "HOLD" in var(--red) with a slow
  pulsing glow.
- Below it, six check rows, each: a 10px status light, the check name in var(--fm)
  13px, and a status word on the right. While the countdown runs, rows tick over one by
  one from "CHECKING…" to their final state:
    Secrets & env vars ......... FAIL  (red)
    Error handling ............. FAIL  (red)
    API authorization .......... FAIL  (red)
    CI pipeline ................ WARN  (amber)
    Critical-flow tests ........ FAIL  (red)
    Monitoring & alerts ........ WARN  (amber)
- Bottom strip: "LAUNCH STATUS" and a red pill "NO-GO · 6 checks unresolved".
Under prefers-reduced-motion, render the final state immediately.

S2 PAIN — "STUCK AT 80%" (light)
- Mono label "[ 01 — WHERE YOU ARE ]"
- H2: "You're not stuck building. You're stuck <em>launching.</em>"
- A full-width horizontal progress track with four stops: "Idea", "Prototype",
  "Production", "Launch". Idea and Prototype have green filled dots and a gradient
  filled line; the line stops at ~80% between Prototype and Production, where a
  pulsing red marker with a mono tooltip says "YOU ARE HERE · prompt #47". Production
  and Launch are hollow grey. The fill animates from 0 to 80% on scroll into view.
  On mobile the track turns vertical.
- Three editorial rows below, each separated by a hairline, laid out as big statement
  (var(--fh) 700 28px var(--navy)) left and one-line explanation right:
    "It demos fine."  —  "It has never met a user who clicks the wrong thing on purpose."
    "The keys are in the code."  —  "Open DevTools and anyone can read them."
    "Nothing tells you when it breaks."  —  "Your first angry user is your monitoring."
- Closing line, var(--fh) 600 22px: "So you keep prompting. And keep not launching."

S3 SOLUTION — THE 6-POINT PRE-FLIGHT (light, id="preflight") — THE CORE OF THE PAGE
- Mono label "[ 02 — PRE-FLIGHT ]"
- H2: "Six checks stand between you and launch."
- Sub: "Run them yourself in five minutes. Be honest — this stays in your browser."
- Layout: on desktop, a two-column area: the six checks on the left (65%), a STICKY
  readiness gauge on the right (35%). On mobile the gauge becomes a sticky bar at the
  bottom of the viewport while this section is in view.
- Each check is a row with: the big outline number behind it, h3 title, a line
  "Why AI skipped it:" + text, a highlighted mono box "CHECK IT YOURSELF" (background
  var(--bs), radius var(--rs)) + text, and two pill buttons "Pass" / "Fail"
  (aria-pressed). Choosing Pass turns the row's status light green; Fail turns it red.
  1. "Secrets & environment variables"
     Why: "The demo needs the key, so the tool puts it where the demo can reach it —
     your frontend."
     Check: "DevTools → Sources → search 'sk_' or 'api_key'. Found anything? It's public."
  2. "Error handling on external calls"
     Why: "Prompts describe the happy path. Nobody prompts for 'what if Stripe times out'."
     Check: "Kill your wifi mid-submit. Clear message, or blank screen?"
  3. "Authorization at the API level"
     Why: "Hiding a button looks like access control. The API still answers anyone."
     Check: "Open user A's URL while logged in as user B. Blocked?"
  4. "A CI pipeline that blocks bad deploys"
     Why: "Deploy-on-every-change is a feature while building, a liability with users."
     Check: "Push a commit you know is broken. Does anything stop it?"
  5. "Tests on the flows that matter"
     Why: "Full test suites feel slow, so tests get skipped — when 3 to 5 would do."
     Check: "List the flows that lose you a customer if they break. Any test for them?"
  6. "Monitoring & alerts"
     Why: "Logging feels like 'later'. Later is after a customer reports the outage."
     Check: "Your app errors at 3am. Do you know before your users do?"
- READINESS GAUGE (white card, radius var(--rx), hairline border, soft shadow):
  a circular SVG ring that fills with var(--grd) as checks pass, centre text
  "X / 6" in var(--fh) 900 56px. Below, a mono status line and a verdict with
  aria-live="polite":
    0 answered → "AWAITING CHECKS" (var(--tm))
    6 passed → "GO" (var(--ok)): "Cleared. Want a second pair of eyes before liftoff?"
    4–5 passed → "HOLD" (var(--amb)): "Close. The last gaps are usually the risky ones."
    0–3 passed → "NO-GO" (var(--red)): "Not launch-ready — but it's a known list, not a
    mystery."
  Then a primary button (data-cta) whose label updates live:
    no answers → "Get a free pre-flight check"
    some fails → "Fix my N failed checks"  (N = number of Fail answers)
    all pass   → "Book a final review"
  Append readiness_score=X and failed=1,3,5 (the failed item numbers) to its link.

S4 NOT A REBUILD (light)
- Mono label "[ 03 — WHAT CHANGES ]"
- H2: "Not a rebuild. A pre-flight."
- Two columns separated by a vertical hairline:
  "STAYS" (mono, var(--ok)) — Your UI and design · Your business logic · Your database
  schema · Your product decisions · The weeks you already put in
  "ADDED" (mono, var(--gs)) — Secret management · API-level authorization · Error
  handling · A CI pipeline · Tests on critical flows · Logging and alerts
  Each item a row with a small check or plus SVG; rows slide in from their side on
  scroll.

S5 FLIGHT PLAN (light)
- Mono label "[ 04 — FLIGHT PLAN ]"
- H2: "Three steps to liftoff."
- Three columns joined by a dashed line with a small moving dot travelling along it
  (static under reduced motion). Step number in mono "STEP 01" etc.
  01 "Free pre-flight audit" — "Send the repo or live URL. Written report against the
     six checks within 48 hours. No call needed."
  02 "Fixed-scope plan" — "Exactly what gets fixed, how long it takes, agreed before we
     start."
  03 "Launch" — "We close the gaps in your repo. You ship. You own all of it."

S6 PROOF (light)
- Mono label "[ 05 — MISSION LOG ]"
- H2: "Founders who made it off the pad."
- Three stats: numbers in gradient text, var(--fh) 900 56px; mono labels below.
  Use "—" placeholders with <!-- REPLACE with real figures. Prefer outcomes: apps
  launched, payments processed, funding raised after launch -->
- Two testimonial cards: quote in var(--fa) italic 22px, then name, role and a mono tag
  like "BUILT WITH LOVABLE". Placeholder text with <!-- REPLACE with real testimonial -->.
- Do NOT invent client logos, certification badges or award seals.

S7 FAQ (light) — <details>/<summary> accordion, max 760px, plus icon rotating to x.
  "Will you rebuild my app?" — "No. We keep what works and add what's missing."
  "Which tools do you work with?" — "Lovable, Bolt, Replit, Cursor, v0 — anything that
   produces a real codebase."
  "Who owns the code?" — "You. Your repo, your accounts, your infrastructure."

S8 LIFTOFF CTA — dark navy band, full width, faint grid, two soft radial glows in
#2F80ED and #14B8A6, centered content.
- When it scrolls into view, a big mono countdown resumes from where the hero froze:
  "T-03 · T-02 · T-01" then "LIFTOFF" in gradient text, while a thin vertical gradient
  line shoots upward behind it (pure CSS).
- H2 white: "Let's get you <em>cleared</em> for launch."
- Sub, var(--on-dark-m) 19px: "Free pre-flight audit. Written report in 48 hours.
  No obligation."
- Primary button, larger: "Book my free pre-flight check" (data-cta).
- Mono micro-line under the button, var(--on-dark-m): "Lovable · Bolt · Replit ·
  Cursor · v0"

FOOTER: one slim hairline row, 13px var(--tm): "© LaunchStudio · launchstudio.eu"

=== JS (vanilla, small) ===
- const CTA_URL = "https://launchstudio.eu/en/#contact"; // REPLACE with real contact
  or booking URL. Every element with data-cta gets href = CTA_URL plus query params.
- Attribution: copy gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content from location.search onto every data-cta link, plus
  landing=ai-app-into-production. The S3 button also adds readiness_score and failed.
- Hero countdown + check rows, scroll progress bar, S2 track fill, S3 scoring and live
  button label, S4/S5 reveals, S8 countdown — IntersectionObserver for all scroll
  triggers, each animation runs once.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section aria-labelledby>, buttons are <button>,
  links are <a>.
- Responsive, single 768px breakpoint, no horizontal scroll at 360px. The hero panel
  stays visible on mobile, scaled down.
- Contrast at least 4.5:1, including muted text on navy. Visible focus rings
  (2px solid var(--ge), 3px offset).
- prefers-reduced-motion: no countdowns, no moving dot, no slides; show final states.
- Status is never conveyed by colour alone: always a word (PASS/FAIL/WARN/GO/NO-GO).
- One HTML file, inline CSS and JS, only the four font links external.
```

---

## 6. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Thay `CTA_URL`** | Trỏ tới trang liên hệ/đặt lịch thật. Kiểm tra `gclid`, `utm_*`, `readiness_score`, `failed` có đi theo |
| 2 | Cho trang liên hệ đọc `readiness_score` + `failed` | Điền sẵn vào form ở đó → sales biết ngay khách yếu ở đâu |
| 3 | Thay số liệu và testimonial thật ở S6 | Không có số thật thì bỏ khối stat, giữ testimonial |
| 4 | Kiểm tra hero và gauge trên mobile 360px | Launch Control panel và thanh gauge dính dưới đáy không được che nội dung |
| 5 | Xác nhận "48h" còn đúng | Lấy từ quy trình trên trang chủ. Đổi ở cả S1, S5, S8 nếu thay đổi |
| 6 | Chuyển vào WordPress | Page template trong theme `launchstudio`, hoặc Custom HTML block |
| 7 | **Quyết định URL** | Đề xuất `/en/ai-app-into-production` + hreflang. Xem §1③ |
| 8 | **Quyết định index hay noindex** | Xem ghi chú bên dưới |
| 9 | Gắn middleware cookie `ls_click` + conversion `Qualified Lead` | `conversion_attribution_setup.md` §2② và §4. Giờ ghi nhận ở trang liên hệ |
| 10 | Internal link từ 60 bài `extra-1` về trang này | Cách để trang có authority mà không cần search volume |

> 🔴 **Mục 8 là quyết định quan trọng nhất, và hai lựa chọn loại trừ nhau.**
>
> **`noindex`** → đo lường ads sạch tuyệt đối, nhưng mất toàn bộ giá trị GEO.
> **`index`** → có thể được LLM trích dẫn, nhưng mất khả năng nói "mọi lead từ URL này là từ ads".
>
> **Đề xuất: chọn `index`.** Vẫn đo được qua `gclid` gắn vào link CTA, chỉ là không tuyệt đối. Còn giá trị GEO (6 cách tự kiểm tra ở S3) thì không có đường nào khác để có. Nếu cần một trang đo sạch cho ads, tạo thêm bản `noindex` ở URL khác.

---

## 7. Nguồn nội dung có sẵn trong repo

Không cần viết lại từ đầu. Trang này là bản tổng hợp của:

| Section | Nguồn |
|---|---|
| S3 pre-flight 6 điểm | `extra-1/02-weekend-framework-six-things-prototype-launch.md` |
| S2 pain | `extra-1/03-why-ai-code-looks-done-not-safe-to-ship.md` · `extra-1/18-why-it-works-on-my-machine-isnt-production-ready.md` |
| S3 điểm 1 | `extra-1/04-hardcoded-secrets-problem-nobody-notices.md` |
| S3 điểm 2 | `extra-1/06-structured-error-handling-what-ai-coding-tool-skipped.md` |
| S3 điểm 3 | `extra-1/07-authentication-looks-done-demo-api-level.md` |
| S3 điểm 4 | `extra-1/08-lovable-prototype-needs-ci-pipeline-before-launch.md` |
| S3 điểm 5 | `extra-1/09-three-to-five-user-flows-worth-testing-before-you-ship.md` |
| S3 điểm 6 | `extra-1/10-observability-production-step-vibe-coders-forget.md` |
| S3 gauge tự chấm điểm | `extra-1/45-production-readiness-score-grade-your-own-ai-built-app.md` |
| S4 không build lại | `extra-1/32-production-ready-doesnt-mean-rebuilt-debunking-common-fear.md` |
