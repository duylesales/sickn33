# ⚡ Landing page `/ai-app-vibe-coding` — Content brief + Lovable prompt

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

**Riêng trang pillar này:** vì nhiệm vụ là phân luồng, ba thẻ dẫn sang spoke phải là phần tử thị giác mạnh nhất sau hero — dùng `--sm` shadow và gradient cho icon, không để chúng trông như link phụ ở cuối trang.

---

## 7. 📝 Cấu trúc nội dung — 10 section

### S1 — Hero
- **Eyebrow:** `LOVABLE · BOLT · REPLIT · CURSOR · V0`
- **H1:** `Vibe coding got you a working app. We make it a real one.`
- **Sub:** `You prompted your way to something that works. Now it needs to be secure, take real money, survive real users, and still be maintainable when you hire your first engineer. That's a different job, and it's the only one we do.`
- **CTA chính:** `Get a free audit`
- **CTA phụ:** `See what it costs ↓` ← **đẩy giá lên trước, vì đối thủ không có**
- **Trust strip:** `Published pricing · Your code stays yours · No full rebuild`

### S2 — ⭐ Ba đường phân luồng (quan trọng nhất ở trang pillar)

Ba thẻ lớn, mỗi thẻ dẫn sang một spoke. Đây là lý do tồn tại của trang.

| Thẻ | Câu hỏi nhận diện | Dẫn tới |
|---|---|---|
| **Finish it** | "It works on my screen but I can't launch it" | `/ai-app-into-production` |
| **Secure it** | "I don't know who can read my database" | `/ai-app-security` |
| **Connect it** | "Payments or the database are broken" | `/ai-app-integrations` |

Mỗi thẻ: icon, tiêu đề, một câu nhận diện vấn đề, 3 bullet, link.

### S3 — Đối tượng này là ai (nhận diện)

Bốn chân dung ngắn: solo founder non-technical · founder có chút code · agency nhận app vibe-coded của khách · team nội bộ dùng AI tool nhưng không có senior review.

> 💡 Chân dung thứ 3 và 4 là người instinctools đang bán cho. Nêu ra để không tự giới hạn vào solo founder.

### S4 — Bốn phản đối, trả lời thẳng

Học cấu trúc FAQ của instinctools nhưng trả lời cụ thể hơn:

| Phản đối | Hướng trả lời |
|---|---|
| **"Phải build lại từ đầu không?"** | Không. Nêu rõ cái gì giữ, cái gì thêm. |
| **"Người của bạn là dev thật hay cũng vibe code?"** | Câu đắt nhất. Trả lời thẳng: ai review, kinh nghiệm bao lâu, dùng công cụ gì (Semgrep/CodeQL/SonarQube). |
| **"Sao không thuê gig $25 trên Fiverr?"** | 🔴 **Bắt buộc có** — xem S6. |
| **"IP thuộc về ai?"** | Code của bạn, repo của bạn, account của bạn. |

### S5 — ⭐ Giá công bố (lợi thế cạnh tranh trực tiếp)

Đặt **cao trên trang**, không ở cuối. Ba mức theo spoke:

| Gói | Giá | Nội dung |
|---|---|---|
| Production readiness | `từ €—` | — |
| Security audit + fix | `từ €—` | — |
| Payment/database setup | `€1.500–2.500` | Theo `google_ads_plan_payments_nl.md` §11 |

> 🔴 Lấy giá thật từ `launchstudio.eu/en/`. Tôi để placeholder vì không muốn tự đặt số.
>
> 💡 Thêm một dòng ngay dưới bảng: *"instinctools, Suffescom and most agencies in this space don't publish prices. We do, because you should be able to rule us out in thirty seconds."* — biến minh bạch thành luận điểm bán hàng.

### S6 — 🔴 `$25 gig vs studio` (bắt buộc)

Trực tiếp xử lý cảnh báo §3.5 của research. Bảng so sánh thật, không chê bai:

| | Fiverr gig $25–50 | launchstudio |
|---|---|---|
| Sửa được lỗi bạn chỉ ra | ✅ | ✅ |
| Tìm lỗi bạn **chưa biết là có** | ❌ | ✅ |
| Kiểm RLS / secret / webhook | ❌ | ✅ |
| Chịu trách nhiệm khi vỡ sau 3 tháng | ❌ | ✅ |
| Báo cáo gửi được cho investor | ❌ | ✅ |
| Phù hợp khi | Một lỗi cụ thể, đã biết | Chuẩn bị launch / gọi vốn / có khách enterprise |

