# 📐 v0 (Vercel) — tài liệu tham chiếu

> **Ngày:** 12/10/2026 · **Mục đích:** nền dữ kiện để viết nội dung và landing page có nhắc v0
> **Dùng cho:** `/ai-app-security` · `/eigen-code-eigen-hosting` · `extra-1/13-v0-built-your-ui-who-builds-the-backend.md`

---

## 1. Thông tin cơ bản

| | |
|---|---|
| **Website hiện tại** | **`v0.app`** |
| Tên miền cũ | `v0.dev` — vẫn còn nhiều nội dung bên thứ ba dùng tên này |
| Nhà phát triển | **Vercel** (hãng làm Next.js) |
| Định vị hiện tại | *"AI agent that helps anyone create real code and **full-stack apps and agents**"* |
| Headline | *"Ship features, refine designs, update copy, and create live prototypes via prompt"* |
| Đối tượng Vercel nhắm | PM, designer, engineer, data scientist, marketing, support, founder |

### 🔴 Cập nhật quan trọng: v0 không còn là công cụ "chỉ frontend"

Đây là chỗ tôi đã cảnh báo cần kiểm lại, và kiểm lại cho kết quả khác với hiểu biết phổ biến:

- Trang chủ v0.app nói rõ **full-stack apps**, không chỉ UI
- Vercel đã **viết lại v0** để giải quyết cái họ gọi là *"the 90% problem"* — khoảng cách giữa code do AI sinh và code chạy được ở production ([VentureBeat](https://venturebeat.com/ai/vercel-rebuilt-v0-to-tackle-the-90-problem-connecting-ai-generated-code-to))

➡️ **Mọi nội dung cũ viết "v0 chỉ làm giao diện" đều cần sửa.** Bao gồm bài `13-v0-built-your-ui-who-builds-the-backend.md` — tiêu đề đó giờ không còn đúng với sản phẩm hiện tại.

Nhưng khoảng trống vẫn còn, chỉ là **sắc nét hơn**: xem §4.

---

## 2. Stack và tích hợp

| | |
|---|---|
| Framework | **Next.js** · **Tailwind CSS** · **shadcn/ui** |
| Deploy | Một cú bấm lên hạ tầng Vercel |
| Nhập thiết kế | **Figma** (import mockup) |
| Lưu file | Vercel Blob |
| Dữ liệu doanh nghiệp | Snowflake |
| **Database** | ⚠️ **Vercel Postgres đã ngừng.** Dự án mới dùng Marketplace: **Neon**, **Supabase**, **AWS Aurora** — giá và giới hạn theo từng nhà cung cấp |

> 💡 **Hai điểm đáng chú ý cho launchstudio:**
>
> **① Stack trùng khít.** Next.js + Tailwind + shadcn/ui là đúng stack launchstudio làm (`/services/react-development`). Người đến từ v0 có frontend sạch, hiện đại, không cần đụng tới.
>
> **② Database là bring-your-own.** Và **Supabase là một trong ba lựa chọn** — nghĩa là app v0 dùng Supabase sẽ gặp **đúng những lỗ hổng RLS** đã mô tả ở `/ai-app-security`. Cầu nối giữa hai trang nằm ở đây.

---

## 3. Giá (2026)

| Gói | Giá | Credit kèm theo |
|---|---|---|
| Free | $0 | **$5**/tháng |
| **Pro** | **$20**/user/tháng | $20 |
| Team | $30/user/tháng | $30/user |
| Business | ~$100/user/tháng | — |
| Enterprise | Theo thoả thuận | — |

**Credit tiêu theo token, không theo số tin nhắn.** Nghĩa là chi phí thật phụ thuộc vào việc bạn build nhiều hay ít, không phụ thuộc gói.

> 💡 Đây là dữ kiện tốt cho nội dung so sánh chi phí: một founder dùng v0 Pro trả $20/tháng và tưởng đó là toàn bộ chi phí — nhưng còn hosting Vercel, database (Neon/Supabase), và credit vượt mức. Bài dạng *"v0 thật sự tốn bao nhiêu"* là nội dung chưa ai làm kỹ và đúng loại LLM trích dẫn.

---

## 4. Code của bạn có lấy ra được không — rất quan trọng cho trang export

**Có, và cơ chế khá tử tế:**

| | |
|---|---|
| Git panel | Tích hợp sẵn trong v0, nối tài khoản GitHub |
| Push | Đẩy project sang một repo mới |
| **Không ghi thẳng vào `main`** | Luôn tạo nhánh riêng, dạng `v0/main-{hash}` |
| Merge | Bạn tự bấm `Merge pull request` trên GitHub |
| Deploy | Nối repo với Vercel → tự build lại mỗi lần merge |
| Two-way sync | Bidirectional git sync ở **beta** cho người dùng premium (từ 5/2025) |

### 🔴 Hệ quả cho trang `/eigen-code-eigen-hosting`

**Đừng nói "v0 khoá code của bạn lại".** Điều đó không đúng — v0 có đường ra tử tế hơn Lovable và Bolt.

Góc đúng cho v0 trên trang đó là khác: **lấy code ra được không có nghĩa là code chạy được ở nơi khác.** Những thứ vỡ sau khi rời Vercel:

- Deploy phụ thuộc hạ tầng Vercel (serverless function, edge runtime, image optimization)
- Vercel Blob không chạy ngoài Vercel
- Biến môi trường và secret phải khai lại
- Database Marketplace (Neon/Supabase) có cấu hình riêng

➡️ Với v0, dịch vụ bán được không phải *"giải thoát code"* mà *"làm nó chạy ở nơi bạn chọn"*.

### Cụm từ khoá export đã validate (Autocomplete, `gl=us`)

```
v0 export code        v0 export to github      v0 export project
how to export from v0  export v0 to cursor     can v0 export to figma
```

---

## 5. ⚠️ Vấn đề bảo mật trong code v0 sinh ra

Phần này là thứ dùng được nhất cho `/ai-app-security` — **nhưng phải đọc kèm §6.**

### Ba lỗi được ghi nhận nhiều nhất

**① XSS qua `dangerouslySetInnerHTML`**
v0 có lúc sinh component render nội dung rich text bằng `dangerouslySetInnerHTML`. Nếu nguồn là dữ liệu người dùng nhập, kẻ tấn công chèn được `<script>` hoặc event handler. Được mô tả là *"mẫu XSS gây hại nhất trong code do v0 sinh"*.

**② Chỉ validate ở client, thiếu bảo vệ phía server**
Code UI do AI sinh ưu tiên đúng về hình ảnh hơn đúng về bảo mật — ra component chỉ kiểm tra dữ liệu ở trình duyệt.

**③ Lộ secret — đặc biệt là dùng sai `NEXT_PUBLIC_`**
Trong Next.js, biến có tiền tố `NEXT_PUBLIC_` **được nhúng vào bundle gửi tới trình duyệt**. Đặt API key vào đó là công khai nó. Đây được ghi nhận là lỗi phổ biến nhất trong các lần deploy bị chặn.

**Cộng thêm:** auth, phân quyền theo role, và tách dữ liệu đa khách (tenant isolation) đều cần triển khai ở mức production — không phải thứ prompt sinh ra đúng.

> 💡 **`NEXT_PUBLIC_` là bước tự kiểm hoàn hảo để thêm vào S3 của `/ai-app-security`:**
>
> > *"Search your repo for `NEXT_PUBLIC_`. Anything after that prefix ships to the browser. If an API key is in there, it's public."*
>
> Nó cụ thể, làm được trong 30 giây, và đặc thù Next.js — nghĩa là áp đúng cho cả người dùng v0 **và** người dùng Lovable (Lovable cũng xuất React/Next).

---

## 6. 🔴 Nhưng Vercel đang tự đóng khoảng trống này — và đó là khác biệt lớn so với Lovable

Đây là nhận định quan trọng nhất trong cả tài liệu.

| | **Lovable** | **v0 / Vercel** |
|---|---|---|
| Mặc định bảo mật | Supabase tắt RLS mặc định; output không bắt buộc bật | Vercel công bố bài [*"v0: vibe coding, securely"*](https://vercel.com/blog/v0-vibe-coding-securely): *"khi code do AI viết, mặc định an toàn phải là nền tảng, không phải tính năng"* |
| Hành động của nền tảng | Vá BOLA chỉ cho project sau 11/2025, project cũ hở ~48 ngày | Tuyên bố đã **chặn hơn 100.000 lần deploy không an toàn** |
| Hướng đi | Sự cố 4/2026 · ban đầu phủ nhận | Viết lại sản phẩm để giải "the 90% problem" |

### Ba hệ quả thực thi

**① Góc security cho v0 yếu hơn cho Lovable, và sẽ còn yếu đi.** Vercel đang chủ động siết. Đừng xây luận điểm bán hàng dựa vào "v0 không an toàn" — nó sẽ lỗi thời nhanh, và Vercel có đủ nguồn lực để chứng minh ngược lại.

**② Nhưng mặc định an toàn không sửa được lỗi tầng code.** `dangerouslySetInnerHTML` với dữ liệu người dùng và việc nhét key vào `NEXT_PUBLIC_` là **quyết định trong code**, không phải cấu hình nền tảng. Deployment guard chặn được một phần, không chặn được hết. Đó là chỗ góc của launchstudio còn đứng vững.

**③ Phân tầng thông điệp theo công cụ, đừng gộp một giọng.**

| Công cụ | Thông điệp đúng |
|---|---|
| **Lovable** | Có sự cố nền tảng có thật, có CVE, có ngày tháng → *"kiểm tra app của bạn"* |
| **v0** | Nền tảng đang siết tốt → *"vẫn còn lỗ ở tầng code mà guard không thấy"* |

Gộp cả hai thành *"app AI thì không an toàn"* sẽ vừa sai với v0 vừa làm loãng lập luận mạnh về Lovable.

---

## 7. Ai đã viết về v0 — bối cảnh cạnh tranh

| Site | Nội dung về v0 | Loại |
|---|---|---|
| **WZ-IT** | `prototype-to-production/from-v0/` | 🔴 **Trang dịch vụ đúng offer của launchstudio, riêng cho v0** |
| vibeappscanner.com | `/question/how-secure-v0` · `/blog/v0-dev-security-best-practices` | Scanner tự động |
| vibe-eval.com | `/safety/v0/` | Scanner / đánh giá |
| unpwned.io | `/platforms/v0` | Theo dõi nền tảng |
| rapidevelopers.com | Hướng dẫn Git · GitHub sync | Nội dung how-to |
| **Vercel** | `vercel.com/blog/v0-vibe-coding-securely` | Nền tảng tự nói về bảo mật |

> 🔴 **WZ-IT là phát hiện đáng chú ý nhất ở đây.** Họ đã có trang `prototype-to-production/from-v0/` — tức một trang dịch vụ *đưa app v0 lên production*, đúng y offer của launchstudio, và họ đã làm riêng cho từng công cụ.
>
> Theo đúng phương pháp ở `volume_analysis_results.md` §4 (chỉ tín hiệu cầu mới đáng tin), **đây là tín hiệu cầu thật**: một agency không tự dưng làm landing page riêng cho v0. Đáng vào xem họ cấu trúc trang thế nào trước khi viết trang của mình.

---

## 8. ⚠️ Một con số không nên dùng

Có nguồn ghi: *"phần lớn app v0.dev deploy mà không quét trước đều có ít nhất một lỗi critical hoặc high."*

**Nguồn của con số này là vibeappscanner** — một đối thủ bán dịch vụ quét, tức có lợi ích thương mại trực tiếp khi con số đó cao.

➡️ **Đừng trích con số này lên trang.** Nó không phải nghiên cứu độc lập. Nếu cần số liệu về v0, dùng con số của chính Vercel (*đã chặn 100.000+ deploy không an toàn*) — vừa kiểm chứng được, vừa là nguồn thù địch với lợi ích của launchstudio nên đáng tin hơn.

Nguyên tắc này giống cảnh báo ở `landing_ai_app_security_brief.md` §7 mục 2: **không dẫn blog SEO của đối thủ làm nguồn.**

---

## 9. Việc nên làm với thông tin này

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Sửa bài `13-v0-built-your-ui-who-builds-the-backend`** | Tiêu đề và luận điểm đã lỗi thời — v0 giờ làm full-stack |
| 2 | Thêm bước tự kiểm `NEXT_PUBLIC_` vào S3 của `/ai-app-security` | Áp cho cả v0 và Lovable |
| 3 | Thêm v0 vào trang `/eigen-code-eigen-hosting` | Nhưng với góc *"chạy ở nơi khác"*, không phải *"giải thoát code"* |
| 4 | Xem trang `WZ-IT /prototype-to-production/from-v0/` | Đối thủ trực tiếp nhất tìm được cho offer này |
| 5 | Cân nhắc bài *"v0 thật sự tốn bao nhiêu"* | Credit theo token + hosting + database — chưa ai làm kỹ |
| 6 | Phân tầng thông điệp security theo công cụ | §6③ — đừng gộp Lovable và v0 cùng một giọng |

---

## 10. Nguồn

- [v0.app](https://v0.app/) — trang chủ chính thức (crawl 12/10/2026)
- [Vercel — v0: vibe coding, securely](https://vercel.com/blog/v0-vibe-coding-securely)
- [VentureBeat — Vercel rebuilt v0 to tackle the "90% problem"](https://venturebeat.com/ai/vercel-rebuilt-v0-tackle-the-90-problem-connecting-ai-generated-code-to)
- [UI Bakery — Vercel v0 Pricing: Plans, Credits & Limits (2026)](https://uibakery.io/blog/vercel-v0-pricing-explained-what-you-get-and-how-it-compares)
- [Costbench — v0 by Vercel Pricing 2026](https://www.costbench.com/software/ai-coding-assistants/v0-vercel/)
- [Vercel Community — push v0 code to GitHub](https://community.vercel.com/t/how-can-i-push-the-code-written-in-v0-to-my-github-repository/7558)
- [WZ-IT — from v0 to production](https://wz-it.com/en/software-development/prototype-to-production/from-v0/) ← đối thủ
- Google Autocomplete (`hl=en`, `gl=us`), 12/10/2026
