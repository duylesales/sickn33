# 🚀 Kế Hoạch Marketing Tổng Thể — OnlyAIJobs

> **Ngày lập**: 08/09/2026 · **Phạm vi**: 12 tháng (Q4/2026 → Q3/2027)
> **Nguồn**: quét trực tiếp onlyaijobs.eu ngày 08/09/2026 · [`onlyaijobs_info.md`](./onlyaijobs_info.md) · [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md)
> **Tài liệu con**: [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) · [`paid_ads_plan.md`](./paid_ads_plan.md) · [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md) · [`google_ads_rsa_copy_onlyaijobs.md`](./google_ads_rsa_copy_onlyaijobs.md) · [`extra-keywords.md`](./extra-keywords.md)

---

## ⚠️ Đọc Trước: Đây Không Phải Bài Toán Marketing

OnlyAIJobs khác Manifera và LaunchStudio ở một điểm căn bản. Hai property kia có **sản phẩm chạy tốt và thiếu kênh phân phối**. OnlyAIJobs có **kênh phân phối chưa mở được và sản phẩm chưa đủ hàng để bán**.

| | Manifera | OnlyAIJobs |
|---|---|---|
| Nội dung/hàng hóa sẵn có | 1.460 bài viết | 52 tin, đều cũ 1 tháng |
| Google nhìn thấy site? | ✅ Đã index | ❌ Bị WAF chặn 39 ngày |
| Trang bán hàng chính | ✅ Có | ❌ Trả về trang trắng |
| Đo lường | ✅ GA4 | ❌ Không phát hiện thấy |
| Việc cần làm đầu tiên | Xuất bản nội dung | **Sửa kỹ thuật + xây nguồn cung** |

**Ba tháng đầu của kế hoạch này gần như không có hoạt động marketing.** Đó là kết luận đúng, không phải sự né tránh. Chi tiền quảng cáo cho một job board 52 tin cũ là mua về một lần thất vọng của mỗi người dùng tiếp cận được.

---

## 1. Phân Tích Hiện Trạng

### 1.1 Sản phẩm

| Yếu tố | Nội dung |
|---|---|
| **Là gì** | Job board chuyên 100% việc làm AI/ML/Data, song ngữ EN/NL |
| **Khác biệt** | Hiển thị việc làm ở **cấp độ địa chỉ chính xác** + khoảng cách từ nhà người tìm việc |
| **Câu chuyện gốc** | Sinh viên Noord-Brabant rời quê ra Randstad không phải vì muốn, mà vì không biết công ty hay nào ở gần |
| **Hai phía** | Người tìm việc (miễn phí, không cần tài khoản) ↔ Nhà tuyển dụng (tin đầu miễn phí, đăng qua email) |
| **Doanh thu** | 🟥 Chưa xác định sau tin miễn phí đầu tiên |

### 1.2 Nguồn cung (chụp ngày 08/09/2026)

| Chỉ số | Giá trị | Đánh giá |
|---|---|---|
| Tổng tin | **52** | Quá ít để giữ chân người tìm việc |
| Độ tươi | **100% đăng cách đây ~1 tháng** | 🔴 Không có tin mới ≥30 ngày |
| Nhà tuyển dụng | ~40 | Chất lượng tốt: Accenture, Cegeka, Sendcloud, Mollie, Heijmans, Rexel, VINCI Energies |
| Địa lý | 49 NL · 3 Mỹ | 3 tin Mỹ làm loãng định vị `.eu` |
| Loại hình | 100% Full-time | Không có tin part-time/stage/remote dù bộ lọc có |
| Danh mục có tin | 5/11 | Development + Machine Learning chiếm ~40/52 |

### 1.3 Website — 10 lỗi chặn đường

| Mức | Lỗi |
|---|---|
| 🔴 | WAF chặn Googlebot 39 ngày (GPTBot/ClaudeBot thì vào được — đảo ngược hoàn toàn) |
| 🔴 | `robots.txt` chặn mọi bot AI bằng `Disallow: /` |
| 🔴 | Không có `JobPosting` schema → không đủ điều kiện vào Google Jobs |
| 🔴 | Không có URL riêng cho từng tin |
| 🔴 | Phân trang canonical về trang 1 → 42/52 tin vô hình |
| 🔴 | 4 URL trong sitemap trả vỏ Admin Portal rỗng (gồm cả 2 trang thương mại quan trọng nhất) |
| 🟡 | `index-sitemap.xml` sai cú pháp |
| 🟡 | hreflang không đối xứng → bản NL bị Google bỏ qua |
| 🟡 | Blog 0 bài |
| 🟡 | Không phát hiện GA4/GTM |

