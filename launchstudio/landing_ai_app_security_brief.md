# 🔒 Landing page `/ai-app-security` — Content brief + Lovable prompt

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-security` (hiện **404**)
> **Design reference:** `launchstudio.eu/` (NL) · `launchstudio.eu/en/` (EN) — token trích từ `themes/launchstudio/style.css`
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

## 4. 🎨 Design system — token chính xác từ theme

Giống hệt trang trước. Đã đối chiếu 0 sai lệch với `style.css` live.

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
  --r:12px; --rs:10px; --rp:999px; --rl:20px; --rx:24px;
  --ss:0 0 0 1px rgba(0,0,0,.03),0 2px 4px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04);
  --sm:0 0 0 1px rgba(0,0,0,.02),0 4px 8px rgba(0,0,0,.03),0 16px 32px rgba(0,0,0,.06);
  --sl:0 0 0 1px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04),0 24px 48px rgba(0,0,0,.08);
  --t:.28s; --ease:cubic-bezier(.22,1,.36,1);
}
```

⚠️ **Satoshi từ Fontshare, không có trên Google Fonts:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
```

| Phần tử | Giá trị |
|---|---|
| `h1` | `--fh` 700, `clamp(34px,4.2vw,52px)`, lh **1.08**, ls **−1.5px** |
| `h2` | `--fh` 700, `clamp(28px,3.5vw,44px)`, lh **1.12**, ls **−0.8px** |
| `body` | `--fb` 16px, lh **1.65**, antialiased |
| Section | **100px 0** desktop · **72px 0** mobile |
| Hero | **72px 0 56px** · **56px 0 40px** mobile |
| Card | padding 24px, `1px solid var(--bd)`, radius `--rl` (20px), shadow `--ss` |
| Button hover | `translateY(-2px)` + `0 14px 34px rgba(47,128,237,.22),0 6px 14px rgba(11,29,53,.1)` |

**Riêng trang security:** dùng `--red` / `--amb` / `--ok` làm hệ màu trạng thái cho severity, nhưng **tiết chế**. Trang phải trông như một báo cáo kỹ thuật bình tĩnh, **không phải trang báo động**. Nền vẫn `#F8FAFE` sáng, không dark mode, không màu đỏ tràn section.

---

## 5. 📝 Cấu trúc nội dung — 10 section

### S1 — Hero
- **Eyebrow:** `LOVABLE · BOLT · REPLIT · CURSOR · SUPABASE`
- **H1:** `Your AI app is live. Nobody has checked who else can read it.`
- **Sub:** `In April 2026, every Lovable project created before November 2025 was readable by any free user for 48 days — source code, database credentials, AI chat history. No warning was sent. Most founders still don't know.`
- **CTA chính:** `Check my app — free, 48 hours`
- **CTA phụ:** `What exactly gets checked ↓`
- **Trust strip:** `Free audit · Written report · No obligation · We fix it or you take the report elsewhere`

### S2 — ⭐ Hai sự cố (trọng tâm, đặt ngay sau hero)

Hai card lớn, mỗi card là một timeline. Không trang trí, trình bày như một bản ghi nhận sự việc. **Mỗi dữ kiện có link nguồn ngoài.**

**Card A — April 2026, platform-level (BOLA)**
```
3 Mar 2026    Matt Palmer reports via HackerOne
Mar 2026      Patched — but only for projects created after Nov 2025
~48 days      Older projects remained readable. No notification sent.
What leaked   Source code · DB credentials · AI chat history · customer data
Why it spreads  Lovable apps embed Supabase, Stripe and Google API keys
```
→ Dưới card: một hộp nhấn mạnh `Was your project created before November 2025?` + button `Check my app`

**Card B — May 2025, app-level (CVE-2025-48757, CWE-863)**
```
Scope     Lovable through 15 Apr 2025
Scanned   1,645 apps from Lovable's public showcase
Found     170 apps (~10.3%) · 303 endpoints
How       Readable/writable with the public anon key — RLS was never enabled
Leaked    Emails, addresses, in some cases API keys
Root cause  Supabase ships new tables with RLS off by default
```

> ⚠️ Không in điểm CVSS. Nêu CWE-863 là đủ và chính xác.

