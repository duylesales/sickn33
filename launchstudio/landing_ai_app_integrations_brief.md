# 🔌 Landing page `/ai-app-integrations` — Content brief + Lovable prompt

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

## 6. 🎨 Design system — token chính xác từ theme

Giống hai trang trước. Đã đối chiếu 0 sai lệch với `style.css` live.

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
| Card | padding 24px, `1px solid var(--bd)`, radius `--rl` (20px), shadow `--ss` |
| Button hover | `translateY(-2px)` + `0 14px 34px rgba(47,128,237,.22),0 6px 14px rgba(11,29,53,.1)` |

**Riêng trang này:** cần **logo nhà cung cấp** (Stripe, Mollie, iDEAL, PayPal, Supabase…). Dùng SVG đơn sắc đổ `currentColor` màu `--tm`, cao 24px, đặt trong khung `--bs` — **không dùng logo màu gốc**, vì một hàng logo nhiều màu sẽ phá vỡ ngay bảng màu lạnh của theme.

---

## 7. 📝 Cấu trúc nội dung — 9 section

### S1 — Hero
- **Eyebrow:** `STRIPE · MOLLIE · iDEAL · PAYPAL · SUPABASE · POSTGRES`
- **H1:** `Your app works. Taking money and storing data is where it breaks.`
- **Sub:** `Payments and databases are the two integrations AI coding tools get almost right. Almost is the problem: the checkout works in test mode, the webhook never fires, and the database has no backup.`
- **CTA chính:** `Tell us what's broken`
- **CTA phụ:** `See the 8 things that break ↓`
- **Trust strip:** `Fixed scope · From €800 · We're not a payment provider`

> 🔴 **Dòng "We're not a payment provider" là bắt buộc**, lấy nguyên tinh thần từ `google_ads_plan_payments_nl.md` §10: *"Dù negative list có tốt đến đâu, vẫn sẽ có người tiêu dùng và người muốn mở tài khoản iDEAL lọt vào. Một dòng ở đầu trang khiến họ tự rời đi trước khi gửi form."*

### S2 — Hai mảng, hai nỗi đau (2 card lớn)

**Card A — Payments:** test mode sang live, webhook không fire, subscription/abonnementen, refund & dispute, iDEAL/SEPA/Bancontact cho thị trường NL, secret key bị lộ.

**Card B — Databases:** RLS chưa bật, không có backup, migration sau khi đã có user thật, export/khoá nhà cung cấp, connection pooling, dữ liệu không lưu được.

### S3 — ⭐ Tám lỗi phổ biến + cách tự kiểm (trọng tâm)

Giống cấu trúc hai trang trước. Mỗi card có cách tự kiểm làm được trong 2 phút.

| # | Lỗi | Mảng | Cách tự kiểm |
|---|---|---|---|
| 1 | **Webhook không fire** | Pay | Stripe Dashboard → Webhooks → xem failed deliveries. Phần lớn thấy 100% fail mà không biết. |
| 2 | **Vẫn ở test mode** | Pay | Thử trả bằng thẻ thật €1. Không về được tiền thật là vẫn test key. |
| 3 | **Secret key ở frontend** | Pay | DevTools → Sources → tìm `sk_live`. Thấy là bất kỳ ai cũng rút tiền được. |
| 4 | **Không xử lý payment failed** | Pay | Dùng thẻ test `4000 0000 0000 0002` (decline). App báo rõ hay treo? |
| 5 | **Không có iDEAL** (thị trường NL) | Pay | iDEAL chiếm phần lớn thanh toán online ở Hà Lan. Chỉ có card = mất khách NL. |
| 6 | **RLS chưa bật** | DB | Supabase → Table Editor. Bảng nào thiếu badge "RLS enabled" là đọc được công khai. |
| 7 | **Không có backup** | DB | Khôi phục DB về trạng thái 3 ngày trước. Làm được không? |
| 8 | **Chưa từng chạy migration** | DB | Đổi một cột khi đã có user thật. Có kế hoạch hay chỉ sửa trực tiếp production? |

### S4 — Widget tự chấm (8 câu → `integration_score`)

| Số lỗi | Kết quả | Màu |
|---:|---|---|
| 0–1 | `Solid. Worth checking webhook retries.` | `--ok` |
| 2–4 | `Normal for an AI-built app. All fixable.` | `--amb` |
| 5+ | `You are likely losing payments right now.` | `--red` |

### S5 — Phủ sóng nhà cung cấp

Grid logo đơn sắc + một dòng mỗi nhà cung cấp. **Nhấn Mollie/iDEAL/Bancontact** — đây là thứ đối thủ quốc tế không có.

### S6 — ⭐ `Lovable + Mollie / iDEAL` (section riêng)

