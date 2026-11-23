# Manifera (manifera.com) - Audit SEO & GEO, ngày 19/11/2026

**Bản tiếng Việt của:** `seo-geo-audit-manifera-com-2026-11-19.md`. Bản tiếng Anh là bản chuẩn; nếu hai bản khác nhau, lấy bản tiếng Anh.

**Thay thế:** `seo-geo-audit-manifera-com.md` (31/7/2026). File cũ vẫn được giữ để tra lịch sử; mục 2 theo dõi từng lỗi của audit đó.

**Phạm vi:**

- SEO kỹ thuật
- On-page
- Dữ liệu có cấu trúc (schema)
- Nội dung và độ phủ chủ đề
- GEO: khả năng hiện diện trong ChatGPT, Perplexity, Claude, Gemini và Google AI Overviews

**Phương pháp:**

- Crawl HTTP thô (`curl`) các file `robots.txt`, `sitemap_index.xml` cùng 12 sitemap con, `llms.txt` và `llms-full.txt`.
- Phân tích on-page 28 URL trong `page-sitemap.xml` và 8 bài mới nhất: title, meta, canonical, OG, heading, ảnh, JSON-LD, số từ.
- Kiểm tra quyền truy cập với 25 user-agent crawler.
- Đo độ giống nhau về nội dung giữa các cặp trang nghi trùng.
- Dữ liệu WordPress qua MCP: plugin, số bài, điểm Yoast của 40 bài sửa gần nhất.
- Tìm kiếm web các nhắc đến Manifera trên trang bên thứ ba.

**Giới hạn:**

- Không có dữ liệu Search Console và GA4.
- API PageSpeed Insights đã hết quota trong ngày nên không có số Core Web Vitals. Phần hiệu năng dùng TTFB, dung lượng HTML và số tài nguyên làm chỉ số ước lượng.
- Crawl đọc HTML thô, không phải DOM sau khi chạy JavaScript.

---

## 1. Tóm tắt

Nền tảng của Manifera khá tốt:

- Mọi crawler AI đều được phép truy cập.
- Sitemap mới, bài viết được cập nhật ngày 18/11.
- Đã có `llms.txt`.
- Bài mới dài 2.100-3.400 từ, chia H2/H3 rõ ràng, có tên tác giả thật.
- Điểm Yoast của các bài gần đây đều tốt hoặc OK, không bài nào kém.
- Từ tháng 7 đã thêm node `Corporation` và schema `WebSite`.

Vấn đề nằm ở **template của site và kho trang cũ**. Đây lại là phần khách hàng và LLM đọc đầu tiên để hiểu "Manifera là ai":

1. **H1 trang chủ vẫn là "Experiences of our clients working with us"**, và trang chủ vẫn chỉ có 1 H2. Cả hai không đổi từ tháng 7.
2. **9 trang quan trọng có `<h1>` rỗng**, trong đó có 4 trang dịch vụ và trang liên hệ. Template của theme xuất ra `<h1></h1>`.
3. **Bài blog bị đánh dấu là `ProfessionalService` thay vì `Article`.** Schema không có tác giả `Person` và không có ngày đăng. Nguyên nhân là plugin *Schema & Structured Data for WP*, plugin này thay thế schema của Yoast. Node `Corporation` có `sameAs: []` và không có địa chỉ.
4. **Các trang trùng vẫn được index**, giống nhau 92-98%:
   - `/contact-us/` = `/contact-us1/`
   - `/services/webshop-development/` ≈ `/services/web-shops-ecommerce-development/`
   - `/about-us/setting-up-your-offshore-team/` ≈ `/about-us/setting-up-your-team/`
5. **Số thứ tự nội bộ lọt vào title và H1**: "04-Blog", "02-Portfolio page", "05-Contact", "06-Privacy Policy", "07-Terms of Service".
6. **Khoảng 600 URL lưu trữ mỏng đang được index.**
   - Có 457 tag, trong đó 263 tag chỉ có 1 bài và 100 tag không có bài nào.
   - 51 trang technology, mỗi trang khoảng 115 từ, không có meta description.
   - `/category/` bị chặn trong `robots.txt`, trong khi `category-sitemap.xml` vẫn khai báo chính các URL đó.
7. **Dữ liệu thực thể cho GEO mỏng và không thống nhất.**
   - Schema không có `sameAs`.
   - Trang About ghi "based in Singapore and Ho Chi Minh City", trong khi tài liệu thương hiệu ghi trụ sở ở Amsterdam.
   - Tìm kiếm không thấy hồ sơ Clutch.
   - **Không có link nào** từ manifera.com sang LaunchStudio.

**Kết luận: 🟡 Nội dung tốt nhưng chạy trên template đã lỗi thời.** Các phát hiện 1-5 là chỉnh template và cài đặt, khoảng 2-3 ngày công dev, nhưng ảnh hưởng tới mọi trang bán hàng.

### Bảng điểm

