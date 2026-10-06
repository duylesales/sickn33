# 🔒 Landing page `/ai-app-security` — Content brief + Lovable prompt (v2: X-ray / Glass App)

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-security` (hiện **404**)
> **Thương hiệu:** giữ màu, font, gradient của `launchstudio.eu` · **Phong cách:** mới hoàn toàn, khác hai landing page vibe-coding và into-production
> **File liên quan:** `keyword_research_lovable_vibecoding_security.md` · `volume_analysis_results.md` · `conversion_attribution_setup.md`

---

## 1. ✅ Trang này khác trang trước: nó thật sự cần thiết

So sánh thẳng với `/ai-app-into-production` để thấy khác biệt:

| | `/ai-app-into-production` | `/ai-app-security` |
|---|---|---|
| Research của bạn có nói cần? | Không — trang chủ đã bao | ✅ **Có — nói thẳng "phải tạo page trước, viết bài sau"** |
| Volume | 10/tháng | **~70/tháng** |
| Tín hiệu cạnh tranh | Yếu | ✅ **≥4 agency đã có landing page riêng** |
| Dữ kiện cứng để trích dẫn | Không có | ✅ **CVE + sự cố 4/2026 + số liệu quét 1.645 app** |
| Giá trị đơn hàng | Trung bình | ✅ **Cao nhất trong 3 cụm** |

`keyword_research_lovable_vibecoding_security.md` §1.2 viết nguyên văn:

> *"Cụm ③ là cụm thương mại nhất trong 3 cụm, và nó đang không có đích đến. **Phải tạo page trước, viết bài sau** — nếu không thì backlink nội bộ và schema `Service` đều không có chỗ bám."*

➡️ **Trang này đang là nút cổ chai trong kế hoạch của chính bạn.** Nên ưu tiên nó trước `/ai-app-into-production`.

### Tín hiệu cầu mạnh nhất trong toàn bộ nghiên cứu

`volume_analysis_results.md` §4 đã kết luận: **chỉ tín hiệu cầu (có đối thủ trả tiền/làm landing page) mới dự đoán được volume**, tín hiệu cung (có nội dung) thì vô giá trị.

Theo tiêu chí đó, cụm security là cụm duy nhất đạt chuẩn:

| Keyword | Đối thủ đã có service page riêng |
|---|---|
| `vibe coding cleanup specialist` | Redwerk · Suffescom · ThirdRock · AleaIT |
| `vibe code cleanup` | Redwerk · Lightning Kite |
| `vibe code audit` | instinctools |
| `vibe coding rescue` | Pragmatic Coders |

Bốn agency không tự dưng làm landing page cho một cụm không ai tìm.

### Volume thật (Keyword Planner)

| Keyword | Volume | Ghi chú |
|---|---:|---|
| **`technische due diligence`** | **40** | 🥇 NL, thuật ngữ chuẩn giới VC/M&A. Đơn hàng lớn nhất |
| `pentest webapplicatie` | 10 | ⚠️ Có thể kéo khách enterprise ngoài ICP |
| `replit security` | 10 | |
| `bolt new security` | 10 | |
| Phần còn lại (~8 kw) | 0 | Dưới 10/tháng |

**~70/tháng.** Mỏng, nhưng gấp 7 lần cụm "to production" và có giá trị đơn hàng cao hơn nhiều.

---

## 2. 🔴 Vũ khí thật của trang này: hai sự cố có thật, kiểm chứng được

Đây là điều khiến trang này mạnh hơn mọi trang security chung chung. Bạn không cần nói "security quan trọng". Bạn có **hai sự kiện cụ thể, công khai, có ngày tháng** mà người đọc có thể tự kiểm.

### Sự cố ②: Tháng 4/2026 — lỗi BOLA của chính Lovable ⭐ MỚI NHẤT, MẠNH NHẤT

| | |
|---|---|
| **Loại** | BOLA (Broken Object Level Authorization) — lỗi của **nền tảng Lovable**, không phải lỗi người dùng |
| **Hậu quả** | Bất kỳ user free nào cũng đọc được source code, **database credentials**, lịch sử chat AI và dữ liệu khách của project khác |
| **Người phát hiện** | Matt Palmer (@weezerOSINT), báo qua HackerOne ngày **3/3/2026** |
| **Vá** | Tháng 3/2026 — **nhưng chỉ cho project tạo sau 11/2025** |
| **Thời gian project cũ vẫn hở** | **~48 ngày**, không có cảnh báo nào gửi tới developer bị ảnh hưởng |
| **Vì sao nghiêm trọng gấp đôi** | App Lovable thường nhúng credential của Supabase, Stripe, Google API → thành rủi ro chuỗi cung ứng |

> 🥇 **Đây là hook mạnh nhất cho toàn trang**, vì nó tạo ra một câu hỏi cụ thể và **tự kiểm được** cho mọi người dùng Lovable:
>
> **"Project của bạn tạo trước tháng 11/2025? Vậy nó đã hở 48 ngày và không ai thông báo cho bạn."**
>
> Đó không phải lời chào hàng. Đó là một sự thật có thể tra cứu, và nó biến một nỗi lo mơ hồ thành một việc cần làm ngay hôm nay.

### Sự cố ①: CVE-2025-48757 — thiếu RLS

| | |
|---|---|
| **CVE** | `CVE-2025-48757` · CWE-863 (Incorrect Authorization) |
| **Công bố** | 5/2025, cùng researcher Matt Palmer |
| **Phạm vi** | Lovable tới 15/4/2025 |
| **Số liệu** | Quét **1.645** app từ showcase công khai của Lovable → **170 app (~10,3%)** và **303 endpoint** đọc/ghi được chỉ bằng public anon key, vì RLS chưa bao giờ được bật |
| **Dữ liệu lộ** | Email, địa chỉ, và một số trường hợp là API key |

> ⚠️ **Hai cảnh báo khi dùng dữ kiện này — đọc kỹ trước khi publish:**
>
> **① Điểm CVSS đang vênh giữa các nguồn** (có nguồn ghi 9.3, nguồn khác 8.26). **Đừng in một con số CVSS cụ thể lên trang.** Tra lại trên NVD trước, hoặc bỏ hẳn điểm số và chỉ nêu CWE-863 — chính xác hơn và không ai bắt lỗi được.
>
> **② Phải phân biệt đúng bản chất hai sự cố.** CVE-2025-48757 là **app-level misconfiguration**, bị khuếch đại bởi việc Supabase tắt RLS mặc định và output của Lovable không bắt buộc bật. Sự cố 4/2026 mới là **lỗi của chính nền tảng Lovable**. Gộp hai thứ thành "Lovable không an toàn" là sai sự thật, và chính sự chính xác này là thứ khiến LLM trích dẫn bạn thay vì trích đối thủ.

### 🔴 Nguyên tắc tông giọng — quan trọng về mặt pháp lý và thương mại

**Đối tượng của trang này LÀ người dùng Lovable.** Nếu trang đọc như một bài đánh Lovable, bạn mất chính khách hàng mình đang nhắm.

| ✅ Nên | ❌ Không nên |
|---|---|
| Nêu sự kiện, ngày tháng, link nguồn | Dùng từ "nguy hiểm", "thảm hoạ", "đừng dùng Lovable" |
| "Lovable vá cho project sau 11/2025; project cũ hở ~48 ngày" | "Lovable che giấu sự cố" / "Lovable nói dối" |
| "Supabase tắt RLS mặc định — đây là nguyên nhân gốc" | Suy diễn động cơ của bất kỳ công ty nào |
| Dẫn link The Register, TNW, Computing, OECD AI Incidents | Dẫn blog SEO của đối thủ |

Việc Lovable ban đầu phủ nhận rồi quy trách nhiệm cho HackerOne **là sự thật được báo chí ghi nhận, nhưng đừng đưa lên trang.** Nó thêm rủi ro mà không thêm giá trị bán hàng. Nêu timeline khô khan, dẫn nguồn, để người đọc tự kết luận.

---

## 3. ⚠️ Ba vấn đề cần quyết trước khi build

### ① URL vẫn sai namespace ngôn ngữ (y như trang trước)

| URL | Ngôn ngữ |
|---|---|
| `launchstudio.eu/` | 🇳🇱 NL |
| `launchstudio.eu/en/` | 🇬🇧 EN |
| `launchstudio.eu/ai-app-security` | ⚠️ Slug EN trong namespace NL |

**Đề xuất:** `launchstudio.eu/en/ai-app-security` (EN) + `launchstudio.eu/ai-app-beveiliging` (NL), hreflang chéo.

### ② 🔴 Bản NL ở đây quan trọng hơn trang trước — và đừng dịch máy

`keyword_research_lovable_vibecoding_security.md` §5 có hai quy tắc áp đúng vào trang này:

- **Compliance bắt buộc dùng NL, và phải dùng "AVG" chứ không phải "GDPR".** Người Hà Lan gõ `AVG`. Dịch "GDPR" nguyên văn là mất toàn bộ cụm này.
- **Ý định thuê dịch vụ → ưu tiên NL:** `beveiligingsaudit webapplicatie`, `code audit laten uitvoeren`, `technische due diligence`.
- **Nhưng lỗi kỹ thuật cụ thể → giữ EN:** `lovable rls vulnerability`, `supabase anon key exposed`. Founder Hà Lan copy nguyên thông báo lỗi tiếng Anh vào Google.

➡️ Bản NL **không phải bản dịch** của bản EN. Nó phải nhấn mạnh phần compliance/AVG và due diligence, giữ nguyên tên lỗi kỹ thuật bằng tiếng Anh.

### ③ Thị trường này đã đông — cần một góc riêng

Đối thủ trực tiếp đã có mặt: **vibeappscanner.com**, **vibe-eval.com**, **unpwned.io**, **guardlayer**, **superblocks**, **shipsafe**, **nocode.mba**, **rapidevelopers**, **buildmvpfast**. `nextlovable` bán audit ở mức **$199–299**.

> 🔴 **Hệ quả về giá:** có đối thủ bán audit $199. Nếu trang này bán "security audit" chung chung, bạn bị so giá với $199 và thua.
>
> **Góc riêng nên chọn:** *audit là miễn phí, giá trị nằm ở việc VÁ.* Đối thủ bán báo cáo; launchstudio bán kết quả đã sửa. Và thêm một góc mà công cụ tự động không làm được: **`technische due diligence`** — chuẩn bị cho Series A technical review. Scanner không ký được báo cáo cho investor; agency thì được.
>
> ⚠️ Lưu ý: `unicoconnect` đang rank cho `supabase security checklist`. Đó là một agency Ấn Độ với rate $25–49/giờ. Không đấu giá với họ ở cụm nội dung chung — đấu ở cụm NL địa phương và due diligence, nơi họ không vào được.

---

## 4. 🎨 Thương hiệu giữ nguyên, phong cách đổi hoàn toàn

### Giữ (nhận diện thương hiệu)

```css
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
  --fm:'JetBrains Mono',ui-monospace,monospace;
}
```

Màu navy, gradient xanh→teal, font Satoshi (Fontshare) / Inter / Instrument Serif, letter-spacing âm ở heading.

### Đổi — concept **"X-ray / Glass App"**

Nỗi đau thật của nhóm khách này **không phải "app bị lỗi"** mà là **"tôi không nhìn thấy được ai đang đọc dữ liệu của tôi"**. Vì vậy cả trang xoay quanh **sự nhìn xuyên thấu**:

| Yếu tố | Thiết kế |
|---|---|
| Hero | **Bố cục giữa**, chữ lớn ở trên và một browser mock rộng ở dưới, hiển thị một app SaaS bình thường. **Một thấu kính tròn đi theo con trỏ** (mobile thì tự lướt) soi xuyên lớp giao diện để lộ lớp dưới: JSON thô có email khách, `service_role` key, `SELECT * FROM customers` |
| Ẩn dụ phụ | **Hồ sơ vụ việc có thanh che (redaction)**: các thanh navy che dữ kiện, cuộn tới đâu mở ra tới đó |
| Không khí | Sáng, điềm tĩnh, kiểu **báo cáo điều tra**: nhiều khoảng trắng, chữ mono cho dữ kiện, nhãn `SOURCE ↗` cạnh mọi số liệu. **Không phải trang báo động** |
| Màu đỏ | Chỉ xuất hiện trong lớp dữ liệu bị lộ dưới thấu kính và nhãn severity. Không có section nào nền đỏ |

| | `/ai-app-vibe-coding` | `/ai-app-into-production` | **`/ai-app-security`** |
|---|---|---|---|
| Hero | Tối, chat AI 2 cột | Sáng, bảng đếm ngược 2 cột | **Sáng, bố cục giữa, thấu kính X-ray tương tác** |
| Ẩn dụ | Tối → sáng | Phóng tên lửa | **Nhìn xuyên thấu / hồ sơ bị che** |
| Tương tác chính | Toggle Before/After | Pass/Fail → GO/NO-GO | **Câu hỏi "trước 11/2025?" + thước đo độ phơi nhiễm Locked ↔ Glass** |

---

## 5. 📝 Cấu trúc nội dung v2 — Pain → Solution → bổ trợ → CTA

**Bỏ theo yêu cầu:** form (mọi CTA trỏ ra trang liên hệ, mang theo tham số). Trang vốn không có bảng giá.
**Giữ có chủ đích:** 2 sự cố có nguồn và 6 cách tự kiểm tra. Đây là "vũ khí thật" ở §2 và là lý do LLM trích dẫn trang.
**Rút gọn:** AVG chỉ còn 1 dải ngắn dẫn sang bản NL. Phạm vi audit gộp vào phần Solution.

| # | Section | Vai trò | Thông điệp |
|---|---|---|---|
| S1 | **Hero X-ray** | 🪝 Hook | `Your users see your app. Who else sees your data?` |
| S2 | **The case file** | 😬 Pain (sự thật) | 2 sự cố, thanh che mở dần, mọi dữ kiện có link nguồn. Cuối section là câu hỏi **"Project tạo trước 11/2025?"** Yes/No/Not sure |
| S3 | **Exposure check** | 😬→✅ Tự kiểm tra | 6 lỗ hổng + bước tự kiểm 2 phút → thước đo **Locked ↔ Glass** → CTA cá nhân hoá |
| S4 | **Free audit, paid fix** | ✅ Solution | 3 bước: audit 48h → vá → re-test + thư xác nhận. Kèm "Covers / Doesn't cover" |
| S5 | Due diligence | Bổ trợ (đơn lớn nhất) | `Raising a round? Investors will open this code.` |
| S6 | AVG strip | Bổ trợ | 1 dòng + link sang bản NL |
| S7 | Proof | Bổ trợ | Placeholder |
| S8 | FAQ | Bổ trợ | 3 câu |
| S9 | **Final CTA** | 🎯 Chốt | Thấu kính trở lại, lần này lớp dưới **đã khoá**: `Make your app opaque again.` |

### Vì sao cách này đánh đúng nỗi đau

1. **Người đọc tự soi.** Họ rê chuột và *thấy* email khách hàng hiện ra dưới một giao diện trông rất bình thường. Đó chính là nỗi sợ của họ, nhưng không có câu chữ nào hù doạ.
2. **Câu hỏi "trước 11/2025?" biến tin tức thành việc cá nhân.** Ai chọn "Yes" hoặc "Not sure" sẽ nhận một dòng riêng và một CTA riêng. Đây là hook mạnh nhất theo §2.
3. **Hình ảnh khép vòng.** Hero là app trong suốt, CTA cuối là app được khoá lại. Toàn bộ câu chuyện bán hàng nằm trong hai hình ảnh đó.
4. **Định vị chống đối thủ $199:** "audit miễn phí, chúng tôi lấy tiền ở việc vá", nói rõ ngay ở S4.

---

## 6. 🤖 Prompt cho Lovable.dev (v2)

> Paste nguyên khối. Tiếng Anh vì Lovable xử lý tốt hơn.

```
Build a single, self-contained landing page as ONE static `index.html` file: all CSS in
one inline <style> block, all JS in one inline <script> block. No React, no build step,
no router, no external dependencies except the four font links below. It will be pasted
into a WordPress page template, so it must work standalone.

