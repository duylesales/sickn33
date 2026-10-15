# 🔄 Cập nhật digital marketing — tháng 10/2026

> **Phạm vi:** những gì đã đổi và **ảnh hưởng trực tiếp** tới tài liệu đang có của launchstudio
> **Không phải** danh sách trend chung — chỉ những thứ áp được vào ngân sách ~€600–730/tháng, thị trường NL, 1–3 lead/tháng
> **File bị ảnh hưởng:** `google_search_ads_master_plan.md` · `google_ads_plan_payments_nl.md` · `volume_analysis_results.md` · 4 brief landing page · `keyword_*.csv`

---

## 1. 🔴 Google Ads AI Max — đã tự nâng cấp 1/9/2026. Đây là tin xấu nhất.

### Chuyện gì xảy ra

**AI Max for Search đã ra khỏi beta và thành mặc định** cho campaign Search mới. Ngày **1/9/2026**, Google **tự động nâng cấp** hai loại campaign:

| Loại campaign | Bị bật gì |
|---|---|
| Có Automatically Created Assets (ACA) | Search term matching **ON** + text customization **ON** |
| Có Broad match ở cấp campaign | Search term matching **ON** |

AI Max gộp ba tính năng: **expanded search term matching** · **text customization** (AI tự viết headline/description) · **final URL expansion** (AI tự chọn landing page).

### 🔴 Vì sao nó phá chiến lược của chúng ta

Google giờ dùng **LLM để đánh giá độ tương đồng ý định**, không còn khớp theo token. Ví dụ Google công bố:

```
Exact match [key lockers]  →  cũng chạy cho "digital key lockers"
                           →  và "lockers with audit trail"
```

Một nghiên cứu tháng 12/2025 ghi nhận AI Max **mở rộng cả Exact và Phrase match**, để Broad match nguyên — và có lúc khớp **brand term sang thương hiệu đối thủ**.

**Toàn bộ kỷ luật match type trong session này dựa vào việc Exact và Phrase là hàng rào.** Hàng rào đó không còn.

### Những bẫy giờ bị phơi ra

Tất cả các bẫy đồng âm tôi tìm được giờ **không còn được Exact/Phrase bảo vệ**:

| Từ khoá | Bẫy | File ghi nhận |
|---|---|---|
| `clutch` | Túi xách, ly hợp xe | phân tích goodfirms |
| `bubble agency` | Hãng PR ở London/LA | brief unicoconnect |
| `lovable agency` | Hãng branding/design | `landing_ai_app_vibe_coding_brief.md` §3 |
| `bolt app` | App gọi xe Bolt, bu lông, súng | cùng file |
| `integratie specialist` | Chuyên viên tái hoà nhập lao động | `landing_ai_app_integrations_brief.md` §3 |
| `systeemintegratie` | Ngành năng lượng (TKI, Topsector) | cùng file |
| `wat kost een app` | `appartement`, `appelboom`, `apple iphone` | `landing_pages_roadmap.md` §11 |
| `ai automation agency` | Khoá học "mở agency" | brief unicoconnect |
| `app aanmaken` | Đăng ký app ngân hàng (ING, DigiD) | `landing_ai_app_vibe_coding_brief.md` §3 |

### Việc phải làm

**① Negative keyword từ "quan trọng" thành **hàng rào duy nhất**.**

Các danh sách negative đã viết trong session này giờ là lớp bảo vệ duy nhất, không phải lớp thứ hai:

| File | Số negative |
|---|---:|
| `unicoconnect/negative_keywords.txt` | 88 |
| `keyword_ai_app_vibe_coding.csv` (role=NEGATIVE) | 30 |
| Khối `re-integratie` + `systeemintegratie` | §3 brief integrations |

➡️ **Áp ở cấp tài khoản**, không phải cấp campaign. Và đọc Search Terms report **hàng tuần** trong 8 tuần đầu — đó là cách duy nhất phát hiện AI Max đang khớp vào đâu.

