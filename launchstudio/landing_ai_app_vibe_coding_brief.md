# ⚡ Landing page `/ai-app-vibe-coding` — Content brief + Lovable prompt (v2: vibe style, Pain → Solution)

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-vibe-coding` (hiện **404**)
> **File kèm:** `keyword_ai_app_vibe_coding.csv` (65 kw — **34 dùng được, 30 negative**)
> **Tham khảo đối thủ:** instinctools.com/vibe-coding-services · jploft.com (đã crawl, phân tích ở §4)
> **Phương pháp:** 45 seed × `gl=us` + `gl=nl` → 484 gợi ý → lọc

---

## 1. 🔴 Vấn đề lớn nhất: đây là trang thứ 4, và nó cạnh tranh với 3 trang kia

Bạn đang xây bốn landing page cùng phục vụ một nhóm khách:

| Trang | Thông điệp |
|---|---|
| `/ai-app-into-production` | "Làm nốt prototype của bạn" |
| `/ai-app-security` | "Kiểm tra bảo mật app của bạn" |
| `/ai-app-integrations` | "Sửa payment và database" |
| `/ai-app-vibe-coding` | ❓ **Chồng lấn cả ba** |

Nếu trang này cũng nói "chúng tôi giúp bạn đưa app vibe-coded lên production", nó **ăn thịt cả ba trang kia** và chính nó.

### ✅ Cách giải: biến nó thành trang trụ (pillar), không phải trang thứ 4

`vibe coding` là **từ danh mục** chứa cả ba vấn đề kia. Nên nó phải ở trên, không ở cạnh:

```
/ai-app-vibe-coding          ← PILLAR: trang danh mục, "vibe coding services"
├── /ai-app-into-production  ← spoke: làm nốt
├── /ai-app-security         ← spoke: bảo mật
└── /ai-app-integrations     ← spoke: payment + database
```

Vai trò cụ thể của pillar:
- **Bắt truy vấn danh mục** (`hire vibe coding developers`, `vibe coding cleanup services`)
- **Phân luồng** người đọc xuống spoke đúng với vấn đề của họ
- **Là trang được LLM trích dẫn** khi ai đó hỏi "who fixes vibe-coded apps"
- **Nhận link nội bộ** từ toàn bộ kho 60 bài `extra-1` → dồn authority về một chỗ

> 🔴 Nếu không làm vậy, bốn trang sẽ chia nhau cùng một lượng cầu vốn đã mỏng, và không trang nào đủ mạnh để rank hay để được trích dẫn.

Research của bạn §3.1 cũng đã gọi đúng nhu cầu này — ba keyword `hire vibe coding developer` (#66), `fix my vibe coded app` (#67), `vibe coding agency` (#68) đều ghi **"→ service page"** và **❌ chưa có**.

---

## 2. 🔴 Phải sửa một kết luận trong research của bạn

`keyword_research_lovable_vibecoding_security.md` §4.2 viết về `vibe coding cleanup specialist`:

> *"**≥4 agency có landing page riêng**: Redwerk, Suffescom, ThirdRock, AleaIT. **Xác minh mạnh nhất trong toàn bộ nghiên cứu.**"*

**Autocomplete cho thấy kết luận này sai.** Đây là những gì người ta thật sự gõ quanh cụm đó:

```
vibe code cleanup jobs                  vibe code cleanup specialist job
vibe code cleanup specialist linkedin   vibe code cleanup specialist salary
vibe code cleanup engineer              vibe coding cleanup jobs
vibe code cleanup specialist meaning    vibe coding cleanup meaning
vibe code cleanup specialist meme       vibe coding vulnerability as a service meme
vibe code cleanup specialist là gì      vibe coding cleanup specialist adalah
vibe code cleanup prompt
```

Ba nhóm, không nhóm nào là người mua:

| Nhóm | Bằng chứng | Họ là ai |
|---|---|---|
| **Người tìm việc** | `jobs`, `job`, `salary`, `linkedin`, `engineer` | Muốn *làm* nghề này |
| **Người tra nghĩa** | `meaning`, `là gì` (tiếng Việt), `adalah` (tiếng Indonesia) | Đọc về một *trend nghề nghiệp* |
| **Người xem meme** | `meme` ×2 | Thuật ngữ đã thành câu chuyện cười |

> 💡 **`là gì` và `adalah` là tín hiệu quyết định.** Hai từ đó là "nghĩa là gì" trong tiếng Việt và tiếng Indonesia. Người Việt và người Indonesia tra nghĩa của một job title tiếng Anh **không phải khách hàng châu Âu đi tìm agency.** Họ đang đọc về một nghề mới nổi.

### Bài học sâu hơn

`volume_analysis_results.md` §4 đã kết luận: chỉ **tín hiệu cầu** (đối thủ trả tiền/làm landing page) mới dự đoán được volume, tín hiệu cung thì vô giá trị.

Cụm này cho thấy một tầng nữa: **tín hiệu cầu cũng sai được, nếu đối thủ cũng nhầm.** Bốn agency kia làm landing page cho một từ mà người tìm phần lớn là người xin việc. Họ sao chép nhau, không ai kiểm autocomplete.

**Dạng an toàn — giữ lại trong CSV:**
```
vibe coding cleanup services     vibe coding cleanup company
vibe code cleanup services       vibe code cleanup company
vibe coding cleanup expert
```
`services` / `company` là cách người mua nói. `specialist` / `engineer` là cách người xin việc nói. Khác biệt một từ, khác biệt toàn bộ ý định.

---

## 3. 🔴 Ba bẫy đồng âm — hai cái rất nặng

### Bẫy 1 — `bolt app` là app gọi xe, không phải bolt.new

```
how to fix bolt app                 how to fix bolt app not showing download
bolt merchant app                   fix bolt action
fix bolt action rifle               fix the bolt
how to use fixing bolts             bolts fixit            bolt fixing
```

Ba thứ khác nhau chiếm cụm này: **Bolt** (hãng gọi xe/thanh toán châu Âu, rất lớn ở Đông Âu và châu Phi), **bolt action rifle** (súng), và **bu lông** (phần cứng). bolt.new chỉ là một phần nhỏ.

**Bid `fix bolt app` là trả tiền cho người không mở được app gọi xe.**

### Bẫy 2 — `lovable` là một tính từ tiếng Anh thông dụng

```
lovable branding agency      lovable design agency      lovable web design agency
lovable services inc         lovable agency template    lovable agency website
```

"Lovable" nghĩa là "đáng yêu" — nên `lovable agency` kéo về các hãng branding/design dùng từ này làm mô tả ("we build lovable brands"). Cùng loại bẫy với `clutch` (túi xách) và `bubble agency` (hãng PR).

Thêm một nhóm nữa phải loại: `lovable expert program`, `become a lovable expert`, `lovable expert jobs`, `lovable agency partner` — đây là **chương trình partner của chính Lovable** và người muốn tham gia nó.

**✅ Dạng an toàn:** `hire lovable ai developers`, `hire lovable expert`, `lovable development agency`, `lovable dev freelancer`, `lovable dev expert`.

### Bẫy 3 — `app aanmaken` (NL) là tạo tài khoản trong app ngân hàng

```
abn amro app aanmaken      rabobank app aanmaken      digid app aanmaken
albert heijn app aanmaken  kpn app aanmaken           postnl app aanmaken
odido app aanmaken         ing app aanmaken           app aanmaken op iphone
```

`aanmaken` = tạo/đăng ký. Toàn bộ cụm là người tiêu dùng Hà Lan đang đăng ký tài khoản trong app của ngân hàng, siêu thị, bưu chính.

**✅ Dạng NL an toàn:** `prototype laten maken`, `van prototype naar productie`, `prototype productie`, `lovable nederlands`.

---

## 4. 📊 Phân tích hai đối thủ bạn gửi

### instinctools.com/vibe-coding-services — đối thủ thật, nghiên cứu kỹ

| | |
|---|---|
| **H1** | "Vibe Coding as a Service" |
| **Giá** | ❌ **Không công bố giá** |
| **Chứng chỉ** | ISO 27001, 9001, 37001, 45001, 14001 (năm chứng chỉ) |
| **Giải thưởng** | Clutch 1000 2025 · Feedbax Top AI Dev 2025 · TechBehemots · DesignRush |
| **Khách tham chiếu** | CTO của Better.com · CEO Lition · VP Engineering Lawpilots · CEO SpexAI |
| **Số liệu họ dùng** | "AI agents shave 20–30% off coding time" · case 72% / 37% / 70% |
| **Công cụ nêu tên** | Semgrep, CodeQL, SonarQube (SAST) |

**🔴 Section 5 của họ là nguyên văn định vị của launchstudio:**

> *"Built with vibes, now stuck somewhere between half-baked prototype and production?"*

Đây không phải trùng hợp — đó là cùng một thị trường, và họ to hơn.

**Họ bán HAI thứ, launchstudio đang chỉ bán một:**

| Dịch vụ | instinctools | launchstudio |
|---|---|---|
| Sửa/hoàn thiện app vibe-coded | ✅ | ✅ |
| **Vibe coding enablement program** (dạy team khách tự làm an toàn) | ✅ | ❌ |

> 💡 **Đây là ý đáng lấy nhất từ họ.** Enablement là dòng doanh thu thứ hai, bán cho cùng một lead, không cần thêm chi phí marketing. Và nó bán được cho khách mà dịch vụ chính **không** bán được: công ty có team dev riêng, không muốn thuê ngoài, nhưng muốn làm đúng. Ở ngân sách ads mỏng của launchstudio, tận dụng mỗi lead theo hai cách là việc đáng làm.

**🥇 Chỗ đánh được họ: họ không công bố giá.** launchstudio đã công bố (từ €800, €1.500–2.500, tới €7.500). Với founder đang cân nhắc, một trang có giá thắng một trang phải "Book a call" — nó tự lọc và tự tạo niềm tin. **Đừng bỏ lợi thế này để bắt chước họ.**

**Cấu trúc FAQ của họ đáng học** — 7 câu đều là xử lý phản đối, không phải giải thích tính năng:
```
Is AI-generated code safe for production?
Are your vibe coders real developers?        ← câu đắt nhất
Who owns the IP, and how is governance handled?
What security risks to expect in vibe-coded applications?
```

### jploft.com — ⚠️ không phải đối thủ của trang này

| | |
|---|---|
| **H1** | "Build AI-Powered Digital Products That Scale Businesses" |
| **Thực chất** | Agency AI/mobile tổng hợp, **không chuyên vibe coding** |
| **Số liệu** | 16+ năm · 1.250+ dự án · 1,8M+ user · $180M+ vốn khách gọi được |
| **Giá** | Không công bố |

**Khuyến nghị thẳng: đừng lấy jploft làm mẫu.** Đó là trang agency đa dịch vụ chung chung — AI + SaaS + ERP + CRM + mobile. Nó cạnh tranh bằng quy mô và số lượng dự án, đúng mô hình mà `unicoconnect` và hàng trăm agency offshore đang dùng.

launchstudio không thắng được ở sân đó (không có 1.250 dự án), và quan trọng hơn: **bắt chước nó sẽ xoá mất thứ khiến launchstudio khác biệt** — chuyên một vấn đề, một thị trường, có giá công khai.

Thứ duy nhất đáng lấy từ jploft: **chỉ số "$180M+ client funding secured"**. Đó là cách diễn đạt giá trị thông minh — không nói về mình, nói về kết quả của khách. Nếu launchstudio có số liệu tương đương (vốn khách gọi được sau khi launch, doanh thu khách xử lý qua payment đã tích hợp), nó mạnh hơn mọi câu "chúng tôi có X năm kinh nghiệm".

### Và một đối thủ bạn chưa biết

Autocomplete trả về: **`vibe coding as a service cognizant`**

Cognizant — hãng IT services ~350.000 người — đã vào sân này. Không ảnh hưởng trực tiếp tới launchstudio (họ bán cho enterprise), nhưng nó xác nhận danh mục này đang được hợp pháp hoá ở tầng enterprise. Đó là tín hiệu tốt cho cầu, và là lý do nên chiếm từ danh mục sớm.

---

## 5. Bộ từ khoá: 34 dùng được / 30 negative

| Cụm | Kw | Vai trò |
|---|---:|---|
| **A — Hire vibe coding** | 13 | 🥇 ADS |
| **B — Hire Lovable** | 11 | 🥇 ADS (chỉ dạng an toàn) |
| **C — Hire tool khác** | 3 | ADS (1 SKIP) |
| **D — Head term nghiên cứu** | 4 | SEO/GEO |
| **E — NEGATIVE** | **30** | 🔴 Chặn |
| **F — NL** | 4 | ADS + SEO |

> 🔴 **Tỉ lệ 30 negative / 34 dùng được chính là kết luận của cụm này.** Gần một nửa truy vấn trông như thương mại lại là người tìm việc, người tra nghĩa, hãng branding, app gọi xe, hoặc người săn hàng miễn phí. Không có negative list, campaign này sẽ đốt phần lớn ngân sách vào nhóm đó.

### Cụm nên bid trước

```
hire vibe coding developers       hire vibe coding expert
hire lovable ai developers        hire lovable expert
lovable development agency        lovable dev freelancer
vibe coding cleanup services      vibe code security audit
hire cursor developers            prototype laten maken (NL)
```

### ⚠️ Cảnh báo giá từ research của bạn (§3.5)

> *"Nhóm 'thuê người' đang bị Fiverr/Upwork chiếm SERP với giá $10–30. LaunchStudio (€800–€7.500) không cạnh tranh bằng giá — phải cạnh tranh bằng góc 'tại sao gig $25 không sửa được lỗ hổng bảo mật'."*

Cảnh báo này vẫn đúng và **phải thể hiện ngay trên trang**, không chỉ nằm trong tài liệu. Xem S6 ở §7.

---

## 6. 🎨 Design system — token chính xác từ theme

Giống ba trang trước, đã đối chiếu 0 sai lệch với `style.css` live.

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
| Card | padding 24px, `1px solid var(--bd)`, radius `--rl`, shadow `--ss` |
| Button hover | `translateY(-2px)` + `0 14px 34px rgba(47,128,237,.22),0 6px 14px rgba(11,29,53,.1)` |

### 🎨 Hướng thiết kế v2 — "Builder-native": từ hỗn loạn tối → sạch sáng

Giữ **nhận diện thương hiệu** (bảng màu, gradient xanh–teal, Satoshi/Inter/Instrument Serif, letter-spacing âm, shadow mềm), nhưng **đổi phong cách** cho hợp dân vibe coding:

| Yếu tố | v1 (cũ) | v2 (mới) |
|---|---|---|
| Hero | Sáng, chữ trái, tĩnh | **Nền navy `#0B1D35`**, lưới mờ + glow gradient, **mock khung chat AI builder có animation** |
| Hình ảnh | Chỉ icon SVG | UI giả lập bằng code: khung chat, toast cảnh báo, thẻ "bug" kiểu console, toggle Before/After |
| Font phụ | — | Thêm **JetBrains Mono** cho chi tiết code/terminal (chỉ làm điểm nhấn) |
| Kể chuyện bằng màu | Sáng toàn trang | **Tối = app vibe-coded đang ẩn lỗi → Sáng = app đã được launchstudio xử lý**. Phần Solution chuyển sang nền sáng như site hiện tại |