> 💡 **Hàng cuối là hàng quan trọng nhất.** Nó thừa nhận gig $25 có chỗ dùng hợp lý — điều đó làm tăng độ tin của cả bảng, và lọc đúng người không phải khách của bạn.

### S7 — Enablement program (dòng doanh thu thứ hai)

Lấy từ instinctools. Bán cho công ty có team dev riêng: chọn công cụ, context engineering, security protocol, CI guardrail, review process.

- **H2:** `Or teach your team to do this safely`
- 4 bullet, một CTA riêng: `Talk about team enablement`

> ⚠️ Chỉ đưa section này lên nếu thật sự định bán. Một trang quảng cáo dịch vụ không tồn tại sẽ tạo lead không chốt được.

### S8 — Chứng minh

Số liệu + testimonial. Nếu có chỉ số dạng "vốn khách gọi được sau launch" hoặc "doanh thu xử lý qua payment đã tích hợp", dùng nó — mạnh hơn "X năm kinh nghiệm". **Nếu chưa có chứng chỉ ISO thì bỏ hẳn, đừng tạo badge trông như chứng chỉ.**

### S9 — Kho nội dung (tài sản GEO)

Link tới 60 bài `extra-1` theo nhóm chủ đề. Đây là chỗ pillar nhận và truyền authority.

### S10 — Form

| Trường | Ghi chú |
|---|---|
| Name, Email | bắt buộc |
| **Built with** | Lovable / Bolt / Replit / Cursor / v0 / Other |
| **What do you need?** | Finish it / Secure it / Connect payments or DB / Not sure — ⭐ phân luồng |
| **Who are you?** | Solo founder / Founder with some code / Agency with a client app / In-house team |
| **Live URL or repo** | optional |
| Mô tả ngắn | textarea |
| **Budget range** | select, bắt buộc |
| 🔒 hidden | `click_id`, `click_type`, `landing`, `source` |

---

## 8. 🤖 Prompt cho Lovable.dev