**② Tắt text customization nếu còn tắt được.**

AI Max tự viết headline từ landing page và keyword. Với launchstudio điều đó nguy hiểm hơn bình thường: nếu nó sinh ra câu hứa "miễn phí" hay "rebuild" thì sai hẳn định vị — mà `landing_ai_app_*_brief.md` đều nhấn *"geen rebuild"* và *"audit là báo giá, không phải audit miễn phí"*.

**③ Tắt Final URL expansion.**

Ba trang service NL đã live (`/ai-app-beveiliging/`, `/ai-app-integraties/`, `/ai-app-naar-productie/`). Để AI Max tự chọn trang đích nghĩa là mất kiểm soát message match — và mất luôn `utm_content` theo từng trang.

**④ Kiểm lại ngay nếu đã có campaign chạy.**

Nếu campaign nào có ACA hoặc broad match ở cấp campaign, nó **đã bị nâng cấp từ 1/9** mà không cần bạn đồng ý.

---

## 2. 🥇 Dark funnel — giải thích được điều cả session này vướng

### Con số

| | |
|---|---|
| **72%** người mua software B2B **bắt đầu tìm nhà cung cấp trong community kín**, không phải Google | 2026 |
| Dark social = **84%** mọi lượt share, **58%** lưu lượng web | |
| Dark funnel = **30–50%** tổng pipeline B2B, attribution truyền thống không thấy | |
| **60–80%** quyết định mua xảy ra ngoài kênh đo được | Slack, LinkedIn DM, podcast, slide nội bộ, lời giới thiệu |

### 🔴 Đây là lời giải cho bí ẩn trong `volume_analysis_results.md`

File đó kết luận:

> *"Luận điểm cốt lõi — 'làm nốt prototype AI dang dở' — gần như không có ai tìm kiếm. 27 keyword có tổng 10 lượt/tháng. 26/27 bằng 0. **Đây là kết luận về thị trường, không phải về danh sách từ khoá.**"*

Kết luận đó **đúng về dữ liệu nhưng sai về nguyên nhân**. Nhu cầu có thật — nó chỉ không đi qua Google.

Người vừa build app bằng Lovable và không launch được **không gõ Google**. Họ hỏi trong Discord của Lovable, trong r/vibecoding, trong Slack của cộng đồng no-code, hoặc DM một người họ tin. Đó là 72% kia.

➡️ **Hướng B ở §6.2 của file đó là đúng** — và giờ có số liệu chống đỡ, không còn là phỏng đoán.

### Việc làm được ngay

| Kênh | Vì sao |
|---|---|
| **Discord/forum chính thức của Lovable, Bolt, Replit** | Nơi người dùng mắc kẹt hỏi nhau. Trả lời thật, không bán |
| **r/vibecoding, r/nocode, r/SaaS** | Đã nêu trong §6.2 nhưng chưa làm |
| **LinkedIn cá nhân, không phải company page** | LinkedIn chiếm ~80% lead social B2B 2026, nhưng mô hình đã chuyển từ page sang **employee advocacy / personal brand** |
| **Câu hỏi "ai dùng gì cho X" trong community NL** | Thị trường nhỏ, một câu trả lời tốt được nhớ lâu |

### Và đo bằng cách nào

Attribution truyền thống không thấy dark funnel. Cách thực tế duy nhất: **thêm một câu vào form** — *"Hoe heb je ons gevonden?"* với lựa chọn tự do. Đó là dữ liệu self-reported, không đẹp, nhưng là dữ liệu duy nhất có.

Thêm vào trang `/request-quote` (mục P0 trong `landing_pages_roadmap.md`) khi làm.

---

## 3. GEO — số liệu đã có, và nó xác nhận hướng đi

### Tin xấu cho organic