WHAT THIS PAGE IS
LaunchStudio audits and FIXES security in apps built with AI coding tools (Lovable,
Bolt, Replit, Cursor, v0), especially apps on Supabase. The audit is free; LaunchStudio
earns its fee by fixing what it finds, then re-testing. Audience: founders whose app is
live or about to be, who cannot see who else can read their data. Story arc: PAIN
(verifiable facts), SOLUTION, short supporting sections, final CTA.
Visual concept for the whole page: X-RAY / GLASS — seeing through a normal-looking app
to the exposed data underneath, and finally locking it.
There is NO pricing and NO form on this page; every CTA links out.

TONE — MANDATORY
Calm, factual, investigative. Like a well-sourced report, never an alarm. Never use the
words "dangerous", "disaster", "hacked", "nightmare", and never say or imply "don't
use Lovable" — the readers ARE Lovable users and the page respects the tool. Every
factual claim about an incident shows a small "SOURCE ↗" link. Do not print any CVSS
score.

=== BRAND — KEEP EXACTLY ===
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
  --fm:'JetBrains Mono',ui-monospace,monospace;
  --rp:999px; --rs:10px; --rl:18px; --rx:26px;
  --t:.3s; --ease:cubic-bezier(.22,1,.36,1);
}
FONTS — exactly these. Satoshi is from Fontshare, NOT Google Fonts. Never substitute:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