Cơ hội ở §4. Nội dung: Lovable không hỗ trợ sẵn PSP Hà Lan; đây là cách nối; đây là thứ cần nếu bán ở Hà Lan.

> ⚠️ Xác minh trạng thái "Lovable Payments" trước khi viết — xem cảnh báo ở §4.

### S7 — Giá & phạm vi

Theo đúng khuyến nghị `google_ads_plan_payments_nl.md` §11: **đừng bán lẻ "tích hợp iDEAL €800"**, bán gói hoàn chỉnh **€1.500–2.500** (iDEAL + PayPal + SEPA + Bancontact + webhook + abonnementen + kiểm thử).

Lý do trong plan: *"Cùng một lead, cùng CAC, biên lợi nhuận gấp đôi. Và khách muốn iDEAL gần như luôn cũng muốn các phương thức khác — bán lẻ từng cái là tự hạ giá mình."*

Thêm bảng **What we don't do**: không mở tài khoản PSP thay bạn, không phải payment provider, không xử lý tranh chấp/chargeback thay bạn, không làm PCI-DSS certification.

### S8 — Liên kết sang hai trang kia (hub/spoke)

Ba thẻ dẫn sang: `/ai-app-security` (nếu secret key đã lộ) · `/ai-app-into-production` (nếu chưa launch) · các trang NL PSP (nếu bán ở Hà Lan).

### S9 — Form

| Trường | Ghi chú |
|---|---|
| Name, Email | bắt buộc |
| **Built with** | Lovable / Bolt / Replit / Cursor / v0 / Custom code / Other |
| **What do you need?** | multi: Payments / Database / Both |
| **Payment provider** | Stripe / Mollie / PayPal / MultiSafepay / Adyen / Not chosen yet / Other |
| **Selling in the Netherlands?** | Yes / No — ⭐ phân luồng sang spoke NL |
| **Database** | Supabase / Firebase / Postgres / MySQL / Not sure |
| **Live URL or repo** | optional |
| What's broken? | textarea |
| 🔒 hidden | `click_id`, `click_type`, `landing`, `source`, `integration_score` |

---

## 8. 🤖 Prompt cho Lovable.dev

