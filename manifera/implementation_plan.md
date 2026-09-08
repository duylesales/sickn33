# 🚀 Kế Hoạch Marketing Tổng Thể — Manifera

> **Ngày lập**: 08/09/2026 · **Phạm vi**: 12 tháng (Q4/2026 → Q3/2027)
> **Nguồn**: [`manifera_info.md`](./manifera_info.md) · [`seo-geo-audit-manifera-com.md`](./seo-geo-audit-manifera-com.md) · `keyword-planner-manifera.com-2026-06-12 (1).csv` · kiểm kê 1.460 bài viết
> **Tài liệu con**: [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md) (SEO/GEO) · [`paid_ads_plan.md`](./paid_ads_plan.md) (quảng cáo trả phí) · [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) · [`google_ads_rsa_copy_manifera.md`](./google_ads_rsa_copy_manifera.md) · [`extra-keywords.md`](./extra-keywords.md)

---

## 1. Phân Tích Hiện Trạng

### 1.1 Sản Phẩm & Giá Trị Cốt Lõi

| Yếu tố | Nội dung |
|---|---|
| **Bán cái gì** | Đội ngũ kỹ sư phần mềm chuyên trách (dedicated team), phần mềm tùy chỉnh, mobile/web app, eCommerce, di trú cloud EU |
| **Bán cho ai** | SME và MNC tại Hà Lan, Bỉ, Đức, EU; thứ cấp là Singapore/APAC |
| **Khác biệt lõi** | Quản trị Hà Lan × Thực thi Việt Nam — trụ sở Amsterdam (Herengracht 420), hub kỹ thuật TP.HCM, pháp nhân Singapore |
| **Bằng chứng** | Thành lập 2014 · 160+ dự án · 120+ khách hàng · 10+ năm · CEO Herre Roelevink (nền tảng Agile/Scrum, quản lý offshore, cybersecurity, đồng sáng lập CyberDevOps → CFLW Cyber Strategies, hợp tác TNO) |
| **Giá trị hợp đồng** | Ước tính €5.000–€15.000/tháng cho một dedicated team; LTV năm đầu €60.000+ |
| **Chu kỳ bán** | 60–120 ngày, nhiều người ra quyết định (CTO + CFO + đôi khi cả board) |

### 1.2 Tài Sản Content Hiện Có

| Tài sản | Số lượng | Trạng thái |
|---|---|---|
| Bài viết tiếng Anh | **1.460** | ✍️ Viết xong · ⛔ **Chỉ ~78 mục được đánh dấu đã đăng** |
| Bài social đi kèm | 1.460 | Chưa dùng |
| Hình minh họa (`_pic.jpg`) | 269 / 1.460 | Thiếu 1.191 |
| Cụm nội dung | 17 thư mục (11 cụm `extra` + 6 tháng) | Chưa gắn vào kiến trúc pillar/cluster nào |
| Phân bổ phễu | 513 decision · 638 consideration · 292 awareness (trên 1.443 mục đã gắn nhãn) | Rất mạnh ở nửa dưới phễu — hiếm có |
| Case study bên thứ ba | 19 case study + 29 review (FeaturedCustomers), review Clutch, 8 review ITviec | Chưa được khai thác trong marketing |
| `llms.txt` | Đã có, kèm `llms-full.txt` | Tài sản GEO hiếm — cần viết lại theo hướng thực thể |

> **🔴 Kết luận quan trọng nhất của toàn bộ tài liệu này**: Manifera **không thiếu nội dung**. Manifera thiếu **kênh phân phối và kiến trúc** cho nội dung đã có. Mọi ngân sách chi cho việc viết thêm bài trước khi đăng 1.382 bài tồn kho đều là chi sai chỗ.

### 1.3 Hiện Trạng Website

Theo audit 31/07/2026: hạ tầng tốt (robots.txt sạch, sitemap Yoast hợp lệ, các trang lõi đã index, HSTS, HTTP/2+3, TLS wildcard), nhưng còn 7 lỗi on-page chưa xử lý:

