# 📧 Email marketing template — LaunchStudio

> **File:** `launchstudio_email.html` (EN) · `launchstudio_email_nl.html` (NL) · **24,1 / 24,3 KB** · cả hai HTML hợp lệ 0 lỗi · 13 link mỗi bản
> **Cập nhật:** 14/10/2026 — đã đồng bộ với mọi thay đổi trong file
> **Tổng hợp từ:** 4 brief landing page · `launchstudio_info.md` · `google_ads_plan_payments_nl.md` · `conversion_attribution_setup.md`

---

## 1. Email khác landing page ở năm chỗ — lý do code trông "cũ"

| | Landing page | Email |
|---|---|---|
| Layout | flexbox / grid | **`<table>` lồng nhau** — Outlook dùng engine của Word, không hiểu flex |
| CSS | file hoặc `<style>` | **inline trên từng thẻ** — nhiều client xoá `<style>` |
| JS | có | **không** — bị xoá hết. Mọi widget tự chấm điểm phải bỏ |
| SVG | có | **không** (Outlook) — dùng ký tự và màu nền |
| Gradient | có | **Outlook chỉ thấy màu đặc** → mỗi nút có `bgcolor="#2F80ED"` dự phòng |

### 🔴 Font Satoshi KHÔNG load trong email

Gmail, Outlook và phần lớn client không tải webfont. Template khai `'Satoshi','Helvetica Neue',Helvetica,Arial,sans-serif` → thực tế hiện **Arial/Helvetica**. Chữ nhấn dùng **Georgia** thay Instrument Serif.

Màu, gradient, letter-spacing âm, bo góc thì giữ được. **Bản sắc còn ~80%**, chỉ mất riêng chữ.

---

## 2. Cấu trúc 8 khối — nội dung hiện tại

| # | Khối | Nội dung thật trong file | Nền |
|---|---|---|---|
| 0 | Preheader | *"Six things stand between a working prototype and a launch…"* | ẩn |
| 1 | Header | `LaunchStudio.eu` + "Prototype → Production" | — |
| 2 | **Hero** | `Your AI app works. Launching it is a different job.` → nút **Get a free quote** · *Fixed scope, fixed price · Reply in 24 hours · No full rebuild* | trắng |
| 3 | 🪝 **Hook** | **THE PART NOBODY TELLS YOU** → `It is six things, not a rewrite.` | trắng, viền trái **xanh** `#0D9668` |
| 4 | **4 thẻ** | 01 Finish it · 02 Secure it · 03 Connect it · 04 Own it | trắng |
| 5 | **Checklist 6 điểm** | *Free, no email required* → `What "production-ready" actually means` | 🔵 **cyan `#E6F7F5`** |
| 6 | Proof | `11+` years of experience · `160+` projects delivered · `24h` reply time + 1 testimonial | trắng |
| 7 | **CTA cuối** | `Your app, visible. Your data, yours.` · *We will reply within 24 hours* → nút **Request a free quote** | navy `#0B1D35` |
| 8 | Footer | Địa chỉ Amsterdam + 4 link tiện ích, **căn giữa** | — |

### Vì sao hook là "gỡ rào cản" chứ không phải "tạo vấn đề"

Bản này không phê phán app của người đọc. Nó gỡ nỗi sợ số một — *"launch-ready nghĩa là phải build lại"* — bằng cách nói rõ cái gì **giữ** và cái gì **thêm**. Nguồn: `extra-1/32-production-ready-doesnt-mean-rebuilt-debunking-common-fear.md`.

Nó cũng khớp với preheader: preheader nói "six things", hook xác nhận "it is six things", rồi khối 5 liệt kê đúng sáu thứ đó. Ba tầng cùng một lời hứa.

### Vì sao khối 5 cho đi checklist thật

Email chỉ bán thì bị bỏ qua hoặc unsubscribe. Checklist kèm bước tự kiểm 2 phút khiến email **đáng lưu lại** — người tự chấm thấy thiếu 3/6 sẽ tự tìm tới CTA.

### 🔵 Vì sao khối 5 có nền cyan — và vì sao màu chữ phải đậm hơn

Nền `#E6F7F5` là tint cyan của chính brand (`--tint-t` trong brief integrations). Nó tách khối "cho đi giá trị" khỏi các card trắng xung quanh.

