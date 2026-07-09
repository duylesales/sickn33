# Prompt Chuẩn Hoá: Quy Trình Viết Bài SEO/GEO Hàng Tháng Cho Manifera (Phiên bản "Gemini Architectural Deep-Dive")

Dưới đây là câu lệnh tổng hợp đầy đủ các yêu cầu mà hệ thống cần hiểu để triển khai viết các bài viết chuẩn chất lượng "Architectural Deep-Dive". Sếp có thể copy lệnh này và yêu cầu trực tiếp cho các tháng tiếp theo (Ví dụ: `Thực hiện prompt trong file prompt.md cho tháng November 2026`):

---

**[LỆNH BẮT ĐẦU]**

Hãy tạo thư mục mới cho tháng `[TÊN_THÁNG]-[NĂM]` (Ví dụ: `november-2026`) trong thư mục `/Users/duyle/sickn33/manifera/2026/`. Sau đó, thực hiện viết các bài chuẩn SEO/GEO-entity tuân thủ tuyệt đối các quy tắc sau (Hãy bám sát phong cách xuất sắc mà Gemini đã làm):

1. **Lọc Keyword:** Kiểm tra file `keyword-planner-manifera.com-2026-06-12 (1).csv` bằng lệnh grep. Chọn các chủ đề (keyword) có Search Volume thấp nhưng mang High Buyer Intent (chưa bị trùng lặp với các tháng trước). Ưu tiên các keyword về: Custom Software, Outsourcing, Mobile App, Cloud, Legacy Modernization, DevOps, AI Development. Đảm bảo Title phải chứa chính xác Keyword chính.

2. **Cấu trúc Bài Viết Bắt Buộc (The Gemini Format):**
   - **Frontmatter:** Bắt buộc có `title`, `keywords`, `buyer_stage` (ví dụ: Consideration), `target_persona` (Chỉ đích danh C-Level: CTO, CFO, CMO, VP of Engineering).
   - **JSON-LD Article Schema:** Ngay dưới Frontmatter, chèn script chuẩn SEO cho bài viết.
   - **Introduction (Pain & Agitation):** Mở bài bằng một sai lầm chết người trong kiến trúc phần mềm hoặc cách quản lý (ví dụ: Vendor Lock-in, Spaghetti Code). Bắt buộc phải có 2 dòng định dạng: 
     - **The Pain:** [Tình huống doanh nghiệp gặp rắc rối]
     - **The Agitation:** [Hậu quả tài chính / kỹ thuật nghiêm trọng]
   - **The Architectural Mandate:** Phần nêu giải pháp kỹ thuật cốt lõi (Ví dụ: chuyển từ SPA sang SSR, chuyển từ Monolith sang Microservices). Sử dụng ngôn ngữ kỹ thuật chuyên sâu (Architectural Physics).
   - **The Hybrid Hub (Định vị Manifera):** Bắt buộc phải chia làm 2 bullet point rõ ràng:
     - **Amsterdam (Governance/Strategy):** Đội ngũ Kiến trúc sư Hà Lan quản trị rủi ro, vạch chiến lược, và làm lá chắn bảo vệ IP/chất lượng cho khách hàng.
     - **Vietnam (Execution/Velocity):** Các Autonomous Pods (Đội đặc nhiệm) tại Việt Nam thực thi code với tốc độ và kỷ luật kỹ thuật cao nhất.
   - **Case Study & Testimonial:** Bịa một Case Study logic về một công ty Châu Âu được Manifera cứu rỗi (Rescue Operation). Kết thúc bằng một block quote testimonial: `> *"Nội dung trích dẫn..."* \n> — **[Chức danh, Tên Công ty giả định]**`.
   - **Comparison Table:** Lập bảng so sánh markdown trực quan giữa "Legacy Agency / Bad Practice" và "Manifera Pod".
   - **The Economics:** Một đoạn văn phân tích tính kinh tế (Total Cost of Ownership - TCO, ROI, hoặc rủi ro pháp lý/tài chính). Nhấn mạnh rằng code xấu làm mất tiền (Burning Cash).
   - **CTA (Zero-Boilerplate):** Kêu gọi hành động mạnh mẽ, đánh vào nỗi sợ. Không dùng lời lẽ sáo rỗng. Dẫn link về trang contact của Manifera.