=== STYLE — "FORENSIC GLASS" (a new style; do NOT make it look like a generic SaaS
template, a hacker terminal, or a dark cyber-security site) ===
- LIGHT page, background var(--bg). Calm, spacious, documentary. Think investigative
  report meets premium product page.
- h1: var(--fh) 900, clamp(42px,6.4vw,84px), line-height 1, letter-spacing -2.5px,
  CENTERED.
- h2: var(--fh) 700, clamp(30px,4.2vw,52px), line-height 1.06, letter-spacing -1.2px
- h3: var(--fh) 700, 20px, letter-spacing -0.3px
- body: var(--fb) 16px/1.7, color var(--ts)
- Facts, dates, keys, labels: var(--fm) 13px. Section labels are mono, uppercase,
  letter-spacing 1.5px, in the form "FILE 01 · THE INCIDENTS".
- Glass surfaces: white at 70% opacity, backdrop-filter blur(14px), 1px solid
  rgba(11,29,53,.08), radius var(--rx), very soft layered shadow.
- REDACTION BARS are a signature element: solid var(--navy) bars with radius 3px that
  cover facts and slide away (scaleX to 0 from the left, 500ms) when the line scrolls
  into view. The text underneath must exist in the DOM for screen readers and SEO.
- Red only for exposed data and severity labels. Green only for "secured" states.
  Gradient for primary buttons, the lens ring, and 1–2 key words as gradient text.
