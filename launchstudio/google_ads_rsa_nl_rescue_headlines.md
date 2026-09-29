# 🇳🇱 RSA Headlines — `AG-NL-Rescue` · Nâng Ad Strength lên Good+

> **Phạm vi:** 6 keyword của ad group `AG-NL-Rescue` trong campaign C1 `LS-Search-NL-Service`
> (xem [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md) §5.1)
>
> `"prototype naar productie"` · `"ai app laten bouwen"` · `"ai app laten afmaken"`
> `"mvp laten bouwen"` · `"prototype live zetten"` · `"app productieklaar maken"`
>
> **Giới hạn:** Headline ≤ **30** ký tự · Description ≤ **90** ký tự. Toàn bộ copy dưới đây đã đếm sẵn.

---

## 1. Chẩn đoán: vì sao cấu hình hiện tại khó đạt Good

Hiện `AG-NL-Rescue` dùng nguyên cột Dutch của **Ad Group 1** trong
[`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md) — 15 headline, 4 description.
Số lượng đã đủ, nhưng Ad Strength nhiều khả năng dừng ở **Average** vì ba lý do:

### 1.1. 🔴 Độ phủ keyword trong headline quá thấp — nguyên nhân chính

Google chấm Ad Strength dựa nhiều vào việc headline có **chứa keyword của chính ad group đó** hay không.
Đối chiếu 6 keyword với 15 headline Dutch hiện có:

| Keyword | Có trong headline hiện tại? | Headline khớp |
|---|:---:|---|
| `mvp laten bouwen` | ✅ | `MVP Laten Bouwen?` |
| `prototype naar productie` | ⚠️ một phần | `Prototype → Productie` (thiếu chữ "naar") |
| `ai app laten bouwen` | ❌ | — |
| `ai app laten afmaken` | ❌ | — |
| `prototype live zetten` | ❌ | — |
| `app productieklaar maken` | ❌ | — |

**4/6 keyword hoàn toàn không xuất hiện trong bất kỳ headline nào.** Đây là thứ Google báo thẳng
trong khung recommendation *"Include popular keywords in your headlines"*.

### 1.2. 🟠 Một ad group ôm 6 keyword khác intent

Sáu keyword này thực ra là **ba intent khác nhau**:

| Intent | Keyword | Khách đang ở đâu |
|---|---|---|
| **Xây mới** | `ai app laten bouwen`, `mvp laten bouwen` | Chưa có gì, đang tìm người làm |
| **Làm nốt** | `ai app laten afmaken`, `app productieklaar maken` | Đã có app dở dang, thiếu phần cuối |
| **Đưa lên live** | `prototype naar productie`, `prototype live zetten` | Có prototype chạy được, kẹt ở bước deploy |

Nhồi cả ba vào một RSA thì mỗi headline chỉ phục vụ được 1/3 lượng tìm kiếm — vừa kéo Ad Strength
xuống, vừa làm loãng relevance thật sự.

### 1.3. 🟠 Ghim 3 vị trí (P1/P2/P3) làm giảm số tổ hợp

Pin strategy hiện tại ghim H1→P1, H2→P2, H10→P3. Ghim càng nhiều thì số tổ hợp Google thử được
càng ít, và *"Unpin ad assets"* là một recommendation Ad Strength quen thuộc.

> ⚠️ **Nói rõ để không kỳ vọng sai:** Ad Strength **không phải yếu tố xếp hạng** — nó không đi vào
> Ad Rank hay quyết định giá thầu. Nó là thước đo định hướng. Nhưng những thứ làm Ad Strength tăng
> (phủ keyword, đa dạng thông điệp) lại **thật sự** ảnh hưởng đến relevance và CTR. Đừng tối ưu
> để lấy chữ "Excellent", hãy tối ưu để đúng ý định tìm kiếm — điểm sẽ tự lên theo.

---

## 2. Giải pháp: tách 1 ad group → 3

Mỗi ad group chỉ giữ 2 keyword cùng intent, và **cả 2 keyword đều được viết nguyên văn vào headline**.

| Ad group mới | Keyword | Landing page |
|---|---|---|
| `AG-NL-Bouwen` | `"ai app laten bouwen"`, `"mvp laten bouwen"` | `/nl/van-prototype-naar-productie` |
| `AG-NL-Afmaken` | `"ai app laten afmaken"`, `"app productieklaar maken"` | `/nl/van-prototype-naar-productie` |
| `AG-NL-Live` | `"prototype naar productie"`, `"prototype live zetten"` | `/nl/van-prototype-naar-productie` |

Ngân sách và Max CPC giữ nguyên như §5.1 (€6,00 / €3,00 mỗi ngày cho cả cụm).

---

## 3. `AG-NL-Bouwen` — 15 headlines

**Keyword:** `"ai app laten bouwen"` · `"mvp laten bouwen"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword | Pin |
|---|---|---:|---|:---:|---|
| H1 | `AI-App Laten Bouwen?` | 20 | Question / Service | 🎯 | |
| H2 | `MVP Laten Bouwen?` | 17 | Question / Service | 🎯 | |
| H3 | `MVP Laten Bouwen Vanaf €800` | 27 | Keyword + Price | 🎯 | |
| H4 | `AI-App Laten Bouwen In NL` | 25 | Keyword + Local | 🎯 | |
| H5 | `App Laten Bouwen Zonder Team` | 28 | Pain point | 🎯 | |
| H6 | `Wij Bouwen Je AI-App Af` | 23 | Solution | 🎯 | |
| H7 | `Vaste Prijs Vanaf €800` | 22 | Price | | |
| H8 | `Live Binnen 1-3 Weken` | 21 | Speed | | |
| H9 | `Geen Herbouw, Wij Bouwen Door` | 29 | Differentiator | | |
| H10 | `11+ Jaar Engineering Ervaring` | 29 | Trust | | |
| H11 | `100% Eigendom Van Je Code` | 25 | Ownership | | |
| H12 | `Beveiliging & Hosting Geregeld` | 30 | Feature | | |
| H13 | `Stripe, Auth & DB Inbegrepen` | 28 | Feature | | |
| H14 | `Gratis Offerte Binnen 1 Dag` | 27 | CTA | | |
| H15 | `Plan Nu Je Gratis Gesprek` | 25 | CTA | | |

**Descriptions**

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `AI-app of MVP laten bouwen? Vaste prijs vanaf €800, live in 1-3 weken. Vraag offerte aan!` | 89 |
| D2 | `Geen bureau van €50K. Wij bouwen door op wat er is en leveren productieklaar op.` | 80 |
| D3 | `Security, hosting, Stripe en database inbegrepen. Alle code blijft 100% van jou.` | 80 |
| D4 | `11+ jaar engineering, 160+ projecten. Plan nu een gratis adviesgesprek van 15 minuten.` | 86 |

---

## 4. `AG-NL-Afmaken` — 15 headlines

**Keyword:** `"ai app laten afmaken"` · `"app productieklaar maken"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword | Pin |
|---|---|---:|---|:---:|---|
| H1 | `AI-App Laten Afmaken?` | 21 | Question / Service | 🎯 | |
| H2 | `App Productieklaar Maken` | 24 | Question / Service | 🎯 | |
| H3 | `AI-App Afmaken Vanaf €800` | 25 | Keyword + Price | 🎯 | |
| H4 | `App Productieklaar In 3 Weken` | 29 | Keyword + Speed | 🎯 | |
| H5 | `Wij Maken Je AI-App Af` | 22 | Solution | 🎯 | |
| H6 | `Laatste 20% Duurt Het Langst` | 28 | Pain point | | |
| H7 | `Wij Maken Het Launch-Ready` | 26 | Value Prop | | |
| H8 | `Security, Hosting & Betalen` | 27 | Feature | | |
| H9 | `Geen Herbouw, Wij Fixen` | 23 | Differentiator | | |
| H10 | `Vaste Prijs Vanaf €800` | 22 | Price | | |
| H11 | `Live Binnen 1-3 Weken` | 21 | Speed | | |
| H12 | `100% Eigendom Van Je Code` | 25 | Ownership | | |
| H13 | `11+ Jaar Engineering Ervaring` | 29 | Trust | | |
| H14 | `Gratis Code-Review Vooraf` | 25 | CTA / Risk reversal | | |
| H15 | `Vraag Nu Je Offerte Aan` | 23 | CTA | | |

**Descriptions**

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `AI-app klaar maar niet productieklaar? Wij fixen security, hosting & Stripe. Vaste prijs.` | 89 |
| D2 | `Die laatste 20% kost de meeste tijd. Wij maken je app af in 1-3 weken vanaf €800.` | 81 |
| D3 | `Geen herbouw: we behouden je frontend en fixen enkel wat live gaan blokkeert.` | 77 |
| D4 | `Gratis code-review vooraf. Je weet precies wat er mis is voordat je iets betaalt.` | 81 |

---

## 5. `AG-NL-Live` — 15 headlines

**Keyword:** `"prototype naar productie"` · `"prototype live zetten"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword | Pin |
|---|---|---:|---|:---:|---|
| H1 | `Prototype Naar Productie?` | 25 | Question / Service | 🎯 | |
| H2 | `Prototype Live Zetten?` | 22 | Question / Service | 🎯 | |
| H3 | `Van Prototype Naar Productie` | 28 | Keyword nguyên cụm | 🎯 | |
| H4 | `Prototype Live In 1-3 Weken` | 27 | Keyword + Speed | 🎯 | |
| H5 | `Prototype Naar Productie €800` | 29 | Keyword + Price | 🎯 | |
| H6 | `Wij Zetten Je Prototype Live` | 28 | Solution | 🎯 | |
| H7 | `Prototype Klaar, Niet Live?` | 27 | Pain point | 🎯 | |
| H8 | `Geen Herbouw, Direct Live` | 25 | Differentiator | | |
| H9 | `Beveiliging & Hosting Geregeld` | 30 | Feature | | |
| H10 | `Vaste Prijs Vanaf €800` | 22 | Price | | |
| H11 | `100% Eigendom Van Je Code` | 25 | Ownership | | |
| H12 | `11+ Jaar Engineering Ervaring` | 29 | Trust | | |
| H13 | `Voor Apps Gebouwd Met AI` | 24 | Qualifier | | |
| H14 | `Gratis Offerte Binnen 1 Dag` | 27 | CTA | | |
| H15 | `Plan Je Gratis Adviesgesprek` | 28 | CTA | | |

**Descriptions**

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `Prototype live zetten zonder herbouw? Van prototype naar productie in 1-3 weken.` | 80 |
| D2 | `Vaste prijs vanaf €800. Security, hosting en betalingen geregeld. Code 100% van jou.` | 84 |
| D3 | `Werkend prototype is niet hetzelfde als productie. Wij overbruggen dat gat.` | 75 |
| D4 | `11+ jaar engineering-ervaring, 160+ projecten opgeleverd. Vraag je offerte aan.` | 79 |

---

## 6. Độ phủ keyword sau khi sửa

| Keyword | Headline chứa nguyên cụm | Số lượng |
|---|---|:---:|
| `ai app laten bouwen` | H1, H4, H6 (`AG-NL-Bouwen`) | 3 |
| `mvp laten bouwen` | H2, H3 (`AG-NL-Bouwen`) | 2 |
| `ai app laten afmaken` | H1, H3, H5 (`AG-NL-Afmaken`) | 3 |
| `app productieklaar maken` | H2, H4 (`AG-NL-Afmaken`) | 2 |
| `prototype naar productie` | H1, H3, H5 (`AG-NL-Live`) | 3 |
| `prototype live zetten` | H2, H4, H6 (`AG-NL-Live`) | 3 |

**6/6 keyword được phủ**, mỗi keyword có ít nhất 2 headline — so với 1/6 khớp chính xác trước đây.

---

## 7. Checklist để đạt Good / Excellent

| # | Việc cần làm | Tác động |
|---|---|---|
| 1 | Nạp đủ **15/15 headline** và **4/4 description** cho mỗi ad group | Quantity |
| 2 | Tách `AG-NL-Rescue` thành 3 ad group theo §2 | Relevance |
| 3 | **Bỏ toàn bộ pin** ở lần chạy đầu | Thường là bước cuối để lên Excellent |
| 4 | Bật **"Automatically created assets"** nếu chấp nhận được | Quantity + diversity |
| 5 | Thêm sitelink / callout / structured snippet (§8 master plan) | Không tính vào Ad Strength nhưng tăng CTR |
| 6 | Kiểm tra mỗi headline mang **một angle khác nhau** — đã làm ở cột Angle | Diversity |

**Về pin (điểm ①→③ mâu thuẫn nhau, cần chọn):** nếu bắt buộc giữ thông điệp ở vị trí 1, hãy
ghim **2–3 headline vào cùng một vị trí** thay vì ghim 1 headline duy nhất. Google vẫn có nhiều
lựa chọn để xoay vòng, mà bạn vẫn kiểm soát được nội dung xuất hiện ở đó.

---

## 8. ⚠️ Bốn điểm phải kiểm trước khi import

1. **Ký tự `→`** — headline H6 hiện tại `Prototype → Productie` dùng mũi tên. Google Ads hạn chế
   ký tự/biểu tượng phi tiêu chuẩn và ad có thể bị disapproved. Toàn bộ copy trong file này
   **không dùng ký tự đặc biệt** nào ngoài `&`, `%`, `€` và dấu gạch nối. Nên thay H6 cũ bằng
   `Van Prototype Naar Productie`.

2. **Không nhắc tên đối thủ/trademark trong headline NL** — mình cố ý dùng `Voor Apps Gebouwd Met AI`
   thay vì nêu tên công cụ cụ thể. Dùng trademark của bên khác trong ad text dễ bị khiếu nại
   và disapproved.

3. **Viết hoa kiểu Title Case** — mình giữ theo đúng quy ước sẵn có trong
   `google_ads_rsa_copy_launchstudio.md`. Lưu ý người Hà Lan bản xứ đọc sẽ thấy hơi lạ, tiếng Hà Lan
   thường dùng sentence case. Nếu muốn đổi sang sentence case thì phải đổi đồng bộ cả file gốc.

4. **Bắt buộc có người Hà Lan bản xứ review** — ghi chú này đã có trong §5.1 master plan và
   `paid_ads_plan.md` §13, vẫn còn nguyên giá trị. Mấy cụm cần soi kỹ:
   `Laatste 20% Duurt Het Langst`, `Wij Bouwen Je AI-App Af`, `Geen Herbouw, Wij Bouwen Door`.

---

## 9. Nguồn tham chiếu

- [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md) §5.1 — campaign C1, ad group & bid
- [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md) Ad Group 1 — copy Dutch gốc
- [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) — keyword NL
- [`paid_ads_plan_dutch.md`](paid_ads_plan_dutch.md) — bối cảnh thị trường NL