> 💡 Ẩn dụ tối → sáng chính là thông điệp bán hàng: người đọc *thấy* app của họ đi từ trạng thái rối sang trạng thái sạch, trước khi đọc chữ nào.

**Ba thẻ dẫn sang spoke vẫn giữ** (nằm trong phần Solution) để trang làm đúng vai trò pillar ở §1.

---

## 7. 📝 Cấu trúc nội dung v2 — Pain → Solution → bổ trợ

**Đã bỏ theo yêu cầu:** bảng giá, form liên hệ. Mọi CTA trỏ ra trang liên hệ/đặt lịch hiện có của launchstudio.eu.
**Đã bỏ để ngắn gọn:** Enablement (S7 cũ), Kho nội dung (S9 cũ). Có thể thêm lại sau nếu cần.

> ⚠️ §4 từng khuyên đẩy giá công khai lên làm lợi thế. Bỏ giá là quyết định có đánh đổi: trang mất một điểm khác biệt so với instinctools. Bù lại bằng hook mạnh hơn ở hero và phần "$25 gig" thẳng thắn.

| # | Section | Vai trò | Thông điệp chính |
|---|---|---|---|
| S1 | **Hero** | 🪝 Hook | `Your AI said "Done." It wasn't.` + chat mock bật cảnh báo |
| S2 | **Pain** | 😬 Nhận diện | 6 lỗi ẩn, viết bằng ngôn ngữ founder chứ không phải ngôn ngữ dev |
| S3 | **Solution** | ✅ Giải pháp | `We keep the vibe. We add the engineering.` + toggle Before/After + 3 thẻ spoke |
| S4 | How it works | Bổ trợ | 3 bước, không có biểu mẫu |
| S5 | $25 gig? | Bổ trợ (bắt buộc, xem §5) | Thừa nhận gig có chỗ dùng → tăng độ tin |
| S6 | Who it's for | Bổ trợ | 4 pill nhận diện |
| S7 | FAQ | Bổ trợ | 4 phản đối, trả lời 1–2 câu |
| S8 | Proof | Bổ trợ | Placeholder số liệu + testimonial thật |
| S9 | **Final CTA** | 🎯 Chốt | `Stop prompting. Start launching.` — nền navy, đối xứng với hero |