- var(--fa) italic for at most 3 emphasis words on the page.
- All visuals in HTML/CSS/SVG. NO stock photos, NO hooded hackers, NO padlock clip-art,
  NO matrix code rain, NO emoji. Icons: inline SVG, 1.5px stroke, 20x20.
- Primary button: var(--grd), white, radius var(--rp), padding 16px 30px, var(--fh) 700,
  hover lift 2px + box-shadow 0 16px 36px rgba(47,128,237,.3). Secondary: transparent,
  1px solid var(--navy), color var(--navy), radius var(--rp).
- Max width 1180px, 20px side padding (16px under 768px). Sections 116px 0 desktop,
  76px 0 mobile.

=== SECTIONS, IN ORDER ===

S1 HERO — X-RAY (centered)
- Mono label: "FOR LOVABLE · BOLT · REPLIT · CURSOR · SUPABASE APPS"
- H1: 'Your users see your app. <span class=grad>Who else</span> sees your data?'
- Sub, 19px var(--ts), max 640px, centered: "AI-built apps can ship with the database
  door open — and nothing on screen tells you. We find what's exposed, fix it, and prove
  it's closed. The audit is free."
- Buttons centered: primary "Check my app for free" (data-cta), secondary "See what
  gets exposed" (href #case-file).
- Mono micro-row: "Free audit · Written report in 48h · We fix it, or you keep the report"

