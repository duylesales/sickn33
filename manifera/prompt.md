# Prompt Chuẩn Hoá: Quy Trình Viết Bài SEO/GEO Hàng Tháng Cho Manifera

Dưới đây là câu lệnh tổng hợp đầy đủ các yêu cầu mà hệ thống cần hiểu để triển khai viết 05 bài viết chuẩn chất lượng như đã làm với tháng 8/2026. Sếp có thể copy lệnh này và yêu cầu trực tiếp cho các tháng tiếp theo (Ví dụ: `Thực hiện prompt trong file prompt.md cho tháng November 2026`):

---

**[LỆNH BẮT ĐẦU]**

Hãy tạo thư mục mới cho tháng `[TÊN_THÁNG]-[NĂM]` (Ví dụ: `november-2026`) trong thư mục `/Users/duyle/sickn33/manifera/2026/`. Sau đó, thực hiện viết 05 bài chuẩn SEO/GEO-entity tuân thủ tuyệt đối các quy tắc sau:

1. **Lọc Keyword:** Kiểm tra file `keyword-planner-manifera.com-2026-06-12 (1).csv` bằng lệnh grep. Chọn 05 chủ đề (keyword) chất lượng cao, chưa bị trùng lặp với các tháng trước (ví dụ như đã viết ở july-2026, august-2026, september-2026). Ưu tiên các keyword về: Custom Software, Outsourcing, Mobile App, Cloud, Legacy Modernization, DevOps, AI Development.
2. **Chất lượng Bài Viết (CTO-level):**

   - Không viết chung chung, không viết qua loa ("no-BS").
   - Bài viết phải mang tính chuyên sâu, tập trung vào đối tượng là CTO, VP Engineering, hoặc Enterprise Founder.
   - Bắt buộc phải **trích dẫn (quote)** từ các chuyên gia công nghệ uy tín (ví dụ: Martin Fowler, Gene Kim, Kelsey Hightower, Werner Vogels, v.v...) để tăng tính xác thực và độ tin cậy.
   - Có bảng so sánh (decision matrix) hoặc số liệu thực tế chứng minh luận điểm.
3. **Cấu Trúc FAQ & Schema (Bắt Buộc):**

   - Cuối mỗi bài viết phải có chính xác **05 câu FAQ độc bản** (Tuyệt đối không nhiều hơn, không ít hơn).
   - Áp dụng kỹ thuật lồng ghép ngữ cảnh: `(Scenario: [Chức danh / Hoàn cảnh])` vào trong tiêu đề câu hỏi FAQ.
   - Thêm mã `<script type="application/ld+json">` chuẩn SEO **FAQPage Schema** bao trọn 5 câu hỏi này và đặt ở cuối file.
4. **Kèm Bài Viết Social Media:**

   - Với mỗi bài viết chính (`.md`), tạo thêm 01 file social post có hậu tố `-social.md`.
   - Viết theo phong cách "Claude-style": Sử dụng emoji làm bullet point, câu văn ngắn gọn, bóc trần sự thật (insightful/contrarian), hook mạnh mẽ, không dài dòng, và có đính kèm hashtag liên quan.
5. **Đặt Tên File Chuẩn:**

   - Đặt tên file theo định dạng: `[Số thứ tự 01-05]-[Tiêu-đề-slug].md` và `[Số thứ tự 01-05]-[Tiêu-đề-slug]-social.md`.

Hãy áp dụng các skill content-creator, content-marketer, và copy-editing để thực hiện!

**[KẾT THÚC LỆNH]**

---

**[MẪU CÂU LỆNH TẠO ẢNH CHUẨN 16:9 CHO BÀI VIẾT MỚI]**

Hãy đọc nội dung bài viết @[đường_dẫn_tới_file_bài_viết.md] và thực hiện chính xác các bước sau:

1. **Tạo ảnh bắt buộc phải đảm bảo chính xác siêu thực:** Sử dụng AI vẽ một bức ảnh minh họa nội dung bài viết với kỹ thuật nhiếp ảnh siêu thực (hyper-realistic), ánh sáng chân thực. Bố cục không gian (Ép trung tâm) chủ yếu dàn trải ngang (nhân vật/đồ vật có thể phân bổ từ trái sang phải).Lưu ý /; không lặp 05 kiểu bố cục được đó.
2. **Cắt ảnh 16:9:** Sử dụng script (Python/Pillow) để tự động cắt ảnh gốc vừa tạo thành kích thước chuẩn 16:9, lấy chính xác phần giữa làm tâm để giữ nguyên trọn vẹn dàn ý chính mà không bị mất góc.
3. **Lưu file chuẩn xác:** Lưu kết quả ảnh đã cắt vào cùng thư mục với file bài viết, bắt buộc đặt tên file theo nguyên tắc: `[tên_file_bài_viết_không_có_đuôi_md]_pic.jpg` (Ví dụ: bài viết là `bai_viet_1.md` thì lưu ảnh thành `bai_viet_1_pic.jpg`).