| | |
|---|---|
| Khi có AI Overview, chỉ **8%** người bấm kết quả truyền thống (so với 15% khi không có) | |
| **AI Mode: 93%** phiên kết thúc **không click** ra ngoài | |
| Google referral tới publisher giảm **~33%** YoY | |
| AI Overviews: **2,5 tỷ** người dùng/tháng · AI Mode: **1 tỷ+** MAU | |

### 🥇 Nhưng tin tốt cho B2B

| | |
|---|---|
| LLM referral chỉ **~1%** lưu lượng (B2B SaaS: 1% vs organic 23,4%) | Khối lượng nhỏ |
| **Nhưng tăng 9,9× trong 19 tháng**, 92,4% đến từ ChatGPT | Đang lên nhanh |
| 🥇 **Lưu lượng từ AI search chuyển đổi gấp 4,4 lần organic** — nghiên cứu trên 500+ chủ đề B2B | Chất lượng rất cao |

➡️ **Đây chính xác là tình huống của launchstudio.** Volume vốn đã nhỏ (toàn tài khoản 1.870 lượt/tháng), nên một kênh "ít lượt nhưng chuyển đổi gấp 4,4 lần" đáng giá hơn nhiều so với đua CPC.

Và nó xác nhận lập luận trong `landing_ai_app_security_brief.md` §2: nội dung có thực chất kỹ thuật (CVE-2025-48757, sự cố Lovable 4/2026, framework 6 điểm, các bước tự kiểm) là loại nội dung LLM trích dẫn.

### Việc chưa làm

| | Trạng thái |
|---|---|
| 3 trang service NL đã live | ✅ |
| `/ai-app-vibe-coding` (pillar) | ❌ chưa có — `landing_pages_roadmap.md` §8 xếp 🥇 |
| `best-ai-agent-development-companies` | ❌ khoảng trống lớn nhất (brief unicoconnect §7) |
| Nghiên cứu gốc từ dữ liệu 160 dự án | ❌ thứ không ai sao chép được |
| `llms.txt` | ⚠️ unicoconnect có, launchstudio chưa kiểm |

---

## 4. ⚪ Agentic commerce — chưa áp dụng được, đừng chạy theo

Gartner dự báo **90% giao dịch B2B sẽ qua trung gian AI agent vào 2028**, đẩy hơn **15.000 tỷ USD** qua các agent exchange. Thị trường AI agent có thể đạt 35–45 tỷ USD cuối thập kỷ.

**Nhưng đọc kỹ thì nó nói về mua sắm có catalog:** replenishment agent, negotiation agent, pricing agent, assortment agent — hoạt động trong khuôn khổ *approved suppliers, negotiated contracts, customer-specific catalogs, spending limits*.

➡️ **Không áp vào launchstudio.** Dự án €800–7.500 làm theo scope riêng không có catalog để agent đặt hàng. Không ai để AI agent tự chọn studio làm app cho mình.

> 💡 **Nhưng công việc GEO chính là sự chuẩn bị cho nó.** Khi buyer dùng AI để lập shortlist (Gartner: đa số buyer B2B đã làm vậy; 6sense: 94% dùng AI ở một điểm trong hành trình mua), thì "được AI trích dẫn" chính là bước vào vòng. Làm GEO bây giờ là làm agentic-ready, không cần làm gì thêm.

---

## 5. Consent Mode v2 — đã siết lại 15/6/2026

Bắt buộc cho mọi lưu lượng EEA + UK nếu dùng Google Ads hoặc Analytics. Đã được tăng cường ngày **15/6/2026**.

`conversion_attribution_setup.md` §2① đã có code. **Việc cần làm: xác nhận nó đã triển khai thật trên launchstudio.eu**, không chỉ nằm trong tài liệu.

Thêm một điểm cho B2B: email công việc, chức danh, profile LinkedIn, IP — **đều là dữ liệu cá nhân theo AVG** nếu định danh được một người. Không có ngoại lệ "B2B" như nhiều người tưởng.