THE X-RAY MOCK (the hook), full container width below the copy, max 1040px:
A browser window (glass surface, top bar with three dots and a URL pill
"app.yourstartup.com/dashboard"). Inside are TWO stacked layers of identical size:
- TOP layer — a clean, friendly SaaS dashboard drawn in HTML/CSS: sidebar, a greeting
  "Good morning, Sam", three KPI tiles, and a "Recent customers" table with avatars,
  names and a status pill. Looks perfectly normal and safe.
- BOTTOM layer — the same area as raw exposed data on a pale grid, var(--fm) 12.5px:
    GET /rest/v1/customers?select=*      200 OK   (anon key)
    { "email": "j.devries@…", "phone": "+31 6…", "address": "Keizersgracht…" }
    { "email": "m.jansen@…", "iban": "NL91 ABNA ••••" }
    SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOi…"
    RLS: disabled  ·  table: customers  ·  policies: 0
  Exposed values are underlined in var(--red); small red mono tags float beside them:
  "PUBLIC", "NO RLS", "SECRET IN BUNDLE".
- A circular LENS (180px; 120px on mobile) with a 2px gradient ring and a soft outer
  glow reveals the bottom layer inside the circle (CSS clip-path: circle() on the
  bottom layer, position driven by CSS variables set from pointer position).
  On desktop the lens follows the pointer inside the window. On touch devices and when
  idle for 3s, the lens auto-sweeps along a slow figure-eight path. Keyboard users can
  focus the window and move the lens with arrow keys.
- Caption under the window, mono 12px var(--tm), centered:
  "Illustration. The pattern behind CVE-2025-48757: tables readable with the public key."
- Under prefers-reduced-motion: no following or sweeping; show a static split — left
  half top layer, right half bottom layer, divided by a vertical gradient line.

