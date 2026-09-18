# 📋 Phase 0 — Báo Cáo Trạng Thái Ticket (Kiểm tra live 11/09/2026)

**Ngày kiểm tra:** 11/09/2026 · **Phương pháp:** kiểm tra từ bên ngoài bằng `curl`, không có quyền truy cập máy chủ/GSC
**Đối chiếu:** [`phase0_dev_tickets.md`](./phase0_dev_tickets.md) (lập 08/09/2026) · [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md)
**Lưu ý về phạm vi kiểm tra:** WAF chặn mọi User-Agent trình duyệt, nên mọi phép thử dưới đây chạy bằng UA `GPTBot/1.0` (UA duy nhất đi qua được). Kết quả phản ánh đúng những gì **crawler** nhìn thấy — cũng chính là điều quan trọng với SEO.

---

## 🔢 Bảng Tổng Hợp

| # | Ticket | Mức | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 1 | Gỡ chặn WAF cho Googlebot/Bingbot | 🔴 | ❌ **Chưa làm** | **Ngày thứ 42** kể từ audit đầu tiên |
| 2 | Sửa `robots.txt` | 🔴 | ❌ **Chưa làm** | Nội dung không đổi một ký tự |
| 3 | Ngừng phục vụ Admin Portal ở URL công khai | 🔴 | ❌ **Chưa làm** | 6/6 URL vẫn trả vỏ Admin Portal |
| 4 | Tạo URL riêng cho từng tin | 🔴 | ⚠️ **Làm dở — đang hỏng** | URL đã sinh và đã link, nhưng **96/96 đều trả 404** |
| 5 | Gắn `JobPosting` schema | 🔴 | ❌ **Chưa làm** | Bị chặn bởi Ticket 4 |
| 6 | Sửa canonical phân trang | 🔴 | ❌ **Chưa làm** | Trang 2–10 vẫn canonical về `/jobs` |
| 7 | Hợp nhất & sửa sitemap | 🟡 | ⚠️ **Làm một phần** | Đã có sitemap tin (96 URL) ✅ · index-sitemap vẫn sai cú pháp ❌ |
| 8 | Sửa hreflang đối xứng | 🟡 | ❌ **Chưa làm** | Trang EN vẫn khai `en` hai lần, thiếu `nl` |
| 9 | Cài GA4 + Search Console | 🟡 | ⚠️ **Làm một phần** | Đã có GTM `GTM-KTJ8LF7D` ✅ · cấu hình GA4 bên trong GTM và xác minh GSC không kiểm tra được từ ngoài |

**Điểm số: 0/9 hoàn thành · 3/9 làm một phần · 6/9 chưa động tới.**

---

## ✅ Tin Tốt Trước

Hai tiến triển thật, đáng ghi nhận:

**Nguồn cung tăng 85%.** Số tin đang hiển thị đã đi từ **52 → 96** (10 trang phân trang, trang cuối 6 tin). Trang 1 cho thấy 4/10 tin được đăng **1 ngày trước** — lần đầu tiên kể từ khi theo dõi, site có tin mới. Đây là chỉ số sống còn quan trọng nhất của một job board và nó đang đi đúng hướng.

**Hạ tầng cho URL từng tin đã được dựng.** Trang danh sách nay phát ra link dạng `/jobs/10549-ai-devops-engineer`, và `/sitemaps/sitemap-1.xml` đã liệt kê đủ **96 URL tin**. Phần sinh route và sinh sitemap đã xong.

---

## 🔴 Lỗi Nghiêm Trọng Mới: 96 URL Tin Đều Trả 404

Đây là phát hiện quan trọng nhất của lần kiểm tra này, và nó **mới xuất hiện** — ngày 08/09 chưa có lỗi này vì chưa có URL nào cả.

```
# Link do chính trang /jobs phát ra:
https://onlyaijobs.eu/jobs/10549-ai-devops-engineer        → 404
https://onlyaijobs.eu/jobs/10551-ai-solutions-architect    → 404
https://onlyaijobs.eu/jobs/10690-ai-engineer               → 404
https://onlyaijobs.eu/jobs/10702-ai-portfolio-architect    → 404

# URL lấy trực tiếp từ /sitemaps/sitemap-1.xml:
https://onlyaijobs.eu/jobs/10493-data-engineer             → 404
https://onlyaijobs.eu/jobs/10495-senior-data-engineer      → 404
https://onlyaijobs.eu/jobs/10496-senior-data-engineer      → 404
https://onlyaijobs.eu/jobs/10511-data-ai-strategy-...      → 404
https://onlyaijobs.eu/jobs/10518-data-engineer             → 404
```