| Hạng mục | Tình trạng | So với 31/7 |
|---|---|---|
| Khả năng crawl (Google, Bing, bot AI) | 🟢 Cả 25 UA đều trả 200 | = |
| Sitemap | 🟡 Mới, nhưng khai báo taxonomy mỏng và một sitemap category bị robots chặn | ⬇ mới phát hiện |
| On-page trang chủ | 🔴 H1 sai, chỉ 1 H2 | = |
| Trang dịch vụ/landing | 🔴 H1 rỗng trên 9 trang, có trang trùng | ⬇ mới phát hiện |
| Title và meta | 🟠 Title có đánh số, title bài mới dài 78-107 ký tự | ⬇ |
| Schema | 🟠 Đã thêm Corporation + WebSite; bài viết sai loại, không có sameAs | ⬆ một phần |
| Độ sâu nội dung (bài mới) | 🟢 2.100-3.400 từ | ⬆⬆ |
| Độ mới nội dung (bài cũ) | 🟠 Bài sự kiện 2017-2022 và bài "2020" vẫn được index | = |
| E-E-A-T và tác giả | 🟡 Có byline "Duy Le" trong meta, chưa có trong schema | ⬆ |
| Thực thể bên ngoài | 🟡 GoodFirms, ITviec, TopDev, VietnamWorks, KVK, FeaturedCustomers; không thấy Clutch | = |
| llms.txt | 🟠 Danh sách tự sinh, bài cũ nhất đứng đầu, không có tóm tắt công ty | = |
| Hiệu năng (ước lượng) | 🟠 TTFB 0,68-1,27 s; HTML trang chủ 211 KB, 37 script, 12 stylesheet | = |

---

## 2. Tiến độ so với audit ngày 31/7

| # | Lỗi tháng 7 | Tình trạng 19/11 | Bằng chứng |
|---|---|---|---|
| 1 | H1 trang chủ = "Experiences of our clients working with us" | ❌ Chưa sửa | Không đổi |
| 2 | Không có schema Organization / WebSite | 🟡 Sửa một phần | Trang chủ đã có `Corporation` + `WebSite` + `ContactPoint`; `sameAs: []`, không có địa chỉ, không có foundingDate |
| 3 | Trang chủ chỉ có 1 H2 | ❌ Chưa sửa | Vẫn 1 H2 ("Our awards"), 6 H3 |
| 4 | Ảnh trang chủ thiếu alt (12 rỗng, 1 thiếu) | ❌ Chưa sửa | Như cũ: 43 ảnh, 12 `alt=""`, 1 thiếu |
| 5 | `og:image` là logo 225×225 | ❌ Chưa sửa | Trang chủ và 12 trang khác vẫn dùng `Manifera-Software-Outsourcing-logo.png` |
| 6 | Quy tắc `/nl/` cũ trong robots.txt | ❌ Chưa sửa | Không đổi |
| 7 | `/favicon.ico` trả 404 | ❌ Chưa sửa | Vẫn 404 |
| 8 | Chạy Lighthouse | ❌ Chưa làm | Chưa làm (hôm nay cũng bị hết quota API) |

---

## 3. Phát hiện và cách sửa

Mức ưu tiên: **P0** = tuần này, **P1** = tháng này, **P2** = để sau. Công sức: S < 2 giờ, M < 1 ngày, L > 1 ngày.

### F1 (P0, S) - H1 và cấu trúc heading của trang chủ

**Bằng chứng.**

- `<title>`: `Manifera | Experienced, Reliable Software Development Teams`
- `<h1>`: `Experiences of our clients working with us`
- Trang 1.516 từ chỉ có 1 H2 (`Our awards`) và 6 H3.

**Vì sao quan trọng.**

- H1 là tín hiệu on-page mạnh nhất để nói trang này nói về gì. Hiện nay nó nói với Google và các LLM rằng trang chủ là trang testimonial.
- Với chỉ 1 H2, máy không tách được các phần của trang (dịch vụ, mô hình, quy trình, khách hàng).

**Cách sửa (theme `manifera3`, template trang chủ).**

1. Heading của phần hero trở thành `<h1>` duy nhất. Đề xuất: `Dedicated software development teams in Vietnam, managed from Amsterdam`, hoặc sát với title hơn: `Experienced, reliable software development teams`.
2. Đổi heading testimonial thành `<h2>Experiences of our clients working with us</h2>`.
3. Mỗi phần của trang chủ có một `<h2>` thật, ví dụ:
   - "Our services"
   - "How a dedicated team works"
   - "Why Manifera"
   - "Clients and projects"
   - "Awards"
   - "Talk to our Amsterdam team"
4. Kiểm tra: `curl -s https://www.manifera.com/ | grep -o '<h1[^>]*>[^<]*'` phải trả về đúng một H1, không rỗng.

---

### F2 (P0, S) - `<h1>` rỗng trên 9 trang quan trọng

**Bằng chứng.** Mỗi trang dưới đây xuất `<h1></h1>` rỗng; heading hiển thị nằm trong một thẻ khác.

| URL | Title |
|---|---|
| `/services/offshore-software-development/` | Offshore Software Development Teams - Manifera |
| `/services/web-app-develop/` | Web app development - Manifera |
| `/services/mobile-app-development/` | Mobile app development - Manifera |
| `/services/webshop-development/` | Webshop/eCommerce Developments - Manifera |
| `/services/migration-to-nl-euro-cloud/` | Migration to NL/Euro Cloud - Manifera |
| `/services/migration-to-nl-euro-cloud-en/` | Migration to NL/Euro Cloud English - Manifera |
| `/contact-us/` | Contact Us - Manifera |
| `/about-us/manifera-technologies/` | Technologies - Manifera |
| `/about-us/setting-up-your-offshore-team/` | Setting Up Your Offshore Development Team - Manifera |

