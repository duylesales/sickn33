# 📘 OnlyAIJobs — Tài Liệu Tham Chiếu SEO/GEO-Entity (Master Brief)

> **MỤC ĐÍCH CỦA FILE NÀY:**
> Nguồn sự thật duy nhất (Single Source of Truth) để viết mọi nội dung blog, social và marketing cho OnlyAIJobs.
> **Nguồn dữ liệu**: quét trực tiếp onlyaijobs.eu ngày 08/09/2026 (qua User-Agent GPTBot — xem [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md)).
> **⚠️ Cảnh báo về mức độ đầy đủ**: OnlyAIJobs chưa có tài liệu thương hiệu nội bộ nào. Mọi trường dưới đây đều **quan sát được từ site thật**. Các trường chưa xác minh được đánh dấu 🟥 **CẦN BỔ SUNG** — không được bịa khi viết nội dung.

---

## 1. THÔNG TIN NỀN TẢNG (Entity Profile)

| Thuộc tính | Giá trị | Nguồn |
|---|---|---|
| **Tên thương hiệu** | OnlyAIJobs (hiển thị: "Only AI Jobs") | `<title>`, `og:site_name` |
| **Website** | https://onlyaijobs.eu | |
| **Loại hình** | Job board chuyên ngành AI (two-sided marketplace) | Quan sát |
| **Ngôn ngữ** | 🇬🇧 English (mặc định) + 🇳🇱 Nederlands tại `/nl` | Menu đã dịch đầy đủ |
| **Email liên hệ / đăng tin** | info@onlyaijobs.eu | Banner "For Employer" |
| **Đơn vị phát triển** | Manifera (Sentry DSN trỏ `sentry.manifera.com`) | Header HTML |
| **Phiên bản ứng dụng** | 2.2.1 | Footer |
| **Bản quyền** | © 2026 OnlyAIJobs | Footer |
| **Pháp nhân, năm thành lập, đội ngũ, nhà sáng lập** | 🟥 **CẦN BỔ SUNG** | Trang `/pages/about-us` hiện rỗng |
| **Mạng xã hội** | 🟥 **CẦN BỔ SUNG** — không tìm thấy liên kết nào trên site | |
| **Google Analytics / GTM** | 🟥 **CẦN XÁC MINH** — không phát hiện trong HTML | |

### 1.1. Tuyên bố sứ mệnh (nguyên văn trên trang chủ)

> *"The platform where findability and accessibility of vacancies are central. Our mission is simple: we want to enable everyone, from graduates to experienced professionals, to quickly and easily find companies in their immediate vicinity that are looking for talent."*

### 1.2. Câu chuyện nguồn gốc (nguyên văn trang chủ) — tài sản kể chuyện mạnh nhất

> *"OnlyAIJobs was created based on an insight from various studies. This showed that many vacancy seekers from **Noord-Brabant** leave for the **Randstad** area, not because they necessarily want to work there, but because they often do not know which interesting companies are in their region."*

**🇻🇳 Vì sao đoạn này quan trọng**: đây là thứ duy nhất trên site không thể sao chép — một luận điểm cụ thể, có địa danh, có nguyên nhân. Mọi job board đều nói "tìm việc dễ hơn". Chỉ OnlyAIJobs nói được "sinh viên Brabant bỏ quê ra Randstad chỉ vì không biết công ty hay nào ở ngay gần nhà". Đây phải là hạt nhân của mọi nội dung.

### 1.3. ⚠️ MÂU THUẪN ĐỊNH VỊ CHƯA GIẢI QUYẾT

| Nguồn | Định vị được ngụ ý |
|---|---|
| Tên miền `.eu` | Toàn châu Âu |
| `meta description` | *"connects AI talents with **top European companies**"* → toàn châu Âu |
| Schema `Organization` | *"**European** job board for AI, ML and Data Science careers"* → toàn châu Âu |
| Nội dung trang chủ | Noord-Brabant → Randstad, "vacancies at the exact **address level**", "distance from your home" → **siêu địa phương, theo bán kính** |
| Thực tế nguồn tin | 49/52 tin tại Hà Lan, 3 tin tại Mỹ | Hà Lan |

**Không thể phục vụ cả hai.** "AI jobs Europe" đấu với LinkedIn/Indeed/AI-Jobs.net trên từ khóa quốc tế; "vacatures AI in de buurt" đấu với Indeed NL trên từ khóa Hà Lan có ý định địa phương. Hai chiến lược nội dung, hai bộ từ khóa, hai kiểu landing page hoàn toàn khác nhau.
👉 **Quyết định này phải chốt trước mọi việc khác** — xem [`implementation_plan.md`](./implementation_plan.md) §9 câu hỏi #1.