### Vì sao hero này hút

1. **Câu "Done." là câu mọi người dùng Lovable/Bolt đã thấy.** H1 lấy đúng câu đó và lật lại → nhận diện ngay trong 2 giây.
2. **Chat mock diễn lại trải nghiệm của chính họ:** gõ prompt → AI báo xong → rồi cảnh báo đỏ bật lên. Người đọc không cần được *thuyết phục* là có vấn đề, họ *xem* nó xảy ra.
3. **Không chê người dùng AI.** Thông điệp là "AI đưa bạn đến 80%, chúng tôi làm 20% còn lại", không phải "vibe coding là rác".

---

## 8. 🤖 Prompt cho Lovable.dev (v2)

```
Build a single, self-contained landing page as ONE static `index.html` file: all CSS in
one inline <style> block, all JS in one inline <script> block. No React, no build step,
no router, no external dependencies except the four font links below. This file will be
pasted into a WordPress page template, so it must work standalone.

WHAT THIS PAGE IS
A landing page for LaunchStudio, a studio that takes apps built with AI coding tools
(Lovable, Bolt, Replit, Cursor, v0 — "vibe coding") and makes them production-ready:
secure, with working payments, and maintainable. Audience: founders who prompted their
way to a working app and now sense it isn't really ready. Story arc: PAIN first, then
SOLUTION, then short supporting sections. Copy is short and punchy. Tone: confident,
a little playful, builder-to-builder. Never mock the reader for using AI tools — the
message is "AI got you 80% there, we do the last 20%".
There is NO pricing section and NO form on this page. Every CTA links out.

=== BRAND — KEEP THESE EXACT TOKENS ===

:root{
  --navy:#0B1D35; --navy-2:#0F2747; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --on-dark:#E6EDF7; --on-dark-m:#9FB0C8; --line-dark:rgba(255,255,255,.08);
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --fm:'JetBrains Mono',ui-monospace,monospace;
  --r:12px; --rs:10px; --rp:999px; --rl:20px; --rx:24px;
  --ss:0 0 0 1px rgba(0,0,0,.03),0 2px 4px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04);
  --sm:0 0 0 1px rgba(0,0,0,.02),0 4px 8px rgba(0,0,0,.03),0 16px 32px rgba(0,0,0,.06);
  --sl:0 0 0 1px rgba(0,0,0,.02),0 8px 16px rgba(0,0,0,.04),0 24px 48px rgba(0,0,0,.08);
  --t:.28s; --ease:cubic-bezier(.22,1,.36,1);
}

FONTS — load exactly these. Satoshi comes from Fontshare, NOT Google Fonts. Never
substitute it:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@700,600,500,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

TYPOGRAPHY
- body: var(--fb) 16px, line-height 1.65, antialiased
- h1: var(--fh) 700, clamp(40px,6vw,76px), line-height 1.02, letter-spacing -2px
- h2: var(--fh) 700, clamp(30px,4vw,48px), line-height 1.08, letter-spacing -1px
- h3: var(--fh) 600, 19px, letter-spacing -0.3px
- Tight NEGATIVE letter-spacing on all headings is the brand signature — keep it.
- var(--fm) only for code-like details: chat text, severity tags, file names, toasts.
- var(--fa) italic for at most 3 emphasis words on the whole page.

LAYOUT
- max width 1160px centered, 20px side padding (16px under 768px)
- sections 112px 0 desktop, 72px 0 under 768px
- light cards: var(--white), 1px solid var(--bd), radius var(--rl), shadow var(--ss);
  hover: shadow var(--sm), translateY(-3px), transition all var(--t) var(--ease)
- primary button: background var(--grd), white, radius var(--rp), padding 15px 30px,
  var(--fh) 600 16px; hover translateY(-2px) + box-shadow 0 14px 34px rgba(47,128,237,.32)
- ghost button on dark: transparent, 1px solid rgba(255,255,255,.18), color var(--on-dark)
- ghost button on light: transparent, 1px solid var(--bd), color var(--navy)

VISUAL DIRECTION — "builder-native", dark chaos → light clarity
- Hero, Pain and Final CTA sit on DARK navy (var(--navy)) — this is "your app as it is
  now, hiding problems". The Solution section and everything after it sit on LIGHT
  var(--bg) — "your app after LaunchStudio". The switch from dark to light between Pain
  and Solution is the visual climax: use a soft 160px vertical gradient fade from
  var(--navy) to var(--bg) between them.
- Dark sections: a faint 40px grid pattern (1px lines, rgba(255,255,255,.035)) and one
  or two large blurred radial glows using #2F80ED and #14B8A6 at 18–25% opacity.
- All imagery is built in HTML/CSS/SVG: chat windows, code snippets, toasts, terminal
  cards. NO stock photos, NO robots, brains or generic AI art, NO emoji anywhere.
- Icons: inline SVG, 1.5px stroke, currentColor, 20x20.
- The blue-teal gradient is an accent: buttons, gradient text on 1–2 key words, icon
  tiles, glows. Never behind paragraphs.
- Red (--red) and amber (--amb) appear ONLY in the Pain story (severity tags, warning
  toasts). Green (--ok) appears ONLY in the Solution story. Colour carries the narrative.

=== PAGE CONTENT — 9 SECTIONS IN THIS ORDER ===

S1 HERO (dark) — two columns on desktop (copy left 52%, visual right), stacked on mobile
with copy first.
Left:
- Pill chip, var(--fm) 12.5px, 1px solid var(--line-dark), color var(--on-dark-m),
  a small pulsing teal dot before the text:
  "Built with Lovable · Bolt · Replit · Cursor · v0?"
- H1, color white: 'Your AI said <em>"Done."</em> It wasn't.'
  The em is var(--fa) italic, weight 400, with the gradient as text fill
  (background-clip:text).
- Sub, 19px var(--on-dark-m), max 520px:
  "Vibe coding got you 80% there. We handle the last 20% — security, payments and
  everything that breaks with real users — without rebuilding what you made."
- Buttons: primary "Get a free audit" (href = CTA_URL, see JS), ghost "See what
  breaks" (href #pain, with a small down-arrow SVG).
- Trust row, 13px var(--on-dark-m), separated by small dots:
  "Your code stays yours" · "No full rebuild" · "Real engineers, not more prompts"

Right — ANIMATED AI-BUILDER MOCK (the hook of the page):
A window card (background var(--navy-2), 1px solid var(--line-dark), radius var(--rx),
large soft shadow, three small grey dots in a top bar, title "my-saas-app" in var(--fm)).
Inside, a chat sequence that plays once when the page loads:
  1. User bubble types in letter by letter (var(--fm) 14px):
     "build me a booking app with stripe payments and user logins"
  2. After 600ms, an assistant bubble with a green check icon:
     "Done! Your app is ready to deploy."  followed by a small fake "Deploy" button
     that gets a pressed state.
  3. Then three warning toasts slide in from the right, 500ms apart, stacking over the
     lower part of the window, each with a severity tag in var(--fm) 11px uppercase:
     [CRITICAL, red]  "Row Level Security disabled on table `bookings`"
     [CRITICAL, red]  "STRIPE_SECRET_KEY exposed in client bundle"
     [HIGH, amber]    "Webhook /api/stripe → 404 · 0 of 37 payments recorded"
     Toasts: background rgba(220,38,38,.10) or rgba(217,119,6,.10), 1px border in the
     same hue at 35%, light text, slight blur backdrop.
  4. Small caption under the window, var(--fm) 12px var(--on-dark-m):
     "// what your AI builder won't tell you"
With prefers-reduced-motion: show the final state immediately, no typing, no sliding.

S2 PAIN (dark) — id="pain"
- Small label, var(--fm) 12px uppercase, color var(--red): "> npm run audit"
- H2 white: "It looks finished. Here's what's hiding underneath."
- Six "bug cards" in a 3x2 grid (1 column on mobile). Dark card style: background
  rgba(255,255,255,.03), 1px solid var(--line-dark), radius var(--rl), padding 24px.
  Each card: severity tag (var(--fm) 11px, coloured pill), h3 in white, one line in
  15px var(--on-dark-m). Cards fade-and-rise in on scroll, staggered 80ms.
  1. CRITICAL — "Anyone can read your database" —
     "Row Level Security is off. One API call exposes every user's data."
  2. CRITICAL — "Your secret keys ship to the browser" —
     "Stripe or OpenAI keys sit in your frontend. Someone else runs up your bill."
  3. HIGH — "Payments succeed. Orders don't." —
     "The webhook never fires. The money arrives, your app never finds out."
  4. HIGH — "One weird input, blank screen" —
     "No error handling. Users leave and you never learn why."
  5. MEDIUM — "Every fix breaks two things" —
     "You're on prompt #47 of 'fix the login'. No tests catch what broke."
     Inside this card add a tiny mono stack of three struck-through lines in
     var(--tf): "fix the login" / "fix the login again" / "pls just fix the login"
  6. MEDIUM — "No developer wants to touch it" —
     "Your first engineer opens the repo and quotes you a rewrite."
- Bridge line centered under the grid, var(--fh) 600 22px white:
  "None of this shows in the preview. <span gradient text>All of it shows at launch.</span>"

[dark → light gradient fade here]

S3 SOLUTION (light)
- Small label, var(--fm) 12px uppercase, color var(--ok): "> all checks passed"
- H2: 'We keep the vibe. We add the <em>engineering.</em>' (em = var(--fa) italic)
- Sub 18px var(--ts), max 620px: "Your UI, your logic and your product decisions stay.
  We fix what the prompt never covered — inside your repo."

Part A — BEFORE / AFTER TOGGLE (interactive, the "wow" moment of the light half):
A large white card (shadow var(--sl), radius var(--rx)) with a segmented toggle at the
top: "Vibe-coded" | "Production-ready". Default is "Vibe-coded". Below, six rows that
mirror the six pain cards. In "Vibe-coded" state each row shows a red cross icon and the
problem in var(--fm); in "Production-ready" state each row animates (staggered 60ms) to a
green check icon and the fix:
  RLS disabled                 → Row Level Security on every table
  Keys in the client bundle    → Secrets in server-side env, keys rotated
  Webhooks silently failing    → Verified webhooks, every payment recorded
  No error handling            → Graceful errors + logging you can read
  No tests                     → Tests on the flows that make you money
  Unreadable codebase          → Clean structure your first hire can own
Auto-flip to "Production-ready" once when the card first scrolls into view (skip the
animation under reduced motion). The toggle remains clickable. Use role="tablist" or
aria-pressed buttons, and announce the state for screen readers.

Part B — THREE ROUTES (keep — this page routes readers to deeper pages)
Intro line, var(--fh) 600 22px: "Start where it hurts most."
Three cards in a row (stacked on mobile), shadow var(--sm). Each: 48x48 rounded tile
with the gradient background and a white 24px SVG icon, h3, one italic question in
var(--fa) 18px var(--ts), three short bullets, and a text link with an arrow SVG that
nudges right on hover.
  "Finish it" — "It works on my screen, but I can't launch it." —
    Secrets & env vars · Error handling & CI · Tests on key flows —
    link "Production readiness" → /ai-app-into-production
  "Secure it" — "Who else can read my database?" —
    Row Level Security · Exposed keys · API authorization —
    link "Security audit" → /ai-app-security
  "Connect it" — "Payments or data are quietly broken." —
    Stripe, Mollie & iDEAL · Webhooks · Migrations & backups —
    link "Payments & databases" → /ai-app-integrations

S4 HOW IT WORKS (light)
H2: "From 'it works on my machine' to live. Three steps."
Three numbered steps in a horizontal row connected by a thin dashed line (vertical on
mobile). Numbers in gradient text, var(--fh) 700 44px.
  01 "Send us the link" — "Repo or live URL. Lovable, Bolt, Replit, Cursor or v0 —
     all fine."
  02 "Get a plain-English audit" — "What's broken, what's risky, what to fix first."
  03 "We fix it in your repo" — "Reviewed by engineers, merged into your code, handed
     back. You keep shipping."

S5 THE $25 GIG QUESTION (light, background var(--white) band with 1px var(--bd) top and
bottom)
H2: "Can't I just hire a $25 gig?" (keep the quotation marks visible on the page)
Sub, 18px var(--ts): "For one bug you already found? Honestly, yes."
A real <table>, max 820px, three columns: criterion | "Freelance gig" | "LaunchStudio".
Check SVG in var(--ok), cross SVG in var(--tf), each with visually-hidden "Yes"/"No".
  "Fixes the bug you point at" — yes / yes
  "Finds the bugs you don't know about" — no / yes
  "Checks database security, keys and webhooks" — no / yes
  "Still around if it breaks in 3 months" — no / yes
Final row on var(--bs), label "Best when":
  "One known bug, no deadline" / "You're about to launch, raise or sign a big customer"

S6 WHO IT'S FOR (light) — one compact row, no cards
Label, var(--fm) 12px uppercase var(--tm): "Built for"
Four pills (white, 1px var(--bd), radius var(--rp), 15px, small icon each):
"Solo founders" · "Founders who code a little" · "Agencies with a client's AI-built app"
· "Teams shipping fast with AI tools"

S7 FAQ (light) — accordion using <details>/<summary>, max 760px, plus/minus icon that
rotates. H2: "Quick answers"
  "Do you rebuild it from scratch?" — "No. We keep what works and add what's missing:
   security, error handling, tests and CI."
  "Do your people vibe code too?" — "We use AI tools daily. Every change is reviewed by
   an engineer, and security issues are confirmed with static analysis (Semgrep, CodeQL,
   SonarQube) — not by asking a model."
  "Which tools do you support?" — "Lovable, Bolt, Replit, Cursor, v0, and anything that
   produces a normal codebase."
  "Who owns the code?" — "You. Your repo, your accounts, your infrastructure."

S8 PROOF (light)
H2: "Founders who shipped"
Three stat blocks: big numbers in gradient text (var(--fh) 700 48px), labels 14px
var(--tm). Use "—" placeholders with:
<!-- REPLACE with real figures. Prefer client outcomes (apps launched, funding raised
after launch, payments processed) over years in business -->
Two testimonial cards: quote in var(--fa) italic 20px, name + role + "Built with
Lovable" style tag in var(--fm) 12px. Placeholder text with <!-- REPLACE with real
testimonial -->.
Do NOT invent certification badges, ISO logos, award seals or client logos.

S9 FINAL CTA (dark, same grid + glow treatment as the hero, centered)
- A mono line in var(--on-dark-m) with a strike-through animation:
  "> fix the login again"  (the strike draws across on scroll into view)
- H2 white, larger (clamp(36px,5vw,60px)):
  'Stop prompting. <span gradient text>Start launching.</span>'
- Sub, 18px var(--on-dark-m): "Free audit. Plain-English report. No obligation."
- Primary button "Get my free audit" (href = CTA_URL)

FOOTER: one slim line, 13px var(--tm) on var(--bg): "© LaunchStudio · launchstudio.eu"

=== JS ===
- const CTA_URL = "https://launchstudio.eu/en/#contact"; // REPLACE with real contact
  or booking URL. Set it on every element with data-cta.
- Attribution: read gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content from location.search and append any that exist to CTA_URL on
  every data-cta link, plus landing=ai-app-vibe-coding.
- Hero chat sequence, scroll reveals (IntersectionObserver), Before/After toggle,
  auto-flip once, strike-through on S9. Keep it small, vanilla, no libraries.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section> elements with aria-labelledby.
- Responsive, single 768px breakpoint, no horizontal scroll at 360px. On mobile the hero
  mock stays visible but scales down; toasts stack inside the window.
- Contrast at least 4.5:1 on both dark and light sections (check the muted text on
  navy). Visible focus rings (2px var(--ge) outline, 3px offset).
- prefers-reduced-motion: disable typing, sliding, staggering and transforms; show all
  final states.
- Severity and yes/no never conveyed by colour alone — always text or hidden labels.
- One HTML file, inline CSS and JS, only the four font links external.
```