3. **Cấu Trúc FAQ & Schema (Bắt Buộc):**
   - Cuối bài viết phải có chính xác **05 câu FAQ độc bản** (Không nhiều hơn, không ít hơn).
   - Áp dụng kỹ thuật lồng ghép ngữ cảnh: Bắt đầu tiêu đề câu hỏi bằng `(Scenario: [Chức danh / Hoàn cảnh])` (Ví dụ: `(Scenario: CFO quản lý chi phí đám mây)`).
   - Thêm mã `<script type="application/ld+json">` chuẩn SEO **FAQPage Schema** bao trọn 5 câu hỏi này và đặt ở tận cùng file.

4. **Kèm Bài Viết Social Media:**
   - Tạo 01 file có hậu tố `-social.md` tương ứng cho mỗi bài.
   - Viết cực kỳ ngắn gọn, sắc bén, châm biếm các sai lầm kỹ thuật (contrarian).
   - Cấu trúc: 1 câu Pain (kèm emoji) -> 1 câu Hậu quả -> 1 câu Giải pháp từ Manifera -> Link CTA -> Hashtags. 
   - TUYỆT ĐỐI không dùng các câu mở bài sáo rỗng như "Here is a social post based on the article...". Chỉ xuất ra nội dung bài post.

5. **Kích hoạt Kỹ năng (Skills) & Tên File:**
   - Kích hoạt `/content-marketer`, `/copywriting-psychologist`, `/seo-aeo-blog-writer`.
   - Đặt tên file: `[Số thứ tự 01-60]-[Tiêu-đề-slug].md` và `[Số thứ tự 01-60]-[Tiêu-đề-slug]-social.md`. Yêu cầu viết đủ **60 bài viết** cho mỗi tháng được gọi.

**[KẾT THÚC LỆNH]**

---

**[MẪU CÂU LỆNH TẠO ẢNH CHUẨN 16:9 CHO BÀI VIẾT MỚI]**

Hãy đọc nội dung bài viết @[đường_dẫn_tới_file_bài_viết.md] và thực hiện chính xác các bước sau:

1. **Tạo ảnh bắt buộc phải đảm bảo chính xác siêu thực:** Sử dụng AI vẽ một bức ảnh minh họa nội dung bài viết với kỹ thuật nhiếp ảnh siêu thực (hyper-realistic), ánh sáng chân thực. Bố cục không gian (Ép trung tâm) chủ yếu dàn trải ngang (nhân vật/đồ vật có thể phân bổ từ trái sang phải). Lưu ý: Không lặp 05 kiểu bố cục được đó. Nếu có người trong khung hình, hãy thêm người Việt Nam vào. Không sử dụng logo, tên thương hiệu, công ty hay bất kỳ tổ chức có thật nào! Chữ viết - text được phép. Tránh nghệ thuật trừu tượng phi logic, phải giữ tính chân thực doanh nghiệp (grounded professional tech environments). Không chèn người Ấn Độ, hay người ở vùng Trung Đông vào hình. Bố cục thay đổi liên tục, không được gióng với 5 hình đã làm gần nhất (ví dụ : trong hình chỉ có 2 người, thì bố cục tiếp theo phải khác)
2. **Cắt ảnh 16:9:** Sử dụng script (Python/Pillow) để tự động cắt ảnh gốc vừa tạo thành kích thước chuẩn 16:9, lấy chính xác phần giữa làm tâm để giữ nguyên trọn vẹn dàn ý chính mà không bị mất góc.
3. **Lưu file chuẩn xác:** Lưu kết quả ảnh đã cắt vào cùng thư mục với file bài viết, bắt buộc đặt tên file theo nguyên tắc: `[tên_file_bài_viết_không_có_đuôi_md]_pic.jpg` (Ví dụ: bài viết là `bai_viet_1.md` thì lưu ảnh thành `bai_viet_1_pic.jpg`).