Chi tiết: [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md).

---

## 2. Phân Tích Thị Trường

### 2.1 Bối cảnh

1. **Nhu cầu tuyển AI tại Hà Lan đang thật và tăng** — chính danh sách 40 nhà tuyển dụng trên site đã chứng minh: từ tập đoàn (Accenture, VINCI) tới scale-up (Sendcloud, Mollie) tới SME vùng (Boltrics, 4Dotnet, Winparts).
2. **Job board tổng hợp phục vụ kém nhóm vai trò AI.** Recruiter đăng lên Indeed nhận về hàng trăm hồ sơ không liên quan; kỹ sư AI phải lọc qua hàng nghìn tin IT chung chung.
3. **Google Jobs đã thay đổi luật chơi.** Với truy vấn tìm việc, widget Google Jobs chiếm gần trọn màn hình đầu. Job board không có `JobPosting` schema gần như không tồn tại — đây vừa là rủi ro sống còn vừa là cơ hội, vì nhiều job board vùng cũng chưa làm đúng.
4. **Chảy máu nhân tài vùng là vấn đề chính sách có ngân sách.** Brainport Eindhoven, Midpoint Brabant, các gemeente và trường đại học đều đang tìm cách giữ sinh viên ở lại vùng. Câu chuyện gốc của OnlyAIJobs **chính là** mục tiêu của họ.

### 2.2 Đối thủ

| Nhóm | Đại diện | Điểm mạnh | Khoảng trống khai thác được |
|---|---|---|---|
| **Job board tổng hợp** | Indeed NL, Nationale Vacaturebank, Monsterboard, Jobbird | Kho tin khổng lồ, thương hiệu mạnh, ngân sách vô hạn | Không chuyên AI; recruiter trả tiền theo click; công ty nhỏ bị đẩy xuống dưới |
| **Mạng nghề nghiệp** | LinkedIn Jobs | Dữ liệu hồ sơ, mạng lưới | Nhiễu recruiter; không hiển thị khoảng cách từ nhà; đắt với nhà tuyển dụng nhỏ |
| **Job board tech EU** | Honeypot, AI-Jobs.net | Chuyên tech/AI | Toàn cầu hoặc Đức-trung tâm; không có chiều sâu vùng tại NL; không có dữ liệu địa chỉ |
| **Nền tảng sinh viên NL** | Magnet.me, Intermediair | Mạnh với sinh viên/starter Hà Lan | Không chuyên AI |
| **Job board ngành NL** | Techniekwerkt và tương tự | Chuyên ngành kỹ thuật | Không phải AI |

**Khoảng trống OnlyAIJobs sở hữu**: *người tìm việc AI tại Hà Lan muốn biết công ty nào ở gần nhà mình đang tuyển* — không ai phục vụ nhóm này, vì các nền tảng lớn tối ưu cho quy mô chứ không cho bán kính.

---

## 3. Định Vị — Quyết Định Phải Chốt Trước

Site đang kể **hai câu chuyện mâu thuẫn**: thẻ meta và schema nói "European job board for AI"; nội dung trang chủ nói "sinh viên Brabant không cần chuyển ra Randstad".

| | Phương án A: "AI jobs châu Âu" | Phương án B: "Việc làm AI theo vùng tại NL" |
|---|---|---|
| Đối thủ | LinkedIn, Indeed, AI-Jobs.net, Honeypot | Indeed NL ở đuôi dài, Magnet.me |
| Từ khóa | `ai jobs europe` — cực gắt | `ai vacatures <stad>` — nhẹ |
| Nguồn cung cần | Hàng nghìn tin khắp EU | Hàng trăm tin tại NL |
| Khớp với 52 tin hiện có | ❌ Không | ✅ Có (49/52 ở NL) |
| Khớp với câu chuyện gốc | ❌ Không | ✅ Hoàn toàn |
| Đối tác tiềm năng | Không rõ | Brainport, Midpoint, gemeente, trường đại học |
| Khớp với USP địa chỉ chính xác | ❌ Vô nghĩa ở quy mô châu Âu | ✅ Đây chính là lý do USP tồn tại |

👉 **Khuyến nghị rõ ràng: chọn phương án B.** Mọi bằng chứng — nguồn tin, câu chuyện, USP sản phẩm, đối tác khả dĩ — đều chỉ về cùng một hướng. Tên miền `.eu` vẫn giữ được (không cần đổi), nhưng thông điệp, từ khóa và nội dung phải nói tiếng Hà Lan và nói về vùng.

