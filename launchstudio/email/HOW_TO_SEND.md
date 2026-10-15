# 📤 Cách nhúng và gửi email

> **Ngày:** 15/10/2026 · cập nhật sau khi thêm footer pháp lý vào bản NL
> **File:** `launchstudio_email_nl.html` (**21,5 KB · 4 link**) · `launchstudio_email.html` (24,1 KB · 13 link)

---

## Bước 0 — Hai việc bắt buộc trước mọi thứ

### ① Thay `CAMPAIGN`

| File | Số chỗ |
|---|---:|
| `launchstudio_email_nl.html` | **5** |
| `launchstudio_email.html` | **10** |

Mở file bằng editor, **Find & Replace All**: `CAMPAIGN` → tên campaign thật, ví dụ `okt26_launchready`.

Quy tắc đặt tên: chữ thường, không dấu, không khoảng trắng, gạch dưới. GA4 phân biệt chữ hoa/thường nên `Okt26` và `okt26` sẽ thành hai campaign khác nhau.

Nếu gửi cả hai ngôn ngữ, dùng hậu tố để tách báo cáo: `okt26_launchready_nl` và `okt26_launchready_en`.

### ② 🔴 Bản NL không còn link huỷ đăng ký — ESP phải tự chèn

| File | Footer | Merge tag |
|---|---|---|
| `launchstudio_email_nl.html` | Chỉ **`Launch Studio`** + địa chỉ | 🔴 **không có** |
| `launchstudio_email.html` | Đủ: afmelden, preferences, archive, privacy | `*\|UNSUB\|*` · `*\|UPDATE_PROFILE\|*` · `*\|ARCHIVE\|*` |

**Telecommunicatiewet 11.7** yêu cầu mọi email thương mại phải có link huỷ đăng ký. Bản NL hiện thiếu, nên nó **chỉ gửi được qua ESP tự chèn footer**:

| Cách gửi | Có đúng luật? |
|---|---|
| Mailchimp · Brevo · MailerLite · Klaviyo | ✅ Tự chèn footer huỷ đăng ký của nền tảng |
| API / SMTP (Resend, Postmark, SES, Nodemailer) | 🔴 **KHÔNG** — không ai chèn gì. Phải tự thêm, xem §2 |
| Apple Mail · Outlook · Gmail thủ công | 🔴 **KHÔNG** — và cũng không nên dùng để gửi campaign |

> 🔴 **Nếu gửi qua API, bạn phải tự thêm link huỷ đăng ký vào nội dung.** Header `List-Unsubscribe` một mình **không đủ** để thoả Tw 11.7 — nó chỉ hiện nút ở thanh trên của Gmail, không phải ai cũng thấy, và luật nói về nội dung thư.
>
> Cách nhanh nhất: copy khối footer từ `launchstudio_email.html` (dòng ~289–298) sang bản NL, rồi dịch 4 nhãn: `Unsubscribe` → `Afmelden` · `Update preferences` → `Voorkeuren aanpassen` · `View in browser` → `In browser bekijken` · `Privacy` → `Privacybeleid`.

Bản EN dùng cú pháp **Mailchimp** — nếu dùng ESP khác thì đổi theo bảng ở §1.

---

## 1. Gửi qua nền tảng email marketing

Đây là cách dễ nhất, **và là cách duy nhất gửi được bản NL đúng luật** — nền tảng tự chèn footer huỷ đăng ký.

### 🔴 Chọn nền tảng nào — Mailchimp không còn là mặc định hợp lý

Số liệu 2026:

| | Free | Trả phí từ | Tính tiền theo | Dữ liệu ở | GDPR/AVG |
|---|---|---|---|---|---|
| **Brevo** | **không giới hạn contact**, 300 email/ngày | ~€9/tháng | **Lượng email gửi** | 🇫🇷 Paris | ✅ EU |
| **MailerLite** | **1.000 contact**, 12.000 email/tháng | $10/tháng | Số contact | 🇱🇹 Vilnius | ✅ EU |
| Mailchimp | **250 contact**, 500 email/tháng (250/ngày) | $13/tháng | Số contact | 🇺🇸 Mỹ | ⚠️ Xem dưới |

