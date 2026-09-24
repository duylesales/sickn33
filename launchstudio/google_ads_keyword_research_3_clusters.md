# 📊 Google Search Ads — Nghiên Cứu Từ Khoá 3 Cụm (Pre-Launch Analysis)

> **Mục đích:** nghiên cứu trước khi chạy Google Search Ads cho 3 nhóm — ① Lovable issues · ② Vibe coding assistance · ③ Security & cleanup
> **Ngày:** 2026-09-24 · **Thị trường:** NL (chính) + EU-EN (phụ)
> **File kèm:** [`keyword_seeds_google_ads_3_clusters.csv`](keyword_seeds_google_ads_3_clusters.csv) — 129 keyword, đã chia ad group, sẵn sàng paste vào Keyword Planner
> **Liên quan:** [`google_ads_keywords_launchstudio.md`](google_ads_keywords_launchstudio.md) · [`paid_ads_plan.md`](paid_ads_plan.md) · [`keyword_research_lovable_vibecoding_security.md`](keyword_research_lovable_vibecoding_security.md)

---

## ⚠️ 0. Trạng thái dữ liệu volume — đọc trước

**Mình không lấy được volume chính xác cho 129 keyword này.** Việc đó bắt buộc phải qua Google Keyword Planner (cần tài khoản Ads đang hoạt động), Ahrefs hoặc Semrush. Mình đã kiểm tra repo: **không có credential hay script nào** truy cập các API đó (`sys/` chỉ có script generate content + sync social).

**Tin tốt:** bạn *đã có* tài khoản Google Ads (theo `google_ads_keywords_launchstudio.md` — 4 campaign, ngân sách €1.500–3.000/tháng). Nghĩa là bạn tự lấy được volume chính xác + CPC dự báo **trong ~20 phút**. File CSV kèm theo được format đúng để làm việc đó — xem §7.

**Cái mình làm được và đã làm:**

| Việc | Kết quả |
|---|---|
| Trích dữ liệu GKP thật đã có trong repo | 8 keyword có volume thật (§1.1) |
| Tìm volume đã công bố công khai | 7 keyword có số từ nguồn bên thứ ba (§1.2) |
| Xác minh nhu cầu bằng bằng chứng cạnh tranh | 129 keyword, gắn tier A/B/C |
| Phát hiện bẫy volume | 3 bẫy nghiêm trọng (§2) — **phần này quan trọng nhất** |
| Dựng cấu trúc campaign + negative list | §4, §5 |

Trong CSV, cột `volume_signal` ghi rõ: số thật thì ghi số + nguồn + ngày; chưa có số thì ghi `Unverified-A/B/C` theo mức độ bằng chứng.

---

## 📈 1. Volume đã xác minh được

### 1.1. Từ Google Keyword Planner (dữ liệu thật, có sẵn trong repo)

Nguồn: [`keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv`](keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv), export 2026-06-15.

| Keyword | Volume/tháng | Competition | Bid Low | Bid High | Liên quan cụm |
|---|---:|---|---:|---:|---|
| `ai coding` | 1.600 | Medium | $2,00 | $7,98 | ② |
| **`bolt ai`** | **1.300** | Medium | $1,78 | $8,05 | ② |
| `ai secure` | 140 | Medium | — | — | ③ |
| `ai database` | 110 | Low | — | — | ① |
| `ai deployment` | 10 | Medium | — | — | ① |
| `ai prototype` | 20 | Medium | — | — | ② |
| `ai security vulnerabilities` | 10 | Medium | — | — | ③ |
| `ai vulnerabilities` | 10 | High | — | — | ③ |

⚠️ **Lưu ý về file CSV này:** nó được seed bằng **URL** (`launchstudio.eu/en/`) chứ không phải bằng keyword. Kết quả là nhiều rác. `paid_ads_plan.md` đã phân tích: tổng "214.280/tháng" ở header thì **94% đến từ một term duy nhất là `day ai` (201.000)** — gần như chắc chắn là nhóm truy vấn broad-match lệch hoàn toàn. Volume dùng được sau khi làm sạch: **~12.700–13.000/tháng**, không phải 214.280.

### 1.2. Từ nguồn công khai bên thứ ba