### 3.1 Positioning Statement (theo phương án B)

> **Dành cho** kỹ sư AI, data scientist và sinh viên mới tốt nghiệp tại Hà Lan,
> **OnlyAIJobs là** nền tảng việc làm chỉ đăng vai trò AI và hiển thị từng vị trí ở cấp độ địa chỉ chính xác kèm khoảng cách từ nhà bạn,
> **khác với** Indeed và LinkedIn nơi công ty trả nhiều tiền hơn thì hiện lên trước và bạn phải lọc qua hàng nghìn tin không liên quan,
> **bởi vì** chúng tôi tin không ai nên rời bỏ vùng quê chỉ vì không biết công ty hay nào ở ngay gần đó.

### 3.2 Tagline (A/B test)

1. 🇳🇱 *Werk in AI, dicht bij huis.*
2. 🇳🇱 *Je hoeft niet naar de Randstad.*
3. 🇳🇱 *Alle AI-vacatures. Op exact adres.*
4. 🇬🇧 *AI jobs, mapped to the street.*

---

## 4. Chiến Lược Nguồn Cung — Ưu Tiên Số 1

> **Đây là chương quan trọng nhất của tài liệu.** Marketing của một marketplace thiếu hàng không phải là quảng cáo, mà là đi lấy hàng.

### 4.1 Mục tiêu số lượng tin

| Mốc | Số tin đang hiệu lực | Mở khóa được gì |
|---|---|---|
| Hiện tại | 52 (cũ) | — |
| Tháng 2 | 120 | Bật quảng cáo nhắm người tìm việc, sinh trang thành phố |
| Tháng 4 | 200 | Trang danh mục vượt ngưỡng, blog có đích để trỏ về |
| Tháng 8 | 400 | Marketplace bắt đầu tự vận hành |
| Tháng 12 | 800 | Có thể bàn tới doanh thu nghiêm túc |

### 4.2 Năm kênh lấy tin, xếp theo chi phí trên mỗi tin

| # | Kênh | Chi phí | Sản lượng dự kiến | Ghi chú |
|---|---|---|---|---|
| 1 | **Quay lại 40 nhà tuyển dụng đã đăng** | Gần như bằng 0 | 40–80 tin | Họ đã nói "có" một lần. Email: "tin của bạn đã đăng một tháng, làm mới hoặc thêm vai trò khác chứ?" |
| 2 | **Đối tác vùng** (Brainport Eindhoven, Midpoint Brabant, gemeente, TU/e, Fontys, Tilburg, JADS) | Thời gian | 50–150 tin | Câu chuyện gốc trùng khớp mục tiêu chính sách của họ |
| 3 | **Agency tuyển dụng chuyên AI/Data** | Thời gian | 100+ tin/agency | Một liên hệ mang lại nhiều tin |
| 4 | **Đi săn thủ công** (công ty đang đăng tin AI ở nơi khác) | Thời gian | 30–60 tin/tháng | Bền vững nhưng tốn công |
| 5 | **Quảng cáo nhắm nhà tuyển dụng** | €600–800/tháng | 10–20 tin/tháng | Xem [`paid_ads_plan.md`](./paid_ads_plan.md) |

### 4.3 Giảm ma sát đăng tin — thay đổi rẻ nhất, hiệu quả nhất

Hiện tại: *"gửi email kèm link tin tuyển dụng tới info@onlyaijobs.eu"*.

Vấn đề: bắt recruiter soạn email là rào cản cao hơn nhiều so với điền form, **và không tạo ra sự kiện chuyển đổi nào để đo**. Thay bằng form 2 trường (URL công ty + URL tin tuyển dụng) có thể là thay đổi có ROI cao nhất trong toàn bộ kế hoạch, và chỉ tốn một ngày lập trình.

---

## 5. Chiến Lược Kênh

### 5.1 SEO/GEO 🥇
Chi tiết ở [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md). Ba việc lớn nhất:
- Gỡ chặn WAF → tạo URL từng việc làm → gắn `JobPosting` schema → **vào Google Jobs**
- Sinh trang tự động theo thành phố/danh mục, có **ngưỡng tối thiểu** để không tạo trang rỗng
- Khai thác việc GPTBot/ClaudeBot đang là bot duy nhất vào được site: sửa `robots.txt`, viết `llms.txt` thật

### 5.2 Quảng cáo trả phí 🥈
Chi tiết ở [`paid_ads_plan.md`](./paid_ads_plan.md). Nguyên tắc duy nhất: **mua nguồn cung, đừng mua nhu cầu.** Quảng cáo nhắm người tìm việc bị khóa sau cột mốc 120 tin.

