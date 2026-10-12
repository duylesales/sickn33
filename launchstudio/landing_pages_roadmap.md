# 🗺️ Roadmap landing page + CTA — đề xuất bổ sung

> **Ngày:** 12/10/2026
> **Nguồn số liệu:** `volume_analysis_results.md` · `keyword_seeds_3_ai_brands_NL.csv` · `keyword_volume_developer_inhuren_nl.csv` · `google_ads_plan_payments_nl.md`
> **Đã có brief:** `/ai-app-vibe-coding` (pillar) · `/ai-app-security` · `/ai-app-integrations` · `/ai-app-into-production`

---

## 1. 🔴 Phát hiện: cụm có volume lớn nhất đang không có trang nào

Toàn bộ keyword đã có volume thật từ Keyword Planner, đối chiếu với 4 trang đã brief:

| Volume | Keyword | Ngôn ngữ | Có landing page? |
|---:|---|---|---|
| **480** | `app laten maken` | NL | ❌ |
| **260** | `webapplicatie laten maken` | NL | ❌ |
| **210** | `replit agency` | EN | ⚠️ nghi vấn — xem §6 |
| **140** | `app laten bouwen` | NL | ❌ |
| **110** | `software laten maken` | NL | ❌ |
| **90** | `maatwerk software laten maken` | NL | ❌ |
| **50** | `mvp laten maken` | NL | ❌ |
| **40** | `technische due diligence` | NL | ⚠️ chỉ là 1 section trong `/ai-app-security` |
| **30** | `mvp ontwikkeling` | NL | ❌ |
| 20 | `app laten maken rotterdam` | NL | ❌ |
| 20 | `app laten maken eindhoven` | NL | ❌ |
| 20 | `developer inhuren app` | NL | ❌ |
| 10 | `webapp laten bouwen` · `app laten maken utrecht` · `pentest webapplicatie` · `bolt new developer` | NL/EN | ❌ |

**Cộng lại: ~1.280 lượt/tháng tiếng Hà Lan không có đích đến.**

Trong khi đó bốn trang đã brief phục vụ:

| Trang | Volume KP xác nhận |
|---|---:|
| `/ai-app-security` | ~70 |
| `/ai-app-into-production` | ~10 |
| `/ai-app-integrations` | chưa có số KP |
| `/ai-app-vibe-coding` | chưa có số KP |

> 🔴 **Tỉ lệ đang ngược hoàn toàn.** Bốn trang đã đầu tư brief đầy đủ phục vụ ~80 lượt/tháng. Cụm 1.280 lượt/tháng chưa có một trang nào.

### Nhưng đây không phải "cứ làm trang là xong"

`volume_analysis_results.md` §5 đã cảnh báo đúng: 1.080/1.280 volume của N1 là người muốn **xây mới**, không phải người có prototype dang dở. Ở CAC €1.600–2.000, gói Launch Ready €800 lỗ nặng.

Và §6.2 đã khuyến nghị **Hướng B** (không dựa vào Search Ads cho luận điểm này) làm chính.

**Tôi không phản đối kết luận đó. Nhưng nó không dẫn tới "đừng làm trang".** Ba lý do:

**① Cụm này là cụm duy nhất có volume organic.** Dù chọn Hướng B — nội dung/SEO/cộng đồng — thì vẫn phải có một trang để rank cho `app laten maken`. Không có trang thì Hướng B cũng không có đích.

**② Sự lệch ICP là bài toán thiết kế trang, không phải lý do bỏ cụm.** Người gõ `app laten maken` chưa nói họ có gì. Một phần trong số đó **đã có prototype** nhưng không diễn đạt bằng từ đó — vì như chính §1 của `volume_analysis_results.md` chứng minh, không ai gõ "làm nốt prototype".

**③ Trang có thể tự phân loại ngay ở màn hình đầu.** Đây là cách gỡ bế tắc ở §6.2:

> Hero hỏi một câu duy nhất: **"Heb je al iets gebouwd?"** (Bạn đã xây gì chưa?)
>
> → **Ja** → luồng prototype rescue, dẫn sang `/ai-app-vibe-coding` + 3 spoke. Tỉ lệ chốt cao, đúng ICP.
> → **Nee** → luồng báo giá xây mới. Bán được thì bán, không thì lọc ra ngay.

Chỉ số quyết định mà §6.2 yêu cầu — *tỉ lệ lead đã có prototype sẵn* — **được đo trực tiếp bằng chính nút này**, không cần đoán từ nội dung form. Nếu dưới 30% chọn "Ja" sau 8 tuần, bạn có câu trả lời dứt khoát cho Hướng A/B.

---

## 2. 🔴 P0 — Trang bắt buộc phải có trước mọi trang khác

### `/audit-aanvragen` (NL) + `/request-audit` (EN) — trang nhận chuyển đổi

**Đây là phụ thuộc cứng của cả bốn trang đã brief, và hiện chưa tồn tại.**

`landing_ai_app_security_brief.md` v2 đã bỏ form khỏi trang và đặt:

```js
const CTA_URL = "https://launchstudio.eu/en/#contact";
```

Ba vấn đề với đích đó:

| Vấn đề | Hậu quả |
|---|---|
| `/en/#contact` là form trang chủ — **không đọc URL param** | `created_before`, `risk_score`, `exposed`, `reason` bị thu thập rồi **ném đi** |
| Không khớp thông điệp | Người bấm *"Close my 4 gaps"* đáp xuống một form liên hệ chung chung → tụt chuyển đổi |
| Phá cơ chế đo lường | Thủ thuật "mọi form từ URL này là từ ads" ở `conversion_attribution_setup.md` §6 mất tác dụng |

**Trang này cần:**

- Tiêu đề **động theo param**: `created_before=yes` → *"Your project was in the exposed window. Let's check it."* · `reason=investor_dd` → *"Due diligence prep — tell us your timeline."* · `risk_score=4` → *"Four gaps to close."*
- Hiển thị lại kết quả người dùng vừa tự chấm (bằng chứng họ đã đầu tư công sức → giảm tỉ lệ bỏ form)
- Form ngắn, có trường ngân sách bắt buộc
- Hidden field: `click_id`, `click_type`, `landing`, `source`, cộng toàn bộ param của 4 trang
- `noindex` — đây là trang chuyển đổi, không phải trang nội dung

> 💡 Một trang này phục vụ cả bốn landing page. Làm nó trước, nếu không toàn bộ dữ liệu phân loại lead mà bốn trang kia dày công thu thập sẽ không đi tới đâu.

---

## 3. P1 — Cụm NL xây mới (~1.230 lượt/tháng)

| # | Trang | Keyword chính | Volume | Ghi chú |
|---|---|---|---:|---|
| 1 | **`/app-laten-maken`** | `app laten maken` · `app laten bouwen` · `webapp laten bouwen` | **630** | 🥇 Trang quan trọng nhất chưa có. H1 phải chứa nguyên keyword |
| 2 | **`/webapplicatie-laten-maken`** | `webapplicatie laten maken` | **270** | Tách riêng, không gộp vào trang 1 — H1 phải khớp keyword |
| 3 | **`/software-laten-maken`** | `software laten maken` · `maatwerk software laten maken` | **200** | `maatwerk` = tuỳ chỉnh, ý định B2B cao hơn |
| 4 | **`/mvp-laten-maken`** | `mvp laten maken` · `mvp ontwikkeling` | **80** | ICP khớp nhất trong nhóm P1 — người làm MVP gần với prototype rescue nhất |

**Cả bốn trang dùng chung một khung**, chỉ đổi H1, ví dụ và case study:

```
H1 = nguyên văn keyword
→ Câu hỏi phân loại: "Heb je al iets gebouwd?" [Ja / Nee]
→ Ja  → luồng rescue, link sang /ai-app-vibe-coding
→ Nee → quy trình + dải giá + form
→ Giá công bố (lợi thế: bureau NL hầu hết không công bố)
→ Case study NL
→ CTA → /audit-aanvragen
```

