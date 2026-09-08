# Báo Cáo Phân Tích SEO/GEO: onlyaijobs.eu (Lần 3)

**Ngày:** 8 tháng 9, 2026
**Người thực hiện:** Phân tích SEO/GEO tự động (đánh giá từ bên ngoài, black-box)
**Đối tượng:** https://onlyaijobs.eu/
**Loại báo cáo:** Đánh giá lại lần 2 — tham chiếu báo cáo 31/7/2026 và 18/8/2026

---

## Tóm Tắt Điều Hành

Sau **39 ngày** kể từ báo cáo đầu tiên, cấu hình WAF chặn crawler **vẫn nguyên vẹn**: trang chủ, `robots.txt` và `sitemap.xml` đều trả `302` vào `/challenge` với curl trần, với User-Agent Chrome, và với User-Agent Googlebot.

Nhưng lần kiểm tra này phát hiện một điều mà hai báo cáo trước chưa thử: **GPTBot và ClaudeBot đi qua được WAF và nhận HTTP 200 với toàn bộ nội dung**. Nói cách khác, tình trạng hiện tại là một sự **đảo ngược hoàn toàn**:

| Bot | WAF cho qua? | robots.txt cho phép? | Kết quả thực tế |
|---|---|---|---|
| **Googlebot** | ❌ Chặn (302 → /challenge) | ✅ `Allow: /` | Không bao giờ đọc được robots.txt để biết mình được phép |
| **Bingbot** | ❌ Chặn (giả định như Googlebot) | ✅ `Allow: /` | Như trên |
| **GPTBot** | ✅ Cho qua (200) | ❌ `Disallow: /` | Vào được nhưng bị robots.txt bảo đi ra |
| **ClaudeBot** | ✅ Cho qua (200) | ❌ `Disallow: /` | Như trên |

Hai bot mà site *muốn* mời vào thì bị tường lửa chặn; hai bot mà site *bảo không được vào* thì tường lửa lại mở cửa. Không có cấu hình nào trong hai lớp này biết lớp kia đang làm gì.

Nhờ đi qua được bằng UA của GPTBot, báo cáo lần này **lần đầu tiên nhìn thấy nội dung thật của site** — và phát hiện thêm 8 lỗi cấu trúc nghiêm trọng mà hai báo cáo trước không thể đánh giá được vì bị chặn hoàn toàn.

**Kết luận: 🔴 Nghiêm trọng. Ngay cả khi gỡ chặn WAF ngày mai, site vẫn không thể xếp hạng — vì 42/52 việc làm bị canonical loại khỏi chỉ mục, không có `JobPosting` schema, và 4/9 URL trong sitemap trả về vỏ ứng dụng quản trị rỗng.**

---

## Phần A — Tình Trạng Chặn Crawler (không đổi)

### A1. Bằng chứng thu thập hôm nay

```
curl https://onlyaijobs.eu/                → 302 → https://onlyaijobs.eu/challenge
curl https://onlyaijobs.eu/robots.txt      → 302 → https://onlyaijobs.eu/challenge
curl https://onlyaijobs.eu/sitemap.xml     → 302 → https://onlyaijobs.eu/challenge
curl -A "…Googlebot/2.1…"  https://onlyaijobs.eu/   → 302 → /challenge
curl -A "…Chrome/128…"     https://onlyaijobs.eu/   → 302 → /challenge
curl -A "GPTBot/1.0"       https://onlyaijobs.eu/   → 200  (35.650 bytes, nội dung đầy đủ)
curl -A "ClaudeBot/1.0"    https://onlyaijobs.eu/   → 200
```

Trang `/challenge` vẫn mang `<title>Bot Detection</title>` và `<meta name="robots" content="nofollow,noarchive,noindex">` — thứ duy nhất Googlebot từng nhìn thấy trong 39 ngày qua.

### A2. Chứng chỉ TLS (bình thường)

Cấp 9/8/2026, hết hạn 7/11/2026, Let's Encrypt — xác nhận hạ tầng vẫn được duy trì tự động. Đây không phải site chết, mà là site đang chạy và tự khóa cửa với Google.