---

## 2. SẢN PHẨM (Product Entities)

### 2.1. Phía người tìm việc (Job Seekers)

| Tính năng | Trạng thái quan sát được |
|---|---|
| Duyệt việc làm | ✅ `/jobs`, 10 tin/trang, 6 trang |
| Bộ lọc | ✅ Thành phố · Loại hình (Full-time, Part-time, Internship, Remote) · Danh mục · Thời gian đăng (2 giờ → 1 tháng) · Sắp xếp tăng/giảm |
| Lưu việc làm | ✅ "Saved jobs" |
| Xem theo khoảng cách từ nhà | ✅ Được nêu trong FAQ trang chủ (điểm khác biệt cốt lõi) |
| Trang chi tiết từng việc làm | ❌ **KHÔNG CÓ** — tin mở rộng ngay trong danh sách, không có URL riêng |
| Tạo hồ sơ / ứng tuyển trên site | ❌ Không — người dùng được dẫn tới trang tuyển dụng của công ty |
| Cảnh báo việc làm qua email | 🟥 **CẦN XÁC MINH** — không thấy trên giao diện công khai |

### 2.2. Phía nhà tuyển dụng (Employers)

> Nguyên văn banner: *"To post a vacancy on OnlyAIJobs, simply send an email with a link to the job listing on your company's website to info@onlyaijobs.eu. **One vacancy on OnlyAIJobs is free**."*

| Yếu tố | Trạng thái |
|---|---|
| Cách đăng tin | 📧 **Gửi email thủ công** — không có luồng tự phục vụ |
| Giá | Tin đầu tiên **miễn phí**; giá cho tin thứ 2 trở đi 🟥 **CẦN BỔ SUNG** (không có trang giá) |
| Trang `/pages/add-a-vacancy` | ❌ Rỗng (trả về vỏ Admin Portal) |
| Trang `/pages/info-for-employers` | ❌ Rỗng |
| Trang thương hiệu nhà tuyển dụng | ❌ Không có |

**🇻🇳 Hệ quả marketing**: mọi chiến dịch nhắm nhà tuyển dụng hiện tại sẽ đổ traffic vào một trang trắng. **Phải viết nội dung cho 2 trang này trước khi chi bất kỳ đồng quảng cáo nào.**

### 2.3. Danh mục việc làm (11 danh mục hiển thị trong bộ lọc)

| Danh mục | Số tin thực tế (8/9/2026) |
|---|---|
| Development | ~27 (kể cả kết hợp) |
| Machine Learning | ~28 (kể cả kết hợp) |
| Research | ~9 |
| Infrastructure | 1 |
| Ethics & Governance | 1 |
| Robotics Engineer | 2 |
| **AI Product** | **0** |
| **Computer Vision** | **0** |
| **Generative AI** | **0** |
| **Quality Control** | **0** |
| **Security and Safety** | **0** |

> ⚠️ 5/11 danh mục hoàn toàn rỗng. Bộ lọc đang hứa hẹn nhiều hơn kho tin thực có — vừa là vấn đề trải nghiệm, vừa tạo ra trang danh mục rỗng nếu sau này index theo danh mục.

---

## 3. NGUỒN CUNG HIỆN TẠI (Supply Snapshot 08/09/2026)

| Chỉ số | Giá trị |
|---|---|
| Tổng số tin | **52** |
| Số công ty | ~40 |
| Độ tươi | ⚠️ **100% tin hiển thị "Posted 1 month ago"** — không có tin mới ≥30 ngày |
| Loại hình | 100% Full-time |
| Quốc gia | 49 Hà Lan · 3 Mỹ (qua Lensa) |
| Thành phố tiêu biểu | Ede, Groningen, Eindhoven, Capelle aan den IJssel, Amsterdam, Utrecht |

**Nhà tuyển dụng đang có tin** (dùng làm bằng chứng xã hội trong mọi nội dung — đây là tài sản thuyết phục mạnh nhất hiện có):
Accenture · Cegeka Nederland · Sendcloud · Stichting Mollie Payments · Heijmans · Rexel Nederland B.V. · VINCI Energies · AMCS · Boltrics · Winparts · Hoppinger · WebNL · Holland Innovative B.V. · Eminent Groep B.V. · UnitedConsumers C.V. · 4Dotnet B.V. · Admix · Data-First Interim · BK IT Solutions · Lensa (Mỹ)

