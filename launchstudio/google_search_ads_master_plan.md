# 🎯 Google Search Ads — Master Plan cho LaunchStudio

> **Phạm vi:** Chỉ Google Search Ads (không LinkedIn/Meta/Reddit — xem [`paid_ads_plan.md`](paid_ads_plan.md) nếu cần đa kênh)
> **Ngày:** 2026-09-24 · **Thị trường:** NL/BE (chính) + EU-EN (phụ)
> **Trạng thái:** Kế hoạch thực thi — cần hoàn thành §3 trước khi tiêu euro đầu tiên

---

## 📑 Mục lục

| § | Nội dung |
|---|---|
| [0](#0) | Tổng hợp từ nguồn nào — và tình trạng thật của từng nguồn |
| [1](#1) | Tóm tắt điều hành: 6 quyết định chính |
| [2](#2) | **Kinh tế đơn vị** — con số quyết định plan này có chạy được không |
| [3](#3) | Điều kiện tiên quyết bắt buộc (chặn launch) |
| [4](#4) | Kiến trúc tài khoản |
| [5](#5) | Chi tiết từng campaign |
| [6](#6) | Negative keywords — **gồm danh sách manufacturing/fabrication** |
| [7](#7) | Conversion tracking |
| [8](#8) | Ad extensions |
| [9](#9) | Ngân sách & lộ trình 90 ngày |
| [10](#10) | **KPI** (Key Performance Indicator — chỉ số hiệu suất chính) và ngưỡng quyết định · §10.1.1–10.1.3 chú thích đầy đủ từ viết tắt |
| [11](#11) | Rủi ro |
| [12](#12) | Checklist ngày 1 |

---

<a id="0"></a>
## 0. Tổng hợp từ nguồn nào — và tình trạng thật của từng nguồn

Plan này gộp 8 nguồn trong repo. Nhưng **không phải nguồn nào cũng dùng được như đang có** — phần này nói rõ cái nào tin được, cái nào không.

| Nguồn | Nội dung | Tình trạng | Dùng vào đâu |
|---|---|---|---|
| [`launchstudio_info.md`](launchstudio_info.md) | Brand, giá, **USP** (Unique Selling Proposition — điểm bán hàng độc nhất), persona, Manifera | ✅ Đầy đủ, tin cậy | §2 kinh tế, §5 ad copy |
| [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md) | **RSA** (Responsive Search Ad — quảng cáo tìm kiếm thích ứng): headline/description song ngữ, đã đếm ký tự | ✅ **Tài sản tốt nhất trong repo** | §5 — dùng gần như nguyên |
| [`paid_ads_plan.md`](paid_ads_plan.md) | Cấu trúc campaign, tier ngân sách, landing page, KPI, checklist 90 ngày | ✅ Chi tiết, nhưng đa kênh và dựa trên keyword cũ | §4, §9, §10 — lọc lấy phần Search |
| [`keyword_seeds_google_ads_3_clusters.csv`](keyword_seeds_google_ads_3_clusters.csv) | 129 keyword, 19 ad group, 3 cụm | ✅ Mới, chưa có volume | §5 — keyword chính |
| [`google_ads_keyword_research_3_clusters.md`](google_ads_keyword_research_3_clusters.md) | Volume đã xác minh, 3 bẫy, negative list | ✅ Mới | §2, §6 |
| [`keyword_ideas_round2.csv`](keyword_ideas_round2.csv) | 78 keyword mới từ changelog mining | ✅ Mới, chưa có volume | §5.6 — 21 cái vào ads, 57 cái cho **SEO** (Search Engine Optimization — tối ưu tìm kiếm không trả phí) |
| [`keyword_idea_playbook.md`](keyword_idea_playbook.md) | 20 phương pháp tìm keyword + quy trình lặp hàng tháng | ✅ Mới | §12 — nhịp tháng |
| [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) | 14 production keyword NL/EN | ⚠️ Ước tính volume NL rất thấp (200–600/tháng) | §2 — dùng làm mốc thực tế |
| [`seo_geo_audit_2026-07-31.md`](seo_geo_audit_2026-07-31.md) | Audit site | ⚠️ Phát hiện thiếu schema, one-page | §3 — điều kiện tiên quyết |
| [`google_ads_keywords_launchstudio.md`](google_ads_keywords_launchstudio.md) | Bảng keyword song ngữ 4 ad group | 🔴 **HỎNG — xem dưới** | Chỉ dùng cấu trúc, không dùng nội dung |

### 🔴 0.1. Cảnh báo: file keyword chính đang rỗng

`google_ads_keywords_launchstudio.md` nhìn thì hoàn chỉnh — có bảng, có cột Match Type, Priority, giải nghĩa tiếng Việt. Nhưng:

- **46 ô keyword trống rỗng.** Cả cột `🇬🇧 English Keyword` và `🇳🇱 Dutch Keyword` đều không có chữ nào trong Ad Group 1–4, Brand Keywords, và cả 5 danh sách Negative Keywords.
- **2 dòng bị hỏng** do escape code của vim bị ghi đè vào file (đoạn `[m[m[0m[H[2J...Vim: Error reading input, exiting...` nằm giữa bảng Sitelinks).

Nghĩa là: **cái vẫn được coi là "bảng từ khoá Google Ads của LaunchStudio" thực chất là một template rỗng.** Nếu ai đó mở file này ra định import Google Ads Editor thì sẽ không có gì để import.

➡️ Plan này **thay thế** file đó. Keyword thật nằm ở [`keyword_seeds_google_ads_3_clusters.csv`](keyword_seeds_google_ads_3_clusters.csv). Đề xuất: đổi tên file cũ thành `google_ads_keywords_launchstudio.DEPRECATED.md` để không ai dùng nhầm.

---

<a id="1"></a>
## 1. Tóm tắt điều hành: 6 quyết định chính

### ① Ngân sách cho 3 cụm AI-tool là **€300–900/tháng**, không phải €5.000

Đây là kết luận quan trọng nhất và nó trái ngược với `paid_ads_plan.md` (đề xuất €3.795/tháng cho Google Search EN).

Lý do: **tài khoản này bị giới hạn bởi volume, không phải bởi tiền.** Xem tính toán đầy đủ ở §2.2. Tóm tắt: với lượng tìm kiếm ước tính của 3 cụm, ở mức **IS** (Impression Share — thị phần hiển thị) 65% và **CTR** (Click-Through Rate — tỉ lệ nhấp) 6–9%, bạn chỉ có thể mua được **15–70 click/tháng**. Ở **CPC** (Cost Per Click — chi phí mỗi lượt nhấp) €8–14, đó là €120–1.000/tháng. Đổ €5.000 vào thì €4.000 sẽ không tiêu được, hoặc tệ hơn — Google sẽ tiêu nó vào truy vấn không liên quan.

### ② Chỉ chạy 60/129 keyword

Campaign C1–C3 chỉ lấy keyword intent **Hire, Service, Decision, Compliance** (55 keyword), cộng 5 keyword intent Fix/How-to được cô lập riêng trong campaign thử nghiệm C5 có ngưỡng kill rõ ràng. **25 keyword intent Fix còn lại không chạy ads** — để dành cho SEO, vì người gõ `lovable custom domain not working` muốn fix miễn phí trong 5 phút, không mua gói €800–7.500.

### ③ Không bid broad match trên bất cứ gì chứa `lovable`

`lovable` vừa là tính từ tiếng Anh thông dụng, vừa là thương hiệu đồ lót toàn cầu. Volume 149.500/tháng mà Semrush báo gần như toàn bộ là rác đối với LaunchStudio. Đây là lặp lại y hệt bẫy `day ai` = 201.000 mà `paid_ads_plan.md` §3.1 đã phát hiện.

### ④ Phải tạo 2 landing page trước khi bật campaign

Site hiện là one-page + anchor. Campaign giá trị cao nhất (Security & Cleanup) không có chỗ đổ traffic về. Xem §3.

### ⑤ Ngưỡng sống còn: landing page phải chuyển đổi ≥5% và close rate ≥40%

Ở 3% (mục tiêu KPI trong plan cũ) và CPC €10, **mô hình lỗ**. Xem bảng ở §2.3.

### ⑥ Thêm C6 Migration — cách duy nhất hợp lệ để nâng trần chi tiêu

§2.2 kết luận tài khoản bị chặn bởi volume, và cách duy nhất để tiêu nhiều hơn là **mở rộng bề mặt keyword**. Đợt changelog mining (xem [`keyword_idea_playbook.md`](keyword_idea_playbook.md)) tìm được 78 keyword mới, trong đó **21 cái đủ điều kiện chạy ads**.

Cơ hội mạnh nhất: **Lovable đổi stack mặc định sang TanStack Start** (13/05/2026) và **không tự động migrate dự án cũ**. Mọi dự án tạo trước tháng 5 đang chạy stack cũ, không **SSR** (Server-Side Rendering — kết xuất phía máy chủ, ảnh hưởng trực tiếp tới thứ hạng tìm kiếm). Đối thủ `nextlovable.com` đã bán audit **$199–299** cho đúng việc này với 3 landing page riêng — tức là đã có người trả tiền.

Ngân sách: €900 → **€1.080/tháng**, vẫn dưới trần €1.300.

---

<a id="2"></a>
## 2. Kinh tế đơn vị — con số quyết định plan này có chạy được không

Không có phần này trong bất kỳ file nào hiện có. Đây là phần quan trọng nhất, vì nó trả lời câu hỏi: *chạy ads cho dịch vụ này có lãi không?*

### 2.1. Giá trị đơn hàng (từ `launchstudio_info.md`)

| Gói | Khoảng giá | Trung bình | Ghi chú |
|---|---|---:|---|
| Gói 1 — Launch Ready | €800–3.500 | **€2.150** | Đa số khách mới vào ở gói này |
| Gói 2 — Launch & Grow | €2.500–7.500 | **€5.000** | + €49/tháng hosting |
| **Giả định hỗn hợp thận trọng** | | **€2.500** | Dùng cho mọi tính toán dưới |

### 2.2. 🔴 Trần chi tiêu bị giới hạn bởi volume

Đây là phép tính mà không ai trong repo đã làm. Công thức:

```
Chi tiêu tối đa/tháng = Volume × %kw-hợp-ads × IS × CTR × CPC

(IS = Impression Share — thị phần hiển thị · CTR = Click-Through Rate — tỉ lệ nhấp · CPC = Cost Per Click — chi phí mỗi lượt nhấp)
```

| Thị trường | Volume ước tính/tháng | × 40% kw hợp ads | × 65% IS | × CTR 6–9% | **× CPC €8–14** |
|---|---:|---:|---:|---:|---:|
| NL/BE | 60–250 | 24–100 | 16–65 | 1–6 click | **€7–82** |
| EU-EN | 900–2.800 | 360–1.120 | 234–728 | 14–66 click | **€112–917** |
| **Tổng** | | | | **15–72 click** | **€120–1.000** |

> **Nguồn volume ước tính:** `seo_geo_plan_production_keywords.md` ước tính 14 production keyword ở NL có tổng 200–600 lượt tìm/tháng. `paid_ads_plan.md` sau khi làm sạch CSV: ~13.000/tháng cho toàn bộ tập keyword EN. 3 cụm mới hẹp hơn nhiều so với tập EN cũ. **Đây là ước tính, không phải số đo — phải verify bằng Keyword Planner (§12).**

**Hệ quả thực tế:**

1. Ngân sách Search cho 3 cụm AI-tool: **€300–900/tháng** là hợp lý. Đặt cao hơn thì tiền không tiêu được.
2. Muốn tiêu nhiều hơn thì phải **mở rộng bề mặt keyword** (thêm cụm, thêm geo, thêm brand + competitor), chứ không phải tăng bid.
3. **Đừng dùng Maximize Conversions sớm.** Với 15–70 click/tháng, Google cần 3–6 tháng mới đủ dữ liệu học. Dùng Manual CPC hoặc Maximize Clicks với cap.

### 2.3. 🔴 Bảng nhạy: cần tỉ lệ chuyển đổi bao nhiêu để không lỗ?

Công thức: `CAC = CPC ÷ (Tỉ lệ chuyển đổi landing page × Tỉ lệ chốt deal)`

> **CAC** = Customer Acquisition Cost (chi phí thu hút một khách hàng) · **CPC** = Cost Per Click (chi phí mỗi lượt nhấp) · **LP conv** = Landing Page conversion rate (tỉ lệ chuyển đổi trang đích). Chú thích đầy đủ mọi chỉ số ở §10.1.1.

Mốc đánh giá với deal trung bình €2.500, biên lợi nhuận gộp giả định 50%:
- **CAC mục tiêu lành mạnh:** ≤ €625 (25% doanh thu)
- **CAC hoà vốn:** €1.250 (bằng toàn bộ lợi nhuận gộp)
- **Trên €1.250:** lỗ trên deal đầu tiên

| CPC | LP conv | Close rate | **CAC** | Đánh giá |
|---:|---:|---:|---:|---|
| €8 | 3% | 25% | €1.067 | 🟡 Căng — gần hoà vốn |
| €8 | 3% | 40% | €667 | 🟡 Căng |
| €8 | 5% | 25% | €640 | 🟡 Căng |
| €8 | **5%** | **40%** | **€400** | ✅ **OK** |
| €8 | 8% | 25% | €400 | ✅ OK |
| €8 | 8% | 40% | €250 | ✅ Rất tốt |
| €10 | **3%** | **25%** | **€1.333** | 🔴 **LỖ** |
| €10 | 3% | 40% | €833 | 🟡 Căng |
| €10 | 5% | 25% | €800 | 🟡 Căng |
| €10 | **5%** | **40%** | **€500** | ✅ **OK** |
| €10 | 8% | 25% | €500 | ✅ OK |
| €14 | 3% | 25% | €1.867 | 🔴 LỖ nặng |
| €14 | 5% | 25% | €1.120 | 🟡 Căng |
| €14 | 8% | 40% | €438 | ✅ OK |

**Ba kết luận rút ra:**

1. **Mục tiêu "landing page conversion >3%" trong `paid_ads_plan.md` §12 là quá thấp cho mô hình này.** Ở 3% và CPC €10 thì lỗ. Phải nâng mục tiêu lên **≥5%**.
2. **Close rate là đòn bẩy mạnh hơn CPC.** Đi từ 25% → 40% giảm CAC 37%. Nghĩa là: đầu tư vào quy trình bán (phản hồi nhanh, gọi tư vấn 15 phút, báo giá trong 24h) có tác động lớn hơn tối ưu bid.
3. **Nếu chỉ bán được Gói 1 (€2.150)**, biên an toàn rất mỏng. Ads nên được dùng để **mở cửa quan hệ**, rồi upsell lên Gói 2 (€5.000) + hosting €49/tháng. **LTV** (Lifetime Value — giá trị trọn đời khách hàng) mới là cái biện minh cho CAC.

### 2.4. Mục tiêu cần đặt ra

| Chỉ số | Mục tiêu | Lý do |
|---|---|---|
| CPC trung bình | ≤ €10 | Trên mức này biên lợi nhuận quá mỏng |
| LP conversion (click → lead) | **≥ 5%** | Ngưỡng sống còn theo §2.3 |
| Lead → khách | ≥ 30% | Đòn bẩy mạnh nhất |
| CAC | ≤ €625 | 25% deal trung bình |
| Lead/tháng | 3–8 | Từ 15–72 click ở 5–10% |
| Khách/tháng | 1–3 | Ở close rate 30% |

➡️ **Kỳ vọng thực tế: 1–3 khách/tháng từ Google Search.** Với deal €2.500–5.000, đó là €2.500–15.000 doanh thu/tháng từ chi phí €300–900. Đây là tỉ lệ tốt — nhưng **chỉ khi** landing page và quy trình bán đạt ngưỡng ở §2.3.

---

<a id="3"></a>
## 3. Điều kiện tiên quyết bắt buộc (chặn launch)

**Không bật campaign nào cho đến khi xong hết 6 mục này.** Mỗi mục đều là lý do trực tiếp làm đốt tiền.

| # | Việc | Tại sao chặn | Nguồn |
|---|---|---|---|
| **1** | **Tạo landing page `/en/ai-code-security-audit`** | Campaign giá trị cao nhất (C3) hiện không có đích. Đổ traffic `vibe code audit` về homepage đa mục đích → Quality Score thấp → CPC cao hơn 30–50% | `paid_ads_plan.md` §11.2 đã có outline sẵn |
| **2** | **Tạo landing page `/en/from-prototype-to-production`** + bản NL `/nl/van-prototype-naar-productie` | Đích cho C1, C2 | `paid_ads_plan.md` §11.1, §11.3 |
| **3** | **Cài GA4** (Google Analytics 4) **+ 3 conversion event**: `calculator_complete`, `contact_form_submit`, `call_booked` | Không có conversion tracking = không biết campaign nào lãi = tối ưu mù | §7 |
| **4** | **Import conversion vào Google Ads** và đánh dấu Primary | Smart Bidding và báo cáo đều cần | §7 |
| **5** | **Thêm `Organization` schema + sửa author schema** | Audit 2026-07-31 phát hiện **không có `Organization` schema ở bất kỳ đâu**, author schema đang là `"phu.lt"`. Ảnh hưởng trust signal và Quality Score gián tiếp | `seo_geo_audit_2026-07-31.md` |
| **6** | **Tạo Shared Negative List** (§6) trước khi campaign chạy phút đầu tiên | Bẫy `lovable` = đồ lót/từ điển sẽ đốt ngân sách ngay ngày 1 | §6 |

**Thời gian ước tính:** 1–2 tuần nếu có dev. Landing page là phần lâu nhất.

> 💡 **Nếu gấp:** có thể launch C1 (NL) trước vì nó trỏ về `/nl/van-prototype-naar-productie` — page này gần nhất với nội dung homepage hiện tại. Nhưng C3 thì **không** được bật trước khi có page riêng.

---

<a id="4"></a>
## 4. Kiến trúc tài khoản

### 4.1. Nguyên tắc thiết kế

1. **Một ad group = một intent.** Không trộn `fix lovable app` (Hire) với `lovable security vulnerabilities` (Research) — ad copy sẽ không khớp được cả hai.
2. **Một ad group = một landing page.** Quyết định message match.
3. **Tách NL và EN thành campaign riêng**, không dùng ad group riêng. Lý do: ngân sách, bid, và ngôn ngữ ad khác nhau hoàn toàn; gộp chung thì EN volume sẽ nuốt hết ngân sách của NL.
4. **Campaign brand tách riêng** với ngân sách nhỏ, Target Impression Share 95–100%.

### 4.2. Sơ đồ

```
TÀI KHOẢN LaunchStudio
│
├── C1 · LS-Search-NL-Service          [NL/BE · Dutch · €200/thg]
│   ├── AG-NL-Rescue        (6 kw)  → /nl/van-prototype-naar-productie
│   ├── AG-NL-Security      (6 kw)  → /nl/beveiligingsaudit-ai-app
│   └── AG-NL-Vibe          (3 kw)  → /nl/van-prototype-naar-productie
│
├── C2 · LS-Search-EN-Hire             [EU-EN · English · €250/thg]
│   ├── AG-LOV-Hire         (10 kw) → /en/from-prototype-to-production
│   ├── AG-VIBE-Hire        (6 kw)  → /en/from-prototype-to-production
│   └── AG-TOOL-Hire        (4 kw)  → /en/from-prototype-to-production
│       (fix bolt app, fix replit app, bolt app developer, replit app to production)
│
├── C3 · LS-Search-EN-Security         [EU-EN · English · €300/thg]
│   ├── AG-SEC-Cleanup      (10 kw) → /en/ai-code-security-audit
│   ├── AG-SEC-Audit        (7 kw)  → /en/ai-code-security-audit
│   └── AG-SEC-Compliance   (3 kw)  → /en/ai-code-security-audit
│
├── C4 · LS-Search-Brand               [NL+EU · cả 2 ngôn ngữ · €50/thg]
│   └── AG-Brand            (4 kw)  → /en/ hoặc /
│
├── C5 · LS-Search-EN-FixTest          [EU-EN · TUỲ CHỌN · €100/thg]
│   └── AG-FIX-Test         (5 kw exact) → /en/from-prototype-to-production
│       ⚠️ Chỉ bật sau khi C2/C3 chạy ổn 4 tuần. Kill nếu **CPL** (Cost Per Lead — chi phí mỗi khách tiềm năng) > €400.
│
└── C6 · LS-Search-EN-Migration        [EU-EN · €180/thg · CỤM MỚI]
    ├── AG-MIG-TanStack     (6 kw)  → /en/lovable-tanstack-migration
    ├── AG-MIG-Service      (4 kw)  → /en/from-prototype-to-production
    └── AG-MIG-Platform     (6 kw)  → /en/from-prototype-to-production
```

**Tổng: €1.080/tháng ở cấu hình đầy đủ** — vẫn dưới trần volume €1.300 ở §2.2.

> 📌 Ngoài ra: **+3 keyword** vào `AG-TOOL-Hire` (C2) và **+2 keyword** vào `AG-SEC-Tool` (C3) — xem §5.6.4.

---

<a id="5"></a>
## 5. Chi tiết từng campaign

### 5.1. C1 · `LS-Search-NL-Service` — €200/tháng (€6,50/ngày)

> **Tại sao ưu tiên NL:** đây là thị trường chính của LaunchStudio, CPC thấp hơn EU-EN, cạnh tranh gần như bằng 0 cho các từ như `code audit laten uitvoeren`. `paid_ads_plan.md` gọi đây là "the biggest untapped opportunity" — mình đồng ý.

| Ad group | Keyword (match type) | Max CPC | Ngày | Landing page |
|---|---|---:|---:|---|
| `AG-NL-Rescue` | `"prototype naar productie"`, `"ai app laten bouwen"`, `"ai app laten afmaken"`, `"mvp laten bouwen"`, `"prototype live zetten"`, `"app productieklaar maken"` | €6,00 | €3,00 | `/nl/van-prototype-naar-productie` |
| `AG-NL-Security` | `"beveiligingsaudit webapplicatie"`, `"code audit laten uitvoeren"`, `"security audit software laten doen"`, `"avg compliance app"`, `"pentest webapplicatie"`, `"applicatie beveiliging laten testen"` | €7,00 | €2,50 | `/nl/beveiligingsaudit-ai-app` |
| `AG-NL-Vibe` | `"vibe coding nederland"`, `"vibe coding beveiliging"`, `"vibe coding uitbesteden"` | €5,00 | €1,00 | `/nl/van-prototype-naar-productie` |

**RSA:** dùng nguyên cột Dutch trong [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md) Ad Group 1 — đã đếm ký tự sẵn, đã có pin strategy. Ví dụ:

- H1 (P1): `MVP Laten Bouwen?` (18)
- H2 (P2): `Wij Maken Het Launch-Ready` (26)
- H3: `Vaste Prijs Vanaf €800` (22)
- H4: `Live Binnen 1-3 Weken` (21)
- H10 (P3): `Gratis Offerte Binnen 1 Dag` (27)
- D1: `AI-prototype klaar maar niet live? We fixen security, hosting & Stripe. Vraag offerte aan!` (90)

⚠️ **Bắt buộc:** cho người Hà Lan bản xứ đọc lại toàn bộ ad copy NL trước khi chạy. Đây là ghi chú đã có trong `paid_ads_plan.md` §13 tuần 2 và vẫn đúng.

---

### 5.2. C2 · `LS-Search-EN-Hire` — €250/tháng (€8/ngày)

| Ad group | Keyword | Max CPC | Ngày |
|---|---|---:|---:|
| `AG-LOV-Hire` | `"fix lovable app"`, `"lovable developer for hire"`, `"lovable developer"`, `[hire lovable developer]`, `"lovable app development service"`, `"take my lovable app to production"`, `"lovable app production ready"`, `"finish my lovable app"`, `"lovable app agency"`, `"lovable freelancer"` | €10,00 | €3,50 |
| `AG-VIBE-Hire` | `"hire vibe coding developer"`, `"vibe coding agency"`, `"fix my vibe coded app"`, `"vibe coding help"`, `"vibe coding consultant"`, `"vibe coding development service"` | €10,00 | €3,00 |
| `AG-TOOL-Hire` | `"fix bolt app"`, `"fix replit app"`, `"bolt app developer"`, `"replit app to production"` | €8,00 | €1,50 |

**Landing page:** `/en/from-prototype-to-production`

#### ⚠️ 5.2.1. Vấn đề cạnh tranh phải giải quyết trong ad copy

**SERP** (Search Engine Results Page — trang kết quả tìm kiếm) và marketplace cho `fix lovable app`, `fix bolt app`, `lovable developer for hire` đang bị **Fiverr/Upwork chiếm với gig $10–30**. LaunchStudio bán €800–7.500 — chênh 30–200 lần.

**Nếu ad copy chỉ nói "we fix your Lovable app" thì bạn đang mời người dùng so sánh giá — và bạn thua.**

Ad copy C2 phải làm ba việc, theo thứ tự:

1. **Tái định nghĩa vấn đề** từ "sửa lỗi" sang "rủi ro bảo mật + không go-live được"
2. **Neo vào bằng chứng** — theo nghiên cứu được Superblocks dẫn lại, quét 1.645 project Lovable công khai phát hiện **~170 (10,3%) thiếu Row Level Security**, làm lộ 303 endpoint chứa tên, email, số điện thoại, địa chỉ, thông tin thanh toán và API key của bên thứ ba
3. **Dựa vào entity Manifera** — 11+ năm, 160+ dự án, khách hàng Vodafone / TNO / CFLW

**RSA đề xuất cho `AG-LOV-Hire`** (dựa trên Ad Group 2 của file RSA copy, chỉnh lại góc):

| # | Headline | Ch | Pin |
|---|---|---:|---|
| H1 | `Lovable App Not Production Ready?` | 30 | P1 |
| H2 | `We Fix Security, Not Just Bugs` | 29 | P2 |
| H3 | `1 in 10 Lovable Apps Leak Data` | 29 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `We Keep Your Frontend` | 21 | |
| H7 | `Backed by 11+ Yrs Engineering` | 29 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Trusted by Vodafone & TNO` | 25 | |
| H10 | `Get a Free Code Review` | 22 | P3 |

| # | Description | Ch |
|---|---|---:|
| D1 | `A $25 gig fixes a bug. We fix the RLS gap that leaks your users' data. Free review.` | 83 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 84 |
| D3 | `Built by Manifera engineers — 160+ projects for Vodafone, TNO, CFLW. Get a quote.` | 82 |

---

### 5.3. C3 · `LS-Search-EN-Security` — €300/tháng (€10/ngày)

> **Campaign giá trị cao nhất.** Intent thương mại rõ ràng nhất trong ba cụm AI-tool: `vibe coding cleanup specialist` có **ít nhất 4 agency đã xây landing page riêng** (Redwerk, Suffescom, ThirdRock, AleaIT) — nghĩa là có người đang bỏ tiền đi rank, tức là có người mua.

| Ad group | Keyword | Max CPC | Ngày |
|---|---|---:|---:|
| `AG-SEC-Cleanup` | `"vibe coding cleanup specialist"`, `"vibe code cleanup"`, `"vibe code audit"`, `"vibe coding rescue"`, `"clean up ai generated code"`, `"refactor ai generated code"`, `"fix ai generated code"`, `"ai code cleanup service"`, `"rescue failed mvp"`, `"mvp rescue service"` | €12,00 | €4,50 |
| `AG-SEC-Audit` | `"ai app security audit"`, `"ai generated code security audit"`, `"ai code security review"`, `"web app security audit"`, `"production readiness audit"`, `"code audit service"`, `"technical due diligence code audit"` | €12,00 | €4,00 |
| `AG-SEC-Compliance` | `"gdpr ai app"`, `"gdpr compliance web application"`, `"owasp llm top 10"` | €8,00 | €1,50 |

**Landing page:** `/en/ai-code-security-audit` — **bắt buộc phải tồn tại trước khi bật.**

**RSA:** dùng `paid_ads_plan.md` §5.2 làm gốc, thêm số liệu:

| # | Headline | Ch | Pin |
|---|---|---:|---|
| H1 | `Is Your AI-Built App Secure?` | 28 | P1 |
| H2 | `Fixed-Price Security Audit` | 26 | P2 |
| H3 | `45% of AI Code Has Flaws` | 25 | |
| H4 | `RLS, Keys, Auth, Rate Limits` | 28 | |
| H5 | `Report in Days, Not Weeks` | 25 | |
| H6 | `11+ Years in Cybersecurity` | 26 | |
| H7 | `Built for Lovable & Supabase` | 28 | |
| H8 | `Ready for Investor Due Dil.` | 27 | |
| H9 | `Get Your Free Scan Quote` | 24 | P3 |

> **Về con số 45%:** đây là thống kê trên chính website LaunchStudio (`launchstudio_info.md` §2.1: *"45% of AI-generated code has security vulnerabilities"*). Trước khi dùng trong ad, **hãy xác minh nguồn gốc của con số này** — Google Ads có chính sách về claim không có căn cứ, và nếu con số đến từ một nghiên cứu cụ thể thì nên trích được nguồn trên landing page.

**Góc "due diligence" đáng khai thác riêng:** `technical due diligence code audit` và `code audit before investor due diligence` nhắm vào founder **sắp gọi vốn** — thời điểm họ có ngân sách và có deadline. Đây là đối tượng sẵn sàng trả Gói 2 (€5.000) nhất.

---

### 5.4. C4 · `LS-Search-Brand` — €50/tháng

| Keyword | Match | Max CPC |
|---|---|---:|
| `[launchstudio]`, `[launch studio]` | Exact | €2,00 |
| `"launchstudio eu"`, `"launchstudio review"`, `"launchstudio vs"` | Phrase | €2,50 |
| `"launch studio manifera"` | Phrase | €2,00 |

**Bid strategy:** Target Impression Share 95%, vị trí Absolute Top.
**Lý do chạy:** rẻ, bảo vệ thương hiệu khỏi đối thủ bid chen vào, và bắt traffic từ 800+ bài blog đang dẫn về brand.

---

### 5.5. C5 · `LS-Search-EN-FixTest` — €100/tháng (TUỲ CHỌN)

> **Chỉ bật sau khi C2/C3 đã chạy ổn định 4 tuần.** Đây là thử nghiệm có kiểm soát cho giả thuyết "người đang kẹt lỗi cũng có thể mua dịch vụ".

| Keyword (Exact only) | Max CPC |
|---|---:|
| `[lovable stripe integration]` | €8,00 |
| `[lovable stripe not working]` | €8,00 |
| `[migrate off lovable]` | €9,00 |
| `[lovable export code]` | €7,00 |
| `[self host lovable app]` | €7,00 |

**Quy tắc kill:** sau 4 tuần, nếu CPL > €400 hoặc 0 conversion với chi > €150 → tắt vĩnh viễn và chuyển toàn bộ 30 keyword intent Fix sang kế hoạch SEO.

---

---

### 5.6. C6 · `LS-Search-EN-Migration` — €180/tháng (€6/ngày)

> **Cụm mới từ changelog mining.** 21 keyword được chọn từ 78 keyword mới — xem [`keyword_ideas_round2.csv`](keyword_ideas_round2.csv) và phương pháp ở [`keyword_idea_playbook.md`](keyword_idea_playbook.md) §9.

#### 5.6.1. Vì sao cụm này đáng làm ngay

Lovable đổi stack mặc định từ **React + Vite → TanStack Start**: mặc định cho dự án mới từ **13/05/2026**, Enterprise từ **22/06/2026**. Lovable **không tự động migrate dự án cũ**.

Ba hệ quả tạo ra nhu cầu tìm kiếm:

1. Mọi dự án tạo trước 05/2026 vẫn chạy stack cũ — và chủ sở hữu thường **không biết điều đó**
2. Stack cũ không có SSR → ảnh hưởng trực tiếp tới SEO, một nỗi đau mà nhiều founder đã cảm thấy nhưng chưa biết nguyên nhân
3. Migration là việc kỹ thuật, không phải prompt — đúng định nghĩa "last-mile" của LaunchStudio

**Xác minh thương mại:** `nextlovable.com` bán audit **$199** (`/lovable-tanstack-ssr`) và **$299** (`/migrate-lovable-tanstack`), cộng một trang `/migration-guide`. Ba landing page cho một vấn đề = họ đang kiếm được tiền từ nó.

⏳ **Tính thời sự:** cửa sổ này sẽ đóng khi Lovable tự migrate hoặc khi dự án cũ chết dần. Ước tính còn **6–12 tháng**.

#### 5.6.2. Ad group & keyword

| Ad group | Keyword | Max CPC | Ngày | Landing page |
|---|---|---:|---:|---|
| `AG-MIG-TanStack` | `"lovable tanstack migration"`, `"migrate lovable to tanstack"`, `"lovable tanstack migration service"`, `"lovable ssr upgrade"`, `"upgrade lovable project tanstack"`, `[lovable tanstack start]` | €10,00 | €3,00 | `/en/lovable-tanstack-migration` |
| `AG-MIG-Service` | `"lovable migration service"`, `"lovable audit service"`, `"nextlovable"`, `"nextlovable alternative"` | €10,00 | €1,50 | `/en/from-prototype-to-production` |
| `AG-MIG-Platform` | `"lovable cloud vs supabase"`, `"lovable payments vs stripe"`, `"lovable cloud pricing"`, `"lovable payments fees"`, `"paddle vs stripe for saas"`, `"do i need lovable cloud"` | €8,00 | €1,50 | `/en/from-prototype-to-production` |

> **Về 4 keyword được nâng hạng:** `lovable ssr upgrade`, `upgrade lovable project tanstack` và `lovable tanstack start` mang intent How-to/Research theo phân loại gốc, nên lẽ ra thuộc nhóm SEO. Mình nâng lên ads vì **nextlovable đang bán audit trả phí cho đúng các truy vấn đó** — bằng chứng thương mại thắng nhãn intent. `[lovable tanstack start]` để **Exact** vì là head term.

#### 5.6.3. ⚠️ Bid tên đối thủ — đọc trước khi bật

`nextlovable` và `vibeappscanner` là **tên thương hiệu đối thủ**. Bid vào chúng là hợp pháp ở EU nhưng có ba ràng buộc:

1. **Không được dùng tên đối thủ trong ad copy** — Google cho phép bid nhưng cấm dùng nhãn hiệu trong text quảng cáo nếu chủ sở hữu đã khiếu nại. Giữ headline trung tính: `"Lovable Migration Done Right"`, không phải `"Better Than NextLovable"`.
2. **Quality Score sẽ thấp** → CPC cao hơn. Chấp nhận, đây là cụm nhỏ.
3. **Có thể bị trả đũa** — họ sẽ bid ngược lại `launchstudio`. C4 Brand (§5.4) tồn tại chính để phòng việc này.

Nếu không muốn rủi ro, bỏ 2 keyword này — 19 keyword còn lại vẫn đủ.

#### 5.6.4. Keyword thêm vào campaign có sẵn

| Vào đâu | Keyword | Lý do |
|---|---|---|
| **C2 → `AG-TOOL-Hire`** | `"v0 to production"`, `"base44 to production"`, `"figma make to production"` | Cùng intent Hire, cùng landing page. CSV hiện chỉ phủ Lovable/Bolt/Cursor/Replit — thị trường đã rộng hơn |
| **C3 → `AG-SEC-Tool`** | `"lovable security scanner"`, `"vibeappscanner"` | Người tìm công cụ quét bảo mật = người biết mình có vấn đề bảo mật |

#### 5.6.5. Landing page mới cần cho C6

| URL | Bắt buộc? | Nội dung |
|---|---|---|
| `/en/lovable-tanstack-migration` | **Nên có** | Giải thích stack cũ vs mới · cách tự kiểm tra dự án mình đang ở stack nào · hệ quả SEO của việc thiếu SSR · giá cố định · **CTA** (Call To Action — lời kêu gọi hành động) báo giá |

⚠️ **Không phải điều kiện chặn.** Có thể bật `AG-MIG-TanStack` trỏ tạm về `/en/from-prototype-to-production` trong 2–4 tuần đầu để đo volume thật. Nhưng nếu cụm cho tín hiệu tốt thì phải làm page riêng — message match quyết định Quality Score và tỉ lệ chuyển đổi.

#### 5.6.6. RSA đề xuất — `AG-MIG-TanStack`

| # | Headline | Ch | Pin |
|---|---|---:|---|
| H1 | `Lovable App Still on Vite?` | 26 | P1 |
| H2 | `We Handle the TanStack Move` | 28 | P2 |
| H3 | `No SSR = No Google Ranking` | 27 | |
| H4 | `Fixed Price, No Surprises` | 25 | |
| H5 | `Your Frontend Stays Intact` | 27 | |
| H6 | `Done in Days, Not Sprints` | 25 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Keep 100% of the Code` | 25 | |
| H9 | `Free Migration Assessment` | 25 | P3 |

| # | Description | Ch |
|---|---|---:|
| D1 | `Lovable switched to TanStack Start in May 2026. Older projects were not migrated.` | 80 |
| D2 | `No SSR means search engines see an empty page. We migrate and keep your UI intact.` | 82 |
| D3 | `Fixed price, code stays yours, built by Manifera engineers. Get a free assessment.` | 82 |

> ⚠️ Câu `Lovable switched to TanStack Start in May 2026` là tuyên bố thực tế về sản phẩm bên thứ ba. Mình lấy từ tài liệu Lovable, nhưng **hãy xác minh lại ngày trước khi chạy** — quảng cáo sai sự thật về sản phẩm khác là rủi ro chính sách và pháp lý.

#### 5.6.7. 57 keyword còn lại — backlog SEO, không chạy ads

Trong 78 keyword mới, **57 cái mang intent How-to / Research / Fix** → không phù hợp paid search theo đúng logic ở §2.3, nhưng **rất phù hợp SEO** vì cạnh tranh gần như bằng 0 (nhiều tính năng mới ra tháng 7–9/2026).

| Nhóm | Số kw | Ghi chú |
|---|---:|---|
| Connector mới (WhatsApp, Power BI, Cloudflare, Mapbox, PostHog, Xero…) | 14 | Gom 1 bài tổng, tách bài riêng nếu có tín hiệu |
| Lovable Cloud (scaling, storage, pressure) | 5 | Surface hạ tầng mới |
| MCP & Agents | 6 | Chưa ai viết |
| Enterprise/bảo mật (SSO, SCIM, 2FA, Trust Center) | 7 | Nối với cụm ③ |
| FAQ cộng đồng (favicon, mobile layout, drafts…) | 6 | Dễ viết, volume ổn định |
| Paddle/Payments dạng How-to & Fix | 7 | |
| TanStack dạng Research | 6 | |
| Công cụ khác (Base44, Windsurf, Firebase Studio…) | 6 | |

➡️ Đưa vào lịch nội dung, không vào Google Ads. Xem quy trình lặp ở [`keyword_idea_playbook.md`](keyword_idea_playbook.md) Phần C.

---

<a id="6"></a>
## 6. Negative keywords

### 6.1. Shared list #1 — `lovable` disambiguation (ưu tiên tuyệt đối)

Áp dụng cho **tất cả** campaign. Đây là thứ chặn bẫy lớn nhất của tài khoản này.

```
-bra          -bras         -lingerie     -underwear    -intimates
-panties      -meaning      -definition   -synonym      -synonyms
-antonym      -quotes       -quote        -song         -songs
-lyrics       -lyric        -movie        -film         -book
-novel        -doll         -plush        -toy          -baby
-babies       -pet          -pets         -dog          -cat
-name         -names        -spelling     -loveable
```

### 6.2. Shared list #2 — lọc người không mua

```
-free         -gratis       -tutorial     -tutorials    -course
-courses      -learn        -learning     -training     -certification
-jobs         -job          -vacature     -salary       -career
-internship   -stage        -download     -crack        -cracked
-torrent      -reddit       -youtube      -github       -template
-templates    -coupon       -promo        -discount     -open source
-day
```

> `-day` kế thừa từ `paid_ads_plan.md` §3.1 để chặn bẫy `day ai` = 201.000/tháng.

### 6.3. 🔴 Shared list #3 — Manufacturing / Fabrication (quan trọng hơn vẻ ngoài)

#### Tại sao cần danh sách này

Đây không phải negative "cho chắc". Định vị cốt lõi của LaunchStudio **trùng trực tiếp** với thuật ngữ chuẩn của ngành sản xuất:

| Từ trong keyword của bạn | Nghĩa trong phần mềm | Nghĩa trong sản xuất |
|---|---|---|
| **prototype** | bản dựng app bằng AI | mẫu vật lý: 3D print, CNC, mockup |
| **production** / **productie** | môi trường chạy thật | dây chuyền sản xuất hàng loạt |
| **prototype to production** | đưa app lên live | **NPI/DFM — đưa sản phẩm vật lý vào sản xuất loạt** |
| **build** / **bouwen** | lập trình | chế tạo, xây dựng |
| **custom / op maat** | phần mềm riêng | gia công theo đơn |
| **launch** | ra mắt app | ra mắt sản phẩm vật lý |

`prototype naar productie` và `prototype to production` — hai keyword trung tâm của C1 và C2 — là **cụm từ chuẩn trong ngành hardware**. Người tìm chúng có thể đang cần xưởng CNC, dịch vụ in 3D, hoặc nhà máy gia công hợp đồng, chứ không cần ai sửa app Lovable.

Với tài khoản chỉ mua được 15–72 click/tháng (§2.2), **vài click lệch ở CPC €10–14 đã là 2–5% ngân sách tháng**. Đây là danh sách có tác động lớn nhất trong §6.

#### 6.3.1. Vật liệu

```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```

#### 6.3.2. Gia công & chế tạo

```
-cnc          -frezen       -freesmachine -milling      -draaien
-draaibank    -turning      -verspanen    -verspaning   -machining
-lasersnijden -lasersnijden -laser        -waterjet     -plasma
-zetten       -kanten       -bending      -buigen       -lassen
-welding      -laswerk      -plaatwerk    -sheet        -metaalbewerking
-gieten       -casting      -spuitgieten  -injection    -molding
-moulding     -extrusie     -extrusion    -matrijs      -matrijzen
-mold         -mould        -tooling      -stansen      -stamping
-ponsen       -slijpen      -grinding     -polijsten    -anodiseren
-anodizing    -poedercoaten -coating      -galvaniseren -stralen
-fabricage    -fabrication  -fabricatie
```

#### 6.3.3. In 3D / additive

```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```

> ⚠️ **Cân nhắc `-3d` ở dạng broad.** Nó chặn cả `3d` đứng một mình. Nếu LaunchStudio có khách làm app có mô hình 3D (configurator, viewer), thì bỏ `-3d` và chỉ giữ các cụm 2 từ.

#### 6.3.4. Prototyping vật lý — khối quan trọng nhất

```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```

#### 6.3.5. Doanh nghiệp sản xuất

```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```

#### 6.3.6. Mua/thuê máy móc

```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```

#### 6.3.7. Phần mềm CAD/CAM (danh mục phần mềm khác)

```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

#### 6.3.8. Nhà cung cấp ERP ngành (người tìm đối thủ, không phải tìm bạn)

```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```

#### 6.3.9. Xây dựng & gevelbouw

```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```

#### 6.3.10. Lưu ý kỹ thuật khi nhập vào Google Ads

1. **Negative keyword KHÔNG tự khớp biến thể gần.** Khác với keyword thường, negative không tự bắt số nhiều, lỗi chính tả hay dấu. Phải nhập riêng: `-machine` **và** `-machines`, `-matrijs` **và** `-matrijzen`.
2. **Từ đơn → negative broad; cụm nhiều từ → negative phrase.** `-cnc` để broad sẽ chặn mọi truy vấn có "cnc". `"-rapid prototyping"` để phrase.
3. **Negative broad yêu cầu tất cả các từ cùng xuất hiện.** `-machine kopen` dạng broad chỉ chặn truy vấn có **cả hai** từ. Muốn chặn chắc thì để phrase.
4. **Áp ở cấp tài khoản** (Shared Library → Negative keyword lists), không phải từng campaign — vì rủi ro `prototype`/`production` áp dụng cho mọi campaign.
5. **Kiểm tra trước khi áp:** dùng Keyword Planner hoặc Search Terms Report để chắc chắn không có negative nào chặn nhầm truy vấn tốt. Ví dụ `-coating` có thể chặn `coating software` — nếu đó là khách tiềm năng thì bỏ.

### 6.4. Negative riêng theo campaign

| Campaign | Thêm |
|---|---|
| C1 (NL) | `-engels`, `-english`, `-vacature`, `-cursus`, `-opleiding` |
| C2 (Hire) | `-fiverr`, `-upwork`, `-freelancer.com`, `-hourly rate`, `-cheap`, `-goedkoop`, `-india`, `-pakistan` |
| C3 (Security) | `-antivirus`, `-vpn`, `-firewall`, `-malware`, `-soc 2`, `-iso 27001` *(bỏ 2 cái cuối nếu LaunchStudio có cung cấp)* |
| C5 (Fix) | `-how to`, `-guide`, `-step by step`, `-documentation`, `-docs`, `-forum` |

### 6.5. Quy trình negative liên tục

**Tuần 1–4: kiểm tra Search Terms Report mỗi 2 ngày.** Sau đó mỗi tuần.

Với tài khoản volume thấp như thế này, một truy vấn rác tốn €14 đã là 2% ngân sách tháng. Không được để trôi.

---

<a id="7"></a>
## 7. Conversion tracking

Không có phần này thì mọi thứ ở §2 và §10 đều vô nghĩa.

### 7.1. Ba conversion action cần tạo

| Tên | Loại | Giá trị gán | Đếm | Primary? |
|---|---|---:|---|---|
| `contact_form_submit` | Lead | €150 | One | ✅ Primary |
| `call_booked` | Lead | €250 | One | ✅ Primary |
| `calculator_complete` | Micro | €25 | One | ❌ Secondary |

> **Về giá trị gán:** đây là *giá trị ước tính của một lead*, không phải doanh thu. Cách tính: deal trung bình €2.500 × close rate giả định. Nếu 1 lead form chốt 10% → €250. Đặt €150 để thận trọng ở giai đoạn đầu, chỉnh lại sau 3 tháng khi có dữ liệu thật.

### 7.2. Thiết lập

1. **GA4** → tạo 3 event trên → đánh dấu là Key Event
2. **Import vào Google Ads** (Tools → Conversions → Import → GA4)
3. **Bật Enhanced Conversions** — với volume thấp, mỗi conversion đều quý, không được mất do chặn cookie
4. **Consent Mode v2** — bắt buộc ở EU. Không có thì dữ liệu conversion sẽ thiếu hụt nghiêm trọng ở thị trường NL
5. **Offline conversion import** (từ tháng thứ 2): khi một lead thành khách hàng thật, upload ngược lại với **GCLID** (Google Click Identifier — mã định danh lượt nhấp) + doanh thu thật. Đây là cách duy nhất để biết campaign nào mang khách **thật**, không chỉ lead

### 7.3. Đo cả chất lượng, không chỉ số lượng

Với 3–8 lead/tháng, một lead rác cũng làm lệch toàn bộ thống kê. Đề xuất: gắn thêm 1 field bắt buộc trong form — *"Bạn đã có prototype chưa?"* (Có / Chỉ có thiết kế / Chỉ có ý tưởng). Lead chọn "Có" mới tính là qualified.

---

<a id="8"></a>
## 8. Ad extensions

File RSA copy đã có sẵn khung; dưới đây là bản đã điền, khớp với plan này.

### 8.1. Sitelinks (4 cái, bắt buộc)

| # | EN | NL | URL |
|---|---|---|---|
| 1 | `Packages & Pricing` | `Pakketten & Prijzen` | `/en/#packages` |
| 2 | `Free Price Calculator` | `Gratis Prijscalculator` | `/en/#calculator` |
| 3 | `Security Audit` | `Beveiligingsaudit` | `/en/ai-code-security-audit` |
| 4 | `How It Works` | `Zo Werkt Het` | `/en/#process` |

### 8.2. Callouts

- **EN:** `Fixed Price From €800` · `Live in 1-3 Weeks` · `You Own 100% Code` · `No Rebuild Needed` · `11+ Years Experience`
- **NL:** `Vaste Prijs Vanaf €800` · `Live in 1-3 Weken` · `100% Code Eigendom` · `Geen Herbouw` · `11+ Jaar Ervaring`

### 8.3. Structured snippets

- **Services / Diensten:** Security · Payments · Authentication · Database · Hosting · Deployment
- **Types:** Website · Webshop · SaaS · Mobile App · Dashboard · Internal Tool

### 8.4. Price extension

| Gói | Giá | Mô tả |
|---|---|---|
| Launch Ready | từ €800 | Security, auth, database, live op eigen domein |
| Launch & Grow | từ €2.500 | + Stripe payments, managed hosting, monitoring |
| Managed Hosting | €49/mnd | SSL, backups, uptime monitoring, security updates |

### 8.5. Nên bật thêm

- **Call extension** — nếu có số điện thoại NL. Với **B2B** (Business-to-Business — doanh nghiệp bán cho doanh nghiệp) dịch vụ, gọi trực tiếp chuyển đổi cao hơn form.
- **Lead form extension** — cân nhắc, nhưng chất lượng lead thường thấp hơn landing page. Test riêng, đừng trộn.
- **Location extension** — Herengracht 420, Amsterdam. Tăng trust cho thị trường NL đáng kể.

---

<a id="9"></a>
## 9. Ngân sách & lộ trình 90 ngày

### 9.1. Ba kịch bản ngân sách

> Khác với `paid_ads_plan.md` (tier €2.500 / €5.000 / €10.000 đa kênh), plan này **chỉ Search** và bị chặn bởi trần volume ở §2.2.

| | **Tier A — Thận trọng** | **Tier B — Đề xuất** | **Tier C — Trần volume** |
|---|---:|---:|---:|
| C1 NL Service | €120 | €200 | €300 |
| C2 EN Hire | €150 | €250 | €350 |
| C3 EN Security | €180 | €300 | €450 |
| C4 Brand | €50 | €50 | €50 |
| C5 Fix Test | — | €100 | €150 |
| **C6 Migration** | **€120** | **€180** | **€250** |
| **Tổng** | **€620** | **€1.080** | **€1.550** |
| Click ước tính | 10–30 | 18–55 | 30–85 |
| Lead ước tính @5–8% | 1–2 | 2–5 | 3–7 |
| Khách ước tính @30% | 0–1 | 1–2 | 1–3 |

**Khuyến nghị: bắt đầu Tier A trong 4 tuần**, lên Tier B từ tuần 5 nếu CPL < €300.

⚠️ **Trên €1.300/tháng là lãng phí** — trần volume ở §2.2. Muốn tiêu nhiều hơn phải mở rộng bề mặt keyword hoặc chuyển kênh, không phải tăng bid.

### 9.2. Lộ trình 90 ngày

| Tuần | Việc |
|---|---|
| **0** | Hoàn thành 6 điều kiện tiên quyết §3. Chạy Keyword Planner lấy volume thật (§12) và **cập nhật lại §2.2 bằng số thật** |
| **1** | Dựng C1 + C4 ở Tier A. Chỉ 2 campaign. Manual CPC. Không bật C2/C3 vội |
| **2** | Kiểm tra Search Terms mỗi 2 ngày, bổ sung negative. Dựng C2, chưa bật |
| **3** | Bật C2. Review ad copy NL bởi người bản xứ (nếu chưa làm ở tuần 0) |
| **4** | **Review lần 1.** Nếu C1 có ≥1 lead → giữ. Nếu 0 lead với chi >€120 → sửa landing page trước khi đổ thêm tiền |
| **5** | Bật C3 (nếu landing page security đã live). Nâng Tier A → Tier B cho campaign nào có CPL < €300 |
| **6–7** | Tối ưu bid theo từng keyword. Tách keyword nào có ≥3 conversion ra ad group riêng |
| **8** | **Review lần 2.** Tính CAC thật theo §2.3. Đối chiếu với bảng nhạy — nếu CAC > €1.250 thì dừng và sửa phễu, không tăng ngân sách |
| **9** | Bật C5 (Fix Test) nếu C2/C3 đã ổn định. **Bật C6** — bắt đầu chỉ với `AG-MIG-TanStack`, trỏ tạm về `/en/from-prototype-to-production` |
| **10–11** | Bắt đầu offline conversion import. Thêm keyword mới từ Search Terms Report. Nếu `AG-MIG-TanStack` có ≥1 lead → dựng `/en/lovable-tanstack-migration`, bật nốt `AG-MIG-Service` + `AG-MIG-Platform` |
| **12** | **Review quý.** Quyết định: mở rộng geo, thêm cụm keyword, hay chuyển ngân sách sang kênh khác. Chạy lại vòng changelog mining ([`keyword_idea_playbook.md`](keyword_idea_playbook.md) Phần C) |

### 9.3. Bid strategy theo giai đoạn

| Giai đoạn | Strategy | Lý do |
|---|---|---|
| Tuần 1–6 | **Manual CPC** hoặc Maximize Clicks + CPC cap | Volume quá thấp cho Smart Bidding |
| Tuần 7–12 | Giữ Manual CPC | Vẫn chưa đủ 30 conversion |
| Sau 30+ conversion | Maximize Conversions | Đây thường là tháng thứ 4–6, không phải tháng 2 |
| Sau 50+ conversion | Target **CPA** (Cost Per Acquisition — chi phí mỗi chuyển đổi) @ €300 | |

⚠️ `google_ads_keywords_launchstudio.md` đề xuất chuyển sang Maximize Conversions sớm. Với volume thật của tài khoản này, làm vậy là **quá sớm** — Google sẽ không có đủ tín hiệu và sẽ tiêu ngân sách vào việc học.

---

<a id="10"></a>
## 10. KPI (Key Performance Indicator — chỉ số hiệu suất chính) và ngưỡng quyết định

### 10.1. Bảng KPI

| Chỉ số | Tuần 4 | Tuần 8 | Tuần 12 | Ngưỡng kill |
|---|---|---|---|---|
| **CPC** (Cost Per Click — chi phí mỗi lượt nhấp) trung bình | ≤ €12 | ≤ €10 | ≤ €10 | > €16 kéo dài 2 tuần |
| **CTR** (Click-Through Rate — tỉ lệ nhấp) | ≥ 4% | ≥ 6% | ≥ 7% | < 2% ở ad group nào đó |
| **LP conversion** (Landing Page conversion rate — tỉ lệ chuyển đổi trang đích) | ≥ 3% | **≥ 5%** | ≥ 6% | < 2% sau khi đã sửa 1 lần |
| **CPL** (Cost Per Lead — chi phí mỗi khách tiềm năng) đã lọc chất lượng | ≤ €400 | ≤ €300 | ≤ €250 | > €500 |
| **CAC** (Customer Acquisition Cost — chi phí thu hút một khách hàng) | — | ≤ €900 | **≤ €625** | > €1.250 (hoà vốn) |
| **IS** (Impression Share — thị phần hiển thị) | ≥ 40% | ≥ 60% | ≥ 65% | — |
| **IS lost (budget)** (Search Lost Impression Share (budget) — thị phần hiển thị mất do hết ngân sách) | — | < 20% | < 15% | > 40% = tăng ngân sách |
| **IS lost (rank)** (Search Lost Impression Share (rank) — thị phần hiển thị mất do thứ hạng thấp) | — | < 30% | < 25% | > 50% = tăng bid hoặc sửa **QS** (Quality Score — điểm chất lượng) |

### 10.1.1. Chú thích đầy đủ từng chỉ số

> Cột **"Tìm ở đâu"** ghi đúng tên cột trong giao diện Google Ads (tiếng Anh) để bạn bật lên xem.

#### CPC — Cost Per Click (chi phí mỗi lượt nhấp)

| | |
|---|---|
| **Công thức** | Tổng chi phí ÷ Tổng số lượt nhấp |
| **Tìm ở đâu** | Google Ads → cột `Avg. CPC` |
| **Nó nói gì** | Giá trung bình bạn trả cho một người bấm vào quảng cáo |
| **Vì sao ngưỡng €10** | §2.3 cho thấy ở CPC €10 với LP conversion 3% và close rate 25% thì CAC = €1.333 → lỗ. €10 là mức cao nhất còn an toàn |
| **Hiểu nhầm thường gặp** | CPC thấp ≠ tốt. CPC €2 từ truy vấn sai còn tệ hơn CPC €12 từ truy vấn đúng |

#### CTR — Click-Through Rate (tỉ lệ nhấp)

| | |
|---|---|
| **Công thức** | (Số lượt nhấp ÷ Số lượt hiển thị) × 100 |
| **Tìm ở đâu** | Google Ads → cột `CTR` |
| **Nó nói gì** | Mức độ khớp giữa quảng cáo và truy vấn. CTR thấp = ad copy không nói đúng điều người ta tìm |
| **Vì sao ngưỡng 6–7%** | Với từ khoá intent thương mại, hẹp, CTR 6–9% là bình thường. Dưới 2% nghĩa là sai thông điệp, không phải sai bid |
| **Hiểu nhầm thường gặp** | Tăng bid để "cứu" CTR thấp. Sai — CTR thấp là vấn đề nội dung quảng cáo, tăng bid chỉ làm đắt hơn |

#### LP conversion — Landing Page conversion rate (tỉ lệ chuyển đổi trang đích)

| | |
|---|---|
| **Công thức** | (Số lead ÷ Số lượt nhấp) × 100 |
| **Tìm ở đâu** | Google Ads → cột `Conv. rate` *(cùng một con số, Google gọi tên khác)* |
| **Nó nói gì** | Trong 100 người bấm vào, bao nhiêu người thật sự để lại liên hệ |
| **Vì sao ngưỡng 5%** | Đây là **ngưỡng sống còn** của cả plan. Xem bảng §2.3: ở 3% và CPC €10 thì mô hình lỗ; ở 5% với close rate 40% thì CAC = €500, có lãi |
| **Hiểu nhầm thường gặp** | Đổ lỗi cho kênh khi tỉ lệ thấp. Nếu CTR tốt mà LP conversion kém thì vấn đề nằm ở trang đích, không nằm ở Google Ads |

#### CPL — Cost Per Lead (chi phí mỗi khách tiềm năng)

| | |
|---|---|
| **Công thức** | Tổng chi phí ÷ Số lead **đã lọc chất lượng** |
| **Tìm ở đâu** | Google Ads → cột `Cost / conv.` — nhưng đó là **tất cả** lead. CPL đã lọc phải tính tay |
| **Nó nói gì** | Giá thật của một khách tiềm năng dùng được |
| **"Đã lọc chất lượng" nghĩa là gì** | §7.3 đề xuất thêm field bắt buộc *"Bạn đã có prototype chưa?"*. Chỉ lead chọn **"Có"** mới được tính |
| **Hiểu nhầm thường gặp** | Dùng `Cost / conv.` của Google làm CPL. Với 3–8 lead/tháng, một lead rác cũng làm lệch toàn bộ con số |

#### CAC — Customer Acquisition Cost (chi phí thu hút một khách hàng)

| | |
|---|---|
| **Công thức** | CPL ÷ Close rate *(hoặc: CPC ÷ (LP conversion × Close rate))* |
| **Tìm ở đâu** | ❌ **Không có trong Google Ads.** Phải ghép dữ liệu quảng cáo với dữ liệu bán hàng (§7.2 mục 5 — offline conversion import) |
| **Nó nói gì** | Tốn bao nhiêu tiền quảng cáo để có **một khách hàng trả tiền thật** |
| **Vì sao ngưỡng €625** | Bằng 25% deal trung bình €2.500. Ngưỡng hoà vốn là €1.250 (toàn bộ lợi nhuận gộp ở biên 50%) |
| **Hiểu nhầm thường gặp** | Nhầm CAC với CPL. Nếu close rate là 25% thì CAC = 4 lần CPL |

#### Close rate (tỉ lệ chốt deal)

| | |
|---|---|
| **Công thức** | (Số khách hàng ÷ Số lead đã lọc) × 100 |
| **Tìm ở đâu** | ❌ Không có trong Google Ads — nằm ở CRM hoặc bảng theo dõi bán hàng của bạn |
| **Nó nói gì** | Chất lượng quy trình bán, không phải chất lượng quảng cáo |
| **Vì sao quan trọng** | §2.3 cho thấy đi từ 25% → 40% làm **giảm CAC 37%** — đòn bẩy mạnh hơn mọi thao tác tối ưu bid |

#### IS — Impression Share (thị phần hiển thị)

| | |
|---|---|
| **Công thức** | (Số lượt hiển thị thực tế ÷ Số lượt hiển thị đủ điều kiện) × 100 |
| **Tìm ở đâu** | Google Ads → cột `Search impr. share` *(nhóm Competitive metrics, phải bật thủ công)* |
| **Nó nói gì** | Bạn xuất hiện được bao nhiêu phần trăm số lần đáng lẽ được xuất hiện |
| **Vì sao ngưỡng 65%** | Dùng trong công thức trần chi tiêu ở §2.2. Trên 65% với tài khoản nhỏ là tốt; 100% thường là dấu hiệu bid quá cao |

#### IS lost (budget) — Search Lost Impression Share (budget)

| | |
|---|---|
| **Nghĩa** | Thị phần hiển thị **mất vì hết ngân sách trong ngày** |
| **Tìm ở đâu** | Google Ads → cột `Search lost IS (budget)` |
| **Nó nói gì** | Có nhu cầu tìm kiếm mà bạn không mua nổi vì ngân sách cạn |
| **Hành động** | > 40% **và** CPL đang tốt → tăng ngân sách. Đây là tín hiệu tăng tiền đáng tin nhất |

#### IS lost (rank) — Search Lost Impression Share (rank)

| | |
|---|---|
| **Nghĩa** | Thị phần hiển thị **mất vì thứ hạng quảng cáo thấp** |
| **Tìm ở đâu** | Google Ads → cột `Search lost IS (rank)` |
| **Nó nói gì** | Bạn có tiền nhưng Google không xếp bạn đủ cao |
| **Hành động** | > 50% → kiểm tra **QS** trước. Nếu QS < 5 thì sửa message match của trang đích, **đừng** tăng bid |

#### QS — Quality Score (điểm chất lượng)

| | |
|---|---|
| **Thang điểm** | 1–10, chấm ở **cấp từ khoá** |
| **Tìm ở đâu** | Google Ads → tab Keywords → cột `Quality Score` *(hiện `—` nếu chưa đủ dữ liệu)* |
| **Ba thành phần** | Expected CTR (CTR kỳ vọng) · Ad relevance (mức liên quan của quảng cáo) · Landing page experience (trải nghiệm trang đích) |
| **Vì sao quan trọng** | QS cao → CPC thấp hơn cho cùng vị trí. Đây là lý do §3 bắt buộc làm landing page riêng trước khi chạy |

---

### 10.1.2. Các từ viết tắt khác dùng trong tài liệu này

| Viết tắt | Tiếng Anh đầy đủ | Nghĩa |
|---|---|---|
| **CPA** | Cost Per Acquisition | Chi phí mỗi chuyển đổi — tên Google dùng cho bid strategy `Target CPA` |
| **LTV** | Lifetime Value | Giá trị trọn đời của một khách hàng |
| **KPI** | Key Performance Indicator | Chỉ số hiệu suất chính |
| **RSA** | Responsive Search Ad | Quảng cáo tìm kiếm thích ứng — Google tự ghép headline/description |
| **SERP** | Search Engine Results Page | Trang kết quả tìm kiếm |
| **SEO** | Search Engine Optimization | Tối ưu hoá công cụ tìm kiếm (không trả phí) |
| **CTA** | Call To Action | Lời kêu gọi hành động |
| **USP** | Unique Selling Proposition | Điểm bán hàng độc nhất |
| **GA4** | Google Analytics 4 | Phiên bản Google Analytics hiện hành |
| **GCLID** | Google Click Identifier | Mã định danh lượt nhấp — dùng để ghép conversion ngoại tuyến |
| **UTM** | Urchin Tracking Module | Tham số gắn vào URL để theo dõi nguồn traffic |
| **B2B** | Business-to-Business | Doanh nghiệp bán cho doanh nghiệp |
| **MVP** | Minimum Viable Product | Sản phẩm khả dụng tối thiểu |
| **SaaS** | Software as a Service | Phần mềm dạng dịch vụ thuê bao |
| **UI** | User Interface | Giao diện người dùng |
| **API** | Application Programming Interface | Giao diện lập trình ứng dụng |
| **CSV** | Comma-Separated Values | Định dạng file bảng phân tách bằng dấu phẩy |
| **URL** | Uniform Resource Locator | Địa chỉ web |
| **FAQ** | Frequently Asked Questions | Câu hỏi thường gặp |
| **SSL** | Secure Sockets Layer | Giao thức mã hoá kết nối web (chứng chỉ https) |
| **DNS** | Domain Name System | Hệ thống phân giải tên miền |
| **SSR** | Server-Side Rendering | Kết xuất phía máy chủ — ảnh hưởng trực tiếp tới SEO |
| **RLS** | Row Level Security | Bảo mật cấp dòng trong cơ sở dữ liệu (Supabase) |
| **MCP** | Model Context Protocol | Giao thức kết nối ứng dụng với trợ lý AI |
| **SSO** | Single Sign-On | Đăng nhập một lần cho nhiều hệ thống |
| **SCIM** | System for Cross-domain Identity Management | Chuẩn đồng bộ tài khoản người dùng |
| **2FA** | Two-Factor Authentication | Xác thực hai yếu tố |
| **ERP** | Enterprise Resource Planning | Hệ thống quản trị tài nguyên doanh nghiệp |
| **CAD / CAM** | Computer-Aided Design / Manufacturing | Phần mềm thiết kế / gia công bằng máy tính |
| **CNC** | Computer Numerical Control | Máy gia công điều khiển số |
| **NPI / DFM** | New Product Introduction / Design For Manufacturing | Đưa sản phẩm mới vào sản xuất / thiết kế để sản xuất được |
| **TNO** | Nederlandse Organisatie voor toegepast-natuurwetenschappelijk onderzoek | Tổ chức Nghiên cứu Khoa học Ứng dụng Hà Lan |
| **CFLW** | CFLW Cyber Strategies | Công ty an ninh mạng (tiền thân CyberDevOps) |
| **GKP** | Google Keyword Planner | Công cụ nghiên cứu từ khoá của Google Ads |
| **GSC** | Google Search Console | Công cụ theo dõi hiệu suất tìm kiếm không trả phí |

---

### 10.1.3. Quy ước đặt tên trong tài liệu này

| Ký hiệu | Nghĩa | Ví dụ |
|---|---|---|
| **C1–C6** | Campaign 1–6 (chiến dịch) | `C3` = chiến dịch Security |
| **LS-** | LaunchStudio — tiền tố tên chiến dịch | `LS-Search-EN-Hire` |
| **AG-** | Ad Group (nhóm quảng cáo) | `AG-LOV-Hire` |
| **H1–H15** | Headline 1–15 (tiêu đề quảng cáo, tối đa 30 ký tự) | |
| **D1–D4** | Description 1–4 (mô tả quảng cáo, tối đa 90 ký tự) | |
| **P1–P3** | Pin position 1–3 (ghim tiêu đề vào vị trí cố định) | `P1` = luôn hiện đầu tiên |
| **Ch** | Characters (số ký tự) | Cột đếm ký tự trong bảng RSA |
| **P1/P2/P3** *(trong CSV)* | Priority 1–3 (mức ưu tiên từ khoá) | Khác với Pin — xem ngữ cảnh |

> ⚠️ **Lưu ý:** `P1–P3` mang hai nghĩa tuỳ ngữ cảnh — **Pin position** trong bảng RSA (§5), và **Priority** trong file CSV từ khoá. Đây là quy ước kế thừa từ [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md); mình giữ nguyên để khớp file gốc.

---

### 10.1.4. ⚠️ Cảnh báo về ý nghĩa thống kê

Với **15–72 lượt nhấp/tháng** (§2.2), gần như **mọi chỉ số trong bảng §10.1 đều nhiễu** ở tuần 4.

| Chỉ số | Cần bao nhiêu dữ liệu để đáng tin |
|---|---|
| CTR | ~500 lượt hiển thị/ad group |
| LP conversion | ~100 lượt nhấp/trang đích |
| CPL | ~10 lead |
| CAC | ~10 khách hàng — **có thể mất 6–12 tháng** |

➡️ Cột "Tuần 4" trong bảng là **mốc tham chiếu để phát hiện sai lệch lớn**, không phải để ra quyết định tối ưu. Quyết định thật bắt đầu từ tuần 8.


### 10.2. Quy tắc quyết định rõ ràng

Đây là phần thường thiếu trong plan và là lý do người ta do dự không dám tắt cái gì.

| Tình huống | Hành động |
|---|---|
| Ad group chi > €150, 0 conversion, sau 4 tuần | **Tắt.** Không "cho thêm cơ hội" |
| Keyword chi > €80, 0 conversion | **Tắt keyword đó**, giữ ad group |
| CPL < €200 ở một ad group | **Tăng ngân sách ad group đó 50%**, tuần sau xem lại |
| IS lost (budget) > 40% và CPL tốt | **Tăng ngân sách** — đang bỏ lỡ nhu cầu có sẵn |
| IS lost (rank) > 50% | Kiểm tra Quality Score. Nếu QS < 5 → sửa message match landing page **trước khi** tăng bid |
| CTR < 2% ở ad group | Ad copy không khớp intent → viết lại RSA, đừng tăng bid |
| LP conversion < 2% | **Dừng đổ tiền vào ad group đó.** Vấn đề ở landing page, không phải ở ads |
| CAC > €1.250 sau tuần 8 | **Dừng toàn bộ**, xem lại §2.3, sửa phễu bán hàng |

### 10.3. Đừng đánh giá bằng chỉ số nào

Với tài khoản 15–70 click/tháng:

- ❌ **Impression count** — vô nghĩa, sẽ luôn trông thảm hại
- ❌ **Click volume** — bị chặn bởi trần volume, không phải bởi hiệu suất
- ❌ **CTR tuần 1** — chưa đủ mẫu
- ✅ **Cost per qualified lead** — chỉ số duy nhất đáng tin ở giai đoạn đầu
- ✅ **CAC và LTV** — chỉ số duy nhất đáng tin ở giai đoạn sau

---

<a id="11"></a>
## 11. Rủi ro

| # | Rủi ro | Mức | Cách giảm |
|---|---|---|---|
| 1 | **Bẫy `lovable` = đồ lót/từ điển** đốt ngân sách ngay ngày 1 | 🔴 Cao | Negative list §6.1 + tuyệt đối không broad match |
| 2 | **Volume thật thấp hơn ước tính**, không tiêu được ngân sách | 🟠 TB-cao | Verify bằng Keyword Planner ở tuần 0. Nếu < 200 search/tháng → cân nhắc chuyển ngân sách sang LinkedIn (`paid_ads_plan.md` §6) |
| 3 | **CPC cao hơn €14** do cạnh tranh B2B SaaS | 🟠 TB | Benchmark 2026 cho B2B SaaS median non-brand là $8,50–14,00. Nếu vượt → tập trung vào NL (CPC thấp hơn) và long-tail |
| 4 | **Landing page chuyển đổi < 3%** → mô hình lỗ | 🔴 Cao | §2.3. Đo từ tuần 2, sửa trước khi tăng ngân sách |
| 5 | **Cạnh tranh giá với Fiverr $25** | 🟠 TB | §5.2.1 — tái định nghĩa vấn đề, không đấu giá |
| 6 | **Smart Bidding bật quá sớm** | 🟡 TB-thấp | §9.3 — giữ Manual CPC tới 30+ conversion |
| 7 | **Con số "45%" và "80%" trên website chưa rõ nguồn** | 🟡 TB-thấp | Xác minh nguồn trước khi đưa vào ad copy; Google Ads có chính sách về claim |
| 8 | **Thiếu Consent Mode v2** → mất dữ liệu conversion ở EU | 🟠 TB | §7.2 mục 4 |
| 9 | **Dùng nhầm file keyword rỗng** | 🟡 Thấp | §0.1 — đổi tên file cũ thành `.DEPRECATED.md` |
| 10 | **C6: cửa sổ TanStack đóng lại** khi Lovable tự migrate hoặc dự án cũ chết | 🟠 TB | Ước tính còn 6–12 tháng. Chạy sớm, đừng để sang 2027 |
| 11 | **C6: bid tên đối thủ bị trả đũa** | 🟡 TB-thấp | C4 Brand đã phòng. Hoặc bỏ 2 keyword đó |
| 12 | **C6: tuyên bố sai về sản phẩm bên thứ ba** trong ad copy | 🟠 TB | §5.6.6 — xác minh ngày 13/05/2026 từ nguồn Lovable trước khi chạy |

---

<a id="12"></a>
## 12. Checklist ngày 1

### Trước khi mở Google Ads

- [ ] Xuất seed list: `awk -F',' 'NR>1{print $3}' keyword_seeds_google_ads_3_clusters.csv`
- [ ] Chạy Keyword Planner: Location = Netherlands (lượt 1), rồi DE/FR/ES/IT/SE/DK/PL/PT/IE/BE (lượt 2)
- [ ] Xoá mọi keyword volume > 20.000 (gần như chắc là bẫy)
- [ ] **Cập nhật lại §2.2 và §9.1 của tài liệu này bằng số thật**
- [ ] Landing page `/en/ai-code-security-audit` đã live
- [ ] Landing page `/en/from-prototype-to-production` đã live
- [ ] Landing page `/nl/van-prototype-naar-productie` đã live, đã có người Hà Lan bản xứ đọc
- [ ] GA4 + 3 conversion event đã cài và đã test
- [ ] Conversion đã import vào Google Ads, đánh dấu Primary
- [ ] Enhanced Conversions + Consent Mode v2 đã bật
- [ ] `Organization` schema đã thêm, author schema `"phu.lt"` đã sửa

### Trong Google Ads

- [ ] Tạo 2 Shared Negative List (§6.1, §6.2) **trước khi** tạo campaign
- [ ] Tạo C1 (NL) + C4 (Brand) ở Tier A
- [ ] Gắn Shared Negative List vào cả 2 campaign
- [ ] Bid strategy = Manual CPC
- [ ] Location targeting: C1 = Netherlands + Flanders, **"Presence" không phải "Presence or interest"**
- [ ] Ad schedule: chạy cả tuần trong 4 tuần đầu để thu dữ liệu, sau đó cắt khung giờ kém
- [ ] Ad rotation: "Do not optimize" trong 4 tuần đầu để so sánh RSA công bằng
- [ ] Tất cả 4 sitelink + callout + structured snippet + price extension đã gắn
- [ ] Đặt lịch nhắc kiểm tra Search Terms Report mỗi 2 ngày

### C6 Migration (tuần 9, không phải ngày 1)

- [ ] Xác minh lại ngày Lovable đổi sang TanStack Start trước khi dùng trong ad copy (§5.6.6)
- [ ] Quyết định có bid tên đối thủ `nextlovable` / `vibeappscanner` không (§5.6.3)
- [ ] Nếu bid: kiểm tra ad copy **không** chứa tên đối thủ
- [ ] Bật trước `AG-MIG-TanStack`, trỏ tạm `/en/from-prototype-to-production`
- [ ] Dựng `/en/lovable-tanstack-migration` nếu có tín hiệu sau 2–4 tuần
- [ ] Thêm 3 kw vào `AG-TOOL-Hire` (C2) và 2 kw vào `AG-SEC-Tool` (C3) — §5.6.4
- [ ] Đưa 57 keyword SEO vào lịch nội dung, **không** vào Ads (§5.6.7)

---

## 📌 Tóm tắt

> **Chạy €500/tháng** vào 60 keyword intent thương mại, ưu tiên NL, Manual CPC, negative list chặn bẫy `lovable`. Đo bằng cost per qualified lead. Sửa landing page cho đến khi chuyển đổi ≥5% — dưới ngưỡng đó mô hình không có lãi dù tối ưu bid đến đâu. Trần volume €1.550/tháng sau khi thêm C6.

---

*Tổng hợp từ 8 nguồn trong repo · Số liệu volume cần verify bằng Keyword Planner trước khi chốt ngân sách · CPC benchmark: B2B SaaS median non-brand $8,50–14,00 (2026)*