> 🔴 **Đừng gộp bốn trang thành một.** `google_ads_plan_payments_nl.md` §10 đã nêu đúng nguyên tắc: *"H1 chứa nguyên keyword — khớp headline, nâng Landing page experience"*. Một trang chung tên "Apps & software" sẽ có Landing Page Experience kém cho cả bốn truy vấn, đẩy CPC lên cho cùng một vị trí.

### P1b — Trang thành phố (~50–70 lượt/tháng, CPC thấp)

`app laten maken rotterdam` 20 · `eindhoven` 20 · `utrecht` 10 · `amsterdam` (dưới 10)

Dùng template của trang 1, thay proof địa phương. Rẻ, CPC thường thấp hơn truy vấn chung.

> ⚠️ **Chỉ làm cho `app laten maken` + thành phố.** `mvp laten maken amsterdam` = 0 và `softwarebureau amsterdam` = 0 — pattern thành phố không áp cho mọi dịch vụ.
>
> ⚠️ Và chỉ làm nếu có **proof địa phương thật** (khách ở thành phố đó). Trang thành phố rỗng nội dung là doorway page, Google phạt.

---

## 4. P2 — `/technische-due-diligence` (NL): tách khỏi section thành trang riêng

| | |
|---|---|
| Volume | **40/tháng** — cao nhất trong toàn bộ cụm security |
| Giá trị đơn hàng | **Cao nhất trong cả ba cụm** (research §4.3) |
| Hiện trạng | Chỉ là **S5** bên trong `/ai-app-security` |

Ba lý do nên tách:

**① Đối tượng khác hẳn.** Founder đang gọi vốn, hoặc investor đang soi target. Họ không đến từ nỗi lo "ai đọc được dữ liệu của tôi" — họ đến từ một deadline.

**② Thuật ngữ chuẩn giới VC/M&A Hà Lan.** `technische due diligence` là từ họ dùng trong nội bộ. H1 phải là chính nó, không thể là một section nằm dưới `Make your data private again`.

**③ Đây là cụm scanner không vào được.** vibeappscanner không ký được báo cáo gửi investor. Đây là góc phòng thủ bền nhất của launchstudio trong cụm security.

Cộng thêm `pentest webapplicatie` 10 — nhưng ⚠️ research đã cảnh báo cụm này kéo khách enterprise ngoài ICP. Nhắc trong trang, đừng bid.

---

## 5. P3 — Sáu trang PSP (đã có plan, chưa làm)

`google_ads_plan_payments_nl.md` §10 đã đề xuất đầy đủ. Nhắc lại thứ tự để không bị quên khi làm `/ai-app-integrations`:

| Ưu tiên | Trang | Lý do trong plan |
|---|---|---|
| 1 | `/nl/ideal-integratie` | 18 kw, chứa `stripe ideal` **260** |
| 2 | `/nl/betaalprovider-kiezen` | 8/9 kw là P1, ý định tư vấn cao nhất |
| 3 | `/nl/wero-webshop` | Cửa sổ first-mover |
| 4–6 | `/nl/paypal-webshop` · `/nl/mollie-integratie` · `/nl/multisafepay-koppelen` | |

> 🔴 `/ai-app-integrations` là **hub**, sáu trang này là **spoke**. Không thay thế nhau — xem `landing_ai_app_integrations_brief.md` §1.

---

## 6. P4 — Hai trang cần verify trước khi đầu tư

### `/developer-inhuren` (NL) — 510/tháng nhưng mô hình kinh doanh khác

`keyword_volume_developer_inhuren_nl.csv`: 510/tháng, trong đó **290 khớp stack**. Trần chi chỉ **€121/tháng**.