---

## 9. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Quyết định kiến trúc pillar/spoke** | Xem §1. Không làm bước này thì 4 trang ăn thịt nhau |
| 2 | 🔴 **Áp 30 negative keyword ở cấp tài khoản** | Xem §2 và §3. Đây là phần quyết định của cụm này |
| 3 | 🔴 **Cập nhật research §4.2** | `vibe coding cleanup specialist` không phải "xác minh mạnh nhất" — xem §2 |
| 4 | 🔴 **Thay `CTA_URL`** | Trỏ tới trang liên hệ/đặt lịch thật. Kiểm tra tham số `gclid`/`utm_*` có đi theo sang trang đích |
| 5 | Kiểm tra animation hero trên mobile | Chat mock + 3 toast phải đọc được ở 360px, không tràn |
| 6 | Thay số liệu và testimonial placeholder ở S8 | Không có số thật thì bỏ khối stat, giữ testimonial |
| 7 | Link nội bộ 4 chiều | Pillar → 3 spoke, và 3 spoke → pillar |
| 8 | Link 60 bài `extra-1` về pillar | Bỏ kho nội dung khỏi trang thì phải link từ bài về đây |
| 9 | Nạp 34 kw dùng được vào Keyword Planner | Chưa có volume thật, trừ `bolt ai` 1.300 (research §3.2) |
| 10 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2② — giờ ghi nhận ở trang liên hệ, không phải form trên trang này |

