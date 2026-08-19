# Báo Cáo Phân Tích SEO/GEO: onlyaijobs.eu (Cập Nhật)

**Ngày:** 18 tháng 8, 2026
**Người thực hiện:** Phân tích SEO/GEO tự động (đánh giá từ bên ngoài, black-box)
**Đối tượng:** https://onlyaijobs.eu/
**Loại báo cáo:** Đánh giá lại (follow-up) — tham chiếu báo cáo trước ngày 31/7/2026 (`seo-geo-audit-onlyaijobs-eu-vie.md`)

---

## Tóm Tắt Điều Hành

**Sau 18 ngày kể từ báo cáo trước, vấn đề nghiêm trọng nhất — website chặn hoàn toàn mọi crawler bằng thử thách bot BunkerWeb — vẫn chưa được khắc phục.** Toàn bộ các URL trọng yếu (trang chủ, `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/favicon.ico`) vẫn trả về redirect `302` vào `/challenge`, kể cả khi giả lập User-Agent của **Googlebot** — một phép thử mới trong lần kiểm tra này, và kết quả xác nhận rằng ngay cả bot tìm kiếm được khai báo rõ ràng cũng không có allow-list nào để bỏ qua thử thách. Kiểm tra chỉ mục (`site:onlyaijobs.eu`) tiếp tục trả về 0 kết quả, và không có bất kỳ đề cập thương hiệu nào trên internet.

Điểm khác biệt duy nhất so với báo cáo trước: chứng chỉ TLS đã được gia hạn tự động (cấp lại ngày **9/8/2026**, hết hạn **7/11/2026**), xác nhận hạ tầng vẫn đang hoạt động và được duy trì — đây **không phải** một website đã ngừng vận hành, mà là một website đang chạy nhưng tự khóa cửa với chính các crawler mà nó cần để được tìm thấy.

**Kết luận tổng thể: 🔴 Nghiêm trọng, không đổi — website vẫn không thể được index. Đây hiện là vấn đề đã tồn tại ít nhất 18 ngày mà chưa có dấu hiệu được xử lý.**

---

## Điều Gì Thay Đổi Kể Từ Báo Cáo 31/7/2026?

| Hạng mục | 31/7/2026 | 18/8/2026 | Thay đổi? |
|---|---|---|---|
| `/` (trang chủ) | `302` → `/challenge` | `302` → `/challenge` | Không |
| `/robots.txt` | `302` (redirect vào challenge) | `302` (redirect vào challenge) | Không |
| `/sitemap.xml` | `302` (redirect vào challenge) | `302` (redirect vào challenge) | Không |
| `/llms.txt` | `302` (redirect vào challenge) | `302` (redirect vào challenge) | Không |
| `/favicon.ico` | `302` (redirect vào challenge) | `302` (redirect vào challenge) | Không |
| Thẻ `<meta name="robots">` trên trang challenge | `nofollow,noarchive,noindex` | `nofollow,noarchive,noindex` | Không |
| Kết quả `site:onlyaijobs.eu` | 0 kết quả | 0 kết quả | Không |
| Đề cập thương hiệu trên web | Không tìm thấy | Không tìm thấy | Không |
| Chứng chỉ TLS | Cấp 10/6/2026, hết hạn 8/9/2026 | Cấp 9/8/2026, hết hạn 7/11/2026 | **Đã gia hạn tự động** (bình thường, xác nhận site vẫn "sống") |
| Allow-list cho Googlebot UA | Chưa kiểm tra trong báo cáo trước | **Đã kiểm tra lần này: vẫn bị chặn** | Bằng chứng mới, xác nhận rõ hơn mức độ nghiêm trọng |

**Kết luận từ bảng trên:** đây không phải một sự cố tạm thời hay một lần bị flag nhầm. Suốt hơn hai tuần rưỡi, cấu hình WAF chặn crawler vẫn y nguyên. Việc chứng chỉ TLS tự gia hạn đúng chu kỳ cho thấy có khả năng **chưa từng có ai chủ động vào kiểm tra hoặc sửa cấu hình BunkerWeb** kể từ lần audit trước — hạ tầng "tự chạy" nhưng không ai theo dõi phần crawlability.

---