| Mức | Lỗi | Ảnh hưởng |
|---|---|---|
| 🔴 P0 | `<h1>` trang chủ là "Experiences of our clients working with us" | Tín hiệu on-page mạnh nhất đang nói với Google rằng trang chủ là trang testimonial |
| 🔴 P0 | Không có schema `Organization`/`WebSite` | Mất khả năng nối thực thể manifera.com với 29 review + 19 case study bên ngoài |
| 🟡 P1 | 1.478 từ trên trang chủ chỉ có 1 thẻ `<h2>` | Không phân đoạn được chủ đề |
| 🟡 P1 | 13/43 ảnh trang chủ thiếu `alt` | Mất image search + lỗi tiếp cận |
| 🟡 P1 | `og:image` 225×225 (cỡ favicon) | Link preview trên LinkedIn vỡ/bé |
| ⚪ P2 | robots.txt còn 2 rule `/nl/` chết · `/favicon.ico` 404 · hai đường dẫn `/about/` vs `/about-us/` | Dọn dẹp |
| 🔴 Gấp | Chứng chỉ TLS hết hạn **09/09/2026** | Kiểm tra ngay hôm nay |

---

## 2. Phân Tích Thị Trường

### 2.1 Bối Cảnh 2026

1. **Khan hiếm kỹ sư tại EU vẫn chưa hạ nhiệt.** Đây là lý do tồn tại của Manifera từ 2014 và vẫn đúng: một senior engineer tại Amsterdam mất 4–6 tháng để tuyển, chi phí toàn phần vượt xa mức mà SME chịu được.
2. **AI làm dịch chuyển kỳ vọng, không xóa nhu cầu.** Khách hàng năm 2026 hỏi "đội của các anh dùng AI thế nào để đi nhanh hơn", chứ không hỏi "có cần thuê người nữa không". Nhóm từ khóa AI trong CSV (`ai software development companies`, `offshore ai developers`) có competition thấp — cửa sổ định vị còn mở.
3. **Sự trưởng thành của mô hình offshore.** Tranh luận "có nên offshore không" đã kết thúc; tranh luận hiện tại là "offshore ở đâu và ai quản trị". Toàn bộ 100 bài `extra-6-dutchvsvietnam` nằm đúng vào câu hỏi này.
4. **Người mua B2B tự nghiên cứu 70% hành trình trước khi liên hệ.** Họ đọc bài so sánh, checklist chọn vendor, bảng giá — Manifera có sẵn 513 bài decision-stage phục vụ đúng giai đoạn này nhưng chưa đăng.
5. **AI answer engine trở thành lớp khám phá mới.** Câu hỏi "best offshore software development companies in the Netherlands" ngày càng được hỏi với ChatGPT/Perplexity thay vì Google. Ai có dữ liệu thực thể có cấu trúc sẽ được trích dẫn.

### 2.2 Đối Thủ & Vị Trí Cạnh Tranh

| Nhóm | Đại diện | Điểm mạnh của họ | Điểm yếu khai thác được |
|---|---|---|---|
| **Agency Hà Lan/EU** | Xebia, iO, Sopra Steria NL, Sogeti | Gần khách, thương hiệu mạnh, hợp đồng lớn | Giá cao gấp 2–3 lần; SME không với tới |
| **Vendor Đông Âu** | Netguru (PL), SoftServe (UA), Intellias | Cùng múi giờ, quen chuẩn EU | Chi phí đang tăng nhanh; rủi ro địa chính trị; cạnh tranh nhân sự gay gắt |
| **Vendor Việt Nam quy mô lớn** | FPT Software, TMA, KMS, NashTech | Quy mô hàng nghìn kỹ sư, chứng chỉ đầy đủ | Quy trình dành cho khách enterprise; SME 3–10 kỹ sư không được ưu tiên; **không có người Hà Lan quản trị** |
| **Marketplace/freelancer** | Toptal, Upwork | Rẻ, nhanh, linh hoạt | Không có quản trị dự án, không cam kết dài hạn, rủi ro IP |
| **No-code / low-code** | Bubble, OutSystems partners | Rẻ, nhanh ra mắt | Vendor lock-in, trần kỹ thuật — Manifera đã có sẵn 100 bài `extra-2-random` nói về đúng rủi ro này |

