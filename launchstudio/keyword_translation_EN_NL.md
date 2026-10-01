# 🇳🇱 Dịch 166 từ khoá sang tiếng Hà Lan — kèm kiểm chứng

> **Nguồn:** `kp_upload_lovable_EN.txt` (166 keyword) · **Ngày:** 01/10/2026
> **Quy tắc giữ nguyên:** `lovable`, `stripe`, `database`, `supabase` — cộng các tên riêng/token kỹ thuật không có bản dịch (`vercel`, `netlify`, `github`, `aws`, `cloudflare`, `paddle`, `mollie`, `ideal`, `tanstack`, `dns`, `ssl`, `cors`, `oauth`, `api key`, `rls`, `cve`, `webhook`, `checkout`, `anon key`, `service role key`, `edge functions`, `secrets manager`, `upwork`, `reddit`, `vite`, `404`, `not_found`)

## File giao

| File | Nội dung |
|---|---|
| **`kp_upload_lovable_NL_translated.txt`** | 166 từ khoá đã dịch, mỗi dòng một từ, dán thẳng vào Keyword Planner |
| **`keyword_translation_EN_NL.csv`** | Bảng đối chiếu EN → NL + trạng thái kiểm chứng + dạng Hà Lan thật |
| **`kp_upload_NL_real.txt`** | ⭐ 69 từ khoá tiếng Hà Lan **đã xác nhận có người tìm** — xem §3 |

---

## 1. 🔴 Kết quả kiểm chứng: chỉ 35/166 bản dịch là truy vấn thật

Mình dịch xong rồi chạy từng bản dịch qua Google Autocomplete (`hl=nl`, `gl=nl`):

| | Số | |
|---|---:|---|
| ✅ Người Hà Lan thật sự gõ | **35** | 21% |
| ❌ Không ai gõ | **131** | 79% |

**Và đây là phần quan trọng: trong 35 cụm đạt, 31 cụm là những cụm mà thực chất không có gì được dịch.**

`lovable stripe`, `lovable supabase`, `lovable paddle`, `lovable mollie`, `lovable 404`, `lovable cve`, `lovable anon key`, `lovable service role key`, `lovable code review`, `lovable secrets manager`, `lovable stripe webhook secret`, `lovable cloud vs supabase`, `supabase rls checker`, `vercel 404 not_found vite`… — toàn bộ đều giữ nguyên tiếng Anh, nên chúng "đạt" chỉ vì chúng chưa bao giờ là tiếng Hà Lan.

**Chỉ có 4 bản dịch thật sự hoạt động:**

| EN | NL | Vì sao sống sót |
|---|---|---|
| `host lovable website` | **`lovable website hosten`** | `hosten` là động từ Hà Lan thông dụng |
| `lovable hosting cost` | **`lovable hosting kosten`** | `kosten` là từ tiền bạc, người Hà Lan luôn dùng tiếng mẹ đẻ |
| `ideal payment gateway` | **`ideal betaalprovider`** | iDEAL là hệ thống Hà Lan, bối cảnh toàn Hà Lan |
| `lovable data exposure` | **`lovable datalek`** | `datalek` là thuật ngữ **pháp lý** trong AVG/GDPR |

> 💡 **Bốn cụm sống sót có cùng một đặc điểm: chúng không phải thuật ngữ kỹ thuật.** Tiền (`kosten`), nghĩa vụ pháp lý (`datalek`), hạ tầng thanh toán nội địa (`betaalprovider`), và một động từ thường (`hosten`). Người Hà Lan chuyển sang tiếng mẹ đẻ khi nói về **tiền, luật, và hành động** — và giữ tiếng Anh khi nói về **lỗi và công cụ**.
>
> Đó là lý do `lovable supabase verbinding mislukt` = 0 nhưng `lovable supabase connection failed` có người gõ: thông báo lỗi hiện ra bằng tiếng Anh, và dev dán nguyên văn vào Google.

### Một số ví dụ dịch đúng ngữ pháp nhưng 0 lượt tìm