---

## 6. Thứ tự việc nên làm

| Ưu tiên | Việc | Vì sao bây giờ |
|---|---|---|
| 🔴 **P0** | Kiểm campaign Google Ads xem có bị nâng cấp AI Max | Đã xảy ra từ 1/9, có thể đang tiêu tiền sai |
| 🔴 **P0** | Áp negative keyword cấp tài khoản (88 + 30 + khối NL) | Giờ là hàng rào duy nhất |
| 🔴 **P0** | Tắt text customization + Final URL expansion | Giữ kiểm soát thông điệp và landing page |
| **P1** | Đọc Search Terms report hàng tuần, 8 tuần | Cách duy nhất thấy AI Max khớp vào đâu |
| **P1** | Bắt đầu hiện diện trong Discord/Reddit của Lovable, Bolt, Replit | 72% buyer bắt đầu ở đó, không ở Google |
| **P1** | Thêm *"Hoe heb je ons gevonden?"* vào form | Cách duy nhất đo dark funnel |
| **P2** | Làm `/ai-app-vibe-coding` (pillar) | Roadmap §8 xếp 🥇, chưa làm |
| **P2** | Chuyển content LinkedIn sang profile cá nhân | Mô hình page đã hết hiệu lực |
| **P3** | Xác nhận Consent Mode v2 đã chạy thật | Bắt buộc pháp lý |
| ⚪ **Bỏ qua** | Agentic commerce | Chưa áp dụng cho mô hình dự án |

---

## 7. Điều quan trọng nhất trong bản cập nhật này

Hai thứ kéo về cùng một hướng:

**① AI Max làm Google Ads kém kiểm soát hơn và dễ rò rỉ ngân sách hơn** — đúng lúc ngân sách của launchstudio vốn đã mỏng (trần chi thật €724 cho nhánh NL, €143 cho nhánh EN).

**② Dark funnel cho biết khách thật ở đâu** — và đó không phải Google.

➡️ Cả hai củng cố **Hướng B** ở `volume_analysis_results.md` §6.2: giữ Search Ads ở mức tối thiểu như công cụ phòng thủ, dồn công sức vào nội dung, cộng đồng và GEO.

Khác biệt so với hồi tháng 9: lúc đó đó là một phỏng đoán có lý. Giờ có ba con số chống đỡ — 72% buyer bắt đầu ở community, AI search chuyển đổi gấp 4,4 lần, và match type không còn là hàng rào.

---

## Nguồn

- [PPC Land — AI Max auto-upgrade 1/9](https://ppc.land/google-ads-ai-max-auto-upgrade-lands-september-1-will-ads-all-look-alike/) · [broad match auto-upgrade](https://ppc.land/google-ads-broad-match-campaigns-face-ai-max-auto-upgrade-on-september-1/)
- [Herdl — Google phasing out Dynamic Search Ads as AI Max takes over](https://herdl.com/google-is-phasing-out-dynamic-search-ads-as-ai-max-takes-over/)
- [SEO Sherpa — AI Search Statistics 2026](https://seosherpa.com/ai-search-statistics/)
- [Omnibound — Google AI Overviews Statistics 2026](https://www.omnibound.ai/blog/google-ai-overviews-statistics)
- [Growthspree — Dark funnel pipeline benchmarks B2B 2026](https://www.growthspreeofficial.com/blogs/dark-funnel-pipeline-impact-benchmarks-b2b-saas-b2b-2026-hidden-pipeline-acv-vertical-channel)
- [Oktopost — Dark social in B2B](https://www.oktopost.com/blog/dark-social-b2b-marketing)
- [Deloitte — B2B agentic commerce](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/b2b-agentic-commerce.html)
- [Cookie-Script — B2B vs B2C privacy 2026](https://cookie-script.com/guides/b2b-vs-b2c-privacy-in-2026-banner-for-b2b-leads)
