# 🎯 Google Ads Search Keywords — OnlyAIJobs.eu
## Bảng Từ khóa & Cấu trúc Campaign Song ngữ: 🇬🇧 English ⟷ 🇳🇱 Nederlands

> **Nguồn**: quét trực tiếp onlyaijobs.eu ngày 08/09/2026 · [`onlyaijobs_info.md`](./onlyaijobs_info.md) · [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md)
> **⚠️ Không có dữ liệu volume.** OnlyAIJobs chưa từng chạy Keyword Planner. Mọi ô Volume/Bid ghi `TBD` — **không điền số ước đoán**. Cách lấy dữ liệu: [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) §3.4.

---

## 🛑 0. ĐỌC PHẦN NÀY TRƯỚC — Hiện Tại Chưa Nên Chạy Quảng Cáo

Tài liệu này **sẵn sàng để triển khai**, nhưng triển khai ngay hôm nay sẽ đốt tiền. Ba lý do:

| Rào chắn | Hiện trạng | Hệ quả nếu chạy ads ngay |
|---|---|---|
| **Nguồn cung** | 52 tin, 100% đăng cách đây ~1 tháng | Người tìm việc nhấp vào, thấy 52 tin cũ, rời đi và không quay lại. Tiền quảng cáo mua được một lần thất vọng. |
| **Landing page nhà tuyển dụng** | `/pages/info-for-employers` và `/pages/add-a-vacancy` đều **trả về trang trắng** | Mọi click từ nhóm quảng cáo nhà tuyển dụng đổ vào trang rỗng. Tỷ lệ chuyển đổi 0%. |
| **Đo lường** | Không phát hiện GA4/GTM nào trên site | Không đo được conversion thì không tối ưu được — chỉ là chi tiền mù. |

### 🚦 Ba cổng phải qua trước khi bật euro đầu tiên

| Cổng | Điều kiện | Nhóm quảng cáo được mở |
|---|---|---|
| **Cổng A** | Cài GA4 + conversion tracking; viết nội dung thật cho `/pages/info-for-employers` | **AG-E1, AG-E2** (nhắm nhà tuyển dụng) |
| **Cổng B** | ≥120 tin đang hiệu lực, có tin mới hàng tuần | **AG-J1 → AG-J5** (nhắm người tìm việc) |
| **Cổng C** | Có trang chi tiết từng việc làm + `JobPosting` schema | Chiến dịch Remarketing + PMax |

**🇻🇳 Chiến lược đúng cho marketplace hai chiều**: **mua nguồn cung trước, đừng mua nhu cầu.** Một job board 52 tin không thể quảng cáo cho người tìm việc — không có gì để họ tìm. Toàn bộ ngân sách giai đoạn đầu phải dồn vào việc lấy thêm tin tuyển dụng. Khi có 200+ tin thì phía người tìm việc mới đáng chi tiền.

---

## 📊 1. Business Context

| Yếu tố | 🇬🇧 English | 🇳🇱 Nederlands | 🇻🇳 Ghi chú |
|---|---|---|---|
| **Brand** | OnlyAIJobs | OnlyAIJobs | |
| **Website** | https://onlyaijobs.eu | https://onlyaijobs.eu/nl | Site song ngữ thật, không phải dịch máy |
| **Sản phẩm** | AI-only job board | AI-vacaturebank | Chỉ việc làm AI/ML/Data |
| **Khác biệt** | Vacancies at exact address level + distance from your home | Vacatures op exact adresniveau + afstand vanaf je woonplaats | USP không job board lớn nào có |
| **Thị trường** | Netherlands (49/52 tin) | Nederland | 3 tin ở Mỹ nên cân nhắc gỡ |
| **Giá cho nhà tuyển dụng** | First vacancy free | Eerste vacature gratis | Giá tin thứ 2 trở đi: 🟥 chưa xác định |
| **Cách đăng tin** | Email tới info@onlyaijobs.eu | idem | Thủ công — là rào cản chuyển đổi lớn |
| **Nhà tuyển dụng tiêu biểu** | Accenture, Cegeka, Sendcloud, Mollie, Heijmans, Rexel, VINCI Energies | idem | Bằng chứng xã hội mạnh nhất hiện có |
| **Danh mục có tin thật** | Development, Machine Learning, Research, Infrastructure, Ethics & Governance | idem | 5/11 danh mục còn rỗng |