Nhưng như `keyword_volume_developer_inhuren_nl.md` §4 đã phân tích: đây là ý định **detachering** (thuê người theo giờ), không phải giao dự án. Bán nó nghĩa là cạnh tranh với Yacht/Brunel, margin mỏng, mất quyền kiểm soát chất lượng.

**Đề xuất:** làm **một** trang, dùng làm cửa vào rồi chuyển hướng sang mô hình dự án — *"Thuê developer thì bạn phải tự quản lý. Giao kết quả thì không."* Không mở dòng sản phẩm detachering.

### ⚠️ `replit agency` — 210/tháng, chưa rõ nghĩa

Đây là từ có volume cao thứ ba toàn tài khoản, và `volume_analysis_results.md` §6.1 mục 6 đã đánh dấu **bất thường**:

> *"Truy vấn này nghĩa là gì chưa rõ — có thể người tìm chương trình agency của chính Replit. Chạy Exact match riêng, đọc Search Terms 1 tuần trước khi tin."*

**Đừng làm trang cho nó trước khi đọc Search Terms report.** 210 lượt/tháng là đáng kể, nhưng nếu đó là người tìm Replit's own agency program thì một trang sẽ không chuyển đổi được gì — giống hệt bẫy `lovable agency partner` và `lovable expert program` đã phát hiện ở `landing_ai_app_vibe_coding_brief.md` §3.

---

## 7. 🎯 CTA — bốn chỗ còn thiếu

### ① Không có bậc thang cam kết thấp

Cả bốn trang có **một** CTA duy nhất: gửi form / xin audit. Người đã tự chấm điểm ở thước đo S3 nhưng **chưa sẵn sàng nói chuyện** sẽ rời trang và không để lại gì.

**Thêm CTA phụ ngay cạnh thước đo:**

> `Email me my results` — chỉ xin email, gửi lại bản PDF kết quả tự chấm kèm 6 bước tự kiểm.

Ba lợi ích: bắt được email của nhóm chưa sẵn sàng · email đó là cớ tự nhiên để follow-up · và nó biến thước đo từ một món đồ chơi thành một lead magnet.

### ② Không có lựa chọn đặt lịch

Form là bất đồng bộ. Một phần khách muốn nói chuyện ngay.

**Thêm:** `Book 15 minutes` (Calendly) làm CTA phụ ở S4 và S9. Trang `/services/ai-development` của unicoconnect dùng đúng cặp này — form + Calendly song song — và đó là cách phục vụ hai tính cách mua khác nhau mà không tăng chi phí.

### ③ Không có CTA riêng cho phân khúc agency / white-label

`landing_ai_app_vibe_coding_brief.md` S3 card 3 đã nhận diện phân khúc *"Agencies holding a client's vibe-coded app"* — nhưng không có CTA nào dành cho họ.

Đây là phân khúc có giá trị khác hẳn: lặp lại, nhiều dự án, và họ cần **NDA + white-label** chứ không cần thuyết phục về giá.

**Thêm:** một dòng ở cuối trang pillar — `Working on a client's app? We work white-label.` → link tới một trang hoặc một mailto riêng.

### ④ Không có CTA dính (sticky) trên mobile

Bốn trang đều dài (9–10 section). Trên mobile, CTA chính ở hero bị cuộn mất sau màn hình đầu, và CTA cuối cách đó rất xa.

**Thêm:** thanh CTA dính ở đáy, xuất hiện sau khi cuộn qua 30% trang, ẩn khi section form/CTA cuối vào khung nhìn. Một nút, nhãn theo trang.

> ⚠️ Giữ nó mảnh (48–56px) và có nút đóng. Thanh dính che nội dung trên màn hình 360px sẽ làm hại nhiều hơn lợi.

---

## 8. Thứ tự thực thi đề xuất