S2 PAIN — THE CASE FILE (id="case-file")
- Label: "FILE 01 · THE INCIDENTS"
- H2: "This isn't hypothetical. It's on the record."
- Two case cards side by side (stacked on mobile), glass surfaces. Each card: a mono
  header row (case date left, "PLATFORM-LEVEL" or "APP-LEVEL" tag right), an h3, and a
  list of fact rows "LABEL ........ value" where each value starts covered by a
  redaction bar that slides away on scroll (stagger 120ms). Each card ends with
  "SOURCE ↗" links.
  Card A — h3 "Spring 2026 · Lovable platform authorization flaw"
    Reported ........ 3 Mar 2026, via HackerOne
    Type ............ Broken object-level authorization (BOLA)
    Patched ......... March 2026 — for projects created after Nov 2025
    Older projects .. readable for ~48 days, no notification sent
    Exposed ......... source code · database credentials · AI chat history
    <!-- REPLACE: link SOURCE to TNW, Computing, The Register, OECD AI Incidents -->
  Card B — h3 "May 2025 · CVE-2025-48757 (CWE-863)"
    Scanned ......... 1,645 apps from Lovable's public showcase
    Affected ........ 170 apps (~10.3%) · 303 endpoints
    How ............. readable/writable with the public anon key
    Root cause ...... Row Level Security never enabled on Supabase tables
    Exposed ......... emails, addresses, some API keys
    <!-- REPLACE: link SOURCE to NVD / Intruder / Pluto Security -->
- Neutral note under the cards, 14px var(--tm): "Lovable patched the platform flaw.
  The app-level gaps are configuration — they stay open until someone closes them."
- THE PERSONAL QUESTION (wide glass bar, centered):
  Big text, var(--fh) 700 26px: "Was your project created before November 2025?"
  Three pill buttons: "Yes" · "No" · "Not sure". On click, an aria-live line appears:
    Yes → "Then it sat in the exposed window. Rotate your keys and get it checked."
    Not sure → "That's the most common answer. A free check settles it in 48 hours."
    No → "Good. The app-level gaps below still apply to every project."
  and a primary button "Check my app for free" (data-cta) with created_before=yes|no|unsure
  appended to its link.

S3 EXPOSURE CHECK (id="check")
- Label: "FILE 02 · CHECK IT YOURSELF"
- H2: "Six gaps. Two minutes each."
- Sub: "Run these yourself. Your answers stay in your browser."
- Layout: on desktop, the six items in a 2-column grid on the left (70%) and a STICKY
  exposure meter on the right (30%). On mobile the meter becomes a slim sticky bar at
  the bottom while this section is in view.
- Each item is a white card: severity tag (mono 11px pill: CRITICAL red / HIGH amber /
  MEDIUM grey-blue), h3, a mono "TRY THIS" box on var(--bs), and three small toggles
  "Exposed" · "Secure" · "Not sure" (aria-pressed).
  1. CRITICAL — "RLS off on Supabase tables" — Try: "Supabase → Table Editor. Any table
     without 'RLS enabled' is publicly readable."
  2. CRITICAL — "Service role key in the frontend" — Try: "DevTools → Sources → search
     'service_role'. If it's there, anyone can write to your database."
  3. CRITICAL — "Authorization only in the UI" — Try: "Open user A's URL while logged in
     as user B. Blocked?"
  4. HIGH — "Public project visibility" — Try: "Lovable → project settings. Public can
     mean code and chat history, not just the live app."
  5. HIGH — "No rate limiting on login" — Try: "Fire 200 login attempts in a row. Does
     anything stop you?"
  6. MEDIUM — "Secrets in git history" — Try: "git log -p | grep -iE
     'sk_live|service_role|password'. Deleting a file doesn't delete history."
- EXPOSURE METER (glass card): a vertical (desktop) / horizontal (mobile) scale from
  "LOCKED" (top, green) to "GLASS" (bottom, red). A marker slides as answers change:
  Exposed = 2 points, Not sure = 1 point, Secure = 0. A small preview square above the
  scale shows a tiny version of the hero dashboard whose opacity drops as the score
  rises — the app literally turns to glass. Verdict with aria-live:
    no answers → "Answer to see your exposure"
    0 → "Locked on the basics. Auth logic is where the subtle gaps hide."
    1–4 → "Some glass. These are usually same-day fixes."
    5+ → "Your data is very likely readable right now."
  Primary button (data-cta) with a live label:
    no answers → "Get a free audit"
    otherwise → "Close my N gaps"  (N = Exposed + Not sure count)
  Append risk_score and exposed=1,2,… to its link.