---

## 🏗️ 2. Campaign Architecture

| Chiến dịch | Cổng | Geo | Ngôn ngữ | Ngân sách khởi điểm | Bidding |
|---|---|---|---|---|---|
| **`OAJ-Employers-NL`** | A | Hà Lan | 🇳🇱 NL | €400/tháng | Manual CPC → Maximize Conversions |
| **`OAJ-Employers-EN`** | A | NL, BE | 🇬🇧 EN | €200/tháng | Manual CPC |
| **`OAJ-Seekers-NL-Role`** | B | Hà Lan | 🇳🇱 NL | €500/tháng | Maximize Clicks (CPC cap €1,20) |
| **`OAJ-Seekers-NL-City`** | B | Theo bán kính từng thành phố | 🇳🇱 NL | €300/tháng | Manual CPC |
| **`OAJ-Seekers-EN`** | B | NL, BE + expat targeting | 🇬🇧 EN | €250/tháng | Maximize Clicks (CPC cap €1,50) |
| **`OAJ-Brand`** | A | Toàn cầu | 🇬🇧+🇳🇱 | €40/tháng | Target Impression Share 95% |
| **`OAJ-Remarketing`** | C | NL | 🇳🇱+🇬🇧 | €150/tháng | Max Conversions |

> **Lưu ý về CPC**: quảng cáo nhắm **người tìm việc** có CPC rất thấp (thường €0,30–€1,50) vì giá trị mỗi click thấp và cạnh tranh chủ yếu là các job board. Quảng cáo nhắm **nhà tuyển dụng** đắt hơn nhiều (€3–€10) vì đó là truy vấn B2B có giá trị. Đừng gộp hai loại vào cùng một chiến dịch — chúng cần chiến lược bid hoàn toàn khác.

---

## 🔑 3. Từ Khóa Theo Ad Group

### 🎯 AG-E1: Nhà Tuyển Dụng — Đăng Tin (Cổng A) 🇳🇱
> **Landing page**: `/nl/pages/vacature-plaatsen` — ⚠️ **hiện là trang trắng, phải viết trước**
> **Persona**: C (hiring manager / recruiter) · **Góc bán**: "Tin đầu tiên miễn phí, chỉ cần gửi một email"

| # | 🇳🇱 Keyword | Match | Ưu tiên | Volume | 🇻🇳 Ý định |
|---|---|---|---|---|---|
| 01 | `vacature plaatsen` | Phrase | 🔴 | TBD | Muốn đăng tin tuyển dụng |
| 02 | `gratis vacature plaatsen` | Phrase | 🔴 | TBD | **Khớp chính xác USP "tin đầu miễn phí"** |
| 03 | `vacature plaatsen gratis` | Phrase | 🔴 | TBD | Biến thể thứ tự từ |
| 04 | `vacaturebank voor werkgevers` | Phrase | 🔴 | TBD | Tìm nền tảng đăng tin |
| 05 | `ai specialist werven` | Phrase | 🔴 | TBD | Tuyển chuyên gia AI |
| 06 | `data scientist werven` | Phrase | 🟡 | TBD | |
| 07 | `machine learning engineer vinden` | Phrase | 🟡 | TBD | |
| 08 | `personeel werven ict` | Phrase | 🟡 | TBD | Rộng hơn, cần negative |
| 09 | `vacature adverteren` | Phrase | 🟡 | TBD | |
| 10 | `waar vacature plaatsen` | Phrase | 🔴 | TBD | Truy vấn so sánh nền tảng — vàng |

