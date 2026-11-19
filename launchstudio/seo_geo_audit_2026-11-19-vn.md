# LaunchStudio (launchstudio.eu) - Audit SEO & GEO, ngày 19/11/2026

**Bản tiếng Việt của:** `seo_geo_audit_2026-11-19.md`. Bản tiếng Anh là bản gốc; nếu hai bản khác nhau, lấy bản tiếng Anh làm chuẩn.

**Thay thế:** `seo_geo_audit_2026-07-31.md`. File cũ vẫn được giữ để tra lịch sử; mục 2 theo dõi từng lỗi của audit đó.

**Phạm vi:**

- SEO kỹ thuật
- On-page
- Dữ liệu có cấu trúc (schema)
- Nội dung và độ phủ chủ đề
- Đa ngôn ngữ (NL/EN)
- GEO: khả năng hiện diện trong ChatGPT, Perplexity, Claude, Gemini và Google AI Overviews

**Phương pháp:**

- Crawl HTTP thô (`curl`) các file `robots.txt`, `sitemap_index.xml` cùng 5 sitemap con, `llms.txt` và `llms-full.txt`.
- Phân tích 21 URL trong `page-sitemap.xml` và 8 bài mới nhất: title, meta, canonical, hreflang, OG, heading, ảnh, JSON-LD, số từ.
- Kiểm tra phần head của toàn bộ 320 URL bài viết: hreflang, title/description bị trùng, thẻ OG.
- Kiểm tra quyền truy cập với 25 user-agent crawler.
- Đo độ giống nhau về nội dung giữa các cặp trang nghi trùng.
- Dữ liệu quản trị WordPress qua MCP: plugin, số bài, điểm Yoast của 40 bài sửa gần nhất.
- Tìm kiếm web các nhắc đến thương hiệu trên trang bên thứ ba.

**Giới hạn:**

- Không có dữ liệu Search Console và GA4.
- API PageSpeed Insights đã hết quota trong ngày nên không có số Core Web Vitals. Phần hiệu năng dùng TTFB, dung lượng HTML và số tài nguyên làm chỉ số ước lượng.
- Crawl đọc HTML thô, không phải DOM sau khi chạy JavaScript.

---

## 1. Tóm tắt

Từ tháng 7, LaunchStudio đã làm rất nhiều về nội dung:

- Số bài đăng tăng từ 71 lên 160 cặp NL/EN (318 bài đã xuất bản).
- Thân bài giờ dài 2.300-2.800 từ.
- Tác giả hiển thị tên thật.
- `llms.txt` đã liệt kê đủ mọi bài.
- Footer đã có link sang Manifera.

Tuy vậy, phần lớn lỗi kỹ thuật và lỗi thực thể (entity) từ tháng 7 vẫn chưa sửa. Lần crawl này còn phát hiện một vấn đề mới, quan trọng hơn tất cả:

1. **🔴 Server chặn ChatGPT và Claude (mới, nghiêm trọng).** `launchstudio.eu` trả **HTTP 403** cho `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `anthropic-ai`, `CCBot`, `Bytespider` và `cohere-ai`, kể cả với `robots.txt` và `llms.txt`. Bản thân `robots.txt` cho phép tất cả, nên việc chặn nằm ở lớp server/WAF.
   - Manifera chạy trên cùng server (136.243.57.57) mà **không** bị chặn.
   - Hiện nay, khi người dùng nhờ ChatGPT mở hoặc đọc một trang LaunchStudio, ChatGPT thất bại.
   - Lỗi này làm hỏng toàn bộ chiến lược GEO và cả kế hoạch test ChatGPT Ads (`chatgpt_ads_plan_launchstudio.md`).
2. **🔴 Mọi trang có hai thẻ `<title>`; 318/320 bài có hai meta description (chưa sửa từ tháng 7).** Một khối code viết cứng trong header của theme lặp lại những gì Yoast đã xuất. Trên trang chủ, `og:url` của khối này vẫn trỏ sang bài blog mới nhất.
3. **🔴 Các trang chính để bán hàng hiển thị yếu trên Google.**
   - Title trang chủ NL là `Launch Studio` (13 ký tự).
   - Title trang chủ EN dài 131 ký tự.
   - Cả 10 landing page dịch vụ đều **để trống meta description** và không có `og:image`.
4. **🟠 Một số trang trùng hoặc lỗi vẫn được index:**
   - `/vibe-coding-nederland/` giống `/ai-app-naar-productie/` 99%.
   - `/en/vibe-coding/` giống `/en/ai-app-into-production/` 99%.
   - `/privacybeleid-1/` hiển thị toàn bộ trang lưu trữ Insights dưới tiêu đề chính sách bảo mật.
   - `/en/homepage/` là trang trống 136 từ, tiêu đề "Homepage".
5. **🟠 Chưa có schema Organization/ProfessionalService, FAQPage hay Offer (còn từ tháng 7).** `CollectionPage` của trang chủ có `"name": ""`.
6. **🟠 Thực thể thương hiệu bị nhầm lẫn bên ngoài site.** Tìm `"launchstudio.eu"` chỉ ra các công ty "Launch Studio" khác (một agency thiết kế ở Czech trên Clutch, một agency ở Anh, một khóa học trên Product Hunt), không có kết quả nào về site này. Không tìm thấy hồ sơ bên thứ ba nào của LaunchStudio.

**Kết luận: 🟠 Cỗ máy nội dung mạnh, lớp kỹ thuật và thực thể yếu.** 5 việc đầu tiên chủ yếu là chỉnh theme, server và cài đặt một lần, khoảng 1-2 ngày công dev. Chúng mở khóa giá trị đang bị giới hạn của 318 bài đã đăng.

### Bảng điểm

| Hạng mục | Tình trạng | So với 31/7 |
|---|---|---|
| Khả năng crawl với Google/Bing | 🟢 Tốt | = |
| Khả năng crawl với trợ lý AI | 🔴 Chặn bot huấn luyện và bot người dùng của OpenAI/Anthropic | ⬇ mới |
| Vệ sinh index (trang trùng, trang trống, tag) | 🔴 Yếu | ⬇ thêm trang |
| Title và meta | 🔴 Thẻ trùng toàn site, trống trên landing page | = |
| Schema | 🟠 Article + Person ổn, thiếu entity/FAQ/Offer | ⬆ nhẹ |
| Độ sâu nội dung | 🟢 2.300-2.800 từ mỗi bài | ⬆⬆ |
| Số lượng nội dung | 🟢 318 bài, 302 có hreflang NL/EN | ⬆⬆ |
| Đa ngôn ngữ (hreflang/slug) | 🟠 18 bài NL chưa có cặp, 9 bài NL dùng slug tiếng Anh "-2" | ⬇ lỗi mới tái phát |
| E-E-A-T và tác giả | 🟠 Có tên thật, hồ sơ trống | ⬆ |
| Thực thể bên ngoài / thương hiệu | 🔴 Không có hồ sơ bên thứ ba, trùng tên | = |
| llms.txt | 🟠 Đủ danh sách bài, thiếu tóm tắt dịch vụ | ⬆ |
| Hiệu năng (ước lượng) | 🟡 TTFB 0,68 s, không có header cache | = |

---

## 2. Tiến độ so với audit ngày 31/7

| # | Lỗi tháng 7 | Tình trạng 19/11 | Bằng chứng |
|---|---|---|---|
| 1 | Khối OG/meta viết cứng trong theme bị trùng | ❌ Chưa sửa | 320/320 bài có 2 `<title>`, 318/320 có 2 meta description, 319/320 có 2 `og:title` |
| 2 | Title trang chủ NL quá ngắn, EN 131 ký tự | ❌ Chưa sửa | NL `Launch Studio` (13), EN 131 ký tự, không đổi |
| 3 | `rel="next"` thừa trên trang chủ | ❌ Chưa sửa | Vẫn còn `<link rel="next" href="https://launchstudio.eu/page/2/">` |
| 4 | Không có schema Organization | ❌ Chưa sửa | Graph trang chủ chỉ có `CollectionPage`, `BreadcrumbList`, `WebSite` |
| 5 | Không có schema FAQPage | ❌ Chưa sửa | Không trang nào được crawl có `FAQPage` |
| 6 | Tác giả hiển thị `phu.lt` | ✅ Đã sửa | Byline và `Person` = "Duy Le" (hồ sơ vẫn trống, xem F9) |
| 7 | Không có schema Offer/Service | ❌ Chưa sửa | Không có |
| 8 | Không có hyperlink sang manifera.com | ✅ Đã sửa | Logo footer link tới `manifera.com/?utm_source=launchstudio&utm_medium=logo-footer`; bài mới link tới `/services/offshore-software-development/` |
| 9 | `llms.txt` chỉ có 5 bài, không nói về dịch vụ | 🟡 Sửa một phần | Đã liệt kê đủ bài (550 dòng), vẫn chưa có tóm tắt dịch vụ, giá, quy trình |
| 10 | Chỉ 71/362 bài được đăng | ✅ Tốt hơn nhiều | 318 bài đã xuất bản, 2 bản nháp |
| 11 | Bài mỏng (250-350 từ) | ✅ Đã sửa với bài mới | Các bài mới nhất có 2.275-2.685 từ trong thân bài |
| 12 | Ảnh testimonial base64 nhúng thẳng, alt rỗng | ❌ Chưa sửa | 1 ảnh base64 alt rỗng trên trang chủ NL và EN |
| 13 | Không có page cache/CDN | ❌ Chưa sửa | HTML không có `Cache-Control`, TTFB 0,68 s ở mọi trang |

---

## 3. Phát hiện và cách sửa

Mức ưu tiên: **P0** = sửa trong tuần này, **P1** = trong tháng này, **P2** = để sau. Công sức: S dưới 2 giờ, M dưới 1 ngày, L trên 1 ngày.

### F1 (P0, S) - Trợ lý AI bị server chặn bằng 403

**Bằng chứng.** Cùng một URL, khác user-agent, ngày 19/11/2026:

| User-agent | Chủ sở hữu / mục đích | launchstudio.eu | manifera.com |
|---|---|---|---|
| `GPTBot` | Crawler huấn luyện của OpenAI | **403** | 200 |
| `ChatGPT-User` | ChatGPT mở trang thay cho người dùng | **403** | 200 |
| `OAI-SearchBot` | Chỉ mục tìm kiếm của ChatGPT | 200 | 200 |
| `ClaudeBot` | Crawler của Anthropic | **403** | 200 |
| `anthropic-ai` | Anthropic (token cũ) | **403** | 200 |
| `Claude-User` / `Claude-SearchBot` | Claude mở trang cho người dùng / tìm kiếm | 200 | 200 |
| `CCBot` | Common Crawl (nguồn dữ liệu của nhiều LLM) | **403** | 200 |
| `Bytespider`, `cohere-ai` | ByteDance, Cohere | **403** | 200 |
| `PerplexityBot`, `Perplexity-User` | Perplexity | 200 | 200 |
| `Google-Extended`, `Googlebot`, `bingbot`, `Applebot` | Google, Bing, Apple | 200 | 200 |

Các chi tiết khác:

- Lệnh chặn 403 áp dụng cả cho `/robots.txt`, `/llms.txt` và sitemap.
- Trang chặn ghi `403 | Forbidden`, có `Request ID` và IP người truy cập, và gửi CSP riêng rất chặt. Đây là dấu hiệu của WAF hoặc danh sách đen user-agent "bad bot" đứng trước WordPress, không phải do WordPress. Trên LaunchStudio không có plugin bảo mật WordPress nào đang bật.
- Manifera, cùng IP, cho qua tất cả các user-agent này. Như vậy quy tắc chặn được cấu hình riêng cho từng site (vhost).

**Vì sao quan trọng.**

- `ChatGPT-User` là cách ChatGPT đọc một trang khi người dùng dán link hoặc nhờ nó kiểm tra một website. Hiện tại ChatGPT nhận 403 với LaunchStudio.
- `GPTBot`, `ClaudeBot` và `CCBot` quyết định 318 bài của LaunchStudio có được đưa vào câu trả lời của các model trong tương lai hay không.
- Site tạo `llms.txt` chính là để mời các crawler này vào, rồi lại chặn chúng. Sửa lỗi này thì mọi việc GEO khác trong audit mới có tác dụng.

**Cách sửa.**

1. Trong cấu hình server/WAF của `launchstudio.eu`, xóa các user-agent sau khỏi danh sách chặn, hoặc thêm một quy tắc cho phép đặt phía trên danh sách đó: `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `ClaudeBot`, `Claude-User`, `Claude-SearchBot`, `anthropic-ai`, `PerplexityBot`, `Perplexity-User`, `CCBot`, `Google-Extended`, `Applebot-Extended`.
   - Có thể tiếp tục chặn `Bytespider`, vì bot này không mang lại giá trị B2B.
   - Cách đơn giản nhất là làm giống vhost của Manifera, vì Manifera đã cho các bot này qua.