## Bằng Chứng Mới: Ngay Cả Googlebot Cũng Bị Chặn

Đây là phép thử **chưa từng thực hiện** trong báo cáo trước, được bổ sung lần này để trả lời trực tiếp câu hỏi "liệu WAF có allow-list riêng cho các bot tìm kiếm đã biết không?":

```
curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://onlyaijobs.eu/
→ 302 redirect_to=https://onlyaijobs.eu/challenge

curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://onlyaijobs.eu/robots.txt
→ 302 redirect_to=https://onlyaijobs.eu/challenge
```

**Ý nghĩa:** giả lập User-Agent của Googlebot thật ra rất dễ làm giả (bất kỳ ai cũng có thể tự khai báo UA này), nên một WAF được cấu hình đúng **không nên** tin tưởng chỉ dựa vào UA — nó cần xác minh qua reverse-DNS hoặc dải IP đã công bố của Google. Nhưng điều đáng nói ở đây là: **kết quả `302` giống hệt như một request `curl` trần trụi không giả UA gì cả**, chứng tỏ hiện tại **không có bất kỳ cơ chế allow-list nào** — kể cả cơ chế yếu (chỉ theo UA) cũng chưa được bật. Nói cách khác, đội ngũ vận hành site chưa thực hiện bước cấu hình cơ bản nhất trong danh sách khuyến nghị P0 của báo cáo trước.

---

## Xác Nhận Lại Các Phát Hiện Từ Báo Cáo Trước (Không Đổi)

Các phần dưới đây được xác nhận lại bằng bằng chứng mới thu thập hôm nay, nội dung không đổi so với báo cáo 31/7:

### 1. Trang thử thách BunkerWeb vẫn là thứ duy nhất mọi crawler nhìn thấy
- `<title>Bot Detection</title>`
- `<meta name="robots" content="nofollow,noarchive,noindex">`
- Form ẩn tính SHA-256 proof-of-work bằng JavaScript, POST đến `/challenge`
- Footer: "This website is protected with BunkerWeb"

### 2. Không có sự hiện diện nào trong chỉ mục tìm kiếm
- `site:onlyaijobs.eu` → 0 kết quả từ chính tên miền
- Tìm kiếm theo tên thương hiệu (`"OnlyAIJobs"`, `onlyaijobs.eu`) → không có kết quả nào từ website; công cụ tìm kiếm trả về các job board đối thủ không liên quan (aijobs.ai, aijobs.com, eudatajobs.com, ai-jobs.global, v.v.)
- WebFetch (công cụ fetch/markdown) → `HTTP 429 Too Many Requests`, nhất quán với cơ chế chống bot đang hoạt động

### 3. SEO on-page và mức độ sẵn sàng GEO — vẫn không thể đánh giá
Toàn bộ các mục sau vẫn **không thể quan sát trực tiếp** vì lý do y hệt báo cáo trước — mọi request tự động chỉ nhận được trang challenge:
- Title tag / meta description thật của các trang tin tuyển dụng
- Cấu trúc heading, độ sâu nội dung
- Structured data `JobPosting` (yếu tố quan trọng nhất cho Google Jobs rich results ở một job board)
- Alt text hình ảnh, Core Web Vitals, internal linking

---

## Đánh Giá GEO — Không Đổi, Rủi Ro Tăng Theo Thời Gian

Mức độ sẵn sàng GEO (khả năng được ChatGPT browsing, Perplexity, Claude, Google AI Overviews trích dẫn) tiếp tục ở mức **0**, vì hai lý do không đổi:

1. `llms.txt` tồn tại như một route nhưng vẫn bị chặn bởi cùng bức tường — ngay cả AI crawler tuân thủ đúng quy ước này cũng không đọc được.
2. Không có tín hiệu thương hiệu bên ngoài (LinkedIn, Product Hunt, báo chí, backlink) để LLM có thể "biết" đến OnlyAIJobs mà không cần crawl trực tiếp.