### 🎯 AG-E2: Nhà Tuyển Dụng — Thay Thế Nền Tảng Đắt (Cổng A) 🇳🇱🇬🇧
> **Góc bán**: "Indeed và LinkedIn tính tiền theo click và vẫn gửi hồ sơ không liên quan. Ở đây chỉ có ứng viên AI."

| # | Keyword | Lang | Match | Ưu tiên | Volume |
|---|---|---|---|---|---|
| 01 | `indeed alternatief` | 🇳🇱 | Phrase | 🔴 | TBD |
| 02 | `linkedin recruiter alternatief` | 🇳🇱 | Phrase | 🟡 | TBD |
| 03 | `goedkoop vacatures plaatsen` | 🇳🇱 | Phrase | 🔴 | TBD |
| 04 | `niche vacaturebank` | 🇳🇱 | Phrase | 🔴 | TBD |
| 05 | `post ai job` | 🇬🇧 | Phrase | 🔴 | TBD |
| 06 | `post machine learning job` | 🇬🇧 | Phrase | 🟡 | TBD |
| 07 | `where to post ai vacancy` | 🇬🇧 | Phrase | 🔴 | TBD |
| 08 | `ai job board for employers` | 🇬🇧 | Phrase | 🔴 | TBD |
| 09 | `hire ai engineer netherlands` | 🇬🇧 | Phrase | 🔴 | TBD |
| 10 | `recruit machine learning engineer` | 🇬🇧 | Phrase | 🟡 | TBD |

---

### 🎯 AG-J1: Người Tìm Việc — Vai Trò (Cổng B) 🇳🇱
> **Landing page**: `/nl/vacatures/<rol>` · **Persona**: A, B
> ⚠️ Chỉ mở khi có ≥120 tin đang hiệu lực.

| # | 🇳🇱 Keyword | Match | Ưu tiên | Volume | 🇻🇳 Ý định |
|---|---|---|---|---|---|
| 01 | `ai vacatures` | Phrase | 🔴 | TBD | Truy vấn cốt lõi của thương hiệu |
| 02 | `ai engineer vacature` | Phrase | 🔴 | TBD | |
| 03 | `machine learning vacature` | Phrase | 🔴 | TBD | Danh mục lớn nhất trên site |
| 04 | `data scientist vacature` | Phrase | 🔴 | TBD | |
| 05 | `artificial intelligence vacatures` | Phrase | 🟡 | TBD | |
| 06 | `ai banen` | Phrase | 🟡 | TBD | "banen" = biến thể của "vacatures" |
| 07 | `data engineer vacature` | Phrase | 🟡 | TBD | |
| 08 | `computer vision vacature` | Exact | ⚪ | TBD | ⛔ Danh mục hiện **rỗng** — chưa chạy |
| 09 | `ai onderzoeker vacature` | Phrase | 🟡 | TBD | Danh mục Research có 9 tin |
| 10 | `robotics engineer vacature` | Exact | ⚪ | TBD | Chỉ 2 tin — thận trọng |

### 🎯 AG-J2: Người Tìm Việc — Vai Trò + Thành Phố (Cổng B) 🇳🇱
> **Landing page**: `/nl/vacatures/<rol>-<stad>` — chỉ chạy cho thành phố có ≥3 tin
> **🇻🇳 Đây là nhóm có tỷ lệ chuyển đổi cao nhất phía người tìm việc**: ý định địa phương rõ, cạnh tranh nhẹ, và khớp đúng USP "địa chỉ chính xác".

