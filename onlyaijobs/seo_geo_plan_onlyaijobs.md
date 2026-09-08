# 🧭 SEO & GEO Plan — OnlyAIJobs.eu
## Job board chuyên ngành AI · 🇬🇧 English ⟷ 🇳🇱 Nederlands · 08/09/2026

> **Sources**: [`seo-geo-audit-onlyaijobs-eu-2026-09-08.md`](./seo-geo-audit-onlyaijobs-eu-2026-09-08.md) · [`onlyaijobs_info.md`](./onlyaijobs_info.md) · quét trực tiếp site ngày 08/09/2026
> **Companion**: [`paid_ads_plan.md`](./paid_ads_plan.md) · [`implementation_plan.md`](./implementation_plan.md) · [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md)
> **⚠️ Không có dữ liệu Keyword Planner cho onlyaijobs.eu.** Khác với Manifera và LaunchStudio (đều có file CSV volume thật), OnlyAIJobs chưa từng chạy nghiên cứu từ khóa. Mọi ô volume trong tài liệu này ghi `TBD` — **không được điền số ước đoán vào**. Cách lấy dữ liệu: §3.4.

---

## 📑 Mục lục

1. [Vì sao kế hoạch này bắt đầu bằng kỹ thuật, không phải nội dung](#1)
2. [Google Jobs — cơ hội lớn nhất và điều kiện để có nó](#2)
3. [Kiến trúc từ khóa song ngữ](#3)
4. [Kiến trúc site — programmatic SEO cho job board](#4)
5. [Chiến lược song ngữ EN/NL](#5)
6. [GEO — lợi thế bất ngờ mà OnlyAIJobs đang có](#6)
7. [Kế hoạch blog từ con số 0](#7)
8. [Liên kết nội bộ](#8)
9. [Lịch 90 ngày theo cổng chặn](#9)
10. [KPI](#10)
11. [Rủi ro](#11)
12. [Quyết định cần chốt](#12)

---

<a name="1"></a>
## 1. ⚠️ Vì Sao Kế Hoạch Này Bắt Đầu Bằng Kỹ Thuật, Không Phải Nội Dung

Với Manifera, bài toán là "có 1.460 bài nhưng chưa đăng". Với OnlyAIJobs, bài toán khác hẳn: **site hiện không thể xếp hạng cho bất cứ thứ gì, và sẽ không thể, kể cả khi viết 1.000 bài blog.**

Bốn rào chắn xếp chồng lên nhau:

| Rào chắn | Hệ quả | Nếu chỉ sửa cái này thì sao? |
|---|---|---|
| **1. WAF chặn Googlebot** (39 ngày) | Google chưa từng tải được một byte nào | Gỡ xong vẫn kẹt ở rào 2 |
| **2. Không có URL riêng cho từng việc làm** | Không có gì để index theo vị trí tuyển dụng | Có URL rồi vẫn kẹt ở rào 3 |
| **3. Không có `JobPosting` schema** | Không đủ điều kiện vào Google Jobs — bề mặt quan trọng nhất của ngành | Có schema rồi vẫn kẹt ở rào 4 |
| **4. Phân trang canonical về trang 1** | 42/52 tin bị loại khỏi chỉ mục | |

**Bốn rào này phải được gỡ theo đúng thứ tự.** Viết blog trước khi gỡ chúng là đổ nội dung vào một cái hố kín.

**🇻🇳 Nói thẳng**: nếu chỉ làm được một việc trong quý này, hãy làm §2. Mọi thứ khác trong tài liệu này đều xếp sau nó.

### 1.1 Kế hoạch này gồm những gì

| Không phải | Mà là |
|---|---|
| Viết 200 bài blog ngay | Gỡ 4 rào chắn, rồi sinh trang tự động từ chính dữ liệu việc làm |
| Đuổi theo từ khóa "AI jobs" (đấu với LinkedIn/Indeed) | Chiếm từ khóa dài dạng `<vai trò> + <thành phố>` mà site có dữ liệu thật |
| Làm SEO trước, dựng nguồn tin sau | Nguồn tin **là** nội dung SEO của job board |
| Bỏ qua các bot AI | Khai thác việc GPTBot/ClaudeBot đang là bot duy nhất vào được site |

---

<a name="2"></a>
## 2. 🎯 Google Jobs — Cơ Hội Lớn Nhất

Với truy vấn dạng "machine learning engineer vacatures Eindhoven", Google hiển thị widget Google Jobs chiếm gần trọn màn hình đầu. Kết quả xanh truyền thống bị đẩy xuống dưới. **Job board không có mặt trong widget đó thì gần như không tồn tại.**

Điều kiện vào Google Jobs — hiện OnlyAIJobs **không đạt điều nào**:

| Yêu cầu | Hiện trạng | Việc phải làm |
|---|---|---|
| Mỗi việc làm có URL riêng, index được | ❌ Không có | Sinh `/jobs/<company>-<role>-<city>` |
| `JobPosting` schema hợp lệ trên URL đó | ❌ Không có khối nào | Xem bảng trường bắt buộc bên dưới |
| Googlebot truy cập được | ❌ Bị WAF chặn | Allow-list theo reverse-DNS |
| Có `datePosted` và `validThrough` | ❌ Chỉ hiển thị "1 month ago" | Lưu và xuất ngày thật |
| Tin còn hiệu lực | ⚠️ 100% tin đã 1 tháng tuổi | Quy trình gỡ/làm mới tin |
| Sitemap có URL từng việc làm | ❌ Sitemap chỉ có 9 URL tĩnh | Sinh sitemap động |

### 2.1 Trường `JobPosting` bắt buộc và nên có

```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "AI Engineer",                          // BẮT BUỘC — chỉ chức danh, không kèm tên công ty
  "description": "<p>…</p>",                       // BẮT BUỘC — HTML, đầy đủ, không cắt cụt
  "datePosted": "2026-09-08",                      // BẮT BUỘC
  "validThrough": "2026-11-08T23:59",              // RẤT NÊN — thiếu thì Google tự loại sau 30 ngày
  "employmentType": "FULL_TIME",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "Winparts",
    "sameAs": "https://www.winparts.nl",
    "logo": "https://…"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Winschoterdiep 70",
      "addressLocality": "Groningen",
      "postalCode": "9723 AB",
      "addressCountry": "NL"
    }
  },
  "baseSalary": { … },                             // nếu có — tăng CTR rõ rệt
  "directApply": false                             // vì ứng tuyển diễn ra trên site công ty
}
```

> **🇻🇳 Lợi thế riêng của OnlyAIJobs**: site đã lưu **địa chỉ đường phố chính xác** của từng việc làm (quan sát được trên `/jobs`). Phần lớn job board chỉ có tên thành phố. Trường `jobLocation` đầy đủ tới số nhà là tín hiệu chất lượng mà Google ưu tiên — và đúng là USP sản phẩm cốt lõi. Đây là chỗ dữ liệu sản phẩm và SEO trùng khớp hoàn hảo.

### 2.2 Cảnh báo về `validThrough` và tin cũ

Google loại bỏ `JobPosting` không có `validThrough` sau khoảng 30 ngày, và **phạt uy tín** những site liên tục giữ tin đã hết hạn. Hiện 100% tin trên site đều 1 tháng tuổi. Nếu bật `JobPosting` mà không có quy trình làm mới, site sẽ vào Google Jobs rồi bị đánh giá tiêu cực — tệ hơn là không vào.
👉 **Điều kiện tiên quyết cho §2 là giải quyết nguồn tin** (xem [`implementation_plan.md`](./implementation_plan.md) §4).

---

<a name="3"></a>
## 3. 🔑 Kiến Trúc Từ Khóa Song Ngữ

### 3.1 Nguyên tắc chọn trận

| Đừng đánh | Vì | Đánh cái này |
|---|---|---|
| `ai jobs`, `artificial intelligence jobs` | Đấu trực diện LinkedIn, Indeed, Glassdoor, AI-Jobs.net với 52 tin | `<vai trò> + <thành phố>` — nơi các site lớn có tin nhưng không có trang chuyên biệt |
| `vacatures` (chung) | Indeed NL thống trị tuyệt đối | `ai vacatures <stad>`, `machine learning vacatures <stad>` |
| `jobs in netherlands` | Quá rộng, đa phần là người nước ngoài tìm visa | `ai engineer vacature eindhoven` — ý định địa phương rõ |

### 3.2 Cụm từ khóa 🇬🇧 English

| Cụm | Mẫu từ khóa | Ý định | Trang đích | Volume |
|---|---|---|---|---|
| **A — Vai trò + địa điểm** | `ai engineer jobs amsterdam`, `machine learning jobs eindhoven`, `data scientist jobs utrecht` | Người tìm việc, ý định cao | Trang tự sinh `/jobs/<role>-<city>` | TBD |
| **B — Vai trò (quốc gia)** | `ai engineer jobs netherlands`, `machine learning engineer jobs netherlands` | Người tìm việc | `/jobs/<role>` | TBD |
| **C — Danh mục** | `computer vision jobs`, `generative ai jobs`, `ai ethics jobs`, `robotics engineer jobs` | Duyệt theo chuyên môn | `/jobs/category/<cat>` | TBD |
| **D — Người mới** | `ai internship netherlands`, `junior machine learning jobs`, `ai graduate jobs netherlands` | Persona A | `/jobs/internship`, landing riêng | TBD |
| **E — Hình thức làm việc** | `remote ai jobs europe`, `hybrid machine learning jobs netherlands` | Lọc theo lối sống | `/jobs/remote` | TBD |
| **F — Nhà tuyển dụng** | `post ai job`, `hire ai engineer netherlands`, `where to post ai vacancy` | Persona C | `/pages/info-for-employers` (**hiện rỗng**) | TBD |
| **G — Thông tin/lương** | `ai engineer salary netherlands`, `machine learning salary amsterdam` | TOFU, kéo backlink | Bài blog | TBD |

### 3.3 Cụm từ khóa 🇳🇱 Nederlands — nơi trận đánh thực sự nằm

> 49/52 tin đang ở Hà Lan. Người tìm việc Hà Lan gõ tiếng Hà Lan. **Đây là mặt trận chính, không phải mặt trận phụ.**

| Cụm | Mẫu từ khóa | Trang đích | Volume |
|---|---|---|---|
| **NL-A — Vai trò + stad** | `ai vacatures amsterdam`, `machine learning vacatures eindhoven`, `data scientist vacatures utrecht` | `/nl/vacatures/<rol>-<stad>` | TBD |
| **NL-B — Vai trò (landelijk)** | `ai vacatures nederland`, `ai engineer vacature`, `machine learning vacature` | `/nl/vacatures/<rol>` | TBD |
| **NL-C — Vùng** | `ai vacatures brabant`, `it vacatures noord-brabant`, `ai banen randstad` | Landing vùng — **đúng câu chuyện nguồn gốc của thương hiệu** | TBD |
| **NL-D — Mới ra trường** | `ai stage`, `afstudeerstage machine learning`, `traineeship data science` | `/nl/vacatures/stage` | TBD |
| **NL-E — Nhà tuyển dụng** | `vacature plaatsen ai`, `ai specialist werven`, `vacature plaatsen gratis` | `/nl/pages/info-voor-werkgevers` | TBD |
| **NL-F — Thông tin** | `salaris ai engineer nederland`, `wat verdient een data scientist` | Blog NL | TBD |

**🇻🇳 Lưu ý dịch thuật**: `vacatures` (Hà Lan) ≠ `jobs` (Anh). Người Hà Lan hiếm khi gõ "jobs"; họ gõ "vacatures" hoặc "banen". Bản NL **không được** là bản dịch từng chữ của bản EN — cấu trúc URL, tiêu đề và nội dung phải viết lại theo cách người Hà Lan tìm kiếm.

### 3.4 Cách lấy dữ liệu volume (việc phải làm, tuần 1)

1. Chạy Google Keyword Planner với seed: `ai jobs`, `ai vacatures`, `machine learning vacature`, `data scientist vacature`, filter **Location = Netherlands**, **Language = Dutch** rồi lặp lại với **English**.
2. Xuất riêng cho 20 thành phố lớn nhất NL để biết thành phố nào đáng sinh trang.
3. Đối chiếu Google Trends giữa `ai vacatures` và `ai jobs` trong lãnh thổ NL để xác nhận tỷ lệ ngôn ngữ.
4. Nạp kết quả vào [`google_ads_keywords_onlyaijobs.md`](./google_ads_keywords_onlyaijobs.md) §3 và bảng §3.2–3.3 ở trên.
5. Seed đầy đủ hơn: [`extra-keywords.md`](./extra-keywords.md).

---

<a name="4"></a>
## 4. 🏗️ Kiến Trúc Site — Programmatic SEO

Job board không xếp hạng bằng blog. Nó xếp hạng bằng **trang được sinh tự động từ chính dữ liệu việc làm**. Đây là kiến trúc đề xuất:

```
onlyaijobs.eu
│
├─ /                                   trang chủ (EN)  ·  /nl  trang chủ (NL)
│
├─ /jobs                               tất cả việc làm (đã có)
│   ├─ /jobs/<company>-<role>-<city>   ◄ TRANG CHI TIẾT — chưa tồn tại, ưu tiên #1
│   ├─ /jobs/category/<category>       ◄ 11 danh mục (chỉ sinh khi ≥5 tin)
│   ├─ /jobs/city/<city>               ◄ theo thành phố (chỉ sinh khi ≥3 tin)
│   ├─ /jobs/<role>-<city>             ◄ giao vai trò × thành phố (chỉ sinh khi ≥3 tin)
│   ├─ /jobs/remote                    ◄ theo hình thức
│   └─ /jobs/internship                ◄ theo cấp độ
│
├─ /companies/<company>                ◄ trang thương hiệu nhà tuyển dụng — chưa có, giá trị cao
│
├─ /pages/info-for-employers           ⚠️ HIỆN RỖNG — phải viết
├─ /pages/info-for-job-seekers         ⚠️ HIỆN RỖNG — phải viết
├─ /pages/about-us                     ⚠️ HIỆN RỖNG — phải viết
├─ /pages/pricing                      ◄ chưa tồn tại; cần sau khi chốt mô hình doanh thu
│
├─ /blog                               ⚠️ HIỆN 0 BÀI
│
└─ /nl/…                               toàn bộ cây trên, viết lại bằng tiếng Hà Lan
```

### 4.1 ⚠️ Quy tắc ngưỡng — thứ quyết định thành bại của programmatic SEO

Với **52 tin**, sinh trang bừa bãi sẽ tạo ra hàng trăm trang rỗng và Google sẽ đánh giá toàn site là thin content. Áp dụng nghiêm ngặt:

| Loại trang | Ngưỡng tối thiểu | Khi dưới ngưỡng |
|---|---|---|
| `/jobs/city/<city>` | ≥ 3 tin đang hiệu lực | `noindex`, không đưa vào sitemap, không link tới |
| `/jobs/<role>-<city>` | ≥ 3 tin | như trên |
| `/jobs/category/<cat>` | ≥ 5 tin | như trên — **5/11 danh mục hiện đang rỗng** |
| `/companies/<company>` | ≥ 1 tin + có mô tả công ty | như trên |

**Trang phải tự động chuyển `noindex` khi tin hết hạn khiến nó rơi xuống dưới ngưỡng.** Đây là logic phải viết vào code, không phải việc làm tay.

**🇻🇳 Ước lượng thực tế với 52 tin**: chỉ khoảng 8–12 trang thành phố và 4–5 trang danh mục vượt ngưỡng. Đó là con số đúng để bắt đầu. Số trang chỉ nên tăng khi số tin tăng — **quy mô trang là hàm số của quy mô nguồn cung**, không phải của tham vọng.

### 4.2 Trang chi tiết việc làm — thiết kế

| Thành phần | Nội dung |
|---|---|
| URL | `/jobs/winparts-ai-engineer-groningen` |
| `<title>` | `AI Engineer bij Winparts — Groningen \| OnlyAIJobs` |
| H1 | Chức danh + tên công ty |
| Nội dung | Mô tả đầy đủ, địa chỉ chính xác, **khoảng cách từ vị trí người dùng** (USP), danh mục, loại hình, ngày đăng |
| Schema | `JobPosting` đầy đủ (§2.1) |
| Liên kết ra | Link `nofollow` tới trang tuyển dụng của công ty; link `dofollow` tới `/companies/<company>` và `/jobs/city/<city>` |
| Khi hết hạn | Giữ URL, hiện "Tin này đã đóng", `noindex`, gợi ý 5 tin tương tự — **không xóa URL** (tránh 404 hàng loạt) |

---

<a name="5"></a>
## 5. 🌐 Chiến Lược Song Ngữ EN/NL

### 5.1 Sửa hreflang (lỗi B7 trong audit)

Hiện `/nl` khai đầy đủ nhưng trang EN **không khai `nl`** → Google bỏ qua toàn bộ cụm. Mỗi trang phải khai đủ 3 dòng, đối xứng hai chiều:

```html
<link rel="alternate" hreflang="en" href="https://onlyaijobs.eu/jobs" />
<link rel="alternate" hreflang="nl" href="https://onlyaijobs.eu/nl/vacatures" />
<link rel="alternate" hreflang="x-default" href="https://onlyaijobs.eu/jobs" />
```

Và **đưa toàn bộ URL `/nl` vào sitemap** — hiện không có URL NL nào trong bất kỳ sitemap nào.

### 5.2 Ngôn ngữ nào ưu tiên?

| | English | Nederlands |
|---|---|---|
| Nguồn tin hiện có | 3/52 (Mỹ) | **49/52** |
| Người tìm việc mục tiêu | Kỹ sư quốc tế ở NL, người tìm remote EU | Sinh viên/kỹ sư Hà Lan |
| Cạnh tranh | Rất gắt (LinkedIn, Indeed, AI-Jobs.net toàn cầu) | Nhẹ hơn nhiều ở đuôi dài |
| Khớp với câu chuyện thương hiệu | Yếu (Brabant→Randstad là chuyện Hà Lan) | **Mạnh** |

👉 **Khuyến nghị: ưu tiên tiếng Hà Lan.** Bản EN vẫn duy trì (nhiều kỹ sư AI ở NL là người nước ngoài và tìm bằng tiếng Anh), nhưng ngân sách và nội dung mới nên nghiêng về NL trước. Điều này gắn trực tiếp với quyết định định vị ở [`onlyaijobs_info.md`](./onlyaijobs_info.md) §1.3.

---

<a name="6"></a>
## 6. 🤖 GEO — Lợi Thế Bất Ngờ

Phát hiện quan trọng nhất của audit hôm nay: **GPTBot và ClaudeBot đi qua được WAF và nhận 200, trong khi Googlebot bị chặn.**

Trong khi Google chưa từng thấy site, các mô hình ngôn ngữ **có thể** đã thấy. Nhưng `robots.txt` lại ghi `Disallow: /` cho `User-agent: *` — tức là site đang tự bảo các bot AI đi ra, đúng vào lúc chúng là những bot duy nhất vào được.

### 6.1 Việc phải làm ngay

```
# robots.txt đề xuất
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

User-agent: *
Allow: /
Disallow: /admin
Disallow: /pages/          # cho tới khi các trang này có nội dung thật

Sitemap: https://onlyaijobs.eu/sitemap.xml
```

### 6.2 `llms.txt` thật (hiện URL này trả về vỏ Admin Portal)

```
# OnlyAIJobs

> OnlyAIJobs is a specialist job board for artificial intelligence, machine
> learning and data science roles, focused on the Netherlands and the wider EU.
> It shows every vacancy at exact street-address level with the distance from
> the job seeker's home, so people can find AI employers near them instead of
> assuming they must move to the Randstad. Available in English and Dutch.

## What we list
- AI, machine learning, data science, computer vision, robotics, AI governance roles
- Full-time, part-time, internship and remote positions
- Employers currently listing include Accenture, Cegeka, Sendcloud, Mollie,
  Heijmans, Rexel Nederland, VINCI Energies, AMCS, Boltrics and Winparts

## What makes us different
- Vacancies mapped to an exact address, not just a city
- Equal visibility for every employer regardless of advertising budget
- AI-only: no filtering through unrelated vacancies
- Built to counter regional talent drain (Noord-Brabant to the Randstad)

## For employers
- Send a link to your vacancy to info@onlyaijobs.eu — the first listing is free

## Key pages
- https://onlyaijobs.eu/jobs
- https://onlyaijobs.eu/nl/vacatures
- https://onlyaijobs.eu/pages/info-for-employers
```

### 6.3 Prompt mục tiêu

- "Where can I find AI jobs in the Netherlands?"
- "AI vacatures in Brabant"
- "Job boards specialised in machine learning roles in Europe"
- "Which companies in Eindhoven hire AI engineers?"

Câu hỏi cuối đặc biệt đáng chú ý: nó **chính xác** là thứ dữ liệu của OnlyAIJobs trả lời được tốt hơn LinkedIn — vì site biết địa chỉ chính xác của từng nhà tuyển dụng. Trang `/jobs/city/<city>` liệt kê tên công ty thật là loại nội dung LLM trích dẫn dễ nhất.

---

<a name="7"></a>
## 7. 📝 Kế Hoạch Blog Từ Con Số 0

Blog hiện có **0 bài**. Đừng viết bừa — mỗi bài phải phục vụ một trong ba mục đích: kéo backlink, chiếm từ khóa thông tin, hoặc nuôi kênh social.

### 7.1 Bốn cụm nội dung, theo thứ tự ưu tiên

| # | Cụm | Số bài đợt đầu | Ngôn ngữ | Mục đích |
|---|---|---|---|---|
| **1** | **Báo cáo lương AI tại Hà Lan** (theo vai trò, theo vùng, theo cấp độ) | 6 | NL trước, EN sau | Nam châm backlink mạnh nhất của mọi job board. Báo chí và blog HR dẫn nguồn dữ liệu lương. |
| **2** | **Bản đồ nhà tuyển dụng AI theo vùng** ("15 công ty AI ở Brabant bạn chưa nghe tên") | 8 | NL | Đúng câu chuyện thương hiệu; dùng dữ liệu công ty đã có trên site |
| **3** | **Hướng dẫn nghề nghiệp** (CV cho vai trò AI, phỏng vấn ML, junior→senior) | 8 | NL + EN | Persona A và B; từ khóa thông tin dài |
| **4** | **Nội dung cho nhà tuyển dụng** (viết JD cho vai trò AI, chi phí tuyển, giữ chân kỹ sư) | 6 | NL | Persona C; phục vụ trang `/pages/info-for-employers` |

### 7.2 Quy tắc bắt buộc

1. **Mỗi bài link tới ít nhất một trang việc làm có thật** (`/jobs/city/eindhoven`, `/jobs/category/machine-learning`). Bài blog không dẫn về tin tuyển dụng là bài chết.
2. **Dùng dữ liệu của chính site**: "trên OnlyAIJobs hiện có X tin tại Y" — số liệu tự thân, không ai copy được.
3. **Không viết bài trước khi §2 xong.** Blog trỏ về trang việc làm không index được thì vô nghĩa.
4. Bài lương phải ghi rõ ngày và phương pháp; cập nhật mỗi 6 tháng.

---

<a name="8"></a>
## 8. 🔗 Liên Kết Nội Bộ

1. Trang chi tiết việc làm → `/companies/<company>` + `/jobs/city/<city>` + `/jobs/category/<cat>` (3 link, luôn luôn)
2. Trang thành phố → 5 thành phố lân cận ("việc làm AI gần Eindhoven: Tilburg, Den Bosch, Helmond…") — mô phỏng đúng hành vi tìm việc theo bán kính
3. Trang danh mục → các danh mục liên quan (Machine Learning ↔ Computer Vision ↔ Generative AI)
4. Blog → tối thiểu 2 trang việc làm
5. Trang chủ → 8–10 trang thành phố/danh mục lớn nhất
6. Link ra site nhà tuyển dụng: **`nofollow`** (link thương mại)
7. Không trang nào cách trang chủ quá 3 cú nhấp

---

<a name="9"></a>
## 9. 📅 Lịch 90 Ngày Theo Cổng Chặn

> Mỗi giai đoạn là một **cổng**: chưa qua cổng trước thì giai đoạn sau vô nghĩa. Đây không phải lịch song song.

### 🚪 Cổng 0 · Tuần 1–2 — Mở cửa
- [ ] Allow-list Googlebot + Bingbot trong BunkerWeb (xác minh reverse-DNS, không chỉ theo UA)
- [ ] Viết lại `robots.txt` theo §6.1 (mở cho cả bot AI)
- [ ] Ngừng phục vụ Admin Portal ở `/pages/*`, `/llms.txt`, `/job/list`
- [ ] Đăng ký Google Search Console + Bing Webmaster Tools, xác minh sở hữu
- [ ] Cài GA4 (hiện chưa phát hiện thấy analytics nào)
- [ ] Chạy Keyword Planner theo §3.4
- **Cổng qua khi**: URL Inspection trong GSC báo trang chủ "crawlable"

### 🚪 Cổng 1 · Tuần 3–6 — Làm cho việc làm index được
- [ ] Sinh URL riêng cho từng việc làm (§4.2)
- [ ] Gắn `JobPosting` schema đầy đủ (§2.1), kiểm bằng Rich Results Test
- [ ] Bỏ canonical ép về trang 1 trên các trang phân trang
- [ ] Sinh sitemap động gồm mọi URL việc làm + URL `/nl`
- [ ] Sửa `index-sitemap.xml` cho đúng cú pháp; hợp nhất hai tệp sitemap
- [ ] Sửa hreflang đối xứng (§5.1)
- **Cổng qua khi**: ≥40 URL việc làm được index và Rich Results Test báo `JobPosting` hợp lệ

### 🚪 Cổng 2 · Tuần 7–10 — Có nội dung để xếp hạng
- [ ] Viết nội dung thật cho `/pages/info-for-employers`, `/pages/info-for-job-seekers`, `/pages/about-us` (cả EN và NL)
- [ ] Sinh trang thành phố/danh mục vượt ngưỡng (§4.1) — dự kiến 12–17 trang
- [ ] Xây trang `/companies/<company>` cho ~40 nhà tuyển dụng đang có tin
- [ ] Viết `llms.txt` thật (§6.2)
- [ ] Ẩn hoặc lấp 5 danh mục rỗng
- **Cổng qua khi**: 0 URL trong sitemap trả về trang rỗng

### 🚪 Cổng 3 · Tuần 11–13 — Tăng trưởng
- [ ] Đợt blog đầu tiên: 6 bài báo cáo lương (§7.1 cụm 1)
- [ ] Bắt đầu chương trình xây nguồn tin (điều kiện sống còn — [`implementation_plan.md`](./implementation_plan.md) §4)
- [ ] Rà GSC lần đầu: truy vấn nào đang có impression
- [ ] Kiểm tra GEO lần 1 (§6.3)

---

<a name="10"></a>
## 10. 📊 KPI

| Chỉ số | Hiện tại (8/9/2026) | Cổng 1 xong | Cổng 2 xong | Tháng 6 |
|---|---|---|---|---|
| Trang được Google index | **0** | 50 | 120 | 400+ |
| Việc làm index được | **0** (thực tế 10/52 nếu gỡ chặn) | 52/52 | 80+ | 300+ |
| Có mặt trong Google Jobs | ❌ | ✅ | ✅ | ✅ |
| Phiên organic/tháng | **0** | 100 | 600 | 3.000 |
| Số tin đang hiệu lực | 52 (đều 1 tháng tuổi) | 60 | 100 | 250 |
| Tin đăng mới/tháng | ~0 | 15 | 40 | 80 |
| Bài blog | 0 | 0 | 0 | 20 |
| Trích dẫn trong AI answer | không rõ | — | 1/4 prompt | 2/4 prompt |

> **🇻🇳 Vì sao mốc đầu tiên là 0 → 50 chứ không phải 0 → 1.000**: site chưa từng được index. Không có lịch sử domain, không có backlink, không có tín hiệu. Ba tháng đầu là dựng nền, không phải thu hoạch.

---

<a name="11"></a>
## 11. ⚠️ Rủi Ro

| Rủi ro | Mức | Xử lý |
|---|---|---|
| **Cổng 0 không được thực hiện** | 🔴 Rất cao | Đã khuyến nghị 3 lần trong 39 ngày mà chưa ai đụng tới. Cần một người chịu trách nhiệm có tên cụ thể và một hạn chót. |
| **Nguồn tin cạn** | 🔴 Cao | 52 tin đều 1 tháng tuổi. Bật `JobPosting` với tin hết hạn sẽ bị Google phạt uy tín. Nguồn cung phải giải trước. |
| **Programmatic SEO sinh trang rỗng** | 🟡 Trung bình | Áp ngưỡng §4.1 vào code, tự động `noindex` khi rơi dưới ngưỡng |
| **Đấu sai trận với LinkedIn/Indeed** | 🟡 Trung bình | Chỉ đánh đuôi dài `<vai trò>+<thành phố>` bằng tiếng Hà Lan |
| **Mâu thuẫn định vị EU vs NL** | 🟡 Trung bình | Chốt quyết định trước Cổng 2 |
| **Không có analytics** | 🟡 Trung bình | Không đo được thì không tối ưu được. Cài ở Cổng 0. |
| **Tin từ aggregator Mỹ (Lensa)** | ⚪ Thấp | 3/52 tin ở Mỹ trên site `.eu` làm loãng định vị. Cân nhắc gỡ. |

---

<a name="12"></a>
## 12. 🖊️ Quyết Định Cần Chốt

| # | Quyết định | Chặn việc gì |
|---|---|---|
| 1 | **Ai chịu trách nhiệm cấu hình BunkerWeb, và khi nào?** | Toàn bộ mọi thứ |
| 2 | Định vị: job board AI châu Âu hay nền tảng việc làm AI theo vùng tại Hà Lan? | Bộ từ khóa, kiến trúc trang, ngôn ngữ ưu tiên |
| 3 | Ngôn ngữ ưu tiên: NL trước hay EN trước? | Thứ tự sản xuất nội dung |
| 4 | Nguồn tin đến từ đâu — crawler, nhà tuyển dụng gửi, hay đội sale đi lấy? | Khả năng tồn tại của cả kế hoạch |
| 5 | Mô hình doanh thu sau tin miễn phí đầu tiên? | Trang giá, quảng cáo nhắm nhà tuyển dụng |
| 6 | Có xây trang chi tiết việc làm không (cần công sức dev)? | Cổng 1 — không có thì không vào được Google Jobs |
| 7 | Giữ hay gỡ 3 tin việc làm tại Mỹ? | Tính nhất quán định vị |

---

*OnlyAIJobs.eu · Tài liệu lập ngày 08/09/2026 dựa trên dữ liệu quét trực tiếp*