| Ưu tiên | Việc | Lý do |
|---|---|---|
| **P0** | `/audit-aanvragen` + `/request-audit` | Phụ thuộc cứng của cả 4 trang đã brief. Không có nó, dữ liệu phân loại lead bị ném đi |
| **P0** | 4 bổ sung CTA ở §7 | Rẻ, áp cho cả 4 trang hiện có |
| **P1** | `/app-laten-maken` (630) | Trang có volume lớn nhất đang trống |
| **P1** | `/ai-app-vibe-coding` (pillar) | Để 3 spoke có chỗ bám — xem brief §1 |
| **P2** | `/webapplicatie-laten-maken` (270) · `/software-laten-maken` (200) | |
| **P2** | `/technische-due-diligence` (40, đơn lớn nhất) | Tách khỏi section |
| **P3** | `/ai-app-security` · `/nl/ideal-integratie` (260) | |
| **P4** | `/mvp-laten-maken` (80) · trang thành phố · `/developer-inhuren` | |
| **Verify** | `replit agency` (210) | Đọc Search Terms 1 tuần trước khi làm trang |

> 💡 **Một nhận định tổng thể, nói thẳng:** bốn trang đã brief đều thuộc câu chuyện vibe-coding/rescue — câu chuyện mà chính dữ liệu của bạn cho thấy **chỉ có ~80 lượt tìm/tháng**. Chúng đáng làm vì giá trị GEO và vì là định vị thật của launchstudio. Nhưng nếu mục tiêu là pipeline trong hai quý tới, **cụm `laten maken` 1.230 lượt/tháng mới là chỗ có người đang tìm**, và nó chưa có một trang nào.
>
> Cách hoà giải hai thứ nằm ở câu hỏi phân loại *"Heb je al iets gebouwd?"* ở §1③ — nó cho bạn đi theo volume mà không phải đổi định vị.

---
---

# 📍 Phần 2 — Sáu hướng bổ sung (harvest 12/10/2026)

> Harvest thêm 56 seed tiếng Hà Lan (`hl=nl`, `gl=nl`) → 343 gợi ý. Dưới đây là những hướng **chưa có trong Phần 1**.

---

## 9. 🔴 Phát hiện quan trọng nhất: thương hiệu `Launch Studio` là từ đồng âm nặng

Autocomplete cho `launch studio` / `launchstudio`:

```
launchstudio.bluetooth.com                 launch studio bluetooth
launch studio bluetooth 75270              launch studio bluetooth driver
launch studio bluetooth 5.0 driver download
launch studio bluetooth com listing details 75270
launch studio azure       launch studio roblox
launch studio st albans   launch studio sa
```

**`Launch Studio` là nền tảng đăng ký sản phẩm chính thức của Bluetooth SIG** (`launchstudio.bluetooth.com`). Nó chiếm gần như toàn bộ cụm thương hiệu: người tìm listing ID, tải driver Bluetooth, tra cứu chứng nhận.

Thêm `launch studio roblox` (Roblox Studio), `launch studio azure`, và `launch studio st albans` (một studio vật lý ở Anh).

Và `launchstudio reviews` **không trả về gợi ý nào** — nghĩa là thương hiệu hiện gần như chưa có volume riêng.

### Ba hệ quả

| | |
|---|---|
| **Ads** | 🔴 **Đừng bid `launch studio` dạng Phrase.** Sẽ đốt tiền vào engineer Bluetooth tìm driver. Chỉ Exact `launchstudio.eu`, và đọc Search Terms 2 tuần trước khi mở rộng |
| **SEO/GEO thực thể** | Google và LLM sẽ khó gán thực thể "Launch Studio" cho công ty này, vì Bluetooth SIG đã sở hữu cái tên. Đây là lý do `sameAs` + Wikidata + `Organization` schema quan trọng hơn bình thường |
| **Thương hiệu** | Nên viết **`LaunchStudio.eu`** hoặc `LaunchStudio` liền một từ ở mọi nơi, không viết `Launch Studio` rời hai từ |