Đây là những trang xếp hạng và được trích dẫn cho các từ khóa thương mại "offshore software development", "web app development" và "mobile app development".

**Cách sửa.** Các trang này dùng chung một template (thấy qua ảnh OG chung `section9-bg.webp` / `custom-software.webp`). Trong template đó:

- In heading hero của trang vào trong `<h1>`, hoặc
- Xóa `<h1>` rỗng và nâng heading hero lên thành `<h1>`.

H1 đề xuất (giữ tiếng Anh/Hà Lan để dán lên site):

| Trang | H1 |
|---|---|
| offshore-software-development | `Offshore software development teams in Vietnam` |
| web-app-develop | `Custom web application development` |
| mobile-app-development | `Native and cross-platform mobile app development` |
| webshop-development | `Webshop and eCommerce development` |
| migration (NL) | `Migratie naar een Nederlandse of Europese cloud` |
| migration (EN) | `Migration to a Dutch or European cloud` |
| contact-us | `Contact Manifera` |
| manifera-technologies | `Technologies we work with` |

---

### F3 (P0, S) - Trang trùng, tất cả đều được index

**Bằng chứng.** Độ giống nhau của nội dung chính, đo theo chuỗi từ:

| Giữ lại | Trang trùng | Độ giống | Ghi chú |
|---|---|---|---|
| `/contact-us/` | `/contact-us1/` (title "Manifera 05-Contact - Manifera Software Company") | **98%** | Bản cũ vẫn để xuất bản |
| `/services/webshop-development/` | `/services/web-shops-ecommerce-development/` (sửa lần cuối năm 2022) | **92%** | Cùng nội dung H1 |
| `/about-us/setting-up-your-offshore-team/` | `/about-us/setting-up-your-team/` (H1 "Setting Up Your Offshore Development Team") | **97%** | Cùng nội dung H1 |

Tất cả đều trả 200, tự canonical về chính mình và có trong `page-sitemap.xml`.

**Ăn thịt từ khóa lẫn nhau** (nội dung khác nhau nhưng cùng ý định tìm kiếm):

- `/remote/` (title `Remote - Manifera`, 17 ký tự, H1 nói về lập trình viên front-end từ xa) với `/remote/frontend-developer/`.
- `/remote/developer/` với `/remote/developer-unlock-excellence-with-manifera/`.

**Cách sửa.**

1. Thêm redirect 301 bằng plugin **Redirection** (đã bật sẵn):
   ```
   /contact-us1/                                   -> /contact-us/                              301
   /services/web-shops-ecommerce-development/      -> /services/webshop-development/            301
   /about-us/setting-up-your-team/                 -> /about-us/setting-up-your-offshore-team/  301
   /remote/developer-unlock-excellence-with-manifera/ -> /remote/developer/                     301
   ```
2. Chuyển các trang nguồn vào thùng rác để chúng ra khỏi sitemap.
3. Biến `/remote/` thành trang trung tâm ("Remote developers and teams from Vietnam"), link tới `/remote/developer/`, `/remote/frontend-developer/` và `/remote/team/`. Đặt title đúng nghĩa, ví dụ `Remote Developers and Teams from Vietnam | Manifera` (50 ký tự).

---

### F4 (P0, S) - Nhãn đánh số nội bộ trong title và H1

| URL | Title hiện tại | H1 hiện tại | Title đề xuất (≤ 60) |
|---|---|---|---|
| `/blog/` | `Checking out new 04-Blog Posts here - Manifera Software Company` | Our insightful blog | `Software Development Blog: Guides for CTOs \| Manifera` |
| `/portfolio/` | `Our partners and clients - 02-Portfolio page - Manifera clients` | Some of our successful projects | `Portfolio: Software Projects We Delivered \| Manifera` |
| `/privacy-policy/` | `06-Privacy Policy - Manifera Offshore Software Development Service` | **06-Privacy Policy** | `Privacy Policy \| Manifera` (H1 `Privacy Policy`) |
| `/terms-of-service/` | `07-Terms of Service - Manifera Offshore Custom Software Development Service` | **07-Terms of Service** | `Terms of Service \| Manifera` (H1 `Terms of Service`) |
| `/about-us/careers/job-application/` | `Apply Jobs - Manifera` | Job Application | thêm meta description; cân nhắc `noindex` |
| `/about-us/` | `About Our Company - Manifera Offshore Custom Software Service` | **Who we are?** | `About Manifera: Dutch-Managed Software Teams Since 2014` (H1 `About Manifera`) |

Các con số này có vẻ là tiền tố sắp xếp trang được gõ thẳng vào tên trang trong WordPress. Đổi tên trang trong WP admin và đặt SEO title trong Yoast.

---

### F5 (P0, M) - Schema bài viết sai loại; `sameAs` của tổ chức để trống

**Bằng chứng.**

- Site đang chạy plugin **Schema & Structured Data for WP & AMP** (v1.69). Schema graph của Yoast không được xuất; trang chủ chỉ có một khối JSON-LD của plugin này.
- **Bài viết:** `BreadcrumbList`, `ProfessionalService`, `ImageObject`. Mỗi bài được khai báo là "một ProfessionalService tên Manifera". Không có `Article`/`BlogPosting`, không có `author` Person, không có `datePublished`/`dateModified` trong schema. Ngày tháng chỉ có ở meta `article:published_time`.
- **`Corporation` trên trang chủ:** có `name`, `url`, `logo`, `contactPoint` (+31619701001, sales). `sameAs: []` để trống. Không có `address`, `foundingDate`, `founder`, `numberOfEmployees`, `areaServed`.
- **`/about-us/` và `/contact-us/`:** có một node `Organization` riêng.
- **FAQPage** chỉ có trên 5 trang `/remote/`. Bài mới có phần FAQ bằng HTML thường, không có markup.

