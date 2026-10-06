# 🔌 Landing page `/ai-app-integrations` — Content brief + Lovable prompt (v2: Live Wire / Money Flow)

> **Ngày:** 06/10/2026 · **URL đích:** `https://launchstudio.eu/ai-app-integrations` (hiện **404**)
> **Phạm vi:** payment gateways + databases
> **File kèm:** `keyword_ai_app_integrations.csv` (66 kw, 66/66 đã xác nhận qua Autocomplete `gl=nl` + `gl=us`)
> **Liên quan:** `google_ads_plan_payments_nl.md` · `keyword_research_lovable_vibecoding_security.md` §2.3–2.4 · `volume_analysis_results.md`

---

## 1. 🔴 Xung đột với plan đã có — phải giải quyết trước

`google_ads_plan_payments_nl.md` §10 (viết 01/10/2026) đã đề xuất **6 trang NL riêng biệt**, không phải một trang chung:

| Ưu tiên | Trang đã plan | Lý do trong plan |
|---|---|---|
| 1 | `/nl/ideal-integratie` | 18 kw, chứa `stripe ideal` **260 lượt/tháng** |
| 2 | `/nl/betaalprovider-kiezen` | 8/9 kw là P1 |
| 3 | `/nl/wero-webshop` | Cửa sổ first-mover |
| 4–6 | `/nl/paypal-webshop` · `/nl/mollie-integratie` · `/nl/multisafepay-koppelen` | |

Và plan yêu cầu rõ: **"H1 chứa nguyên keyword (`iDEAL integratie`) — khớp headline, nâng Landing page experience"**.

### Vì sao một trang `/ai-app-integrations` chung **không thay thế được** 6 trang đó

Một trang EN tiêu đề "AI App Integrations" sẽ có Landing Page Experience **kém** cho truy vấn `ideal integratie`: H1 không khớp keyword → Ad Rank thấp hơn → CPC cao hơn cho cùng vị trí. Đó là mất tiền có thể đo được, không phải lý thuyết.

### ✅ Cách giải: hub và spoke

| Vai trò | Trang | Nhiệm vụ |
|---|---|---|
| **HUB** | `/ai-app-integrations` (EN) | Trang trụ: tổng quan dịch vụ, GEO, long-tail organic, tài sản bán hàng. **Không phải đích ads chính** |
| **SPOKE** | 6 trang NL trong plan payments | Đích ads, H1 khớp keyword, mỗi trang một PSP |
| **SPOKE** | Cụm Lovable/Supabase (§4) | Đích ads cho truy vấn tiếng Anh theo tool |

Hub trỏ xuống spoke; spoke trỏ ngược lên hub. Đây là kiến trúc dùng được cả plan cũ và trang mới — không phải chọn một.

> 💡 Nếu buộc phải chọn thứ tự: **hub trước**, vì `keyword_research_lovable_vibecoding_security.md` §1.2 đã nêu đúng vấn đề này cho cụm security — không có service page thì internal link và schema `Service` không có chỗ bám. Cụm integrations cũng vậy.

---

## 2. Cầu thật nằm ở đâu

Tôi harvest 43 seed × 2 thị trường (`gl=nl`, `gl=us`) → 474 gợi ý → lọc còn **66 keyword đã xác nhận**.

| Cụm | Kw | Ngôn ngữ | Vai trò |
|---|---:|---|---|
| **A — Lovable Stripe** | 16 | EN | 🥇 ADS + SEO |
| **B — Lovable Database / Supabase** | 25 | EN | 🥇 ADS + SEO |
| **C — Stripe service chung** | 8 | EN | ADS (CPC cao hơn) |
| **D — NL Payments** | 5 | NL | ADS (đã có plan riêng) |
| **E — NL API koppeling** | 6 | NL | ADS (dạng an toàn) |
| **F — API integration chung** | 6 | EN | 🔴 **SKIP** — xem §3 |

### 🔴 Kết luận: cầu nằm ở tên tool + lỗi cụ thể, không nằm ở từ trừu tượng

Đây đúng là điều `keyword_research_lovable_vibecoding_security.md` §1.1 đã kết luận: *"Volume nằm ở tên tool, không nằm ở từ trừu tượng."* Dữ liệu integrations xác nhận lại lần nữa.