⚠️ Nhưng nền sáng buộc chữ phải đậm hơn. Nền cũ `#EEF2F7` **vốn đã không đạt WCAG AA**:

| Chữ | Trên nền cũ | Trên nền cyan hiện tại |
|---|---:|---:|
| Nhãn | `#64748B` → **4.23** ❌ | `#0F766E` → **4.95** ✅ |
| Số 1–6 | `#2F80ED` → **3.44** ❌ | `#1D4ED8` → **6.06** ✅ |
| Chữ mô tả | `#64748B` → 4.23 ❌ | `#475569` → **6.85** ✅ |

Quan trọng với email hơn web: người đọc mail trên điện thoại ngoài trời hoặc màn hình tối.

---

## 3. 🔴 Còn gì phải sửa trước khi gửi

| # | Chỗ | Trạng thái |
|---|---|---|
| 1 | `CAMPAIGN` — **10 lần** | ❌ Đổi thành tên thật, ví dụ `oct26_sixthings`. Find & Replace All |
| 2 | **Nút hero** → `/en/request-quote` | 🔴 **404.** Xem §5 — chỗ chặn duy nhất còn lại |
| 3 | Testimonial (dòng 246) | ❌ Quote thật, hoặc **xoá cả khối**. Đừng bịa |
| 4 | Preheader (dòng 54) | 🟡 Viết lại theo từng lần gửi |
| 5 | `<title>` (dòng 10) | 🟡 Dùng làm subject line — viết lại cho khớp campaign |
| 6 | `*\|UNSUB\|*` · `*\|UPDATE_PROFILE\|*` · `*\|ARCHIVE\|*` | ❌ Merge tag Mailchimp — đổi theo ESP, bảng ở §4 |
| 7 | ~~Footer: tên pháp lý, địa chỉ, KVK~~ | ✅ **Xong** — Herengracht 420, 1017 BZ Amsterdam |
| 8 | ~~Khối Proof: ba dấu `—`~~ | ✅ **Xong** — 11+ / 160+ / 24h, đều là số thật |
| 9 | ~~4 link thẻ dịch vụ~~ | ✅ **Xong** — 3 trang đã live, thẻ 04 trỏ về `/en/` |

---

## 4. ⚖️ Phần pháp lý

Email thương mại ở Hà Lan chịu **AVG (GDPR)** + **Telecommunicatiewet**.

| | Trạng thái |
|---|---|
| Địa chỉ thật | ✅ Herengracht 420, 1017 BZ Amsterdam |
| Link huỷ đăng ký | ✅ có (`*\|UNSUB\|*` — cần đổi merge tag) |
| Lý do nhận email | ✅ dòng đầu footer |
| Tên pháp lý | 🟡 Không có. Danh tính đã xác lập qua logo + địa chỉ `from`. Chấp nhận được, nhưng ghi tên vẫn an toàn hơn nếu bị khiếu nại |
| Số KVK | ⚪ Luật NL yêu cầu KVK trên **hoá đơn và website**, không bắt buộc trong footer email |

➡️ **Footer hiện tại đủ để gửi.**

### Merge tag theo ESP

| ESP | Unsubscribe | Xem trên web |
|---|---|---|
| Mailchimp | `*\|UNSUB\|*` | `*\|ARCHIVE\|*` |
| Brevo | `{{ unsubscribe }}` | `{{ mirror }}` |
| MailerLite | `{$unsubscribe}` | `{$url}` |
| Klaviyo | `{% unsubscribe %}` | — |
| Resend / Postmark | header `List-Unsubscribe` | — |

---

## 5. Hai bản ngôn ngữ — và link KHÔNG chỉ là bỏ `/en/`

| | EN `launchstudio_email.html` | NL `launchstudio_email_nl.html` |
|---|---|---|
| `lang` | `en` | **`nl`** |
| Trang chủ | `/en/` | **`/`** |
| Security | `/en/ai-app-security/` | **`/ai-app-beveiliging/`** |
| Integrations | `/en/ai-app-integrations/` | **`/ai-app-integraties/`** |
| Into production | `/en/ai-app-into-production/` | **`/ai-app-naar-productie/`** |
| Privacy | `/privacy` (301) | **`/privacybeleid/`** |
| mailto subject | `Book 15 minutes` | `Plan 15 minuten` |