**Hai lý do Mailchimp kém phù hợp với launchstudio:**

**① Dữ liệu nằm ở Mỹ.** Với doanh nghiệp Hà Lan, chuyển dữ liệu cá nhân sang Mỹ tạo thêm nghĩa vụ pháp lý theo AVG. Brevo (Paris) và MailerLite (Vilnius) đều lưu trong EU nên không có vấn đề này.

**② Tính tiền cả contact đã huỷ đăng ký.** Mailchimp đếm cả người đã unsubscribe vào hạn mức, **trừ khi bạn tự tay archive họ**. Danh sách càng cũ, hoá đơn càng phình mà số người nhận thật không tăng.

Thêm nữa: free plan Mailchimp đã bị cắt từ **2.000 contact (2022) xuống 250** — và giá tăng 5–10%/năm kể từ khi Intuit mua lại năm 2021.

> 💡 **Với launchstudio tôi khuyên Brevo.** Nó tính theo *lượng email gửi* chứ không theo số contact — hợp với mô hình gửi thỉnh thoảng cho một danh sách ổn định. Ví dụ thực tế: 5.000 subscriber gửi 20.000 email/tháng ≈ **€49 ở Brevo** so với **€135+ ở Mailchimp**.
>
> ⚠️ **Nếu đổi sang Brevo hoặc MailerLite, phải đổi merge tag** — bản EN đang dùng cú pháp Mailchimp (`*|UNSUB|*`). Bảng đổi ở cuối §1.

### Mailchimp

1. `Campaigns` → `Create` → `Email` → `Regular`
2. Chọn audience, điền **Subject** và **Preview text** (xem §3)
3. `Content` → `Design Email` → kéo xuống dưới cùng, chọn template **`Code your own`** → **`Paste in code`**
4. Xoá hết nội dung mẫu trong ô, dán toàn bộ file HTML
5. `Save` → `Preview` → `Enter preview mode`

Bản EN dùng cú pháp `*|TAG|*` nên khớp sẵn. Bản NL không có tag — Mailchimp tự thêm footer huỷ đăng ký của nó.

> ⚠️ **Free plan chỉ 250 contact · 500 email/tháng · 250/ngày.** Nếu danh sách của bạn lớn hơn 250 người thì phải trả phí ngay, và Mailchimp đếm cả người đã huỷ đăng ký vào hạn mức.

> ⚠️ **Đừng dùng `Classic Builder` hay drag-and-drop.** Nó sẽ bọc HTML của bạn vào template riêng và phá layout. Phải là `Code your own` → `Paste in code`.

### Brevo (Sendinblue) — 🥇 khuyến nghị cho launchstudio

1. `Campaigns` → `Email` → `Create a campaign`
2. Ở bước chọn editor, chọn **`Paste your code`** (không phải Drag & Drop)
3. Dán HTML
4. Đổi merge tag: `*|UNSUB|*` → `{{ unsubscribe }}` · `*|ARCHIVE|*` → `{{ mirror }}`

Free plan: **không giới hạn contact**, 300 email/ngày — đủ để test và gửi danh sách nhỏ mà không trả gì.

### MailerLite — rẻ nhất ở mọi cỡ danh sách

Free plan: **1.000 contact**, 12.000 email/tháng. EU-based (Vilnius).

1. `Campaigns` → `Create campaign` → `Regular campaign`
2. Chọn **`Custom HTML editor`**
3. Dán HTML
4. Merge tag: `*|UNSUB|*` → `{$unsubscribe}` · `*|ARCHIVE|*` → `{$url}`

### Klaviyo

1. `Campaigns` → `Create Campaign` → `Email`
2. Chọn **`Paste in your own HTML`**
3. Merge tag: `*|UNSUB|*` → `{% unsubscribe %}`

### Bảng đổi merge tag