### S3 — Sáu lỗ hổng phổ biến nhất + cách tự kiểm

Giống cấu trúc framework ở trang `/ai-app-into-production`, nhưng góc security. 6 card, mỗi card có severity pill và một bước tự kiểm 2 phút.

| # | Lỗ hổng | Severity | Cách tự kiểm |
|---|---|---|---|
| 1 | **RLS not enabled on Supabase tables** | 🔴 Critical | Supabase → Table Editor. Bảng nào không có badge "RLS enabled" là đọc được công khai. |
| 2 | **Service role key in frontend** | 🔴 Critical | DevTools → Sources → tìm `service_role`. Thấy là bất kỳ ai cũng ghi được vào DB của bạn. |
| 3 | **Authorization only in the UI** | 🔴 Critical | Copy URL khi đăng nhập user A, mở bằng user B. Có chặn không? |
| 4 | **Public project visibility** | 🟠 High | Lovable → project settings. Public nghĩa là code + chat history đọc được, không chỉ app đã publish. |
| 5 | **No rate limiting on API routes** | 🟠 High | Gửi 200 request liên tiếp vào endpoint login. Có bị chặn? |
| 6 | **Secrets in git history** | 🟡 Medium | `git log -p \| grep -iE "sk_live\|service_role\|password"`. Xoá file không xoá history. |

> 🔴 Mỗi bước tự kiểm phải **làm được thật trong 2 phút**. Đây là điều kiện để LLM trích dẫn và để prospect tin. Nếu card chỉ nói "cái này rủi ro, hãy liên hệ", trang mất toàn bộ giá trị.

### S4 — Widget tự chấm (6 câu, giống trang trước nhưng thang risk)

| Số lỗ hổng | Kết quả | Màu |
|---:|---|---|
| 0 | `Clean on the basics. Worth a deeper look at auth logic.` | `--ok` |
| 1–2 | `Two gaps. Both are same-day fixes.` | `--amb` |
| 3+ | `Your database is very likely readable right now.` | `--red` |

Điểm ghi vào hidden field `risk_score`.

### S5 — Phạm vi audit (minh bạch — chống so giá $199)

Bảng 2 cột: **What the free audit covers** vs **What it doesn't** (ví dụ: không phải pentest đầy đủ, không phải ISO/SOC2 certification, không review mã của third-party vendor).

> 💡 Nêu rõ cái **không** làm là thứ tạo uy tín và lọc khách sai. Scanner tự động không dám viết phần này.

### S6 — "Audit miễn phí. Giá nằm ở việc vá."

Định vị trực diện chống đối thủ bán báo cáo $199. Ba bước: **Free audit (48h)** → **Fixed-scope fix plan** → **Re-test và ký xác nhận**.

### S7 — `Technische due diligence` (section riêng, đơn hàng lớn nhất)

Đối tượng khác hẳn: founder đang gọi vốn, hoặc investor đang soi target. Keyword `technische due diligence` = 40/tháng, cao nhất cụm.

- **H2:** `Raising a round? Investors will look at this code.`
- Nội dung: what a technical DD covers, what AI-generated code specifically triggers, deliverable là báo cáo gửi được cho investor
- **Có nút ngôn ngữ riêng sang bản NL** — đây là cụm mà NL quan trọng nhất

### S8 — AVG / GDPR compliance

Trên bản EN: ngắn, dẫn sang bản NL. **Trên bản NL: đây là section lớn, dùng từ "AVG" xuyên suốt.** Nội dung: personsgegevens, datalek-meldplicht, verwerkersovereenkomst.

### S9 — Social proof + certifications

Số liệu + testimonial. Nếu có chứng chỉ security nào thật thì đặt ở đây. **Nếu không có, bỏ hẳn — đừng tạo badge trông như chứng chỉ.**

### S10 — Form

| Trường | Ghi chú |
|---|---|
| Name, Email | bắt buộc |
| **Built with** | select: Lovable / Bolt / Replit / Cursor / v0 / Other |
| **Project created before Nov 2025?** | select: Yes / No / Not sure — ⭐ **nối trực tiếp với hook ở S1** |
| **Repo or live URL** | optional |
| **Using Supabase?** | Yes / No / Not sure |
| What worries you most? | textarea |
| **Reason for audit** | select: Launching soon / Investor DD / Enterprise customer asked / Already had an incident / Just want to know — ⭐ **phân loại giá trị đơn hàng ngay tại form** |
| 🔒 hidden | `click_id`, `click_type`, `landing`, `source`, `risk_score` |

