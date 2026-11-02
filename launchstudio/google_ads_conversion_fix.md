# Sửa conversion Google Ads cho launchstudio.eu

Ngày quét: 2026-11-02

Trang đã quét:
- https://launchstudio.eu/
- https://launchstudio.eu/vibe-coding-nederlands/
- https://launchstudio.eu/ai-app-bouwen-vanaf-scratch/
- https://launchstudio.eu/ai-app-beveiliging/
- https://launchstudio.eu/ai-app-integraties/
- https://launchstudio.eu/en/ai-app-into-production/

Trang nào cũng có Google tag (`GT-PHGNSPL8`, `AW-18358422807`), nhưng chưa trang nào ghi nhận được conversion. Các nút đều gọi hàm `gtag_report_conversion()`, nhưng hàm này không tồn tại.

**Conversion cần ghi nhận:** "Lượt yêu cầu thông tin báo giá", label `AW-18358422807/M9EmCJ_VzNscEJea_bFE`, giá trị 1 EUR.

---

## Bước 1: Dán code vào `<head>` (làm 1 lần cho cả site)

Dán vào `wp-content/themes/launchstudio/header.php`, ngay sau dòng `wp_head();`:

```html
<script>
function gtag_report_conversion(url) {
  var done = false;
  var callback = function () {
    if (done) return;
    done = true;
    if (typeof url !== 'undefined') { window.location = url; }
  };
  if (typeof gtag === 'function') {
    gtag('event', 'conversion', {
      'send_to': 'AW-18358422807/M9EmCJ_VzNscEJea_bFE',
      'value': 1.0,
      'currency': 'EUR',
      'event_callback': callback
    });
  }
  setTimeout(callback, 1000);
  return false;
}
</script>
```

⚠️ Không dán thêm đoạn `gtag.js` trong hướng dẫn của Google, vì Site Kit đã cài đoạn đó rồi.

---

## Bước 2: Thêm 1 dòng vào form của từng trang

Ở mỗi chỗ trong bảng, tìm đúng dòng ở cột "Tìm dòng", rồi thêm dòng này ngay bên dưới:

```js
gtag_report_conversion();
```

| # | Trang | File / form | Tìm dòng |
|---|---|---|---|
| 1 | Trang chủ | Template trang chủ, form `cContactForm` | `if (result && result.success) {` |
| 2 | Trang chủ (popup báo giá) | `wp-content/themes/launchstudio/main.js`, form `qqContactForm` | `if (result && result.success) {` |
| 3 | `/vibe-coding-nederlands/` | Template trang, form `quote-form` | `if (result?.success !== true) throw new Error("Request not confirmed");` |
| 4 | `/ai-app-bouwen-vanaf-scratch/` | Template trang, form `lsContactForm` | `if (result?.success !== true) throw new Error('Request not confirmed');` |
| 5 | `/ai-app-beveiliging/` | Template trang, form `security-quote` | `if (result?.success !== true) throw new Error("Request not confirmed");` |
| 6 | `/ai-app-integraties/` | Template trang, form `lsContactForm` | `if (result?.success !== true) throw new Error("Request not confirmed");` |
| 7 | `/en/ai-app-into-production/` | Template trang, form `launchInquiry` | `if (result?.success !== true) throw new Error("Request not confirmed");` |

---

## Bước 3: Xóa `onclick="gtag_report_conversion()"` ở các nút sau

**Nút dùng chung trên mọi trang** (nằm trong header/menu, chỉ cần xóa 1 lần):

| Nút | Đoạn code |
|---|---|
| "Gratis offerte" ở menu (NL) | `<a href="https://launchstudio.eu/#contact" class="btn" onclick="gtag_report_conversion()">` |
| Nút báo giá ở menu (EN) | `<a href="https://launchstudio.eu/en/#contact" class="btn" onclick="gtag_report_conversion()">` |
| Nút cuộn xuống form | `<a href="#contact" class="pbtn" onclick="gtag_report_conversion()">` |

**Nút gửi form, mỗi trang một nút:**

| Trang | Nút |
|---|---|
| Trang chủ | `<button type="submit" class="btn bfm" onclick="gtag_report_conversion()">` |
| Trang chủ (popup báo giá) | `<button type="submit" class="btn qq-btn" onclick="gtag_report_conversion()">` |
| `/vibe-coding-nederlands/` | `<button class="vcp-btn vcp-btn-p" id="quote-submit" type="submit" onclick="gtag_report_conversion()">` |
| `/ai-app-bouwen-vanaf-scratch/` | `<button class="bas-btn bas-form-submit" type="submit" onclick="gtag_report_conversion()">` |
| `/ai-app-beveiliging/` | `<button class="ais-btn ais-primary" type="submit" onclick="gtag_report_conversion()">` |
| `/ai-app-integraties/` | `<button type="submit" class="ai-btn ai-primary" ... onclick="gtag_report_conversion()">` |
| `/en/ai-app-into-production/` | `<button class="vc-button vc-button-primary" type="submit" id="f-submit" onclick="gtag_report_conversion()">` |

✅ **Không sửa** các link email `mailto:wearehereforyou@launchstudio.eu`. Có Bước 1 là các link này tự hoạt động.

---

## Bước 4: Lưu và kiểm tra

1. Lưu file và upload lên server. Nếu theme có child theme thì sửa trong child theme.
2. Xóa cache nếu site có plugin cache.
3. Quét lại cả 6 trang để xác nhận.

Có thể tự kiểm tra bằng https://tagassistant.google.com: gửi thử 1 form, phải thấy event `conversion` gửi tới `AW-18358422807/M9EmCJ_VzNscEJea_bFE`.

---

**Kết quả sau khi sửa:** conversion chỉ được đếm khi **form gửi thành công**, hoặc khi khách **bấm link email**. Bấm nút "Gratis offerte" để cuộn xuống form sẽ không còn bị tính là lead.