| Mailchimp (mặc định trong cả hai file) | Brevo | MailerLite | Klaviyo |
|---|---|---|---|
| `*\|UNSUB\|*` | `{{ unsubscribe }}` | `{$unsubscribe}` | `{% unsubscribe %}` |
| `*\|UPDATE_PROFILE\|*` ⟨chỉ bản EN⟩ | `{{ update_profile }}` | `{$preferences}` | — |
| `*\|ARCHIVE\|*` | `{{ mirror }}` | `{$url}` | — |

---

## 2. Gửi qua API hoặc SMTP (Resend, Postmark, SendGrid, AWS SES)

Ở đây **không có ai tự chèn gì** — bạn phải tự xử lý huỷ đăng ký.

### Resend

```js
import { Resend } from 'resend';
import { readFileSync } from 'fs';

const resend = new Resend(process.env.RESEND_API_KEY);
const html = readFileSync('launchstudio_email_nl.html', 'utf8');

await resend.emails.send({
  from: 'LaunchStudio <hallo@launchstudio.eu>',
  to: ['klant@voorbeeld.nl'],
  subject: 'Jouw AI-app werkt. Live gaan is een ander verhaal.',
  html,
  headers: {
    // ⚖️ BAT BUOC khi gui qua API: thay cho link afmelden trong noi dung
    'List-Unsubscribe': '<https://launchstudio.eu/afmelden?e=klant@voorbeeld.nl>, <mailto:afmelden@launchstudio.eu>',
    'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click',
  },
});
```

### Nodemailer / SMTP

```js
await transporter.sendMail({
  from: '"LaunchStudio" <hallo@launchstudio.eu>',
  to: 'klant@voorbeeld.nl',
  subject: 'Jouw AI-app werkt. Live gaan is een ander verhaal.',
  html: readFileSync('launchstudio_email_nl.html', 'utf8'),
  headers: {
    'List-Unsubscribe': '<https://launchstudio.eu/afmelden?e=klant@voorbeeld.nl>',
    'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click',
  },
});
```

> 🔴 **Hai header này không phải tuỳ chọn.** Từ 2024 Gmail và Yahoo **bắt buộc** `List-Unsubscribe` + `List-Unsubscribe-Post` với người gửi từ 5.000 email/ngày, và họ đưa email thiếu nó vào spam. Kể cả gửi ít hơn, có header này vẫn cải thiện deliverability đáng kể.
>
> Header chỉ hiện nút "Unsubscribe" ở thanh trên của Gmail — không phải ai cũng thấy, và Tw 11.7 nói về **nội dung thư**. Bản NL hiện **không có link afmelden trong nội dung**, nên gửi qua API là chưa đúng luật. Copy khối footer từ bản EN sang trước khi gửi.

---

## 3. Subject line và preheader

Hai thứ này **nằm ngoài file HTML** (trừ preheader) và quyết định tỉ lệ mở nhiều hơn toàn bộ nội dung bên trong.

| | Lấy ở đâu | Giá trị hiện tại |
|---|---|---|
| **Subject** | Điền trong ESP | Gợi ý: thẻ `<title>` của file |
| **Preview text** | Điền trong ESP **hoặc** đã có trong file (dòng 58–61) | *"Zes dingen staan tussen een werkend prototype en live gaan…"* |

**Subject gợi ý (NL):** `Jouw AI-app werkt. Live gaan is een ander verhaal.`
**Subject gợi ý (EN):** `Your AI app works. Launching it is a different job.`

> ⚠️ **Đừng điền Preview text trong ESP nếu file đã có preheader** — sẽ hiện hai lần hoặc đè nhau. File này **đã có** khối preheader ẩn, nên để trống ô Preview text trong ESP.
>
> Nếu ESP bắt buộc điền, thì **xoá khối preheader trong file** (dòng 57–61) và dùng ô của ESP.

---

## 4. Kiểm tra trước khi gửi