2. Giữ nguyên `robots.txt`, vì file này đã cho phép tất cả. Nếu muốn ghi rõ, có thể thêm các nhóm `User-agent: GPTBot` / `Allow: /`.
3. Kiểm tra lại bằng lệnh dưới đây. Mỗi dòng phải trả về `200`.

```bash
for ua in GPTBot/1.1 ChatGPT-User/1.0 ClaudeBot/1.0 anthropic-ai CCBot/2.0; do
  printf "%-18s %s\n" $ua $(curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; $ua)" https://launchstudio.eu/en/)
done
```

**Người làm:** quản trị server. **Phải xong trước khi test ChatGPT Ads bắt đầu ngày 24/11.**

---

### F2 (P0, S) - `<title>`, meta description và khối OG bị trùng trên mọi trang

**Bằng chứng.** `<head>` của trang chủ có một khối của theme (dòng 11-26), sau đó đến khối Yoast (dòng 32-44):

```html
<title>Launch Studio</title>                          <!-- theme -->
<meta name="description" content="LaunchStudio helps ...">    <!-- theme -->
<meta property="og:title" content="Launch Studio">            <!-- theme -->
<meta property="og:url" content="https://launchstudio.eu/app-development-cost-2026-three-year-total-cost-compared-2/"> <!-- theme: bài mới nhất, sai -->
...
<!-- This site is optimized with the Yoast SEO plugin v27.6 -->
<title>Launch Studio</title>                          <!-- Yoast -->
<meta property="og:url" content="https://launchstudio.eu/" />  <!-- Yoast, đúng -->
```

Trên toàn bộ 320 bài: 320 bài có 2 `<title>`, 318 bài có 2 `meta description`, 319 bài có 2 `og:title`. Ở bài viết, description của theme là đoạn trích thô, bị cắt giữa câu.

**Vì sao quan trọng.**

- Hai title và hai description là HTML sai chuẩn, Google sẽ chọn một trong hai một cách không đoán trước được.
- LinkedIn, Facebook, Slack và WhatsApp đọc `og:url` và `og:title` **đầu tiên**. Vì vậy khi chia sẻ link trang chủ, bản xem trước lại hiện bài blog mới nhất.
- Crawler LLM đọc phần head sẽ thấy hai bản tóm tắt mâu thuẫn nhau.

**Cách sửa.**

1. Trong `wp-content/themes/<theme launchstudio>/header.php`, xóa các dòng `<title>`, `meta description`, `og:*` và `twitter:*` được viết cứng.
2. Giữ `wp_head()` và `add_theme_support('title-tag')`, để Yoast là nguồn duy nhất cho title và meta.
3. Kiểm tra: lệnh `curl -s https://launchstudio.eu/ | grep -c '<title'` phải trả về `1`.

---

### F3 (P0, S) - Title trang chủ, meta description và ảnh OG của landing page

**Bằng chứng.**

| URL | Title (ký tự) | Meta description | og:image |
|---|---|---|---|
| `/` | `Launch Studio` (13) | mặc định của theme (115) | không có |
| `/en/` | title 131 ký tự, lặp lại khẩu hiệu | mặc định của theme (115) | không có |
| `/ai-app-naar-productie/`, `/en/ai-app-into-production/` | 37 / 38 | **trống** | không có |
| `/ai-app-beveiliging/`, `/en/ai-app-security/` | 33 / 31 | **trống** | không có |
| `/ai-app-integraties/`, `/en/ai-app-integrations/` | 34 / 35 | **trống** | không có |
| `/ai-app-bouwen-vanaf-scratch/`, `/en/build-ai-app-from-scratch/` | 43 / 41 | **trống** | không có |
| `/vibe-coding-nederlands/`, `/en/vibe-coding-netherlands/` | 38 / 39 | **trống** | không có |

10 landing page này là trang đích của Google Ads và ChatGPT Ads. Một số title viết hoa sai, ví dụ `Ai App Security - Launch Studio` ("Ai" thay vì "AI").

**Cách sửa.** Nhập trong Yoast cho từng trang: SEO title, meta description và ảnh mạng xã hội. Nội dung đề xuất dưới đây chỉ dùng thông tin đã có trên site: giá cố định €800-7.500, 1-3 tuần, Lovable/Bolt/Cursor. Nội dung giữ nguyên tiếng Hà Lan/tiếng Anh vì sẽ dán thẳng lên site.