S4 SOLUTION — FREE AUDIT, PAID FIX
- Label: "FILE 03 · WHAT WE DO"
- H2: 'Reports are cheap. <em>Closed</em> gaps aren't.'
- Sub, max 640px: "Scanners sell you a list. We hand you the list for free — and get
  paid to close it."
- Three steps in a row joined by a thin line; each step icon morphs from an open
  circle to a check as it scrolls into view:
  01 "Free audit" — "Repo or live URL. Written findings within 48 hours."
  02 "We fix it" — "Fixed scope, agreed upfront, done in your repo."
  03 "Re-test & sign-off" — "We verify every fix and give you a letter you can forward
     to customers or investors."
- Below, two compact columns separated by a hairline:
  "THE AUDIT COVERS" (mono, var(--ok)): Supabase RLS & policies · Keys and secrets ·
  API authorization · Auth flows · Rate limiting · Git history
  "IT ISN'T" (mono, var(--tm)): A full penetration test · An ISO or SOC 2 certification
  · A review of third-party vendors' code
  One line under: "Saying what we don't do is how you know the rest is real."

S5 DUE DILIGENCE (a glass panel with a soft gradient border)
- Label: "FILE 04 · RAISING A ROUND"
- H2: "Investors will open this code."
- Text, max 600px: "Technical due diligence on an AI-built codebase looks for the same
  six gaps — plus how fast you can fix them. Walk in with a report and a sign-off
  letter instead of surprises."
- Mono row of three deliverables: "Investor-ready report · Fix plan with timeline ·
  Sign-off letter"
- Secondary button "Prepare for due diligence" (data-cta, adds reason=investor_dd)
- Small link: "Nederlands: technische due diligence ↗" (href /ai-app-beveiliging,
  <!-- REPLACE when the NL page exists -->)

S6 AVG STRIP — one slim row, mono label "NL", text: "Dutch customers? We cover AVG:
personal data, datalek-meldplicht and verwerkersovereenkomsten." Link "Lees in het
Nederlands ↗" to /ai-app-beveiliging.

S7 PROOF
- Label: "FILE 05 · AFTER THE FIX"
- H2: "Founders who closed the gaps."
- Three stats, numbers in gradient text var(--fh) 900 52px, mono labels. Use "—" with
  <!-- REPLACE with real figures: apps audited, critical gaps closed, avg. days to fix -->
- Two testimonial cards: quote var(--fa) italic 21px, name, role, mono tag "BUILT WITH
  LOVABLE". Placeholders with <!-- REPLACE with real testimonial -->.
- Do NOT invent certification badges, ISO logos, award seals or client logos.

S8 FAQ — <details> accordion, max 760px.
  "Is Lovable unsafe?" — "No. It's a fast way to build. The gaps come from defaults
   and missing configuration, which is fixable."
  "Do I need to stop my app during the audit?" — "No. We work read-only until you
   approve fixes."
  "Who sees my code?" — "Only the engineers on your audit, under NDA if you want one."

S9 FINAL CTA — the X-ray returns, closed
- A smaller version of the hero window (max 720px) with the lens sweeping, but the
  bottom layer now shows:
    GET /rest/v1/customers?select=*      401 Unauthorized
    RLS: enabled  ·  policies: 4  ·  secrets: server-side
  with green "SECURED" tags instead of red.
- H2 centered: 'Make your app <span class=grad>opaque</span> again.'
- Sub: "Free audit. Written report in 48 hours. You decide what happens next."
- Primary button, larger: "Check my app for free" (data-cta)

FOOTER: one hairline row, 13px var(--tm): "© LaunchStudio · launchstudio.eu"

=== JS (vanilla, small) ===
- const CTA_URL = "https://launchstudio.eu/en/#contact"; // REPLACE with the real
  contact or booking URL. Every [data-cta] gets href = CTA_URL + query params.
- Attribution: copy gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content from location.search onto every data-cta link, plus
  landing=ai-app-security. Section-specific params: created_before (S2), risk_score
  and exposed (S3), reason=investor_dd (S5).
- Lens (pointer / auto-sweep / arrow keys, via requestAnimationFrame), redaction
  reveals, S2 question, S3 scoring + live button label + preview opacity, S4 step
  morph. IntersectionObserver for scroll triggers; each runs once.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section aria-labelledby>, buttons are <button>,
  links are <a>. Redacted text stays in the DOM (bars are decorative, aria-hidden).
