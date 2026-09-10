# 🎫 Phase 0 — Ticket Kỹ Thuật Cho Đội Dev (Manifera)

> Nguồn: [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md) · [`implementation_plan.md`](./implementation_plan.md) §9
> Mục đích: chuyển audit thành danh sách việc có thể giao thẳng cho dev, theo thứ tự ưu tiên. Không cần đọc audit gốc để hiểu phải sửa gì.
> **Người phụ trách hạ tầng (WAF/BunkerWeb) cần được chỉ định trước khi làm bất kỳ ticket nào ở đây** — đã khuyến nghị 3 lần trong 39 ngày mà chưa ai nhận.

---

## Ticket 1 — 🔴 Gỡ chặn WAF cho Googlebot/Bingbot

**Hiện trạng**: `curl` trần, Chrome UA, và Googlebot UA đều bị WAF trả `302 → /challenge`. Chỉ GPTBot và ClaudeBot UA đi qua được (200). Tức là công cụ tìm kiếm duy nhất quan trọng cho traffic thương mại (Google) bị khóa hoàn toàn 39 ngày qua.

**Cần sửa**: whitelist Googlebot + Bingbot (theo IP range xác thực, không chỉ theo User-Agent — UA giả mạo được) trong luật WAF/BunkerWeb, để các bot này nhận `200` thay vì `302 → /challenge` trên mọi URL công khai.

**Acceptance criteria**:
```
curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://onlyaijobs.eu/ → 200
curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://onlyaijobs.eu/robots.txt → 200
curl -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://onlyaijobs.eu/sitemap.xml → 200
```
Xác nhận thêm bằng Search Console → URL Inspection → "Live Test" sau khi deploy.

**Phụ thuộc**: không có — có thể làm ngay, độc lập với các ticket khác. **Đây là ticket khẩn nhất.**

---

## Ticket 2 — 🔴 Sửa `robots.txt`

**Hiện trạng** (đọc được qua GPTBot UA):
```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: *
Disallow: /
Sitemap: https://onlyaijobs.eu/index-sitemap.xml
```
`Disallow: /` cho `User-agent: *` chặn GPTBot, ClaudeBot, PerplexityBot — chính là nhóm bot AI duy nhất hiện qua được WAF.

**Cần sửa** — thay bằng:
```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://onlyaijobs.eu/sitemap.xml
```
*(Chọn một tệp sitemap chuẩn — xem Ticket 7 — thay vì khai `index-sitemap.xml`.)*

**Acceptance criteria**: `Disallow: /` không còn xuất hiện cho `User-agent: *`; `Sitemap:` trỏ đúng vào tệp sitemap thật đang dùng.

**Phụ thuộc**: nên làm cùng lúc với Ticket 1 (vô nghĩa nếu WAF vẫn chặn Googlebot trước khi đọc được file này).

---

## Ticket 3 — 🔴 Ngừng phục vụ Admin Portal ở URL công khai

**Hiện trạng**: các URL sau trả về `200` nhưng nội dung thực là bundle JS của **Admin Portal** nội bộ (`<title>Admin Portal</title>`, kèm `appSettings` lộ quyền hệ thống và Sentry DSN nội bộ trỏ `sentry.manifera.com`):
- `/pages/about-us`
- `/pages/info-for-employers`
- `/pages/info-for-job-seekers`
- `/pages/add-a-vacancy`
- `/llms.txt`
- `/job/list`

Hai trong số này (`info-for-employers`, `add-a-vacancy`) là **trang thương mại quan trọng nhất của site** — nơi mọi traffic quảng cáo nhắm nhà tuyển dụng sẽ đổ vào.

**Cần sửa**:
1. Route các URL `/pages/*` công khai về đúng nội dung trang tĩnh (nội dung đã soạn sẵn ở [`phase0_static_pages_content.md`](./phase0_static_pages_content.md)), không phải bundle Admin Portal.
2. `/job/list` và `/llms.txt`: nếu không dùng cho public, trả `404`; nếu `/llms.txt` được giữ, thay bằng nội dung `llms.txt` thật (bản nháp cũng ở file trên).
3. Rà lại toàn bộ routing để chắc chắn Admin Portal chỉ phục vụ ở subdomain/path nội bộ, không lẫn vào path công khai — đây là rò rỉ thông tin cấu hình hệ thống, nên ưu tiên bảo mật chứ không chỉ SEO.

**Acceptance criteria**: `curl` 6 URL trên → không còn `<title>Admin Portal</title>`; `/pages/*` trả nội dung thật; `/job/list`, `/llms.txt` trả 404 hoặc nội dung hợp lệ.