> 💡 Trường `Reason for audit` là trường giá trị nhất trên trang. `Investor DD` và `Enterprise customer asked` là hai lý do có ngân sách và deadline thật.

---

## 6. 🤖 Prompt cho Lovable.dev

> Paste nguyên khối. Tiếng Anh vì Lovable xử lý tốt hơn đáng kể.

```
Build a single, self-contained landing page as ONE static `index.html` file, with all CSS
in one inline <style> block and all JS in one inline <script> block. No React, no build
step, no router, no external dependencies except the three font links below. This file
will be pasted into a WordPress page template, so it must work standalone.

The subject is security auditing for apps built with AI coding tools (Lovable, Bolt,
Replit, Cursor, v0). The tone is a calm technical report, NOT an alarm page. Factual,
precise, zero hype. The reader is a non-technical founder who shipped something real and
does not know what to check.

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

FONTS — load exactly these three. Satoshi comes from Fontshare, NOT Google Fonts.
Never substitute a Google font for Satoshi:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">

TYPOGRAPHY — exact:
- body: var(--fb), 16px, line-height 1.65, color var(--text), background var(--bg),
  -webkit-font-smoothing:antialiased
- h1: var(--fh) 700, clamp(34px,4.2vw,52px), line-height 1.08, letter-spacing -1.5px,
  color var(--navy)
- h2: var(--fh) 700, clamp(28px,3.5vw,44px), line-height 1.12, letter-spacing -0.8px
- h3: var(--fh) 600, 20px, letter-spacing -0.3px
- small: 14px, var(--tm), line-height 1.7 · caption: 12.5px, var(--tf)
- monospace blocks: ui-monospace, 'SF Mono', Menlo, monospace, 13px

LAYOUT:
- max width 1140px, centered, 20px side padding (16px under 768px)
- section padding 100px 0 desktop, 72px 0 under 768px
- hero padding 72px 0 56px desktop, 56px 0 40px mobile
- cards: var(--white), padding 24px, 1px solid var(--bd), border-radius var(--rl),
  box-shadow var(--ss)
- card hover: border-color rgba(37,99,235,.15), box-shadow var(--sm),
  transition all var(--t) var(--ease)
- primary button: background var(--grd), white, border-radius var(--rp),
  padding 14px 28px, var(--fh) 600
- primary hover: translateY(-2px), box-shadow 0 14px 34px rgba(47,128,237,.22),
  0 6px 14px rgba(11,29,53,.1)
- secondary button: transparent, 1px solid var(--bd), color var(--navy), radius var(--rp)

SEVERITY PILLS — small, uppercase, 11px, letter-spacing .8px, border-radius var(--rp),
padding 4px 10px:
- Critical: color var(--red), background rgba(220,38,38,.08)
- High: color var(--amb), background rgba(217,119,6,.08)
- Medium: color var(--tm), background var(--bs)
- Clean/pass: color var(--ok), background rgba(13,150,104,.08)

VISUAL CHARACTER — critical to match the existing site:
- Light, airy, clinical. Page background is #F8FAFE, never pure white, NEVER dark mode.
- Shadows are always soft and multi-layered. Never one heavy shadow.
- Headings use tight NEGATIVE letter-spacing — this is the brand signature.
- The blue-teal gradient is an ACCENT only: primary buttons, big stat numbers, small
  badges. NEVER a full-width section background, never behind body text.
- Red is used ONLY in small severity pills and single result lines. Never a red section
  background, never a red hero. This page must read as a calm report, not a warning siren.
- Instrument Serif italic very sparingly — one or two emphasis phrases maximum.
- No stock photos, no shield/padlock clip art, no hacker-in-a-hoodie imagery, no emoji
  in the UI. Use simple inline SVG icons, 1.5px stroke, currentColor, 20x20.

=== PAGE CONTENT — 10 SECTIONS IN THIS ORDER ===

S1 HERO (left-aligned, max 780px, not centered)
- Eyebrow, uppercase 12px letter-spacing 1.2px color var(--gs):
  "LOVABLE · BOLT · REPLIT · CURSOR · SUPABASE"
- H1: "Your AI app is live. Nobody has checked who else can read it."
- Sub (18px var(--ts), max 640px): "In April 2026, every Lovable project created before
  November 2025 was readable by any free user for 48 days — source code, database
  credentials, AI chat history. No warning was sent. Most founders still don't know."
- Primary button "Check my app — free, 48 hours" (anchor #audit),
  secondary "What exactly gets checked" (anchor #checks)
- Thin row below, 13px var(--tm), middot separated: "Free audit" · "Written report" ·
  "No obligation" · "We fix it, or you take the report elsewhere"

S2 THE TWO INCIDENTS — the most important section. Two large cards side by side
(stack under 768px). Present as a factual record, not marketing. Each card has a small
label at top, an h3, and a definition-list style timeline with the label in 12px
uppercase var(--tf) and the value in 14px var(--text). Add a placeholder
<a href="#" class="src">Source</a> after each card with an HTML comment
<!-- ADD source links: The Register, TNW, Computing, OECD AI Incidents -->

Card A — label "APRIL 2026 · PLATFORM-LEVEL", h3 "Broken object level authorization"
  3 Mar 2026     Reported via HackerOne by researcher Matt Palmer
  Mar 2026       Patched — but only for projects created after November 2025
  ~48 days       Older projects stayed readable. No notification was sent.
  What leaked    Source code, database credentials, AI chat history, customer data
  Why it spread  Lovable apps commonly embed Supabase, Stripe and Google API keys
Below the card, a highlighted callout box (background var(--bs), border-left 3px solid
var(--red), border-radius var(--rs), padding 18px):
  "Was your project created before November 2025?" + inline primary button "Check my app"

Card B — label "MAY 2025 · APP-LEVEL", h3 "CVE-2025-48757 — missing row level security"
  Classification  CWE-863, Incorrect Authorization
  Scope           Lovable through 15 April 2025
  Scanned         1,645 apps from Lovable's public showcase
  Found           170 apps (~10.3%), 303 endpoints
  How             Readable and writable with the public anon key, because RLS had never
                  been enabled on those tables
  Leaked          Emails, addresses, in some cases API keys
  Root cause      Supabase creates new tables with RLS switched off by default
Add an HTML comment: <!-- Do NOT add a CVSS score: sources disagree (8.26 vs 9.3) -->

Then one short clarifying paragraph, 15px var(--ts), max 720px:
"These are two different kinds of problem. The 2025 CVE was a configuration gap in apps
people built, made likely by a default that ships switched off. The 2026 issue was in
Lovable's own platform. Both are fixable, and neither is a reason to stop using these
tools — but both are reasons to check what you shipped."

S3 THE SIX MOST COMMON GAPS — id="checks"
H2: "The six gaps we find most often"
Sub: "Each one has a two-minute check you can run yourself, right now, without us."
Six cards in a 2-column grid (1 column mobile). Each card: severity pill top-right,
a number in var(--fh) 800 26px with gradient text fill, h3, one paragraph on why AI
tools leave this gap, then a "RUN THIS CHECK" block (background var(--bs), radius
var(--rs), padding 14px, monospace 13px, label 11px uppercase letter-spacing 1px
color var(--tf)).

1. Critical — "RLS not enabled on Supabase tables"
   Why: "Supabase creates every new table with row level security switched off. The app
   works perfectly without it, so nothing ever tells you it is missing."
   Check: "Supabase → Table Editor. Any table without an 'RLS enabled' badge is readable
   by anyone holding your public key."

2. Critical — "Service role key in the frontend"
   Why: "The service role key bypasses every security rule by design. It ends up in
   frontend code because that is where the call that needed it was written."
   Check: "DevTools → Sources → search for 'service_role'. If it appears, anyone can
   write to your database."

3. Critical — "Authorization only in the UI"
   Why: "Hiding a button is not access control. The API underneath usually still answers
   anyone who asks it directly."
   Check: "Copy a URL while logged in as one user. Open it as a different user. Are you
   actually blocked, or just missing a menu item?"

4. High — "Project visibility set to public"
   Why: "'Public' sounds like it refers to the published app. It also exposed the source
   code and the AI chat history."
   Check: "Open your project settings and read what 'public' actually covers for your
   plan."

5. High — "No rate limiting on API routes"
   Why: "Nobody prompts for rate limiting. It only matters once someone decides to
   point a script at your login endpoint."
   Check: "Send 200 requests in a row to your login route. Does anything slow down or
   block you?"

6. Medium — "Secrets left in git history"
   Why: "Deleting the file removes it from the current version, not from history. The
   key is still there in an earlier commit."
   Check: "git log -p | grep -iE 'sk_live|service_role|password'"

S4 SELF-ASSESSMENT WIDGET — vanilla JS
H2: "Check your own app"
Sub: "Six questions. Two minutes. No email required."
Six rows, one per gap above, each a short question with Yes / No / Not sure pill buttons
(selected state uses var(--grd)). Count the number of gaps found.
Large result number "X of 6" using gradient text fill, with an aria-live region:
- 0 gaps  → var(--ok): "Clean on the basics. Auth logic is still worth a closer look."
- 1-2     → var(--amb): "Two gaps. Both are usually same-day fixes."
- 3+      → var(--red): "Your database is very likely readable right now."
Count every "Not sure" as a gap, and say so in a 12.5px note under the widget.
Then a primary button "Get these checked properly" that scrolls to #audit and writes the
count into the hidden input named "risk_score".

S5 AUDIT SCOPE — two columns, equal width
H2: "What the free audit covers — and what it doesn't"
Left card, border-left 3px solid var(--ok), h3 "Covered":
  RLS and table-level access · Key and secret exposure (frontend + git history) ·
  API-level authorization on your real endpoints · Project visibility settings ·
  Rate limiting on auth routes · A written report you keep
Right card, border-left 3px solid var(--tf), h3 "Not covered":
  A full penetration test · ISO 27001 or SOC 2 certification ·
  Third-party vendor code review · Infrastructure and network testing ·
  Load and performance testing
Below, 14px var(--tm): "If you need a full pentest or a certification audit, say so and
we will tell you who to call. That is a different job."

S6 POSITIONING — H2: "The audit is free. The value is in the fix."
One paragraph, 16px var(--ts), max 720px: "Automated scanners will sell you a report for
a couple of hundred euros. A report is not a fixed app. We give you the findings for
free because the findings are the easy part — then you decide whether we close the gaps
or you take the report to someone else."
Then three steps, horizontal on desktop with a thin connecting line:
1. "Free audit, 48 hours" — "Send the repo or the live URL. Written report back in two
   working days. No call required."
2. "Fixed-scope fix plan" — "Exactly what gets fixed, what it costs, how long it takes.
   Before anything starts."
3. "Re-test and sign-off" — "We re-run every check and give you the written
   confirmation. Useful when a customer or an investor asks."

S7 TECHNICAL DUE DILIGENCE — give this its own distinct section with a subtle
background change (background var(--white), with a top and bottom 1px solid var(--bd))
H2: "Raising a round? Investors will read this code."
Sub: "Technical due diligence on an AI-generated codebase asks different questions than
it did three years ago. Those questions have predictable answers, and you can prepare
them in advance."
Three cards:
- "What gets looked at" — "Architecture decisions, dependency risk, secret handling,
  test coverage, and whether one person leaving stops the product."
- "What AI-generated code triggers specifically" — "Reviewers now ask how much was
  generated, who reviewed it, and whether anyone on the team can explain the parts
  that matter."
- "What you get" — "A report written to be forwarded. Findings, severity, remediation
  status, and what was fixed before the round."
Primary button: "Prepare for technical due diligence"

S8 AVG / GDPR — keep SHORT on this English page
H2: "AVG and GDPR for AI-built apps"
Two short paragraphs covering personal data handling, breach notification duty, and
processor agreements, then a link styled as a secondary button:
"Read this in Dutch — AVG compliance" pointing to "/ai-app-beveiliging" with an HTML
comment <!-- NL version: expand this section substantially and use the word AVG, not GDPR -->

S9 SOCIAL PROOF
H2: "What others experience"
Three stat blocks, big numbers with gradient text fill, labels 13px var(--tm). Use "—"
placeholders with <!-- REPLACE with real figures -->.
Two testimonial cards: quote in var(--fa) italic 18px, then name and role 13px var(--tm),
also placeholders.
Do NOT invent certification badges or trust seals.

S10 CONTACT FORM — id="audit"
H2: "Send it over. Report back in 48 hours."
Form, stacked, max-width 620px:
- Name (text, required)
- Email (email, required)
- "Built with" (select, required): Lovable, Bolt, Replit, Cursor, v0, Other
- "Was your project created before November 2025?" (select, required): Yes, No, Not sure
- "Using Supabase?" (select): Yes, No, Not sure
- "Repo or live URL" (url, optional)
- "What worries you most?" (textarea, 4 rows)
- "Reason for the audit" (select, required): "Launching soon", "Investor due diligence",
  "An enterprise customer asked", "We already had an incident", "Just want to know"
- Five hidden inputs named exactly: click_id, click_type, landing, source, risk_score
- Submit, primary, full width: "Request free audit"
Inputs: var(--white) background, 1px solid var(--bd), border-radius var(--rs),
padding 13px 16px, var(--fb) 15px. Focus: border-color var(--gs),
box-shadow 0 0 0 3px rgba(47,128,237,.1), no default outline.
Add a 12.5px var(--tf) line under the submit button: "We do not run anything against
your app without written permission."

Add a script at the end that reads a cookie named ls_click inside try/catch and fills
the hidden fields, setting source to 'organic_or_other' when no click id is present.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section> elements, <label> bound to every input.
- Responsive, single 768px breakpoint, no horizontal scroll at 360px.
- Accessible: visible focus rings, aria-live on the widget result, 4.5:1 minimum
  contrast, and severity never communicated by colour alone — always include the text
  label.
- Respect prefers-reduced-motion: disable transforms and transitions.
- Light mode only. No dark mode.
- One HTML file, inline CSS and JS, only the three font links external.
```

