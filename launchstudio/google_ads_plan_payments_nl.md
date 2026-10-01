# 💳 Google Search Ads Plan — iDEAL / PayPal / PSP Hà Lan

> **Nguồn:** `ideal-paypal_google_ads_keywords_en_nl.csv` — 4 keyword Keyword Planner (mỗi từ 10 lượt/tháng, Low competition)
> **Đích:** launchstudio.eu · **Ngày:** 01/10/2026
> **Yêu cầu:** headline phải thực tế đạt **Ad Strength ≥ Good** → §5
> **File kèm:** `payments_nl_keywords_validated.csv` (58 kw) · `kp_upload_payments_nl.txt`
> **Đã verify bằng script:** 6 ad group · 90 headline · 24 description · **6/6 đạt Good+, 0 vi phạm** · 58/58 keyword xác nhận bằng Autocomplete

---

## 1. Vấn đề đầu tiên: 4 keyword = 40 lượt/tháng, không đủ để chạy

| Keyword gốc | Lượt/tháng | Cạnh tranh | CPC |
|---|---:|---|---|
| `ideal integratie` | 10 | Low | — |
| `ideal koppelen` | 10 | Low | — |
| `paypal integratie` | 10 | Low | — |
| `paypal koppelen` | 10 | Low | — |
| **Tổng** | **40** | | |

Ở 40 lượt/tháng với Impression Share 60% và CTR 5%, bạn mua được khoảng **1,2 click/tháng**. Không có campaign nào chạy được trên con số đó.

Nên trước khi viết plan, mình làm hai việc: **kiểm ý định thật của 4 từ này**, và **mở rộng pattern** sang các nhà cung cấp Hà Lan khác. Cả hai đều bằng Google Autocomplete (`hl=nl&gl=nl`) — nguồn chỉ gợi ý truy vấn thật sự có người gõ.

---

## 2. 🔴 Kiểm ý định: 2 trong 4 keyword gốc là người tiêu dùng, không phải khách

### `paypal koppelen` — bỏ hẳn

Google gợi ý **10/10 là người tiêu dùng nối PayPal với ngân hàng hoặc ví của họ:**

```
paypal koppelen aan bankrekening          paypal koppelen aan rabobank
paypal koppelen aan google pay            paypal koppelen aan ing
paypal koppelen aan bankrekening veilig   paypal koppelen aan apple pay
paypal koppelen aan rabobank lukt niet    paypal koppelen aan tiktok
paypal koppelen aan abn amro
```

Không một gợi ý nào là doanh nghiệp muốn **nhận** thanh toán PayPal. Đây là người đã có PayPal và đang cố nối nó với thẻ/ngân hàng của mình. Họ cần hỗ trợ của PayPal hoặc của ngân hàng, không cần developer.

### `paypal integratie` — Autocomplete trả về **rỗng hoàn toàn**

Không gợi ý gì, kể cả chính nó. Keyword Planner ghi 10 lượt/tháng, nhưng 10 là mức sàn làm tròn của Google (nghĩa là *dưới 10*). Kết hợp hai dấu hiệu: cụm này gần như không tồn tại trong tiếng Hà Lan.

### `ideal koppelen` — ý định lẫn, 7/10 là người tiêu dùng

```
❌ ideal koppelen aan prive rekening    ❌ ideal koppelen aan apple id
❌ ideal koppelen aan paypal            ❌ ideal koppelen aan revolut
❌ ideal koppelen aan creditcard        ❌ ideal koppelen aan google pay
✅ ideal koppelen aan webshop           ✅ ideal koppelen aan website
```

Dùng được, nhưng **phải để Exact match và chặn nặng** — hoặc tốt hơn: bid thẳng hai biến thể dài `ideal koppelen aan webshop` và `ideal koppelen aan website`, vốn đã sạch sẵn.

### `ideal integratie` — ✅ từ duy nhất sạch

Autocomplete chỉ trả về `ideal integratie` và `ideal integratie website`. Cả hai đều là doanh nghiệp. Đây là từ tốt nhất trong 4 seed.

> 💡 **Bài học áp dụng được cho mọi keyword thanh toán: động từ quyết định ý định, không phải danh từ.**
>
> `integratie` là từ của người xây — chỉ doanh nghiệp mới "tích hợp" một cổng thanh toán.
> `koppelen` là từ của người dùng — ai cũng "nối" thẻ, tài khoản, ví của mình.
>
> Cùng nói về iDEAL và PayPal, nhưng một động từ mang khách và một động từ mang người tiêu dùng. Khi mở rộng bộ từ khoá thanh toán, hãy ưu tiên `integratie`, `api`, `checkout`, `webshop` — và cẩn thận với `koppelen`, `toevoegen`, `aanvragen`.

---

## 3. Mở rộng: pattern chỉ đúng với một số nhà cung cấp

Mình thử `<provider> integratie` và `<provider> koppelen` cho 13 nhà cung cấp Hà Lan/EU:

| Có người tìm ✅ | Không ai tìm ❌ |
|---|---|
| `mollie integratie` · `mollie koppelen` | `multisafepay integratie` · `multisafepay koppelen` |
| `stripe integratie` · `stripe koppelen` | `adyen integratie` · `adyen koppelen` |
| `wero integratie` · `wero koppelen` | `buckaroo` · `pay.nl` · `sisow` · `worldline` |
| `klarna koppelen` *(người tiêu dùng)* | `sepa` · `bancontact` · `rabo integratie` |