> **🇻🇳 Đây là bài toán "con gà quả trứng" kinh điển của marketplace.** 52 tin cũ 1 tháng thì không đáng để chi tiền kéo người tìm việc — họ vào, thấy ít tin cũ, rời đi và không quay lại. **Nguồn cung phải được giải trước nhu cầu.** Toàn bộ [`implementation_plan.md`](./implementation_plan.md) được xây theo nguyên tắc này.

---

## 4. GIÁ TRỊ KHÁC BIỆT (USPs)

### USP 1: Hiển thị việc làm ở cấp độ **địa chỉ chính xác**
Không phải "Amsterdam" hay "Noord-Holland" mà là địa chỉ cụ thể + khoảng cách từ nhà bạn. Không job board lớn nào làm điều này vì họ tối ưu cho quy mô, không cho bán kính.

### USP 2: Sân chơi bình đẳng cho công ty nhỏ
Nguyên văn FAQ: *"a level playing field where all companies can showcase their vacancies without being pushed aside by competitors with larger advertising budgets."* — trên Indeed, công ty trả nhiều tiền hơn thì hiện lên trước. Ở đây thì không.

### USP 3: Chống chảy máu nhân tài vùng
Giữ nhân tài ở lại quê nhà bằng cách cho họ thấy công ty hay ngay gần đó. Đây là góc kể chuyện có sức nặng với **chính quyền địa phương, khu công nghệ và hiệp hội doanh nghiệp** — nhóm đối tác mà job board thương mại không tiếp cận được.

### USP 4: Chuyên biệt 100% về AI
Không phải "job board có mục AI" mà là job board chỉ có việc làm AI. Người tìm việc AI không phải lọc qua hàng nghìn tin không liên quan.

### USP 5: Thân thiện với thông tuyến bền vững
Nguyên văn FAQ: chọn việc gần nhà → đi lại ít hơn → phát thải thấp hơn. Góc ESG này ít job board nào chạm tới.

---

## 5. ĐỐI TƯỢNG MỤC TIÊU

### Persona A — Sinh viên/mới tốt nghiệp ngành AI/Data tại NL
- **Nỗi đau**: không biết công ty nào gần nhà đang tuyển; mặc định nghĩ phải lên Amsterdam
- **Nội dung phù hợp**: "10 công ty AI ở Brabant bạn chưa từng nghe tên", hướng dẫn nghề nghiệp, mức lương khởi điểm
- **Kênh**: TikTok/Instagram, hợp tác trường đại học (TU/e, Tilburg, Fontys, JADS), Reddit

### Persona B — Kỹ sư AI/ML có kinh nghiệm đang cân nhắc chuyển việc
- **Nỗi đau**: LinkedIn đầy recruiter spam; muốn xem việc thật ở nơi mình sống
- **Nội dung phù hợp**: so sánh lương, phân tích thị trường AI Hà Lan, "remote vs hybrid trong ngành AI"
- **Kênh**: LinkedIn, newsletter, cộng đồng kỹ thuật

### Persona C — Hiring manager / recruiter tại công ty tuyển AI
- **Nỗi đau**: đăng LinkedIn/Indeed tốn kém và thu về hồ sơ không liên quan
- **Nội dung phù hợp**: chi phí tuyển dụng, cách viết JD cho vai trò AI, thị trường lương
- **Kênh**: LinkedIn, email trực tiếp, hiệp hội ngành

### Persona D — Tổ chức vùng (chính quyền, khu công nghệ, hiệp hội doanh nghiệp)
- **Nỗi đau**: nhân tài trẻ rời khỏi vùng
- **Nội dung phù hợp**: số liệu chảy máu nhân tài, báo cáo vùng, câu chuyện thành công
- **Kênh**: quan hệ trực tiếp, PR địa phương
- **🇻🇳 Ghi chú**: đây là persona **bị bỏ quên hoàn toàn** hiện nay, nhưng có thể là kênh phân phối rẻ nhất — Brainport Eindhoven, Midpoint Brabant, các gemeente đều có ngân sách cho đúng vấn đề này.

---

## 6. GIỌNG VĂN & QUY TẮC VIẾT