| # | Mẫu từ khóa | Match | Ưu tiên | Volume |
|---|---|---|---|---|
| 01 | `ai vacatures amsterdam` | Phrase | 🔴 | TBD |
| 02 | `ai vacatures eindhoven` | Phrase | 🔴 | TBD |
| 03 | `ai vacatures utrecht` | Phrase | 🔴 | TBD |
| 04 | `ai vacatures rotterdam` | Phrase | 🔴 | TBD |
| 05 | `ai vacatures groningen` | Phrase | 🟡 | TBD |
| 06 | `machine learning vacatures <stad>` | Phrase | 🔴 | TBD |
| 07 | `data scientist vacatures <stad>` | Phrase | 🟡 | TBD |
| 08 | `it vacatures noord-brabant` | Phrase | 🔴 | TBD |
| 09 | `ai vacatures brabant` | Phrase | 🔴 | TBD |
| 10 | `tech vacatures bij mij in de buurt` | Phrase | 🔴 | TBD |

> **Quy tắc**: mỗi thành phố chỉ được đưa vào chiến dịch khi trang đích tương ứng vượt ngưỡng 3 tin (xem [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) §4.1). Quảng cáo dẫn về trang rỗng là cách nhanh nhất để đốt ngân sách và làm hỏng Quality Score.

### 🎯 AG-J3: Người Mới Ra Trường (Cổng B) 🇳🇱
> **Persona A** — nhóm khớp nhất với câu chuyện gốc "sinh viên Brabant rời quê"

| # | 🇳🇱 Keyword | Match | Ưu tiên | Volume |
|---|---|---|---|---|
| 01 | `ai stage` | Phrase | 🔴 | TBD |
| 02 | `afstudeerstage ai` | Phrase | 🔴 | TBD |
| 03 | `stage machine learning` | Phrase | 🔴 | TBD |
| 04 | `data science stage` | Phrase | 🟡 | TBD |
| 05 | `traineeship data science` | Phrase | 🟡 | TBD |
| 06 | `starterfunctie ai` | Phrase | 🟡 | TBD |
| 07 | `junior data scientist vacature` | Phrase | 🔴 | TBD |
| 08 | `eerste baan na studie ai` | Phrase | ⚪ | TBD |

### 🎯 AG-J4: Người Tìm Việc — English (Cổng B) 🇬🇧
> Nhóm kỹ sư AI người nước ngoài đang sống/muốn chuyển tới Hà Lan

| # | 🇬🇧 Keyword | Match | Ưu tiên | Volume | 🇻🇳 Ghi chú |
|---|---|---|---|---|---|
| 01 | `ai jobs netherlands` | Phrase | 🔴 | TBD | |
| 02 | `machine learning jobs netherlands` | Phrase | 🔴 | TBD | |
| 03 | `ai engineer jobs amsterdam` | Phrase | 🔴 | TBD | |
| 04 | `data scientist jobs netherlands` | Phrase | 🟡 | TBD | |
| 05 | `ai jobs eindhoven` | Phrase | 🟡 | TBD | Brainport — mật độ công ty AI cao |
| 06 | `ai jobs europe` | Exact | ⚪ | TBD | ⚠️ Rộng và đắt, chỉ Exact |
| 07 | `english speaking tech jobs netherlands` | Phrase | 🔴 | TBD | Ý định expat rõ |
| 08 | `ai jobs with visa sponsorship netherlands` | Phrase | 🟡 | TBD | 🟥 Chỉ chạy nếu site lọc được theo visa |

### 🎯 AG-J5: Remote & Hình Thức (Cổng B) 🇬🇧🇳🇱
| # | Keyword | Lang | Match | Ưu tiên | Volume |
|---|---|---|---|---|---|
| 01 | `remote ai jobs` | 🇬🇧 | Phrase | 🔴 | TBD |
| 02 | `remote machine learning jobs europe` | 🇬🇧 | Phrase | 🟡 | TBD |
| 03 | `thuiswerk it vacatures` | 🇳🇱 | Phrase | 🟡 | TBD |
| 04 | `hybride vacatures ai` | 🇳🇱 | Phrase | 🟡 | TBD |
| 05 | `parttime data science vacature` | 🇳🇱 | Phrase | ⚪ | TBD |