Thử với cả `GPTBot/1.0` và `ClaudeBot/1.0` — kết quả giống hệt. Trang `/jobs` vẫn trả 200 bình thường với cùng UA, nên **đây không phải do WAF** mà là lỗi route/render của chính ứng dụng.

### Vì sao lỗi này tệ hơn là chưa làm gì

| | Trước 08/09 | Hiện nay |
|---|---|---|
| Link nội bộ | Không có link tin | **96 link nội bộ gãy** trên trang quan trọng nhất |
| Sitemap | 9 URL tĩnh | **96 URL 404 được chủ động nộp cho Google** |
| Đánh giá của Google | Không có gì để đánh giá | Sitemap toàn URL chết = tín hiệu chất lượng site kém |

Nộp một sitemap mà 100% URL trả 404 là một trong số ít thứ có thể làm tình hình **xấu đi** so với việc không có sitemap. Cần hoặc sửa route, hoặc tạm gỡ 96 URL đó khỏi sitemap cho tới khi trang chi tiết chạy được.

### ⚠️ Một khả năng cần đội dev xác nhận

Vì WAF chặn mọi UA trình duyệt, tôi **không thể kiểm tra các URL này bằng trình duyệt thật**. Có khả năng trang chi tiết render bình thường cho người dùng đã qua `/challenge`, và chỉ 404 với các UA bot. Nếu đúng vậy thì lỗi nằm ở tầng khác — nhưng **kết luận về SEO không đổi**: Googlebot sẽ không bao giờ qua được challenge, nên với công cụ tìm kiếm, 96 URL này là 404 dù nguyên nhân là gì.

---

## 📄 Chi Tiết Từng Ticket

### Ticket 1 — WAF ❌ Chưa làm (ngày thứ 42)
```
curl -A "…Googlebot/2.1…"  https://onlyaijobs.eu/  → 302 → /challenge
curl -A "…bingbot/2.0…"    https://onlyaijobs.eu/  → 302 → /challenge
curl -A "…Chrome/128…"     https://onlyaijobs.eu/  → 302 → /challenge
curl -A "GPTBot/1.0"       https://onlyaijobs.eu/  → 200
```
Không có allow-list nào được thêm. Đây vẫn là ticket chặn toàn bộ mọi thứ khác.

### Ticket 2 — robots.txt ❌ Chưa làm
Nội dung hiện tại y hệt ngày 08/09: `Allow: /` cho Googlebot và Bingbot (hai bot đang bị WAF chặn), `Disallow: /` cho `User-agent: *` (chặn đúng các bot AI đang là bot duy nhất vào được).

### Ticket 3 — Admin Portal ở URL công khai ❌ Chưa làm
Cả 6 URL vẫn trả `<title>Admin Portal</title>`:
`/pages/about-us` · `/pages/info-for-employers` · `/pages/info-for-job-seekers` · `/pages/add-a-vacancy` · `/llms.txt` · `/job/list`

Nội dung thay thế cho 4 trang này đã viết sẵn tại [`phase0_static_pages_content.md`](./phase0_static_pages_content.md) — chỉ còn chờ đưa lên.

Ngoài ra phát hiện thêm hai URL cũng trả vỏ Admin Portal: `/job/1` và `/vacancy/1`.

### Ticket 4 — URL từng tin ⚠️ Làm dở, đang hỏng
Xem mục 🔴 ở trên.

### Ticket 5 — `JobPosting` schema ❌ Chưa làm
Schema trên `/jobs` hiện chỉ có `Organization`, `WebSite`, `BreadcrumbList`. Không có khối `JobPosting` nào. Không thể làm ticket này cho tới khi Ticket 4 chạy được, vì `JobPosting` phải nằm trên URL riêng của từng tin.

### Ticket 6 — Canonical phân trang ❌ Chưa làm
```
/jobs?page=1 → canonical https://onlyaijobs.eu/jobs
/jobs?page=2 → canonical https://onlyaijobs.eu/jobs
/jobs?page=3 → canonical https://onlyaijobs.eu/jobs
```
Với 96 tin trải trên 10 trang, hiện **86/96 tin bị canonical loại khỏi chỉ mục**. Tỷ lệ này tệ hơn ngày 08/09 (khi đó 42/52) vì số tin tăng mà canonical không đổi.

### Ticket 7 — Sitemap ⚠️ Làm một phần
| Hạng mục | Trạng thái |
|---|---|
| `/sitemaps/sitemap-1.xml` với 96 URL tin | ✅ Đã có |
| `/sitemap.xml` | ❌ Vẫn là tệp tĩnh 9 URL cũ, không có tin nào |
| `/index-sitemap.xml` | ❌ Vẫn sai cú pháp — phần tử `<sitemap>` trỏ tới trang (`https://onlyaijobs.eu`, `/add-a-vacancy`, `/jobs`) thay vì tệp sitemap |
| URL `/nl` trong sitemap | ❌ Vẫn không có |
| 96 URL trong sitemap có hoạt động không | 🔴 **Không — tất cả 404** |