**Kết luận: không thể nhân bản pattern một cách máy móc.** MultiSafepay và Adyen là nhà cung cấp lớn ở Hà Lan nhưng không ai gõ `multisafepay integratie` — họ gõ `multisafepay api` và `multisafepay vs mollie`. Mỗi thương hiệu có cách người ta nói riêng, phải kiểm từng cái.

### ⭐ Phát hiện lớn nhất: Wero

`wero` · `wero ideal` · `wero webshop` · `wero webshops` · `wero zakelijk` · `wero integratie` · `wero koppelen` — **tất cả đều đã xác nhận có người tìm.**

Wero là ví thanh toán của European Payments Initiative, và nó **đang thay thế iDEAL ở Hà Lan**. Nghĩa là mọi webshop Hà Lan sẽ phải chuyển — một sự kiện bắt buộc, có thời hạn, ảnh hưởng toàn thị trường.

> 💡 **Đây là loại cơ hội hiếm trong Google Ads: một chuyển đổi hạ tầng bắt buộc mà gần như chưa ai bid.** Khác với `ideal integratie` (nhu cầu ổn định, ai cũng biết), `wero webshop` là nhu cầu **sẽ tăng mạnh** trong 12–24 tháng tới và hiện CPC còn ở mức sàn. Chi phí giữ chỗ bây giờ gần bằng không, còn giá trị thì nằm ở việc bạn đã có trang đích và lịch sử tài khoản khi nhu cầu bùng lên.
>
> Và nó bán được cho **mọi webshop Hà Lan**, không chỉ khách dùng AI builder — tức là thoát hẳn khỏi giới hạn volume của nhánh Lovable.

### PayPal: dạng có ý định doanh nghiệp

Vì `paypal koppelen` và `paypal integratie` không dùng được, mình đi tìm dạng PayPal thật sự thương mại:

```
✅ paypal webshop          ✅ paypal checkout              ✅ paypal api
✅ paypal webshop integration  ✅ paypal checkout integration  ✅ paypal api key
✅ paypal betalen webshop  ✅ paypal checkout button       ✅ paypal api credentials
✅ paypal pos webshop      ✅ paypal checkout websites     ✅ paypal api payment
✅ paypal button           ✅ paypal button for website    ✅ paypal button checkout
```

`webshop`, `checkout`, `api`, `button` — bốn từ này **không bao giờ xuất hiện trong ngữ cảnh người tiêu dùng**. Đó là cách giữ PayPal trong plan mà không mua người tiêu dùng.

---

## 4. Bộ từ khoá cuối: 58 keyword, 58/58 đã xác nhận

| Ad group | Keyword | P1 | Ghi chú |
|---|---:|---:|---|
| **AG-IDEAL** | 18 | 12 | Gồm `stripe ideal` — **260 lượt/tháng**, volume cao nhất bộ |
| **AG-PAYPAL** | 15 | 6 | Chỉ dạng `webshop`/`checkout`/`api`/`button` |
| **AG-MOLLIE** | 4 | 2 | Mollie là PSP Hà Lan |
| **AG-MULTISAFEPAY** | 6 | 2 | Theo gợi ý của bạn — nhưng là `api`/`ideal`, không phải `integratie` |
| **AG-WERO** | 6 | 4 | ⭐ Cửa sổ first-mover |
| **AG-KEUZE** | 9 | 8 | So sánh/chọn PSP — ý định tư vấn |
| **Tổng** | **58** | **33** | |

> 💡 **`stripe ideal` (260 lượt/tháng) một mình gấp 6,5 lần cả 4 keyword gốc cộng lại.** Nó không có trong file bạn gửi, nhưng cùng chủ đề và cùng ý định — người Hà Lan muốn nhận iDEAL thì phần lớn đi qua Stripe hoặc Mollie. Đây là lý do nên mở rộng bộ từ khoá thay vì chạy đúng 4 từ được cấp.

---
## 5. Ad Strength ≥ Good — thiết kế theo đúng tiêu chí nào

Ad Strength chấm **chất lượng và đa dạng của asset**, không chấm nội dung hay dở. 4 trục: số lượng headline, độ độc nhất, có keyword trong headline, chất lượng description. Google công bố cải thiện Poor → Excellent cho trung bình **+12% conversion**.

**7 quy tắc đã áp dụng cho cả 6 ad group, verify bằng script:**

| # | Quy tắc | Kết quả |
|---|---|---|
| 1 | Đủ **15 headline** (mức tối đa Google cho) | ✅ 6/6 |
| 2 | Đủ **4 description** | ✅ 6/6 |
| 3 | **≥3 headline chứa nguyên keyword** (🔑) | ✅ 4–5 mỗi nhóm |
| 4 | **Không headline trùng/gần trùng** — đo độ chồng từ sau khi loại chính keyword | ✅ 0 cặp |
| 5 | **Độ dài đa dạng ≥8 giá trị** → Google có nhiều tổ hợp hợp lệ | ✅ 8–9 giá trị |
| 6 | Trong giới hạn ký tự (H ≤30, D ≤90) | ✅ 0 vi phạm |
| 7 | 🔴 **Không pin headline nào** | ✅ 0 pin |