**Phụ thuộc**: cần nội dung trang tĩnh xong trước khi route (đã có, xem file liên kết).

---

## Ticket 4 — 🔴 Tạo URL riêng cho từng tin tuyển dụng

**Hiện trạng**: không có trang chi tiết việc làm — tin chỉ mở rộng inline trong danh sách `/jobs`, không có URL/slug riêng. Không có gì để gắn `JobPosting` schema (chặn Ticket 5) và không có gì để index theo từng vị trí.

**Cần sửa**: mỗi tin có URL riêng, dạng `/jobs/<slug>` (slug từ tên vị trí + công ty), trả về trang HTML tĩnh/SSR có đủ nội dung tin (không chỉ client-render), để crawler đọc được không cần chạy JS.

**Acceptance criteria**: `curl` một URL tin bất kỳ trả về HTML chứa tiêu đề, công ty, mô tả — không phải shell rỗng cần JS.

**Phụ thuộc**: chặn Ticket 5 (JobPosting schema) và một phần Ticket 7 (sitemap cần liệt kê các URL này).

---

## Ticket 5 — 🔴 Gắn `JobPosting` schema

**Hiện trạng**: toàn site chỉ có 3 khối JSON-LD (`Organization`, `WebSite`, `BreadcrumbList`). Không có `JobPosting` → không đủ điều kiện xuất hiện trong Google Jobs, bề mặt quan trọng nhất cho truy vấn "AI engineer vacatures".

**Cần sửa**: gắn JSON-LD `JobPosting` vào từng trang chi tiết tin (Ticket 4), tối thiểu các field bắt buộc của Google:
```json
{
  "@context": "https://schema.org/",
  "@type": "JobPosting",
  "title": "…",
  "description": "…",
  "identifier": {
    "@type": "PropertyValue",
    "name": "OnlyAIJobs",
    "value": "<job-id>"
  },
  "datePosted": "2026-09-08",
  "validThrough": "2026-10-08",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "…",
    "sameAs": "…"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "…",
      "addressRegion": "…",
      "addressCountry": "NL"
    }
  }
}
```
`baseSalary` nếu có dữ liệu; nếu không, bỏ trường này (không bịa số).

**Acceptance criteria**: Google Rich Results Test pass cho `JobPosting` trên ≥1 URL mẫu; Search Console → "Enhancements → Job Postings" ghi nhận sau reindex.

**Phụ thuộc**: cần Ticket 4 xong trước (cần URL riêng để gắn schema vào).

---

## Ticket 6 — 🔴 Sửa canonical phân trang `/jobs`

**Hiện trạng**: `/jobs?page=2` đến `page=6` đều tự khai `<link rel="canonical" href="https://onlyaijobs.eu/jobs">`. Google chỉ index 10 tin ở trang 1; 42 tin còn lại vô hình. Cộng dồn với Ticket 4/5, tỷ lệ tin có thể được tìm thấy hiện là 10/52 (19%).

**Cần sửa**: mỗi trang phân trang tự canonical về chính nó (`/jobs?page=2` canonical → `/jobs?page=2`), không phải luôn về `/jobs`. Cân nhắc thêm `rel="next"`/`rel="prev"` (không bắt buộc với Google nhưng vô hại).

**Acceptance criteria**: view-source từng trang phân trang → canonical khớp URL hiện tại.

**Phụ thuộc**: không có — độc lập, có thể làm song song với các ticket khác.

---

## Ticket 7 — 🟡 Hợp nhất & sửa sitemap

**Hiện trạng**: hai tệp sitemap khác nhau đang tồn tại (`sitemap.xml` và `index-sitemap.xml`), khai hai bộ URL khác nhau. `index-sitemap.xml` là sitemap index nhưng 2/3 phần tử `<sitemap>` trỏ vào **trang nội dung** (`https://onlyaijobs.eu`, `/add-a-vacancy`) thay vì **tệp sitemap** — sai cú pháp chuẩn sitemap index, Google sẽ báo lỗi parse. `/add-a-vacancy` (không tiền tố `/pages/`) còn là URL khác với bản có `/pages/` trong `sitemap.xml`.

**Cần sửa**:
1. Chọn **một** sitemap làm chuẩn (khuyến nghị: sitemap index đúng chuẩn trỏ tới các file `sitemap-*.xml` con).
2. Mỗi phần tử `<sitemap>` trong index phải trỏ tới file `.xml`, không phải trang HTML.
3. Đưa vào sitemap: URL `/nl/*`, URL từng tin (`/jobs/<slug>` từ Ticket 4), 4 trang tĩnh đã sửa (Ticket 3).
4. Xóa/301 tệp sitemap không dùng để không còn hai nguồn khai URL khác nhau.