---

## 7. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Tra lại CVE-2025-48757 trên NVD** | Nguồn vênh CVSS 8.26 vs 9.3. Không in số nếu chưa chắc |
| 2 | 🔴 **Thêm link nguồn thật cho cả hai sự cố** | The Register, TNW, Computing, OECD AI Incidents. **Không dẫn blog SEO của đối thủ** |
| 3 | Thay placeholder social proof | Đừng để `—` lên production |
| 4 | **Quyết định URL** + hreflang | Đề xuất `/en/ai-app-security` + `/ai-app-beveiliging` |
| 5 | **Viết bản NL — không dịch máy** | Mở rộng hẳn phần AVG + due diligence, giữ EN cho tên lỗi kỹ thuật |
| 6 | Schema `Service` + `FAQPage` + `HowTo` | 6 bước tự kiểm là `HowTo` rất tự nhiên |
| 7 | Internal link từ các bài security có sẵn | `keyword_research_lovable_vibecoding_security.md` §1.2: đây là lý do page phải có trước |
| 8 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2② |
| 9 | Conversion action `Qualified Lead` | Phân tầng theo trường `Reason for the audit` |
| 10 | ⚖️ **Rà lại tông giọng lần cuối** | Mục tiêu: không câu nào có thể đọc thành cáo buộc. Chỉ sự kiện + nguồn |

> 🔴 **Mục 1, 2 và 10 không được bỏ qua.** Trang này nêu tên một công ty thật và một CVE thật. Chính xác về dữ kiện vừa là nghĩa vụ, vừa là **chính thứ khiến LLM trích dẫn bạn** thay vì trích vibeappscanner. Một con số CVSS sai sẽ phá huỷ uy tín của cả trang.

> 💡 **Khác với `/ai-app-into-production`, trang này nên `index`, không `noindex`.** Nó có volume thật (~70/tháng), có đối thủ xác minh, và có hai entity (`CVE-2025-48757`, sự cố Lovable 4/2026) mà LLM sẽ tra. Nếu cần một URL đo lường ads sạch, tạo bản sao `noindex` riêng.

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