**Cụm có người gõ thật (đã validate):**
```
lovable stripe integration        lovable stripe webhook
lovable stripe webhook secret     lovable stripe checkout
lovable stripe api key            lovable stripe connect
does lovable have stripe integration   ← dạng câu hỏi, rất tốt cho GEO
lovable database migration        lovable database export
lovable database backup           lovable supabase migrations
lovable supabase service role key  lovable supabase edge functions
bolt new stripe integration       replit stripe integration
```

> 💡 **`loveable stripe integration` (sai chính tả) cũng đã validate.** Thêm vào ở Exact match — rẻ, và không ai bid.

### Ba keyword là cầu nối sang trang `/ai-app-security`

`lovable stripe webhook secret` · `lovable stripe api key` · `lovable supabase service role key`

Đây là người đang tìm cách cấu hình, nhưng vấn đề thật của họ là **secret key đã bị lộ**. Chính research của bạn (§2.4 #44) ghi nhận: *"có nguồn ghi nhận builder dán nhầm secret key thay vì publishable key"*. Ba từ này nên dẫn sang `/ai-app-security` chứ không dẫn vào form integration — giá trị đơn hàng cao hơn nhiều.

---

## 3. 🔴 Ba cái bẫy — một cái rất nghiêm trọng

### Bẫy 1 — `integratie specialist` trong tiếng Hà Lan nghĩa là chuyên viên **tái hoà nhập lao động**

Autocomplete `gl=nl` cho `integratie specialist` trả về:

```
re integratie specialist           re integratie specialist opleiding
re integratie specialist vacature  re-integratie specialist salaris
werk en re integratie              werk integratie
werkervaringsplek re integratie    werkflow re integratie
opleiding integratie specialist    vacatures integratie specialist
integratieklas                     integratief gedragsmodel
```

**`Re-integratie` là thuật ngữ an sinh xã hội Hà Lan** — chuyên viên giúp người bệnh/thất nghiệp trở lại công việc. Gần như toàn bộ cụm là tuyển dụng, đào tạo và lương trong ngành đó. Không liên quan gì tới software.

Đây cùng loại bẫy với `clutch` (túi xách) và `bubble agency` (hãng PR) đã gặp ở các phân tích trước — nhưng tệ hơn, vì nó ở ngay thị trường mục tiêu.

### Bẫy 2 — `systeemintegratie` ở Hà Lan là từ của ngành năng lượng

```
systeemintegratie energie        systeemintegratie energietransitie
tki systeemintegratie            topsector systeemintegratie
knx systeemintegratie            integratie systeem water
terberg systeemintegratie        systeemintegratie betekenis
```

TKI và Topsector là chương trình nhà nước Hà Lan về chuyển đổi năng lượng. Bid từ này sẽ kéo nhà thầu năng lượng và sinh viên.

**✅ Dạng NL an toàn — bắt buộc dùng thay thế:**
```
api koppeling          api koppeling maken      api koppeling website
api koppelingen        api integraties          database koppelen
```
`koppeling` / `koppelen` (= nối, kết nối) là từ người Hà Lan thật sự dùng cho việc nối hệ thống. Không có nghĩa thứ hai.

### Bẫy 3 — `api integration services` là sân của agency offshore

```
api integration services in india     api integration services in delhi
api integration servicenow            odoo api integration services
rest api integration servicenow       flight api integration services
stripe integration with servicenow    servicenow payment gateway integration
```

Hai nhóm chiếm cụm này: **agency Ấn Độ** (cuộc đua xuống đáy về giá) và **ServiceNow/Odoo** (hệ sinh thái enterprise khác hẳn). Cả 6 keyword cụm F đều để `SKIP` trong CSV.

> ⚠️ Thêm một lưu ý: `stripe integration help` và `stripe integration support` — phần lớn người gõ muốn **support của chính Stripe**, không muốn thuê agency. Cùng loại bẫy với `claude code enterprise pricing` ở phân tích unicoconnect. Để SEO, không bid.

---

## 4. 🥇 Cơ hội lớn nhất: `lovable mollie` + `lovable ideal`

Lấy từ research của chính bạn, §2.4 #46–47:

> *"**Đề xuất mạnh nhất của cụm này:** cặp `lovable mollie` + `lovable ideal`. Không đối thủ quốc tế nào viết (họ không quan tâm thị trường NL), nhưng mọi founder Hà Lan bán hàng đều cần iDEAL. Đây là lợi thế địa phương thuần tuý."*

Lý do nó mạnh, diễn giải thêm:

| | |
|---|---|
| **Lovable không hỗ trợ sẵn Mollie/iDEAL** | Khoảng trống sản phẩm thật, không phải khoảng trống nội dung |
| **iDEAL là phương thức thanh toán số 1 ở Hà Lan** | Mọi founder NL bán hàng đều vướng |
| **Đối thủ quốc tế không quan tâm** | vibeappscanner, rapidevelopers, instinctools không viết về iDEAL |
| **Đối thủ NL không biết Lovable** | Agency Mollie truyền thống không phục vụ người dùng vibe-coding |

➡️ launchstudio nằm đúng chỗ giao nhau của hai thị trường mà không ai khác đứng được. **Đây là nội dung nên viết trước mọi thứ khác trong cụm này.**

> ⚠️ Nhưng kiểm tra lại một việc trước khi làm: **Lovable đã ra "Lovable Payments" built-in** (research §2.4 #43, yêu cầu Pro + Lovable Cloud). Cần xác minh nó hỗ trợ iDEAL/Mollie đến mức nào ở thời điểm này. Nếu Lovable đã hỗ trợ iDEAL native, lập luận ở trên yếu đi đáng kể — và bài cần viết sẽ là `lovable payments vs mollie` thay vì `how to add mollie to lovable`.

---

## 5. ⚠️ Giới hạn dữ liệu — đọc trước khi cấp ngân sách

**66 keyword này đã xác nhận có người gõ, nhưng tôi KHÔNG có volume Keyword Planner cho chúng.**

Autocomplete chứng minh truy vấn tồn tại; nó không đo được bao nhiêu lượt/tháng. `volume_analysis_results.md` §4 chính là bài học về chuyện này: bộ EN trước đây có 68% keyword volume = 0 dù đều "trông hợp lý".

➡️ **Nạp `keyword_ai_app_integrations.csv` vào Keyword Planner trước khi mở campaign.** Số duy nhất tôi có chắc trong vùng này là `stripe ideal` = **260/tháng** (từ `google_ads_plan_payments_nl.md`), và nó thuộc spoke `/nl/ideal-integratie`, không thuộc hub này.

Hub `/ai-app-integrations` nên được xây **cho GEO và bán hàng trước**, và chỉ cấp ngân sách ads sau khi có volume thật.

---

## 6. 🎨 Thương hiệu giữ nguyên, phong cách đổi hoàn toàn

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
}
```

Màu navy, gradient xanh→teal, font Satoshi (Fontshare) / Inter / Instrument Serif, letter-spacing âm ở heading. Logo nhà cung cấp vẫn dùng **SVG đơn sắc**, không dùng logo màu gốc.

### Đổi — concept **"Live Wire / Money Flow"**

Nỗi đau của nhóm khách này **không nhìn thấy được bằng mắt**: checkout báo "Paid" nhưng tiền không về tới app, dữ liệu không có backup. Nên trang **vẽ dòng tiền ra** thành một sơ đồ sống:

| Yếu tố | Thiết kế |
|---|---|
| Hero | **Hai cột ngang nhau 50/50**: pain bên trái, **sơ đồ dòng tiền có animation** bên phải. Đồng xu € chạy dọc dây từ Customer → Checkout → Stripe → Webhook → App → Database. **Webhook bị đứt**, xu rơi xuống ô "Not recorded", bộ đếm tăng dần |
| Ngôn ngữ hình ảnh | **Bản đồ tàu điện / dây dẫn**: dây dày 6px tô gradient, ga tròn bo lớn, nút hình viên thuốc |
| Nền | **Các mảng màu pastel** nhạt từ màu thương hiệu (xanh nhạt `#EAF2FE`, teal nhạt `#E6F7F5`) xen kẽ, kèm **bento card** bo 28px. Không lưới, không nền tối, không kính mờ |
| Cảm giác | Thân thiện, rõ ràng, hơi vui, như một sản phẩm fintech hiện đại. Không kỹ thuật nặng, không báo động |

| | Vibe-coding | Into-production | Security | **Integrations** |
|---|---|---|---|---|
| Hero | Tối, chat AI | Sáng, đếm ngược | Sáng, bố cục giữa, X-ray | **Pastel, 50/50, sơ đồ dòng tiền** |
| Ẩn dụ | Tối → sáng | Phóng tên lửa | Nhìn xuyên thấu | **Dây đứt → dây nối lại** |
| Tương tác chính | Gạt Before/After | Pass/Fail → GO | Thước đo Locked ↔ Glass | **Bấm vào ga trên bản đồ, nối dây đứt** |
| Bề mặt | Card tối | Đường kẻ mảnh editorial | Kính mờ | **Bento pastel, dây gradient dày** |

---

## 7. 📝 Cấu trúc nội dung v2 — Pain ngay trên cùng → Solution → bổ trợ → CTA

**Bỏ theo yêu cầu:** giá (kể cả "From €800" ở trust strip) và form. Mọi CTA trỏ ra trang liên hệ, mang theo tham số.
**Giữ bắt buộc:** dòng `We're not a payment provider` ngay ở hero (lý do ở `google_ads_plan_payments_nl.md` §10: tự lọc người tiêu dùng muốn mở tài khoản iDEAL).

| # | Section | Vai trò | Thông điệp |
|---|---|---|---|
| S1 | **Hero = Pain** (50/50) | 🪝😬 | `Your checkout says "Paid." Your app never heard about it.` + sơ đồ xu rơi ở webhook đứt |
| S2 | **Solution** (50/50 đảo chiều) | ✅ | Cùng sơ đồ, giờ **mọi đồng xu tới nơi**. `We wire it so every payment lands.` + 3 kết quả |
| S3 | **The line map** (tự kiểm) | Bổ trợ tương tác | 8 ga trên 2 tuyến (Payments, Database). Bấm ga → bước tự kiểm 2 phút → đánh dấu → dây nối lại hoặc đứt |
| S4 | **Selling in NL** | Bổ trợ (lợi thế địa phương §4) | iDEAL · Mollie · Bancontact · SEPA + hàng logo đơn sắc |
| S5 | How it works | Bổ trợ | 3 bước |
| S6 | Clear lines | Bổ trợ | "We do / We don't" (không phải PSP, không mở tài khoản PSP thay bạn…) |
| S7 | Related | Hub/spoke | Lộ key → `/ai-app-security` · Chưa launch → `/ai-app-into-production` |
| S8 | Proof | Bổ trợ | Placeholder |
| S9 | **Final CTA** | 🎯 | Dây sáng chạy ngang màn hình, `Let every payment land.` |

### Vì sao hero này đánh đúng nỗi đau

1. **Hai cột ngang nhau, nhìn một lần là hiểu:** chữ nói "tiền không về tới app", hình cho thấy đúng đồng xu đang rơi. Hover vào từng pain bullet bên trái thì điểm tương ứng trên sơ đồ sáng lên.
2. **Bộ đếm "Not recorded: 3… 7… 12" biến lỗi vô hình thành tiền mất đếm được.** Đây là nỗi sợ thật của founder bán hàng.
3. **S2 lặp lại đúng sơ đồ đó nhưng đã được sửa.** Phần Solution không cần giải thích dài, người đọc thấy ngay sự khác biệt.

---

## 8. 🤖 Prompt cho Lovable.dev (v2)

> Paste nguyên khối. Tiếng Anh vì Lovable xử lý tốt hơn.

```
Build a single, self-contained landing page as ONE static `index.html` file: all CSS in
one inline <style> block, all JS in one inline <script> block. No React, no build step,
no router, no external dependencies except the three font links below. It will be
pasted into a WordPress page template, so it must work standalone.

WHAT THIS PAGE IS
LaunchStudio fixes payments and databases in apps built with AI coding tools (Lovable,
Bolt, Replit, Cursor, v0): Stripe, Mollie, iDEAL, PayPal, webhooks, subscriptions,
Supabase/Postgres, backups and migrations. Audience: founders whose app is live or
nearly live, where money or data quietly goes missing. The PAIN is the very first thing
on the page. Story arc: PAIN (hero), SOLUTION, short supporting sections, final CTA.
Visual concept for the whole page: LIVE WIRE / MONEY FLOW — payments and data drawn as
coins travelling along transit-map wires; broken wires drop coins, fixed wires deliver.
There is NO pricing and NO form on this page; every CTA links out.
Tone: clear, friendly, concrete, a little playful. Never alarmist, never mocking.

=== BRAND — KEEP EXACTLY ===
:root{
  --navy:#0B1D35; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --tint-b:#EAF2FE; --tint-t:#E6F7F5; --tint-r:#FDECEC;
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --rp:999px; --rm:16px; --rb:28px;
  --t:.32s; --ease:cubic-bezier(.22,1,.36,1);
}
FONTS — exactly these three. Satoshi is from Fontshare, NOT Google Fonts. Never
substitute:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">

=== STYLE — "LIVE WIRE" (a new style: do NOT use a dark hero, a background grid,
glassmorphism, terminal/monospace aesthetics, or a generic SaaS template) ===
- Light and friendly. Sections alternate soft pastel washes made from brand colours:
  var(--bg), var(--tint-b), var(--tint-t), white. Section edges are gentle 48px-radius
  curves (the next section's background overlaps with rounded top corners).
- BENTO CARDS: white, radius var(--rb), no border, shadow
  0 1px 2px rgba(11,29,53,.04), 0 12px 32px rgba(11,29,53,.06). Hover: lift 4px.
- WIRES: the signature element. 6px thick SVG paths with rounded caps and joins,
  stroked with the brand gradient (define an SVG linearGradient #2F80ED → #14B8A6).
  STATIONS: 22px white circles with a 5px gradient ring. Broken wires: a gap with two
  small frayed ends and a red spark. Coins: 18px circles filled var(--grd) with a white
  "€" in Satoshi 700.
- Typography: h1 var(--fh) 900, clamp(38px,5vw,66px), line-height 1.02, letter-spacing
  -2px · h2 var(--fh) 700, clamp(30px,4vw,50px), line-height 1.06, letter-spacing
  -1.2px · h3 var(--fh) 700, 20px · body var(--fb) 16px/1.7, var(--ts).
- Section labels: small pill chips (var(--white), radius var(--rp), 13px var(--fh) 600,
  a 8px gradient dot before the text), e.g. "● The leak".
- Amounts and counters in var(--fh) 900 with tabular numbers (no monospace font).
- var(--fa) italic for at most 3 emphasis words on the page.
- Red only for broken wires, dropped coins and "broken" states. Green only for
  delivered/working. Gradient for wires, coins, primary buttons, 1–2 key words.
- All visuals in inline SVG/CSS. NO stock photos, NO 3D renders, NO emoji. Icons: inline
  SVG, 1.75px stroke, rounded caps, 22x22.
- Provider logos (Stripe, Mollie, iDEAL, PayPal, Bancontact, Supabase, Postgres): simple
  monochrome inline SVG wordmarks or text wordmarks filled var(--tm), 22px tall, inside
  white pill tiles. Never the original brand colours.
  <!-- REPLACE with self-hosted monochrome SVG logos -->
- Primary button: var(--grd), white, radius var(--rp), padding 16px 30px, var(--fh) 700,
  arrow slides 3px on hover, hover lift 2px + shadow 0 16px 36px rgba(20,184,166,.28).
  Secondary: white, color var(--navy), radius var(--rp), shadow like bento cards.
- Max width 1200px, 24px side padding (16px under 768px). Sections 112px 0 desktop,
  72px 0 mobile.

=== SECTIONS, IN ORDER ===

S1 HERO = PAIN. Background var(--tint-b). TWO EQUAL COLUMNS SIDE BY SIDE (50/50),
vertically centred, 56px gap. Copy left, animated illustration right. On mobile: copy
first, illustration directly below it, full width.
LEFT:
- Pill chip: "● Stripe · Mollie · iDEAL · Supabase"
- H1: 'Your checkout says <em>"Paid."</em> Your app never heard about it.'
  (em = var(--fa) italic, gradient text)
- Sub, 18px, max 500px: "AI coding tools get payments and databases almost right.
  Almost means the webhook never fires, the order never saves, and there's no backup
  when it matters."
- Three pain rows, each a small white pill-card with a red-tinted icon tile
  (var(--tint-r)) and one line. Each row is linked to a point on the diagram
  (data-node). Hover or focus on a row highlights that node with a pulse:
    "Money arrives. The order doesn't."          → node: webhook
    "Test mode is still on in production."       → node: checkout
    "No backup. One bad migration from zero."    → node: database
- Buttons: primary "Find my leaks" (data-cta), secondary "See how it should work"
  (href #fixed).
- Required disclaimer line, 13px var(--tm), with a small info icon:
  "We're a development studio, not a payment provider. We don't open accounts or
  process payments."

RIGHT — THE MONEY FLOW DIAGRAM (animated SVG inside a large white bento card,
aspect ratio about 5:4):
- Stations along a wire that bends like a transit map, each with an icon and a label
  (13px var(--fh) 600): "Customer" → "Checkout" → "Stripe" → "Webhook" → "Your app"
  → "Database". A short branch from "Your app" goes to "Email receipt".
- COINS (€) are emitted from "Customer" every 900ms and travel along the wire
  (use SVG path + getPointAtLength, or CSS offset-path).
- The wire between "Webhook" and "Your app" is BROKEN: a visible gap, frayed ends, a
  small red spark that flickers. Every coin that reaches the gap drops (falls with
  slight rotation, fades to red) into a rounded tray below labelled "Not recorded".
- A live counter on the tray, var(--fh) 900 28px var(--red): "Not recorded: 1, 2, 3…"
  counting each dropped coin, and a small label "€ paid, order missing".
- The "Database" station shows a small amber tag "Last backup: never".
- The "Checkout" station shows a small amber tag "TEST MODE".
- A tiny caption under the card, 12.5px var(--tm): "Illustration of a webhook that
  never reaches your app."
- Under prefers-reduced-motion: no moving coins; show three coins frozen mid-fall
  under the gap and the counter at a static "12".

S2 SOLUTION — id="fixed". Background white. TWO EQUAL COLUMNS, MIRRORED (illustration
LEFT, copy RIGHT) so it visually answers the hero.
LEFT — the SAME diagram, now repaired: the gap is joined by a glowing gradient
segment, coins travel all the way and land in "Database" with a soft green tick burst;
"Checkout" tag reads "LIVE" (green), "Database" tag reads "Backed up daily" (green).
A counter, var(--ok): "Recorded: every payment". The repair animates once when the
section scrolls into view: the gap closes with a quick "zip" along the wire.
RIGHT:
- Pill chip: "● The fix"
- H2: "We wire it so every payment lands."
- Sub: "We keep your app and rebuild only the plumbing — tested end to end, with real
  money, before we hand it back."
- Three outcome rows with green-tinted icon tiles (var(--tint-t)):
    "Payments that reach your app" — "Verified webhooks, retries, failed-payment
     handling, live keys done right."
    "Methods your customers expect" — "Cards, iDEAL, Bancontact, SEPA, PayPal and
     subscriptions."
    "Data you can't lose" — "Row Level Security, daily backups, safe migrations."
- Primary button "Fix my payments" (data-cta).

S3 THE LINE MAP — self-check. Background var(--tint-t). id="map"
- Pill chip: "● Check your lines"
- H2: "Eight places money and data go missing."
- Sub: "Tap a station, run the two-minute check, tell us what you found. Your answers
  stay in your browser."
- A wide bento card containing a transit map with TWO horizontal lines (stacked
  vertically on mobile):
  PAYMENTS LINE (blue end of the gradient), 5 stations:
    1 "Webhooks" · 2 "Live mode" · 3 "Secret keys" · 4 "Failed payments" · 5 "iDEAL"
  DATABASE LINE (teal end), 3 stations:
    6 "Row Level Security" · 7 "Backups" · 8 "Migrations"
  Wire segments between stations start grey and dashed (unknown).
- Clicking a station opens a detail panel below the map (accordion-style, one open at
  a time) with: title, "Try this:" text, and three pill buttons "Works" · "Broken" ·
  "Not sure" (aria-pressed).
  1 "Webhooks" — "Stripe Dashboard → Developers → Webhooks → check failed deliveries.
     Many AI-built apps show 100% failed and nobody noticed."
  2 "Live mode" — "Pay €1 with a real card. If no real money arrives, you're still on
     test keys."
  3 "Secret keys" — "DevTools → Sources → search 'sk_live'. If it's there, anyone can
     issue refunds or read your customers."
  4 "Failed payments" — "Use Stripe's decline test card 4000 0000 0000 0002. Clear
     message, or a frozen screen?"
  5 "iDEAL" — "Selling in the Netherlands? Check your checkout offers iDEAL. Card-only
     checkouts lose Dutch buyers."
  6 "Row Level Security" — "Supabase → Table Editor. Any table without 'RLS enabled' is
     publicly readable."
  7 "Backups" — "Try restoring your database to how it was three days ago. Can you?"
  8 "Migrations" — "Change one column with real users on board. Is there a plan, or do
     you edit production directly?"
- Visual feedback: "Works" turns the station green and the wire segments touching it
  solid gradient; "Broken" turns it red and shows a frayed gap with a spark on the
  segment; "Not sure" turns it amber with a dotted segment.
- A readout bar under the map (white pill): "Solid connections: X / 8" in var(--fh)
  900, plus a short message (aria-live):
    0–1 broken or unsure → "Solid. Worth a look at webhook retries."
    2–4 → "Normal for an AI-built app. All fixable."
    5+  → "Money is very likely slipping through right now."
  and a primary button (data-cta) with a live label:
    no answers → "Get a free check"
    otherwise → "Fix my N broken lines" (N = Broken + Not sure)
  Append integration_score and broken=1,4,7 (station numbers) to its link.
- Note under the readout, 14px: "Found an exposed secret key? That's a security issue
  first →" linking to /ai-app-security.

S4 SELLING IN THE NETHERLANDS — background white
- TWO EQUAL COLUMNS: left copy, right a bento mock of a checkout sheet.
- Pill chip: "● Made for NL"
- H2: "Selling in the Netherlands? Your checkout needs iDEAL."
- Text, max 480px: "AI builders tend to default to a card checkout. Dutch customers
  pay with iDEAL. We add iDEAL, Bancontact and SEPA through Mollie or Stripe, and make
  them work with your subscriptions and webhooks."
  <!-- VERIFY: check current native payment support in Lovable before publishing -->
- Small link "Lees in het Nederlands ↗" (href /nl/ideal-integratie
  <!-- REPLACE when the NL page exists -->).
- RIGHT: a phone-shaped checkout card with a payment-method list: "iDEAL" (selected,
  gradient ring), "Bancontact", "Card", "PayPal". The selection rotates every 2.5s with
  a smooth slide, and the "Pay €49" button gives a small tick animation each time.
  Static under reduced motion.
- Below both columns, a single row of monochrome provider pills: Stripe · Mollie ·
  iDEAL · Bancontact · PayPal · Supabase · Postgres, gently auto-scrolling as a
  marquee (paused on hover, static under reduced motion).

S5 HOW IT WORKS — background var(--tint-b)
- H2: "From leaking to landing in three stops."
- A horizontal wire with three big stations (vertical on mobile); a coin travels from
  stop 1 to stop 3 when the section scrolls into view.
  01 "Free check" — "Send the repo or live URL. We trace every payment and data path."
  02 "Fixed-scope plan" — "What gets fixed, how long it takes, agreed before we start."
  03 "Tested with real money" — "We verify end to end in live mode, then hand it back.
     Your code, your accounts."

S6 CLEAR LINES — background white, two bento cards side by side
  "WE DO" (green chip): Stripe & Mollie integration · Webhooks & retries ·
  Subscriptions · iDEAL, Bancontact, SEPA, PayPal · Supabase RLS, backups, migrations
  "WE DON'T" (grey chip): Open payment-provider accounts for you · Process or hold
  payments · Handle disputes or chargebacks for you · PCI-DSS certification

S7 RELATED — background var(--tint-t), two compact bento link cards with arrows:
  "Keys already exposed?" → "Security audit" (/ai-app-security)
  "Not launched yet?" → "Production readiness" (/ai-app-into-production)

S8 PROOF — background white
- H2: "Founders whose payments now land."
- Three stats in gradient text, var(--fh) 900 52px. "—" placeholders with
  <!-- REPLACE with real figures: payments processed after the fix, apps connected,
  avg. days to fix -->
- Two testimonial bento cards: quote var(--fa) italic 21px, name, role, a chip
  "Lovable + Mollie". Placeholders with <!-- REPLACE with real testimonial -->.
- Do NOT invent certification badges, award seals or client logos.

S9 FINAL CTA — background var(--tint-b) with a large rounded white bento in the
centre.
- Behind the bento, one long gradient wire runs edge to edge across the screen with
  coins flowing continuously and all arriving at a station icon on the right with a
  soft green pulse.
- Inside the bento, centred:
  H2: 'Let every payment <span class=grad>land.</span>'
  Sub: "Free check. We trace your payment and data paths and tell you exactly what's
  leaking."
  Primary button, larger: "Find my leaks" (data-cta)
  Disclaimer, 13px var(--tm): "Development studio, not a payment provider."

FOOTER: one slim row, 13px var(--tm): "© LaunchStudio · launchstudio.eu"

=== JS (vanilla, small) ===
- const CTA_URL = "https://launchstudio.eu/en/#contact"; // REPLACE with the real
  contact or booking URL. Every [data-cta] gets href = CTA_URL + query params.
- Attribution: copy gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content from location.search onto every data-cta link, plus
  landing=ai-app-integrations. S3 adds integration_score and broken.
- Coin animation with requestAnimationFrame along SVG paths; pause all animations when
  their section is off-screen (IntersectionObserver) and when the tab is hidden.
- Hero row ↔ node highlight, S2 repair "zip", S3 stations + readout + live button
  label, S4 checkout rotation and marquee, S5 travelling coin.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section aria-labelledby>, <button> for actions,
  <a> for links. Diagrams are decorative (aria-hidden) with a visually-hidden text
  description of what they show. S3 stations are real buttons with aria-expanded and
  readable labels.
- Two-column sections: CSS grid 1fr 1fr with equal heights and vertical centring on
  desktop; single column under 768px. No horizontal scroll at 360px; the hero diagram
  scales to full width on mobile and stays legible.
- Contrast at least 4.5:1 on all pastel backgrounds. Visible focus rings (2px solid
  var(--ge), 3px offset).
- prefers-reduced-motion: no moving coins, marquee, zips or rotations; show final
  states.
- Status never by colour alone: always a word (Works, Broken, Not sure, TEST MODE,
  LIVE).
- One HTML file, inline CSS and JS, only the three font links external.
```

---

## 9. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Nạp 66 kw vào Keyword Planner** | Xem §5. Chưa có volume thật, đừng cấp ngân sách trước |
| 2 | 🔴 **Xác minh Lovable Payments có hỗ trợ iDEAL/Mollie chưa** | Ảnh hưởng trực tiếp câu chữ ở S4 (prompt đã để comment `VERIFY`). Xem §4 |
| 3 | 🔴 **Thay `CTA_URL`** | Kiểm tra `gclid`, `utm_*`, `integration_score`, `broken` có đi theo sang trang đích |
| 4 | Giữ dòng "not a payment provider" ở hero và CTA cuối | Bắt buộc, để tự lọc người tiêu dùng (`google_ads_plan_payments_nl.md` §10) |
| 5 | Thay logo bằng SVG đơn sắc tự host | Không fetch logo từ CDN ngoài |
| 6 | Kiểm tra animation đồng xu trên mobile 360px | Sơ đồ phải đọc được nhãn ga, không giật, tự dừng khi ra khỏi màn hình |
| 7 | Thay số liệu và testimonial thật ở S8 | Không có thì bỏ khối stat |
| 8 | **Quyết định URL** + hreflang | Đề xuất `/en/ai-app-integrations` |
| 9 | **Giữ 6 trang NL trong plan payments** | Hub này không thay thế chúng (§1). S4 link xuống `/nl/ideal-integratie` |
| 10 | Negative keyword: khối `re-integratie` và `systeemintegratie` | Xem §3 bẫy 1 và 2 |
| 11 | Internal link 3 chiều giữa các landing page | S7 là một nửa; trang security và production cần link ngược lại |
| 12 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2②, giờ ghi nhận ở trang liên hệ |

> 💡 **Lưu ý về giá:** bản này bỏ giá theo yêu cầu. Khuyến nghị bán gói €1.500–2.500 thay vì lẻ €800 (`google_ads_plan_payments_nl.md` §11) vẫn đúng, nhưng giờ áp dụng ở bước báo giá sau buổi kiểm tra miễn phí, không nằm trên trang.

---

## 10. Thứ tự ưu tiên giữa ba landing page

| | Trang | Lý do |
|---|---|---|
| 🥇 | `/ai-app-security` | Research gọi là nút cổ chai · ~70/tháng · 4 đối thủ xác minh · có CVE + sự cố 4/2026 |
| 🥈 | **`/ai-app-integrations`** | 66 kw validate · là nơi duy nhất có lợi thế địa phương thật (`lovable mollie`/`lovable ideal`) · **nhưng chưa có volume KP** |
| 🥉 | `/ai-app-into-production` | Trùng thông điệp trang chủ · ~10/tháng · giá trị chủ yếu là GEO |

> 💡 Trang integrations có **cơ hội độc nhất** mà hai trang kia không có: giao điểm Lovable × thị trường thanh toán Hà Lan. Không đối thủ quốc tế nào phục vụ, và không agency Mollie truyền thống nào biết Lovable. Nếu volume KP xác nhận, đây là trang nên ưu tiên cao nhất.

---

## 11. File

| File | Nội dung |
|---|---|
| `keyword_ai_app_integrations.csv` | 66 kw × 10 cột: cluster, match, intent, ngôn ngữ, vai trò (ADS/SEO/SKIP), priority, ghi chú, geo autocomplete |
| `landing_ai_app_integrations_brief.md` | Tài liệu này |