**Khoảng trống Manifera sở hữu**: *SME châu Âu cần 3–10 kỹ sư, muốn chi phí Đông Nam Á nhưng không chấp nhận rủi ro quản trị của Đông Nam Á.* Nhóm lớn thì bỏ qua họ; freelancer thì không quản được; agency EU thì quá đắt.

---

## 3. Chiến Lược Định Vị

### 3.1 Positioning Statement

> **Dành cho** CTO và founder tại SME châu Âu không tuyển đủ kỹ sư,
> **Manifera là** đối tác phát triển phần mềm vận hành theo mô hình kép — quản trị từ Amsterdam, thực thi tại TP.HCM,
> **khác với** vendor offshore quy mô lớn (bạn chỉ là khách hàng nhỏ) và agency EU (bạn không đủ ngân sách),
> **bởi vì** người sáng lập là người Hà Lan, hợp đồng theo luật châu Âu, và đội kỹ sư gắn bó dài hạn thay vì luân chuyển liên tục.

### 3.2 Messaging Framework

| Persona | Nỗi đau | Thông điệp chính | Bằng chứng |
|---|---|---|---|
| **A — CTO/VP Eng (SME EU)** | Không tuyển được người, roadmap trượt mỗi quý | "Đội của bạn bắt đầu sprint đầu tiên trong 2–4 tuần" | Quy trình onboarding 4 bước; 160+ dự án |
| **B — CEO/COO scale-up** | Cần ra sản phẩm nhanh, ngân sách giới hạn | "Chi phí kỹ sư Đông Nam Á, kỷ luật giao hàng Hà Lan" | Case study; mô hình hợp đồng linh hoạt |
| **C — IT Manager/PO (MNC)** | Hiện đại hóa hệ thống cũ, tuân thủ GDPR | "Hợp đồng châu Âu, dữ liệu lưu tại EU, quy trình kiểm soát được" | Dịch vụ NL/Euro Cloud; nền tảng cybersecurity của CEO |
| **D — Founder không rành kỹ thuật** | Sợ bị lừa, không biết bắt đầu từ đâu | "Chúng tôi nói bằng ngôn ngữ kinh doanh và bạn sở hữu 100% code" | 29 review công khai; 19 case study |

### 3.3 Tagline (A/B test)

1. *Dutch-managed. Vietnam-built.*
2. *European governance, Southeast Asian engineering.*
3. *Your engineering team — in Ho Chi Minh City, run from Amsterdam.*
4. *The offshore team that answers to Dutch standards.*

---

## 4. Chiến Lược Kênh

### 4.1 Owned Media — Content & SEO/GEO 🥇 *Ưu tiên số 1*

Toàn bộ chi tiết ở [`seo_geo_plan_vendor_keywords.md`](./seo_geo_plan_vendor_keywords.md). Tóm tắt quyết định:

| Việc | Quy mô | Vì sao |
|---|---|---|
| Xây 5 money page (pillar) | 5 trang, 2.000–3.000 từ | Toàn bộ 1.460 bài hiện không có đích thương mại nào để trỏ về |
| Chốt cơ chế publish hàng loạt | WP-CLI / REST API | **Nút thắt lớn nhất**: đăng tay 1.382 bài ở nhịp 25 bài/tuần mất 55 tuần |
| Đăng theo 5 pha ưu tiên | 1.382 bài trong 50 tuần | Pha 1 là decision + cost (gần doanh thu nhất), pha cuối là head term |
| Sửa 7 lỗi audit | 1–2 tuần | Ảnh hưởng mọi phiên truy cập, cả organic lẫn trả phí |
| Viết lại `llms.txt` theo hướng thực thể | 1 tệp | Đòn bẩy GEO rẻ nhất và ít người làm nhất |