### 🔴 Cái bẫy: bỏ `/en/` KHÔNG tự ra bản Hà Lan

Tôi đã kiểm từng URL. Nếu chỉ xoá `/en/`:

```
launchstudio.eu/ai-app-security/   →  HTTP 301  →  /en/ai-app-security/
```

Nó **bật về lại trang tiếng Anh**, qua thêm một redirect. Người đọc Hà Lan bấm link trong email tiếng Hà Lan và đáp xuống nội dung tiếng Anh.

Slug Hà Lan là **từ khác hẳn**, không phải cùng slug bỏ tiền tố:

| Đúng ✅ | Sai ❌ |
|---|---|
| `/ai-app-beveiliging/` | ~~`/ai-app-security/`~~ |
| `/ai-app-integraties/` | ~~`/ai-app-integrations/`~~ |
| `/ai-app-naar-productie/` | ~~`/ai-app-into-production/`~~ |
| `/privacybeleid/` | ~~`/privacy`~~ |

**Cả 5 URL Hà Lan đã verify HTTP 200, không redirect.**

### Trạng thái link — cả hai bản

| Đích | Link | HTTP |
|---|---:|---|
| Trang chủ (`/en/` hoặc `/`) | 6 | ✅ 200 |
| 3 trang dịch vụ | 4 | ✅ 200 |
| `mailto:wearehereforyou@` | 1 | ✅ |
| Privacy | 1 | ✅ 200 (bản NL), 301 (bản EN) |
| Merge tag ESP | 3 | — tuỳ ESP |

➡️ **Không còn link 404 nào ở cả hai bản.**

### Ba điểm kỹ thuật về link — đừng phá

**① Mỗi nút có HAI href phải khớp nhau.** Một trong block `<!--[if mso]>` (VML roundrect cho Outlook) và một trong `<a>` thường. Sửa một mà quên cái kia → Outlook đi tới URL cũ.

**② Fragment phải đứng sau query string.** `…utm_content=footer_cta#contact` ✅ · `…#contact?utm_…` ❌ — viết ngược là `utm` bị coi là phần của fragment và **không bao giờ tới Analytics**.

**③ Mọi link có dấu `/` ở cuối.** Bỏ dấu đó thì WordPress trả 301 và thêm một hop không cần thiết.

> ⚠️ **Click vào `mailto:` không được ESP đếm.** Mailchimp/Brevo không track mailto, nên nút "Book 15 minutes / Plan 15 minuten" sẽ hiện 0 click dù có người dùng. Đếm theo số email thật nhận được theo subject.

### `utm_content` giống nhau ở cả hai bản — chủ ý

```
logo · hero · hook · card_production · card_security
card_integrations · card_own · footer_cta
```

Giữ nguyên tên để **so sánh được hiệu suất khối giữa hai thị trường**. Phân biệt ngôn ngữ bằng `utm_campaign` (ví dụ `oct26_sixthings_en` vs `oct26_sixthings_nl`), không bằng `utm_content`.

---

## 6. 🤖 Dán vào Lovable để xem và sửa

### Nhanh nhất — không cần Lovable

Mở file bằng Chrome, thu cửa sổ về ~620px để thấy bản mobile.

### Prompt cho Lovable — harness xem song song EN / NL

> Paste nguyên khối. Đã cập nhật cho **hai file**.