> ⚠️ Bộ lọc trên site có "Remote" nhưng **cả 52 tin hiện tại đều Full-time** và không rõ có tin remote nào. Xác minh trước khi bật nhóm này.

---

## 🏷️ 4. Brand Campaign

| # | Keyword | Match | Ưu tiên | 🇻🇳 Mục đích |
|---|---|---|---|---|
| 01 | `onlyaijobs` | Exact + Phrase | 🔴 | Tên thương hiệu |
| 02 | `only ai jobs` | Phrase | 🔴 | Cách viết tách từ |
| 03 | `onlyaijobs.eu` | Phrase | 🔴 | Gõ tên miền vào ô tìm kiếm |
| 04 | `onlyaijobs vacatures` | Phrase | 🟡 | |

> Ngân sách €40/tháng là đủ ở giai đoạn này — thương hiệu chưa có nhận biết nên volume rất thấp. Nhưng bật sớm để chiếm chỗ trước khi có ai đấu giá tên này.

---

## 🚫 5. Negative Keywords (5 danh sách dùng chung)

| Danh sách | 🇬🇧 English | 🇳🇱 Nederlands | 🇻🇳 Lý do |
|---|---|---|---|
| **1. Nhầm phía marketplace** | `hire`, `recruit`, `post a job`, `for employers` | `werven`, `vacature plaatsen`, `voor werkgevers` | **Thêm vào chiến dịch người tìm việc** để không ăn traffic của chiến dịch nhà tuyển dụng — và ngược lại. Đây là negative quan trọng nhất của mọi marketplace hai chiều. |
| **2. Học tập, không tìm việc** | `course`, `tutorial`, `learn ai`, `bootcamp`, `certification`, `study`, `university`, `master` | `cursus`, `opleiding`, `studie`, `leren`, `master` | Người muốn học AI, không tìm việc AI |
| **3. Ngoài phạm vi ngành** | `ai tools`, `chatgpt`, `midjourney`, `ai generator`, `ai writing`, `prompt` | `ai tools`, `chatgpt` | Truy vấn về công cụ AI, không phải việc làm AI — nhóm rác lớn nhất của ngành này |
| **4. Ngoài phạm vi địa lý** | `usa`, `india`, `uk`, `germany`, `dubai`, `canada`, `visa sponsorship india` | `duitsland`, `belgië` (nếu chỉ nhắm NL) | 49/52 tin ở Hà Lan |
| **5. Sai loại việc** | `data entry`, `freelance`, `part time student`, `bijbaan`, `weekend job`, `internship abroad` | `bijbaan`, `vakantiewerk`, `uitzendbureau` | Không khớp với kho tin (100% full-time chuyên môn cao) |

**Negative đặc thù**: thêm `computer vision`, `generative ai`, `ai product`, `quality control`, `security` vào negative **cho tới khi các danh mục đó có tin thật** — hiện cả 5 đều rỗng.

---

## 🔗 6. Ad Extensions

### 📌 Sitelinks — 🇳🇱 (chiến dịch NL)
| # | Sitelink | Mô tả | URL |
|---|---|---|---|
| 1 | Alle AI-vacatures | 52 vacatures bij 40 werkgevers | `/nl/vacatures` |
| 2 | Vacatures in je buurt | Zie de afstand vanaf je woonplaats | `/nl/vacatures` |
| 3 | Machine Learning | De grootste categorie op OnlyAIJobs | `/nl/vacatures/machine-learning` |
| 4 | Gratis vacature plaatsen | Je eerste vacature is gratis | `/nl/pages/vacature-plaatsen` ⚠️ *phải viết trước* |

### 📌 Sitelinks — 🇬🇧
| # | Sitelink | Mô tả | URL |
|---|---|---|---|
| 1 | Browse All AI Jobs | AI, ML and data roles in the Netherlands | `/jobs` |
| 2 | Jobs Near You | Every vacancy at exact address level | `/jobs` |
| 3 | For Employers | First vacancy is free | `/pages/info-for-employers` ⚠️ *phải viết trước* |
| 4 | About OnlyAIJobs | Why we built a regional AI job board | `/pages/about-us` ⚠️ *phải viết trước* |