```
lovable publiceren mislukt              ← lovable publishing failed
lovable supabase verbinding mislukt     ← lovable supabase connection failed
lovable beveiliging op rijniveau        ← lovable row level security
lovable betaalverwerker                 ← lovable payment processor
gevibecode app beveiligingsscanner      ← vibe coded app security scanner
hoe beveilig je gevibecode apps         ← how to secure vibe coded apps
lovable database fout bij opslaan nieuwe gebruiker
```

Tất cả đều là tiếng Hà Lan chuẩn. Không ai gõ.

---

## 2. 4 trường hợp dịch sai thứ tự từ — đã tìm ra dạng thật

Autocomplete chỉ ra dạng người Hà Lan dùng khác thứ tự với bản dịch của mình:

| Bản dịch của mình | ❌ | Dạng thật | ✅ |
|---|---|---|---|
| `lovable naar vercel 404` | 0 | `lovable to vercel 404` | có |
| `lovable stripe connect` | 0 | **`stripe connect lovable`** | có |
| `database voor lovable` | 0 | **`database lovable`** | có |
| `lovable cloud of supabase` | 0 | `lovable cloud supabase` | có |
| `lovable supabase rls` | có | **`rls supabase`** | cũng có — hai thứ tự đều dùng được |

---

## 3. ⭐ 69 từ khoá tiếng Hà Lan **thật** mình tìm thêm được

Vì bản dịch trực tiếp hỏng 79%, mình đi tìm xem người Hà Lan **thật sự** gõ gì về các chủ đề này. Toàn bộ 69 cụm dưới đây **đã xác nhận khớp chính xác** (69/69) — file `kp_upload_NL_real.txt`.

### 3.1 🥇 Cụm `stripe ideal` — phát hiện tốt nhất

```
stripe ideal                stripe ideal kosten         stripe ideal betalingen
stripe ideal fees           stripe ideal pricing        stripe ideal recurring
stripe ideal shopify        stripe ideal wero
```

Đây là cụm thương mại tốt nhất trong cả tiếng Hà Lan: người đang tích hợp iDEAL qua Stripe và hỏi về **chi phí** (`kosten`, `fees`, `pricing`) và **thanh toán định kỳ** (`recurring`). Không gắn thương hiệu AI builder nào, nên bán được cho cả khách không dùng Lovable.

### 3.2 🥇 Cụm Mollie — quyết định nhà cung cấp

```
mollie of stripe            wat is beter mollie of stripe
mollie integratie           mollie integratie website
```

`wat is beter mollie of stripe` là truy vấn **Decision** hoàn hảo: họ chưa chọn, đang cần tư vấn. Mollie là nhà cung cấp Hà Lan và **không nằm trong Lovable Payments** — nên bất kỳ ai muốn dùng Mollie đều cần người tích hợp thủ công.

### 3.3 iDEAL — thêm vào website

```
ideal toevoegen aan website        ideal betaling toevoegen aan website
ideal integreren in website        ideal in webshop            ideal betaalprovider
```

### 3.4 🥇 `is lovable veilig` và `gevibecode`

| Keyword | Ghi chú |
|---|---|
| **`is lovable veilig`** | Câu hỏi bảo mật bằng tiếng Hà Lan — khớp đúng dịch vụ audit |
| **`gevibecode`** · **`gevibecoded`** | Từ Hà Lan cho "vibe coded" **tồn tại thật**. Đối thủ devneth.nl dùng đúng từ này |
| `lovable datalek` | Thuật ngữ AVG/GDPR |

### 3.5 ⭐ Thị trường Hà Lan thật — lớn hơn hẳn nhánh Lovable

```
mvp laten maken                      webapp laten maken
software laten maken                 software laten ontwikkelen
software laten ontwikkelen kosten    maatwerk software laten maken
ai software laten maken              prototype laten maken
prototype laten maken in nederland   prototype laten ontwikkelen
ai app laten maken                   ai een app laten maken
app bouwen met ai                    app bouwen met ai coding
kan ik een app bouwen met ai         app developer inhuren
```