**Điểm mới đáng lo ngại:** thời gian càng kéo dài mà crawler AI không thể tiếp cận, thì "cửa sổ cơ hội" để được các mô hình LLM ghi nhận sớm trong một ngách (niche) còn tương đối mới — "AI jobs board tại châu Âu" — càng bị đối thủ (aijobs.ai, eudatajobs.com, ai-jobs.global — đều xuất hiện rõ ràng trong kết quả tìm kiếm hôm nay) chiếm lĩnh trước. Đây là chi phí cơ hội tăng dần theo từng ngày bức tường chặn bot chưa được gỡ, không chỉ là một khoản nợ kỹ thuật tĩnh.

---

## Khuyến Nghị — Không Đổi Về Nội Dung, Nhưng Cấp Bách Hơn

Danh sách khuyến nghị P0/P1/P2 từ báo cáo 31/7 **vẫn giữ nguyên giá trị và vẫn chưa được thực hiện**. Nhắc lại đúng 3 việc P0 vì đây là thứ duy nhất cần làm trước để mọi thứ khác có ý nghĩa:

**P0 — Cần làm ngay (đã trễ 18 ngày):**
1. Thêm allow-list trong cấu hình BunkerWeb cho các bot đã xác minh qua reverse-DNS/IP chính thức (Googlebot, Bingbot, GPTBot, ClaudeBot, PerplexityBot, CCBot) — **hiện tại xác nhận: chưa có, kể cả ở mức UA cơ bản.**
2. Loại trừ `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/favicon.ico` khỏi luật thử thách — các file này phải trả `200` với nội dung thật, vô điều kiện.
3. Đảm bảo thẻ `noindex,nofollow,noarchive` chỉ nằm trên route `/challenge`, không rò rỉ sang nội dung thật.

Xem lại báo cáo `seo-geo-audit-onlyaijobs-eu-vie.md` (31/7/2026) để có đầy đủ danh sách P1/P2.

---

## Phụ Lục: Bằng Chứng Thô Thu Thập Hôm Nay (18/8/2026)

- `curl -D - https://onlyaijobs.eu/ -L` (UA trình duyệt thật) → `302` → `/challenge` → `200` trang "Bot Detection" (đã lưu HTML đầy đủ, xác nhận nội dung y hệt báo cáo trước)
- `curl -A "Googlebot/2.1..." https://onlyaijobs.eu/` → `302` → `/challenge` (**phép thử mới**)
- `curl -A "Googlebot/2.1..." https://onlyaijobs.eu/robots.txt` → `302` → `/challenge` (**phép thử mới**)
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/robots.txt` → `200` nhưng effective URL là `/challenge` (tức đã bị redirect và nội dung trả về là trang challenge, không phải robots.txt thật)
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/sitemap.xml` → tương tự, effective URL `/challenge`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/llms.txt` → tương tự, effective URL `/challenge`
- `curl -o /dev/null -w "%{http_code}" https://onlyaijobs.eu/favicon.ico` → tương tự, effective URL `/challenge`
- WebFetch trên trang chủ → `HTTP 429 Too Many Requests`
- Tìm kiếm `site:onlyaijobs.eu` → 0 kết quả từ tên miền
- Tìm kiếm `"onlyaijobs.eu" OR "OnlyAIJobs" AI jobs board Europe` → 0 kết quả từ tên miền; chỉ có đối thủ (aijobs.ai, aijobs.com, eudatajobs.com, ai-jobs.global, workingnomads.com)
- `dig onlyaijobs.eu A` → `136.243.57.57` (không đổi)
- `dig onlyaijobs.eu NS` → `ns1/ns2/ns3.digitalocean.com` (không đổi)
- Chứng chỉ TLS → Let's Encrypt, cấp **9/8/2026**, hết hạn **7/11/2026** (đã gia hạn tự động một lần kể từ báo cáo trước, xác nhận hạ tầng vẫn hoạt động bình thường ở tầng dưới WAF)

---

*Báo cáo này là bản cập nhật/đánh giá lại, thực hiện từ bên ngoài và tự động, không có quyền truy cập Google Search Console hay CMS của chủ sở hữu. So với báo cáo gốc ngày 31/7/2026, tình trạng crawlability không có bất kỳ cải thiện nào. Khuyến nghị: xử lý báo cáo này như một lời nhắc khẩn — mỗi ngày trì hoãn là một ngày website tiếp tục vô hình với Google, Bing, và mọi AI answer engine.*