| Keyword | Volume/tháng | Tăng trưởng | Nguồn | Geo |
|---|---:|---|---|---|
| `vibe coding` | **95.000** | **+599% / 12 tháng** | SaasCrisp trends (cập nhật 07/2026) | Không ghi rõ — nhiều khả năng global |
| `lovable` | 149.500 | — | Semrush | Global |
| `lovable ai` | 122.200 | — | Semrush | Global |
| `loveable` (sai chính tả) | 118.100 | — | Semrush | Global |
| `ai agents` | 164.000 | +584% | SaasCrisp | Global |
| `ai website builder` | 78.000 | +611% | SaasCrisp | Global |
| `ai landing page generator` | 8.000 | +575% | SaasCrisp | Global |

Một nguồn khác ghi nhận cụm truy vấn `vibe coding` tăng từ **dưới 1.000/tháng (03/2024) lên trên 60.000/tháng (03/2026)** — khoảng 60× trong 18 tháng.

⚠️ **Ba con số `lovable*` ở trên gần như vô dụng cho ads.** Xem §2.1 ngay dưới.

### 1.3. CPC benchmark ngành (để ước tính ngân sách)

| Chỉ số | Giá trị | Nguồn |
|---|---:|---|
| B2B SaaS — CPC trung bình 2026 | **$8,86** (+29% YoY, +57% so với TB 8 năm) | ROA Marketing |
| B2B SaaS — CPC median non-brand | **$8,50–14,00** | Two Spouts |
| Technology/SaaS — CPC trung bình liên ngành | $3,80 | Digital Applied |
| B2B nói chung | $3,33 | WebFX |

➡️ Kế hoạch cũ đặt CPC cap €8–10. Benchmark 2026 cho thấy mức đó **sát trần dưới** của B2B SaaS non-brand. Với keyword `Service`/`Hire` intent, nên chuẩn bị tinh thần CPC €8–14.

---

## 🚨 2. Ba cái bẫy volume phải xử lý TRƯỚC khi bid

Đây là phần quan trọng nhất của tài liệu này. Bỏ qua §2 thì §1 sẽ dẫn bạn tới quyết định sai.

### 2.1. 🔴 Bẫy số 1: `lovable` là từ điển + là thương hiệu đồ lót

`lovable` = tính từ tiếng Anh thông dụng (*đáng yêu*). Đồng thời **Lovable là thương hiệu đồ lót/nội y toàn cầu**. Con số 149.500/tháng là hỗn hợp của:

- người tra nghĩa từ (`lovable meaning`, `lovable synonym`)
- người mua đồ lót
- lời bài hát, tên phim, tên thú cưng
- và **một phần nhỏ** là founder tìm công cụ Lovable

➡️ **Tuyệt đối không bid broad match trên `lovable`.** Đây chính xác là lặp lại sai lầm `day ai` = 201.000. Bắt buộc:
- Chỉ dùng **Phrase/Exact** với từ định tính: `lovable app`, `lovable ai`, `lovable dev`, `lovable supabase`…
- Áp negative list §5.1 ngay từ ngày 1.

### 2.2. 🟠 Bẫy số 2: `vibe coding` 95.000/tháng là volume global, intent nghiên cứu

Con số 95K nghe hấp dẫn, nhưng:

- **Geo:** nguồn không ghi rõ — gần như chắc là global, không phải NL. Volume NL có thể chỉ là vài phần nghìn của con số đó.
- **Intent:** nguồn phân tích trend ghi nhận truy vấn `how to` áp đảo `what is` — tức người tìm muốn **tự làm**, không phải muốn **thuê người làm**.
- **Hệ quả cho ads:** bid head term `vibe coding` sẽ đốt tiền vào sinh viên, người tò mò, và dev đang học. Tỉ lệ chuyển đổi sang gói €800–7.500 gần như bằng 0.

➡️ Trong CSV mình để `vibe coding` ở **P3** đúng vì lý do này, dù nó có volume cao nhất cụm ②.

### 2.3. 🟡 Bẫy số 3 — quan trọng nhất cho ads: intent "Fix" ≠ intent "Hire"

Phân bố intent của 129 keyword:

| Intent | Số keyword | Phù hợp SEO? | Phù hợp Paid Search? |
|---|---:|---|---|
| **Fix** (sửa lỗi) | 30 | ✅ Rất tốt | ⚠️ **Kém** |
| **Hire** (thuê người) | 26 | ✅ Tốt | ✅ **Rất tốt** |
| **Service** (mua dịch vụ) | 24 | ✅ Tốt | ✅ **Rất tốt** |
| Research | 17 | ✅ Tốt | ❌ Đốt tiền |
| How-to | 10 | ✅ Tốt | ❌ Đốt tiền |
| Decision | 7 | ✅ Tốt | ✅ Tốt |
| Security | 6 | ✅ Tốt | 🟡 Test |
| Compare | 4 | ✅ Tốt | 🟡 Test |
| Compliance | 3 | ✅ Tốt | ✅ Tốt |
| Cost | 2 | ✅ Tốt | 🟡 Test |

**Vấn đề:** người gõ `lovable custom domain not working` đang bực mình và muốn **cách sửa miễn phí trong 5 phút**. Họ không ở trạng thái mua gói €800–7.500. Click đó tốn €8–14 và gần như chắc chắn bounce.

Ngược lại, người gõ `vibe coding cleanup specialist` hoặc `code audit laten uitvoeren` **đang đi tìm nhà cung cấp**. Đó là click đáng €14.

➡️ **Khuyến nghị rõ ràng:**
- **Paid Search chỉ chạy nhóm `Hire` + `Service` + `Decision` + `Compliance`** = 60/129 keyword.
- **Nhóm `Fix` (30 keyword) để cho SEO**, không bid. Đây chính là nội dung mà [`keyword_research_lovable_vibecoding_security.md`](keyword_research_lovable_vibecoding_security.md) đã đề xuất viết bài.
- Nếu muốn test nhóm `Fix`, chỉ test **tối đa 5 keyword, exact match, ngân sách riêng €5/ngày**, và đo bằng cost-per-qualified-lead chứ không phải CTR.

---

## 🎯 3. Kỳ vọng volume thực tế cho account này

Trước khi bạn chạy Keyword Planner và có thể thất vọng, đây là con số tham chiếu từ chính repo:

- `seo_geo_plan_production_keywords.md` ước tính 14 production keyword ở **NL** có tổng **200–600 lượt tìm/tháng** → CTR 6–9% → **15–50 click/tháng**.
- `paid_ads_plan.md` sau khi làm sạch CSV: **~13.000/tháng** cho toàn bộ tập keyword EN (global-ish), không phải 214.280.

➡️ **Đây là account low-volume, high-intent.** Với 3 cụm mới này, dự đoán hợp lý:

| Cụm | Ước tính volume NL/tháng | Ước tính volume EU-EN/tháng |
|---|---|---|
| ① Lovable issues (chỉ nhóm Hire) | 20–80 | 300–900 |
| ② Vibe coding (chỉ nhóm Hire) | 10–50 | 200–700 |
| ③ Security & cleanup | 30–120 | 400–1.200 |

*(Đây là ước tính có căn cứ, không phải số đo. Verify ở §7.)*

**Cách đánh giá account này:** cost per qualified lead. **Không bao giờ** đánh giá bằng impression hay click volume — với niche B2B thế này, con số đó sẽ luôn trông tệ.

---

## 🏗️ 4. Cấu trúc campaign đề xuất

File CSV đã chia sẵn 19 ad group. Gợi ý gom thành 4 campaign:

| Campaign | Ad group | Ngôn ngữ / Geo | Ngân sách gợi ý | Ghi chú |
|---|---|---|---:|---|
| **C1 — NL Service** | AG-NL-Rescue, AG-NL-Security, AG-NL-Vibe | 🇳🇱 NL + Flanders | €600/tháng | Intent mua cao nhất, cạnh tranh thấp nhất |
| **C2 — EU-EN Hire** | AG-LOV-Hire, AG-VIBE-Hire, AG-VIBE-Bolt (chỉ kw Hire), AG-VIBE-Replit (chỉ kw Hire) | 🇬🇧 EU-EN | €700/tháng | Cạnh tranh trực tiếp với Fiverr/Upwork — xem §4.1 |
| **C3 — EU-EN Security** | AG-SEC-Cleanup, AG-SEC-Audit, AG-SEC-Tool, AG-SEC-Compliance | 🇬🇧 EU-EN | €700/tháng | Giá trị đơn hàng cao nhất |
| **C4 — Test Fix** (tuỳ chọn) | AG-LOV-Stripe, AG-LOV-Export, AG-LOV-Deploy | 🇬🇧 EU-EN | €150/tháng | Exact match only, cắt sau 4 tuần nếu CPL > €400 |