```
I have two finished HTML email templates — an English one and a Dutch one. Build me a
preview harness around them. Do NOT rewrite the emails themselves.

=== RULE ZERO: BOTH EMAIL FILES ARE READ-ONLY STRUCTURE ===
Put them at `public/email-en.html` and `public/email-nl.html`, byte-for-byte.
You may NOT:
- convert <table> layout to <div>/flex/grid
- move inline styles into a CSS file, a <style> block, or Tailwind classes
- reformat, prettify, minify or re-indent them
- remove any HTML comment, especially the <!--[if mso]> ... <![endif]--> blocks
- remove the hidden preheader <div> (opacity:0, max-height:0 — it is NOT dead code,
  it is the text shown next to the subject line in the inbox)
- change any colour, hex value, font-family stack or px size
- "fix" the duplicated hrefs — every button intentionally has TWO copies of its URL,
  one inside the MSO conditional comment for Outlook and one in the <a> tag
- strip the trailing slashes from any URL
- reorder query strings and #fragments (the fragment must stay AFTER the ?query)
- touch the @media (prefers-color-scheme:dark) block or the [data-ogsc] selectors
- change the `lang` attribute on <html> (en / nl) or any ´ ´ accented character
- translate, "normalise" or spellcheck either file — the Dutch one is deliberately
  Dutch and uses informal jij/je/jouw, plus English loanwords (secrets, webhooks,
  error handling, launch-ready, rebuild). Leave every word alone.
This is email HTML. Every one of those "improvements" breaks it in Outlook, Gmail or
the inbox preview. If you think something is wrong, leave it and tell me instead.

=== WHAT TO BUILD ===
A single-page React preview app (this part can use any styling you like):
1. A language switch: EN / NL. It only changes which file the iframe loads.
2. An <iframe> loading the selected file, centred on a neutral grey background.
3. Width toggle: 600px (desktop) / 375px (mobile). Only the iframe width changes.
4. Light / dark toggle that sets `color-scheme` on the iframe document, so I can check
   the prefers-color-scheme rules inside the email.
5. A <textarea> prefilled with the raw contents of the selected file, and a "Render"
   button that pushes the textarea value into the iframe via srcdoc. This is how I
   edit copy and see the result. Keep it a plain textarea — no code editor library,
   no auto-formatting, no syntax reformatting on paste, no spellcheck
   (set spellcheck="false").
6. "Copy HTML" and "Download .html" buttons that output the textarea content unchanged,
   named after the selected language.
7. A read-only panel listing every href found in the current textarea content: show the
   path and the utm_content value. Do not modify them. Add a small warning badge next
   to any href that contains "/en/" while NL is selected, or any href whose path is
   English while NL is selected — the Dutch email must use /ai-app-beveiliging/,
   /ai-app-integraties/ and /ai-app-naar-productie/, never the English slugs.
8. A side-by-side mode that shows both iframes at 600px next to each other, so I can
   compare EN and NL block by block.

=== DO NOT ===
- Do not add a build step, bundler plugin or post-processor for the email files
- Do not add a linter, formatter or prettier config that touches them
- Do not add images, icons or fonts to the emails
- Do not "componentise" the emails into React components
- Do not generate a third language or auto-translate anything
```

### 🔴 Bốn thứ Lovable hay phá nhất ở hai file này

| Thứ nó sẽ làm | Hậu quả |
|---|---|
| Xoá `<div>` preheader (opacity:0, max-height:0 — trông như code rác) | Mất dòng text cạnh tiêu đề trong hộp thư → tỉ lệ mở giảm |
| Gộp 2 href trùng của mỗi nút thành 1 | **Nút vỡ trong Outlook** — VML roundrect mất link |
| Đổi table thành div hoặc gom inline style vào class | Layout vỡ hoàn toàn trong Outlook |
| 🆕 "Sửa" tiếng Hà Lan — bỏ dấu `é`/`í`, đổi loanword tiếng Anh, hoặc đổi `jij` thành `u` | Giọng văn sai hẳn so với `launchstudio.eu` (site dùng **informal `jij/je`**) |

### Kiểm nhanh sau khi Lovable chạy

```bash
for f in public/email-en.html public/email-nl.html; do
  echo "$f"
  grep -c "if mso"    "$f"   # phai ra 3
  grep -c "opacity:0" "$f"   # phai ra 1
  grep -c "<table"    "$f"   # phai ra 10
  grep -c "<a "       "$f"   # phai ra 13
done
grep -c "/en/" public/email-nl.html   # phai ra 0
```

## 7. ✅ Kiểm tra trước khi gửi