> **⚠️ Không đầu tư vào schema trong tệp `.md`.** Chỉ phần chữ của bài được đăng lên site; khối JSON-LD trong markdown không bao giờ tới nơi. Mọi việc structured data làm ở tầng WordPress/Yoast.

### 4.2 Paid Acquisition 🥈

Chi tiết ở [`paid_ads_plan.md`](./paid_ads_plan.md). Ba điểm cần nhớ:

1. **Google Search có trần rất thấp.** Sau khi loại `software in software` (49.500) và `dev ops` (5.400), nhu cầu tìm kiếm thương mại thật chỉ khoảng 900–1.200 lượt/tháng toàn cầu. Google Search là kênh *thu* nhu cầu sẵn có, không phải kênh *tạo* nhu cầu.
2. **LinkedIn là động cơ tăng trưởng thật.** Đây là nơi duy nhất nhắm đúng CTO tại công ty 50–1.000 người ở Hà Lan/Bỉ. Nguyên liệu quảng cáo lấy nguyên từ kho bài đã viết — không cần sản xuất mới.
3. **Thư mục agency (Clutch, Sortlist) là inventory có ý định mua cao nhất.** Nhưng phải gom thêm 5+ review mới trước khi trả tiền cho sponsored listing.

### 4.3 Social Media & Community 🥉

| Kênh | Vai trò | Nhịp | Nguyên liệu |
|---|---|---|---|
| **LinkedIn công ty** | Kênh chính | 4–5 bài/tuần | 1.460 bài social đã viết sẵn |
| **LinkedIn cá nhân — Herre Roelevink** | Kênh có tỷ lệ tiếp cận cao nhất | 2–3 bài/tuần | Góc nhìn founder, chuyện quản trị offshore, bài học 2014→2026 |
| **LinkedIn cá nhân — kỹ sư/tech lead** | E-E-A-T + tuyển dụng | 1 bài/tuần | Nội dung kỹ thuật từ `extra-2-random` |
| **X (@ManiferaSW)** | Duy trì tối thiểu | 2 bài/tuần, tự động | Không đầu tư thêm — audience không ở đây |
| **Facebook** | Thương hiệu tuyển dụng tại VN | 2 bài/tuần | Văn hóa công ty, đội ngũ HCMC |
| **YouTube** | Đã có video nhúng trên trang chủ | 1 video/tháng | Case study, giải thích quy trình onboarding |

### 4.4 Email

| Chuỗi | Đối tượng | Nội dung |
|---|---|---|
| **Lead magnet nurture** | Người tải checklist chọn vendor | 5 email từ `extra-9-decision` |
| **Chuỗi so sánh quốc gia** | Người đọc bài NL vs VN | 4 email từ `extra-6-dutchvsvietnam` |
| **Chuỗi chi phí** | Người xem trang giá | 4 email từ `extra-3-longtail` |
| **Khách hàng cũ** | 120+ khách hàng | Bản tin quý — nguồn upsell và referral rẻ nhất |

Xem [`email_sequences.md`](./email_sequences.md) (đã có sẵn).

---

## 5. Partnership & Referral

### 5.1 Đối Tác Chiến Lược

| Loại | Đối tác mục tiêu | Mô hình |
|---|---|---|
| **Agency Hà Lan quá tải** | Agency thiết kế/marketing không có năng lực dev | White-label development, chia hoa hồng |
| **Công ty tư vấn/ERP** | Đơn vị triển khai ERP cần dev tùy chỉnh | Thầu phụ |
| **VC & accelerator NL** | Quỹ đầu tư có portfolio startup thiếu người | Gói ưu đãi cho portfolio |
| **Mạng lưới BNI** | CEO đã là thành viên tích cực | Kênh referral offline sẵn có, chưa hệ thống hóa |
| **Cộng đồng người Hà Lan tại VN/SG** | Phòng thương mại Hà Lan tại HCMC/Singapore | Uy tín địa phương + tuyển dụng |