| Trang | SEO title (≤ 60) | Meta description (≤ 155) |
|---|---|---|
| `/` | `AI-prototype live in 1-3 weken \| LaunchStudio` | `Gebouwd met Lovable, Bolt of Cursor? Wij maken je app launch-ready: beveiliging, betalingen, hosting en deployment. Vaste prijs €800-7.500.` |
| `/en/` | `Get Your AI-Built App Launch-Ready \| LaunchStudio` | `Built with Lovable, Bolt or Cursor? We make it launch-ready: security, payments, hosting and deployment. Fixed price €800-7,500, live in 1-3 weeks.` |
| `/ai-app-naar-productie/` | `AI-app naar productie in 1-3 weken \| LaunchStudio` | `Je AI-app werkt in de demo, maar is hij klaar voor echte gebruikers? Wij doen de 6 checks voor lancering. Vaste prijs vanaf €800.` |
| `/en/ai-app-into-production/` | `AI App Into Production in 1-3 Weeks \| LaunchStudio` | `Your AI app works in the demo. Is it ready for real users? We run the 6 launch checks and fix what fails. Fixed price from €800.` |
| `/ai-app-beveiliging/` | `AI-app beveiliging en security audit \| LaunchStudio` | `Publieke Supabase-keys, open databases, geen RLS? Wij controleren en repareren de beveiliging van je AI-gebouwde app voor lancering.` |
| `/en/ai-app-security/` | `AI App Security Audit and Fixes \| LaunchStudio` | `Public Supabase keys, open databases, missing RLS? We audit and fix the security of your AI-built app before launch. Fixed price.` |
| `/ai-app-integraties/` | `Betalingen en integraties voor AI-apps \| LaunchStudio` | `Mollie, Stripe, iDEAL en webhooks die echt werken. Wij koppelen betalingen en integraties aan je Lovable- of Bolt-app.` |
| `/en/ai-app-integrations/` | `Payments and Integrations for AI Apps \| LaunchStudio` | `Stripe, Mollie, iDEAL and webhooks that actually fire. We connect payments and integrations to your Lovable or Bolt app.` |
| `/ai-app-bouwen-vanaf-scratch/` | `AI-app laten bouwen vanaf nul \| LaunchStudio` | `Nog geen prototype? Wij bouwen je app van idee tot live product, met beveiliging, betalingen en hosting vanaf dag één.` |
| `/en/build-ai-app-from-scratch/` | `Build an AI App From Scratch \| LaunchStudio` | `No prototype yet? We build your app from idea to live product, with security, payments and hosting in place from day one.` |
| `/vibe-coding-nederlands/` | `Vibe coding app laten afmaken \| LaunchStudio` | `Je AI zei "Klaar." Dat was het niet. Wij maken je vibe-coded app af en klaar voor productie, met vaste prijs en duidelijke planning.` |
| `/en/vibe-coding-netherlands/` | `Finish Your Vibe-Coded App \| LaunchStudio` | `Your AI said "Done." It wasn't. We finish your vibe-coded app and get it production-ready, at a fixed price with a clear timeline.` |

Sau đó:

- Thiết kế một ảnh mạng xã hội 1200×630 cho mỗi cặp landing page, cộng một ảnh mặc định trong Yoast → Settings → Site basics.
- Sửa "Ai" thành "AI" trong title các trang.
- Bỏ `rel="next"` trên trang chủ. Thẻ này cho thấy trang chủ đang chạy vòng lặp của blog. Đặt Settings → Reading thành trang tĩnh, hoặc bỏ link phân trang trong template.

---

### F4 (P0, S) - Trang trùng, trang lỗi và trang trống đang được index

**Bằng chứng.** Độ giống nhau của nội dung chính, đo theo chuỗi từ:

| URL A | URL B | Độ giống | Vấn đề |
|---|---|---|---|
| `/vibe-coding-nederland/` | `/ai-app-naar-productie/` | **99%** | Trùng hoàn toàn, cạnh tranh với một landing page quảng cáo |
| `/en/vibe-coding/` | `/en/ai-app-into-production/` | **99%** | Trùng hoàn toàn |
| `/vibe-coding-nederland/` | `/vibe-coding-nederlands/` | 20% | Hai URL cho cùng một từ khóa ("vibe coding nederland(s)") |
| `/privacybeleid-1/` | `/inzichten/` | **100%** | URL chính sách bảo mật lại hiển thị toàn bộ trang Insights (514 KB, H1 "Inzichten") |
| `/en/homepage/` | `/en/` | n/a | Trang trống 136 từ, title và H1 là "Homepage", không có hreflang, nằm trong sitemap |

Tất cả đều trả về `200`, là `index, follow`, tự canonical về chính mình và có trong `page-sitemap.xml`.

**Cách sửa.**

1. Thêm redirect 301. LaunchStudio chưa có plugin Redirection, nên cài plugin `Redirection` hoặc thêm quy tắc trong cấu hình server:

```
/vibe-coding-nederland/   -> /vibe-coding-nederlands/        301
/en/vibe-coding/          -> /en/vibe-coding-netherlands/    301
/privacybeleid-1/         -> /privacybeleid/                 301
/en/homepage/             -> /en/                            301
```

2. Xóa hoặc chuyển vào thùng rác 4 trang nguồn để chúng ra khỏi sitemap.

Trong các trang này, chỉ `/ai-app-naar-productie/`, `/en/ai-app-into-production/` và `/vibe-coding-nederlands/` được nhắc trong các tài liệu quảng cáo. Không URL nào bị redirect đang được dùng làm trang đích quảng cáo trong dự án này.

---

### F5 (P1, M) - Thiếu schema thực thể: Organization / ProfessionalService, FAQPage, Offer

**Bằng chứng.**

- Graph trang chủ: `CollectionPage` (với `"name": ""`), `BreadcrumbList`, `WebSite`.
- Landing page: chỉ có `WebPage`.
- Bài viết: `Article`, `WebPage`, `Person`, không có tổ chức `publisher`.
- Trang chủ có công cụ tính giá và FAQ ("Wat kost jouw project?") dạng HTML thường, không có markup.

**Vì sao quan trọng.** Công cụ trả lời AI dựa vào dữ liệu thực thể có cấu trúc để trả lời "LaunchStudio là ai, giá bao nhiêu, ở đâu". Vì tên bị trùng (F11), một graph thực thể rõ ràng có `sameAs` và `parentOrganization: Manifera` là cách chính để máy biết đây là "Launch Studio" nào.

Từ năm 2023, Google chỉ hiển thị rich result FAQ cho site chính phủ và y tế. Vì vậy FAQPage chủ yếu giúp LLM trích xuất và giúp với Bing, không phải để có sao trên kết quả Google.