```
Build a single, self-contained landing page as ONE static `index.html` file, with all CSS
in one inline <style> block and all JS in one inline <script> block. No React, no build
step, no router, no external dependencies except the three font links below. This file
will be pasted into a WordPress page template, so it must work standalone.

Subject: a service page for fixing payment gateway and database integrations in apps
built with AI coding tools (Lovable, Bolt, Replit, Cursor, v0). Audience: a founder who
shipped something that works, but whose checkout or database is quietly broken. Tone:
practical, specific, calm. No hype, no fear-mongering.

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
- monospace: ui-monospace, 'SF Mono', Menlo, monospace, 13px

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

PROVIDER LOGOS — IMPORTANT:
Render provider names (Stripe, Mollie, iDEAL, PayPal, MultiSafepay, Adyen, Supabase,
Postgres, Firebase) as simple MONOCHROME inline SVG wordmarks or plain text in var(--fh)
weight 600, filled with currentColor set to var(--tm), max-height 24px, each inside a
tile with background var(--bs) and border-radius var(--rs). Do NOT use full-colour brand
logos and do NOT fetch logos from external URLs — a multi-coloured logo row would break
the cool palette of this site.

VISUAL CHARACTER — critical to match the existing site:
- Light, airy, clinical. Page background #F8FAFE, never pure white, NEVER dark mode.
- Shadows always soft and multi-layered. Never one heavy shadow.
- Headings use tight NEGATIVE letter-spacing — the brand signature.
- Blue-teal gradient is an ACCENT only: primary buttons, big stat numbers, small badges.
  NEVER a full-width section background, never behind body text.
- Red only in small status pills and single result lines. No red section backgrounds.
- Instrument Serif italic very sparingly — one or two emphasis phrases maximum.
- No stock photos, no credit-card or coin illustrations, no emoji in the UI. Simple
  inline SVG icons only, 1.5px stroke, currentColor, 20x20.

=== PAGE CONTENT — 9 SECTIONS IN THIS ORDER ===

S1 HERO (left-aligned, max 780px, not centered)
- Eyebrow, uppercase 12px letter-spacing 1.2px color var(--gs):
  "STRIPE · MOLLIE · iDEAL · PAYPAL · SUPABASE · POSTGRES"
- H1: "Your app works. Taking money and storing data is where it breaks."
- Sub (18px var(--ts), max 640px): "Payments and databases are the two integrations AI
  coding tools get almost right. Almost is the problem: the checkout works in test mode,
  the webhook never fires, and the database has no backup."
- Primary button "Tell us what's broken" (anchor #contact),
  secondary "See the 8 things that break" (anchor #breaks)
- Thin row below, 13px var(--tm), middot separated: "Fixed scope" · "From €800" ·
  "We are not a payment provider"
  (That last item matters — keep it in the hero, it filters out consumers looking for
  payment support.)

S2 TWO AREAS — two large cards side by side (stack under 768px)
Card A, h3 "Payments": a list with small SVG icons —
  Test mode to live · Webhooks that never fire · Subscriptions and recurring billing ·
  Refunds and disputes · iDEAL, SEPA and Bancontact for the Dutch market ·
  Secret keys that ended up in the frontend
Card B, h3 "Databases": —
  Row level security that was never switched on · No backups · Migrations after you
  already have real users · Export and vendor lock-in · Connection pooling under load ·
  Data that silently does not save

S3 THE EIGHT THINGS THAT BREAK — id="breaks". The most important section.
H2: "The eight things we find broken most often"
Sub: "Each one has a check you can run yourself in two minutes, without us."
Eight cards in a 2-column grid (1 column mobile). Each card: a small pill top-right
reading either "PAYMENTS" or "DATABASE" (background var(--bs), color var(--tm), 11px
uppercase letter-spacing .8px, border-radius var(--rp)), a number in var(--fh) 800 26px
with gradient text fill, an h3, one short paragraph on why AI tools get this wrong, and
a "RUN THIS CHECK" block (background var(--bs), border-radius var(--rs), padding 14px,
monospace 13px, label 11px uppercase letter-spacing 1px color var(--tf)).

1. PAYMENTS — "The webhook never fires"
   Why: "The checkout redirect works, so it looks finished. The webhook is what actually
   tells your app the money arrived, and nothing complains when it is missing."
   Check: "Stripe Dashboard → Developers → Webhooks → look at failed deliveries. Many
   founders find 100% failure here and had no idea."

2. PAYMENTS — "Still running in test mode"
   Why: "Test keys and live keys look nearly identical, and test mode is what you built
   against for weeks."
   Check: "Pay €1 with a real card. If the money never lands in your account, you are
   still on test keys."

3. PAYMENTS — "Secret key in the frontend"
   Why: "The call that needed the secret key was written in frontend code, because that
   is where the button was."
   Check: "DevTools → Sources → search for 'sk_live'. If it appears, anyone can move
   money out of your account."

4. PAYMENTS — "Failed payments are not handled"
   Why: "Prompts describe a successful purchase. Declines, expired cards and 3D Secure
   challenges are a different code path nobody asked for."
   Check: "Pay with the Stripe test card 4000 0000 0000 0002, which always declines.
   Does your app explain what happened, or just stop?"

5. PAYMENTS — "No iDEAL, and you are selling in the Netherlands"
   Why: "AI tools default to card payments because that is what the global examples use.
   iDEAL is the dominant online payment method in the Netherlands."
   Check: "Open your own checkout as a Dutch customer. Is iDEAL there? If not, you are
   asking Dutch buyers to use their least preferred option."

6. DATABASE — "Row level security was never enabled"
   Why: "Supabase creates every new table with row level security switched off. The app
   works fine without it, so nothing ever tells you."
   Check: "Supabase → Table Editor. Any table without an 'RLS enabled' badge is readable
   by anyone holding your public key."

7. DATABASE — "There are no backups"
   Why: "Backups are a setting, not a feature, so they are never part of the prompt."
   Check: "Try to restore your database to how it looked three days ago. Can you?"

8. DATABASE — "No migration has ever been run"
   Why: "While building, changing a column is harmless. Once real users have real rows,
   the same change can lose data."
   Check: "Rename a column that is in use. Is there a migration process, or would you
   edit production directly?"

S4 SELF-CHECK WIDGET — vanilla JS
H2: "Check your own integrations"
Sub: "Eight questions. Two minutes. No email required."
Eight rows matching the eight items above, each a short question with Yes / No /
Not sure pill buttons (selected state uses var(--grd)). Count issues found; count every
"Not sure" as an issue and state that in a 12.5px note.
Large result "X of 8" with gradient text fill, in an aria-live region:
- 0-1 → var(--ok): "Solid. Still worth checking webhook retries."
- 2-4 → var(--amb): "Normal for an AI-built app. All of these are fixable."
- 5+  → var(--red): "You are very likely losing payments right now."
Then a primary button "Get these fixed" that scrolls to #contact and writes the count
into the hidden input named "integration_score".

S5 PROVIDERS WE CONNECT
H2: "What we connect"
Two labelled groups of monochrome provider tiles as described above:
"Payments" — Stripe, Mollie, iDEAL, PayPal, MultiSafepay, Adyen, SEPA, Bancontact
"Data" — Supabase, Postgres, Firebase, MySQL, Neon
Under the payments group, one line in 14px var(--ts): "Mollie, iDEAL and Bancontact
matter if you sell in the Netherlands or Belgium. Most international agencies do not
set these up."

S6 LOVABLE + DUTCH PAYMENT PROVIDERS — give this its own section with a subtle
background change (background var(--white) with 1px solid var(--bd) top and bottom)
H2: "Lovable, Mollie and iDEAL"
Three short cards: "Why it is not built in" / "How we connect it" / "What you get".
Keep copy to two sentences per card and leave an HTML comment above the section:
<!-- VERIFY current Lovable Payments iDEAL/Mollie support before publishing this -->
Primary button: "Add iDEAL to my Lovable app"

S7 PRICING AND SCOPE
H2: "What it costs"
Present ONE bundled package, not a per-provider price list: a single highlighted card
(background var(--white), border-color var(--gs), box-shadow 0 0 0 1px var(--gs) and
var(--sm)) titled "Complete payment setup", price "€1,500 – €2,500", and a list:
iDEAL + PayPal + SEPA + Bancontact · webhook handling and retries · subscriptions ·
refund and dispute flow · test coverage on the payment path · live-mode verification.
Next to it a smaller plain card "Database work" with "From €800" and a short list.
Then a two-column block "What we do" / "What we don't do". The second column must
include: "Open a payment provider account for you" · "Act as your payment provider" ·
"Handle your chargebacks and disputes" · "PCI-DSS certification".

S8 RELATED — three small link cards, each with a one-line reason:
"App not launched yet?" → /ai-app-into-production
"Think a key has leaked?" → /ai-app-security
"Selling in the Netherlands?" → /nl/ideal-integratie

S9 CONTACT FORM — id="contact"
H2: "Tell us what's broken."
Form, stacked, max-width 620px:
- Name (text, required)
- Email (email, required)
- "Built with" (select, required): Lovable, Bolt, Replit, Cursor, v0, Custom code, Other
- "What do you need?" (checkbox group): Payments, Database, Both
- "Payment provider" (select): Stripe, Mollie, PayPal, MultiSafepay, Adyen,
  Not chosen yet, Other
- "Selling in the Netherlands?" (select, required): Yes, No
- "Database" (select): Supabase, Firebase, Postgres, MySQL, Not sure
- "Live URL or repo" (url, optional)
- "What's broken?" (textarea, 4 rows)
- Five hidden inputs named exactly: click_id, click_type, landing, source,
  integration_score
- Submit, primary, full width: "Send it over"
Inputs: var(--white), 1px solid var(--bd), border-radius var(--rs), padding 13px 16px,
var(--fb) 15px. Focus: border-color var(--gs), box-shadow 0 0 0 3px rgba(47,128,237,.1),
no default outline.
Add a 12.5px var(--tf) line under submit: "We never ask for your live API keys by email."

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section> elements, <label> bound to every input.
- Responsive, single 768px breakpoint, no horizontal scroll at 360px.
- Accessible: visible focus rings, aria-live on the widget result, 4.5:1 minimum
  contrast, and status never communicated by colour alone — always include a text label.
- Respect prefers-reduced-motion: disable transforms and transitions.
- Light mode only. No dark mode.
- One HTML file, inline CSS and JS, only the three font links external.
```

