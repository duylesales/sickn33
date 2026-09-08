# 🎯 Google Ads Search Keywords — Manifera.com
## Bảng Từ khóa & Cấu trúc Campaign · 🇬🇧 English-only (thị trường NL / EU / APAC)

> **Nguồn dữ liệu**: `keyword-planner-manifera.com-2026-06-12 (1).csv` (1.595 từ khóa, 137.460 volume/tháng, avg competition 12/100, avg top bid $2.00) + [`manifera_info.md`](./manifera_info.md) + [`seo-geo-audit-manifera-com.md`](./seo-geo-audit-manifera-com.md)
> **Cập nhật**: 08/09/2026 · Mọi volume/bid dưới đây là số thật trích từ CSV, không phải ước lượng
> **Ngôn ngữ**: Chỉ tiếng Anh. Manifera.com là site English-only (phần `/nl/` cũ đã ngừng, xem Finding #6 của audit) — **không** chạy ad group tiếng Hà Lan vì không có landing page tiếng Hà Lan để đổ traffic vào.

---

## ⚠️ 0. Đọc phần này trước khi tiêu euro đầu tiên

CSV có 137.460 volume/tháng nhưng **con số đó gây hiểu lầm nghiêm trọng**:

| Từ khóa | Volume | Vấn đề |
|---|---|---|
| `software in software` | 49.500 | Rác cú pháp, không phải nhu cầu thương mại. **Chiếm 36% toàn bộ volume của CSV.** |
| `dev ops` | 5.400 | Người tìm định nghĩa/nghề nghiệp, không tìm vendor |
| `developer s`, `software developer` (biến thể) | ~2.900 | Chủ yếu là người tìm việc / học nghề |
| `app development`, `application development` | 1.300 mỗi từ | Head term toàn cầu, chủ yếu US, intent hỗn tạp |
| `mobile app development` + ~20 biến thể | 880 mỗi biến thể | Cùng một tập tìm kiếm bị Planner nhân bản nhiều dòng |

**Volume có ý định thương mại thật, sau khi lọc, chỉ khoảng 900–1.200 lượt/tháng trên toàn cầu** — và phần thuộc NL/EU còn nhỏ hơn nhiều (`software companies amsterdam` 50, `software companies in netherlands` 40).

**Ba hệ quả bắt buộc phải chấp nhận:**

1. **Google Search không thể một mình lấp đầy pipeline của Manifera.** Nó là kênh thu "nhu cầu đã tồn tại" với quy mô nhỏ nhưng chất lượng cao. Tăng trưởng khối lượng phải đến từ LinkedIn ABM, SEO local (200 bài city sẵn có) và các nền tảng review (Clutch, Sortlist, FeaturedCustomers) — xem [`paid_ads_plan.md`](./paid_ads_plan.md) và [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md).
2. **Đừng đấu giá theo volume, đấu giá theo bid.** Google Keyword Planner đã tự nói cho ta biết tiền nằm ở đâu: `custom software development companies` volume chỉ 70 nhưng top-of-page bid **$14,33–$34,36**. Đó là nơi các đối thủ đang tranh giành khách hàng thật.
3. **Ngân sách phải rất tập trung.** Với vỏn vẹn ~1.000 lượt tìm kiếm thương mại/tháng, một tài khoản 8 ad group đã là đủ rộng. Mở rộng thêm chỉ làm loãng dữ liệu học của Smart Bidding.

---

## 📊 1. Business Context (Bối cảnh Doanh nghiệp)

| Yếu tố | Giá trị | 🇻🇳 Ghi chú vận hành |
|---|---|---|
| **Brand** | Manifera (MANIFERA SOFTWARE DEVELOPMENT PTE LTD) | Thành lập 2014 |
| **Website** | https://www.manifera.com/ | WordPress + Yoast, đã index tốt |
| **Trụ sở EU** | Herengracht 420, Amsterdam, NL | Là tài sản đấu giá quan trọng nhất cho từ khóa local |
| **Hub kỹ thuật** | TP.HCM, Việt Nam · Văn phòng Singapore | Nguồn tin cậy cho nhóm từ khóa "vietnam/singapore sourcing" |
| **Dịch vụ lõi** | Offshore Teams · Custom Software · Mobile App · Web App · Webshop/eCommerce · NL/Euro Cloud Migration | 6 dịch vụ → không quảng cáo cùng lúc, chỉ 4 nhóm sinh lợi (xem §2) |
| **Chứng minh năng lực** | 160+ dự án · 120+ khách hàng · 10+ năm | Đưa vào callout & RSA headline |
| **Bằng chứng bên thứ ba** | Clutch · ITviec (8 review) · Sortlist · FeaturedCustomers (29 review / 19 case study) · ZoomInfo | Dùng làm sitelink + social proof trong ad copy |
| **Persona mục tiêu** | A: CTO/VP Eng tại SME EU · B: CEO/COO scale-up · C: IT Manager/PO tại MNC · D: Non-technical founder | Mỗi ad group chỉ phục vụ 1–2 persona |
| **Mô hình hợp đồng** | Dedicated Team · Project-based · Staff Augmentation | Không công bố giá → landing page phải bán bằng "team proposal trong 48h" |

### 1.1. Kinh tế đơn vị — cơ sở để chấp nhận CPC cao

| Chỉ số | Giả định thận trọng | Diễn giải |
|---|---|---|
| Giá trị hợp đồng dedicated team | €5.000 – €15.000 / tháng | 2–5 kỹ sư, hợp đồng thường kéo 12+ tháng |
| Giá trị vòng đời (LTV) thận trọng | €60.000+ | 1 team 3 kỹ sư × 12 tháng |
| Tỷ lệ Lead → SQL | 30% | Form trên site B2B services |
| Tỷ lệ SQL → Closed | 15–20% | Chu kỳ bán 60–120 ngày |
| **CPA chấp nhận được / lead** | **€150 – €250** | |
| **CPA chấp nhận được / SQL** | **€500 – €800** | |
| **Chi phí / hợp đồng chốt** | **€3.000 – €5.000** | Vẫn < 8% giá trị năm đầu |

> **Kết luận**: CPC €8–€25 cho từ khóa vendor-selection là **hợp lý**, không phải đắt. Một lead chốt được bù cho hàng trăm click.

---

## 🏗️ 2. Campaign Architecture (Cấu trúc Chiến dịch)

| Chiến dịch | Geo | Ad Group | Ngân sách Lean | Ngân sách Standard | Bidding |
|---|---|---|---|---|---|
| **`MF-Search-EU-VendorSelection`** | NL, BE, DE, SE, DK, NO, FI, IE, CH, AT | AG1, AG3 | €900/th | €1.800/th | Maximize Clicks (CPC cap €18) → Maximize Conversions sau 30 conv |
| **`MF-Search-EU-OffshoreTeams`** | NL, BE, DE, SE, DK, UK, IE | AG2 | €600/th | €1.200/th | Maximize Clicks (CPC cap €12) → tCPA €200 |
| **`MF-Search-NL-Local`** | NL (bán kính Amsterdam/Randstad + toàn quốc) | AG6 | €400/th | €900/th | Manual CPC → Target Impression Share 70% (top) |
| **`MF-Search-EU-MobileApp`** | NL, BE, DE, SE, DK | AG4 | €300/th | €700/th | Maximize Clicks (CPC cap €10) |
| **`MF-Search-Global-Sourcing`** | SG, MY, AU, HK, UK, US (chỉ nếu còn ngân sách) | AG7 | €0 (tắt) | €400/th | Maximize Clicks (CPC cap €6) |
| **`MF-Search-BOFU-Cost`** | NL, BE, DE, EU-EN | AG5 | €200/th | €500/th | Manual CPC — theo dõi sát, dễ đốt tiền |
| **`MF-Search-AI-Emerging`** | NL, BE, DE, EU-EN | AG8 | €0 (tắt) | €300/th | Maximize Clicks (CPC cap €8) — thử nghiệm |
| **`MF-Brand-Defence`** | Toàn cầu | Brand | €80/th | €150/th | Target Impression Share 95–100% |
| **`MF-PMax-Retargeting`** | NL/BE/EU-EN | — | €0 | €350/th | Max Conversion Value — chỉ bật sau khi có 100+ conversion |

**Tổng Lean ≈ €2.480/tháng · Standard ≈ €6.300/tháng.** Chi tiết phân bổ theo tier ở [`paid_ads_plan.md`](./paid_ads_plan.md) §9.

> **Nguyên tắc Geo**: Không chạy US/India/Bangladesh cho các ad group AG1–AG6. Đó là nơi giá click bị đẩy lên bởi hàng nghìn agency giá rẻ, và Manifera không cạnh tranh ở phân khúc đó.

---

## 🔑 3. Core Keywords theo từng Ad Group

> **Ký hiệu**: Vol = volume/tháng theo Keyword Planner · Comp = mức cạnh tranh (chỉ số 0–100) · Bid = khoảng giá top-of-page (USD, theo CSV) · 🔴 Cao / 🟡 Trung bình / ⚪ Thử nghiệm

---

### 🎯 Ad Group 1: Vendor Selection — Software Development Company (AG1)
> **Persona**: A (CTO/VP Eng), C (IT Manager tại MNC) · **Stage**: MOFU→BOFU
> **Landing page**: `/services/custom-software-development/` hoặc money page mới `P2 — Choosing a Software Development Partner`
> **Vì sao đây là ad group số 1**: Bid cao nhất toàn tài khoản ($34,36) = ý định mua rõ ràng nhất.

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `custom software development companies` | 70 | Medium (39) | $14,33 – $34,36 | Phrase | 🔴 | Đang lập shortlist vendor phần mềm tùy chỉnh |
| 02 | `custom software development firms` | 70 | Medium (39) | $14,33 – $34,36 | Phrase | 🔴 | Cùng intent, biến thể "firm" |
| 03 | `software development company` | 170 | Medium (48) | $9,30 – $29,52 | Phrase | 🔴 | Head term vendor, cần lọc negative kỹ |
| 04 | `software development firm` | 170 | Medium (48) | $9,30 – $29,52 | Phrase | 🔴 | Ngôn ngữ của người mua doanh nghiệp |
| 05 | `it software development company` | 170 | Medium (48) | $9,30 – $29,52 | Phrase | 🟡 | Người mua phía IT department |
| 06 | `it companies software development` | 170 | Medium (48) | $9,30 – $29,52 | Broad Match Modifier→Phrase | 🟡 | Cùng cụm, thứ tự từ khác |
| 07 | `custom software company` | 30 | Low (0) | — | Exact | 🔴 | Rẻ, intent sạch |
| 08 | `custom development company` | 30 | Low (0) | — | Exact | 🔴 | Rẻ, intent sạch |
| 09 | `software outsourcing` | 20 | Low (26) | — | Phrase | 🔴 | Đang cân nhắc mô hình outsourcing |
| 10 | `best software development companies` | 10 | Low | — | Phrase | 🟡 | Truy vấn so sánh — đẩy về bài decision-stage |
| 11 | `web development company` | 50 | Medium (45) | $5,99 – $20,40 | Phrase | 🟡 | Rộng hơn, cần negative "wordpress/wix" |
| 12 | `software house` | — | — | — | Phrase | ⚪ | Thuật ngữ phổ biến ở EU, thêm thủ công |

---

### 🎯 Ad Group 2: Offshore & Dedicated Teams (AG2)
> **Persona**: A (CTO thiếu người), B (CEO scale-up) · **Stage**: MOFU
> **Landing page**: `/services/offshore-software-development/`
> **Đặc điểm**: Volume thấp nhưng **competition gần như bằng 0** — đây là nhóm rẻ nhất và đúng USP nhất của Manifera.

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `offshore app development` | 70 | Low (0) | — | Phrase | 🔴 | Tìm đội offshore làm app |
| 02 | `offshore mobile app development` | 70 | Low (0) | — | Phrase | 🔴 | Cùng nhóm, cụ thể mobile |
| 03 | `dedicated software development team` | 30 | Low (0) | — | Exact + Phrase | 🔴 | Đúng tên sản phẩm cốt lõi của Manifera |
| 04 | `dedicated development team` | 20 | Low (0) | — | Exact + Phrase | 🔴 | Như trên |
| 05 | `software development team` | 30 | Low (0) | — | Phrase | 🟡 | Rộng hơn, có lẫn intent "team structure" |
| 06 | `development team` | 170 | Low (4) | $2,39 – $13,78 | Phrase + negative | 🟡 | Volume tốt, nhưng lẫn nhiều intent quản trị |
| 07 | `offshore software development team` | 10 | Low (0) | — | Exact | 🔴 | Intent cực sạch |
| 08 | `offshore development team` | 10 | Medium (64) | — | Exact | 🔴 | Có đối thủ đấu giá — tín hiệu tốt |
| 09 | `offshore dedicated development team` | 10 | High (76) | — | Exact | 🔴 | Cạnh tranh cao = giá trị cao |
| 10 | `outsourcing development team` | 10 | Low (0) | — | Exact | 🟡 | |
| 11 | `remote development team` | 10 | Low (0) | — | Exact | 🟡 | |
| 12 | `remote software development teams` | 10 | Low (0) | — | Exact | 🟡 | |
| 13 | `dedicated developer` / `dedicated team services` | 10 / 10 | Low (0) | — | Phrase | 🟡 | |
| 14 | `team of developers` | 50 | Low (6) | — | Phrase | 🟡 | Ngôn ngữ của non-technical founder (persona D) |
| 15 | `staff augmentation` / `it staff augmentation` | — | — | — | Phrase | 🔴 | **Không có trong CSV** — thêm thủ công, đây là tên gọi hợp đồng phổ biến nhất của MNC |
| 16 | `best offshore software development companies` | 10 | Low | — | Phrase | 🟡 | Truy vấn so sánh cuối phễu |

---

### 🎯 Ad Group 3: Custom Software & Web Application (AG3)
> **Persona**: A, C · **Stage**: MOFU
> **Landing page**: `/services/custom-software-development/` + `/services/web-app-develop/`

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `custom software development` | 30 | Low (25) | $11,68 – $21,31 | Phrase | 🔴 | Bid cao = intent mua |
| 02 | `custom software development services` | 30 | Low (13) | — | Phrase | 🔴 | Chữ "services" = tìm nhà cung cấp |
| 03 | `bespoke software development services` | 30 | Low (13) | — | Phrase | 🔴 | Thuật ngữ Anh/EU cho phần mềm may đo |
| 04 | `custom software` | 40 | Low (30) | $5,73 – $18,28 | Phrase | 🟡 | Rộng, cần negative "template/off the shelf" |
| 05 | `web application development` | 70 | Low (31) | $4,07 – $11,90 | Phrase | 🔴 | |
| 06 | `web app development` | 70 | Low (31) | $4,07 – $11,90 | Phrase | 🔴 | |
| 07 | `web and application development` | 70 | Low (31) | $4,07 – $11,90 | Phrase | 🟡 | |
| 08 | `build software` / `build a software` | 40 | Low (27) | $4,51 – $17,42 | Phrase | 🟡 | Non-technical founder (persona D) |
| 09 | `application development` | 1.300 | Low (31) | $3,99 – $17,00 | **Chỉ Exact** | 🟡 | Volume lớn nhưng intent hỗn tạp — **không dùng Phrase/Broad** |
| 10 | `bespoke software development` | 10 | High | — | Phrase | 🟡 | |
| 11 | `business software development` | 10 | High | — | Phrase | ⚪ | |
| 12 | `legacy system modernization` | — | — | — | Phrase | 🔴 | **Không có trong CSV** — thêm thủ công, đúng dịch vụ Manifera, khách MNC |

---

### 🎯 Ad Group 4: Mobile App Development (AG4)
> **Persona**: B, D · **Stage**: TOFU→MOFU
> **Landing page**: `/services/mobile-app-development/`
> **⚠️ Cảnh báo**: Đây là nhóm dễ đốt ngân sách nhất. `mobile app development` và ~20 biến thể đều 880 volume, competition Low(2) nhưng bid tới $22 — dấu hiệu điển hình của traffic toàn cầu chất lượng thấp. **Chỉ dùng match type hẹp.**

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `mobile app development company` | 40 | Medium (52) | $7,59 – $15,66 | Phrase | 🔴 | Có chữ "company" = tìm vendor |
| 02 | `mobile application development companies` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🔴 | |
| 03 | `app development companies` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🔴 | |
| 04 | `app development firm` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🔴 | |
| 05 | `mobile development company` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🟡 | |
| 06 | `mobile software development company` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🟡 | |
| 07 | `application development firm` | 40 | Medium (60) | $5,56 – $16,09 | Phrase | 🟡 | |
| 08 | `app developers` | 320 | Medium (52) | $4,20 – $24,29 | **Chỉ Exact** | 🟡 | Lẫn nhiều người tìm việc |
| 09 | `mobile app development` | 880 | Low (2) | $4,45 – $22,02 | **Chỉ Exact + geo NL/BE** | ⚪ | Chỉ mở sau khi AG1–AG3 đã ổn định |
| 10 | `ecommerce app development companies` | 10 | Low (0) | — | Phrase | 🟡 | Cầu nối sang dịch vụ webshop |
| 11 | `react native development company` | — | — | — | Phrase | ⚪ | Thêm thủ công theo tech stack |

---

### 🎯 Ad Group 5: Cost & Pricing — BOFU (AG5)
> **Persona**: B, D · **Stage**: BOFU
> **Landing page**: money page mới `P4 — What Custom Software Actually Costs` (bắt buộc phải có khoảng giá thật, nếu không CPC sẽ lãng phí)
> **⚠️** Toàn nhóm này competition High (76–86). Người tìm giá thường chưa có ngân sách. **Chỉ chạy khi đã có trang giá tử tế.**

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `custom software development cost` | 10 | Low (0) | — | Phrase | 🔴 | Sạch nhất trong nhóm |
| 02 | `custom software development pricing` | 10 | Low (0) | — | Phrase | 🔴 | |
| 03 | `custom software cost` | 10 | Low (0) | — | Phrase | 🔴 | |
| 04 | `cost to build software` | 10 | Low (0) | — | Phrase | 🟡 | |
| 05 | `cost of web application development` | 10 | Low (0) | — | Phrase | 🟡 | |
| 06 | `mobile app development cost` | 40 | High (76) | $2,30 – $9,42 | Phrase | 🟡 | Volume cao nhất nhóm nhưng cạnh tranh gắt |
| 07 | `application development cost` | 40 | High (76) | $2,30 – $9,42 | Phrase | 🟡 | |
| 08 | `app development cost` | 40 | High (76) | $2,30 – $9,42 | Phrase | 🟡 | |
| 09 | `cost to build an app` | 10 | Medium (61) | $3,80 – $5,63 | Phrase | ⚪ | |
| 10 | `software development cost` | 10 | High (86) | — | Phrase | ⚪ | |
| 11 | `developer cost` / `software engineer cost` | 10 / 10 | Low (0) | — | Phrase | ⚪ | Có thể lẫn người tìm lương |

---

### 🎯 Ad Group 6: Netherlands Local (AG6)
> **Persona**: A, C tại Hà Lan · **Stage**: MOFU→BOFU
> **Landing page**: trang Amsterdam/NL riêng (chưa tồn tại — **phải xây**, xem [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md) §4)
> **Vì sao quan trọng nhất về mặt chiến lược**: đây là nhóm duy nhất mà "Herengracht 420, Amsterdam" là lợi thế không thể sao chép, và Manifera đã có sẵn **200 bài local** (`extra-1-local`, `extra-8-local`) phủ Amsterdam, Rotterdam, Haarlem, Utrecht, Amstelveen, Zaanstad… để hỗ trợ Quality Score bằng nội dung.

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `software companies amsterdam` | 50 | Medium (57) | $2,73 – $9,80 | Phrase | 🔴 | Rẻ + đúng địa bàn trụ sở |
| 02 | `software companies in netherlands` | 40 | High (69) | $3,52 – $14,33 | Phrase | 🔴 | Competition High = có người mua thật |
| 03 | `software development companies in netherlands` | 10 | High (100) | — | Exact | 🔴 | **Competition Index 100** — mức cạnh tranh cao nhất toàn CSV |
| 04 | `mobile app development company in netherlands` | 10 | Low (0) | — | Exact | 🔴 | Rẻ, intent hoàn hảo |
| 05 | `netherlands software` | 10 | Low (0) | — | Phrase | 🟡 | |
| 06 | `software development company amsterdam` | — | — | — | Phrase | 🔴 | Thêm thủ công |
| 07 | `custom software development amsterdam` | — | — | — | Phrase | 🔴 | Thêm thủ công |
| 08 | `software bedrijf amsterdam` | — | — | — | Phrase | ⚪ | ❌ **Không chạy** — không có landing page NL |

---

### 🎯 Ad Group 7: Vietnam / Singapore Sourcing (AG7)
> **Persona**: A, C đã quyết định outsourcing sang châu Á, đang chọn quốc gia · **Stage**: MOFU
> **Landing page**: `/about-offshore-software-development-vietnam/` (đã tồn tại)
> **Tài sản nội dung hỗ trợ**: cụm `extra-6-dutchvsvietnam` (100 bài so sánh NL vs VN) — đúng ngay chủ đề của nhóm từ khóa này.

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `it outsourcing company in vietnam` | 10 | Low (0) | — | Phrase | 🔴 | |
| 02 | `software outsourcing company in vietnam` | 10 | Low (0) | — | Phrase | 🔴 | |
| 03 | `software development company vietnam` | 10 | Low (0) | — | Phrase | 🔴 | |
| 04 | `vietnam software development company` | 10 | Low (0) | — | Phrase | 🔴 | |
| 05 | `outsourcing company in vietnam` | 10 | Low (0) | — | Phrase | 🟡 | |
| 06 | `it companies in vietnam` | 10 | Low (0) | — | Phrase | 🟡 | |
| 07 | `software developer vietnam` | 10 | High (71) | — | Exact | 🟡 | Cạnh tranh cao, có lẫn tuyển dụng |
| 08 | `custom software development singapore` | 10 | Low (0) | — | Phrase | 🟡 | |
| 09 | `software development company singapore` | 10 | Low (0) | — | Phrase | 🟡 | |
| 10 | `mobile app development company singapore` | 10 | Low (0) | — | Phrase | ⚪ | |
| 11 | `best software company in singapore` | 10 | Low (0) | — | Phrase | ⚪ | |

---

### 🎯 Ad Group 8: AI & Emerging Tech (AG8 — thử nghiệm)
> **Persona**: A, B · **Stage**: TOFU
> **⚠️** Nhóm này chỉ bật ở tier Standard trở lên. Traffic AI hiện rẻ nhưng ý định mua chưa rõ; mục tiêu là thu audience cho retargeting, không phải lead trực tiếp.

| # | Keyword | Vol | Comp | Bid (USD) | Match | Ưu tiên | 🇻🇳 Search Intent |
|---|---|---|---|---|---|---|---|
| 01 | `ai software development companies` | 20 | Low (17) | — | Phrase | 🔴 | Intent vendor rõ nhất trong nhóm |
| 02 | `ai app development company` | 10 | Low (0) | — | Phrase | 🔴 | |
| 03 | `ai app development services` | 10 | Low (0) | — | Phrase | 🔴 | |
| 04 | `ai development services` | 10 | Low (0) | — | Phrase | 🟡 | |
| 05 | `offshore ai developers` | 10 | Low (0) | — | Phrase | 🔴 | Giao điểm hoàn hảo giữa AI và USP offshore |
| 06 | `ai solution development` | 10 | Low (14) | — | Phrase | 🟡 | |
| 07 | `ai software development` | 70 | Medium (63) | $3,87 – $8,74 | Exact | 🟡 | |
| 08 | `ai developers` | 320 | Medium (60) | $2,23 – $15,71 | **Chỉ Exact** | ⚪ | Lẫn rất nhiều người tìm việc |

---

## 🏷️ 4. Brand Keywords (Chiến dịch Bảo vệ Thương hiệu)

> Ngân sách nhỏ (€80–150/tháng) nhưng **bắt buộc**: Manifera đã có mặt trên Clutch/Sortlist, đối thủ hoàn toàn có thể đấu giá tên thương hiệu để cướp lead cuối phễu.

| # | Keyword | Match | Ưu tiên | 🇻🇳 Mục đích |
|---|---|---|---|---|
| 01 | `manifera` | Exact + Phrase | 🔴 | Tên thương hiệu chính |
| 02 | `manifera.com` / `manifera com` | Phrase | 🔴 | Người gõ tên miền vào ô tìm kiếm |
| 03 | `manifera software development` | Phrase | 🔴 | |
| 04 | `manifera vietnam` / `manifera amsterdam` | Phrase | 🔴 | Truy vấn xác minh địa điểm |
| 05 | `manifera reviews` / `manifera clutch` | Phrase | 🔴 | **Quan trọng**: chặn đối thủ chen vào truy vấn kiểm chứng uy tín |
| 06 | `manifera careers` | — | — | ❌ Thêm làm **negative** — người tìm việc, không phải khách hàng |

---

## 🚫 5. Negative Keywords (6 danh sách dùng chung)

> Áp dụng dạng **Shared Negative List** cho toàn tài khoản. Với ngân sách nhỏ và head term rác chiếm 36% CSV, đây là phần có ROI cao nhất của cả tài liệu này.

| Danh sách | Negative keywords | 🇻🇳 Lý do loại trừ |
|---|---|---|
| **1. Job seekers & tuyển dụng** | `job`, `jobs`, `vacancy`, `vacature`, `career`, `careers`, `hiring`, `recruitment`, `salary`, `salaries`, `wage`, `intern`, `internship`, `resume`, `cv`, `apply`, `glassdoor`, `indeed`, `linkedin jobs`, `itviec` | Nhóm rác lớn nhất: rất nhiều truy vấn `developer`, `software developer`, `ai developers` là người tìm việc |
| **2. Học tập & tự làm** | `course`, `courses`, `tutorial`, `learn`, `training`, `certification`, `bootcamp`, `degree`, `university`, `pdf`, `book`, `roadmap`, `how to become`, `w3schools`, `udemy`, `coursera` | Không có ý định thuê dịch vụ |
| **3. Miễn phí & tải phần mềm** | `free`, `download`, `crack`, `trial`, `open source`, `github`, `template`, `demo`, `sample`, `cheap`, `cheapest` | Ngân sách €0 |
| **4. Head term rác của CSV** | `software in software`, `developer s`, `dev ops`, `devops engineer`, `what is`, `meaning`, `definition`, `wikipedia`, `reddit`, `quora` | `software in software` một mình chiếm 49.500 volume — nếu lọt Broad Match sẽ đốt sạch ngân sách trong vài ngày |
| **5. Sai phân khúc / DIY** | `wordpress`, `wix`, `squarespace`, `shopify theme`, `no code`, `low code`, `bubble.io`, `freelancer`, `freelance`, `upwork`, `fiverr`, `toptal`, `hourly rate india`, `student project` | Manifera bán đội ngũ kỹ sư, không cạnh tranh với freelancer/no-code |
| **6. Sản phẩm phần mềm (không phải dịch vụ)** | `erp`, `sap`, `salesforce`, `crm software`, `accounting software`, `antivirus`, `driver`, `app store`, `play store`, `login`, `pricing plan` | Người tìm mua *phần mềm đóng gói*, không tìm đơn vị phát triển |

**Negative theo campaign (không dùng chung):**
- `MF-Search-NL-Local`: thêm `belgium`, `germany`, `india`, `poland`, `ukraine`
- `MF-Search-EU-*`: thêm `vietnam`, `singapore` (để không ăn traffic của AG7)
- `MF-Search-BOFU-Cost`: thêm `calculator`, `template`, `estimate spreadsheet`

---

## 🔗 6. Ad Extensions (Tiện ích mở rộng)

### 📌 Sitelinks
| # | Sitelink | Description line 1 | Description line 2 | URL đích |
|---|---|---|---|---|
| 1 | Offshore Dev Teams | Dedicated engineers, Dutch-managed | Scale up or down in 2–4 weeks | `/services/offshore-software-development/` |
| 2 | Our Portfolio | 160+ delivered projects | SME and enterprise clients | `/portfolio/` |
| 3 | Client Reviews | Verified on Clutch & FeaturedCustomers | 29 reviews, 19 case studies | `/testimonials/` |
| 4 | About Manifera | Amsterdam HQ, Vietnam engineering hub | Founded 2014, 120+ clients | `/about-us/` |
| 5 | Get a Team Proposal | Custom proposal within 48 hours | No obligation, no hourly billing | `/contact-us/` |
| 6 | Cloud Migration (EU) | GDPR-compliant EU hosting | AWS EU / Azure West Europe | `/services/migration-to-nl-euro-cloud-en/` |

### 📌 Callout Extensions
`Founded 2014` · `160+ Projects Delivered` · `120+ Global Clients` · `Amsterdam HQ` · `Dutch Project Management` · `4–5h CET Overlap` · `Scale in 2–4 Weeks` · `No Long-Term Lock-In` · `English-Fluent Engineers` · `GDPR-Compliant Delivery`

### 📌 Structured Snippets
- **Services**: Offshore Teams · Custom Software · Mobile Apps · Web Applications · eCommerce · Cloud Migration
- **Types**: Dedicated Team · Staff Augmentation · Project-Based · MVP Development · Legacy Modernization
- **Technologies**: Laravel · .NET · React · Node.js · React Native · Flutter · AWS · Azure

### 📌 Lead Form Extension (chỉ NL/BE)
Headline: `Get a dedicated team proposal in 48 hours` — Trường: Company, Role, Team size needed, Email công ty. **Không** hỏi số điện thoại ở bước này (giảm 30–40% tỷ lệ điền form B2B).

### 📌 Image & Location Extensions
- Location Extension: bật với địa chỉ Amsterdam (Herengracht 420) — tăng CTR đáng kể cho AG6.
- Image Extension: ảnh đội ngũ thật tại HCMC + văn phòng Amsterdam. Không dùng ảnh stock.

---

## 📅 7. Kế hoạch Triển khai 30 ngày

| Tuần | Việc phải xong | Tiêu chí nghiệm thu |
|---|---|---|
| **Tuần 1** | Cài đặt đo lường: GA4 (G-ZGH74C8BL4) + Google Ads conversion tracking + Enhanced Conversions. Định nghĩa 3 conversion: `form_submit_contact`, `proposal_request`, `phone_call_60s`. Import 6 shared negative list. | Test conversion bắn đúng trên staging; negative list đã gắn vào tài khoản |
| **Tuần 2** | Xây landing page bắt buộc: `/nl-amsterdam/` (AG6) và money page giá (AG5). Chưa có 2 trang này thì **chưa bật** AG5, AG6. | 2 trang live, có form, tốc độ LCP < 2,5s |
| **Tuần 3** | Bật AG1 + AG2 + Brand (chỉ 3 nhóm này). Ngân sách Lean. Manual CPC để lấy dữ liệu thật về CPC. | 7 ngày đầu: ≥ 50 click, search term report được rà thủ công mỗi ngày |
| **Tuần 4** | Rà 100% search term report → bổ sung negative đợt 2. Bật AG3 + AG6. Đánh giá có nên bật AG4/AG5 hay không dựa trên CPL thực tế. | CPL < €250; nếu > €400 thì dừng mở rộng, tối ưu landing page trước |
| **Ngày 30** | Báo cáo: CPC thực tế vs bid dự kiến, CPL, tỷ lệ search term rác, Quality Score từng ad group. | Quyết định tăng lên tier Standard hay giữ Lean thêm 30 ngày |

> **Quy tắc vàng**: Không bật cả 8 ad group cùng lúc. Với ~1.000 lượt tìm kiếm thương mại/tháng, mở hết một lượt sẽ khiến mỗi nhóm chỉ nhận vài click/tuần — không đủ dữ liệu để tối ưu bất cứ thứ gì.

---

## 📎 8. Việc còn thiếu — cần bổ sung bằng nghiên cứu riêng

CSV tháng 6/2026 **không phủ** những mảng sau, dù Manifera có bán dịch vụ:

| Mảng | Vì sao thiếu | Việc cần làm |
|---|---|---|
| **Magento / WooCommerce / webshop** | CSV chỉ có 2 từ khóa eCommerce (`ecommerce app developers`, `ecommerce app development companies`, đều 10 volume) | Chạy Keyword Planner riêng với seed `magento development agency`, `magento migration`, `b2b webshop` — đây là dịch vụ Manifera bán nhưng gần như vô hình trong dữ liệu hiện tại |
| **Staff augmentation** | Không xuất hiện dòng nào | Nghiên cứu riêng; đây là thuật ngữ hợp đồng chuẩn của khách MNC (persona C) |
| **Legacy modernization** | Không xuất hiện | Nghiên cứu riêng; giá trị hợp đồng cao nhất |
| **Volume theo quốc gia** | CSV là volume toàn cầu, không tách NL/BE/DE | Xuất lại Keyword Planner với filter Location = Netherlands để biết quy mô thật của thị trường nhà |
| **Từ khóa đối thủ** | Không có | Dùng Ads Transparency Center + Semrush để xem Sortlist/Clutch top-agency đang đấu giá gì |

---

*Tài liệu liên quan: [`google_ads_rsa_copy_manifera.md`](./google_ads_rsa_copy_manifera.md) · [`paid_ads_plan.md`](./paid_ads_plan.md) · [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md) · [`implementation_plan.md`](./implementation_plan.md)*
