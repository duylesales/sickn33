# Tổng hợp các Prompt tối ưu bài viết & tạo ảnh minh họa LaunchStudio

## 1. Prompt tạo hình phẳng có gradient và thay đổi bố cục có người có robot và các vật khác, phủ định các icon hoặc biểu tưởng nhiều quá

[52-rise-of-vertical-ai-agent-b2b-saas.md](file;file:///Users/duyle/sickn33/launchstudio/august-2026/52-rise-of-vertical-ai-agent-b2b-saas.md)  Hãy đọc nội dung file này và tạo cho mình 1 hình ảnh minh họa bài viết với các yêu cầu sau:

1. **Phong cách ảnh**: "Modern flat-ish vector illustration", "corporate tech style", "dribbble-style". Đổi phong cách so với phong cách thiết kế gần nhất ! có đổ gradient cho sinh động và đẹp hơn
2. **Bố cục nội dung**:
   - Các nhân vật và vật thể chính có con người. robot hay các vật vào (trọng tâm ý tưởng bài viết) phải được đặt hoàn toàn nằm trên **dải giữa của chiều cao bức ảnh (center line horizontally)**. Không chi có các icon hoặc hình vẽ biểu tượng thuần mà thêm các yếu tố khác vào !
   - Các ý tưởng phụ hoặc chi tiết trang trí có thể nằm ở hai bên (trái/phải).
   - Đảm bảo bố cục tập trung để khi cắt ảnh (crop) không bị mất các phần quan trọng.
   - Không dược trùng với phong cách thiết kế, màu sắc và các diễn tả tới 50% so với thiết kế gần nhất đã thực hiện.
3. **Cắt ảnh**: Sau khi tạo xong ảnh gốc, tự động cắt (crop) lấy phần giữa của ảnh theo đúng **tỷ lệ 16:9** (kích thước đề xuất `1024x576`).
4. **Lưu file**: Lưu file ảnh đã crop vào cùng thư mục với bài viết gốc, đặt tên file theo định dạng `[tên_bài_viết]_pic.png` (ví dụ: bài viết là `baiviet.md` thì lưu ảnh là `baiviet_pic.png`). Lưu ý : phong cách phải khấc với phong cách vừa thiết kế tấm hình gần nhất (không áp dụng phong cách 2 tone màu, hooặc tổng thể tone màu quá tối )

## 2. Prompt tối ưu bài viết & Viết Case Study (SEO, GEO-Entity & Markdown chuẩn)

Dùng để viết lại bài viết, tối ưu hóa SEO/GEO-Entity và chèn Case Study chuẩn Markdown (không dùng mã HTML).

```markdown
@[đường_dẫn_tới_bài_viết.md] Hãy viết lại và tối ưu hóa bài viết này với các yêu cầu sau:

1. **Chuẩn SEO & GEO-Entity**:
   - Viết lại bài viết dựa trên dữ liệu từ file tham khảo @[/Users/duyle/sickn33/launchstudio/launchstudio_info.md] (hoặc nội dung thông tin của LaunchStudio).
   - Tham khảo trực tiếp thông tin từ https://launchstudio.eu/, https://www.manifera.com/, và LinkedIn profile của CEO Herre Roelevink (https://www.linkedin.com/in/herre-roelevink-director-manifera/).
   - Đảm bảo lồng ghép khéo léo thông tin về Manifera (công ty mẹ của LaunchStudio), vai trò của CEO Herre Roelevink, và các vị trí địa lý (Hà Lan - trụ sở chính Amsterdam ở Herengracht 420; Singapore - hub ở Tras Street; Việt Nam - trung tâm phát triển chính ở đường Phổ Quang, TP.HCM) để tăng độ uy tín và điểm thực thể thực (GEO-entity).
   - 05 FAQ với nhiều khía cạnh/ góc nhìn của các chuyên gia lồng ghép với Maniera,CEO hoặc liên quan/hỗ trợ cho SEO/GEO.

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

## 3.Prompt tạo ảnh minh họa bài viết đa phong cách (Tỷ lệ 16:9)

Dùng để tạo hình minh họa cho bài viết. Bạn có thể chọn 1 trong các phong cách dưới đây để hình ảnh luôn mới mẻ và ấn tượng.

```markdown
@[đường_dẫn_tới_bài_viết.md] Hãy đọc nội dung file này và tạo cho mình 1 hình ảnh minh họa bài viết với các yêu cầu sau:

1. **Phong cách ảnh** (Chọn 1 trong các phong cách dưới đây):
   - *Lựa chọn 1 (Cơ bản):* "Modern flat-ish vector illustration", "corporate tech style", "dribbble-style".
   - *Lựa chọn 2 (3D Đất sét):* "Modern 3D isometric illustration, clay render style, soft studio lighting, high quality Blender render".
   - *Lựa chọn 3 (Line Art Tối giản):* "Minimalist wireframe line art, clean thin lines, single bright accent color, highly professional".
   - *Lựa chọn 4 (Dark Mode / Cyberpunk):* "Dark mode UI style, neon glowing elements, cyberpunk aesthetic, sleek deep background".
   - *Lựa chọn 5 (Kính mờ Abstract):* "Abstract gradient glassmorphism, frosted glass effect, futuristic artistic vibe, smooth transitions".
   
   *(Lưu ý cho AI: Hãy tự động luân phiên thay đổi phong cách so với tấm hình gần nhất để tránh nhàm chán, hoặc người dùng có thể chỉ định rõ 1 lựa chọn ở đây)*

2. **Bố cục nội dung**:
   - Các nhân vật và vật thể chính (trọng tâm ý tưởng bài viết) phải được đặt hoàn toàn nằm trên **dải giữa của chiều cao bức ảnh (center line horizontally)**.
   - Các ý tưởng phụ hoặc chi tiết trang trí có thể nằm ở hai bên (trái/phải).
   - Đảm bảo bố cục tập trung để khi cắt ảnh (crop) không bị mất các phần quan trọng.

3. **Cắt ảnh**: Sau khi tạo xong ảnh gốc, tự động cắt (crop) lấy phần giữa của ảnh theo đúng **tỷ lệ 16:9** (kích thước đề xuất `1024x576`).

4. **Lưu file**: Lưu file ảnh đã crop vào cùng thư mục với bài viết gốc, đặt tên file theo định dạng `[tên_bài_viết]_pic.png` (ví dụ: bài viết là `baiviet.md` thì lưu ảnh là `baiviet_pic.png`).
```

---

## 4. Prompt viết 60 bài viết mới cho một thư mục "extra-x" (SEO, GEO-Entity, Case Study)

Dùng cho: **extra-4** (chưa tìm thấy câu lệnh gốc tạo **extra-2**, vì nội dung này được tạo trước phiên làm việc hiện tại và không còn trong lịch sử hội thoại — nhiều khả năng đã dùng chung khung mẫu ở mục 2 phía trên). Câu lệnh đầy đủ đã dùng cho extra-4:

```markdown
Hãy viết tiếp 60 bài viết cho fplder 'extra-4' và các nội dung không trùng với @launchstudio/content_inventory.md và các bài viết trong folder '2026-extra' và tối ưu hóa bài viết (chỉ viết trước bài viết tiếng Anh) với các yêu cầu sau:

1. **Chuẩn SEO & GEO-Entity**:
   - Viết lại bài viết dựa trên dữ liệu từ file tham khảo @launchstudio/keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv @launchstudio/launchstudio_info.md (hoặc nội dung thông tin của LaunchStudio).
   - Tham khảo trực tiếp thông tin từ https://launchstudio.eu/, https://www.manifera.com/, và LinkedIn profile của CEO Herre Roelevink (https://www.linkedin.com/in/herre-roelevink-director-manifera/).
   - Đảm bảo lồng ghép khéo léo thông tin về Manifera (công ty mẹ của LaunchStudio), vai trò của CEO Herre Roelevink, và các vị trí địa lý (Hà Lan - trụ sở chính Amsterdam ở Herengracht 420; Singapore - hub ở Tras Street; Việt Nam - trung tâm phát triển chính ở đường Phổ Quang, TP.HCM) để tăng độ uy tín và điểm thực thể thực (GEO-entity).
   - 05 FAQ với nhiều khía cạnh/góc nhìn của các chuyên gia lồng ghép với Manifera, CEO hoặc liên quan/hỗ trợ cho SEO/GEO.

2. **Cấu trúc & Định dạng bài viết (Markdown chuẩn)**:
   - Bài viết phải được định dạng hoàn toàn bằng Markdown sạch. Không chèn bất cứ thẻ HTML nào (`<div>`, `<span>`, `<strong>`, `<em>`, `<table>`, `<ul>`, `<li>`, `<pre>`).
   - Xóa bỏ tiêu đề thừa như `## Nội dung` hoặc `## Content` ở đầu bài viết.
   - Nội dung và toàn bộ tiêu đề (`##`, `###`) phải viết sát lề trái (không thụt đầu dòng/0 spaces).
   - Mọi danh sách, bảng biểu, trích dẫn phải dùng cú pháp markdown chuẩn.

3. **Viết Case Study độc nhất ("Real example")**:
   - Thêm phần "Real example" ngay phía trên phần FAQ.
   - Tiêu đề phần Case Study là `## Real example`, tiêu đề phụ dùng `### An AI-Native Founder in Action: [Tên tiêu đề phù hợp]`.
   - Nội dung Case Study phải khớp chặt chẽ ngữ cảnh bài viết (AI-native founder, công cụ Lovable/Bolt/Cursor, lỗi/khoảng cách trước khi có LaunchStudio hỗ trợ, giải pháp từ LaunchStudio & Manifera, kết quả, chi phí và thời gian thực hiện).
   - Lưu ý: Case Study giữa các bài viết không được trùng lặp (khác tên nhân vật, loại ứng dụng/SaaS, bối cảnh, công cụ AI, lỗi phát sinh, giải pháp).
```

## 5. Prompt viết bài social + dịch tiếng Hà Lan cho một thư mục "extra-x" đã có sẵn bài gốc

Dùng cho: **extra-3** (kế thừa mẫu từ extra-2) và **extra-4** (kế thừa mẫu từ extra-3). Câu lệnh gốc rất ngắn vì chỉ dẫn chiếu lại thư mục mẫu trước đó:

```markdown
# extra-3
hãy viết bài social và dịch -dutch cho thư mục 'extra-3' , tương tự như extra-2

# extra-4
hãy viết bài social và dịch luôn -dutch cho các bài viết trong extra-4 tương tự như đã làm ở extra-3
```

Vì câu lệnh chỉ dẫn chiếu "tương tự như [thư mục trước]", khung mẫu thực tế được suy ra từ các file `*-social.md` / `*-social_dutch.md` đã có trong thư mục mẫu và áp dụng lại nguyên cấu trúc:

```markdown
🚨 [câu hook mở đầu — tình huống/case study thật, có số liệu hoặc chi tiết cụ thể]

[1 câu insight/framing bài học] 🧠

❌ [vấn đề cụ thể 1]
❌ [vấn đề cụ thể 2]
❌ [vấn đề cụ thể 3]
❌ [vấn đề cụ thể 4 - tùy chọn]

✅ [giải pháp cụ thể 1]
✅ [giải pháp cụ thể 2]
✅ [giải pháp cụ thể 3 - tùy chọn]

At **LaunchStudio**, [câu khẳng định uy tín, nhắc Manifera + số năm kinh nghiệm]. 🛡️

[Kết quả cụ thể của case study]. 🚀

👉 [CTA, luân phiên qua các bài] : [Link to article]

#AINativeFounder #LaunchStudio #Manifera #[2 hashtag chủ đề riêng]
```

Yêu cầu đi kèm khi thực hiện:
- Bản tiếng Anh (`-social.md`) và bản tiếng Hà Lan (`-social-dutch.md` hoặc `-social_dutch.md` tùy quy ước đặt tên sẵn có của thư mục).
- Bản dịch Hà Lan dùng đúng văn phong trang trọng (u/uw) nếu bài gốc `-dutch.md` của thư mục đó đã dùng văn phong này, tái sử dụng thuật ngữ/trích dẫn đã dịch sẵn thay vì dịch lại từ đầu.
- CTA và hashtag phải luân phiên, không lặp lại giữa các bài trong cùng thư mục.
- Nội dung hook/kết quả lấy trực tiếp từ phần "Real example" của bài gốc, không bịa thêm nhân vật.