### 5.2 Referral Program

- Khách hàng hiện tại giới thiệu thành công → 5% giá trị hợp đồng 6 tháng đầu, hoặc 1 tháng dịch vụ miễn phí.
- Đối tác agency → 10% giá trị hợp đồng năm đầu.
- **Bắt buộc kèm**: quy trình xin review sau mỗi dự án bàn giao. 29 review hiện có là tài sản GEO/SEO mạnh nhất của Manifera; phải tăng đều đặn, không để đóng băng.

---

## 6. Conversion Rate Optimization

### 6.1 Việc phải làm trên website

| Ưu tiên | Việc | Lý do |
|---|---|---|
| 🔴 | Sửa `<h1>` trang chủ | Người đọc lẫn máy đều không biết trang chủ nói về cái gì |
| 🔴 | Xây trang `/get-a-team-proposal/` | Một lời mời duy nhất, dùng chung cho mọi kênh: "báo giá đội ngũ trong 48 giờ" |
| 🔴 | Đưa 5 pillar page lên | Không có đích thì nội dung không bán được gì |
| 🟡 | Đưa review Clutch/FeaturedCustomers lên trang chủ + trang dịch vụ | Bằng chứng đang nằm ở site người khác |
| 🟡 | Rút gọn form liên hệ, bỏ trường số điện thoại | Giảm 30–40% tỷ lệ bỏ form B2B |
| 🟡 | Thêm calendar đặt lịch trực tiếp (Amsterdam) | Rút ngắn 1 vòng email qua lại |
| ⚪ | Trang giá có số thật | Quyết định của ban lãnh đạo — xem §9 |

### 6.2 Phễu & Chỉ số

| Bước | Chỉ số hiện tại | Mục tiêu 6 tháng |
|---|---|---|
| Truy cập → đọc bài | — | 2.500 phiên organic/tháng |
| Đọc bài → xem money page | — | 12% |
| Money page → điền form | — | 5% |
| Form → SQL | — | 30% |
| SQL → hợp đồng | — | 15–20% |
| **Chu kỳ trung bình** | — | 60–120 ngày |

---

## 7. KPIs & Ngân Sách

### 7.1 Mục tiêu theo quý

| Chỉ số | Q4/2026 | Q1/2027 | Q2/2027 | Q3/2027 |
|---|---|---|---|---|
| Bài đã đăng (lũy kế) | 280 | 680 | 1.080 | 1.460 |
| Trang được index | 350 | 750 | 1.200 | 1.500+ |
| Phiên organic/tháng | +40% | ×2,5 | ×4 | ×5 |
| Từ khóa top-10 (bảng §2 SEO plan) | 2 | 6 | 9 | 12 |
| Lead/tháng (tổng kênh) | 8 | 25 | 40 | 55 |
| Yêu cầu báo giá/tháng | 3 | 10 | 15 | 22 |
| Hợp đồng chốt/quý | 1 | 2–3 | 3–5 | 5–7 |
| Trích dẫn trong AI answer (6 prompt) | 0–1/6 | 2/6 | 3/6 | 4/6 |

### 7.2 Ngân sách đề xuất

| Hạng mục | Tháng 1–2 | Tháng 3–6 | Tháng 7–12 |
|---|---|---|---|
| Quảng cáo trả phí | €3.000 | €6.000 | €6.000–12.000 |
| Sản xuất hình minh họa (1.191 ảnh còn thiếu) | €500 | €500 | €300 |
| Công cụ (Semrush/Ahrefs, GSC, CRM, LinkedIn Sales Nav) | €400 | €400 | €400 |
| Viết 5 pillar page | €1.500 (một lần) | — | — |
| Kỹ thuật (sửa audit, dựng pipeline publish) | €1.500 (một lần) | €300 | €300 |
| Thu thập review (quà tặng, thời gian) | €200 | €200 | €200 |
| **Tổng/tháng** | **~€3.800–5.300** | **~€7.400** | **~€7.200–13.200** |