- The X-ray mock is decorative: aria-hidden on both layers, with a visually-hidden
  description: "Illustration: a normal dashboard with customer data exposed underneath."
- Responsive, single 768px breakpoint, no horizontal scroll at 360px.
- Contrast at least 4.5:1. Visible focus rings (2px solid var(--ge), 3px offset).
- prefers-reduced-motion: no lens movement, no bar slides, no morphs; final states.
- Severity and status never by colour alone: always a word (CRITICAL, EXPOSED,
  SECURED…).
- One HTML file, inline CSS and JS, only the four font links external.
```

---

## 7. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Tra lại CVE-2025-48757 trên NVD** | Prompt đã cấm in CVSS. Kiểm tra lại cả mốc 15/4/2025 và số 1.645 / 170 / 303 |
| 2 | 🔴 **Gắn link nguồn thật vào mọi nút `SOURCE ↗`** | The Register, TNW, Computing, OECD AI Incidents, NVD. **Không dẫn blog SEO của đối thủ** |
| 3 | 🔴 **Rà lại tông giọng lần cuối** | Không câu nào được đọc thành cáo buộc. Chỉ sự kiện + nguồn. Kiểm tra cả FAQ "Is Lovable unsafe?" |
| 4 | 🔴 **Thay `CTA_URL`** | Kiểm tra `gclid`, `utm_*`, `created_before`, `risk_score`, `exposed`, `reason` có đi theo sang trang đích |
| 5 | Cho trang liên hệ đọc các tham số trên | `reason=investor_dd` và `created_before=yes` là hai lead nóng nhất → chấm điểm `Qualified Lead` cao hơn |
| 6 | Kiểm tra thấu kính X-ray trên mobile | Tự lướt mượt, không giật, không che mất nội dung ở 360px |
| 7 | Dữ liệu giả dưới thấu kính | Phải là dữ liệu bịa rõ ràng (đã che `…`, `••••`). Không dùng tên/email thật |
| 8 | Thay số liệu và testimonial thật ở S7 | Không có thì bỏ khối stat |
| 9 | **Quyết định URL** + hreflang | `/en/ai-app-security` + `/ai-app-beveiliging` |
| 10 | **Viết bản NL — không dịch máy** | Mở rộng AVG + due diligence, giữ EN cho tên lỗi kỹ thuật (§3②) |
| 11 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2②, giờ ghi nhận ở trang liên hệ |

> 🔴 **Mục 1, 2 và 3 không được bỏ qua.** Trang nêu tên một công ty thật và một CVE thật. Chính xác về dữ kiện vừa là nghĩa vụ, vừa là thứ khiến LLM trích dẫn bạn thay vì vibeappscanner.

> 💡 **Trang này nên `index`.** Có volume thật (~70/tháng), có đối thủ xác minh, và có hai entity (`CVE-2025-48757`, sự cố Lovable 2026) mà LLM sẽ tra. Nếu cần URL đo ads sạch, tạo bản sao `noindex` riêng.

---

## 8. Thứ tự ưu tiên giữa hai landing page

| | Trang | Lý do |
|---|---|---|
| 🥇 | **`/ai-app-security`** | Research của bạn gọi nó là nút cổ chai · volume gấp 7 lần · 4 đối thủ xác minh · có dữ kiện cứng · đơn hàng lớn nhất |
| 🥈 | `/ai-app-into-production` | Trùng thông điệp trang chủ · volume ~10/tháng · giá trị chủ yếu là GEO |

Nếu chỉ build được một trang trong tháng này, build trang security.

---

## 9. Nguồn đã xác minh

- [CVE-2025-48757 — Pluto Security phân tích](https://blog.pluto.security/p/cve-202548757-what-happened-why-it-b22)
- [Intruder — CVE-2025-48757](https://cvemon.intruder.io/cves/CVE-2025-48757)
- [TNW — Lovable left thousands of projects exposed for 48 days](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
- [Computing — Lovable flaw exposed source code, credentials and AI chats](https://www.computing.co.uk/news/2026/security/lovable-flaw-exposed-source-code-credentials-and-ai-chats)
- [The Register — Lovable denies data leak](https://assets.theregister.com/2026/04/20/lovable_denies_data_leak/)
- [OECD AI Incidents — 2026-04-20](https://oecd.ai/en/incidents/2026-04-20-b869)
- Volume: `volume_analysis_results.md` · Keyword: `keyword_research_lovable_vibecoding_security.md` §4
- Design token: `launchstudio.eu/wp-content/themes/launchstudio/style.css` (đối chiếu 0 sai lệch)