**Vì sao quan trọng.**

- Google dùng `Article` + `author` + ngày tháng để hiểu bài viết và xét điều kiện vào Top Stories/Discover.
- LLM dùng các trường này để đánh giá độ mới và tác giả.
- Gọi mọi bài viết là `ProfessionalService` là sai nghĩa, và lặp thực thể công ty 347 lần.
- `sameAs` trống bỏ phí tài sản thật của Manifera là các hồ sơ bên thứ ba.

**Cách sửa (trong SASWP, Structured Data → Schema Types).**

1. Sửa loại schema đang áp cho "Post Type = post": đổi `ProfessionalService` thành **BlogPosting**. Gán:
   - `headline` = title bài
   - `author` = tác giả bài (Person)
   - `datePublished` / `dateModified`
   - `image` = ảnh đại diện
   - `publisher` = tổ chức
2. Chỉ áp `ProfessionalService` (hoặc `LocalBusiness`) cho `/contact-us/` và trang chủ.
3. Trong SASWP → Settings → Knowledge Graph:
   - Đặt loại tổ chức (`Organization` hoặc `Corporation`) và logo (tối thiểu 112×112, nên vuông).
   - Thêm `sameAs` gồm các hồ sơ thật: Facebook (`https://www.facebook.com/manifera`), trang LinkedIn công ty, GoodFirms (`https://www.goodfirms.co/company/manifera`), ITviec (`https://itviec.com/companies/manifera-software-development`), FeaturedCustomers (`https://www.featuredcustomers.com/vendor/manifera`), kênh YouTube, và Clutch nếu hồ sơ còn tồn tại.
   - Thêm địa chỉ (Herengracht 420, Amsterdam, NL, theo `manifera_info.md`), `foundingDate` 2014, founder Herre Roelevink kèm LinkedIn.
4. Bật schema FAQ của SASWP cho bài viết, hoặc thêm FAQPage cho bài có FAQ hiển thị. Từ năm 2023, Google chỉ hiện rich result FAQ cho site chính phủ/y tế, nên việc này phục vụ LLM và Bing.
5. Kiểm tra 3 bài bằng Rich Results Test của Google.

Phương án khác: tắt SASWP và để Yoast xuất graph (Yoast → Settings → Site representation). Chỉ chọn một; không bao giờ chạy cả hai.

---

### F6 (P1, S) - Title và description bài mới bị cắt

**Bằng chứng.** 8 bài mới nhất có title 78-107 ký tự và meta description 150-233 ký tự, trong khi Google chỉ hiện khoảng 60 ký tự title và 155 ký tự description. Một số title mở đầu bằng câu gây tò mò thay vì từ khóa.

| Bài (slug) | Ký tự title | Ký tự desc | SEO title đề xuất (≤ 60, từ khóa đứng đầu) |
|---|---|---|---|
| `cheapest-software-development-quote-risk` | 107 | 201 | `Cheapest Software Development Quote: The Hidden Risk` (52) |
| `custom-software-development-cost-breakdown` | 95 | 199 | `Custom Software Development Cost Breakdown (2026)` (49) |
| `mobile-app-development-cost-2026` | 98 | 178 | `Mobile App Development Cost 2026: The Full Breakdown` (52) |
| `evaluate-custom-software-development-company` | 85 | 150 | `How to Evaluate a Custom Software Development Company` (53) |
| `offshore-web-development-company` | 91 | 227 | `Offshore Web Development Company: 3 Warning Signs` (49) |
| `mobile-app-and-web-development-company` | 94 | 233 | `Mobile and Web App Development With React Native Web` (52) |
| `full-stack-web-application` | 89 | 208 | `Full Stack Web Application Scaling: 3 DB Bottlenecks` (52) |
| `ai-software-development-vendors-comparison` | 78 | 151 | `AI Software Development Vendors: Track Records Compared` (55) |

**Cách sửa.**

- Giữ H1 dài kiểu biên tập. Đặt bản ngắn vào trường **SEO title** của Yoast và cắt meta description xuống ≤ 155 ký tự.
- Thêm quy tắc này vào quy trình upload bài: mỗi bài mới có SEO title ≤ 60 và meta description ≤ 155.

**Focus keyphrase trong Yoast:** 3 trong 40 bài gần đây dùng nguyên cụm `Software Development` và 2 bài dùng `Mobile App Development`. Các bài này cạnh tranh với nhau và với các trang dịch vụ. Hãy cho mỗi bài một keyphrase dài riêng, còn các từ khóa chính để dành cho trang dịch vụ.

---

### F7 (P1, M) - Khoảng 600 URL lưu trữ mỏng được index; xung đột robots và sitemap

**Bằng chứng.**