**Acceptance criteria**: Search Console → Sitemaps → submit lại, không còn lỗi parse; số URL "Discovered" tăng đúng với số URL thật.

**Phụ thuộc**: nên làm sau Ticket 4 (cần URL tin đã tồn tại để liệt kê).

---

## Ticket 8 — 🟡 Sửa hreflang đối xứng

**Hiện trạng**: trang `/nl` khai `hreflang` đầy đủ (en + nl + x-default), nhưng trang EN gốc **không** khai `hreflang="nl"` trỏ ngược lại. hreflang bắt buộc hai chiều — vì bất đối xứng, Google sẽ bỏ qua toàn bộ cụm hreflang này. Ngoài ra không URL `/nl` nào có trong sitemap.

**Cần sửa**: thêm `<link rel="alternate" hreflang="nl" href="https://onlyaijobs.eu/nl/...">` (và `x-default`) vào mọi trang EN tương ứng; đưa URL `/nl/*` vào sitemap (gộp vào Ticket 7).

**Acceptance criteria**: Search Console → International Targeting không còn báo lỗi hreflang; cặp EN/NL trỏ hai chiều đúng.

**Phụ thuộc**: gộp chung đợt deploy với Ticket 7.

---

## Ticket 9 — 🟡 Cài GA4 + Search Console

**Hiện trạng**: không phát hiện GA4/GTM trong HTML; không có Search Console (audit phải làm black-box, không quyền truy cập analytics).

**Cần sửa**: cài GA4, đăng ký Search Console (verify bằng DNS hoặc HTML tag), thiết lập tối thiểu 5 sự kiện chuyển đổi:
1. Click "Apply"/xem chi tiết tin (job seeker engagement)
2. Submit form đăng tin miễn phí (khi Ticket "form 2 trường" xong — xem `implementation_plan.md` §4.3)
3. Click email `info@onlyaijobs.eu` từ trang nhà tuyển dụng
4. Lọc theo thành phố/danh mục (đo mức độ dùng USP "theo bán kính")
5. Chuyển đổi ngôn ngữ EN↔NL (đo mức độ dùng nội dung NL)

**Acceptance criteria**: GA4 Realtime ghi nhận sự kiện khi thao tác thử; Search Console xác minh quyền sở hữu thành công.

**Phụ thuộc**: không có — độc lập, làm song song được.

---

## Thứ tự triển khai đề xuất

```
Tuần 1:  Ticket 1 (WAF) + Ticket 2 (robots.txt)  ─┬─ phải cùng lúc, vô nghĩa nếu tách rời
         Ticket 9 (GA4/Search Console)             ─┘  độc lập, làm song song
         Ticket 6 (canonical phân trang)            ── độc lập, làm song song

Tuần 2:  Ticket 3 (ngừng phục vụ Admin Portal ở URL công khai)
         → cần nội dung tĩnh xong trước (phase0_static_pages_content.md — đã có)

Tuần 3–4: Ticket 4 (URL riêng cho từng tin) → Ticket 5 (JobPosting schema)
          Ticket 7 (hợp nhất sitemap) → Ticket 8 (hreflang đối xứng)
```

---

## Quyết định cần chốt song song (không phải việc của dev)

**Định vị: "AI jobs châu Âu" hay "Việc làm AI theo vùng tại Hà Lan"?**
Dữ liệu hiện có nghiêng hẳn về phương án B (vùng NL): 49/52 tin tại Hà Lan, câu chuyện gốc (Brabant → Randstad) chỉ có ý nghĩa ở cấp vùng, và từ khóa "ai jobs europe" phải đấu trực tiếp với LinkedIn/Indeed — một trận không thể thắng với 52 tin. Khuyến nghị: **chốt phương án B**, vì nó khớp với nguồn cung thật, câu chuyện gốc thật, và độ khó từ khóa thấp hơn nhiều. Quyết định này cần được xác nhận bởi người phụ trách sản phẩm/thương hiệu — nó quyết định `meta description`, schema `Organization`, và toàn bộ bộ từ khóa SEO/Ads đi kèm (xem `implementation_plan.md` §3).

---

*Soạn 10/09/2026 dựa trên `seo-geo-audit-onlyaijobs-eu-2026-09-08.md`. Không có quyền truy cập CMS/hạ tầng thật — mọi acceptance criteria dùng lệnh `curl`/công cụ công khai (Search Console, Rich Results Test) để đội dev tự xác minh sau khi deploy.*