> 💡 **Cụm `laten maken` / `laten ontwikkelen` là nơi nhu cầu thật của bạn nằm.** Cấu trúc `laten + động từ` trong tiếng Hà Lan nghĩa là *"nhờ người khác làm"* — tức bản thân cú pháp đã mang ý định thuê dịch vụ. Không có cấu trúc tương đương trong tiếng Anh, nên không đối thủ nước ngoài nào nhắm được.
>
> Và để ý `software laten ontwikkelen kosten` — ý định thuê **cộng** câu hỏi giá. Đó là truy vấn gần quyết định nhất trong toàn bộ tập tiếng Hà Lan.
>
> `ai app laten maken` và `app bouwen met ai` thì bắt đúng người đang cân nhắc dùng AI builder — **trước khi** họ tự làm rồi mắc kẹt. Rẻ hơn là chờ họ vỡ rồi mới bắt.

---

## 4. ⚠️ Negative bắt buộc cho nhánh tiếng Hà Lan

**`app beveiliging` trong tiếng Hà Lan bị Samsung chiếm hoàn toàn.** Autocomplete trả về: `app beveiliging samsung aan of uit`, `app beveiliging inschakelen samsung`, `app beveiliging samsung mcafee`, `app beveiliging android`. Đây là người tìm cách bật tính năng bảo mật trên điện thoại Samsung.

```
-samsung  -android  -iphone  -ios  -mcafee  -telefoon  -mobiel  -"aan of uit"  -inschakelen
```

Ngoài ra:
```
-gratis  -zelf  -handleiding  -tutorial  -cursus  -uitleg  -betekenis  -reddit
-vacature  -salaris  -stage  -baan  -opleiding
-hoover                    ← "hoover lovable app" la may hut bui!
-shopify  -uber  -paypal  -"google pay"  -"apple pay"  -factuur  -"apple id"
     ← tu `ideal toevoegen aan ...`: phan lon nguoi muon them iDEAL vao VI DIEN TU, khong vao website
```

> ⚠️ **Khối cuối quan trọng.** `ideal toevoegen aan website` là khách của bạn, nhưng `ideal toevoegen aan google pay` / `uber` / `apple id` / `paypal` / `factuur` thì không — họ là người tiêu dùng muốn thêm iDEAL vào ví điện tử của họ. Cùng một tiền tố, hai thế giới khác nhau. Không chặn thì ad group iDEAL sẽ tiêu hết ngân sách vào người tiêu dùng.

---

## 5. Nên dùng file nào

| Tình huống | File |
|---|---|
| Bạn muốn xem toàn bộ bản dịch như đã yêu cầu | `kp_upload_lovable_NL_translated.txt` (166) |
| Bạn muốn chạy Keyword Planner tiếng Hà Lan có ý nghĩa | ⭐ **`kp_upload_NL_real.txt` (69)** |
| Bạn muốn đối chiếu từng dòng EN↔NL + trạng thái | `keyword_translation_EN_NL.csv` |

**Thiết lập Keyword Planner cho file NL:** Location = **Netherlands** · Language = **Dutch** · chạy riêng, không gộp với English.

> 🔴 **Khuyến nghị thẳng: đừng dựng campaign trên 166 bản dịch.** Mình đã dịch đủ như bạn yêu cầu và file có đó, nhưng 131/166 không ai gõ — đưa vào Google Ads thì chúng không bao giờ được kích hoạt, và chúng làm loãng Search Terms Report khiến bạn khó đọc dữ liệu thật trong 3 tuần đầu.
>
> Cấu trúc nên dùng: **giữ các từ khoá kỹ thuật ở campaign tiếng Anh** (vì người Hà Lan gõ lỗi bằng tiếng Anh), và mở **một campaign tiếng Hà Lan riêng chỉ cho 69 cụm đã xác nhận** — trọng tâm là `stripe ideal`, Mollie, `is lovable veilig`, và họ `laten maken`.

---

*166 từ khoá đã dịch · 35 xác nhận có người tìm (chỉ 4 là bản dịch thật) · 131 không ai gõ · 69 từ khoá Hà Lan thật tìm thêm, 69/69 xác nhận · phương pháp: Google Autocomplete `hl=nl&gl=nl`*