| Taxonomy | Số URL trong sitemap | Vấn đề |
|---|---|---|
| Tag | 357 trong sitemap; có 457 tag, **263 tag có 1 bài, 100 tag không có bài** | Được index (`index, follow`), không có nội dung riêng |
| Technology (`/technology/…`) | 51 | Khoảng 115 từ mỗi trang, không có meta description (ví dụ `/technology/android/`) |
| Category testimonial | 13 | Mỏng |
| Category portfolio / job | 4 + 4 | Mỏng |
| Category | 8 | **Bị chặn bởi `Disallow: /category/` trong robots.txt, nhưng vẫn khai báo trong `category-sitemap.xml`** |

**Cách sửa.**

1. Trong Yoast → Settings → Taxonomies:
   - Tag = không hiện trong kết quả tìm kiếm.
   - Category testimonial, category portfolio và category job = không hiện trong kết quả tìm kiếm.
2. Trang technology, chọn một trong hai:
   - Làm dày 10-15 trang khớp với dịch vụ (React, .NET, Node.js, Flutter, Laravel...) lên 400+ từ, có meta description và link tới dự án.
   - Hoặc noindex toàn bộ loại trang này.
3. Category, chọn một trong hai:
   - Bỏ `Disallow: /category/` (khuyến nghị: category là trang trung tâm hữu ích; mỗi category thêm đoạn giới thiệu 150-300 từ).
   - Hoặc giữ chặn và bỏ category khỏi sitemap.

   Không bao giờ vừa chặn vừa khai báo trong sitemap.
4. Trong quy trình upload, ngừng tự tạo một tag mới cho mỗi bài.

---

### F8 (P1, M) - Nội dung cũ có năm tháng vẫn được index và đứng đầu llms.txt

**Bằng chứng.**

- Ít nhất 13 bài trong `llms.txt` có năm 2017-2022 trong title, ví dụ:
  - `4 Best eCommerce platforms to choose in 2020`
  - `B2B vs. B2C E-Commerce: Trends & Insights for 2020`
  - `Comparison between B2B and B2C eCommerce and Trends for 2020`
  - `[Web development languages 2022] ...`
  - `Fireside Chat Event in Singapore on 8 July 2019`
  - `Manifera trip in Nha Trang 2017`
  - `Thank You To Everyone Who Joined Us At Our Christmas 2018 Event!`
- `llms.txt` xếp theo bảng chữ cái, nên `.Net Core: Things You Need To Know (2021)` và các bài năm 2020 là những gì LLM đọc đầu tiên.

**Cách sửa.**

| Loại bài | Việc cần làm |
|---|---|
| Hai bài B2B/B2C năm 2020 gần như giống nhau | Gộp thành một bài cập nhật 2026; 301 bài còn lại |
| Bài "Best X in 2020/2022" vẫn có người tìm | Cập nhật nội dung và title lên 2026, giữ nguyên URL |
| Bài du lịch công ty, Giáng sinh, sự kiện 2018-2020 | Giữ cho phần văn hóa nhưng đặt `noindex`, hoặc chuyển về một trang "Life at Manifera" |
| Mọi bài khác trước 2023 | Xem trong GSC: không có click trong 12 tháng và không có backlink thì noindex hoặc gộp |

---

### F9 (P1, S) - GEO: llms.txt không có phần tóm tắt công ty

**Bằng chứng.**

- File do plugin **LLMS Full TXT Generator** (2.1.2) tạo.
- Phần đầu chỉ có khẩu hiệu WordPress ("Offshore Software Development Team - Custom Software Development") và `Contact: vu@manifera.com`, tiếp theo là hơn 300 link bài xếp theo bảng chữ cái.
- `llms-full.txt` nặng 3,0 MB.

**Cách sửa.** Thêm phần đầu do mình biên soạn, hoặc dùng một file `llms.txt` tĩnh và vẫn để plugin tạo file full. Chỉ dùng thông tin site đã công bố, và dùng email chung thay cho email cá nhân. Mẫu giữ tiếng Anh vì LLM sẽ đọc trực tiếp:

```markdown
# Manifera

> Manifera is a Dutch-managed software development company founded in 2014 by Herre Roelevink. Headquarters in Amsterdam (Herengracht 420), engineering centre in Ho Chi Minh City, Vietnam, office in Singapore. We build custom web, mobile and cloud software and provide dedicated offshore development teams for European companies.

## Services
- [Offshore software development teams](https://www.manifera.com/services/offshore-software-development/)
- [Custom software development](https://www.manifera.com/services/custom-software-development/)
- [Web app development](https://www.manifera.com/services/web-app-develop/)
- [Mobile app development](https://www.manifera.com/services/mobile-app-development/)
- [Migration to a Dutch/European cloud](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/)
- [Remote developers](https://www.manifera.com/remote/)
- [AI prototype to production: LaunchStudio](https://launchstudio.eu/en/)

## Company
- [About](https://www.manifera.com/about-us/) · [Way of working](https://www.manifera.com/about-us/our-way-of-working/) · [Portfolio](https://www.manifera.com/portfolio/) · [Contact](https://www.manifera.com/contact-us/)

## Cornerstone guides (2026)
- (10-15 newest buyer guides: cost, vendor evaluation, offshore teams, AI vendors)
```

Sau đó, nếu plugin cho phép, sắp danh sách bài theo thứ tự mới nhất trước hoặc theo nhóm chủ đề. Cập nhật plugin lên 2.1.3.

---

### F10 (P1, M) - GEO: thông tin thực thể không thống nhất, thiếu nguồn xác nhận

**Bằng chứng.**