### Ticket 8 — hreflang ❌ Chưa làm
Trang chủ EN vẫn khai:
```html
<link rel="alternate" hreflang="en" href="https://onlyaijobs.eu" />
<link rel="alternate" hreflang="x-default" href="https://onlyaijobs.eu" />
<link rel="alternate" hreflang="en" href="https://onlyaijobs.eu" />   <!-- trùng lặp -->
```
Vẫn thiếu hoàn toàn dòng `nl`, nên cụm hreflang không đối xứng và Google sẽ bỏ qua.

### Ticket 9 — Đo lường ⚠️ Làm một phần
Đã phát hiện **Google Tag Manager `GTM-KTJ8LF7D`** trên trang chủ — trước đây không có. Không thể xác minh từ bên ngoài: GA4 có được cấu hình bên trong GTM chưa, 5 sự kiện chuyển đổi đã định nghĩa chưa, và Search Console đã xác minh sở hữu chưa. **Cần đội dev xác nhận 3 điểm này.**

---

## 🎯 Ba Việc Cần Làm Ngay, Theo Thứ Tự

1. **Sửa route trang chi tiết tin, hoặc tạm gỡ 96 URL khỏi sitemap.** Đây là việc gấp nhất vì nó đang chủ động gửi tín hiệu xấu cho Google. Nếu route cần thêm thời gian, hãy gỡ `sitemaps/sitemap-1.xml` khỏi sitemap index trước, rồi đưa lại khi trang chạy.
2. **Gỡ chặn WAF (Ticket 1) + sửa robots.txt (Ticket 2).** Hai ticket này đi cùng nhau, tổng công sức ước tính dưới một ngày, và chúng mở khóa toàn bộ phần còn lại.
3. **Bỏ canonical ép về trang 1 (Ticket 6).** Một dòng code, giải phóng 86 tin đang bị loại khỏi chỉ mục.

Sau ba việc đó mới đến `JobPosting` schema (Ticket 5) — vốn là thứ đưa OnlyAIJobs vào Google Jobs và là mục tiêu cuối cùng của cả Phase 0.

---

## 📎 Phụ Lục: Lệnh Tái Lập Toàn Bộ Kiểm Tra

```bash
UA="GPTBot/1.0"

# T1 — WAF
for ua in "Googlebot/2.1" "bingbot/2.0" "Chrome/128.0" "GPTBot/1.0"; do
  curl -s -o /dev/null -w "$ua: %{http_code} %{redirect_url}\n" -A "$ua" https://onlyaijobs.eu/
done

# T2 — robots.txt
curl -s -A "$UA" https://onlyaijobs.eu/robots.txt

# T3 — vỏ Admin Portal
for p in /pages/about-us /pages/info-for-employers /pages/info-for-job-seekers \
         /pages/add-a-vacancy /llms.txt /job/list; do
  echo -n "$p "; curl -s -A "$UA" "https://onlyaijobs.eu$p" | grep -oE '<title>[^<]*</title>'
done

# T4 — URL từng tin
curl -s -A "$UA" https://onlyaijobs.eu/jobs \
  | grep -oE 'https://onlyaijobs\.eu/jobs/[0-9]+-[a-z0-9-]+' | sort -u | head -5 \
  | while read u; do echo -n "$u "; curl -s -o /dev/null -w "%{http_code}\n" -A "$UA" "$u"; done

# T5 — schema
curl -s -A "$UA" https://onlyaijobs.eu/jobs | grep -o '"@type": *"[A-Za-z]*"' | sort | uniq -c

# T6 — canonical phân trang
for p in 1 2 3; do
  echo -n "page $p: "
  curl -s -A "$UA" "https://onlyaijobs.eu/jobs?page=$p" | grep -oE '<link rel="canonical"[^>]*>'
done

# T7 — sitemap
curl -s -A "$UA" https://onlyaijobs.eu/index-sitemap.xml | head -20
curl -s -A "$UA" https://onlyaijobs.eu/sitemaps/sitemap-1.xml | grep -c '<loc>'

# T8 — hreflang
curl -s -A "$UA" https://onlyaijobs.eu/ | grep -oE '<link rel="alternate"[^>]*>'

# T9 — đo lường
curl -s -A "$UA" https://onlyaijobs.eu/ | grep -oE 'GTM-[A-Z0-9]+|G-[A-Z0-9]+' | sort -u
```

---

*Báo cáo lập từ bên ngoài ngày 11/09/2026, không có quyền truy cập máy chủ, Search Console hay analytics của onlyaijobs.eu.*