---

## 10. Thứ tự ưu tiên bốn landing page (cập nhật)

| | Trang | Vai trò | Lý do |
|---|---|---|---|
| 🥇 | **`/ai-app-vibe-coding`** | **PILLAR** | Phải có trước để ba trang kia có chỗ bám. Bắt từ danh mục. Nhận authority từ 60 bài |
| 🥈 | `/ai-app-security` | spoke | Research gọi là nút cổ chai · ~70/tháng · có CVE + sự cố 4/2026 |
| 🥉 | `/ai-app-integrations` | spoke | 66 kw validate · lợi thế địa phương `lovable mollie`/`lovable ideal` |
| 4 | `/ai-app-into-production` | spoke | Trùng thông điệp trang chủ · ~10/tháng |

> 💡 **Thứ tự này đã đổi so với lần trước.** Trước đây tôi xếp security hạng nhất. Sau khi thấy rõ bốn trang chồng lấn nhau, pillar phải đi trước — không phải vì nó mang nhiều traffic hơn, mà vì **nó là thứ quyết định ba trang kia có cạnh tranh nhau hay không.**

---

## 11. Nguồn

- [instinctools — Vibe Coding as a Service](https://www.instinctools.com/vibe-coding-services/) (crawl 06/10/2026)
- [JPLoft](https://www.jploft.com/) (crawl 06/10/2026)
- Google Autocomplete (`hl=en`, `gl=us` + `gl=nl`), 45 seed → 484 gợi ý, 06/10/2026
- `keyword_research_lovable_vibecoding_security.md` §3 (cụm ②), §4.2
- `volume_analysis_results.md` §4 (bài học tín hiệu cầu vs tín hiệu cung)
- `google_ads_plan_payments_nl.md` §11 (giá gói payment)
- Design token: `launchstudio.eu/wp-content/themes/launchstudio/style.css`