### 6.1. Giọng văn
- **Thực tế, không kêu gào** — job board nói quá dễ mất tin cậy
- **Cụ thể theo địa danh** — luôn nêu tên thành phố, tên công ty thật, khoảng cách thật
- **Ngôi thứ hai** ("you" / "je" trong tiếng Hà Lan — dùng "je" chứ không dùng "u", vì nhóm người tìm việc trẻ)
- **Song ngữ nhưng không dịch máy móc**: bản NL phải là bản viết lại cho người Hà Lan, không phải bản dịch từng chữ của bản EN

### 6.2. ❌ KHÔNG BAO GIỜ
1. Không tuyên bố quy mô mà site không có ("hàng nghìn việc làm" khi đang có 52)
2. Không bịa số liệu thống kê thị trường AI — dẫn nguồn thật hoặc bỏ
3. Không copy mô tả công ty nguyên văn từ tin tuyển dụng vào bài blog
4. Không dùng cùng một cấu trúc mở bài cho hai bài liên tiếp
5. Không viết bài tiếng Anh nhắm từ khóa Hà Lan và ngược lại

### 6.3. ✅ PHẢI LÀM
1. Mỗi bài chọn **một** persona và **một** ngôn ngữ
2. Dùng tên công ty thật đang có tin trên site làm ví dụ (danh sách ở §3)
3. Kết bài bằng CTA cụ thể luân phiên: xem việc làm theo danh mục / theo thành phố / đăng tin miễn phí / nhận cảnh báo việc làm
4. Nêu số liệu có kiểm chứng được và ghi ngày (thị trường AI thay đổi nhanh, số liệu cũ làm mất uy tín)

---

## 7. HIỆN TRẠNG KỸ THUẬT — ĐỌC TRƯỚC KHI LẬP KẾ HOẠCH BẤT KỲ

| Vấn đề | Mức | Chi tiết |
|---|---|---|
| WAF chặn Googlebot 39 ngày liên tiếp | 🔴 | GPTBot/ClaudeBot lại vào được — đảo ngược hoàn toàn |
| `robots.txt` chặn mọi bot AI | 🔴 | `Disallow: /` cho `User-agent: *` |
| Không có `JobPosting` schema | 🔴 | Không đủ điều kiện vào Google Jobs |
| Không có URL riêng cho từng tin | 🔴 | Không có gì để index theo vị trí tuyển dụng |
| Phân trang canonical về trang 1 | 🔴 | 42/52 tin vô hình với công cụ tìm kiếm |
| 4 URL trong sitemap trả vỏ admin rỗng | 🔴 | Gồm cả 2 trang thương mại quan trọng nhất |
| `index-sitemap.xml` sai cú pháp | 🟡 | Phần tử `<sitemap>` trỏ tới trang, không phải tệp sitemap |
| hreflang không đối xứng | 🟡 | Trang EN không khai `nl` → Google bỏ qua cả cụm |
| Blog rỗng | 🟡 | 0 bài |
| 5/11 danh mục rỗng | 🟡 | |

Chi tiết đầy đủ: [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md).

---

## 8. NHỮNG GÌ CÒN THIẾU TRONG TÀI LIỆU NÀY

Trước khi sản xuất nội dung quy mô lớn, cần bổ sung từ phía chủ sở hữu:

| # | Thông tin thiếu | Vì sao cần |
|---|---|---|
| 1 | Pháp nhân, năm thành lập, người sáng lập | E-E-A-T, schema `Organization`, trang About |
| 2 | Mô hình doanh thu sau tin miễn phí đầu tiên | Không có thì không viết được trang giá, không chạy được quảng cáo nhắm nhà tuyển dụng |
| 3 | Quyết định định vị: châu Âu hay Hà Lan/Brabant? | Quyết định toàn bộ bộ từ khóa (§1.3) |
| 4 | Có tài khoản mạng xã hội nào không? | Kênh phân phối + `sameAs` schema |
| 5 | Nguồn tin: tự thu thập, crawler, hay nhà tuyển dụng gửi? | Site có quyền `VIEW_CRAWLER` trong admin → nghi có crawler; ảnh hưởng tới chiến lược nguồn cung |
| 6 | Ngân sách và người phụ trách marketing | Quy mô kế hoạch |

---

*Tài liệu liên quan: [`implementation_plan.md`](./implementation_plan.md) · [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) · [`paid_ads_plan.md`](./paid_ads_plan.md) · [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md) · [`google_ads_rsa_copy_onlyaijobs.md`](./google_ads_rsa_copy_onlyaijobs.md) · [`extra-keywords.md`](./extra-keywords.md)*
