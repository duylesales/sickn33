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

---

## 6. Prompt tạo ảnh minh họa bài viết chuẩn phong cách Hình 47 (UI & Backend Enterprise Fusion - Tối ưu 16:9)

> **Đặc trưng phong cách Hình 47:**
>
> - **Chủ đề**: Hợp tác công nghệ cao (Human + AI Robot + Cloud Infra + Creative UI).
> - **Bố cục dải giữa thu gọn (Tight Center Line)**: Nhân vật và hạ tầng kỹ thuật tập trung gọn ở giữa (từ trục Y 25% đến 75%), tạo khoảng thở phía trên và dưới để crop 16:9 (`1024x576`) không bao giờ bị cắt đầu/chân hay chạm mép.
> - **Tuyệt đối KHÔNG chữ & số (Zero Text, Zero Numbers)**: Dùng 100% biểu tượng trực quan (khiên an ninh xanh, ổ khóa vàng, khối database hình trụ, đám mây, tia sét, panel wireframe giao diện, màn hình kính cong HUD).
> - **Phối màu & Ánh sáng**: Phong cách Dribbble Corporate Tech với ánh sáng studio hiện đại, đổ màu gradient sinh động (Magenta-Violet, Electric Cyan, Royal Cobalt Blue, Mint Emerald, Solar Gold).

### Cú pháp Prompt tiếng Anh chuẩn (dùng cho công cụ tạo ảnh):

```text
Modern flat-ish vector illustration, dribbble corporate tech style, vibrant gradients, strictly no text and no numbers, pure visual storytelling. A sleek technology and software engineering collaboration scene with tightly centered composition along the horizontal middle line: in the center, an illuminated holographic gateway and transformation engine where colorful frontend UI wireframe mockups seamlessly fuse with robust backend enterprise server racks, database cylinders, and glowing green security shields; closely on the left, a professional tech founder holding a sleek UI prototype tablet; closely on the right, a senior enterprise software architect and an agile collaborative AI robot engineer operating powerful cloud infrastructure with verified green checkmarks. Compact central composition with ample top and bottom breathing room, bright clean minimalist studio background with soft spotlights, vibrant magenta-violet, electric cyan, royal cobalt blue, and solar gold gradients, sleek vector art, zero text, zero letters, zero numbers.
```

### Mẫu câu lệnh tiếng Việt để yêu cầu trợ lý AI thực hiện:

```markdown
@[đường_dẫn_tới_bài_viết.md] Hãy đọc nội dung file này và tạo cho mình 1 hình ảnh minh họa bài viết chuẩn theo phong cách Hình 47 với các yêu cầu sau:

1. **Phong cách & Thị giác (Style Hình 47)**:
   - "Modern flat-ish vector illustration", "dribbble corporate tech style", phối màu gradient sống động (Magenta/Tím, Xanh Cyan, Xanh Cobalt, Xanh lá Mint, Vàng Amber) trên nền studio trắng sáng có ánh đèn chiếu nhẹ.
   - **Tuyệt đối KHÔNG có chữ và số (Zero text, Zero numbers)**: Thể hiện ý tưởng 100% bằng hình ảnh ẩn dụ (bảng wireframe giao diện, máy chủ, ổ khóa, khiên an ninh, robot AI, đám mây).
2. **Bố cục thu gọn trung tâm (Tight Center Composition)**:
   - Tất cả nhân vật (founder, kỹ sư, robot AI) và thiết bị trọng tâm đặt gọn trên trục ngang dải giữa.
   - Giữ khoảng thở rộng rãi phía trên và phía dưới để khi cắt tỷ lệ 16:9 không bị mất chi tiết.
3. **Cắt ảnh & Lưu file**:
   - Tự động cắt (crop) lấy dải giữa chuẩn **tỷ lệ 16:9** (`1024x576`).
   - Lưu vào cùng thư mục với bài viết gốc dưới tên `[tên_bài_viết]_pic.png`.
```
