# Báo Cáo Phân Tích SEO/GEO: onlyaijobs.eu

**Ngày:** 31 tháng 7, 2026
**Người thực hiện:** Phân tích SEO/GEO tự động (đánh giá từ bên ngoài, black-box)
**Đối tượng:** https://onlyaijobs.eu/

---

## Tóm Tắt Điều Hành

onlyaijobs.eu hiện đang **vô hình trước các công cụ tìm kiếm, các AI answer engine, và cả với công cụ phân tích trong báo cáo này**. Mọi URL được kiểm tra trên tên miền — trang chủ, `/robots.txt`, `/sitemap.xml`, `/llms.txt`, và `/favicon.ico` — đều bị chặn bởi một **thử thách bot bằng JavaScript proof-of-work của BunkerWeb** trước khi bất kỳ nội dung thật nào được trả về. Kiểm tra chỉ mục tìm kiếm (`site:onlyaijobs.eu`) trả về 0 trang được index, và các tìm kiếm theo tên thương hiệu trên toàn bộ internet cũng không tìm thấy bất kỳ đề cập nào đến website này (LinkedIn, Product Hunt, báo chí, diễn đàn). Đây không phải là vấn đề về thứ hạng hay chất lượng nội dung; đây là một **"điểm mù" về khả năng thu thập dữ liệu (crawlability blackout)** nằm ở tầng trên của mọi yếu tố SEO/GEO khác. Dù có tối ưu on-page tốt đến đâu cũng sẽ vô nghĩa cho đến khi vấn đề này được khắc phục, vì Google, Bing, và các crawler của LLM (GPTBot, ClaudeBot, PerplexityBot, v.v.) đều không thể vượt qua trang thử thách để đọc dù chỉ một câu nội dung thật.

Chính vì lý do đó, báo cáo này **không thể đánh giá SEO on-page** (title, heading, độ sâu nội dung, schema markup) hay **mức độ sẵn sàng GEO thực sự** (structured data, tín hiệu E-E-A-T) thông qua quan sát trực tiếp — toàn bộ tầng nội dung này hiện không thể tiếp cận được bởi các công cụ tự động, và đây tự nó chính là phát hiện quan trọng nhất. Mọi nội dung bên dưới đều dựa trên bằng chứng thực tế: phản hồi HTTP thô, bản ghi DNS/TLS, và xác minh qua tìm kiếm bên ngoài.

**Kết luận tổng thể: 🔴 Nghiêm trọng — website hiện không thể được index trong cấu hình hiện tại.**

---

## Phương Pháp & Giới Hạn

Báo cáo này hoàn toàn dựa vào các công cụ bên ngoài, không cần xác thực — không có quyền truy cập vào Google Search Console, công cụ phân tích (analytics), hay bảng quản trị của website. Các phương pháp sử dụng:

1. Gửi request HTTP trực tiếp (`curl`) đến trang chủ và các file quan trọng dành cho crawler, kiểm tra mã trạng thái, header, và nội dung phản hồi.
2. Công cụ fetch tự động chuyển đổi trang thành markdown (tương tự cách nhiều công cụ duyệt web dựa trên LLM hoạt động).
3. Phân giải DNS (`dig`) và kiểm tra chứng chỉ TLS (`openssl s_client`) để có bối cảnh về hạ tầng.
4. Tra cứu `whois` để có bối cảnh đăng ký tên miền (bị giới hạn bởi chính sách riêng tư của TLD `.eu` — EURid không công khai thông tin người đăng ký).
5. Xác minh qua tìm kiếm web (toán tử `site:` và tìm kiếm theo tên thương hiệu) để kiểm tra tình trạng lập chỉ mục và các đề cập bên ngoài.
6. Tra cứu Wayback Machine / archive.org để kiểm tra có phiên bản lưu trữ lịch sử nào của website hay không.

**Giới hạn quan trọng:** vì website chặn truy cập tự động một cách đồng loạt, báo cáo này không thể mô tả những gì một người dùng thật nhìn thấy trên trình duyệt thật (nơi thử thách JS được giải sau vài giây và trang thật được tải). Các phát hiện dưới đây mô tả trải nghiệm thực tế của **mọi crawler và bot không phải trình duyệt** — bao gồm cả các crawler tìm kiếm và AI mà báo cáo này vốn nhằm mục đích tối ưu cho chúng.

---

## Phát Hiện Nghiêm Trọng #1: Toàn Bộ Crawler Bị Chặn Hoàn Toàn Bởi Thử Thách BunkerWeb

Mọi URL được kiểm tra đều trả về redirect vào, hoặc nội dung của, một trang xen giữa (interstitial) phát hiện bot:

| URL | Kết quả |
|---|---|
| `https://onlyaijobs.eu/` | `302` → `/challenge`, sau đó `200` trả về trang "Bot Detection" bằng JS proof-of-work (không phải nội dung website) |
| `https://onlyaijobs.eu/robots.txt` | `302 Found` (bị redirect vào luồng thử thách thay vì trả về file) |
| `https://onlyaijobs.eu/sitemap.xml` | `302 Found` (tương tự) |
| `https://onlyaijobs.eu/llms.txt` | `302 Found` (tương tự) |
| `https://onlyaijobs.eu/favicon.ico` | `302 Found` (tương tự) |

Trang thử thách này được phục vụ bởi **BunkerWeb** (một WAF/reverse-proxy mã nguồn mở), và mã HTML của nó thể hiện rõ mục đích:

- `<title>Bot Detection</title>`
- `<meta name="description" content="Please wait while we check if you are a Human">`
- `<meta name="robots" content="nofollow,noarchive,noindex">`
- Một form ẩn tính toán một nonce SHA-256 proof-of-work ở phía client bằng JavaScript và POST đến `/challenge` trước khi trang thật được mở khóa
- Footer: "Protected by BunkerWeb"

**Tại sao đây là vấn đề nghiêm trọng, không phải chỉ là tiểu tiết:**

- **Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, và hầu hết mọi crawler khác đều không thực thi loại JavaScript proof-of-work phía client này giống như trình duyệt thật**, và ngay cả khi một crawler *có thể* chạy JS (Googlebot có thể, ở một đợt quét thứ hai bị trễ), các thử thách kiểu proof-of-work/CAPTCHA vốn được thiết kế đặc biệt để lọc bỏ các client không phải con người, không tương tác — chính xác là bản chất của mọi crawler tìm kiếm và AI.
- `robots.txt` và `sitemap.xml` theo giao thức robots exclusion protocol phải được phục vụ **vô điều kiện, không redirect hay thử thách**. Các công cụ tìm kiếm không thể tải `robots.txt` một cách sạch sẽ sẽ hoặc mặc định hiểu theo hướng bảo thủ nhất (chặn toàn bộ), hoặc đơn giản là hạ thấp mức độ tin cậy/ngân sách crawl (crawl budget) dành cho tên miền.
- Chính thẻ `<meta name="robots" content="nofollow,noarchive,noindex">` trên trang thử thách có nghĩa là ngay cả trong trường hợp hiếm hoi một request của crawler được coi là "thành công," thứ được index chính là trang xen giữa với `noindex` — nói cách khác, **website đang chủ động yêu cầu công cụ tìm kiếm không index trang duy nhất mà nó thực sự nhìn thấy được.**
- `llms.txt` — quy ước mới nổi để báo hiệu cho các crawler AI/LLM biết nội dung nào cần thu thập — cũng bị chặn sau cùng một bức tường này, nên ngay cả một AI crawler tuân thủ đúng quy ước này cũng không thể đọc được nó.

Chỉ riêng một cấu hình sai này (bộ luật crawler/bot của WAF không có allow-list cho các bot tìm kiếm và AI hợp lệ đã biết, và không loại trừ `robots.txt`/`sitemap.xml`/`llms.txt` khỏi thử thách) đã đủ để giải thích mọi triệu chứng khác được phát hiện trong báo cáo này.

---

## Phát Hiện Nghiêm Trọng #2: Không Có Sự Hiện Diện Nào Trong Chỉ Mục Tìm Kiếm

Truy vấn `site:onlyaijobs.eu` cùng nhiều tìm kiếm theo tên thương hiệu (`"OnlyAIJobs" AI jobs board`, `onlyaijobs.eu LinkedIn`, `onlyaijobs.eu Product Hunt`) đều trả về **0 kết quả từ chính tên miền này**. Tất cả kết quả trả về đều là các job board bên thứ ba không liên quan (aijobs.ai, aijobs.com, theaijobboard.com, jobforagent.com, các cổng việc làm của EU như EURES) — đối thủ cạnh tranh và các trang liên quan, chứ không phải onlyaijobs.eu.

Điều này hoàn toàn nhất quán với, và được giải thích trực tiếp bởi, Phát hiện #1: nếu crawler không thể vượt qua thử thách bot, thì sẽ không có gì để index. Dựa trên bằng chứng hiện có, đây không phải là một hình phạt (penalty), một manual action, hay vấn đề chất lượng nội dung — mà giống như một website chưa từng được crawl thành công.

**Kiểm tra Wayback Machine:** Các nỗ lực kiểm tra archive.org để tìm snapshot lịch sử đều không có kết quả rõ ràng (liên tục bị timeout/lỗi kết nối từ môi trường thực hiện báo cáo này). Đây không phải là bằng chứng mạnh theo hướng nào, nhưng kết hợp với phát hiện về việc không được index, hiện không có bằng chứng xác nhận nào cho thấy website từng được bất kỳ bên thứ ba nào crawl và lưu trữ.