> Quy tắc: **không** tăng lên mức ngân sách kế tiếp cho tới khi chi phí trên mỗi yêu cầu báo giá dưới €400 trong 2 tháng liên tiếp.

---

## 8. Lộ Trình Thực Hiện

### Phase 1 — Nền móng (T9–T10/2026)
- Kiểm tra chứng chỉ TLS (hết hạn 09/09/2026)
- Sửa 7 lỗi audit; cấu hình schema `Organization` + `Person` trong Yoast
- **Chốt và dựng cơ chế publish hàng loạt** ← nút thắt quan trọng nhất
- Viết + đăng 5 pillar page; xây `/get-a-team-proposal/`
- Viết lại `llms.txt`; kiểm tra nhất quán NAP trên 6 nền tảng
- Cài GA4 key event, LinkedIn Insight Tag, Meta Pixel
- Xin 5+ review Clutch mới
- Bật Google Ads AG1 + AG2 + Brand ở ngân sách Lean

### Phase 2 — Xuất bản & Tăng tốc (T11/2026–T2/2027)
- Đăng pha 1 (200 bài decision + cost), nhịp 25 bài/tuần
- Đăng pha 2 (200 bài local), so le theo tỉnh
- Xây trang `/software-development-cost/` (nếu ban lãnh đạo đồng ý công bố giá)
- Bật LinkedIn Awareness + ABM
- Bật Clutch sponsored listing; import tài khoản sang Bing
- Bắt đầu sản xuất hình minh họa còn thiếu theo cụm đang đăng

### Phase 3 — Mở rộng (T3–T6/2027)
- Đăng pha 3 và 4 (600 bài)
- Bật LinkedIn retargeting + Message Ads từ Herre Roelevink
- Kích hoạt chương trình referral và đối tác white-label
- Chuỗi email nurture chạy tự động
- Đo GEO hàng tháng; tối ưu answer block theo kết quả

### Phase 4 — Tối ưu (T7/2027+)
- Đăng nốt pha 5 (380 bài)
- Hợp nhất/xóa bài không có impression sau 6 tháng
- Nâng ngân sách trả phí lên tier Aggressive nếu CPA đạt chuẩn
- Xem xét mở cụm nội dung mới cho các mảng còn trống (xem [`extra-keywords.md`](./extra-keywords.md))

---

## 9. Câu Hỏi Cần Ban Lãnh Đạo Quyết

| # | Câu hỏi | Chặn việc gì |
|---|---|---|
| 1 | Có công bố khoảng giá thật trên website không? | Trang `/software-development-cost/` và nhóm quảng cáo BOFU |
| 2 | Cơ chế publish hàng loạt: WP-CLI, REST API hay plugin import? | Toàn bộ pha 1 trở đi |
| 3 | Ai viết 5 pillar page — nội bộ hay cùng pipeline đã tạo 1.460 bài? | Phase 1 |
| 4 | Dịch vụ webshop/Magento có được cấp một pillar riêng không? | Cần nghiên cứu từ khóa riêng trước (CSV hiện gần như trống mảng này) |
| 5 | Có bao giờ khôi phục phần tiếng Hà Lan của site không? | Hiện mặc định **không** — mọi kế hoạch đang thuần tiếng Anh |
| 6 | Google Business Profile cho Herengracht 420 đã xác minh chưa? | Khả năng lên local pack của pillar P3 |
| 7 | Ai sở hữu quy trình xin review sau bàn giao? | Ngân sách Clutch và toàn bộ đòn bẩy GEO |

---

*Manifera Software Development Pte Ltd · Amsterdam · Singapore · TP. Hồ Chí Minh*