### 5.3 Nội dung & Social 🥉

| Kênh | Vai trò | Nhịp | Nguyên liệu |
|---|---|---|---|
| **Blog** (hiện 0 bài) | SEO + backlink | 4 bài/tháng sau Cổng 2 | Báo cáo lương AI Hà Lan (nam châm backlink mạnh nhất), bản đồ nhà tuyển dụng theo vùng |
| **LinkedIn công ty** | Cả hai phía | 3 bài/tuần | "5 vacatures AI mới tuần này ở Brabant" — nội dung tự sinh từ chính dữ liệu tin |
| **Instagram/TikTok** | Persona A (sinh viên) | 2 bài/tuần sau Cổng 2 | Câu chuyện "không cần chuyển ra Randstad" |
| **Newsletter** | Giữ chân người tìm việc | 1 email/tuần | Tin mới trong tuần theo vùng — kênh giữ chân rẻ nhất của mọi job board |

> **🇻🇳 Ghi chú về newsletter**: với job board, email hàng tuần "5 việc mới gần bạn" là công cụ giữ chân mạnh hơn mọi thứ khác, vì người tìm việc không quay lại site mỗi ngày nhưng có mở email. Nên xây từ sớm — chỉ cần một trường email trên trang danh sách.

---

## 6. Đối Tác

| Loại | Mục tiêu | Đề xuất hợp tác |
|---|---|---|
| **Tổ chức vùng** | Brainport Eindhoven, Midpoint Brabant, gemeente Eindhoven/Tilburg/Den Bosch | Giữ nhân tài ở lại vùng — cùng mục tiêu, họ có ngân sách và kênh truyền thông |
| **Trường đại học** | TU/e, Tilburg University, Fontys, JADS, Avans | Trang việc làm cho sinh viên tốt nghiệp AI/Data; đổi lại là nguồn tin và lưu lượng |
| **Hiệp hội ngành** | Nederland ICT, các hiệp hội AI Hà Lan | Uy tín + tiếp cận nhà tuyển dụng |
| **Agency tuyển dụng AI/Data** | Các agency chuyên ngành | Đăng tin số lượng lớn |
| **Cộng đồng kỹ thuật** | Meetup AI/ML tại Eindhoven, Amsterdam, Utrecht | Tài trợ nhỏ đổi lấy hiện diện thương hiệu |

---

## 7. Tối Ưu Chuyển Đổi (CRO)

| Ưu tiên | Việc | Lý do |
|---|---|---|
| 🔴 | Viết nội dung cho `/pages/info-for-employers` và `/pages/info-for-job-seekers` | Hiện là trang trắng — mọi chiến dịch đổ vào đây đều mất trắng |
| 🔴 | Form đăng tin 2 trường thay cho hướng dẫn gửi email | Giảm ma sát + tạo sự kiện đo được |
| 🔴 | Cài GA4 | Không đo được thì không tối ưu được |
| 🟡 | Đăng ký nhận cảnh báo việc làm qua email trên trang danh sách | Kênh giữ chân rẻ nhất |
| 🟡 | Hiển thị số tin thật và ngày đăng thật ("3 vacatures nieuw deze week") | Tín hiệu sống của job board |
| 🟡 | Ẩn 5 danh mục rỗng | Hứa nhiều hơn thực có làm mất niềm tin |
| ⚪ | Cân nhắc gỡ 3 tin việc làm tại Mỹ | Nhất quán định vị |

---

## 8. KPI & Ngân Sách

### 8.1 Mục tiêu theo quý

| Chỉ số | Q4/2026 | Q1/2027 | Q2/2027 | Q3/2027 |
|---|---|---|---|---|
| Tin đang hiệu lực | 120 | 250 | 450 | 800 |
| Tin mới/tháng | 40 | 70 | 120 | 200 |
| Nhà tuyển dụng hoạt động | 70 | 130 | 220 | 350 |
| Tỷ lệ đăng lại (≥2 tin) | 15% | 25% | 35% | 45% |
| Trang được index | 50 | 200 | 450 | 800 |
| Phiên organic/tháng | 500 | 3.000 | 8.000 | 15.000 |
| Có mặt trong Google Jobs | ✅ | ✅ | ✅ | ✅ |
| Chi phí trên mỗi tin mới | < €80 | < €60 | < €50 | < €40 |

### 8.2 Ngân sách

