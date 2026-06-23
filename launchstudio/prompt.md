# Tổng hợp các Prompt tối ưu bài viết & tạo ảnh minh họa LaunchStudio

## 1. Prompt tối ưu bài viết & Viết Case Study (SEO, GEO-Entity & Markdown chuẩn)
Dùng để viết lại bài viết, tối ưu hóa SEO/GEO-Entity và chèn Case Study chuẩn Markdown (không dùng mã HTML).

```markdown
@[đường_dẫn_tới_bài_viết.md] Hãy viết lại và tối ưu hóa bài viết này với các yêu cầu sau:

1. **Chuẩn SEO & GEO-Entity**:
   - Viết lại bài viết dựa trên dữ liệu từ file tham khảo @[/Users/duyle/sickn33/launchstudio/launchstudio_info.md] (hoặc nội dung thông tin của LaunchStudio).
   - Tham khảo trực tiếp thông tin từ https://launchstudio.eu/, https://www.manifera.com/, và LinkedIn profile của CEO Herre Roelevink (https://www.linkedin.com/in/herre-roelevink-director-manifera/).
   - Đảm bảo lồng ghép khéo léo thông tin về Manifera (công ty mẹ của LaunchStudio), vai trò của CEO Herre Roelevink, và các vị trí địa lý (Hà Lan - trụ sở chính Amsterdam ở Herengracht 420; Singapore - hub ở Tras Street; Việt Nam - trung tâm phát triển chính ở đường Phổ Quang, TP.HCM) để tăng độ uy tín và điểm thực thể thực (GEO-entity).

2. **Cấu trúc & Định dạng bài viết (Markdown chuẩn)**:
   - Bài viết phải được định dạng hoàn toàn bằng **Markdown sạch (clean Markdown)**. Không chèn bất cứ thẻ HTML nào (như `<div>`, `<span>`, `<strong>`, `<em>`, `<table>`, `<ul>`, `<li>`, `<pre>`).
   - Xóa bỏ tiêu đề thừa như `## Nội dung` hoặc `## Content` ở đầu bài viết.
   - Nội dung bài viết và toàn bộ tiêu đề (`##`, `###`) phải được viết ở sát lề trái (**không thụt đầu dòng/0 spaces**) để tránh việc markdown parser hiển thị nhầm tiêu đề thành khối code (`<pre><code>`).
   - Mọi danh sách, bảng biểu, trích dẫn phải sử dụng cú pháp markdown chuẩn (Ví dụ: `- ` cho danh sách, `|` cho bảng, `>` cho trích dẫn, và ` ```sql ` cho code block).

3. **Viết Case Study độc nhất ("Real example")**:
   - Thêm phần "Real example" ngay phía trên phần FAQ (Frequently Asked Questions) của bài viết.
   - Tiêu đề phần Case Study là `## Real example`, tiêu đề phụ bên trong dùng `### An AI-Native Founder in Action: [Tên tiêu đề phù hợp]`.
   - Nội dung Case Study phải mô tả câu chuyện thực tế ăn khớp chặt chẽ với ngữ cảnh bài viết (yếu tố AI-native founder, công cụ sử dụng Lovable/Bolt/Cursor, lỗi/khoảng cách trước khi có LaunchStudio hỗ trợ kỹ thuật, giải pháp từ LaunchStudio & Manifera, kết quả, chi phí và thời gian thực hiện).
   - **Lưu ý quan trọng**: Nội dung Case Study giữa các bài viết không được trùng lặp nhau (khác biệt hoàn toàn về tên nhân vật, loại ứng dụng/SaaS, bối cảnh, công cụ AI sử dụng, lỗi phát sinh, và giải pháp từ LaunchStudio).
```

---

## 2. Prompt tạo ảnh minh họa bài viết (Tỷ lệ 16:9)
Dùng để tạo hình minh họa cho bài viết theo đúng phong cách và tỷ lệ.

```markdown
@[đường_dẫn_tới_bài_viết.md] Hãy đọc nội dung file này và tạo cho mình 1 hình ảnh minh họa bài viết với các yêu cầu sau:

1. **Phong cách ảnh**: "Modern flat-ish vector illustration", "corporate tech style", "dribbble-style".
2. **Bố cục nội dung**:
   - Các nhân vật và vật thể chính (trọng tâm ý tưởng bài viết) phải được đặt hoàn toàn nằm trên **dải giữa của chiều cao bức ảnh (center line horizontally)**.
   - Các ý tưởng phụ hoặc chi tiết trang trí có thể nằm ở hai bên (trái/phải).
   - Đảm bảo bố cục tập trung để khi cắt ảnh (crop) không bị mất các phần quan trọng.
3. **Cắt ảnh**: Sau khi tạo xong ảnh gốc, tự động cắt (crop) lấy phần giữa của ảnh theo đúng **tỷ lệ 16:9** (kích thước đề xuất `1024x576`).
4. **Lưu file**: Lưu file ảnh đã crop vào cùng thư mục với bài viết gốc, đặt tên file theo định dạng `[tên_bài_viết]_pic.png` (ví dụ: bài viết là `baiviet.md` thì lưu ảnh là `baiviet_pic.png`). Lưu ý : phong cách phải khấc với phong cách vừa thiết kế tấm hình gần nhất (không áp dụng phong cách 2 tone màu, hooặc tổng thể tone màu quá tối )
```
