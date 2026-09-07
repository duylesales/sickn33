# 🧭 Kế Hoạch SEO & GEO-Entity — Bộ Từ Khóa Production-Readiness
## LaunchStudio.eu · 🇻🇳 Bản tiếng Việt

> **Bản dịch của:** [`seo_geo_plan_production_keywords.md`](seo_geo_plan_production_keywords.md)
>
> **⚠️ Quy ước dịch:** Toàn bộ phần **giải thích, phân tích và hướng dẫn** được dịch sang tiếng Việt. Các **tài sản sẽ triển khai thật lên website** được **giữ nguyên tiếng Hà Lan/Anh**, vì đây là văn bản chạy trực tiếp trên site — dịch sang tiếng Việt sẽ khiến chúng vô dụng:
> - Từ khóa (EN + NL) · Title tag · Meta description · H1/H2 · URL & slug
> - Answer block (đoạn trích cho AI) · Toàn bộ JSON-LD schema · Nội dung `llms.txt`

> **Bối cảnh:** Đây là bản đối ứng "organic" của [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md), xây trên cùng 14 từ khóa trong [`extra-keywords.md`](extra-keywords.md). Nếu kế hoạch Ads **mua** hiển thị, thì kế hoạch này **giành lấy** hiển thị — trên ba mặt trận: tìm kiếm truyền thống (SEO), công cụ trả lời bằng AI (GEO — Generative Engine Optimization), và nhận diện thực thể (LaunchStudio *là ai* đối với Knowledge Graph của Google và với các LLM).

| | |
|---|---|
| **Website** | 🇳🇱 `launchstudio.eu/` · 🇬🇧 `launchstudio.eu/en/` |
| **Thị trường chính** | Hà Lan (`nl-NL` chính, `en` phụ) |
| **Từ khóa nguồn** | 14 từ khóa duy nhất (xem §2) |
| **Nền so sánh (audit)** | [`seo_geo_audit_2026-07-31.md`](seo_geo_audit_2026-07-31.md) |
| **Tài liệu thương hiệu gốc** | [`launchstudio_info.md`](launchstudio_info.md) |
| **CMS** | WordPress + Yoast SEO v27.6 |
| **Trạng thái** | Bản nháp v1.0 — kế hoạch triển khai, chưa thực thi |

---

## 📑 Mục Lục