| Hạng mục | Tháng 1–3 | Tháng 4–6 | Tháng 7–12 |
|---|---|---|---|
| Kỹ thuật (sửa WAF, URL từng tin, schema, form) | €3.000 (một lần) | €500 | €500 |
| Quảng cáo | €0 → €1.140 | €2.600 | €2.600–5.000 |
| Nội dung (blog + trang tĩnh, EN+NL) | €800 | €800 | €600 |
| Công cụ (GA4 free, Semrush, email) | €200 | €200 | €250 |
| Thời gian đi lấy nguồn tin | nội bộ | nội bộ | nội bộ |
| **Tổng/tháng** | **~€1.500–2.500** | **~€4.100** | **~€4.000–6.400** |

> Ba tháng đầu, phần lớn ngân sách là **kỹ thuật chứ không phải media**. Đó là phân bổ đúng cho tình trạng hiện tại.

---

## 9. Lộ Trình

### Phase 0 — Mở cửa (T9–T10/2026)
- Gỡ chặn WAF cho Googlebot/Bingbot; sửa `robots.txt` mở cho bot AI
- Ngừng phục vụ Admin Portal ở `/pages/*`, `/llms.txt`, `/job/list`
- Cài GA4 + 5 sự kiện chuyển đổi; đăng ký Search Console
- Viết nội dung thật cho 3 trang tĩnh (EN + NL)
- Xây form đăng tin 2 trường
- Email 40 nhà tuyển dụng hiện có; mở 3 cuộc trò chuyện đối tác vùng
- Chạy Keyword Planner (toàn bộ tài liệu từ khóa đang là `TBD`)
- **Chốt quyết định định vị (§3)**

### Phase 1 — Làm cho việc làm index được (T11–T12/2026)
- URL riêng cho từng tin + `JobPosting` schema + sửa canonical phân trang
- Sitemap động; sửa `index-sitemap.xml`; hreflang đối xứng
- Bật quảng cáo nhắm nhà tuyển dụng (Tier 1, €1.140/tháng)
- Đẩy nguồn cung lên 120 tin
- Viết `llms.txt` thật

### Phase 2 — Hai chiều (T1–T3/2027)
- Sinh trang thành phố/danh mục vượt ngưỡng
- Trang `/companies/<company>` cho ~70 nhà tuyển dụng
- Bật quảng cáo nhắm người tìm việc (Tier 2) ở 3–5 thành phố mạnh nhất
- Đợt blog đầu: 6 bài báo cáo lương
- Newsletter hàng tuần

### Phase 3 — Tăng tốc (T4–T9/2027)
- Mở rộng phủ thành phố theo đà tăng nguồn cung
- Ký 2–3 đối tác vùng/trường đại học
- Retargeting sau khi có trang chi tiết từng tin
- Triển khai mô hình doanh thu đã chốt
- Cân nhắc mở rộng sang Bỉ (Flanders) — cùng ngôn ngữ, cùng mô hình

---

## 10. Câu Hỏi Cần Chốt

| # | Câu hỏi | Chặn việc gì | Mức khẩn |
|---|---|---|---|
| 1 | **Ai chịu trách nhiệm cấu hình BunkerWeb và bao giờ xong?** | Toàn bộ mọi thứ. Đã khuyến nghị 3 lần trong 39 ngày. | 🔴 Ngay |
| 2 | Định vị: châu Âu hay vùng Hà Lan? | Từ khóa, kiến trúc trang, ngôn ngữ ưu tiên | 🔴 Ngay |
| 3 | Nguồn tin đến từ đâu — crawler, nhà tuyển dụng gửi, hay đội đi lấy? | Khả năng tồn tại của mô hình | 🔴 Ngay |
| 4 | Mô hình doanh thu sau tin miễn phí đầu tiên? | Trang giá, tính ROI quảng cáo | 🟡 Tháng 1 |
| 5 | Có đầu tư dev cho trang chi tiết từng tin không? | Google Jobs — không có thì không vào được | 🔴 Ngay |
| 6 | Ai viết nội dung, và bằng ngôn ngữ nào trước? | Phase 0 | 🟡 Tháng 1 |
| 7 | Ngân sách marketing 12 tháng là bao nhiêu? | Quy mô toàn kế hoạch | 🟡 Tháng 1 |
| 8 | Pháp nhân/nhà sáng lập/năm thành lập là gì? | Trang About, schema `Organization`, E-E-A-T | ⚪ Tháng 2 |

---

*OnlyAIJobs.eu · Kế hoạch lập ngày 08/09/2026 dựa trên dữ liệu quét trực tiếp từ site*