**Cách sửa.**

1. Trong Yoast → Settings → Site representation:
   - Chọn Organization, tên `LaunchStudio`, logo 512×512.
   - Thêm các hồ sơ mạng xã hội sẽ tạo ở F11.
   - Đặt ký tự phân cách title cho trang chủ.

   Khi đó Yoast sẽ xuất node `Organization` và dùng nó làm `publisher` cho mọi Article.
2. Thêm khối dưới đây trên toàn site, ví dụ bằng một mu-plugin nhỏ hoặc trong `footer.php` của theme. Địa chỉ lấy từ `launchstudio_info.md` §1.3; điền `sameAs` khi đã có hồ sơ.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://launchstudio.eu/#organization",
  "name": "LaunchStudio",
  "alternateName": ["Launch Studio", "LaunchStudio by Manifera"],
  "url": "https://launchstudio.eu/",
  "logo": "https://launchstudio.eu/wp-content/uploads/<logo-512.png>",
  "description": "LaunchStudio takes apps built with AI tools such as Lovable, Bolt and Cursor to production: security, payments, hosting and deployment, at a fixed price of €800-7,500 in 1-3 weeks.",
  "priceRange": "€800-€7,500",
  "areaServed": ["NL", "BE", "DE", "EU"],
  "knowsAbout": ["Lovable", "Bolt", "Cursor", "Replit", "Supabase", "Stripe", "Mollie", "iDEAL", "AI app security", "vibe coding"],
  "parentOrganization": {
    "@type": "Organization",
    "@id": "https://www.manifera.com/#Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com/"
  },
  "founder": {"@type": "Person", "name": "Herre Roelevink", "sameAs": "https://www.linkedin.com/in/herre-roelevink-director-manifera/"},
  "address": [
    {"@type": "PostalAddress", "streetAddress": "Herengracht 420", "postalCode": "1017 BZ", "addressLocality": "Amsterdam", "addressCountry": "NL"},
    {"@type": "PostalAddress", "streetAddress": "100 Tras Street #16-01", "postalCode": "079027", "addressLocality": "Singapore", "addressCountry": "SG"},
    {"@type": "PostalAddress", "streetAddress": "Floor 11, Block C, 10 Pho Quang Street", "addressLocality": "Ho Chi Minh City", "addressCountry": "VN"}
  ],
  "sameAs": []
}
</script>
```

3. Thêm `FAQPage` trên trang chủ (NL và EN), dùng nguyên văn các câu hỏi FAQ đang hiển thị. Làm tương tự trên mỗi landing page có khối FAQ.
4. Thêm `OfferCatalog` cho hai gói (Launch Ready, Launch & Grow). Dùng đúng giá đang hiển thị trên trang, để markup và nội dung hiển thị khớp nhau.
5. Sửa `CollectionPage.name` đang trống. Lỗi này tự hết khi trang chủ thành trang tĩnh có title Yoast (F3).
6. Kiểm tra bằng Rich Results Test của Google và validator.schema.org.

---

### F6 (P1, S) - Bài NL dùng slug tiếng Anh có đuôi "-2" (quy trình bị lỗi trở lại)

**Bằng chứng.** 9 bài NL dùng slug tiếng Anh có đuôi `-2`, vì bản EN đã lấy slug đó trước. **Cả 3 bài NL mới nhất (tháng 11/2026) đều bị**, nghĩa là quy trình upload hiện tại đang tạo ra lỗi này.

```
/app-development-cost-2026-three-year-total-cost-compared-2/
/github-copilot-agent-code-review-production-checks-for-agent-pull-requests-2/
/bolt-cloud-or-your-own-backend-taking-a-bolt-app-to-production-2/
/lovable-hosting-environment-variables-across-three-environments-2/
/supabase-data-processing-agreement-what-dutch-founders-need-2/
/mollie-integration-for-ai-built-apps-step-by-step-2/
/ai-gegenereerde-data-naar-notion-pushen-via-api-ai-software-engineering-best-practices-2/
/bolt-ai-alkmaar-2/
/waarom-90-van-ai-prototypes-nooit-live-gaat-2/
```

**Vì sao quan trọng.**

- Người tìm kiếm tiếng Hà Lan và LLM thấy URL tiếng Anh trên trang tiếng Hà Lan, nên từ khóa NL trong URL yếu đi.
- Đuôi `-2` trông giống trang trùng.
- Ví dụ: title NL là "Kosten van App-Ontwikkeling in 2026", nhưng URL là `app-development-cost-2026-...-2`.

**Cách sửa.**

1. Trong script upload, đặt `slug` NL rõ ràng theo title NL, ví dụ `kosten-app-ontwikkeling-2026-totaal-drie-jaar`. Polylang chỉ cho phép hai ngôn ngữ dùng chung một slug khi bật tùy chọn "share slugs" (bản Pro), nên dịch slug là cách gọn nhất.
2. Với 9 bài hiện có:
   - Đổi slug.
   - Thêm redirect 301 từ URL cũ.
   - Cập nhật `social_link_map.tsv` và các bài social đang link tới URL cũ.

---

### F7 (P1, S) - 18 bài NL chưa có bản EN tương ứng (không có hreflang)

**Bằng chứng.** 302/320 URL bài viết có `hreflang nl + en + x-default`. 18 bài chỉ có bản NL thì không có hreflang, phần lớn thuộc đợt tháng 3/2026:

- `wat-kost-het-om-je-prototype-live-te-krijgen`
- `bureau-vs-freelancer-vs-launchstudio`
- `wie-zitten-er-achter-launchstudio`
- `kan-mijn-lovable-code-echt-in-productie`
- `hoe-wij-werken-van-intake-tot-oplevering-in-5-stappen`
- 13 bài khác (danh sách đầy đủ ở phụ lục).

**Cách sửa.** Nhiều bài trong số này thuộc giai đoạn ra quyết định (giá, chúng tôi là ai, cách làm việc, agency hay freelancer), đúng những câu khách EN và LLM cũng hỏi. Dịch 6 bài quan trọng nhất và nối chúng làm bản dịch trong Polylang.

---

### F8 (P1, M) - Trang tag mỏng nhưng vẫn được index

**Bằng chứng.**

- Có 445 tag: **292 tag chỉ có 1 bài, 75 tag không có bài nào**.
- Mọi trang tag đều là `index, follow` và có trong `post_tag-sitemap.xml` (370 URL).
- Ví dụ `/en/tag/ai-app/` chỉ là trang lưu trữ, không có nội dung riêng.

**Vì sao quan trọng.** Khoảng 370 URL gần như trống làm loãng ngân sách crawl và tín hiệu chất lượng của site; tính ra gần như mỗi bài viết sinh ra một trang tag.

**Cách sửa.**

1. Vào Yoast → Settings → Tags, đặt "Show tags in search results" = **Off**. Thao tác này gắn noindex và loại tag khỏi sitemap.
2. Giữ category được index (14 URL) và viết cho mỗi category một đoạn giới thiệu 150-300 từ.
3. Ngừng tạo tag mới cho mỗi bài trong script upload. Dùng lại một danh sách cố định khoảng 30 tag.

---

### F9 (P1, S) - Thực thể tác giả chỉ có tên, không có hồ sơ

**Bằng chứng.**

- `Person` = "Duy Le", ảnh Gravatar mặc định, `url` là `/en/author/duy-le/`.
- Không có `jobTitle`, `description` hay `sameAs`.
- Trang tác giả không có tiểu sử.

**Cách sửa.**

1. Trong WordPress → Users, thêm:
   - tiểu sử 2-3 câu: vai trò ở LaunchStudio/Manifera và tác giả review những gì
   - ảnh thật
   - URL LinkedIn
2. Yoast đọc trường "Website" và các trường mạng xã hội để đưa vào `sameAs`.
3. Với bài kỹ thuật, có thể thêm dòng người review ("Technically reviewed by …, Manifera engineering") nếu đúng sự thật. Không bịa người review.

---

### F10 (P1, S) - Trang lưu trữ Insights nặng và khó tiếp cận

**Bằng chứng.**

| Trang | Dung lượng HTML | Số ảnh | Alt rỗng | Số H2 |
|---|---|---|---|---|
| `/inzichten/` | 513 KB | 169 | 168 | 0 |
| `/en/insights/` | 460 KB | 151 | 150 | 0 |

Cả hai có TTFB khoảng 1,0 s, trong khi các trang khác là 0,68 s. Title bản EN là `Blogs - Launch Studio`.

**Cách sửa.**

- Phân trang, mỗi trang 12-24 bài.
- Dùng title bài làm `alt` cho ảnh thumbnail, hoặc để `alt=""` nhưng đặt title trong một heading có link. Mỗi thẻ bài cần có title dạng `<h2>`/`<h3>`.
- Thêm đoạn giới thiệu khoảng 100 từ cho mỗi trang lưu trữ và nhóm bài theo category (Security, Payments, Hosting, Tools).
- Title: `Insights: AI App Security, Payments and Launch Guides | LaunchStudio`, hoặc bản ngắn hơn (≤ 60 ký tự).

---

### F11 (P1, L) - GEO: trùng tên thương hiệu, không có dấu ấn bên thứ ba

**Bằng chứng.**

- Tìm `"launchstudio.eu"` trên web (19/11) ra các kết quả sau:
  - [Launch Studio trên Clutch](https://clutch.co/profile/launch-studio), một agency thiết kế ở Czech thành lập năm 2025
  - [một agency ở Anh](https://launch-studio-ltd.squarespace.com/services)
  - [một khóa học gọi vốn cộng đồng trên Product Hunt](https://www.producthunt.com/products/launch-studio)
  - [một công cụ NFT](https://saasbrowser.com/saas/966783/launch-studio)
- Không có kết quả nào về LaunchStudio này. Không tìm thấy hồ sơ review, danh bạ doanh nghiệp hay bài báo nào nhắc đến nó.
- Ngay trên site, tên được viết hai kiểu: "Launch Studio" (tên site, title, schema WebSite) và "LaunchStudio" (nội dung, phần mở đầu llms.txt).

**Vì sao quan trọng.**

- LLM trả lời câu "LaunchStudio là ai" theo những gì phần lớn web nói. Hiện nay phần lớn web đang nói về các công ty khác.
- Khi không có nguồn độc lập xác nhận, câu trả lời AI cũng hiếm khi giới thiệu một nhà cung cấp cho câu hỏi kiểu "ai có thể đưa app Lovable của tôi lên production".

**Cách sửa.**

1. Chọn **một** cách viết, "LaunchStudio", và dùng thống nhất ở: tên site trong Yoast, title, schema, footer, hồ sơ mạng xã hội và llms.txt. "Launch Studio" chỉ giữ làm `alternateName`.
2. Tạo các hồ sơ ghi rõ "LaunchStudio by Manifera" và link về launchstudio.eu:
   - LinkedIn Company Page
   - Clutch
   - GoodFirms (dự án đã có thư mục `goodfirms/` cho Manifera)
   - Crunchbase
   - Product Hunt (ra mắt checklist miễn phí hoặc công cụ tính giá)
   - G2 hoặc Sortlist
   - KVK/Google Business Profile, chỉ khi có địa chỉ đăng ký thật
3. Nhờ 3-5 khách hàng cũ viết review trên Clutch hoặc Google. Chỉ dùng review thật.
4. Thêm một dòng trên site Manifera, ví dụ ở `/services/` và `/about-us/`: "AI prototype to production: see LaunchStudio, our launch service", kèm link. Hiện Manifera link sang LaunchStudio từ **0** trên 36 trang đã crawl. Một link từ domain của công ty mẹ là cách xác nhận rẻ nhất.
5. Đưa tất cả URL hồ sơ này vào mảng `sameAs` (F5).

---

### F12 (P1, S) - llms.txt: đủ danh sách bài, nhưng không nói mình bán gì

**Bằng chứng.**

- `llms.txt` do plugin **LLMS Full TXT Generator** (v2.1.2) tạo, không phải Yoast.
- File mở đầu bằng khẩu hiệu của site và `Contact: phu.le@manifera.com`, sau đó là 320 link xếp theo bảng chữ cái, NL và EN lẫn lộn.
- Không có mô tả dịch vụ, giá, quy trình, các trang dịch vụ hay FAQ.
- `llms-full.txt` nặng 3,7 MB.

**Cách sửa.**

- Nếu plugin cho phép phần đầu tùy chỉnh, thêm khối dưới đây lên đầu file.
- Nếu không, thay bằng một file `llms.txt` tĩnh do mình biên soạn, còn `llms-full.txt` vẫn để plugin tạo.
- Chỉ dùng thông tin đã công bố trên site.
- Dùng email chung (ví dụ `hello@`) thay cho email cá nhân.

```markdown
# LaunchStudio

