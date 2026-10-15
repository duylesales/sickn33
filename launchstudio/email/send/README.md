# 📬 Mail merge — gửi từng email từ danh sách

> `send.py` · mặc định **dry run**, phải thêm `--send` mới gửi thật

---

## 1. 🔴 Đọc trước: khi nào KHÔNG nên dùng script này

| Số người nhận | Nên dùng |
|---|---|
| < 50, danh sách riêng, gửi một lần | ✅ Script này |
| 50–500 | ⚠️ Được, nhưng ESP tốt hơn |
| > 500, hoặc gửi định kỳ | 🔴 **Dùng Brevo hoặc MailerLite** |

Ba thứ ESP làm mà script này không làm được:

- **Quản lý huỷ đăng ký tự động** — người bấm Afmelden được gỡ khỏi list ngay. Script này cần bạn tự thêm họ vào `unsubscribed.csv`
- **Xử lý bounce** — email không tồn tại sẽ dội lại; gửi tiếp cho họ làm hỏng uy tín domain
- **Warm-up IP và throttle thông minh** — gửi 500 email trong một giờ từ domain mới là vào spam chắc chắn

---

## 2. Chạy thử

```bash
cd launchstudio/email/send
python3 send.py --html ../launchstudio_email_nl.html --csv recipients.csv
```

Không có `--send` nên nó chỉ in ra xem sẽ gửi cho ai, và cảnh báo nếu thiếu gì.

### Gửi thật

```bash
export RESEND_API_KEY=re_xxxxx
export UNSUB_SECRET="chuoi-bi-mat-dai-ngau-nhien"

python3 send.py --html ../launchstudio_email_nl.html --csv recipients.csv --send
```

### Gửi thử 1 người trước — luôn làm bước này

```bash
python3 send.py --html ../launchstudio_email_nl.html --csv recipients.csv --limit 1 --send
```

---

## 3. File CSV

`recipients.csv` — hai cột, header đúng chính tả:

```csv
name,email
Thijs de Vries,thijs@voorbeeld.nl
Sanne Bakker,sanne@voorbeeld.nl
```

`unsubscribed.csv` — ai đã huỷ. Script **tự bỏ qua** họ:

```csv
email
mark@voorbeeld.nl
```

> 💡 Export từ Excel/Numbers thì chọn **CSV UTF-8**. Script đọc `utf-8-sig` nên BOM của Excel không gây lỗi.

---

## 4. Token cá nhân hoá

Đặt vào HTML, script tự thay:

| Token | Thành |
|---|---|
| `{{name}}` | `Thijs de Vries` |
| `{{first_name}}` | `Thijs` |
| `{{email}}` | `thijs@voorbeeld.nl` |
| **`{{unsubscribe_url}}`** | `https://launchstudio.eu/afmelden?e=…&t=<hmac>` |

### 🔴 `{{unsubscribe_url}}` là token bắt buộc

Bản NL hiện **không có link huỷ đăng ký**, nên script sẽ **từ chối gửi**:

```
DUNG: khong gui khi thieu link huy dang ky. Them {{unsubscribe_url}} vao HTML.
```

Đây là chủ ý — không phải lỗi. Mở `footer-snippet.html` trong thư mục này, copy, dán thay cho khối địa chỉ ở cuối `launchstudio_email_nl.html`.

### Vì sao link có HMAC

Đặt `UNSUB_SECRET` thì link thành `?e=thijs@…&t=a3f2…`. Chữ `t` là HMAC-SHA256 của email.

Không có nó, ai cũng đoán được URL và huỷ đăng ký thay người khác — chỉ cần đổi `?e=` thành email bất kỳ. Endpoint `/afmelden` của bạn phải kiểm `t` khớp trước khi huỷ.

---

## 5. Bốn rào an toàn trong script

| Rào | Làm gì |
|---|---|
| **Dry run mặc định** | Không có `--send` thì không gửi gì |
| **`sent.log`** | Mỗi email gửi xong được ghi vào đây. Chạy lại script sẽ **bỏ qua người đã gửi** — crash giữa chừng không gây gửi trùng |
| **`unsubscribed.csv`** | Tự bỏ qua. Gửi cho người đã huỷ là vi phạm Tw 11.7 |
| **Chặn khi thiếu unsubscribe** | Script `exit 1`, không gửi một email nào |

Thêm `--delay` (mặc định 2 giây/email) để không bị nhà cung cấp chặn.

---

## 6. Giới hạn gửi theo nhà cung cấp

| Nhà cung cấp | Giới hạn | Ghi chú |
|---|---|---|
| **Resend** | 100/ngày (free) · 50.000/tháng (trả phí) | API đơn giản nhất, deliverability tốt |
| Postmark | Theo gói | Rất tốt cho transactional |
| AWS SES | 200/ngày lúc đầu (sandbox) | Phải xin mở sandbox |
| Gmail SMTP | **~500/ngày** | 🔴 Đừng dùng cho marketing — hỏng uy tín tài khoản |
| Microsoft 365 SMTP | ~10.000/ngày, 30/phút | 🔴 Vi phạm điều khoản nếu dùng gửi bulk |

> 🔴 **Đừng dùng SMTP của Gmail hay Microsoft 365 để gửi marketing.** Điều khoản của họ cấm, và tài khoản bị khoá thì mất luôn email công việc. Dùng Resend/Postmark/SES.

---

## 7. Ba thứ phải có ở DNS, không thì vào spam

Bất kể script tốt đến đâu:

| | Kiểm ở |
|---|---|
| **SPF** | [mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx) |
| **DKIM** | Nhà cung cấp cấp bản ghi, bạn thêm vào DNS |
| **DMARC** | [dmarcian.com/dmarc-inspector](https://dmarcian.com/dmarc-inspector/) |

Từ 2024 Gmail và Yahoo **bắt buộc** người gửi từ 5.000 email/ngày phải có đủ ba, cộng `List-Unsubscribe` header — script đã tự thêm header đó cho mỗi email.

---

## 8. Quy trình đề xuất

```
1. Dán footer-snippet.html vào launchstudio_email_nl.html
2. Thay CAMPAIGN (5 chỗ) bằng tên campaign thật
3. export UNSUB_SECRET=... && export RESEND_API_KEY=...
4. python3 send.py ... --limit 1 --send     ← gửi cho chính mình
5. Mở trên Gmail + Outlook + Apple Mail, kiểm link Afmelden
6. python3 send.py ... --send               ← gửi cả list
7. Người bấm Afmelden → thêm vào unsubscribed.csv
```

Bước 7 là bước dễ quên nhất, và cũng là bước mà ESP làm tự động. Nếu list lớn dần, đó là lúc chuyển sang ESP.

### Chuyển sang ESP nào

| | Free | Tính tiền theo | Dữ liệu ở |
|---|---|---|---|
| **Brevo** 🥇 | không giới hạn contact, 300 email/ngày | lượng email gửi | 🇫🇷 EU |
| **MailerLite** | 1.000 contact, 12.000 email/tháng | số contact | 🇱🇹 EU |
| Mailchimp | 250 contact, 500 email/tháng | số contact (**gồm cả người đã huỷ**) | 🇺🇸 Mỹ |

Với doanh nghiệp Hà Lan, Brevo và MailerLite lưu dữ liệu trong EU nên không phát sinh nghĩa vụ chuyển dữ liệu xuyên biên giới theo AVG. Mailchimp lưu ở Mỹ.

Chi tiết ở `../HOW_TO_SEND.md` §1.