### A3. Nội dung `robots.txt` (lần đầu đọc được)

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: *
Disallow: /
Sitemap: https://onlyaijobs.eu/index-sitemap.xml
```

**Ba vấn đề trong 8 dòng này:**
1. `Disallow: /` cho `User-agent: *` chặn mọi crawler khác — bao gồm GPTBot, ClaudeBot, PerplexityBot, tức là **toàn bộ lớp khám phá AI**, đúng vào lúc các bot đó là những bot duy nhất qua được WAF.
2. Sitemap khai báo ở đây là `index-sitemap.xml`, nhưng site còn phục vụ một `sitemap.xml` khác với nội dung khác hẳn. Hai tệp không đồng bộ.
3. Toàn bộ tệp này vô nghĩa với Googlebot vì Googlebot không bao giờ tải được nó (bị 302 ở tầng WAF).

---

## Phần B — 8 Phát Hiện Mới (lần đầu đánh giá được nội dung)

### 🔴 B1. Không có `JobPosting` schema — mất toàn bộ cơ hội vào Google Jobs

Toàn site chỉ có 3 khối JSON-LD: `Organization`, `WebSite`, `BreadcrumbList`. **Không có một khối `JobPosting` nào.**

Với một job board, đây là lỗi nghiêm trọng nhất về mặt SEO. `JobPosting` là điều kiện bắt buộc để xuất hiện trong Google Jobs — giao diện tìm việc chiếm phần lớn diện tích màn hình cho mọi truy vấn dạng "AI engineer vacatures". Không có nó, site không cạnh tranh trên bề mặt quan trọng nhất của chính ngành mình.

### 🔴 B2. Không có URL riêng cho từng việc làm

52 việc làm được render trực tiếp trong trang danh sách; không tồn tại `/jobs/<slug>` hay bất kỳ URL chi tiết nào (`/jobs/1` → 404). Hệ quả dây chuyền:
- Không có URL để gắn `JobPosting` schema (B1 không thể sửa nếu không sửa B2 trước)
- Không có gì để index theo từng vị trí tuyển dụng
- Không chia sẻ được một việc làm cụ thể qua link — mất hoàn toàn kênh lan truyền tự nhiên của job board

### 🔴 B3. Phân trang canonical về trang 1 — 42/52 việc làm bị loại khỏi chỉ mục

```
/jobs?page=2  →  <link rel="canonical" href="https://onlyaijobs.eu/jobs">
```

Cả 6 trang phân trang đều tự khai canonical về `/jobs`. Google sẽ chỉ index 10 việc làm ở trang 1; 42 việc còn lại **không tồn tại** với công cụ tìm kiếm. Cộng với B2, tổng số việc làm thực sự có khả năng được tìm thấy là **10/52 (19%)**.

### 🔴 B4. 4/9 URL trong sitemap trả về vỏ ứng dụng quản trị rỗng

| URL (đều nằm trong `sitemap.xml`) | HTTP | Nội dung thực tế |
|---|---|---|
| `/pages/info-for-employers` | 200 | `<title>Admin Portal</title>` — 59 ký tự văn bản: *"Admin Portal You need to enable JavaScript to run this app."* |
| `/pages/info-for-job-seekers` | 200 | Như trên |
| `/pages/about-us` | 200 | Như trên |
| `/pages/add-a-vacancy` | 200 | Như trên |
| `/llms.txt` | 200 | Như trên (đáng lẽ phải là 404 hoặc một tệp llms.txt thật) |
| `/job/list` | 200 | Như trên |

Site đang chủ động nộp cho Google 4 trang rỗng — trong đó có **hai trang quan trọng nhất về mặt thương mại** (trang dành cho nhà tuyển dụng và trang dành cho người tìm việc). Đây là dạng "soft 404" tệ nhất: HTTP 200 nhưng không có nội dung.

> **Ghi chú kỹ thuật**: vỏ HTML được phục vụ ở các URL công khai này là bundle của **Admin Portal**, kèm theo danh sách đầy đủ quyền hệ thống trong `appSettings` và Sentry DSN trỏ về `sentry.manifera.com`. Không phải lỗ hổng bảo mật trực tiếp, nhưng không nên phục vụ ứng dụng quản trị ở URL nội dung công khai.

### 🟡 B5. `BreadcrumbList` trỏ crawler vào chính trang rỗng đó

```json
{"@type":"ListItem","position":2,"name":"Jobs listing - OnlyAIJobs",
 "item":"https://onlyaijobs.eu/job/list"}
```

Breadcrumb khai URL `/job/list` trong khi canonical của trang là `/jobs`. Mà `/job/list` lại chính là một trong các URL trả về vỏ Admin Portal rỗng (B4). Structured data đang dẫn crawler đi sai đường.

### 🔴 B6. `index-sitemap.xml` sai cú pháp

```xml
<sitemapindex>
  <sitemap><loc>https://onlyaijobs.eu/sitemaps/sitemap-1.xml</loc></sitemap>  ✅ đúng
  <sitemap><loc>https://onlyaijobs.eu</loc></sitemap>                          ❌ đây là trang, không phải sitemap
  <sitemap><loc>https://onlyaijobs.eu/add-a-vacancy</loc></sitemap>            ❌ như trên
  <sitemap><loc>https://onlyaijobs.eu/jobs</loc></sitemap>                     ❌ như trên