---

## Bối Cảnh Hạ Tầng & Kỹ Thuật

Các phát hiện không liên quan đến bức tường chặn bot, thu thập qua kiểm tra DNS/TLS:

| Mục | Giá trị |
|---|---|
| Bản ghi A | `136.243.57.57` (dải IP Hetzner) |
| Subdomain `www` | CNAME trỏ về apex, phân giải cùng IP |
| Nameserver | `ns1/ns2/ns3.digitalocean.com` |
| Chứng chỉ TLS | Let's Encrypt, cấp ngày **10/6/2026**, hết hạn **8/9/2026** (chứng chỉ chuẩn 90 ngày) |
| Đơn vị quản lý TLD | `.eu`, đăng ký qua EURid (thông tin người đăng ký được bảo vệ riêng tư theo mặc định của EURid — không thể tra cứu qua WHOIS công khai) |
| HTTP/3 | Được công bố qua header `alt-svc: h3` |
| Header bảo mật quan sát được trên phản hồi thử thách | HSTS, `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, `referrer-policy: no-referrer-when-downgrade`, CSP dựa trên nonce |

Ngày cấp chứng chỉ tháng 6/2026 cho thấy triển khai hiện tại khá gần đây (một chứng chỉ Let's Encrypt 90 ngày được cấp lại không chứng minh được ngày ra mắt thật sự của website, nhưng phù hợp với phát hiện "chưa từng được index" — đây có thể đơn giản là một dự án mới hoặc mới được relaunch mà crawler chưa từng tiếp cận được). Mức độ chỉn chu của các header bảo mật (HSTS, CSP, nosniff, frame-options) khá tốt, cho thấy một hạ tầng được xây dựng khá bài bản — vấn đề chặn crawler có vẻ là do cấu hình mặc định "bot-fight-mode" quá gắt của WAF, chứ không phải do thiếu chăm sóc tổng thể.

---

## SEO On-Page — Không Thể Đánh Giá

Vì mọi request tự động (kể cả công cụ của chính báo cáo này) đều nhận được trang thử thách thay vì nội dung thật, các mục sau đây không thể đánh giá trực tiếp và cần được kiểm tra thủ công qua trình duyệt thật hoặc Google Search Console:

- Title tag / meta description trên các trang thật
- Cấu trúc heading (phân cấp H1/H2)
- Độ sâu và chất lượng nội dung trên các trang tin tuyển dụng, giới thiệu/liên hệ
- Cấu trúc internal linking
- Structured data (schema `JobPosting` là loại schema có đòn bẩy cao nhất cho một website việc làm, và là yếu tố then chốt để có Google Jobs rich results — không thể xác nhận có hay không)
- Alt text hình ảnh, Core Web Vitals, khả năng hiển thị trên di động

**Sự thiếu vắng dữ liệu này tự nó chính là phát hiện quan trọng nhất**: một cuộc phân tích SEO/GEO — dù được thực hiện bởi một chuyên gia tư vấn, một công cụ tự động, chính hệ thống của Google, hay một trợ lý AI mà một người tìm việc hỏi "tìm giúp tôi việc làm AI ở châu Âu" — đều gặp phải chính xác cùng một bức tường. Nếu công cụ của báo cáo này không nhìn thấy nội dung, thì các hệ thống có nhiệm vụ đưa nội dung đó đến người dùng cũng không thể.

---

## Đánh Giá GEO (Khả Năng Được AI/LLM Phát Hiện)

Mức độ sẵn sàng GEO phụ thuộc vào việc nội dung vừa có thể được crawl, vừa được cấu trúc để các AI answer engine (ChatGPT browsing, Perplexity, Claude, Google AI Overviews) có thể trích xuất. Các phát hiện:

- **`llms.txt` tồn tại như một route nhưng không thể truy cập được** — nó redirect `302` vào cùng thử thách, nên ngay cả các AI crawler chủ động tìm kiếm theo quy ước này cũng bị chặn.
- **Không phát hiện allow-list cho AI crawler nào đã biết.** BunkerWeb (và các WAF nói chung) thường yêu cầu một allow-list bot rõ ràng (theo user-agent và/hoặc dải IP/reverse-DNS đã xác minh) cho Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, và CCBot. Không có hành vi quan sát được nào cho thấy điều này đã được cấu hình — mọi request, kể cả `curl` thông thường, đều gặp chính xác bức tường mà một scraper độc hại sẽ gặp.
- **Không có sự hiện diện thương hiệu nào để làm điểm tựa cho câu trả lời GEO.** GEO cũng phụ thuộc rất nhiều vào các tín hiệu thương hiệu bên ngoài website (được trích dẫn, liên kết, hoặc thảo luận ở nơi khác) để LLM biết đến thương hiệu ngay cả khi không crawl trực tiếp website. Không tìm thấy bất kỳ đề cập nào như vậy trong suốt quá trình phân tích.

---

## Khuyến Nghị Theo Thứ Tự Ưu Tiên

**P0 — Khắc phục ngay lập tức (đang chặn mọi thứ khác):**
1. Trong cấu hình BunkerWeb, thêm allow-list ngoại lệ cho user-agent/dải IP của các crawler tìm kiếm và AI đã được xác minh (tối thiểu gồm Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, CCBot) để chúng bỏ qua hoàn toàn thử thách JS/proof-of-work.
2. Loại trừ rõ ràng `/robots.txt`, `/sitemap.xml`, `/llms.txt`, và `/favicon.ico` khỏi bộ luật thử thách bot — các file này phải luôn trả về `200` với nội dung thật, vô điều kiện, bất kể client là ai.
3. Gỡ bỏ hoặc giới hạn phạm vi của thẻ meta `noindex,nofollow,noarchive` chỉ áp dụng cho route thử thách/xen giữa, không được rò rỉ sang các trang nội dung thật.

**P1 — Sau khi có thể crawl được, cần xác minh:**
4. Xác nhận `robots.txt` không tự nó chặn việc crawl một khi đã có thể truy cập được.
5. Gửi `sitemap.xml` qua Google Search Console và Bing Webmaster Tools sau khi xác nhận có thể truy cập, và yêu cầu index.
6. Thêm structured data `JobPosting` (schema.org) cho mọi trang tin tuyển dụng — đây là hành động SEO có tác động lớn nhất cho một website việc làm, giúp đủ điều kiện hiển thị Google Jobs rich results.
7. Xác minh nội dung `llms.txt` thực sự hữu ích một khi có thể truy cập (nên trỏ AI crawler đến các trang/nội dung quan trọng, chứ không chỉ tồn tại như một file trống).

**P2 — Xây dựng khả năng được phát hiện sau khi gỡ bức tường chặn:**
8. Xây dựng sự hiện diện cơ bản bên ngoài website (trang công ty trên LinkedIn, listing trên Product Hunt hoặc directory, một số backlink) — hiện tại không có bất kỳ dấu ấn bên ngoài nào để làm điểm tựa cho cả tìm kiếm truyền thống lẫn trích dẫn từ AI answer engine.
9. Chạy lại một cuộc audit on-page đầy đủ (title, heading, độ sâu nội dung, internal linking, Core Web Vitals) một khi nội dung thật có thể được các công cụ tự động truy cập — báo cáo này chưa thể đánh giá được tầng nào trong số đó.

---

## Phụ Lục: Tổng Hợp Bằng Chứng Thô

- `curl -D - https://onlyaijobs.eu/ -L` → `302` đến `/challenge`, sau đó `200` trả về trang xen giữa "Bot Detection" của BunkerWeb (đã lưu lại cục bộ trong quá trình phân tích để tham chiếu).
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/robots.txt` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/sitemap.xml` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/llms.txt` → `302`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/favicon.ico` → `302`
- WebFetch (công cụ fetch chuyển đổi markdown) trên trang chủ → `HTTP 429 Too Many Requests` (phù hợp với việc bot-mitigation đang hoạt động/giới hạn tốc độ, không phải sự cố ngẫu nhiên)
- Tìm kiếm `site:onlyaijobs.eu` → 0 kết quả từ tên miền
- Tìm kiếm `"OnlyAIJobs" AI jobs board` → 0 kết quả từ tên miền; chỉ có các job board đối thủ
- Tìm kiếm `onlyaijobs.eu LinkedIn` → 0 kết quả
- Tìm kiếm `onlyaijobs.eu Product Hunt` → 0 kết quả
- `dig onlyaijobs.eu A` → `136.243.57.57`; NS trên `digitalocean.com`
- Chứng chỉ TLS → Let's Encrypt, cấp ngày 10/6/2026, hết hạn 8/9/2026
- `whois onlyaijobs.eu` → thông tin người đăng ký được EURid bảo vệ riêng tư (tiêu chuẩn cho tên miền `.eu`)
- Tra cứu archive.org / Wayback Machine → không có kết quả rõ ràng (timeout/lỗi kết nối từ môi trường thực hiện báo cáo; không tìm thấy snapshot lịch sử nào được xác nhận)

---

*Báo cáo này được thực hiện từ bên ngoài và tự động, không có quyền truy cập vào công cụ phân tích, Search Console, hay CMS của chủ sở hữu website. Mọi phát hiện phản ánh đúng những gì các crawler và công cụ công khai, không xác thực trải nghiệm khi truy cập onlyaijobs.eu — chính là trải nghiệm hiện tại của Google, Bing, và các crawler AI.*