---

## 9. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Nạp 66 kw vào Keyword Planner** | Xem §5. Chưa có volume thật — đừng cấp ngân sách trước |
| 2 | 🔴 **Xác minh trạng thái Lovable Payments với iDEAL/Mollie** | Quyết định S6 viết thế nào. Xem §4 |
| 3 | Thay logo bằng SVG đơn sắc tự host | Đừng fetch logo từ CDN ngoài — vừa chậm vừa rủi ro thương hiệu |
| 4 | Thay giá placeholder bằng giá thật | €1.500–2.500 là đề xuất từ plan payments §11, cần bạn chốt |
| 5 | **Quyết định URL** + hreflang | Cùng vấn đề namespace: đề xuất `/en/ai-app-integrations` |
| 6 | **Giữ 6 trang NL trong plan payments** | Hub này **không** thay thế chúng. Xem §1 |
| 7 | Negative keyword: thêm khối `re-integratie` và `systeemintegratie` | Xem §3 bẫy 1 và 2 |
| 8 | Internal link 3 chiều giữa 3 landing page | S8 là một nửa; hai trang kia cần link ngược lại |
| 9 | Schema `Service` + `FAQPage` + `HowTo` | 8 bước tự kiểm là `HowTo` tự nhiên |
| 10 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2② |

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