| # | Việc | Vì sao |
|---|---|---|
| 1 | **Gửi thử tới Gmail + Outlook + Apple Mail** | Ba engine render khác nhau. Outlook dễ vỡ nhất |
| 2 | Kiểm trên điện thoại thật | 4 thẻ phải xếp dọc dưới 620px |
| 3 | **Kiểm dark mode** | ⚠️ Khối cyan có class `.bg-soft` → dark mode đổi nền thành `#16203A`, nhưng chữ `#0F766E` và `#1D4ED8` sẽ **quá tối**. Xem §8① |
| 4 | Bấm từng link (13 link) | Nhất là 2 cặp nút MSO/anchor |
| 5 | Tắt ảnh rồi đọc lại | Template không dùng ảnh nào — xác nhận lại |
| 6 | Kích thước < 102 KB | Hiện **24,1 KB**. Gmail cắt ở 102 KB và ẩn cả phần unsubscribe |
| 7 | Spam score | mail-tester.com. Chú ý tỉ lệ chữ/ảnh |
| 8 | SPF + DKIM + DMARC | Thiếu là vào spam bất kể nội dung tốt thế nào |
| 9 | Merge tag unsubscribe đã đổi đúng ESP | §4 |

---

## 8. Việc còn lại và gợi ý

### ① 🟡 Dark mode cho khối cyan chưa hoàn chỉnh

`.bg-soft` trong dark mode đổi nền sang `#16203A`. Trên nền tối đó:

| Chữ | Vấn đề |
|---|---|
| `#0F766E` nhãn | Quá tối, gần như không đọc được |
| `#1D4ED8` số 1–6 | Quá tối |

**Cần thêm 2 dòng** vào block `@media (prefers-color-scheme:dark)` và `[data-ogsc]`, ví dụ `.cy-label{color:#5EEAD4!important}` và `.cy-num{color:#93C5FD!important}` + gắn class tương ứng. Nói là tôi làm.

### ② 🟡 Preheader là chỗ duy nhất còn nói 48 giờ

Email giờ nói **24 giờ** ở ba chỗ, nhưng preheader vẫn nói 48 giờ:

| Nội dung | Mốc | Ở đâu |
|---|---|---|
| *Reply in 24 hours* | **24h** | trust strip hero |
| *reply time* | **24h** | ô stat 3 |
| *We will reply within 24 hours.* | **24h** | CTA cuối |
| *plus a fixed-price quote in 48 hours* | ⚠️ **48h** | **preheader (dòng 54)** |

🔴 Preheader là **dòng đầu tiên người nhận đọc**, ngay cạnh tiêu đề trong hộp thư. Để nó nói 48h trong khi cả email nói 24h là tự tạo mâu thuẫn ở đúng chỗ dễ thấy nhất.

**Sửa gợi ý:** *"Six things stand between a working prototype and a launch. Here they are — and we reply within 24 hours."*

### ③ Email không còn nhắc Manifera

`launchstudio_info.md` §1.2 yêu cầu mọi nội dung LaunchStudio nhắc Manifera ít nhất 1 lần cho E-E-A-T. Hai vị trí ít lộ nhất nếu muốn đưa lại: dòng attribution của testimonial (*"Name, role · built with Lovable"* → thêm *"· via Manifera"*), hoặc footer cạnh địa chỉ.

### ④ Cắt thành chuỗi 3 email thay vì một email dài

Email này nói cả 4 dịch vụ. Hiệu quả hơn: email 1 = hook "six things, not a rewrite" + checklist · email 2 = security · email 3 = payments/iDEAL→Wero. Mỗi email **một CTA duy nhất**.

### ⑤ Bản tiếng Hà Lan không phải bản dịch

`keyword_research_lovable_vibecoding_security.md` §5: compliance dùng **"AVG"** không phải "GDPR", nhưng tên lỗi kỹ thuật giữ tiếng Anh. Nhánh NL có cầu gấp **2,5 lần** nhánh EN.

### ⑥ Email iDEAL → Wero là email dễ mở nhất

iDEAL ngừng **31/12/2027**, mốc đổi branding checkout đã qua **31/3/2026**. Câu *"Mở checkout của bạn ra — nó ghi `iDEAL | Wero` chưa?"* có tính cấp thiết thật.

### Hook thay thế — nếu muốn A/B test

| Register | Headline |
|---|---|
| Tự kiểm, tiền | *Buy something from your own app. Does it notice?* |
| Hạn chót bên ngoài | *iDEAL switches off on 31 December 2027.* |
| Dự đoán | *Your first engineer will read this code.* |
| Người gác cổng | *An enterprise customer will send you a security questionnaire.* |
| Sự cố vendor | *Was your Lovable project created before November 2025?* |