### 4.1. ⚠️ Cảnh báo cạnh tranh cho C2

SERP và marketplace cho `fix lovable app`, `fix bolt app`, `lovable developer for hire` đang bị **Fiverr/Upwork chiếm** với gig **$10–30**. LaunchStudio bán €800–7.500.

➡️ Ad copy cho C2 **không được đấu giá**. Phải đấu bằng:
- "Gig $25 không vá được lỗ hổng RLS" (neo vào CVE-2025-48757 — ~10,3% app Lovable công khai bị lộ dữ liệu theo nghiên cứu được Superblocks dẫn lại)
- Entity Manifera: 11 năm, 160+ dự án, khách hàng Vodafone / TNO / CFLW
- Fixed price, 100% code ownership, live 1–3 tuần

Nếu ad copy chỉ nói "we fix your Lovable app" thì bạn đang mời người dùng so sánh giá với gig $25 — và bạn thua.

### 4.2. 🔴 Điều kiện tiên quyết: chưa có landing page cho C3

Mình đã kiểm tra `launchstudio.eu/en/` hôm 23/09: site vẫn là **one-page + anchor** (`#process`, `#calculator`, `#packages`, `#proof`, `#contact`) + blog `/insights/`. **Không có URL riêng nào** cho security / audit / cleanup.

➡️ **C3 (ngân sách lớn nhất, intent cao nhất) hiện không có chỗ để đổ traffic về.** Gửi traffic `vibe code audit` về homepage đa mục đích sẽ giết Quality Score và tỉ lệ chuyển đổi.

**Phải làm trước khi bật C3:**
1. Tạo `launchstudio.eu/en/services/ai-app-security-audit/` (+ bản NL `/diensten/beveiligingsaudit-ai-app/`)
2. Nội dung khớp keyword: scope audit, thời gian, giá khởi điểm, quy trình, form
3. Schema `Service` + `Organization` (audit 2026-07-31 ghi nhận **chưa có `Organization` schema ở bất kỳ đâu**, author schema đang là `"phu.lt"` — sửa luôn)

---

## 🚫 5. Negative keywords (bắt buộc — copy nguyên khối)

### 5.1. Shared negative list — `lovable` disambiguation (ƯU TIÊN CAO NHẤT)

```
-bra
-bras
-lingerie
-underwear
-intimates
-panties
-meaning
-definition
-synonym
-synonyms
-antonym
-quotes
-quote
-song
-songs
-lyrics
-lyric
-movie
-film
-book
-novel
-doll
-plush
-toy
-baby
-babies
-pet
-pets
-dog
-cat
-name
-names
-spelling
-loveable
```

### 5.2. Shared negative list — lọc người không mua

```
-free
-gratis
-tutorial
-tutorials
-course
-courses
-learn
-learning
-training
-certification
-jobs
-job
-vacature
-salary
-career
-internship
-stage
-download
-crack
-cracked
-torrent
-reddit
-youtube
-github
-template
-templates
-coupon
-promo
-discount
-alternative to
-open source
-day
```

> `-day` kế thừa từ `paid_ads_plan.md` để chặn bẫy `day ai` = 201.000.

### 5.3. Negative theo campaign

| Campaign | Thêm negative |
|---|---|
| C1 (NL) | `-engels`, `-english` |
| C2 (Hire) | `-fiverr`, `-upwork`, `-freelancer.com`, `-hourly rate`, `-cheap`, `-goedkoop` |
| C3 (Security) | `-antivirus`, `-vpn`, `-firewall`, `-soc 2` *(nếu không cung cấp)*, `-iso 27001` *(nếu không cung cấp)* |
| C4 (Fix) | `-how to`, `-guide`, `-step by step`, `-documentation`, `-docs` |

---

## ⚙️ 6. Match type & bid strategy