- **Địa điểm ghi không thống nhất giữa các nguồn:**
  - Meta description của `/about-us/` ghi "based in Singapore and Ho Chi Minh City".
  - Schema `Corporation` không có địa chỉ.
  - `manifera_info.md` ghi Amsterdam (Herengracht 420) là trụ sở châu Âu.
  - Sổ đăng ký KVK của Hà Lan ghi *Manifera Software Development*, KVK 83156135, trụ sở đăng ký ở Amsterdam, ngày đăng ký năm 2021 ([liza.nl](https://www.liza.nl/en/83156135/manifera-software-development)).
  - Các trang tuyển dụng ghi "Singapore and HCMC" ([ITviec](https://itviec.com/companies/manifera-software-development)) hoặc "Vietnam, Singapore and the Netherlands".
- **Hồ sơ bên thứ ba tìm thấy ngày 19/11:**
  - [GoodFirms](https://www.goodfirms.co/company/manifera)
  - [ITviec](https://itviec.com/companies/manifera-software-development)
  - [TopDev](https://topdev.vn/companies/manifera-software-development-79865)
  - [VietnamWorks](https://www.vietnamworks.com/nha-tuyen-dung/manifera-software-development-c182942)
  - [FeaturedCustomers](https://www.featuredcustomers.com/vendor/manifera)
  - [Danh sách thành viên ADB DutchCham Singapore](https://adb-dutchcham.sg/members-directories/corporate-members/page/4)
  - **Không thấy hồ sơ Clutch trong kết quả tìm kiếm.** Audit tháng 7 có liệt kê Clutch, nên cần kiểm tra hồ sơ đó còn tồn tại và còn được link không.
- **manifera.com link sang LaunchStudio từ 0 trên 36 trang đã crawl.** Ngược lại, LaunchStudio có link về Manifera ở footer và trong bài viết.

**Vì sao quan trọng.** Công cụ trả lời AI đối chiếu thông tin công ty giữa website, schema và các danh bạ. Khi các nguồn mâu thuẫn, trợ lý AI trả lời dè dặt hoặc bỏ qua công ty. Năm thành lập, thành phố trụ sở, quy mô và dịch vụ phải giống nhau ở mọi nơi.

**Cách sửa.**

1. Soạn một "bảng thông tin thực thể" chuẩn, rồi áp dụng cho trang About, schema `Corporation`, llms.txt, LinkedIn, GoodFirms, Clutch, ITviec và Google Business Profile. Bảng gồm:
   - tên pháp lý
   - năm thành lập (2014)
   - người sáng lập
   - trụ sở (Amsterdam), trung tâm kỹ thuật (TP.HCM) và văn phòng Singapore
   - khoảng quy mô nhân sự
   - 5 dịch vụ chính
   - 3 khách hàng/dự án tiêu biểu được phép nêu tên
2. Viết lại meta description của `/about-us/` để có Amsterdam.
3. Nhận hoặc làm mới hồ sơ Clutch, và nhờ 3-5 khách hàng viết review. Clutch là danh bạ LLM hay trích dẫn nhất cho các danh sách "best offshore development company".
4. Thêm nhắc tên và link LaunchStudio trên `/services/` và `/about-us/`, ví dụ "Built an app with AI tools? Our LaunchStudio service takes it to production". Thêm `subOrganization` → LaunchStudio trong schema. Việc này củng cố cả hai thực thể.

---

### F11 (P1, S) - Trang tiếng Hà Lan trên site tiếng Anh; alt text là tên file ảnh chụp màn hình

**Bằng chứng.**

- `/services/migration-to-nl-euro-cloud/` viết bằng tiếng Hà Lan ("Migratie naar Nederlandse/Europese Cloud"), nhưng:
  - title bằng tiếng Anh
  - trang khai báo `lang="en-US"`
  - không có hreflang trỏ tới bản tiếng Anh `/services/migration-to-nl-euro-cloud-en/`
- Cả hai trang dùng alt text kiểu `Screenshot from 2025-05-14 10-59-54` và có 2 ảnh base64 nhúng thẳng.

**Cách sửa.**

1. Trên trang tiếng Hà Lan:
   - đặt `lang="nl-NL"`, ví dụ bằng một trường ngôn ngữ riêng cho từng trang trong template
   - đặt title tiếng Hà Lan: `Migratie naar Nederlandse of Europese cloud | Manifera`
   - thêm `<link rel="alternate" hreflang="nl">` / `hreflang="en"` hai chiều giữa hai trang
2. Nếu được, làm slug EN gọn hơn: `/services/cloud-migration-netherlands-eu/`, kèm 301.
3. Thay alt text bằng mô tả nội dung thật của từng ảnh chụp màn hình.

---

### F12 (P1, S) - Ảnh mạng xã hội và alt text

**Bằng chứng.**

- `og:image` là logo 225×225 trên trang chủ, `/blog/`, `/portfolio/`, `/services/`, `/remote/*`, `/privacy-policy/` và nhiều trang khác.
- Các template khác dùng ảnh nền (`section9-bg.webp`) hoặc một **icon** (`arrow-right-alt.svg` trên `/services/offshore-software-development/`) làm ảnh chia sẻ.
- Số ảnh alt rỗng:
  - trang chủ: 12/43
  - `/services/web-app-develop/`: 34/55
  - `/services/mobile-app-development/`: 16/35
  - `/remote/developer-unlock-excellence-with-manifera/`: 14/30
  - `/services/webshop-development/`: 12/33

**Cách sửa.**

- Tạo một ảnh chia sẻ mặc định 1200×630 (logo + "Software development teams, Amsterdam & Vietnam") và đặt trong Yoast → Settings → Site basics.
- Tạo một ảnh riêng cho mỗi trang dịch vụ.
- Logo và huy hiệu dùng `alt="<Tên khách hàng> logo"` hoặc `alt="<Tên giải thưởng> badge"`. Hình trang trí giữ `alt=""`.

---

### F13 (P2, M) - Hiệu năng, robots.txt và các việc dọn dẹp

| Hạng mục | Bằng chứng | Cách sửa |
|---|---|---|
| TTFB | 0,68-1,27 s (trang chủ 1,27 s, `/portfolio/` 1,20 s) | Page cache + CDN; mục tiêu < 0,3 s |
| Dung lượng trang | HTML trang chủ 211 KB, 37 `<script>`, 12 stylesheet; trang dịch vụ 164-246 KB HTML | Rà output của Visual Composer + Smart Slider trên các template không cần dùng; hoãn tải JS không quan trọng |
| Core Web Vitals | Chưa đo (hết quota PSI) | Chạy PageSpeed Insights cho `/`, 3 trang dịch vụ, 1 bài; ghi kết quả vào đây |
| robots.txt | Vẫn chặn `/nl/how-to-choose-a-custom-software-company/` (301) và `/nl/in-house-vs-outsourcing-software-development-2/` (404) | Xóa cả hai dòng; xử lý `/category/` (F7) |
| `/favicon.ico` | 404 | Tải lên favicon.ico ở thư mục gốc |
| PHP | 8.2.35; Contact Form 7 6.2.5 cần PHP 8.3 | Lên kế hoạch nâng lên PHP 8.3 (bản vá bảo mật của plugin form chính đang bị chặn) |
| Plugin cũ | Yoast 28.8 → 28.9, SASWP 1.69 → 1.70, ACF, UpdraftPlus, WP Mail SMTP, Easy MCP AI 2.3.2 → 2.4.1 | Cập nhật sau khi backup |
| Trang nộp đơn tuyển dụng | Không có meta description, mỏng (197 từ) | `noindex` |

---

## 4. Điểm nội dung Yoast (40 bài sửa gần nhất)

- **Điểm SEO:** 23 tốt, 17 OK, 0 kém.
- **Điểm yếu:**
  - Các keyphrase chung chung đã nêu ở F6 (`Software Development` ×3, `Mobile App Development` ×2, `Outsourcing`, `development software`).
  - Keyphrase thường không nằm ở đầu SEO title, vì SEO title đang giống H1 dài.

---

## 5. KPI và cách đo

| KPI | Mốc hiện tại (19/11) | Mục tiêu đến 28/02/2027 | Đo ở đâu |
|---|---|---|---|
| Trang có đúng 1 H1 không rỗng (page-sitemap) | 18/28 | 28/28 | crawl |
| Trang trùng được index | 4 | 0 | `page-sitemap.xml` |
| Title có tiền tố đánh số | 5 | 0 | crawl |
| Bài có `BlogPosting` + tác giả + ngày trong schema | 0/347 | 347/347 | Rich Results Test trên 3 bài mẫu |
| Số mục `sameAs` trong schema tổ chức | 0 | ≥ 6 | JSON-LD trang chủ |
| Trang lưu trữ mỏng được index (tag, technology, category testimonial) | khoảng 430 | dưới 30 | sitemap |
| Trang manifera.com có link sang launchstudio.eu | 0 | ≥ 3 (services, about, footer) | crawl |
| Phiên truy cập từ AI (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai) | đo ngay bây giờ | +100% so với tháng 12 | GA4, regex session source `chatgpt\|perplexity\|gemini\|copilot\|claude` |
| Độ chính xác khi AI trả lời về thương hiệu (bộ câu hỏi) | đo ngay bây giờ | ≥ 7/10 câu đúng | test thủ công hằng tháng |
| Click GSC vào `/services/*` | đo ngay bây giờ | +30% | Search Console |

**Bộ câu hỏi test GEO hằng tháng.** Hỏi từng câu trong ChatGPT, Perplexity và Gemini. Ghi lại Manifera có được nhắc tên không, và địa điểm, năm thành lập, dịch vụ có được mô tả đúng không. Giữ nguyên câu hỏi tiếng Anh vì đó là ngôn ngữ khách hàng sẽ hỏi.

1. What is Manifera (manifera.com)?
2. Best offshore software development companies in Vietnam for Dutch companies
3. Dutch-managed software development team in Vietnam
4. How much does a dedicated development team in Vietnam cost?
5. Software development company Amsterdam with offshore team
6. Who founded Manifera and where is it based?
7. Alternatives to hiring in-house developers in the Netherlands
8. Custom software development company for European SMEs with fixed teams
9. Migrate my application to a Dutch or European cloud provider
10. Manifera reviews

---

## 6. Kế hoạch hành động

| Thời gian | Việc cần làm | Phát hiện | Người làm | Công sức |
|---|---|---|---|---|
| Tuần 19/11 | H1 + cấu trúc H2 trang chủ | F1 | Dev | S |
| Tuần 19/11 | Sửa H1 rỗng trong template trang dịch vụ | F2 | Dev | S |
| Tuần 19/11 | 4 redirect, xóa trang trùng | F3 | Content | S |
| Tuần 19/11 | Đổi tên title/H1 có đánh số | F4 | Content | S |
| Tuần 24/11 | SASWP: BlogPosting cho bài viết, sameAs, địa chỉ, founder | F5 | Dev | M |
| Tuần 24/11 | SEO title ≤ 60 / description ≤ 155 cho 8 bài mới nhất; thêm quy tắc vào quy trình upload | F6 | Content | S |
| Tuần 24/11 | Noindex tag và taxonomy mỏng; xử lý xung đột `/category/` | F7 | Content | S |
| Tuần 1/12 | Phần đầu llms.txt do mình biên soạn | F9 | Content | S |
| Tuần 1/12 | Bảng thông tin thực thể; meta About; link từ Manifera sang LaunchStudio | F10 | Marketing | M |
| Tuần 1/12 | Lang/hreflang cho trang cloud tiếng Hà Lan, alt text | F11 | Dev | S |
| Tháng 12 | Ảnh chia sẻ, alt text trên trang dịch vụ | F12 | Design/content | M |
| Tháng 12 | Rà bài cũ: gộp, cập nhật, noindex | F8 | Content | L |
| Tháng 12 | Nhận/làm mới hồ sơ Clutch; review của khách hàng | F10 | Marketing | L |
| Tháng 1/2027 | PHP 8.3, cache/CDN, đo mốc PageSpeed | F13 | Quản trị server | M |
| Hằng tháng | Test câu hỏi GEO + cập nhật bảng KPI | 5 | Marketing | S |

---

## Phụ lục A - Dữ liệu thô

**Hạ tầng**

- IP 136.243.57.57 (dùng chung với launchstudio.eu); DNS ở DigitalOcean.
- HTTP/1.1 có quảng bá h3; HSTS preload.
- WordPress 7.1.4, PHP 8.2.35, theme `manifera3`.
- 24 plugin đang bật, trong đó có Yoast 28.8, Schema & Structured Data for WP 1.69, Visual Composer, Smart Slider 3, Redirection, Wordfence, Site Kit, LLMS Full TXT Generator.

**Quyền truy cập của crawler AI (tất cả trả 200):**

- OpenAI: GPTBot, OAI-SearchBot, ChatGPT-User
- Anthropic: ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai
- Perplexity: PerplexityBot, Perplexity-User
- Google: Google-Extended, Googlebot
- Khác: bingbot, Applebot(-Extended), CCBot, meta-externalagent, Amazonbot, Bytespider, cohere-ai, DuckAssistBot, MistralAI-User

**Sitemap (19/11)**

| Sitemap | Số URL | Sửa lần cuối |
|---|---|---|
| post | 347 | 2026-11-18 |
| page | 28 | 2026-10-07 |
| dt_portfolio | 27 | 2026-06-08 |
| dt_job | 2 | 2026-10-12 |
| dt_testimonial | 13 | 2026-06-02 |
| dt_technology | 51 | 2025-02-10 |
| category | 8 | 2026-11-18 (bị chặn trong robots.txt) |
| post_tag | 357 | 2026-11-18 |
| dt_portfolio_category | 4 | 2026-06-08 |
| dt_job_category | 4 | 2026-10-12 |
| dt_testimonial_category | 13 | 2026-06-02 |
| author | 3 | 2026-05-07 |

**Lastmod của bài theo tháng:** T1: 1, T5: 86, T6: 83, T7: 33, T8: 28, T9: 24, T10: 17, T11: 24. Trạng thái bài: 347 đã xuất bản, 3 riêng tư.

**Tóm tắt on-page của page-sitemap**

| URL | Ký tự title | H1 | H2 | Số từ | Schema (loại chính) |
|---|---|---|---|---|---|
| `/` | 59 | Experiences of our clients working with us | 1 | 1.516 | Corporation, WebSite, VideoObject |
| `/about-us/` | 61 | Who we are? | 5 | 754 | AboutPage, Organization |
| `/about-us/careers/` | 75 | 3 H1 (Join us; Your future - Our values; Our efficient recruitment process) | 2 | 413 | Breadcrumb |
| `/about-us/our-way-of-working/` | 69 | Our Way Of Working | 4 | 1.396 | Breadcrumb |
| `/services/` | 58 | Our software development services | 5 | 470 | Breadcrumb |
| `/services/custom-software-development/` | 61 | Custom-made software development services | 3 | 710 | Breadcrumb |
| `/services/offshore-software-development/` | 46 | (rỗng) | 5 | 873 | Breadcrumb |
| `/services/web-app-develop/` | 30 | (rỗng) | 4 | 856 | Breadcrumb |
| `/services/mobile-app-development/` | 33 | (rỗng) | 4 | 784 | VideoObject |
| `/remote/` | 17 | Elevate with Manifera's Skilled Remote Front-End Developers | 10 | 1.620 | FAQPage |
| `/portfolio/` | 63 | Some of our successful projects | 0 | 957 | Breadcrumb |
| `/contact-us/` | 21 | (rỗng) | 1 | 722 | ContactPage, Organization |

`/about-us/careers/` có 3 H1. Giữ một ("Careers at Manifera") và đổi các H1 còn lại thành H2.

**Lệnh test crawler đã dùng:** `curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; <UA>)" <url>`