### 🔴 Quy tắc 7 là quy tắc dễ phá nhất

**Pinning giết Ad Strength nhanh hơn mọi thứ khác.** Ghim một headline vào vị trí 1 làm Google mất phần lớn tổ hợp, và Ad Strength thường tụt về *Average* hoặc *Poor* bất kể copy tốt đến đâu. Nếu bạn muốn ≥ Good thì phải chọn: pin hoặc Ad Strength, không thể cả hai.

> 💡 **Và đây là chỗ bộ từ khoá này dễ hơn nhánh Lovable rất nhiều.** Ở các plan trước, mình phải ghim `Not Affiliated With Lovable` vì lý do nhãn hiệu — mà ghim thì tụt Ad Strength. Bộ keyword thanh toán này **không có xung đột đó**: iDEAL, PayPal, Mollie, MultiSafepay, Wero đều là **nhà cung cấp bạn tích hợp**, không phải đối thủ bạn đang chen vào. Nói "PayPal Checkout Instellen" là mô tả dịch vụ thật, không gợi ý quan hệ đối tác giả.
>
> Không cần tuyên bố độc lập → không cần pin → Ad Strength đạt tự nhiên. **Yêu cầu Ad Strength ≥ Good của bạn thực ra dễ thoả mãn hơn ở bộ từ khoá này so với bộ Lovable** — đó là một lý do nữa để ưu tiên nó.

### Hai thứ chỉ đo được sau khi chạy

- **Asset ratings** (*Low / Good / Best*) chỉ xuất hiện khi đã có dữ liệu hiển thị. Sau 2–4 tuần vào **Asset details → ratings** và thay mọi headline bị gắn *Low*.
- **Ad Strength thật trong giao diện** có thể khác dự đoán cấu trúc. Nếu nhóm nào dưới Good, Google ghi rõ thiếu gì — thường là "add more unique headlines".

---

## 6. Cấu trúc: 1 campaign, 6 ad group

```
CAMPAIGN · LS-NL-Payments     [geo Netherlands · language DUTCH · Search only · €220/thang]
│
├── AG-IDEAL         (18 kw)  → /nl/ideal-integratie        ⭐ volume cao nhat
├── AG-PAYPAL        (15 kw)  → /nl/paypal-webshop
├── AG-MOLLIE         (4 kw)  → /nl/mollie-integratie
├── AG-MULTISAFEPAY   (6 kw)  → /nl/multisafepay-koppelen
├── AG-WERO           (6 kw)  → /nl/wero-webshop            ⭐ first-mover
└── AG-KEUZE          (9 kw)  → /nl/betaalprovider-kiezen   ⭐ y dinh tu van
```

**Bắt buộc:** `language = Dutch` (không chỉ geo = Netherlands — hai thiết lập độc lập) · Phrase match toàn bộ, trừ `[ideal koppelen]` để **Exact** · tắt Display Network · tắt Search partners.

> 💡 **Tách 6 ad group theo thương hiệu, không theo ý định** — ngược với cách mình làm ở các plan khác. Lý do: tiêu chí Ad Strength #3 đòi headline chứa nguyên keyword. Nếu gộp Mollie và MultiSafepay vào một nhóm "PSP", headline không thể chứa cả hai tên, và Google sẽ báo "headline không liên quan keyword". Một thương hiệu một nhóm là cách duy nhất vừa đạt Ad Strength vừa giữ liên quan.

---

## 7. RSA — 6 ad group, 90 headline, đã verify đạt Good+