| Nhóm intent | Match type | Lý do |
|---|---|---|
| Service / Hire (P1) | **Phrase** + Exact cho top 10 | Cần bắt biến thể nhưng vẫn kiểm soát |
| Decision / Compliance | Phrase | |
| Tool-branded (`lovable app`, `bolt ai`) | **Exact bắt buộc** | Tránh bẫy §2.1 |
| Fix (nếu test) | **Exact only** | Volume thấp, dễ lệch |
| Head term (`vibe coding`) | **Không bid** hoặc Exact với ngân sách riêng | Xem §2.2 |

**Broad match: không dùng trong 8 tuần đầu.** Với niche này và với hai bẫy từ điển/thương hiệu ở trên, broad + Smart Bidding sẽ đốt ngân sách trước khi kịp học.

**Bid strategy:** Maximize Clicks với CPC cap €10 (EU-EN) / €8 (NL) trong 3–4 tuần đầu để thu dữ liệu → chuyển Maximize Conversions khi đạt ~30 conversion → Target CPA sau đó. Đây là lộ trình mà `google_ads_keywords_launchstudio.md` đã đặt; benchmark CPC 2026 ở §1.3 xác nhận mức cap đó là hợp lý nhưng sát trần dưới.

---

## 🔧 7. Quy trình 20 phút để lấy volume THẬT

Đây là bước bạn cần tự làm — mình không thay thế được.

**Bước 1 — Chuẩn bị seed list (2 phút)**
```bash
# Xuất cột keyword thuần để paste vào Keyword Planner
awk -F',' 'NR>1{print $3}' keyword_seeds_google_ads_3_clusters.csv
```

**Bước 2 — Keyword Planner (10 phút)**
1. Google Ads → Tools → **Keyword Planner** → *Get search volume and forecasts*
2. Paste danh sách từ Bước 1
3. **Quan trọng:** đặt Location = **Netherlands** → export → chạy lại với Location = **Germany, France, Spain, Italy, Sweden, Denmark, Poland, Portugal, Ireland, Belgium** (để khớp Campaign 2 hiện tại)
4. Language = Dutch cho lượt 1, English cho lượt 2
5. Export CSV cả hai lượt

**Bước 3 — Làm sạch (5 phút)**
- Xoá mọi dòng volume > 20.000 và kiểm tra thủ công — gần như chắc là bẫy kiểu `day ai` / `lovable` từ điển
- Xoá dòng có `Competition = Low` **và** `Top of page bid high < €2` — thường là truy vấn không thương mại

**Bước 4 — Quyết định (3 phút)**
- Giữ keyword có volume ≥ 10/tháng **và** intent ∈ {Hire, Service, Decision, Compliance}
- Với những keyword volume = 0 nhưng intent cao (ví dụ `vibe coding cleanup specialist`): **vẫn giữ ở Exact**. Keyword Planner hay báo 0 cho long-tail thương mại mới nổi, trong khi thực tế vẫn có truy vấn.

**Bước 5 — Đối chiếu Search Console**
71 bài đang live trên `/insights/` đã có dữ liệu impression thật. Truy vấn nào đã có impression mà chưa có bài riêng → đó là keyword rẻ nhất để vừa chạy ads vừa làm SEO.

---

## ✅ 8. Tóm tắt khuyến nghị

1. **Đừng bid broad match trên bất cứ gì chứa `lovable`** — từ điển + thương hiệu đồ lót. Đây là rủi ro đốt tiền lớn nhất.
2. **Paid Search chỉ chạy 60/129 keyword** (Hire + Service + Decision + Compliance). 30 keyword intent `Fix` để cho SEO.
3. **Tạo service page trước khi bật C3** — cụm ngân sách lớn nhất đang không có đích đến.
4. **Ad copy C2 không được đấu giá với Fiverr** — đấu bằng bảo mật + entity Manifera.
5. **Kỳ vọng low-volume**: vài trăm tới ~2.000 lượt tìm/tháng cho cả 3 cụm ở NL + EU-EN. Đánh giá bằng cost per qualified lead.
6. **Chạy §7 trước khi chốt ngân sách** — mọi con số ước tính ở §3 cần được thay bằng số thật từ Keyword Planner.

---

*Chuẩn bị bởi: LaunchStudio paid ops · Dữ liệu nền: GKP export 2026-06-15 (repo) + quét nguồn công khai 2026-09-23/24 + benchmark CPC ngành 2026*