```
Build a single, self-contained landing page as ONE static `index.html` file, with all CSS
in one inline <style> block and all JS in one inline <script> block. No React, no build
step, no router, no external dependencies except the three font links below. This file
will be pasted into a WordPress page template, so it must work standalone.

This is a PILLAR page for a service category: fixing and finishing apps built with AI
coding tools (Lovable, Bolt, Replit, Cursor, v0) — commonly called vibe coding. Its main
job is to route the reader to one of three deeper pages, and to state pricing openly
because competitors hide theirs. Audience: a founder who shipped something that works
and now needs it to be real. Tone: direct, specific, confident without hype. Never
mock the reader for using AI tools.

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
- h1: var(--fh) 700, clamp(34px,4.2vw,52px), line-height 1.08, letter-spacing -1.5px
- h2: var(--fh) 700, clamp(28px,3.5vw,44px), line-height 1.12, letter-spacing -0.8px
- h3: var(--fh) 600, 20px, letter-spacing -0.3px
- small: 14px var(--tm) line-height 1.7 · caption: 12.5px var(--tf)

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

VISUAL CHARACTER — critical to match the existing site:
- Light, airy, clinical. Page background #F8FAFE, never pure white, NEVER dark mode.
- Shadows always soft and multi-layered. Never one heavy shadow.
- Headings use tight NEGATIVE letter-spacing — the brand signature.
- Blue-teal gradient is an ACCENT only: primary buttons, big numbers, small badges,
  and the three routing card icons. NEVER a full-width section background, never
  behind body text.
- Instrument Serif italic very sparingly — one or two emphasis phrases maximum.
- No stock photos, no AI/robot/brain imagery, no emoji in the UI. Simple inline SVG
  icons only, 1.5px stroke, currentColor, 20x20 (28x28 for the three routing cards).

=== PAGE CONTENT — 10 SECTIONS IN THIS ORDER ===

S1 HERO (left-aligned, max 780px, not centered)
- Eyebrow, uppercase 12px letter-spacing 1.2px color var(--gs):
  "LOVABLE · BOLT · REPLIT · CURSOR · V0"
- H1: "Vibe coding got you a working app. We make it a real one."
- Sub (18px var(--ts), max 650px): "You prompted your way to something that works. Now
  it needs to be secure, take real money, survive real users, and still be maintainable
  when you hire your first engineer. That is a different job, and it is the only one
  we do."
- Primary button "Get a free audit" (anchor #contact),
  secondary "See what it costs" (anchor #pricing)
- Thin row below, 13px var(--tm), middot separated: "Published pricing" ·
  "Your code stays yours" · "No full rebuild"

S2 THREE ROUTES — the most important section on this page. Three large cards in a row
(stack under 768px), each visually prominent: box-shadow var(--sm), a 28x28 SVG icon in
a 48x48 rounded tile with the gradient as background and white stroke, an h3, one
italic identifying question in var(--fa) 17px color var(--ts), three short bullets, and
a text link with a right-arrow SVG.
H2: "Three things break. Pick the one that sounds like you."

Card 1 — h3 "Finish it"
  Question: "It works on my screen, but I cannot launch it."
  Bullets: Secrets and environment variables · Error handling and CI · Tests on the
  flows that matter
  Link: "Production readiness" → /ai-app-into-production

Card 2 — h3 "Secure it"
  Question: "I do not know who else can read my database."
  Bullets: Row level security · Exposed keys · API-level authorization
  Link: "Security audit" → /ai-app-security

Card 3 — h3 "Connect it"
  Question: "Payments or the database are quietly broken."
  Bullets: Stripe, Mollie and iDEAL · Webhooks that never fire · Migrations and backups
  Link: "Payments and databases" → /ai-app-integrations

S3 WHO THIS IS FOR — four compact cards in a 2x2 grid, each an h3 and two sentences
H2: "Who we work with"
1. "Solo founders, non-technical" — "You built it with prompts and it works. You have
   no way to tell what is missing."
2. "Founders who code a little" — "You know enough to be worried, and not enough to
   be sure."
3. "Agencies holding a client's vibe-coded app" — "You inherited it and now you own
   the risk. We work white-label."
4. "In-house teams using AI tools" — "The code ships fast. Nobody senior is reviewing
   what it ships."

S4 FOUR OBJECTIONS — accordion or four stacked cards, each an h3 question and a
direct answer in 15px var(--ts). Answer plainly, no marketing language.
H2: "The four things people ask first"
1. "Do you rebuild it from scratch?" — "No. Your UI, your business logic, your database
   schema and your product decisions stay. We add the parts that were never in the
   prompt: secret management, API-level authorization, error handling, CI, tests and
   logging."
2. "Are your people real developers, or do they vibe code too?" — "We use AI tools
   daily, and every change is reviewed by an engineer who can explain it. Security
   findings are confirmed with static analysis — Semgrep, CodeQL and SonarQube — not
   by asking a model whether the code is safe."
3. "Why not a 25 dollar gig instead?" — "Sometimes that is the right call. See the
   comparison below."
4. "Who owns the code and the IP?" — "You do. Your repo, your accounts, your
   infrastructure. We work in your environment and hand it back."

S5 PRICING — id="pricing". Place this HIGH on the page, not at the bottom.
H2: "What it costs"
Sub: "Three starting points, matched to the three routes above."
Three cards in a row, the middle one highlighted (background var(--white), border-color
var(--gs), box-shadow 0 0 0 1px var(--gs) and var(--sm)):
1. "Production readiness" — price "from €—" with <!-- REPLACE from launchstudio.eu/en/ -->
2. "Security audit and fix" — price "from €—" with the same comment
3. "Payment and database setup" — price "€1,500 – €2,500"
Each card lists four short line items.
Below the three cards, one line in 15px var(--ts), max 720px:
"Most agencies in this space do not publish prices. We do, because you should be able
to rule us out in thirty seconds."

S6 GIG COMPARISON — a real comparison table, 3 columns: criterion, "Freelance gig
($25–50)", "LaunchStudio". Use a check SVG in var(--ok) and a cross SVG in var(--tf) —
never colour alone, always keep the row label readable.
H2: "When a 25 dollar gig is enough, and when it is not"
Rows:
  "Fixes a bug you can point at" — yes / yes
  "Finds the problems you do not know about" — no / yes
  "Checks row level security, exposed keys and webhooks" — no / yes
  "Still answerable if it breaks in three months" — no / yes
  "Produces a report you can forward to an investor" — no / yes
Final row, styled differently (background var(--bs)), label "Right choice when":
  "One specific bug you already identified" / "Launching, raising, or an enterprise
  customer started asking questions"
Under the table, 14px var(--tm): "If you have one clear bug and no deadline, a gig is
genuinely the cheaper answer. We are the answer when you do not know what you are
looking for."

S7 ENABLEMENT — its own section with a subtle background change (background var(--white)
with 1px solid var(--bd) top and bottom)
H2: "Or teach your team to do this safely"
Sub: "Some teams do not want to outsource. They want to keep moving fast with AI tools
without shipping the same six gaps every time."
Four short cards: "Tool selection and setup" / "Context engineering and prompt
standards" / "Security guardrails and CI gates" / "A review process that scales"
Secondary button: "Talk about team enablement"
Add an HTML comment above: <!-- Remove this whole section if enablement is not an
actual offering yet -->

S8 PROOF
H2: "What others experience"
Three stat blocks, big numbers with gradient text fill, labels 13px var(--tm). Use "—"
placeholders with <!-- REPLACE with real figures. Prefer client outcomes (funding
raised after launch, revenue processed) over years-in-business -->
Two testimonial cards: quote in var(--fa) italic 18px, name and role 13px var(--tm).
Do NOT invent certification badges, ISO logos or award seals.

S9 LIBRARY — H2: "Everything we have written about this"
Four grouped link lists, each with a group heading in 12px uppercase letter-spacing 1px
color var(--tf) and 4 to 6 placeholder links:
"Getting to production" / "Security" / "Payments and data" / "Tool-specific guides"
Add <!-- REPLACE with real article links from the content library -->

S10 CONTACT FORM — id="contact"
H2: "Tell us where you are stuck."
Form, stacked, max-width 620px:
- Name (text, required)
- Email (email, required)
- "Built with" (select, required): Lovable, Bolt, Replit, Cursor, v0, Other
- "What do you need?" (select, required): "Finish it", "Secure it",
  "Connect payments or database", "Not sure yet"
- "Who are you?" (select, required): "Solo founder", "Founder who codes a little",
  "Agency with a client app", "In-house team"
- "Live URL or repo" (url, optional)
- "Tell us briefly what is going on" (textarea, 4 rows)
- "Budget range" (select, required): "Under €1k", "€1k–5k", "€5k–15k", "€15k+",
  "Not sure yet"
- Four hidden inputs named exactly: click_id, click_type, landing, source
- Submit, primary, full width: "Request free audit"
Inputs: var(--white), 1px solid var(--bd), border-radius var(--rs), padding 13px 16px,
var(--fb) 15px. Focus: border-color var(--gs), box-shadow 0 0 0 3px rgba(47,128,237,.1),
no default outline.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section> elements, <label> bound to every input.
- Responsive, single 768px breakpoint, no horizontal scroll at 360px.
- Accessible: visible focus rings, 4.5:1 minimum contrast, comparison table marked up
  as a real <table> with <th scope>, and yes/no never shown by colour or icon alone —
  include screen-reader text.
- Respect prefers-reduced-motion: disable transforms and transitions.
- Light mode only. No dark mode.
- One HTML file, inline CSS and JS, only the three font links external.
```

---

## 9. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Quyết định kiến trúc pillar/spoke** | Xem §1. Không làm bước này thì 4 trang ăn thịt nhau |
| 2 | 🔴 **Áp 30 negative keyword ở cấp tài khoản** | Xem §2 và §3. Đây là phần quyết định của cụm này |
| 3 | 🔴 **Cập nhật research §4.2** | `vibe coding cleanup specialist` không phải "xác minh mạnh nhất" — xem §2 |
| 4 | Thay giá placeholder bằng giá thật | Lấy từ `launchstudio.eu/en/` |
| 5 | **Quyết định có bán enablement không** | Nếu không, xoá hẳn S7. Đừng quảng cáo dịch vụ chưa có |
| 6 | Link nội bộ 4 chiều | Pillar → 3 spoke, và 3 spoke → pillar |
| 7 | Link 60 bài `extra-1` về pillar | Đây là cách pillar có authority |
| 8 | Nạp 34 kw dùng được vào Keyword Planner | Chưa có volume thật, trừ `bolt ai` 1.300 (research §3.2) |
| 9 | Schema `Service` + `FAQPage` | 4 phản đối ở S4 là `FAQPage` tự nhiên |
| 10 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2② |

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