🔑 = chứa nguyên keyword của ad group (tiêu chí #3)

### AG-IDEAL — 18 kw · `ideal integratie` `ideal koppelen aan webshop` `stripe ideal` (260) `ideal api`

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `iDEAL Integratie Vanaf €800` 🔑 | 27 | | D1 | `iDEAL integratie met een vaste prijs. Geen uurtarief en geen open einde.` | 72 |
| H2 | `iDEAL Koppelen Aan Je Webshop` 🔑 | 29 | | D2 | `Wij koppelen iDEAL aan je webshop of website en testen elke betaling echt.` | 74 |
| H3 | `iDEAL Integratie Door Experts` 🔑 | 29 | | D3 | `Webhooks, testmodus en live keys correct ingesteld. Binnen dagen live.` | 70 |
| H4 | `iDEAL Integratie Voor Webshops` 🔑 | 30 | | D4 | `Nederlands team met 11+ jaar ervaring en 160+ opgeleverde projecten.` | 68 |
| H5 | `iDEAL API Netjes Ingericht` 🔑 | 26 | | | | |
| H6 | `Vaste Prijs, Binnen Dagen Live` | 30 | | | | |
| H7 | `Ook SEPA En Bancontact` | 22 | | | | |
| H8 | `Abonnementen Of Eenmalig` | 24 | | | | |
| H9 | `Webhooks Correct Ingericht` | 26 | | | | |
| H10 | `Nederlandse Developers` | 22 | | | | |
| H11 | `11+ Jaar Ervaring` | 17 | | | | |
| H12 | `Gratis Check Van Je Setup` | 25 | | | | |
| H13 | `Van Testmodus Naar Live` | 23 | | | | |
| H14 | `Werkt Je Betaling Nog Niet?` | 27 | | | | |
| H15 | `Vraag Een Vaste Prijs Aan` | 25 | | | | |

### AG-PAYPAL — 15 kw · `paypal webshop` `paypal checkout` `paypal api` `paypal button`

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `PayPal Webshop Integratie` 🔑 | 25 | | D1 | `PayPal in je webshop, correct ingericht. Vaste prijs vanaf €800, binnen dagen live.` | 83 |
| H2 | `PayPal Checkout Instellen` 🔑 | 25 | | D2 | `Checkout, button of volledige API-koppeling. Wij bouwen wat bij je shop past.` | 77 |
| H3 | `PayPal Button Op Je Site` 🔑 | 24 | | D3 | `Van sandbox naar live zonder verrassingen. Elke betaling wordt echt getest.` | 75 |
| H4 | `PayPal API Koppeling` 🔑 | 20 | | D4 | `Nederlands ontwikkelteam, 11+ jaar ervaring, 160+ projecten opgeleverd.` | 71 |
| H5 | `Vaste Prijs Vanaf €800` | 22 | | | | |
| H6 | `Binnen Dagen Live` | 17 | | | | |
| H7 | `Ook iDEAL En Creditcard` | 23 | | | | |
| H8 | `Abonnementen Of Eenmalig` | 24 | | | | |
| H9 | `Webhooks Die Echt Werken` | 24 | | | | |
| H10 | `Wij Testen Elke Betaling` | 24 | | | | |
| H11 | `Nederlands Ontwikkelteam` | 24 | | | | |
| H12 | `11+ Jaar Ervaring` | 17 | | | | |
| H13 | `Gratis Check Van Je Checkout` | 28 | | | | |
| H14 | `Van Sandbox Naar Live` | 21 | | | | |
| H15 | `Vraag Een Vaste Prijs Aan` | 25 | | | | |

### AG-MOLLIE — 4 kw · `mollie integratie` `mollie integratie website`

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `Mollie Integratie Vanaf €800` 🔑 | 28 | | D1 | `Mollie integratie uitbesteden tegen een vaste prijs. Binnen dagen live.` | 71 |
| H2 | `Mollie Integratie Voor Shops` 🔑 | 28 | | D2 | `iDEAL, creditcard en Bancontact via Mollie. Wij richten de webhooks correct in.` | 79 |
| H3 | `Mollie Integratie Uitbesteden` 🔑 | 29 | | D3 | `Je weet de prijs voordat we beginnen. Geen uurtarief en geen nacalculatie.` | 74 |
| H4 | `Mollie Koppelen Aan Je Site` 🔑 | 27 | | D4 | `Nederlands team met 11+ jaar ervaring en 160+ opgeleverde projecten.` | 68 |
| H5 | `iDEAL Via Mollie Regelen` | 24 | | | | |
| H6 | `Vaste Prijs, Geen Uurtarief` | 27 | | | | |
| H7 | `Binnen Dagen Live` | 17 | | | | |
| H8 | `Abonnementen Of Eenmalig` | 24 | | | | |
| H9 | `Webhooks Correct Ingericht` | 26 | | | | |
| H10 | `Wij Testen Elke Betaling` | 24 | | | | |
| H11 | `Nederlandse Developers` | 22 | | | | |
| H12 | `11+ Jaar Ervaring` | 17 | | | | |
| H13 | `Gratis Setup Check` | 18 | | | | |
| H14 | `Van Test Naar Live Modus` | 24 | | | | |
| H15 | `Vraag Advies En Prijs Aan` | 25 | | | | |

### AG-MULTISAFEPAY — 6 kw · `multisafepay ideal` `multisafepay api`

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `MultiSafepay iDEAL Opzetten` 🔑 | 27 | | D1 | `MultiSafepay koppelen aan je webshop, inclusief iDEAL en API-sleutels.` | 70 |
| H2 | `MultiSafepay API Koppelen` 🔑 | 25 | | D2 | `Vaste prijs vanaf €800. Webhooks en testmodus correct ingesteld, binnen dagen live.` | 83 |
| H3 | `MultiSafepay iDEAL Werkend` 🔑 | 26 | | D3 | `Wij testen elke betaling voordat je live gaat. Geen verrassingen achteraf.` | 74 |
| H4 | `MultiSafepay API Sleutels` 🔑 | 25 | | D4 | `Nederlands ontwikkelteam, 11+ jaar ervaring, 160+ projecten opgeleverd.` | 71 |
| H5 | `Vaste Prijs Vanaf €800` | 22 | | | | |
| H6 | `Binnen Dagen Live` | 17 | | | | |
| H7 | `Ook SEPA En Bancontact` | 22 | | | | |
| H8 | `Abonnementen Of Eenmalig` | 24 | | | | |
| H9 | `Webhooks Correct Ingericht` | 26 | | | | |
| H10 | `Wij Testen Elke Betaling` | 24 | | | | |
| H11 | `Nederlands Ontwikkelteam` | 24 | | | | |
| H12 | `11+ Jaar Ervaring` | 17 | | | | |
| H13 | `Gratis Check Van Je Betalingen` | 30 | | | | |
| H14 | `Van Testmodus Naar Live` | 23 | | | | |
| H15 | `Vraag Een Vaste Prijs Aan` | 25 | | | | |

### AG-WERO — 6 kw · `wero integratie` `wero webshop` `wero zakelijk` ⭐ first-mover

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `Wero Integratie Voor Je Shop` 🔑 | 28 | | D1 | `Wero komt naast en straks in plaats van iDEAL. Wij maken je webshop er klaar voor.` | 82 |
| H2 | `Wero Koppelen Aan Je Site` 🔑 | 25 | | D2 | `Wero koppelen aan je site of webshop, met vaste prijs en binnen dagen live.` | 75 |
| H3 | `Wero Webshop Klaarmaken` 🔑 | 23 | | D3 | `Je houdt iDEAL werkend terwijl Wero erbij komt. Geen downtime in je checkout.` | 77 |
| H4 | `Wero Zakelijk Instellen` 🔑 | 23 | | D4 | `Nederlands team, 11+ jaar ervaring, 160+ projecten opgeleverd sinds 2015.` | 73 |
| H5 | `iDEAL Wordt Wero: Klaar?` | 24 | | | | |
| H6 | `Nu Al Wero Accepteren` | 21 | | | | |
| H7 | `Vaste Prijs Vanaf €800` | 22 | | | | |
| H8 | `Binnen Dagen Live` | 17 | | | | |
| H9 | `Naast iDEAL En Creditcard` | 25 | | | | |
| H10 | `Webhooks Correct Ingericht` | 26 | | | | |
| H11 | `Nederlandse Developers` | 22 | | | | |
| H12 | `11+ Jaar Ervaring` | 17 | | | | |
| H13 | `Gratis Migratie-advies` | 22 | | | | |
| H14 | `Wij Testen Elke Betaling` | 24 | | | | |
| H15 | `Vraag Een Vaste Prijs Aan` | 25 | | | | |

### AG-KEUZE — 9 kw · `betaalprovider vergelijken` `multisafepay vs mollie` `mollie of stripe`

| # | Headline (≤30) | Ch | | # | Description (≤90) | Ch |
|---|---|---:|---|---|---|---:|
| H1 | `Betaalprovider Vergelijken` 🔑 | 26 | | D1 | `Welke betaalprovider past bij jouw shop? Wij rekenen de tarieven voor je door.` | 78 |
| H2 | `Betaalmethoden Webshop Kiezen` 🔑 | 29 | | D2 | `Mollie, Stripe of MultiSafepay. We adviseren eerst en koppelen daarna de juiste.` | 80 |
| H3 | `MultiSafepay Vs Mollie` 🔑 | 22 | | D3 | `Overstappen zonder downtime. Abonnementen en klantgegevens verhuizen netjes mee.` | 80 |
| H4 | `Mollie Of Stripe Gebruiken?` 🔑 | 27 | | D4 | `Nederlands ontwikkelteam, 11+ jaar ervaring. Vaste prijs vanaf €800.` | 68 |
| H5 | `Wij Rekenen Tarieven Door` | 25 | | | | |
| H6 | `Welke Past Bij Jouw Shop?` | 25 | | | | |
| H7 | `Advies En Daarna Koppelen` | 25 | | | | |
| H8 | `Vaste Prijs Vanaf €800` | 22 | | | | |
| H9 | `Payouts En Fees Vergeleken` | 26 | | | | |
| H10 | `Overstap Zonder Downtime` | 24 | | | | |
| H11 | `Nederlands Ontwikkelteam` | 24 | | | | |
| H12 | `11+ Jaar Ervaring` | 17 | | | | |
| H13 | `Gratis Adviesgesprek` | 20 | | | | |
| H14 | `Abonnementen Meeverhuizen` | 25 | | | | |
| H15 | `Vraag Advies Aan` | 16 | | | | |
---

## 8. Extensions

| Link text | Ch | Dòng 1 | Ch | Dòng 2 | Ch |
|---|---:|---|---:|---|---:|
| `Vaste Prijs Vanaf €800` | 22 | `Tarieven` | 8 | `Geen uurtarief, geen nacalculatie` | 33 |
| `Gratis Setup Check` | 18 | `Stuur je shop-url` | 17 | `Reactie binnen 1 werkdag` | 24 |
| `Betaalmethoden` | 14 | `iDEAL, PayPal, SEPA` | 19 | `Creditcard en Bancontact` | 24 |
| `Werkwijze` | 9 | `Koppelen en testen` | 18 | `Elke betaling echt getest` | 25 |

**Callouts:** `Vaste prijs vanaf €800` · `Binnen dagen live` · `Geen uurtarief` · `Elke betaling getest` · `11+ jaar ervaring` · `160+ projecten` · `Nederlands team` · `Gratis intakegesprek`
**Display path** (2 × 15 ký tự):

| Ad group | Display path |
|---|---|
| AG-IDEAL | `launchstudio.eu/ideal/integratie` |
| AG-PAYPAL | `launchstudio.eu/paypal/webshop` |
| AG-MOLLIE | `launchstudio.eu/mollie/koppelen` |
| AG-MULTISAFEPAY | `launchstudio.eu/multisafepay/setup` |
| AG-WERO | `launchstudio.eu/wero/webshop` |
| AG-KEUZE | `launchstudio.eu/betaalprovider/advies` |

---

## 9. 🔴 Negative keywords — phần quyết định sống còn của plan này

Vì 2/4 keyword gốc là ý định người tiêu dùng, negative list ở đây **quan trọng hơn keyword list**.

### Khối ví điện tử & ngân hàng cá nhân — broad (bắt buộc)

```
-bankrekening  -"prive rekening"  -prive  -creditcard  -"apple id"  -"apple pay"
-"google pay"  -googlepay  -revolut  -bunq  -tikkie  -wise  -n26
-abn  -"abn amro"  -ing  -rabobank  -rabo  -sns  -asn  -knab  -regiobank
-tiktok  -instagram  -marktplaats  -vinted  -steam  -spotify  -netflix
```

> ⚠️ **Đây là khối tiết kiệm tiền nhiều nhất.** Mọi gợi ý của `paypal koppelen` và 7/10 gợi ý của `ideal koppelen` rơi vào khối này. Không chặn thì bạn trả tiền cho người đang cố nối PayPal với tài khoản Rabobank của họ.

### Khối hỗ trợ / sự cố — phrase

```
-storing  -"werkt niet vandaag"  -"lukt niet"  -inloggen  -login  -wachtwoord
-contact  -bellen  -klantenservice  -telefoonnummer  -"mijn account"
-terugboeken  -chargeback  -refund  -terugbetaling  -geweigerd  -geblokkeerd
-verwijderen  -opzeggen  -sluiten  -wijzigen  -ontbreekt
```
> ⚠️ Từ dữ liệu thật: `multisafepay storing`, `multisafepay inloggen`, `multisafepay bellen`, `paypal betaalmethode geweigerd`, `paypal betaalmethode verwijderen`, `paypal zakelijke rekening sluiten`, `wero storing`, `wero ideal storing vandaag`. Người này đang gặp sự cố **với nhà cung cấp**, không cần developer.

### Khối du lịch & BNPL — broad (ít ai nghĩ tới)

```
-esta  -eta  -visa  -visum  -vliegticket  -reis
-in3  -"in 3"  -klarna  -afterpay  -billink  -spraypay  -achteraf
```
> ⚠️ **`-esta -eta -visa` là negative bất ngờ nhưng bắt buộc.** Autocomplete cho `ideal aanvragen` trả về `esta aanvragen ideal` và `eta aanvragen ideal betalen` — người xin giấy phép du lịch Mỹ/Anh và trả bằng iDEAL. Họ không liên quan gì đến webshop.
>
> Và `in3`/`klarna`/`afterpay` là BNPL (mua trước trả sau) — `ideal in 3 webshops`, `ideal in3 zakelijk`. Khác hẳn tích hợp iDEAL.

### Khối tự làm / plugin có sẵn — phrase + broad

```
-gratis  -zelf  -goedkoop  -plugin  -module  -extensie  -app  -addon
-shopify  -woocommerce  -wordpress  -magento  -lightspeed  -prestashop  -ccvshop
-wix  -squarespace  -shopware  -opencart
-handleiding  -tutorial  -uitleg  -documentatie  -voorbeeld  -"hoe werkt"
```
> 💡 **Khối platform là lựa chọn khó và mình vẫn khuyên chặn.** `mollie integratie shopify`, `paypal checkout shopify`, `mollie koppelen aan shopify` đều là truy vấn thật. Nhưng với Shopify/WooCommerce thì **đã có plugin chính thức miễn phí** — bạn cạnh tranh với "cài app, xong". Khách thật của bạn là người có **website hoặc app tự xây** mà plugin không giải quyết được.
>
> Nếu sau này muốn vào thị trường Shopify thì làm ad group riêng với thông điệp khác hẳn (ví dụ "plugin cài rồi nhưng webhook vẫn fail"), đừng để nó lẫn vào đây.

### Khối kế toán — broad

```
-snelstart  -"exact online"  -moneybird  -twinfield  -afas  -boekhouding
-boekhoudprogramma  -factuur  -facturen  -btw  -administratie
```
> ⚠️ Gợi ý của `mollie koppelen` và `stripe koppelen` gần như toàn bộ là `aan snelstart`, `aan exact online`, `met moneybird` — người muốn nối cổng thanh toán với **phần mềm kế toán**. Đó là dịch vụ khác (và thường đã có connector sẵn).

### Khối tuyển dụng & học — broad

```
-vacature  -vacatures  -baan  -salaris  -stage  -zzp  -freelancer  -uurtarief
-cursus  -opleiding  -leren  -betekenis  -"wat is"
```

**Dựng 5 Shared Negative List:** `NEG-CONSUMER-WALLET` · `NEG-SUPPORT-STORING` · `NEG-TRAVEL-BNPL` · `NEG-PLATFORM-PLUGIN` · `NEG-BOEKHOUDING`

---

## 10. Trang đích

**Thứ tự nếu không làm hết 6 trang:**

| Ưu tiên | Trang | Lý do |
|---|---|---|
| **1** | `/nl/ideal-integratie` | 18 kw, chứa `stripe ideal` 260 lượt |
| **2** | `/nl/betaalprovider-kiezen` | 8/9 kw là P1, ý định tư vấn cao nhất |
| **3** | `/nl/wero-webshop` | Cửa sổ first-mover, CPC còn ở sàn |
| 4–6 | `/nl/paypal-webshop` · `/nl/mollie-integratie` · `/nl/multisafepay-koppelen` | |

**Mỗi trang cần:**
- H1 chứa nguyên keyword (`iDEAL integratie`) — khớp headline, nâng Landing page experience
- **Giá từ €800 ở màn hình đầu** — bộ lọc, không phải nhược điểm
- Một dòng nói rõ bạn làm gì: *"Wij koppelen de betaalprovider aan jouw website of app"*
- 🔴 **Một dòng nói rõ bạn KHÔNG làm gì:** *"Wij zijn geen betaalprovider en openen geen rekening voor je."*
- Form ngắn: URL shop, email, nhà cung cấp hiện tại, 1 câu mô tả

> 🔴 **Dòng "chúng tôi không phải nhà cung cấp thanh toán" là thứ bảo vệ ngân sách của bạn.** Dù negative list có tốt đến đâu, vẫn sẽ có người tiêu dùng và người muốn mở tài khoản iDEAL lọt vào. Một dòng ở đầu trang khiến họ tự rời đi **trước khi** gửi form — tiết kiệm thời gian bạn gọi lại, và quan trọng hơn: tránh làm bẩn dữ liệu conversion. Nếu Google học rằng những người đó là "conversion", nó sẽ tìm thêm người giống họ.

**Trang `/nl/betaalprovider-kiezen` nên có một bảng so sánh thật** (Mollie vs Stripe vs MultiSafepay: phí giao dịch, payout, iDEAL, abonnementen). Đây là nội dung phục vụ 9 keyword so sánh và là lý do hợp lý để người ta để lại email.

---

## 11. Ngân sách

Keyword Planner không trả CPC cho 4 từ gốc (Low competition, dưới ngưỡng dữ liệu). Mình dùng €6,88 — mức giữa đo được của `stripe ideal` (€1,85–11,92), là từ cùng chủ đề duy nhất có số thật.

| Ad group | Volume ước tính | Trần/tháng | Đề xuất |
|---|---:|---:|---:|
| AG-IDEAL | ~340 | €70 | **€80** |
| AG-PAYPAL | ~120 | €25 | **€40** |
| AG-KEUZE | ~90 | €19 | **€40** |
| AG-WERO | ~70 | €14 | **€35** |
| AG-MOLLIE | ~40 | €8 | **€15** |
| AG-MULTISAFEPAY | ~40 | €8 | **€10** |
| **Tổng** | **~700** | **€144** | **€220** |

**Đề xuất €220/tháng** (≈ €7,30/ngày) — **cao hơn trần €144 có chủ ý**.

> 💡 **Vì sao cấp trên trần, ngược với plan NL Service?** Ở đó CPC là €12–25 và trần đã tính từ volume lớn — cấp thêm là đốt tiền. Ở đây CPC khoảng €7 và toàn bộ là Low competition, nên rủi ro mỗi click thấp. Thừa ngân sách trong trường hợp này không gây hại: Google sẽ đơn giản không tiêu hết.
>
> Quan trọng hơn, mình cố ý cấp **AG-WERO €35 trong khi trần chỉ €14** và **AG-KEUZE €40 trong khi trần €19**. Đó không phải tính sai — đó là đặt cược: Wero vì nhu cầu sẽ tăng và bạn muốn có lịch sử tài khoản trước lúc đó; AG-KEUZE vì ý định tư vấn cho ra khách chịu nghe báo giá, không chỉ hỏi giá.

### Kinh tế

| | |
|---|---|
| Click/tháng ở €220 và CPC €6,88 | **~32** |
| Lead (5% chuyển đổi trang) | **1,6** |
| €/lead | **€138** |
| CAC ở tỷ lệ chốt 25% | **€551** |
| Giá trị dự án tích hợp thanh toán | **€800–1.500** |
| Tỷ lệ doanh thu/chi phí ở dự án €1.000 | **~1,8×** |

> 🔴 **1,8× là mỏng, và đây là rủi ro thật của plan này.** CAC €551 trên một dự án €800 chỉ còn €249 biên — chưa trừ thời gian làm việc. Plan này chỉ có lãi rõ ràng nếu đạt được **một trong hai** điều:
>
> **① Nâng giá trị đơn hàng.** Đừng bán "tích hợp iDEAL €800". Bán "thiết lập thanh toán hoàn chỉnh": iDEAL + PayPal + SEPA + Bancontact + webhook + abonnementen + kiểm thử, €1.500–2.500. Cùng một lead, cùng CAC, biên lợi nhuận gấp đôi. Và khách muốn iDEAL gần như luôn cũng muốn các phương thức khác — bán lẻ từng cái là tự hạ giá mình.
>
> **② Dùng nó làm cửa vào.** Một khách đã tin bạn với checkout của họ là khách dễ bán tiếp MVP hoặc app. CAC €551 cho một dự án €800 là lỗ; cho một quan hệ dẫn tới dự án €3.500 thì rất rẻ. Nếu chọn hướng này, hãy đo **giá trị khách hàng trọn đời**, đừng đo lợi nhuận đơn hàng đầu.
>
> Nếu không làm được cả hai thì nói thẳng: bộ từ khoá này không nên là kênh chính.

---

## 12. Checklist

**Trước khi bật**
- [ ] 🔴 Tạo 5 Shared Negative List ở §9. **Khối ví điện tử/ngân hàng là bắt buộc** — không có nó plan này lỗ ngay tuần đầu
- [ ] Đặt `language = Dutch`, không chỉ geo = Netherlands
- [ ] Tắt Display Network và Search partners
- [ ] `[ideal koppelen]` để **Exact match**; cân nhắc tạm dừng hẳn và chỉ chạy hai biến thể dài
- [ ] **Loại `paypal koppelen` và `paypal integratie`** khỏi bộ keyword — thay bằng 15 từ ở AG-PAYPAL
- [ ] **Không pin headline nào** (§5)
- [ ] Dựng 3 trang đích đầu theo §10, mỗi trang có dòng *"Wij zijn geen betaalprovider"*
- [ ] Bật Conversion tracking **trước** khi bật ads
- [ ] Chốt gói bán: giá trị đơn hàng €1.500–2.500 thay vì €800 (§11)

**Tuần 1–3**
- [ ] Search Terms Report **2 ngày/lần** — mục tiêu duy nhất là bắt truy vấn người tiêu dùng lọt qua
- [ ] Kiểm **Ad Strength thật** trong giao diện sau khi ad được duyệt; nếu nhóm nào dưới Good, Google ghi rõ thiếu gì
- [ ] Chạy `kp_upload_payments_nl.txt` (58 kw) trong Keyword Planner, Language = **Dutch** → có volume thật thì tính lại §11

**Tuần 4**
- [ ] **Asset details → ratings**, thay headline bị gắn *Low*
- [ ] Nếu >30% truy vấn là ý định người tiêu dùng → thắt toàn bộ về Exact match
- [ ] Nếu AG-MULTISAFEPAY và AG-MOLLIE chưa có click → dồn ngân sách sang AG-IDEAL và AG-WERO

**Tuần 8**
- [ ] Tính lại CAC bằng số thật
- [ ] Quyết định về Wero: nếu đã thấy click thì tăng ngân sách trước khi thị trường nóng lên
- [ ] Viết bảng so sánh PSP trên `/nl/betaalprovider-kiezen` nếu chưa làm

---

## 13. Tóm tắt

> **4 keyword trong file = 40 lượt/tháng, tức khoảng 1,2 click.** Không chạy được. Mình mở rộng lên **58 keyword, 58/58 xác nhận có người tìm** bằng Google Autocomplete.
>
> **2 trong 4 keyword gốc phải bỏ.** `paypal koppelen` có **10/10 gợi ý là người tiêu dùng** nối PayPal với ngân hàng/ví của họ. `paypal integratie` không có gợi ý nào, kể cả chính nó. `ideal koppelen` lẫn 7/10 → Exact match + chặn nặng. Chỉ `ideal integratie` là sạch.
>
> **Quy tắc rút ra: động từ quyết định ý định, không phải danh từ.** `integratie` là từ của người xây; `koppelen` là từ của người dùng. Cùng nói về iDEAL nhưng một từ mang khách, một từ mang người tiêu dùng.
>
> **PayPal vẫn giữ được** — qua `paypal webshop`, `paypal checkout`, `paypal api`, `paypal button`. Bốn từ này không bao giờ xuất hiện trong ngữ cảnh người tiêu dùng.
>
> **MultiSafepay như bạn gợi ý: có, nhưng không phải dạng bạn nghĩ.** `multisafepay integratie` và `multisafepay koppelen` đều **không ai gõ**. Dạng thật là `multisafepay api` và `multisafepay vs mollie`.
>
> **⭐ Phát hiện lớn nhất là Wero** — ví của European Payments Initiative đang **thay thế iDEAL ở Hà Lan**. `wero webshop`, `wero zakelijk`, `wero integratie` đều đã xác nhận. Đây là chuyển đổi hạ tầng **bắt buộc, có thời hạn, toàn thị trường** mà gần như chưa ai bid — và nó bán được cho mọi webshop Hà Lan, không chỉ khách dùng AI builder.
>
> **`stripe ideal` một mình 260 lượt/tháng** — gấp 6,5 lần cả 4 keyword gốc cộng lại.
>
> **Về Ad Strength ≥ Good: 6/6 ad group đạt**, verify bằng script — 90 headline + 24 description, 0 vi phạm, theo 7 tiêu chí gồm **không pin headline nào**. Bộ từ khoá này dễ đạt hơn bộ Lovable, vì iDEAL/PayPal/Mollie là **nhà cung cấp bạn tích hợp**, không phải đối thủ — nên không cần tuyên bố độc lập, không cần pin.
>
> **Ngân sách €220/tháng**, ~32 click, ~1,6 lead, CAC €551.
>
> 🔴 **Rủi ro phải nhìn thẳng: ở dự án €800 thì tỷ lệ doanh thu/chi phí chỉ 1,8× — quá mỏng.** Plan chỉ lãi rõ nếu bạn **bán gói hoàn chỉnh €1.500–2.500** (iDEAL + PayPal + SEPA + webhook + abonnementen + kiểm thử) thay vì bán lẻ từng tích hợp, **hoặc** dùng nó làm cửa vào rồi đo giá trị khách trọn đời. Nếu không làm được cả hai thì đây không nên là kênh chính.

---

*4 keyword gốc → 58 keyword đã xác nhận · 2/4 keyword gốc bị loại vì ý định người tiêu dùng · 6 ad group · 90 headline + 24 description · 6/6 đạt Ad Strength Good+, verify bằng script · 0 pinning · 5 Shared Negative List*