### 📌 Callouts
- 🇬🇧 `AI Roles Only` · `Exact Address Shown` · `Distance From Home` · `First Listing Free` · `No Recruiter Spam`
- 🇳🇱 `Alleen AI-vacatures` · `Exact adresniveau` · `Afstand vanaf huis` · `Eerste vacature gratis` · `Geen recruiterspam`

### 📌 Structured Snippets
- **Categories (EN)**: Machine Learning · Development · Research · Infrastructure · AI Governance
- **Categorieën (NL)**: Machine Learning · Development · Research · Infrastructuur · AI-governance
- ⚠️ Chỉ liệt kê 5 danh mục **có tin thật**. Không quảng cáo Computer Vision / Generative AI khi chúng đang rỗng.

### 📌 Location Extension
🟥 **Cần bổ sung** — chưa biết địa chỉ pháp lý của OnlyAIJobs. Nếu có văn phòng tại Noord-Brabant, đây là tài sản mạnh cho chiến dịch vùng.

---

## 📅 7. Lộ Trình Triển Khai

| Giai đoạn | Điều kiện | Việc làm | Ngân sách |
|---|---|---|---|
| **Bước 0** | — | Cài GA4 + conversion tracking. Viết nội dung `/pages/info-for-employers` và trang đăng tin. Import 5 negative list. | €0 |
| **Bước 1** | Cổng A xong | Bật `OAJ-Employers-NL` + `OAJ-Brand`. Rà search term mỗi ngày trong 2 tuần. | €440/tháng |
| **Bước 2** | 30 ngày sau Bước 1 | Đánh giá: chi phí trên mỗi tin tuyển dụng thu được. Nếu < €80 thì tăng ngân sách; nếu > €150 thì sửa landing page trước khi chi thêm. | €440–800 |
| **Bước 3** | Cổng B xong (≥120 tin) | Bật `OAJ-Seekers-NL-Role` + `OAJ-Seekers-NL-City`. | +€800/tháng |
| **Bước 4** | Cổng C xong | Bật Remarketing. Cân nhắc PMax. | +€150/tháng |

**Chỉ số quyết định ở Bước 2**: *chi phí trên mỗi tin tuyển dụng mới thu được*. Đây là KPI duy nhất đáng quan tâm ở giai đoạn đầu, vì nguồn cung là nút thắt của toàn bộ mô hình.

---

## 📎 8. Việc Nghiên Cứu Còn Thiếu

| # | Việc | Vì sao cần |
|---|---|---|
| 1 | Chạy Keyword Planner NL + EN, filter Location = Netherlands | Toàn bộ cột Volume/Bid trong tài liệu này đang là `TBD` |
| 2 | Xuất volume theo 20 thành phố lớn nhất NL | Quyết định thành phố nào đáng sinh trang và đáng đấu giá |
| 3 | Google Trends: `ai vacatures` vs `ai jobs` trong lãnh thổ NL | Xác nhận tỷ lệ phân bổ ngân sách NL/EN |
| 4 | Rà Ads Transparency Center: Indeed NL, Nationale Vacaturebank, Techniekwerkt đang đấu giá gì | Biết mặt bằng cạnh tranh thật |
| 5 | Xác minh giá đăng tin sau tin miễn phí đầu tiên | Không có giá thì không tính được ROI của AG-E1/E2 |

---

*Tài liệu liên quan: [`google_ads_rsa_copy_onlyaijobs.md`](./google_ads_rsa_copy_onlyaijobs.md) · [`paid_ads_plan.md`](./paid_ads_plan.md) · [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) · [`implementation_plan.md`](./implementation_plan.md) · [`extra-keywords.md`](./extra-keywords.md)*