| # | Việc | Vì sao |
|---|---|---|
| 1 | **Gửi thử tới Gmail, Outlook, Apple Mail** | Ba engine render khác nhau. Outlook (engine Word) dễ vỡ nhất |
| 2 | Mở thử trên điện thoại thật | 4 thẻ phải xếp dọc dưới 620px |
| 3 | Bấm từng link (**4 link** bản NL) | Nhất là nút — mỗi nút có **2 bản href** (MSO + anchor) |
| 4 | Kiểm dark mode | Bật dark mode trên máy rồi mở lại |
| 5 | Kích thước < 102 KB | Hiện **21,5 KB** ✅. Gmail cắt ở 102 KB và ẩn cả footer |
| 6 | Spam score | [mail-tester.com](https://www.mail-tester.com/) — gửi email thử tới địa chỉ nó cấp, xem điểm |
| 7 | **SPF + DKIM + DMARC** | Thiếu là vào spam bất kể nội dung tốt thế nào. Xem §5 |
| 8 | Gửi thử cho chính mình trước | Luôn luôn. Không có nút hoàn tác sau khi gửi |

---

## 5. Ba bản ghi DNS quyết định email có vào inbox hay không

Đây là phần người ta hay bỏ qua rồi thắc mắc sao email vào spam.

| Bản ghi | Làm gì | Kiểm ở đâu |
|---|---|---|
| **SPF** | Khai server nào được gửi thay cho `launchstudio.eu` | [mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx) |
| **DKIM** | Ký số từng email để chứng minh không bị sửa dọc đường | ESP cấp bản ghi, bạn thêm vào DNS |
| **DMARC** | Nói cho Gmail/Outlook biết phải làm gì khi SPF/DKIM không khớp | [dmarcian.com/dmarc-inspector](https://dmarcian.com/dmarc-inspector/) |

Mọi ESP đều có hướng dẫn riêng cho phần này — tìm "domain authentication" trong phần cài đặt của họ. Làm xong một lần, dùng mãi.

---

## 6. Những thứ KHÔNG được làm với file này

| ❌ Đừng | Vì sao |
|---|---|
| Mở bằng trình soạn thảo rich text (Word, Google Docs) rồi copy | Nó thêm rác và phá inline style |
| Chạy qua prettier / formatter / minifier | Phá comment `<!--[if mso]-->` → **nút vỡ trong Outlook** |
| Dán vào drag-and-drop builder của ESP | Builder bọc lại HTML và phá layout. Phải dùng chế độ "paste HTML" |
| Xoá `<div>` preheader vì trông như code rác | Nó là dòng text cạnh tiêu đề trong hộp thư |
| Gộp hai href trùng của mỗi nút | Một cái cho Outlook (VML), một cho client khác. Cả hai đều cần |
| Thêm ảnh mà không có `alt` | Nhiều client tắt ảnh mặc định |

### Kiểm nhanh file còn nguyên vẹn

```bash
grep -c "if mso"    launchstudio_email_nl.html   # phai ra 3
grep -c "opacity:0" launchstudio_email_nl.html   # phai ra 1
grep -c "<table"    launchstudio_email_nl.html   # phai ra 9
grep -c "<a "       launchstudio_email_nl.html   # phai ra 4
grep -c "CAMPAIGN"  launchstudio_email_nl.html   # phai ra 0 SAU khi thay
```

---

## 7. Sau khi gửi — đọc báo cáo ở đâu

Ba link web đều có `utm_content` khác nhau, nên trong **GA4** bạn xem được nút nào mang click:

`Reports` → `Acquisition` → `Traffic acquisition` → đổi dimension sang **`Session manual ad content`**

| `utm_content` | Nút |
|---|---|
| `logo` | Logo ở header |
| `btn-visitus` | Nút chính "Bekijk onze site" |
| `footer_cta` | Nút "Gratis prijsopgave aanvragen" |

> ⚠️ **Nút `Plan 15 minuten` là `mailto:` nên không đo được.** ESP không đếm click mailto, GA4 cũng không thấy. Đếm theo số email thật nhận được với subject `Plan 15 minuten`.

Nếu `btn-visitus` thắng `footer_cta` nhiều, lần sau đẩy nội dung quan trọng lên cao hơn. Nếu ngược lại, người đọc cần đọc hết mới quyết định — giữ email dài.