1. [Vì sao kế hoạch này KHÔNG phải "viết thêm bài"](#1)
2. [Ánh xạ Từ khóa → Ý định → Trang đích](#2)
3. [Kiến trúc site: Pillar & Cluster](#3)
4. [Brief chi tiết 5 trang money page](#4)
5. [Tận dụng 800 bài viết đã có](#5)
6. [Kế hoạch Entity & Schema.org](#6)
7. [GEO-entity: định vị địa lý](#7)
8. [GEO: Tối ưu cho công cụ trả lời AI](#8)
9. [Chiến lược song ngữ & hreflang](#9)
10. [Điều kiện kỹ thuật SEO bắt buộc](#10)
11. [Quy tắc liên kết nội bộ](#11)
12. [Lịch triển khai 90 ngày](#12)
13. [KPI & cách đo lường](#13)
14. [Rủi ro](#14)
15. [Các quyết định cần bạn duyệt](#15)

---

<a id="1"></a>
## 1. ⚠️ Vì Sao Kế Hoạch Này KHÔNG Phải "Viết Thêm Bài"

> **Hãy đọc phần này trước tiên. Nó thay đổi bản chất của khối lượng công việc.**

Ba dữ kiện từ hiện trạng khiến cách tiếp cận hiển nhiên trở thành cách sai:

**1. Không thiếu content — thiếu việc xuất bản và thiếu entity.**
Kho nội dung đang có **hơn 800 bài viết đã sản xuất** cho LaunchStudio, trong khi audit ngày 31/07/2026 chỉ đếm được **71 bài đang live** trên site. Viết thêm bài thứ 15 về bảo mật AI-code không hề đẩy được các từ khóa này; nhưng xuất bản và cấu trúc hóa những gì đã có thì có.

**2. Không có trang nào để 14 từ khóa này rank.**
Đây là các truy vấn mang ý định thương mại, hình dạng dịch vụ ("productionize AI app", "AI application security audit"). Bài blog rất hiếm khi thắng những SERP đó — **trang dịch vụ (service page)** mới thắng. Hiện tại LaunchStudio là site một trang với các anchor (`/#packages`, `/#calculator`); **không tồn tại URL nào có thể index mà *chính là* câu trả lời** cho "AI prototype to production".

**3. Nền tảng thực thể (entity) đang trống.**
Audit phát hiện: **không có `Organization` schema ở bất kỳ đâu**, không có `sameAs`, không có `FAQPage` (dù homepage đã có sẵn phần FAQ đầy đủ dạng HTML thuần), và `Person` schema của tác giả blog ghi là `"phu.lt"`. Với các công cụ trả lời bằng AI, đây là yếu tố quyết định: **một LLM không thể trích dẫn một công ty mà nó không nhận diện được**. Sửa phần này nâng *toàn bộ* từ khóa lên, không riêng 14 từ khóa này.

### 1.1 Vậy kế hoạch này gồm những gì

| Ưu tiên | Công việc | Công sức | Tác động |
|---|---|---|---|
| 🥇 **1** | Sửa tầng entity: `Organization`, `Service`, `FAQPage`, `Person`, `sameAs` (§6) | 1–2 ngày dev | 🔴 Toàn site, vĩnh viễn |
| 🥈 **2** | Xây **5 trang money page có thể index** cho 14 từ khóa (§4) | 3–5 ngày | 🔴 Không có trang thì không thể rank |
| 🥉 **3** | Viết lại `llms.txt` + thêm khối trích dẫn cho AI (§8) | 1 ngày | 🟡 Hiển thị trên công cụ trả lời AI |
| 4 | Xuất bản & liên kết các bài đã có làm lớp hỗ trợ cluster (§5) | Liên tục | 🟡 Thẩm quyền chủ đề |
| 5 | Sửa các lỗi kỹ thuật từ audit (§10) | 1 ngày | 🟡 Gỡ bỏ rào cản xếp hạng |

> **Lưu ý tỷ lệ:** khoảng **một tuần làm việc tập trung** vào cấu trúc và entity mang lại nhiều hơn hàng tháng sản xuất bài viết bổ sung, đối với riêng bộ từ khóa này.

---

<a id="2"></a>
## 2. 🎯 Ánh Xạ Từ Khóa → Ý Định → Trang Đích

Mỗi từ khóa được phân loại theo **ý định SERP** (thứ Google đang thực sự thưởng cho truy vấn đó) và gán cho **đúng một trang đích**. Gán hai trang cho cùng một từ khóa sẽ gây "ăn thịt lẫn nhau" (cannibalisation) — lỗi SEO tự gây ra phổ biến nhất trên các site nhỏ.

| # | Từ khóa (EN) | Từ khóa đích tiếng Hà Lan | Ý định | Loại trang thắng SERP | Trang đích |
|---|---|---|---|---|---|
| 01 | AI prototype to production | `ai prototype naar productie` | Thương mại - tìm hiểu | Dịch vụ + hướng dẫn (lai) | **P1** |
| 02 | AI app to production | `ai app live zetten` | Thương mại - tìm hiểu | Dịch vụ | **P1** |
| 03 | AI code to production | `ai code productieklaar` | Hỗn hợp (có ý định tự làm) | Một mục trong hướng dẫn | **P1** § |
| 04 | AI generated code production | `ai gegenereerde code productie` | Thông tin - thương mại | Một mục trong hướng dẫn | **P2** § |
| 05 | productionize AI application | `applicatie productieklaar maken` | Thương mại | Dịch vụ | **P2** |
| 06 | productionize AI app | `ai app productieklaar maken` | Thương mại | Dịch vụ | **P2** |
| 07 | make AI generated app production ready | `ai app productieklaar maken` | Thương mại | Dịch vụ + checklist | **P2** |
| 08 | AI development | `ai ontwikkeling` | ⚠️ Điều hướng / quá rộng | — | ❌ **Không nhắm tới** |
| 09 | AI app production problems | `ai app werkt niet live` | Nhận biết vấn đề | Hướng dẫn + FAQ | **P1** § |
| 10 | AI application production ready | `applicatie productieklaar` | Thương mại | Dịch vụ | **P2** |
| 11 | AI generated app security | `ai app beveiligen` | Thương mại | Dịch vụ | **P3** |
| 12 | AI generated code security | `ai gegenereerde code beveiliging` | Thông tin - thương mại | Hướng dẫn | **P3** |
| 13 | AI application security audit | `security audit applicatie` | 💰 Giao dịch | Dịch vụ (money page) | **P4** |
| 14 | AI application scalability | `applicatie schaalbaar maken` | Cân nhắc | Hướng dẫn + dịch vụ | **P5** |

### 2.1 Vì sao từ khóa #08 bị loại bỏ có chủ đích

Nhất quán với kế hoạch Ads: `AI development` là một **head term** mà kết quả tìm kiếm bị thống trị bởi các công ty tư vấn *xây dựng mô hình AI*, các chương trình đại học và tin tuyển dụng.

Rank được từ khóa này sẽ kéo về những người tìm một dịch vụ mà LaunchStudio không bán → tăng tỷ lệ thoát và **làm loãng tín hiệu chủ đề của toàn bộ cụm**. Cần hiểu rằng **độ chính xác chủ đề (topical precision) là một tài sản xếp hạng** — nhắm vào một từ khóa mà bạn không thể đáp ứng sẽ làm hại chính các trang xung quanh nó.

**Ngoại lệ:** từ này *được phép* xuất hiện trong nội dung bài như ngôn ngữ tự nhiên (ví dụ: "AI development không giống với production engineering") — đó là độ liên quan theo ngữ cảnh, không phải nhắm mục tiêu.

### 2.2 Ghi chú về hành vi tìm kiếm (kế thừa từ kế hoạch Ads)

Người mua kỹ thuật ở Hà Lan tìm các khái niệm kỹ thuật **bằng tiếng Anh**, và từ "productionize" **không có từ tương đương trong tiếng Hà Lan**.

Với SEO, hệ quả khác với Ads: thay vì chia ngân sách, bạn **xuất bản cả hai phiên bản ngôn ngữ và để trang tiếng Hà Lan mang thuật ngữ tiếng Anh một cách tự nhiên trong nội dung** (ví dụ: *"productieklaar maken — in het Engels vaak 'production-ready' genoemd"*). Cách này bắt được người Hà Lan gõ thuật ngữ tiếng Anh, đồng thời vẫn giữ trang là tiếng Hà Lan rõ ràng cho hreflang.

---

<a id="3"></a>
## 3. 🏗️ Kiến Trúc Site — Pillar & Cluster

Một trang pillar, bốn trang dịch vụ/hướng dẫn hỗ trợ, và thư viện bài viết hiện có làm vòng ngoài. Mọi trang đều link **lên** pillar; pillar link **xuống** cả bốn trang con. Đây chính là cấu trúc Google dùng để suy ra thẩm quyền chủ đề, và cũng là cấu trúc một LLM đi qua khi quyết định URL nào trả lời câu hỏi tốt nhất.

```
                    ┌─────────────────────────────────────┐
                    │  P1 · PILLAR                        │
                    │  Van AI-prototype naar productie    │
                    │  /van-prototype-naar-productie/     │
                    │  Từ khóa #01 #02 #03 #09            │
                    └───────────────┬─────────────────────┘
                                    │
        ┌───────────────┬───────────┴───────┬────────────────┐
        │               │                   │                │
┌───────▼──────┐ ┌──────▼───────┐ ┌─────────▼──────┐ ┌───────▼────────┐
│ P2           │ │ P3           │ │ P4  💰         │ │ P5             │
│ Productie-   │ │ Beveiliging  │ │ Security audit │ │ Schaalbaarheid │
│ klaar maken  │ │ AI-code      │ │ applicatie     │ │ applicatie     │
│ /productie-  │ │ /ai-code-    │ │ /security-     │ │ /applicatie-   │
│ klaar-maken/ │ │ beveiligen/  │ │ audit/         │ │ schaalbaar/    │
│ #04 #05 #06  │ │ #11 #12      │ │ #13            │ │ #14            │
│ #07 #10      │ │              │ │                │ │                │
└──────┬───────┘ └──────┬───────┘ └────────┬───────┘ └───────┬────────┘
       │                │                  │                 │
       └────────────────┴──────────────────┴─────────────────┘
                                    │
                    ┌───────────────▼─────────────────────┐
                    │  BÀI VIẾT HỖ TRỢ (800 bài đã có)    │
                    │  extra-8/9/10-decision, extra-6, -7 │
                    │  Mỗi bài link LÊN trang pillar của nó│
                    └─────────────────────────────────────┘
```

### 3.1 Cấu trúc URL

| Trang | 🇳🇱 URL tiếng Hà Lan | 🇬🇧 URL tiếng Anh |
|---|---|---|
| **P1** Pillar | `/van-prototype-naar-productie/` | `/en/prototype-to-production/` |
| **P2** Production-ready | `/productieklaar-maken/` | `/en/production-ready/` |
| **P3** Bảo mật code | `/ai-code-beveiligen/` | `/en/ai-code-security/` |
| **P4** Security audit 💰 | `/security-audit-applicatie/` | `/en/application-security-audit/` |
| **P5** Khả năng mở rộng | `/applicatie-schaalbaar-maken/` | `/en/application-scalability/` |

> **Vì sao không dùng `/diensten/...`?** Trên một site nhỏ, slug nông có chứa từ khóa xếp hạng tốt hơn slug lồng nhiều cấp, và mỗi trang trong năm trang này tự nó đã là một thực thể thương mại độc lập. Giữ độ sâu ở một cấp; đừng chôn chúng dưới thư mục `/services/`.

> **Quy tắc slug:** chữ thường, nối bằng dấu gạch ngang, không chứa ngày tháng, không có stop word, **không bao giờ đổi sau khi đã xuất bản** (đổi slug làm mất 3–6 tháng thẩm quyền tích lũy, trừ khi 301-redirect đúng cách).

---

<a id="4"></a>
## 4. 📄 Brief Chi Tiết — 5 Trang Money Page

Mỗi brief đủ hoàn chỉnh để giao thẳng cho người viết mà không cần giải thích thêm: từ khóa mục tiêu, title tag và meta description kèm số ký tự, H1, dàn ý đầy đủ các heading, số từ, schema bắt buộc, liên kết nội bộ, và **answer block** — đoạn văn 40–60 từ có thể trích dẫn trực tiếp mà các công cụ trả lời AI sẽ lấy ra (xem §8).

> **Giới hạn ký tự:** Title ≤ 60 · Meta description ≤ 155 · H1 = một trên mỗi trang
> **Lưu ý:** toàn bộ title, meta, H1 và dàn heading dưới đây **giữ nguyên tiếng Hà Lan/Anh** vì đây là văn bản sẽ chạy thật trên website.

---

### 📄 P1 — PILLAR · Từ AI-prototype đến production

| Trường | 🇳🇱 Tiếng Hà Lan | 🇬🇧 Tiếng Anh |
|---|---|---|
| **URL** | `/van-prototype-naar-productie/` | `/en/prototype-to-production/` |
| **Từ khóa chính** | `ai prototype naar productie` | `ai prototype to production` |
| **Từ khóa phụ** | `ai app live zetten`, `prototype werkt niet in productie`, `ai code productieklaar` | `ai app to production`, `ai code to production`, `ai app production problems` |
| **Ý định** | Thương mại - tìm hiểu | Thương mại - tìm hiểu |
| **Số từ** | 1.800–2.400 | 1,800–2,400 |
| **Loại trang** | Pillar: lai dịch vụ + hướng dẫn | Pillar: lai dịch vụ + hướng dẫn |

**Title tag**
- 🇳🇱 `Van AI-prototype naar productie in 1-3 weken | LaunchStudio` *(59)*
- 🇬🇧 `AI Prototype to Production: What It Takes | LaunchStudio` *(56)*

**Meta description**
- 🇳🇱 `Je AI-prototype werkt, maar gaat niet live. Ontdek wat er tussen prototype en productie zit: beveiliging, database, betalingen en hosting. Vanaf €800.` *(150)*
- 🇬🇧 `Your AI prototype works but will not go live. See exactly what sits between prototype and production: security, database, payments, hosting. From €800.` *(151)*

**H1**
- 🇳🇱 `Van AI-prototype naar productie: wat er echt tussen zit`
- 🇬🇧 `AI Prototype to Production: What Actually Sits in Between`

**Dàn ý heading**

| Cấp | 🇳🇱 Tiếng Hà Lan | 🇻🇳 Nghĩa tiếng Việt |
|---|---|---|
| H2 | Waarom een werkend prototype nog niet live kan | Vì sao một prototype chạy được vẫn chưa thể lên live |
| H2 | De zes dingen die tussen prototype en productie staan | Sáu thứ nằm giữa prototype và production |
| H3 | 1. Toegangsrechten en authenticatie | 1. Quyền truy cập và xác thực |
| H3 | 2. Database en dataintegriteit | 2. Database và tính toàn vẹn dữ liệu |
| H3 | 3. Betalingen en facturatie | 3. Thanh toán và xuất hóa đơn |
| H3 | 4. Hosting, domein en deployment | 4. Hosting, tên miền và triển khai |
| H3 | 5. Monitoring, back-ups en herstel | 5. Giám sát, sao lưu và phục hồi |
| H3 | 6. AVG en dataverwerking | 6. AVG (GDPR) và xử lý dữ liệu |
| H2 | Gebouwd in Lovable, Bolt of Cursor? Wat er per tool ontbreekt | Xây bằng Lovable, Bolt hay Cursor? Mỗi tool thiếu gì |
| H2 | Wat het kost en hoe lang het duurt | Chi phí bao nhiêu và mất bao lâu |
| H2 | Zelf doen of uitbesteden — een eerlijke afweging | Tự làm hay thuê ngoài — cân nhắc thẳng thắn |
| H2 | Zo werkt het bij LaunchStudio: in 3 stappen live | Quy trình LaunchStudio: live trong 3 bước |
| H2 | Veelgestelde vragen | Câu hỏi thường gặp |

**Answer block (GEO) — đặt ngay dưới H1**
- 🇳🇱 *"Een AI-prototype naar productie brengen betekent zes dingen afdichten die AI-tools zoals Lovable, Bolt en Cursor standaard niet regelen: toegangsrechten, database-integriteit, betalingen, hosting, monitoring en AVG-naleving. Bij LaunchStudio duurt dat 1 tot 3 weken tegen een vaste prijs van €800 tot €7.500, waarbij je frontend onaangeroerd blijft."*
- 🇬🇧 *"Taking an AI prototype to production means closing six gaps that AI tools such as Lovable, Bolt and Cursor do not handle by default: access rules, database integrity, payments, hosting, monitoring and GDPR compliance. At LaunchStudio this takes 1 to 3 weeks at a fixed price of €800 to €7,500, with your frontend left untouched."*
- 🇻🇳 *Nghĩa:* "Đưa một AI-prototype lên production nghĩa là bịt sáu khoảng trống mà các tool AI như Lovable, Bolt và Cursor mặc định không xử lý: quyền truy cập, toàn vẹn database, thanh toán, hosting, giám sát và tuân thủ GDPR. Tại LaunchStudio việc này mất 1–3 tuần với giá cố định €800–€7.500, giữ nguyên frontend của bạn."

**Schema bắt buộc:** `Service` + `FAQPage` + `BreadcrumbList` + `Organization` (toàn site) — xem §6
**Link đi ra:** P2, P3, P4, P5 + `/#calculator` + `/#contact` + 4–6 bài hỗ trợ
**Link đi vào:** menu chính trên homepage, toàn bộ bài hỗ trợ trong cụm
**CTA chính:** `Plan een 15-minuten gesprek` / `Book a 15-minute call` → `/#contact`

---

### 📄 P2 — Làm ứng dụng "productieklaar" (production-ready)

| Trường | 🇳🇱 Tiếng Hà Lan | 🇬🇧 Tiếng Anh |
|---|---|---|
| **URL** | `/productieklaar-maken/` | `/en/production-ready/` |
| **Từ khóa chính** | `applicatie productieklaar maken` | `make ai generated app production ready` |
| **Từ khóa phụ** | `ai app productieklaar maken`, `software productieklaar`, `in productie nemen applicatie`, `ai gegenereerde code productie` | `productionize ai application`, `productionize ai app`, `ai application production ready`, `ai generated code production` |
| **Ý định** | Thương mại | Thương mại |
| **Số từ** | 1.500–2.000 | 1,500–2,000 |
| **Loại trang** | Dịch vụ + checklist | Dịch vụ + checklist |

**Title tag**
- 🇳🇱 `Applicatie productieklaar maken | Vaste prijs vanaf €800` *(56)*
- 🇬🇧 `Make Your AI App Production Ready | Fixed Price From €800` *(57)*

**Meta description**
- 🇳🇱 `Wat betekent productieklaar precies? De complete checklist plus wat het kost om je AI-app veilig, stabiel en live te krijgen. Vaste prijs, 1-3 weken.` *(149)*
- 🇬🇧 `What does production-ready actually mean? The full checklist plus what it costs to get your AI app secure, stable and live. Fixed price, 1-3 weeks.` *(147)*

**H1**
- 🇳🇱 `Applicatie productieklaar maken: de complete checklist`
- 🇬🇧 `Make Your AI App Production Ready: The Complete Checklist`

**Dàn ý heading**

| Cấp | 🇳🇱 Tiếng Hà Lan | 🇻🇳 Nghĩa tiếng Việt |
|---|---|---|
| H2 | Wat "productieklaar" precies betekent | "Production-ready" chính xác nghĩa là gì |
| H3 | Productieklaar versus "het werkt op mijn laptop" | Production-ready so với "máy tôi chạy được mà" |
| H2 | De productieklaar-checklist: 24 punten | Checklist production-ready: 24 điểm |
| H3 | Beveiliging en toegangsrechten (6 punten) | Bảo mật và quyền truy cập (6 điểm) |
| H3 | Data en database (5 punten) | Dữ liệu và database (5 điểm) |
| H3 | Betrouwbaarheid en herstel (5 punten) | Độ tin cậy và khả năng phục hồi (5 điểm) |
| H3 | Prestaties en schaal (4 punten) | Hiệu năng và khả năng mở rộng (4 điểm) |
| H3 | Compliance en juridisch (4 punten) | Tuân thủ và pháp lý (4 điểm) |
| H2 | Wat AI-tools standaard níét regelen | Những gì tool AI mặc định KHÔNG xử lý |
| H2 | Zelf doen: wat je realistisch in een weekend haalt | Tự làm: một cuối tuần thực tế làm được gì |
| H2 | Wat het kost om het te laten doen | Chi phí nếu thuê làm |
| H2 | Veelgestelde vragen | Câu hỏi thường gặp |

**Answer block (GEO)**
- 🇳🇱 *"Productieklaar betekent dat een applicatie veilig, herstelbaar en controleerbaar is met echte gebruikers en echte data — niet alleen dat hij werkt. Concreet: toegangsrechten afgedwongen op de server, een getest back-upherstel, betalingen die niet dubbel boeken, monitoring die jou als eerste waarschuwt en een AVG-grondslag voor elke opgeslagen persoonsgegeven."*
- 🇬🇧 *"Production-ready means an application is secure, recoverable and observable with real users and real data — not merely that it works. Concretely: access rules enforced on the server, a tested backup restore, payments that cannot double-charge, monitoring that alerts you before customers do, and a lawful basis for every piece of personal data stored."*
- 🇻🇳 *Nghĩa:* "Production-ready nghĩa là ứng dụng an toàn, có thể phục hồi và quan sát được với người dùng thật và dữ liệu thật — không chỉ là chạy được. Cụ thể: quyền truy cập được thực thi ở phía server, quy trình khôi phục backup đã được kiểm chứng, thanh toán không thể trừ tiền hai lần, giám sát cảnh báo bạn trước khi khách hàng phát hiện, và có căn cứ pháp lý cho mọi dữ liệu cá nhân được lưu."

**Schema bắt buộc:** `Service` + `HowTo` (cho checklist) + `FAQPage` + `BreadcrumbList`
**Link đi ra:** P1 (lên), P3, P4, P5, `/#packages`, `/#calculator`
**CTA chính:** `Bereken je prijs` / `Calculate your price` → `/#calculator`

> **⚠️ Lưu ý quan trọng về từ "productionize":** từ này **không có từ tương đương trong tiếng Hà Lan** và **tuyệt đối không được dịch máy móc thành *productionaliseren*** — từ đó không tồn tại. Thay vào đó, chèn đúng một câu tự nhiên vào trang tiếng Hà Lan: *"In het Engels heet dit 'productionize' of 'production-ready maken'."* Cách này bắt được người Hà Lan gõ thuật ngữ tiếng Anh mà không làm hỏng tín hiệu ngôn ngữ của trang.

---

### 📄 P3 — Bảo mật AI-code

| Trường | 🇳🇱 Tiếng Hà Lan | 🇬🇧 Tiếng Anh |
|---|---|---|
| **URL** | `/ai-code-beveiligen/` | `/en/ai-code-security/` |
| **Từ khóa chính** | `ai app beveiligen` | `ai generated app security` |
| **Từ khóa phụ** | `beveiliging ai applicatie`, `ai gegenereerde code beveiliging`, `is ai code veilig`, `datalek voorkomen applicatie` | `ai generated code security`, `secure ai generated code`, `lovable app security`, `supabase rls security` |
| **Ý định** | Thông tin → thương mại | Thông tin → thương mại |
| **Số từ** | 1.600–2.200 | 1,600–2,200 |
| **Loại trang** | Hướng dẫn + dịch vụ | Hướng dẫn + dịch vụ |

**Title tag**
- 🇳🇱 `AI-code beveiligen: de 7 lekken die het vaakst voorkomen` *(56)*
- 🇬🇧 `AI Code Security: The 7 Most Common Leaks | LaunchStudio` *(56)*

**Meta description**
- 🇳🇱 `AI-gegenereerde code lekt vaker data dan founders denken. De 7 meestvoorkomende lekken, hoe je ze zelf test en wat het kost om ze te dichten.` *(141)*
- 🇬🇧 `AI-generated code leaks data more often than founders expect. The 7 most common flaws, how to test for them yourself, and what a fix costs.` *(139)*

**H1**
- 🇳🇱 `AI-code beveiligen: de 7 lekken die we het vaakst vinden`
- 🇬🇧 `AI Code Security: The 7 Flaws We Find Most Often`

**Dàn ý heading**

| Cấp | 🇳🇱 Tiếng Hà Lan | 🇻🇳 Nghĩa tiếng Việt |
|---|---|---|
| H2 | Waarom AI-gegenereerde code structureel anders faalt | Vì sao code do AI sinh ra hỏng theo cách mang tính cấu trúc |
| H2 | De 7 lekken die we het vaakst aantreffen | 7 lỗ hổng chúng tôi gặp nhiều nhất |
| H3 | 1. Toegangsregels alleen in de frontend | 1. Quy tắc phân quyền chỉ nằm ở frontend |
| H3 | 2. Ontbrekende row-level security in Supabase | 2. Thiếu row-level security trong Supabase |
| H3 | 3. API-sleutels in de browserbundel | 3. API key nằm trong bundle trình duyệt |
| H3 | 4. Onbeperkte endpoints zonder rate limiting | 4. Endpoint không giới hạn, không rate limiting |
| H3 | 5. Bestandsuploads zonder validatie | 5. Upload file không kiểm tra |
| H3 | 6. Wachtwoordherstel dat accounts prijsgeeft | 6. Quên mật khẩu làm lộ tài khoản có tồn tại hay không |
| H3 | 7. Persoonsgegevens in logbestanden | 7. Dữ liệu cá nhân bị ghi vào log |
| H2 | Zelf testen: 5 controles zonder technische kennis | Tự kiểm tra: 5 bước không cần kiến thức kỹ thuật |
| H2 | AVG: wat een lek juridisch betekent | GDPR: một vụ rò rỉ có nghĩa gì về mặt pháp lý |
| H2 | Wat een beveiligingsronde kost | Chi phí một vòng gia cố bảo mật |
| H2 | Veelgestelde vragen | Câu hỏi thường gặp |

**Answer block (GEO)**
- 🇳🇱 *"AI-gegenereerde code is niet onveiliger door slechte code, maar doordat de beveiliging op de verkeerde plek staat: toegangsregels zitten in de frontend in plaats van in de database. De zeven lekken die wij het vaakst vinden zijn ontbrekende row-level security, sleutels in de browserbundel, endpoints zonder rate limiting, uploads zonder validatie, wachtwoordherstel dat accounts prijsgeeft en persoonsgegevens in logs."*
- 🇬🇧 *"AI-generated code is not insecure because the code is bad, but because the security sits in the wrong place: access rules live in the frontend instead of in the database. The seven flaws we find most often are missing row-level security, keys in the browser bundle, endpoints without rate limiting, unvalidated uploads, password reset that leaks account existence, and personal data written into logs."*
- 🇻🇳 *Nghĩa:* "Code do AI sinh ra không kém an toàn vì code tệ, mà vì **bảo mật nằm sai chỗ**: quy tắc phân quyền nằm ở frontend thay vì trong database. Bảy lỗ hổng chúng tôi gặp nhiều nhất là: thiếu row-level security, key nằm trong bundle trình duyệt, endpoint không rate limiting, upload không kiểm tra, quên mật khẩu làm lộ sự tồn tại của tài khoản, và dữ liệu cá nhân bị ghi vào log."

**Schema bắt buộc:** `Service` + `FAQPage` + `BreadcrumbList`
**Link đi ra:** P4 (audit — đường dẫn chuyển đổi), P1 (lên), P2, `/#contact`
**CTA chính:** `Laat je app controleren` / `Get your app checked` → P4, rồi `/#contact`

---

### 📄 P4 — Security audit ứng dụng 💰 MONEY PAGE

| Trường | 🇳🇱 Tiếng Hà Lan | 🇬🇧 Tiếng Anh |
|---|---|---|
| **URL** | `/security-audit-applicatie/` | `/en/application-security-audit/` |
| **Từ khóa chính** | `security audit applicatie` | `ai application security audit` |
| **Từ khóa phụ** | `beveiligingsaudit software`, `pentest webapplicatie`, `security audit saas`, `security audit kosten` | `web app security audit`, `saas security audit`, `penetration test web app`, `security audit cost` |
| **Ý định** | 💰 Giao dịch | 💰 Giao dịch |
| **Số từ** | 1.200–1.600 | 1,200–1,600 |
| **Loại trang** | Dịch vụ (ưu tiên chuyển đổi) | Dịch vụ (ưu tiên chuyển đổi) |

**Title tag**
- 🇳🇱 `Security audit applicatie | Vaste prijs, rapport in 5 dagen` *(59)*
- 🇬🇧 `Application Security Audit | Fixed Price, Report in 5 Days` *(58)*

**Meta description**
- 🇳🇱 `Onafhankelijke beveiligingsaudit van je webapplicatie of SaaS. Vaste prijs, rapport met prioriteiten in begrijpelijke taal, plus offerte om het te dichten.` *(155)*
- 🇬🇧 `Independent security audit of your web app or SaaS. Fixed price, a prioritised report in plain English, plus a fixed quote to close every gap found.` *(148)*

**H1**
- 🇳🇱 `Security audit voor je applicatie — vaste prijs, geen nacalculatie`
- 🇬🇧 `Security Audit for Your Application — Fixed Price, No Hourly Billing`

**Dàn ý heading**

| Cấp | 🇳🇱 Tiếng Hà Lan | 🇻🇳 Nghĩa tiếng Việt |
|---|---|---|
| H2 | Wat de audit precies onderzoekt | Audit kiểm tra chính xác những gì |
| H2 | Wat je krijgt: het rapport | Bạn nhận được gì: bản báo cáo |
| H2 | Wat het kost | Chi phí bao nhiêu |
| H2 | Ook voor AI-gebouwde applicaties (Lovable, Bolt, Cursor) | Áp dụng cả cho ứng dụng dựng bằng AI |
| H2 | Audit én herstel in één traject | Audit và khắc phục trong cùng một gói |
| H2 | Wie het uitvoert | Ai là người thực hiện |
| H2 | Wanneer je een audit nodig hebt | Khi nào bạn cần một cuộc audit |
| H3 | Voor een investeringsronde of due diligence | Trước vòng gọi vốn hoặc due diligence |
| H3 | Voor je eerste enterprise-klant | Trước khách hàng doanh nghiệp đầu tiên |
| H3 | Na een incident of verdenking | Sau một sự cố hoặc khi nghi ngờ |
| H2 | Veelgestelde vragen | Câu hỏi thường gặp |

**Answer block (GEO)**
- 🇳🇱 *"Een security audit van LaunchStudio onderzoekt toegangsrechten, dataopslag, authenticatie, afhankelijkheden en AVG-naleving van een webapplicatie of SaaS, inclusief applicaties gebouwd met AI-tools. Je ontvangt een rapport met geprioriteerde bevindingen in begrijpelijke taal plus een vaste offerte om ze te herstellen. Vaste prijs vanaf €500, rapport binnen 5 werkdagen."*
- 🇬🇧 *"A LaunchStudio security audit examines access control, data storage, authentication, dependencies and GDPR compliance of a web application or SaaS, including applications built with AI tools. You receive a prioritised report in plain language plus a fixed quote to remediate every finding. Fixed price from €500, report within 5 working days."*
- 🇻🇳 *Nghĩa:* "Một cuộc security audit của LaunchStudio kiểm tra phân quyền truy cập, lưu trữ dữ liệu, xác thực, các thư viện phụ thuộc và mức tuân thủ GDPR của một web app hoặc SaaS, bao gồm cả ứng dụng dựng bằng tool AI. Bạn nhận báo cáo các phát hiện đã sắp xếp theo mức ưu tiên, viết bằng ngôn ngữ dễ hiểu, kèm báo giá cố định để khắc phục. Giá cố định từ €500, báo cáo trong 5 ngày làm việc."

**Schema bắt buộc:** `Service` + `Offer` (kèm `priceRange`) + `FAQPage` + `BreadcrumbList` + `AggregateRating` *(chỉ khi có review thật — tuyệt đối không bịa)*
**Link đi ra:** P3 (ngữ cảnh), P1 (lên), `/#contact`
**Link đi vào:** P1, P2, P3, P5 + mọi bài viết chủ đề bảo mật
**CTA chính:** `Vraag een audit aan` / `Request an audit` → `/#contact`

> **Đây là trang có giá trị cao nhất trong cụm:** "audit" là một từ khóa mang ý định mua hàng rõ ràng. Hãy cho nó lộ trình chuyển đổi ngắn nhất — form ngay trên màn hình đầu, giá hiển thị công khai trên trang, không che giấu sau bất kỳ rào cản nào.

---

### 📄 P5 — Làm ứng dụng có khả năng mở rộng

| Trường | 🇳🇱 Tiếng Hà Lan | 🇬🇧 Tiếng Anh |
|---|---|---|
| **URL** | `/applicatie-schaalbaar-maken/` | `/en/application-scalability/` |
| **Từ khóa chính** | `applicatie schaalbaar maken` | `ai application scalability` |
| **Từ khóa phụ** | `schaalbaarheid applicatie`, `applicatie traag bij veel gebruikers`, `database performance verbeteren` | `ai app scalability`, `app slow with many users`, `prototype breaks at scale` |
| **Ý định** | Cân nhắc | Cân nhắc |
| **Số từ** | 1.400–1.800 | 1,400–1,800 |
| **Loại trang** | Hướng dẫn + dịch vụ | Hướng dẫn + dịch vụ |

**Title tag**
- 🇳🇱 `Applicatie schaalbaar maken: van 10 naar 10.000 gebruikers` *(58)*
- 🇬🇧 `Application Scalability: From 10 to 10,000 Users` *(48)*

**Meta description**
- 🇳🇱 `Waarom een prototype breekt bij 1.000 gebruikers en niet bij 10. De vijf knelpunten, hoe je ze meet en wat het kost om ze op te lossen.` *(135)*
- 🇬🇧 `Why a prototype breaks at 1,000 users and not at 10. The five bottlenecks, how to measure them, and what it costs to remove them.` *(129)*

**H1**
- 🇳🇱 `Applicatie schaalbaar maken: waarom prototypes breken bij groei`
- 🇬🇧 `Application Scalability: Why Prototypes Break as They Grow`

**Dàn ý heading**

| Cấp | 🇳🇱 Tiếng Hà Lan | 🇻🇳 Nghĩa tiếng Việt |
|---|---|---|
| H2 | Waarom het werkt bij 10 gebruikers en niet bij 1.000 | Vì sao chạy tốt với 10 người mà hỏng với 1.000 |
| H2 | De vijf knelpunten, op volgorde van hoe vaak ze voorkomen | Năm nút thắt, xếp theo tần suất gặp phải |
| H3 | 1. Een query per rij in plaats van één query | 1. Một query cho mỗi dòng thay vì một query duy nhất |
| H3 | 2. Ontbrekende database-indexen | 2. Thiếu index trong database |
| H3 | 3. Geen paginering op lijsten | 3. Danh sách không phân trang |
| H3 | 4. Berekeningen bij elke paginaweergave | 4. Tính toán tổng hợp lại ở mỗi lần tải trang |
| H3 | 5. Zwaar werk in het verzoek in plaats van in de achtergrond | 5. Việc nặng chạy trong request thay vì chạy nền |
| H2 | Zelf meten: waar je het ziet voordat klanten het merken | Tự đo: nhìn ở đâu để thấy trước khi khách hàng thấy |
| H2 | Wat je nú moet bouwen en wat kan wachten | Cái gì phải làm ngay, cái gì để sau |
| H2 | Wat het kost om het op te lossen | Chi phí để khắc phục |
| H2 | Veelgestelde vragen | Câu hỏi thường gặp |

**Answer block (GEO)**
- 🇳🇱 *"Een prototype breekt bij groei zelden door de hoeveelheid gebruikers, maar door vijf patronen die bij tien records onzichtbaar zijn: één databasequery per rij, ontbrekende indexen, lijsten zonder paginering, totalen die bij elke weergave opnieuw worden berekend, en zwaar werk dat in het webverzoek draait in plaats van op de achtergrond."*
- 🇬🇧 *"A prototype rarely breaks at scale because of user numbers, but because of five patterns that are invisible at ten records: one database query per row, missing indexes, lists without pagination, totals recomputed on every page view, and heavy work running inside the web request instead of in the background."*
- 🇻🇳 *Nghĩa:* "Một prototype hiếm khi vỡ khi mở rộng vì số lượng người dùng, mà vì năm mẫu lỗi vốn vô hình khi chỉ có mười bản ghi: một truy vấn database cho mỗi dòng, thiếu index, danh sách không phân trang, các con số tổng bị tính lại ở mỗi lần tải trang, và việc nặng chạy bên trong web request thay vì chạy nền."

**Schema bắt buộc:** `Service` + `FAQPage` + `BreadcrumbList`
**Link đi ra:** P1 (lên), P2, P4, `/#calculator`
**CTA chính:** `Bereken je prijs` / `Calculate your price` → `/#calculator`

---

<a id="5"></a>
## 5. 📚 Tận Dụng 800 Bài Viết Đã Có

Thư viện bài viết đã được viết xong rồi; vấn đề là phần lớn **chưa xuất bản** và gần như **không được liên kết**. Mỗi bài hỗ trợ cần link **lên** đúng một trang pillar bằng anchor text mô tả. Chỉ riêng thay đổi đó đã biến một kho lưu trữ phẳng thành một cụm chủ đề mà Google đọc được.

### 5.1 Ánh xạ bài viết → pillar (ví dụ từ thư viện thật)

| Pillar | Bài viết hỗ trợ đã viết sẵn |
|---|---|
| **P1** Prototype → production | `extra-9-decision/11-you-built-it-in-lovable-the-exact-gaps-to-production.md`<br>`extra-9-decision/13-your-cursor-codebase-works-production-readiness-review.md`<br>`extra-9-decision/15-replit-deployed-it-why-thats-not-launched.md`<br>`extra-7-longtail/31-how-to-make-your-own-ai-app-production.md`<br>`extra-6-random/52-ai-deployment-day-checklist.md` |
| **P2** Production-ready | `extra-8-decision/19-what-production-ready-really-costs-pricing-breakdown.md`<br>`extra-6-random/35-production-readiness-score-measures.md`<br>`extra-9-decision/21-launching-an-ai-wrapper-what-production-ready-means.md`<br>`extra-6-random/25-rejected-enterprise-deal-not-production-ready.md`<br>`extra-10-decision/82-deploying-changes-without-holding-your-breath.md` |
| **P3** Bảo mật AI-code | `extra-7-longtail/15-where-security-in-ai-generated-code-usually-breaks.md`<br>`extra-7-longtail/16-ai-and-security-the-gap-every-founder-discovers.md`<br>`extra-6-random/01-security-means-different-things.md`<br>`extra-8-decision/88-ssl-certificate-easy-part-real-security-work.md`<br>`extra-10-decision/19-logging-what-to-record-and-what-you-must-never-write-down.md` |
| **P4** Security audit 💰 | `extra-9-decision/34-what-a-real-security-audit-report-looks-like.md`<br>`extra-8-decision/33-non-technical-founder-reads-security-audit-case-study.md`<br>`extra-9-decision/60-your-first-enterprise-security-questionnaire.md`<br>`extra-8-decision/13-enterprise-security-review-without-rebuilding-frontend-case-study.md`<br>`extra-6-random/04-acronym-cheat-sheet-security-review.md` |
| **P5** Khả năng mở rộng | `extra-8-decision/57-what-founders-get-wrong-about-scalable-architecture.md`<br>`extra-8-decision/43-prototype-survives-viral-traffic-spike-case-study.md`<br>`extra-10-decision/88-performance-when-your-biggest-customer-arrives.md`<br>`extra-10-decision/18-caching-decisions-before-your-first-traffic-spike.md`<br>`extra-8-decision/53-why-prototype-database-schema-breaks-at-1000-users.md` |

### 5.2 Thứ tự ưu tiên xuất bản

Với 71/800+ bài đang live, **thứ tự quan trọng hơn số lượng**. Hãy xuất bản theo trình tự sau:

1. **5 trang pillar trước tiên** (§4) — chúng là đích đến của link; xuất bản bài hỗ trợ trước sẽ lãng phí toàn bộ giá trị liên kết nội bộ.
2. **5 bài hỗ trợ cho mỗi pillar** (tổng 25 bài) — đủ để thiết lập cụm; mỗi bài link lên ngay khi xuất bản.
3. **Các case study có tên founder và kết quả cụ thể** — đây là tài sản dễ được AI trích dẫn nhất (§8) và thuyết phục người mua mạnh nhất.
4. **Phần còn lại**, với nhịp đều 2–3 bài/tuần. Audit đã chỉ đích danh việc xuất bản dồn dập theo đợt là mẫu cần tránh.

### 5.3 Quy tắc anchor text

| ❌ Tuyệt đối tránh | ✅ Luôn dùng |
|---|---|
| `klik hier`, `lees meer`, `deze pagina` | `applicatie productieklaar maken` |
| `click here`, `read more`, `this page` | `AI prototype to production` |
| Dùng y hệt một anchor trên mọi bài viết | Đa dạng tự nhiên: khớp chính xác, khớp một phần, và dạng thương hiệu |
| Hơn 3 link về cùng một trang trong một bài | 1–2 link theo ngữ cảnh mỗi bài, đặt trong phần thân |

> **Đừng quên chiều ngược lại:** từ mỗi pillar phải có link **xuống** 4–6 bài hỗ trợ tốt nhất. Liên kết một chiều (chỉ spoke → hub) là lỗi phổ biến và hoàn toàn tránh được; Google đọc chính **cấu trúc hai chiều** để xác định ranh giới của cụm.

---

<a id="6"></a>
## 6. 🏛️ Kế Hoạch Entity & Schema.org

Đây là **ưu tiên số 1 của toàn bộ kế hoạch**. Audit ngày 31/07/2026 phát hiện: **không có `Organization` schema ở bất kỳ đâu trên site**, không có `sameAs`, không có `FAQPage` dù homepage đã chứa sẵn một mục FAQ đầy đủ dạng HTML thuần, và node `Person` trên blog có tên tác giả là username nội bộ `"phu.lt"`.

Chừng nào chưa sửa, cả Google lẫn mọi LLM đều phải **đoán** LaunchStudio là ai — và không bên nào đoán theo hướng có lợi cho bạn.

### 6.1 `Organization` — toàn site (ưu tiên cao nhất) 🥇

Đặt một lần, toàn site, trong `<head>` của mọi trang. Đây là node thiết lập thực thể, quan hệ thương hiệu mẹ với Manifera, và địa chỉ Amsterdam.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://launchstudio.eu/#organization",
  "name": "LaunchStudio",
  "alternateName": ["Launch Studio", "Launch Studio door Manifera"],
  "url": "https://launchstudio.eu/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://launchstudio.eu/wp-content/uploads/launchstudio-logo.png",
    "width": 512,
    "height": 512
  },
  "description": "LaunchStudio takes AI-generated prototypes from tools such as Lovable, Bolt and Cursor to production: security, payments, authentication, database, hosting and deployment. Fixed price EUR 800-7,500, live in 1-3 weeks.",
  "slogan": "Launch Your Real Ideas to the Real World",
  "foundingDate": "2026",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Manifera Software Development Pte Ltd",
    "url": "https://www.manifera.com/"
  },
  "founder": {
    "@type": "Person",
    "@id": "https://launchstudio.eu/#herre-roelevink"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Herengracht 420",
    "postalCode": "1017 BZ",
    "addressLocality": "Amsterdam",
    "addressCountry": "NL"
  },
  "areaServed": [
    { "@type": "Country", "name": "Netherlands" },
    { "@type": "Country", "name": "Belgium" },
    { "@type": "Place", "name": "European Union" }
  ],
  "knowsAbout": [
    "AI prototype to production",
    "production readiness",
    "application security audit",
    "AI-generated code security",
    "Lovable", "Bolt", "Cursor", "Replit", "v0",
    "Supabase", "Stripe", "GDPR compliance"
  ],
  "sameAs": [
    "https://www.manifera.com/",
    "FILL_IN: https://www.linkedin.com/company/…",
    "FILL_IN: X / Facebook / Instagram profile URLs if they exist"
  ]
}
```

> **⚠️ CẢNH BÁO:** `sameAs` chỉ được chứa **những profile thật sự tồn tại và do LaunchStudio sở hữu**. Một URL bịa hoặc sai **làm hỏng độ tin cậy thực thể** — tệ hơn cả để mảng rỗng. Nếu LaunchStudio chưa có trang công ty trên LinkedIn, thì việc tạo trang đó tự nó đã là một đầu việc entity có giá trị cao.

### 6.2 `Person` — sửa node tác giả 🥇

Thay thế `"name": "phu.lt"` trên mọi bài blog. Tiêu chí E-E-A-T đánh giá **ai là người viết**; một username nội bộ là tín hiệu của site không được chăm sóc. Đồng thời thêm node CEO ở cấp toàn site, vì ông là gương mặt đại diện công khai của thực thể.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://launchstudio.eu/#herre-roelevink",
  "name": "Herre Roelevink",
  "jobTitle": "Founder & Managing Director",
  "description": "Founder of Manifera and CEO of LaunchStudio. Background in Agile/Scrum, offshore software management and cybersecurity. Co-founder of CyberDevOps, now CFLW Cyber Strategies, which developed the Dark Web Monitor with TNO.",
  "worksFor": { "@id": "https://launchstudio.eu/#organization" },
  "nationality": { "@type": "Country", "name": "Netherlands" },
  "sameAs": [
    "https://www.linkedin.com/in/herre-roelevink-director-manifera/"
  ]
}
```

### 6.3 `Service` + `Offer` — cho từng trang trong 5 trang 🥈

Mỗi money page một node `Service`. Giá là một trong những thứ người dùng hỏi trợ lý AI nhiều nhất, và một `Offer` có `priceRange` thật thì trích xuất được trực tiếp. Ví dụ cho **P4 (security audit)**:

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://launchstudio.eu/security-audit-applicatie/#service",
  "name": "Security audit voor webapplicaties en SaaS",
  "serviceType": "Application security audit",
  "provider": { "@id": "https://launchstudio.eu/#organization" },
  "areaServed": { "@type": "Country", "name": "Netherlands" },
  "audience": {
    "@type": "Audience",
    "audienceType": "Startups and scale-ups with AI-generated applications"
  },
  "description": "Onafhankelijke beveiligingsaudit van een webapplicatie of SaaS, inclusief applicaties gebouwd met AI-tools zoals Lovable, Bolt of Cursor. Rapport met geprioriteerde bevindingen plus vaste offerte voor herstel.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "500",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "500",
      "maxPrice": "3500",
      "priceCurrency": "EUR",
      "valueAddedTaxIncluded": false
    },
    "availability": "https://schema.org/InStock",
    "url": "https://launchstudio.eu/security-audit-applicatie/"
  }
}
```

**Lặp lại với các giá trị sau:**

| Trang | `name` | `price` | `priceRange` |
|---|---|---|---|
| P1 | Van AI-prototype naar productie | 800 | €800 – €7.500 |
| P2 | Applicatie productieklaar maken | 800 | €800 – €3.500 |
| P3 | Beveiliging van AI-gegenereerde code | 500 | €500 – €2.000 |
| P4 | Security audit applicatie | 500 | €500 – €3.500 |
| P5 | Applicatie schaalbaar maken | 800 | €800 – €4.500 |

> **Chỉ công bố mức giá bạn sẽ thực sự tôn trọng.** Một `priceRange` mâu thuẫn với máy tính giá trên trang là vấn đề niềm tin — với cả người dùng lẫn Google.

### 6.4 `FAQPage` — homepage + cả 5 trang 🥇

Homepage đã có sẵn mục FAQ đầy đủ dạng HTML thuần ("Wat kost het precies?", "Blijft mijn code van mij?") nhưng **chưa được đánh dấu schema**. Đánh dấu chỉ tốn khoảng một giờ và đây là định dạng được AI trích xuất đáng tin cậy nhất cho câu trả lời trực tiếp. Mỗi trang trong 5 trang mới cũng kết thúc bằng mục FAQ riêng, đánh dấu theo cách tương tự.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost het om een AI-prototype productieklaar te maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij LaunchStudio kost dit een vaste prijs tussen €800 en €7.500, afhankelijk van wat er gebouwd moet worden en wat er al werkt. Je krijgt de offerte na een gesprek van 15 minuten, met vaste scope en vaste doorlooptijd van 1 tot 3 weken."
      }
    },
    {
      "@type": "Question",
      "name": "Blijft mijn code van mij?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Alle code blijft 100% eigendom van de opdrachtgever, tijdens en na het traject. Er is geen licentieconstructie en geen lock-in."
      }
    }
  ]
}
```

### 6.5 Checklist triển khai schema

- [ ] `Organization` trong `<head>` toàn site, `@id` chính xác
- [ ] Node `Person` cho Herre Roelevink; thay tác giả blog (không bao giờ để `phu.lt`)
- [ ] `Service` + `Offer` trên từng trang P1–P5
- [ ] `FAQPage` trên homepage **và** trên P1–P5
- [ ] `BreadcrumbList` trên mọi trang mới
- [ ] Giữ nguyên `WebSite` kèm `SearchAction` (đã có sẵn)
- [ ] Mọi node liên kết với nhau qua `@id` — **một đồ thị liền mạch**, không phải năm mảnh rời rạc
- [ ] Đã kiểm tra bằng Google Rich Results Test **và** Schema.org validator
- [ ] ❌ Không dùng `AggregateRating` nếu chưa có review thật, kiểm chứng được

---

<a id="7"></a>
## 7. 📍 GEO-Entity — Định Vị Địa Lý

Trong dự án này, "GEO-entity" mang **hai nghĩa cùng lúc**, và cả hai đều quan trọng. §8 xử lý Generative Engine Optimization; mục này xử lý **thực thể địa lý** — làm cho LaunchStudio trở thành một công ty **Hà Lan** một cách rõ ràng trong mắt Google, đây chính là điều cho phép nó cạnh tranh với các agency bản địa trên các truy vấn thương mại tiếng Hà Lan.

### 7.1 Vấn đề nhất quán NAP

NAP = Name (Tên), Address (Địa chỉ), Phone (Điện thoại). Google đối chiếu chéo ba thông tin này trên toàn web để xác nhận doanh nghiệp có thật và đặt ở nơi nó tuyên bố.

LaunchStudio thừa hưởng ba văn phòng từ Manifera, và sự thừa hưởng đó **vừa là tài sản vừa là rủi ro**: nếu địa chỉ Amsterdam chỉ xuất hiện trên site của Manifera mà không bao giờ xuất hiện trên site của chính LaunchStudio, Google có thể coi LaunchStudio là một thương hiệu con **không có vị trí xác định**.

| Thành phần | Giá trị dùng thống nhất ở mọi nơi |
|---|---|
| **Name** | `LaunchStudio` (trong structured data không bao giờ dùng `Launch Studio` — chọn một dạng và không đổi) |
| **Address** | `Herengracht 420, 1017 BZ Amsterdam, Nederland` |
| **Country** | `NL` |
| **Parent** | `Manifera Software Development Pte Ltd` |
| **Phone** | ⚠️ `CẦN BỔ SUNG` — số Hà Lan (+31) là tín hiệu tin cậy bản địa đáng kể; số nước ngoài làm suy yếu tín hiệu này |

### 7.2 Tín hiệu thực thể Hà Lan phải xuất hiện ở đâu

| # | Vị trí | Hành động | Ưu tiên |
|---|---|---|---|
| 1 | Footer, trên mọi trang | Khối NAP đầy đủ dạng **text HTML** (không phải ảnh) | 🔴 |
| 2 | `Organization` schema | `address` + `addressCountry: NL` (§6.1) | 🔴 |
| 3 | Mục liên hệ | Hiển thị địa chỉ Amsterdam, không chỉ có form | 🔴 |
| 4 | Google Business Profile | Tạo/xác nhận sở hữu cho địa điểm Amsterdam | 🟡 |
| 5 | Trang công ty LinkedIn | Đặt vị trí là Amsterdam, Netherlands | 🟡 |
| 6 | Manifera.com | Link tới launchstudio.eu, mô tả là dịch vụ launch tại Hà Lan | 🟡 |
| 7 | Thư mục doanh nghiệp Hà Lan | Hồ sơ KvK, các directory startup Hà Lan, hồ sơ BNI | 🟢 |
| 8 | Nội dung trang | Nhắc Amsterdam / Nederland một cách tự nhiên trong thân bài P1–P5 | 🟢 |

> **Điểm số 6 đã được audit nêu đích danh:** homepage có ghi "door Manifera" nhưng **không đặt hyperlink**. Chỉ một link từ `manifera.com` sang `launchstudio.eu` — và ngược lại — biến hai site rời rạc thành **một đồ thị thực thể duy nhất** với 11 năm thẩm quyền tích lũy phía sau. Đây là khoản lợi thẩm quyền rẻ nhất có thể có.

### 7.3 Độ liên quan địa phương mà không tạo trang "địa phương" giả

Cụm `extra-5-local` đã chứa sẵn các bài nhắm theo thành phố (Amsterdam, Utrecht, Arnhem, Nijmegen…). Những bài đó hỗ trợ truy vấn long-tail địa phương và **nên link lên P1–P5**.

Điều **tuyệt đối không được làm** là nhân bản năm trang money page thành 40 biến thể thành phố gần giống nhau — Google coi các trang thành phố sinh tự động với nội dung trùng lặp là **doorway page**, và án phạt áp lên toàn site.

---

<a id="8"></a>
## 8. 🤖 GEO — Tối Ưu Cho Công Cụ Trả Lời AI

GEO là việc tối ưu để **được trích dẫn bởi** ChatGPT, Perplexity, Claude và Google AI Overviews, thay vì được click trong danh sách link xanh. Nó tưởng thưởng một bộ đặc tính khác với SEO truyền thống: độ rõ ràng của thực thể, các phát biểu trích dẫn trực tiếp được, con số cụ thể, bảng so sánh, và HTML render sẵn ở phía server.

Audit đã xác định hai điểm mạnh sẵn có (nội dung render phía server, đã có file `llms.txt`) và một điểm yếu mang tính quyết định (độ rõ ràng thực thể — đã xử lý ở §6).

### 8.1 Answer block — kỹ thuật GEO có đòn bẩy cao nhất

Ngay **dưới mỗi H1**, đặt một **đoạn văn 40–60 từ trả lời trọn vẹn câu hỏi cốt lõi của trang, tự nó đứng được, và có chứa một con số**.

Các LLM trích xuất những đoạn văn **tự chứa**; một đoạn cần đọc phần xung quanh mới hiểu được thì sẽ không được trích dẫn. Cả năm brief ở §4 đều đã có sẵn answer block, dán được ngay.

| ✅ Trích dẫn được | ❌ Không trích dẫn được |
|---|---|
| "Đưa AI prototype lên production mất 1–3 tuần và tốn €800–€7.500." | "Còn tùy tình huống của bạn — đọc tiếp để biết thêm." |
| Có con số, có khung thời gian, có tên thực thể cụ thể | Mơ hồ, mang tính so sánh, hoặc phụ thuộc ngữ cảnh phía trước |
| Một ý duy nhất, hoàn chỉnh trong chính nó | "Như đã nói ở trên…", "Đây là lúc chúng tôi vào cuộc…" |

### 8.2 Các prompt cần nhắm tới

Trong GEO bạn tối ưu cho **prompt**, không phải keyword. Đây là những câu hỏi thật mà một founder Hà Lan đặt cho trợ lý AI, mỗi câu ánh xạ tới một trang bắt buộc phải trả lời được nó.

| Prompt (như người dùng gõ vào trợ lý AI) | Trang phải trả lời |
|---|---|
| "My Lovable app works but I can't launch it — what's missing?" | P1 |
| "Wat betekent productieklaar voor een webapplicatie?" | P2 |
| "Is code generated by AI tools secure enough for production?" | P3 |
| "Hoeveel kost een security audit voor een SaaS in Nederland?" | P4 |
| "Why does my app get slow after 1,000 users?" | P5 |
| "Who can take an AI prototype to production in the Netherlands?" | P1 + `Organization` (§6) |
| "What does LaunchStudio cost?" | `FAQPage` homepage + `Offer` (§6) |

### 8.3 Viết lại `llms.txt`

File hiện tại là bản Yoast tự sinh: liệt kê 5/71 bài, có cả văn bản pháp lý mẫu, và **không hề nhắc tới giá, gói dịch vụ hay giá trị cốt lõi**. Một LLM chỉ đọc file này sẽ **không biết LaunchStudio bán gì**. Hãy thay bằng một file được biên soạn thủ công, mở đầu bằng chính lời chào hàng.

> *Nội dung dưới đây giữ nguyên tiếng Anh vì đây là file thật sẽ đặt lên server.*

```markdown
# LaunchStudio

> LaunchStudio takes AI-generated prototypes to production. Founders build in
> Lovable, Bolt, Cursor, Replit or v0; LaunchStudio adds the security, database,
> payments, hosting and deployment work needed to launch, without rebuilding the
> frontend. Fixed price EUR 800-7,500, live in 1-3 weeks. Based in Amsterdam,
> the Netherlands. Part of Manifera Software Development, 11+ years of
> engineering experience, 160+ delivered projects.

## What we do
- Prototype to production: https://launchstudio.eu/van-prototype-naar-productie/
- Production-ready checklist: https://launchstudio.eu/productieklaar-maken/
- AI code security: https://launchstudio.eu/ai-code-beveiligen/
- Application security audit: https://launchstudio.eu/security-audit-applicatie/
- Application scalability: https://launchstudio.eu/applicatie-schaalbaar-maken/

## Pricing
- Launch Ready (Klaar voor lancering): EUR 800-3,500 fixed price
- Launch & Grow (Lancering & Groei): EUR 2,500-7,500 fixed price + EUR 49/month
- Security audit: from EUR 500
- Price calculator: https://launchstudio.eu/#calculator
- All code remains 100% owned by the client.

## How it works
1. Describe your product (no technical knowledge required)
2. 15-minute intro call, then a fixed-price quote with fixed scope
3. We build, you launch - typically 1-3 weeks

## Who we serve
AI-native founders, technical solo founders, agencies needing a white-label
engineering partner, and SaaS scale-ups. Primary market: the Netherlands,
Belgium and the wider EU.

## Company
LaunchStudio (Launch Studio door Manifera)
Herengracht 420, 1017 BZ Amsterdam, Netherlands
Parent company: Manifera Software Development Pte Ltd - https://www.manifera.com/
Founder & CEO: Herre Roelevink
Enterprise clients of the parent company include Vodafone, TNO and CFLW.

## Key articles
[liệt kê 20-30 bài viết mạnh nhất đã xuất bản, kèm tiêu đề + URL]
```

### 8.4 Các đòn bẩy GEO khác

| Đòn bẩy | Hành động | Vì sao |
|---|---|---|
| **Bảng so sánh** | Mỗi money page một bảng (LaunchStudio vs agency vs freelancer vs tự làm) | LLM trích xuất bảng đáng tin cậy hơn nhiều so với văn xuôi |
| **Con số cụ thể** | €800, 1–3 tuần, 11+ năm, 160+ dự án, checklist 24 điểm | Con số là thứ được trích dẫn nguyên văn |
| **Case study có tên** | Tên founder, sản phẩm, vấn đề, kết quả, thời gian | Tính cụ thể là tín hiệu "đáng trích dẫn" mạnh nhất |
| **Khối định nghĩa** | Định nghĩa rõ "productieklaar" / "production-ready" trên P2 | Truy vấn dạng định nghĩa được AI trả lời rất nhiều |
| **Không phụ thuộc JS** | Giữ các dữ kiện quan trọng trong HTML render phía server | Đa số crawler của LLM **không chạy JavaScript** |
| **`robots.txt`** | **Không** chặn `GPTBot`, `ClaudeBot`, `PerplexityBot` | Chặn chúng là tự loại mình khỏi tập câu trả lời |
| **Độ mới** | Hiển thị `dateModified` rõ ràng trên mọi trang | Độ mới có trọng số trong việc chọn nguồn của AI |

### 8.5 Cách đo lường GEO

Không tồn tại "Search Console cho câu trả lời AI", nên việc đo là **thủ công và so sánh**. Chạy quy trình này mỗi tháng một lần:

1. Đặt 7 prompt ở §8.2 vào **ChatGPT, Perplexity, Claude và Google AI Overviews**, bằng cả tiếng Hà Lan và tiếng Anh.
2. Ghi nhận: LaunchStudio có được nhắc tới không? có kèm link nguồn không? URL nào? đối thủ nào được trích dẫn thay thế?
3. Theo dõi traffic giới thiệu từ `chat.openai.com`, `perplexity.ai`, `claude.ai` trong GA4 như tín hiệu phụ.
4. Lưu kết quả trong một bảng tính đơn giản — **xu hướng qua các tháng** mới là thước đo, không phải một câu trả lời đơn lẻ.

---

<a id="9"></a>
## 9. 🌐 Chiến Lược Song Ngữ & hreflang

Cả năm trang đều tồn tại hai bản: **tiếng Hà Lan ở thư mục gốc**, **tiếng Anh dưới `/en/`**. Bản tiếng Hà Lan là bản canonical cho thị trường Hà Lan; bản tiếng Anh phục vụ cả người Hà Lan gõ tiếng Anh lẫn khán giả EU rộng hơn.

### 9.1 Triển khai hreflang

```html
<!-- Trên trang tiếng Hà Lan -->
<link rel="alternate" hreflang="nl-NL" href="https://launchstudio.eu/productieklaar-maken/" />
<link rel="alternate" hreflang="en"    href="https://launchstudio.eu/en/production-ready/" />
<link rel="alternate" hreflang="x-default" href="https://launchstudio.eu/en/production-ready/" />
<link rel="canonical" href="https://launchstudio.eu/productieklaar-maken/" />
```

| Quy tắc | Nội dung |
|---|---|
| **Đối ứng** | Hai trang phải trỏ lẫn nhau, nếu không Google bỏ qua cả cặp |
| **Tự tham chiếu** | Mỗi trang phải chứa `hreflang` của chính nó |
| **Canonical** | Luôn tự-canonical, **không bao giờ** canonical chéo ngôn ngữ |
| **`x-default`** | Trỏ về bản tiếng Anh (khán giả rộng nhất) |
| **❌ Tránh** | Không dùng `nl-BE` trừ khi thực sự có một trang riêng cho Bỉ |

### 9.2 Dịch ≠ bản địa hóa

Trang tiếng Anh **không phải** bản dịch máy của trang tiếng Hà Lan. Ba điểm khác nhau có chủ đích:

- **Thuật ngữ:** trang Hà Lan dùng *productieklaar* và nhắc **một lần** *"in het Engels: production-ready"*. Trang tiếng Anh dùng *production-ready* và *productionize* — hai từ không có tương đương tiếng Hà Lan.
- **Khung tuân thủ:** trang Hà Lan mở đầu bằng **AVG**; trang tiếng Anh mở đầu bằng **GDPR** và thêm một câu về nơi lưu trữ dữ liệu trong EU, điều quan trọng hơn với độc giả EU không phải người Hà Lan.
- **Bằng chứng:** trang Hà Lan nhấn mạnh Amsterdam và khách hàng Hà Lan; trang tiếng Anh nhấn mạnh bề dày toàn EU của công ty mẹ.

---

<a id="10"></a>
## 10. 🔧 Điều Kiện Kỹ Thuật SEO Bắt Buộc

Các mục dưới đây lấy trực tiếp từ audit ngày 31/07/2026 và là **rào cản chặn đường**: năm trang mới sẽ hoạt động kém cho tới khi chúng được sửa, vì đây là lỗi ở cấp toàn site.

| # | Vấn đề từ audit | Cách sửa | Công sức | Ưu tiên |
|---|---|---|---|---|
| 1 | Khối OG/meta-description bị hardcode trùng lặp trong header theme — thẻ meta trùng, sai chuẩn, trên toàn site | Xóa khối hardcode; để Yoast tự xuất | 1h | 🔴 |
| 2 | `<title>` homepage bản EN dài 131 ký tự và trùng nội dung với meta description | Viết lại ≤60 ký tự | 15p | 🔴 |
| 3 | Thẻ `rel="next"` thừa trên homepage | Xóa | 15p | 🟢 |
| 4 | Chữ `"door Manifera"` không được đặt link | Link tới `manifera.com` (§7.2) | 15p | 🔴 |
| 5 | Không có `Organization` schema | §6.1 | 2h | 🔴 |
| 6 | FAQ trên homepage chưa đánh dấu `FAQPage` | §6.4 | 1h | 🔴 |
| 7 | Schema tác giả ghi `"phu.lt"` | §6.2 | 1h | 🔴 |
| 8 | Không có `Service`/`Offer` schema | §6.3 | 2h | 🟡 |
| 9 | `llms.txt` sơ sài, không có thông tin chào hàng | §8.3 | 2h | 🟡 |
| 10 | Nhiều bài viết quá mỏng (đặc biệt case study) | Mở rộng lên 800–1.200 từ | Liên tục | 🟡 |
| 11 | TTFB / Core Web Vitals | Bật cache trang + CDN | 4h | 🟡 |
| 12 | 71 bài live trên 800+ đã sản xuất | Nhịp xuất bản đều (§5.2) | Liên tục | 🔴 |

### 10.1 Kiểm tra riêng cho 5 trang mới

- [ ] Cho phép index: không có `noindex`, có mặt trong `sitemap.xml`
- [ ] Tự-canonical + `hreflang` đối ứng (§9.1)
- [ ] Đúng một `<h1>` mỗi trang, các heading theo thứ bậc
- [ ] LCP < 2,5 giây trên mobile
- [ ] Mọi ảnh có `alt` mô tả và đã nén
- [ ] Answer block (§8.1) nằm trong HTML render phía server, không phải do JS chèn
- [ ] Schema pass Rich Results Test
- [ ] Đã submit trong Search Console sau khi xuất bản

---

<a id="11"></a>
## 11. 🔗 Quy Tắc Liên Kết Nội Bộ

| Chiều liên kết | Quy tắc |
|---|---|
| **Homepage → pillar** | Link P1 từ **menu chính**, không chỉ từ footer |
| **Pillar → trang con** | P1 link tới P2, P3, P4, P5 trong thân bài, dùng anchor chứa từ khóa |
| **Trang con → pillar** | Mỗi trang con link ngược lên P1 trong **300 từ đầu tiên** |
| **Trang con ↔ trang con** | P3 → P4 là **đường chuyển đổi then chốt** (lo ngại bảo mật → mua audit) |
| **Bài viết → pillar** | Mỗi bài hỗ trợ link lên **đúng một** pillar, **một lần**, trong thân bài |
| **Pillar → bài viết** | Mỗi pillar link xuống 4–6 bài hỗ trợ mạnh nhất |
| **Bất kỳ → Manifera** | Ít nhất một link theo ngữ cảnh tới `manifera.com` trên mỗi money page (§7.2) |
| **Độ sâu** | Không money page nào cách homepage quá 2 cú click |

> **Đừng thay link ngữ cảnh bằng widget "bài viết liên quan".** Widget tự động truyền tín hiệu yếu hơn nhiều so với một link nằm trong câu văn giải thích vì sao người đọc nên bấm vào.

---

<a id="12"></a>
## 12. 📅 Lịch Triển Khai 90 Ngày

### Tuần 1–2 · Nền móng
| # | Công việc | Người phụ trách | Kết quả bàn giao |
|---|---|---|---|
| 1 | Sửa các mục 1–4, 7 từ audit (§10) | Dev | Meta sạch, tác giả thật, có link Manifera |
| 2 | Triển khai `Organization` + `Person` schema (§6.1, §6.2) | Dev | Pass Rich Results Test |
| 3 | Đánh dấu FAQ homepage thành `FAQPage` (§6.4) | Dev | Đã validate |
| 4 | Tạo/nhận LinkedIn company page + Google Business Profile | Marketing | Có URL `sameAs` thật |
| 5 | Chốt URL và slug cuối cùng (§3.1) | Marketing | Danh sách URL đã duyệt |

### Tuần 3–5 · Money page
| # | Công việc | Người phụ trách | Kết quả bàn giao |
|---|---|---|---|
| 6 | Viết và xuất bản **P4** (security audit) trước tiên | Content | Ý định thương mại cao nhất lên trước |
| 7 | Viết và xuất bản **P1** (pillar) | Content | Trung tâm cụm đã live |
| 8 | Viết và xuất bản **P2** | Content | — |
| 9 | Thêm `Service` + `Offer` + `FAQPage` cho từng trang (§6.3) | Dev | Đã validate |
| 10 | Cặp hreflang cho mọi trang đã xuất bản (§9.1) | Dev | Đối ứng, đã validate |

### Tuần 6–8 · Cụm nội dung
| # | Công việc | Người phụ trách | Kết quả bàn giao |
|---|---|---|---|
| 11 | Viết và xuất bản **P3** và **P5** | Content | Đủ 5 trang live |
| 12 | Xuất bản 25 bài hỗ trợ, 5 bài/pillar (§5.1) | Content | Mỗi bài link lên khi xuất bản |
| 13 | Thêm link đi xuống từ mỗi pillar tới bài của nó | Content | Cụm hai chiều hoàn chỉnh |
| 14 | Viết lại `llms.txt` (§8.3) | Marketing | File dẫn dắt bằng chào hàng |
| 15 | Lần đo GEO đầu tiên (§8.5) | Marketing | Bảng số liệu nền |

### Tuần 9–12 · Củng cố
| # | Công việc | Người phụ trách | Kết quả bàn giao |
|---|---|---|---|
| 16 | Duy trì nhịp 2–3 bài/tuần | Content | Backlog dịch chuyển |
| 17 | Cache trang + CDN (§10 mục 11) | Dev | LCP < 2,5s |
| 18 | Mở rộng các case study mỏng lên 800–1.200 từ | Content | Tăng khả năng được trích dẫn |
| 19 | Lần đo GEO thứ hai — so với lần nền | Marketing | Thấy được xu hướng |
| 20 | Báo cáo quý: thứ hạng, hiển thị, trích dẫn AI, số lead | Marketing | Review ngày 90 |

---

<a id="13"></a>
## 13. 📊 KPI & Cách Đo Lường

### 13.1 Mục tiêu theo mốc

| Chỉ số | Ngày 30 | Ngày 60 | Ngày 90 | Ngày 180 |
|---|---|---|---|---|
| Money page đã live | 3 | 5 | 5 | 5 |
| Đã index trong Search Console | 3 | 5 | 5 | 5 |
| Từ khóa vào top 100 (trên 14 từ) | 4 | 8 | 11 | 13 |
| Từ khóa vào top 10 | 0 | 1 | 3 | 6 |
| Phiên organic vào 5 trang | 40 | 150 | 400 | 1.200 |
| Trích dẫn AI (7 prompt × 4 engine = 28) | 2 | 6 | 10 | 16 |
| Lead organic từ cụm này | 0–1 | 1–2 | 3–5 | 8–12 |
| Tổng số bài live | 80 | 100 | 125 | 180 |

### 13.2 Thời gian thực tế

Trang dịch vụ mới trên một domain đã có tuổi thường cần **3–6 tháng** để đạt thứ hạng ổn định với các từ khóa thương mại.

Nhóm từ khóa tiếng Hà Lan sẽ dịch chuyển nhanh hơn nhóm tiếng Anh vì cạnh tranh mỏng hơn; nhóm tiếng Anh phải cạnh tranh với sân chơi toàn cầu.

**Đừng đánh giá kế hoạch trước ngày 90**, và hãy chuẩn bị tinh thần rằng đường cong thứ hạng sẽ **đi ngang trong 6–8 tuần đầu** — đó là bình thường, không phải thất bại.

### 13.3 Công cụ

| Mục đích | Công cụ | Tần suất |
|---|---|---|
| Thứ hạng & hiển thị | Google Search Console | Hàng tuần |
| Traffic & chuyển đổi | GA4 (kèm Consent Mode v2) | Hàng tuần |
| Kiểm tra schema | Rich Results Test + Schema.org validator | Mỗi lần xuất bản |
| Trích dẫn AI | Nhật ký prompt thủ công (§8.5) | Hàng tháng |
| Sức khỏe crawl | Screaming Frog hoặc Ahrefs Site Audit | Hàng tháng |
| Tăng trưởng backlink | Ahrefs / báo cáo link trong Search Console | Hàng tháng |

---

<a id="14"></a>
## 14. ⚠️ Rủi Ro

| # | Rủi ro | Mức độ | Biện pháp |
|---|---|---|---|
| 1 | **Money page không bao giờ được xây**, kế hoạch lại quay về viết thêm bài | 🔴 Cao | §1: bài viết không rank được truy vấn dịch vụ thương mại; 5 trang này **chính là** sản phẩm bàn giao |
| 2 | **Volume từ khóa tiếng Hà Lan thực sự nhỏ** | 🔴 Cao | Xuất bản cả hai ngôn ngữ (§9); đánh giá bằng số lead, không bằng số phiên |
| 3 | **Schema triển khai nhưng không validate** — hỏng âm thầm | 🟡 TB | Đưa validate thành một bước bắt buộc trong checklist xuất bản (§10.1) |
| 4 | **`sameAs` bị điền URL bịa** | 🔴 Cao | Chỉ dùng profile thật, do mình sở hữu; chưa có LinkedIn thì tạo mới (§6.1) |
| 5 | **P1 và P2 ăn thịt lẫn nhau** | 🟡 TB | Ánh xạ nghiêm ngặt một-từ-khóa-một-trang (§2); P1 là hướng dẫn, P2 là checklist |
| 6 | **Cám dỗ nhân bản trang theo thành phố** để phủ địa phương | 🟡 TB | §7.3: tuyệt đối không nhân bản money page theo từng thành phố |
| 7 | **Xuất bản vẫn theo đợt rồi dừng hẳn** | 🟡 TB | Nhịp cố định 2–3 bài/tuần (§5.2); audit đã nêu đích danh vấn đề xuất bản dồn đợt |
| 8 | **Crawler AI bị chặn trong `robots.txt`** | 🔴 Cao | Kiểm tra `GPTBot`, `ClaudeBot`, `PerplexityBot` đều được phép (§8.4) |
| 9 | **Giá trong schema lệch với máy tính giá trên site** | 🟡 TB | Một nguồn sự thật duy nhất: `launchstudio_info.md` §3 |
| 10 | **Đánh giá kết quả ngay tuần thứ 4** | 🟡 TB | §13.2 đã thống nhất trước: review vào ngày 90 |

---

<a id="15"></a>
## 15. 🖊️ Các Quyết Định Cần Bạn Duyệt

| # | Quyết định | Khuyến nghị | Trạng thái |
|---|---|---|---|
| 1 | Xây 5 trang money page có thể index, thoát khỏi cấu trúc site một trang | ✅ Có — không có chúng thì các từ khóa này không thể rank | ☐ |
| 2 | Ưu tiên phần entity/schema **trước** việc sản xuất nội dung mới | ✅ Có — 1–2 ngày dev, lợi ích toàn site và vĩnh viễn | ☐ |
| 3 | Loại từ khóa #08 `AI development` khỏi SEO, giống như đã loại khỏi Ads | ✅ Có — nhất quán với §2.1 | ☐ |
| 4 | Xuất bản cả bản tiếng Hà Lan lẫn tiếng Anh cho cả 5 trang | ✅ Có — bản Hà Lan là canonical, bản Anh phục vụ người Hà Lan gõ tiếng Anh | ☐ |
| 5 | Tạo LinkedIn company page + Google Business Profile | ✅ Có — bắt buộc để có `sameAs` thật và tín hiệu thực thể Hà Lan | ☐ |
| 6 | Thêm link hai chiều giữa `manifera.com` và `launchstudio.eu` | ✅ Có — khoản lợi thẩm quyền rẻ nhất có thể có (§7.2) | ☐ |
| 7 | Áp dụng nhịp xuất bản cố định 2–3 bài/tuần | ✅ Có — 800 bài đã viết mà chỉ 71 bài live mới là nút thắt thật | ☐ |
| 8 | Review vào ngày 90 dựa trên lead và trích dẫn AI, không phải tuần 4 dựa trên thứ hạng | ✅ Thống nhất trước | ☐ |

### Các mục còn thiếu, cần bạn cung cấp

| # | Hạng mục | Cần từ |
|---|---|---|
| A | URL profile `sameAs` thật (LinkedIn, X, v.v.) — **không được bịa** | LaunchStudio |
| B | Số điện thoại Hà Lan (+31) cho tính nhất quán NAP (§7.1) | LaunchStudio |
| C | URL logo và kích thước chính xác cho `Organization` schema | LaunchStudio |
| D | Duyệt 10 URL cuối cùng (§3.1) trước khi xuất bản bất cứ thứ gì | LaunchStudio |
| E | Xác nhận có review thật, kiểm chứng được hay không (cho `AggregateRating`) | LaunchStudio |

---

> **Nguồn:** [`extra-keywords.md`](extra-keywords.md) · [`launchstudio_info.md`](launchstudio_info.md) (thực thể thương hiệu, giá, persona, bản đồ liên kết) · [`seo_geo_audit_2026-07-31.md`](seo_geo_audit_2026-07-31.md) (hiện trạng kỹ thuật, thiếu sót schema, phát hiện GEO) · [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) (bản đối ứng trả phí, dùng chung phân tích từ khóa) · thư viện bài viết `2026-extra/`.
>
> **Lưu ý:** Volume tìm kiếm, thời gian lên hạng và mục tiêu traffic đều là **ước tính phục vụ lập kế hoạch** cho thị trường dịch vụ phần mềm B2B tại Hà Lan. Kết quả xếp hạng phụ thuộc vào cạnh tranh, thẩm quyền domain và tính nhất quán khi thực thi — không yếu tố nào trong đó có thể đảm bảo. Hãy xác minh dữ liệu từ khóa trong Search Console và Keyword Planner trước khi cam kết nguồn lực.
>
> **Bản gốc song ngữ EN/NL:** [`seo_geo_plan_production_keywords.md`](seo_geo_plan_production_keywords.md)