> LaunchStudio (by Manifera) takes apps built with AI tools such as Lovable, Bolt, Cursor and Replit to production. We fix security, payments, hosting and deployment. Fixed price €800-7,500, delivered in 1-3 weeks. Based in Amsterdam, engineering in Ho Chi Minh City.

## Services
- [AI app into production](https://launchstudio.eu/en/ai-app-into-production/): the 6 launch checks
- [AI app security](https://launchstudio.eu/en/ai-app-security/): Supabase RLS, exposed keys, auth
- [Payments and integrations](https://launchstudio.eu/en/ai-app-integrations/): Stripe, Mollie, iDEAL, webhooks
- [Finish a vibe-coded app](https://launchstudio.eu/en/vibe-coding-netherlands/)
- [Build from scratch](https://launchstudio.eu/en/build-ai-app-from-scratch/)

## Pricing
- Launch Ready: <exact range from site>
- Launch & Grow: <exact range from site>

## Best guides
- (10-15 cornerstone articles, EN, by cluster)

## Nederlands
- (same structure, NL URLs)
```

Đồng thời cập nhật plugin (2.1.2 → 2.1.3).

---

### F13 (P2, M) - Hiệu năng và các việc dọn dẹp

| Hạng mục | Bằng chứng | Cách sửa |
|---|---|---|
| TTFB | 0,68 s trên mọi trang, 1,0 s trên trang lưu trữ; HTML không có `Cache-Control` | Page cache (FastCGI cache trên server hoặc plugin WP) + CDN; mục tiêu TTFB < 0,3 s |
| Core Web Vitals | Chưa đo (hết quota PSI) | Chạy PageSpeed Insights cho `/`, `/en/`, 2 landing page, 1 bài; ghi kết quả vào file này |
| Ảnh base64 nhúng thẳng | 1 ảnh `data:` lớn, `alt=""`, trên cả hai trang chủ | Chuyển thành file WebP; alt = tên và vai trò của người trong ảnh |
| Meta Google AdSense | `Google AdSense meta tags toegevoegd door Site Kit` trên trang chủ | Nếu không dùng AdSense, ngắt kết nối trong Site Kit (quảng cáo hiển thị trên site dịch vụ B2B làm giảm độ tin cậy) |
| `/favicon.ico` | 404 | Tải lên favicon.ico ở thư mục gốc |
| Plugin cũ | Yoast 27.6 → 28.9, Polylang 3.8.3 → 3.9.2, WP Mail SMTP 4.8.0 → 4.10.4, UpdraftPlus, Flying Scripts | Cập nhật sau khi backup, ưu tiên Yoast và Polylang |
| Analytics | Đã có Site Kit (GA4 + Ads) | Thêm báo cáo exploration "AI referrals" trong GA4 (mục 5) |

---

## 4. Điểm nội dung Yoast (40 bài sửa gần nhất)

- **Điểm SEO:** 21 tốt, 19 OK, 0 kém.
- **Điểm yếu:**
  - Focus keyphrase đôi khi chỉ là một mảnh từ, ví dụ `AI-Gegenereerde`, `AI-Generated`, `App-Ontwikkeling`, `Offshore-Ontwikkelteam`. Không ai tìm kiếm cụm như vậy, nên điểm Yoast tính theo nó không có ý nghĩa.
  - Keyphrase NL đôi khi để nguyên tiếng Anh hoặc dịch nửa vời (`Bolt App` trên bài Bolt bản NL).
- **Việc cần làm:** trong script upload, lấy focus keyphrase từ các danh sách từ khóa đã kiểm chứng (`nl_security_verified_keywords.csv`, `payments_nl_keywords_validated.csv`, `lovable_5_seeds_volume_validated.csv`) thay vì suy ra từ title.

---

## 5. KPI và cách đo

| KPI | Mốc hiện tại (19/11) | Mục tiêu đến 28/02/2027 | Đo ở đâu |
|---|---|---|---|
| User-agent AI trả về 200 | 5/10 UA chính | 10/10 | Lệnh curl ở F1 (hằng tuần) |
| Trang có đúng 1 `<title>` | 0% | 100% | `curl \| grep -c '<title'` trên 5 URL |
| Landing page có meta description + og:image | 0/10 | 10/10 | Yoast |
| Trang trùng/trang trống được index | 4 | 0 | `page-sitemap.xml` |
| Trang tag được index | 370 | 0 | `post_tag-sitemap.xml` |
| Hồ sơ bên thứ ba link về launchstudio.eu | chưa tìm thấy | ≥ 5 | Kiểm tra thủ công |
| Phiên truy cập từ AI (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai) | đo ngay bây giờ | +100% so với mốc tháng 12 | GA4 → Traffic acquisition → session source, regex `chatgpt\|perplexity\|gemini\|copilot\|claude` |
| Độ chính xác khi AI trả lời về thương hiệu (bộ câu hỏi bên dưới) | đo ngay bây giờ | ≥ 7/10 câu mô tả đúng LaunchStudio | Test thủ công hằng tháng |
| Lượt hiển thị GSC của landing page | đo ngay bây giờ | +50% | Search Console → Pages, lọc `/ai-app-` |

**Bộ câu hỏi test GEO hằng tháng.** Hỏi từng câu trong ChatGPT (cả khi đăng xuất và đăng nhập), Perplexity và Gemini. Ghi lại LaunchStudio có được nhắc tên không, và mô tả, giá, địa điểm có đúng không. Giữ nguyên câu hỏi tiếng Anh/tiếng Hà Lan, vì đó là ngôn ngữ khách hàng thật sẽ hỏi.

1. What is LaunchStudio (launchstudio.eu)?
2. Who can take my Lovable app to production in the Netherlands?
3. How much does it cost to make an AI prototype production-ready?
4. Is my Supabase anon key safe in a Lovable app? Who can audit it?
5. Bureau die mijn Bolt-app live kan zetten met iDEAL-betalingen?
6. Wat kost het om een AI-prototype live te krijgen?
7. Vibe coding app laten afmaken door een developer in Nederland
8. LaunchStudio vs hiring a freelancer to fix a Lovable app
9. Who is behind LaunchStudio and Manifera?
10. Best services to secure an AI-built app before launch in Europe

---

## 6. Kế hoạch hành động

| Thời gian | Việc cần làm | Phát hiện | Người làm | Công sức |
|---|---|---|---|---|
| Tuần 19/11 | Bỏ chặn user-agent AI trên server/WAF | F1 | Quản trị server | S |
| Tuần 19/11 | Xóa khối meta/OG trong theme | F2 | Dev | S |
| Tuần 19/11 | 4 redirect + xóa trang trống | F4 | Dev | S |
| Tuần 19/11 | Title, description, ảnh mạng xã hội cho 12 trang | F3 | Content | S |
| Tuần 24/11 | Sửa slug NL trong script upload; đổi tên 9 bài + 301 | F6 | Content/dev | S |
| Tuần 24/11 | Noindex tag; danh sách tag cố định trong script | F8 | Content | S |
| Tuần 24/11 | Schema Organization + FAQPage + Offer | F5 | Dev | M |
| Tuần 1/12 | Hồ sơ tác giả; thống nhất cách viết tên thương hiệu | F9, F11 | Content | S |
| Tuần 1/12 | Phần đầu llms.txt do mình biên soạn | F12 | Content | S |
| Tháng 12 | Hồ sơ LinkedIn, Clutch, GoodFirms, Crunchbase, Product Hunt; link từ Manifera sang LaunchStudio | F11 | Marketing | L |
| Tháng 12 | Dịch 6 bài NL giai đoạn ra quyết định | F7 | Content | M |
| Tháng 12 | Page cache + CDN; đo mốc PageSpeed | F13 | Quản trị server | M |
| Hằng tháng | Test câu hỏi GEO + cập nhật bảng KPI | 5 | Marketing | S |

---

## Phụ lục A - Dữ liệu thô

**Hạ tầng**

- IP 136.243.57.57 (giống manifera.com); DNS ở DigitalOcean.
- HTTP/1.1, có quảng bá h3; HSTS preload.
- WordPress 7.1.5, Yoast 27.6, Polylang 3.8.3, Site Kit 1.192.0, LLMS Full TXT Generator 2.1.2.

**Sitemap (19/11)**

| Sitemap | Số URL | Sửa lần cuối |
|---|---|---|
| post | 320 (169 NL / 151 EN) | 2026-11-19 |
| page | 21 | 2026-10-26 |
| category | 14 | 2026-11-19 |
| post_tag | 370 | 2026-11-19 |
| author | 2 | 2026-06-22 |

**Số URL bài theo tháng (lastmod trong sitemap):** T3: 17, T6: 13, T7: 88, T8: 74, T9: 20, T10: 32, T11: 76.

**18 bài NL chưa có cặp hreflang:**

- `mijn-eerste-klant-betaalde-er-gebeurde-niets`
- `hoeveel-is-jouw-gebruikersdata-waard-voor-een-hacker`
- `de-echte-kosten-van-niet-lanceren`
- `van-prototype-naar-47-betalende-klanten-in-3-weken`
- `wat-gebeurt-er-als-je-app-gehackt-wordt`
- `hoe-behoud-je-eigendom-als-je-met-developers-werkt`
- `de-launch-checklist-die-je-wel-begrijpt`
- `bureau-vs-freelancer-vs-launchstudio`
- `wat-kost-het-om-je-prototype-live-te-krijgen`
- `waarom-90-van-ai-prototypes-nooit-live-gaat-2`
- `kan-mijn-lovable-code-echt-in-productie`
- `wie-zitten-er-achter-launchstudio`
- `wat-als-het-niet-werkt-hoe-wij-risico-wegnemen`
- `je-eerste-100-gebruikers-wat-breekt-er-het-eerst`
- `zelf-doorbouwen-of-uitbesteden-na-de-launch`
- `van-bijbaan-idee-naar-200-gebruikers-in-6-weken`
- `hoe-een-fysiotherapeut-zijn-wachtlijst-oploste-met-een-app`
- `hoe-wij-werken-van-intake-tot-oplevering-in-5-stappen`

**On-page của các bài mới nhất** (tất cả trả 200, canonical về chính nó, hreflang nl/en/x-default, H1 = title)

| Bài | Số từ thân bài | H2 | Ký tự title |
|---|---|---|---|
| EN app-development-cost-2026 | 2.275 | 16 | 75 |
| NL kosten app-ontwikkeling 2026 | 2.344 | 16 | 89 |
| EN github-copilot-agent-code-review | 2.459 | 10 | 91 |
| NL github-copilot … productiechecks | 2.658 | 10 | 90 |
| EN bolt-cloud-or-your-own-backend | 2.367 | 11 | 79 |
| NL bolt cloud of een eigen backend | 2.685 | 11 | 84 |

Google cắt title dài hơn 60 ký tự. Đặt SEO title ngắn hơn trong Yoast, và giữ H1 dài.

**Lệnh test crawler đã dùng:** `curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; <UA>)" <url>`