> 💡 Đối chiếu với unicoconnect: ở đó thương hiệu bị người tìm việc chiếm. Ở đây bị một tổ chức lớn hơn ở ngành hoàn toàn khác chiếm. Trường hợp thứ hai khó gỡ hơn, nhưng cũng có nghĩa **không cần ngân sách phòng thủ brand** — vì chưa có ai tìm bạn để mà mất.

---

## 10. 🥇 `/eigen-code-eigen-hosting` — trang thoát khoá nhà cung cấp

Cụm validate tốt nhất trong lần harvest này, và là **một ý định hoàn toàn khác** với bốn trang đã brief:

```
can lovable export code              does lovable export code
can you export lovable code to github
lovable ai export code               export database lovable
export lovable code to wordpress
bolt new export code                 bolt new export database
bolt new export project              bolt new export to github
how to export replit database        how to export apk from replit
lovable alternative self hosted      lovable alternative local
lovable alternatives                 app migratie
```

### Vì sao cụm này mạnh về thương mại

| | |
|---|---|
| **Ý định rõ** | Không phải "app tôi có an toàn không" mà **"cho tôi ra khỏi nền tảng này"** — họ đã quyết định hành động |
| **Phạm vi gọn** | Một dự án một lần, dễ báo giá, dễ chốt |
| **Có nguồn nội dung sẵn** | `moving-a-replit-app-to-your-own-infrastructure` · research §2.5 "Export, GitHub & Lock-in" |
| **Dạng câu hỏi cho GEO** | `can lovable export code`, `does lovable export code` — LLM trả lời đúng loại truy vấn này |
| **Research đã xếp Tier A** | `replit export to vercel` (§3.3 #86) |

### Góc nên chọn

Không phải "Lovable khoá bạn lại" — mà **"code là của bạn, hãy chạy nó ở nơi bạn kiểm soát"**. Tông giọng tôn trọng công cụ, giống nguyên tắc ở `/ai-app-security`.

Nội dung: export được gì / không export được gì · chuyện gì vỡ sau khi export (env var, edge function, RLS, webhook) · Supabase self-hosted hay managed · chi phí hosting thật.

> ⚠️ `lovable alternatives` cũng validate, nhưng **đừng làm trang so sánh công cụ.** Người gõ nó đang chọn công cụ, không thuê agency — và đó là cụm vibeappscanner/vibe-eval đã chiếm. Chỉ lấy phần `self hosted` / `local`.

---

## 11. 🥇 Trang chi phí — và một cái bẫy rất dễ sập

Cụm validate:

```
app laten maken kosten          app laten maken prijs
app maken prijs                 mvp prijs
wat kost een app laten maken    wat kost een app laten bouwen
wat kost een app laten ontwikkelen
app onderhoud kosten            onderhoudskosten app
```

### 🔴 Bẫy: `wat kost een app` trần kéo về căn hộ, cây táo và Apple

```
wat kost een appartement            wat kost een appartement in dubai
wat kost een appartement in spanje  wat kost een appartement op curacao
wat kost een appelboom              wat kost een appelflap bij de bakker
wat kost een apple iphone 17        wat kost een apple watch
wat kost een apple tv abonnement    wat kost een apple laptop
```

`app` là tiền tố của **appartement**, **appel** và **apple** trong tiếng Hà Lan. Bid `wat kost een app` ở Phrase sẽ trả tiền cho người hỏi giá căn hộ ở Dubai và bánh táo ở lò bánh.

**Dạng an toàn — bắt buộc có động từ đi kèm:**
`wat kost een app laten maken` · `laten bouwen` · `laten ontwikkelen` · `app laten maken kosten` · `app laten maken prijs`

### Vì sao trang này đáng làm

Ba lý do, và lý do thứ ba là lợi thế riêng:

1. **Ý định mua cao** — người hỏi giá là người có ngân sách và đang ở giai đoạn quyết định
2. **GEO rất mạnh** — LLM trích dẫn số liệu giá cụ thể hơn bất kỳ loại nội dung nào khác
3. **Bureau Hà Lan hầu hết không công bố giá** — launchstudio đã công bố. Đây là trang biến sự minh bạch đó thành traffic

Trang chủ đã có công cụ tính giá (*"Wat kost jouw project? Reken het uit."*) nhưng nó là **anchor trên trang chủ**, không phải URL riêng — nên nó không rank được cho cụm này và không dùng được làm đích ads.

> 💡 Tách công cụ tính giá đó ra thành `/wat-kost-een-app-laten-maken`. Nội dung đã có, chỉ cần một URL riêng với H1 khớp keyword.

---

## 12. ⚠️ WBSO / MIT subsidie — cầu rất thật, nhưng cơ chế phải xác minh

### Cầu đã validate

```
wbso aanvragen        wbso aanvragen 2026     wbso ai
wbso ontwikkeling     wbso voorwaarden        wbso forfaitair uurloon
subsidie software ontwikkeling                software subsidie
mit subsidie ai       mit subsidie r&d        mit subsidie aanvragen
mit subsidie 2026 + 8 biến thể tỉnh (noord-brabant, gelderland, zuid-holland,
  noord-holland, utrecht, overijssel, flevoland)
```

`wbso ai` và `mit subsidie ai` đều validate — đúng loại dự án launchstudio làm. Và 8 biến thể tỉnh là cơ hội trang địa phương có nội dung khác biệt thật.

### Vì sao đòn bẩy này mạnh

**MIT Haalbaarheid trả 35% chi phí đủ điều kiện, tối đa €20.000/dự án.** So với gói Launch Ready €800–3.500 của launchstudio, đó là mức có thể thay đổi hoàn toàn quyết định mua — và nó sửa đúng bài toán CAC €1.600–2.000 ở `volume_analysis_results.md` §5.

### 🔴 Nhưng cơ chế không đơn giản — và đây là chỗ dễ tư vấn sai

**WBSO:** dành cho công tác R&D do **nhân sự của chính doanh nghiệp** thực hiện (gắn với thuế lương). Việc lập trình **thuê ngoài nói chung không đủ điều kiện**.

Có một ngoại lệ: theo một phán quyết của College van Beroep voor het bedrijfsleven, nếu **giai đoạn thiết kế kỹ thuật do nhân sự của khách tự làm** và phần lập trình thuê ngoài, khách vẫn có thể được WBSO. Nhưng cách giải thích thực tế của **RVO hẹp hơn** phán quyết đó.

➡️ **launchstudio tuyệt đối không được nói "công việc của chúng tôi đủ điều kiện WBSO".** Đó là tuyên bố sai và tạo rủi ro cho cả hai bên.

**MIT Haalbaarheid 2026:** cửa sổ nộp đã đóng (7/4 – 15/9/2026, và ngân sách dự kiến cạn ngay ngày đầu). Chu kỳ tiếp theo là 2027 — nghĩa là làm trang bây giờ có thời gian chuẩn bị tốt. Tôi **chưa xác minh được** chi phí thuê ngoài có nằm trong "kosten derden" đủ điều kiện hay không.

### Cách làm đúng

| ✅ Được | ❌ Không được |
|---|---|
| *"Chúng tôi xây theo cách khớp với những gì các chương trình này tài trợ"* | *"Dự án của bạn được WBSO 30%"* |
| *"Thiết kế kỹ thuật do team bạn sở hữu; chúng tôi triển khai"* | Tự nhận là tư vấn subsidie |
| Dẫn sang cố vấn WBSO/MIT thật | Tự tính số tiền khách sẽ nhận |

> 💡 **Hướng đi tốt hơn một landing page: đối tác giới thiệu.** Các hãng tư vấn subsidie Hà Lan — Hezelburcht, Leyton, Moore DRV — đều xuất hiện ở đầu kết quả cho những truy vấn này. Họ **có khách cần làm phần phát triển**, và họ không làm phát triển. Đó là kênh giới thiệu hai chiều, không phải đối thủ.
>
> Việc nên làm trước: một cuộc gọi với một hãng trong số đó, trước khi viết một dòng nội dung nào về subsidie.

---

## 13. ✏️ Hai ý tôi tự loại sau khi kiểm dữ liệu

Nêu ra để không ai mất thời gian làm lại.

### `/app-onderhoud` — trang retainer: đúng về chiến lược, sai về kênh

**Về chiến lược nó quan trọng nhất trong cả danh sách:** doanh thu định kỳ là thứ duy nhất sửa được bài toán CAC. Một retainer biến CAC €1.600 từ chỗ lỗ trên gói €800 thành có lãi.

**Nhưng cụm từ khoá tiếng Hà Lan gần như không dùng được:**

```
ing app onderhoud        belfius app onderhoud      digid app onderhoud
knab app onderhoud       odido app onderhoud        ovpay app onderhoud
crelan app onderhoud     betcity app onderhoud
    ↑ toàn bộ là "app của ngân hàng/telco đang bảo trì"
app onderhoud auto · app onderhoud huis · app onderhoud planten
    ↑ app theo dõi bảo dưỡng xe, nhà, cây
machine onderhoud software · onderhoudsplanning software · onderhoudsbeheer software
    ↑ phần mềm quản lý bảo trì (CMMS) — ngành khác hẳn
```

➡️ **Xây trang retainer cho upsell khách hiện có, không làm đích ads.** Dạng còn dùng được rất hẹp: `app onderhoud kosten`, `onderhoudskosten app`, `doorontwikkeling software`, `onderhoudscontract software`.

### `/second-opinion` — chết hẳn trong tìm kiếm

Ý tưởng là một sản phẩm mồi giá thấp: *"Ai đó đã build cái này cho bạn. Muốn một ý kiến thứ hai không?"* — giải đúng vấn đề giá vào cửa €800 quá cao so với CAC.

Nhưng autocomplete cho `second opinion code`:

```
second opinion cpt code      second opinion icd 10 code
second opinion ada code      second opinion cdt code
second opinion billing code  second opinion pathology cpt code
second opinion diagnosis code
```

**Toàn bộ là mã thanh toán y tế.** `second opinion + code` thuộc hẳn về ngành bảo hiểm y tế Mỹ.

➡️ **Giữ "second opinion" làm sản phẩm và làm CTA, bỏ hẳn ý định làm trang bắt tìm kiếm.** Nó vẫn là cách tốt để hạ ngưỡng vào cửa — chỉ là không ai google nó.

Hai dạng NL còn sống, nhưng mỏng: `app overnemen`, `broncode overdragen`.

---

## 14. Cập nhật thứ tự thực thi

| Ưu tiên | Việc | Thay đổi so với Phần 1 |
|---|---|---|
| **P0** | `/request-audit` + 4 bổ sung CTA | giữ nguyên |
| **P1** | `/app-laten-maken` (630) · `/ai-app-vibe-coding` pillar | giữ nguyên |
| **P1+** | **`/wat-kost-een-app-laten-maken`** | 🆕 Nội dung đã có trên trang chủ, chỉ cần tách URL. Rẻ nhất trong nhóm P1 |
| **P2** | `/webapplicatie-laten-maken` (270) · `/software-laten-maken` (200) · `/technische-due-diligence` (40) | giữ nguyên |
| **P2+** | **`/eigen-code-eigen-hosting`** | 🆕 Ý định riêng, cụm validate tốt, nội dung đã có |
| **P3** | `/ai-app-security` · `/nl/ideal-integratie` (260) | giữ nguyên |
| **P4** | `/mvp-laten-maken` (80) · trang thành phố · `/developer-inhuren` | giữ nguyên |
| **Verify** | `replit agency` (210) · **WBSO/MIT qua một hãng tư vấn** | 🆕 thêm mục WBSO |
| **Không làm** | ~~`/app-onderhoud` làm đích ads~~ · ~~`/second-opinion`~~ · ~~bid brand Phrase~~ | 🆕 ba mục đã loại |