```

Phần tử `<sitemap>` trong sitemap index bắt buộc phải trỏ tới **tệp sitemap**, không phải trang nội dung. Google sẽ báo lỗi phân tích cho các mục này. Ngoài ra `/add-a-vacancy` (không có tiền tố `/pages/`) khác với URL trong `sitemap.xml` — hai tệp sitemap khai hai bộ URL khác nhau.

### 🟡 B7. hreflang không đối xứng — bản tiếng Hà Lan sẽ bị bỏ qua

Site **có** bản tiếng Hà Lan thật tại `/nl` (menu đã dịch: Werkzoekenden, Werkgevers, Vacatures, Over ons), nhưng:

| Trang | Khai báo hreflang |
|---|---|
| `/nl` | `en` → `/`, `nl` → `/nl`, `x-default` → `/` ✅ đầy đủ |
| `/` (EN) | `en` → `/` (**khai hai lần**), `x-default` → `/`, **thiếu hoàn toàn `nl`** ❌ |

hreflang bắt buộc phải khai báo hai chiều. Vì trang EN không thừa nhận trang NL, Google sẽ **bỏ qua toàn bộ cụm hreflang này**. Ngoài ra, không một URL `/nl` nào có mặt trong bất kỳ sitemap nào.

### 🟡 B8. Blog rỗng + 6/11 danh mục không có việc làm

- `/blog` trả về: *"📚 No posts published yet."* — không có một bài viết nào.
- Bộ lọc quảng cáo 11 danh mục (AI Product, Computer Vision, Development, Ethics & Governance, Generative AI, Infrastructure, Machine Learning, Quality Control, Research, Robotics Engineer, Security and Safety) nhưng thực tế chỉ **5 danh mục có việc làm**. Development + Machine Learning chiếm ~40/52 tin.

---

## Phần C — Bức Tranh Nội Dung & Cung Ứng (lần đầu quan sát được)

| Chỉ số | Giá trị đo được hôm nay |
|---|---|
| Tổng số việc làm | **52** (6 trang × 10, trang cuối 2 tin) |
| Số công ty | ~40 công ty khác nhau |
| Độ tươi | **100% tin đăng đều hiển thị "Posted 1 month ago"** — không có tin mới trong ít nhất 30 ngày |
| Loại hình | 100% Full-time |
| Địa lý | Chủ yếu Hà Lan (Ede, Capelle aan den IJssel, Groningen, Eindhoven…); **3/52 tin là việc làm tại Mỹ** (đăng qua Lensa, một job aggregator Mỹ) |
| Công ty tiêu biểu | Accenture, Cegeka Nederland, Sendcloud, Mollie, Heijmans, Rexel Nederland, VINCI Energies, AMCS, Boltrics, Winparts, Hoppinger |
| Bài blog | **0** |
| Trang nội dung có thật | 3 (`/`, `/jobs`, `/blog`) — mọi trang `/pages/*` đều rỗng |

### C1. Mô hình kinh doanh (trích từ site)

> *"To post a vacancy on OnlyAIJobs, simply send an email with a link to the job listing on your company's website to info@onlyaijobs.eu. One vacancy on OnlyAIJobs is free."*

Đăng tin bằng **email thủ công**, tin đầu tiên **miễn phí**, không có trang giá, không có luồng tự phục vụ, không có cổng đăng nhập cho nhà tuyển dụng ở phía công khai.

### C2. Định vị (trích từ trang chủ)

> *"OnlyAIJobs was created based on an insight from various studies. This showed that many vacancy seekers from **Noord-Brabant** leave for the **Randstad** area, not because they necessarily want to work there, but because they often do not know which interesting companies are in their region."*
> *"OnlyAIJobs is a vacancy platform that displays vacancies at the exact **address level**."*

Đây là định vị **địa phương, theo khoảng cách** — sinh ra từ một vấn đề chảy máu nhân tài vùng Noord-Brabant. Nhưng thẻ meta của site lại nói: *"connects AI talents with top European companies"*, và tên miền là `.eu`.

**Hai câu chuyện này mâu thuẫn nhau.** Không thể vừa là "job board AI toàn châu Âu" vừa là "tìm việc gần nhà bạn ở Brabant" — hai định vị đó nhắm hai tập từ khóa khác nhau, hai tập đối thủ khác nhau, và cần hai chiến lược nội dung khác nhau. Đây là quyết định chiến lược quan trọng nhất cần chốt trước mọi việc SEO/quảng cáo (xem [`implementation_plan.md`](./implementation_plan.md) §9).

---

## Phần D — Khuyến Nghị Theo Thứ Tự Ưu Tiên

### P0 — Chặn dòng máu (tuần này)

| # | Việc | Ghi chú |
|---|---|---|
| 1 | **Thêm allow-list cho Googlebot/Bingbot trong BunkerWeb**, xác minh bằng reverse-DNS chứ không chỉ theo User-Agent | Đã được khuyến nghị 3 lần liên tiếp (31/7, 18/8, hôm nay) |
| 2 | Sau khi gỡ, kiểm chứng bằng công cụ URL Inspection trong Search Console | Không tin vào curl — phải xem Google thực sự thấy gì |
| 3 | Sửa `robots.txt`: bỏ `Disallow: /` cho `*`, hoặc chí ít cho phép GPTBot/ClaudeBot/PerplexityBot | Hiện đang tự chặn đúng những bot duy nhất vào được |
| 4 | Ngừng phục vụ Admin Portal ở các URL công khai (`/pages/*`, `/llms.txt`, `/job/list`) | Trả 404 hoặc nội dung thật |

### P1 — Không có những thứ này thì gỡ chặn cũng vô ích (2–4 tuần)

| # | Việc |
|---|---|
| 5 | **Tạo URL riêng cho từng việc làm** (`/jobs/<company>-<title>-<city>`) — điều kiện tiên quyết cho mọi việc còn lại |
| 6 | **Gắn `JobPosting` schema** đầy đủ cho từng URL đó (`title`, `hiringOrganization`, `jobLocation`, `datePosted`, `validThrough`, `employmentType`, `baseSalary` nếu có) |
| 7 | Bỏ canonical ép về trang 1 trên các trang phân trang; dùng `rel=next/prev` hoặc để mỗi trang tự canonical |
| 8 | Viết nội dung thật cho `/pages/info-for-employers`, `/pages/info-for-job-seekers`, `/pages/about-us` |
| 9 | Sửa `index-sitemap.xml` cho đúng cú pháp; hợp nhất hai tệp sitemap; đưa URL `/nl` và URL từng việc làm vào sitemap |
| 10 | Bổ sung `hreflang="nl"` vào trang EN để cụm hreflang đối xứng |

### P2 — Xây dựng động lực (1–3 tháng)

| # | Việc |
|---|---|
| 11 | Chốt định vị: "AI jobs châu Âu" hay "việc làm AI gần bạn tại NL"? (Phần C2) |
| 12 | Giải bài toán nguồn cung: 52 tin, tất cả đều 1 tháng tuổi. Một job board không có tin mới sẽ chết cả với người dùng lẫn với Google |
| 13 | Ẩn các danh mục rỗng, hoặc chủ động lấp tin cho chúng |
| 14 | Khởi động blog (hiện 0 bài) theo kế hoạch tại [`seo_geo_plan_onlyaijobs.md`](./seo_geo_plan_onlyaijobs.md) |
| 15 | Viết `llms.txt` thật — hiện là URL trả về vỏ admin |

---

## Phụ Lục: Bằng Chứng Thô (8/9/2026)

```
# WAF
curl -o /dev/null -w "%{http_code} %{redirect_url}" https://onlyaijobs.eu/
  → 302 https://onlyaijobs.eu/challenge
curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" …/
  → 302 https://onlyaijobs.eu/challenge
curl -A "Mozilla/5.0 (Macintosh…Chrome/128.0 Safari/537.36)" …/
  → 302 https://onlyaijobs.eu/challenge
curl -A "GPTBot/1.0" …/          → 200, 35.650 bytes
curl -A "ClaudeBot/1.0" …/       → 200

# Nội dung (qua UA GPTBot)
/                     200  · server-rendered · 2.352 ký tự văn bản · title "Only AI Jobs"
/jobs                 200  · server-rendered · 10.921 ký tự · 10 tin/trang · 6 trang · 52 tin
/jobs?page=2..6       200  · canonical → https://onlyaijobs.eu/jobs
/blog                 200  · "No posts published yet."
/nl                   200  · lang="nl" · hreflang en+nl+x-default đầy đủ
/pages/about-us       200  · vỏ Admin Portal · 59 ký tự văn bản
/pages/info-for-employers    200 · vỏ Admin Portal
/pages/info-for-job-seekers  200 · vỏ Admin Portal
/pages/add-a-vacancy         200 · vỏ Admin Portal
/llms.txt             200  · vỏ Admin Portal
/job/list             200  · vỏ Admin Portal (nhưng được BreadcrumbList trỏ tới)
/zzz-does-not-exist   404  · "404 | Not Found" (404 thật vẫn hoạt động đúng)

# JSON-LD toàn site: Organization, WebSite, BreadcrumbList — 0 khối JobPosting
# TLS: Let's Encrypt, notBefore 9/8/2026, notAfter 7/11/2026
```

---

*Báo cáo thực hiện từ bên ngoài, không có quyền truy cập Search Console, analytics hay CMS của onlyaijobs.eu. Nội dung site đọc được nhờ User-Agent GPTBot đi qua được WAF — bản thân điều đó đã là một phát hiện.*
