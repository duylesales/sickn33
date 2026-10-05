# 🎯 Phân biệt conversion từ Google Ads và từ truy cập tự nhiên

> **Ngày:** 05/10/2026 · **Áp dụng cho:** launchstudio.eu (NL/EU) và unicoconnect.com (US/IN)
> **Bối cảnh:** cả hai dự án đều ở volume rất thấp (<1 đến ~3 lead/tháng từ ads). Điều này thay đổi câu trả lời — xem §5.

---

## 1. Cơ chế gốc: GCLID

Mỗi lượt nhấp từ Google Ads đều được Google tự gắn tham số vào URL đích:

```
https://launchstudio.eu/nl/developer-inhuren?gclid=Cj0KCQjw...
```

**Truy cập tự nhiên không bao giờ có `gclid`.** Đây là tín hiệu xác định (deterministic), không phải suy đoán thống kê. Nếu form submit kèm theo một `gclid`, lead đó đến từ ads — chắc chắn.

Điều kiện: bật **Auto-tagging** trong Google Ads (`Settings → Account settings → Auto-tagging`). Mặc định bật, nhưng phải kiểm tra lại.

> ⚠️ Trên iOS, một phần lượt nhấp trả về `wbraid` hoặc `gbraid` thay vì `gclid` (do giới hạn quyền riêng tư của Apple). Code phải bắt cả ba tham số, nếu không sẽ mất một phần traffic iOS.

---

## 2. 🔴 Ba thứ phá vỡ cơ chế này — và thứ thứ hai là nghiêm trọng nhất

### ① Từ chối cookie (EU/NL)

Nếu khách bấm "Từ chối" trên cookie banner, tag không được phép ghi cookie → mất gclid. Ở thị trường Hà Lan, tỷ lệ từ chối thường **30–50%**.

**Xử lý:** Consent Mode v2 (bắt buộc pháp lý ở EU từ 2024). Nó không cứu được dữ liệu đã mất, nhưng cho phép Google mô hình hoá phần thiếu, và giữ cho tài khoản không bị hạn chế.

```javascript
// Phải chạy TRƯỚC khi load gtag
gtag('consent', 'default', {
  'ad_storage':        'denied',
  'ad_user_data':      'denied',
  'ad_personalization':'denied',
  'analytics_storage': 'denied',
  'wait_for_update':   500
});
// Sau khi khách đồng ý:
gtag('consent', 'update', { 'ad_storage':'granted', 'ad_user_data':'granted',
                            'ad_personalization':'granted', 'analytics_storage':'granted' });
```

### ② 🔴 Safari cắt cookie chứa gclid xuống **24 giờ**

Đây là chi tiết quan trọng nhất trong cả tài liệu này, và là thứ hầu hết hướng dẫn bỏ sót.

Safari ITP giới hạn cookie tạo bằng `document.cookie` ở **7 ngày**. Nhưng khi URL có tham số theo dõi (`gclid`, `fbclid`…) — gọi là *link decoration* — giới hạn tụt xuống **24 giờ**.

**Hệ quả cho B2B:** chu kỳ cân nhắc của một deal €15.000–150.000 là nhiều tuần. Khách bấm quảng cáo thứ Hai, nghiên cứu hai tuần, điền form sau đó. Trên Safari, gclid đã biến mất từ thứ Ba. **Lead đó sẽ bị ghi nhận là organic.**

Safari chiếm phần lớn traffic iPhone/Mac — ở thị trường Hà Lan và Mỹ, đó là một tỷ lệ rất lớn của buyer B2B.

**Xử lý:** đặt cookie **từ phía server** qua header `Set-Cookie`. Cookie server-set không chịu giới hạn 7 ngày / 24 giờ của ITP.

```javascript
// Express / Next.js middleware — chạy ở server, KHÔNG phải trong browser
export function middleware(req) {
  const url  = new URL(req.url);
  const click = url.searchParams.get('gclid')
             || url.searchParams.get('wbraid')
             || url.searchParams.get('gbraid');
  const res = NextResponse.next();
  if (click && !req.cookies.get('ls_click')) {
    res.cookies.set('ls_click', JSON.stringify({
      id:      click,
      type:    url.searchParams.get('gclid') ? 'gclid'
             : url.searchParams.get('wbraid') ? 'wbraid' : 'gbraid',
      lp:      url.pathname,
      utm:     url.searchParams.get('utm_campaign') || '',
      ref:     req.headers.get('referer') || '',
      ts:      new Date().toISOString(),
    }), {
      maxAge:   90 * 24 * 3600,  // 90 ngày = cửa sổ upload tối đa của Google
      httpOnly: false,           // false để form JS đọc được; server-set nên vẫn thoát ITP cap
      secure:   true,
      sameSite: 'lax',
      path:     '/',
    });
  }
  return res;
}
```

> 💡 **Ghi first-touch, không ghi đè.** Điều kiện `!req.cookies.get('ls_click')` giữ lại lần nhấp ads đầu tiên. Nếu ghi đè mỗi lần, một khách quay lại qua organic rồi lại qua ads sẽ làm rối chuỗi. Với B2B, first-touch phản ánh đúng ai *mang khách đến*.

### ③ Đa điểm chạm: ads mang đến, organic chốt

Trường hợp khó nhất, và là trường hợp **phổ biến nhất** trong B2B:

> Khách bấm quảng cáo → đọc → rời đi → một tuần sau Google tên thương hiệu → vào thẳng website → điền form.

- **GA4** (last-non-direct) ghi công cho **Organic Search**
- **Google Ads** (data-driven, cửa sổ 30–90 ngày) ghi công cho **chiến dịch đó**
- Cả hai đều "đúng" theo định nghĩa của mình, và **hai bảng điều khiển sẽ không bao giờ khớp nhau**

Đây là nguồn gốc của gần như mọi tranh cãi về số liệu ads. Nó không phải lỗi cài đặt.

**Xử lý:** đừng cố làm hai dashboard khớp nhau. Lấy **cookie first-touch trong CRM** làm nguồn sự thật duy nhất (§3).

---

## 3. Triển khai: 4 tầng theo thứ tự công sức

### Tầng 1 — Hidden field trong form → CRM ⭐ bắt buộc

Giá trị cao nhất, công sức thấp nhất.

```html
<form id="contact">
  <input type="hidden" name="click_id"   id="click_id">
  <input type="hidden" name="click_type" id="click_type">
  <input type="hidden" name="landing"    id="landing">
  <input type="hidden" name="source"     id="source">
  <!-- các trường thật -->
</form>

<script>
(function () {
  var c = {};
  try {
    var raw = document.cookie.split('; ').find(s => s.startsWith('ls_click='));
    if (raw) c = JSON.parse(decodeURIComponent(raw.split('=').slice(1).join('=')));
  } catch (e) {}
  document.getElementById('click_id').value   = c.id   || '';
  document.getElementById('click_type').value = c.type || '';
  document.getElementById('landing').value    = c.lp   || location.pathname;
  document.getElementById('source').value     = c.id ? 'google_ads' : 'organic_or_other';
})();
</script>
```

Trong CRM, mỗi lead giờ có trường `source` = `google_ads` hoặc `organic_or_other`. **Đây là câu trả lời trực tiếp cho câu hỏi của bạn**, và nó không phụ thuộc vào bất kỳ dashboard nào.

### Tầng 2 — Offline Conversion Import ⭐ bắt buộc từ tháng 2

Khi lead trở thành *qualified call* hoặc *deal won*, upload ngược về Google Ads kèm `gclid` và giá trị thật.

| Trường | Ví dụ |
|---|---|
| `Google Click ID` | `Cj0KCQjw...` |
| `Conversion Name` | `Qualified Call` / `Deal Won` |
| `Conversion Time` | `2026-10-20 14:30:00+02:00` |
| `Conversion Value` | `45000` |
| `Conversion Currency` | `EUR` |

> 🔴 **Hạn 90 ngày.** Google chỉ giữ gclid trong 90 ngày kể từ lượt nhấp. Conversion upload muộn hơn **bị từ chối im lặng**. Với chu kỳ bán B2B dài, phải upload ở mốc *qualified*, đừng đợi tới *deal won* — nhiều deal sẽ vượt 90 ngày.

### Tầng 3 — Enhanced Conversions for Leads

Thay vì (hoặc bên cạnh) gclid, gửi email đã hash SHA-256 ở bước lead, rồi upload lại cùng hash khi lead chuyển đổi. Google tự ghép.

**Ưu điểm:** hoạt động cả khi gclid đã mất vì consent hoặc ITP. Dễ cài hơn gclid matching. **Nên bật song song với Tầng 2, không thay thế.**

### Tầng 4 — Server-side tagging (GTM Server Container)

Chỉ cân nhắc khi volume đã đủ lớn để sai lệch dữ liệu gây tốn tiền thật. **Ở volume hiện tại của cả hai dự án: chưa cần.** Chi phí hạ tầng và công bảo trì vượt giá trị thu được.

---

## 4. Tách conversion action — việc 10 phút, tác động lớn

Trong Google Ads, tạo **hai conversion action riêng**, không gộp:

| Action | Đếm | Primary? | Dùng để |
|---|---|---|---|
| `Form Submit` | Mọi form | ❌ Secondary | Quan sát |
| `Qualified Lead` | Chỉ lead đã sàng lọc (upload offline) | ✅ **Primary** | Smart Bidding học |

> 🔴 Nếu để `Form Submit` làm primary, Smart Bidding sẽ đi tìm **thêm form submit**, không tìm thêm khách hàng. Với CPL ngành này, đó là cách nhanh nhất để đốt ngân sách vào lead rác. Điểm này đã nêu trong `google_search_ads_master_plan.md` §9.3 — phần cài đặt kỹ thuật nằm ở đây.

---

## 5. 🔴 Điều quan trọng nhất: ở volume này, dashboard sẽ nói dối

| Dự án | Lead ads/tháng (ước tính) |
|---|---:|
| launchstudio — cluster `developer inhuren` tier 🟢 | **0,3 – 0,8** |
| unicoconnect — toàn tài khoản @ $5.000/tháng | **2 – 3** |

Ở mức này:

- **GA4 sẽ làm tròn và mô hình hoá.** Với vài chục session, mô hình attribution của GA4 không có đủ dữ liệu để chạy, và nó vẫn sẽ hiển thị một con số trông có vẻ chính xác.
- **Google Ads sẽ báo conversion "được mô hình hoá"** cho phần traffic từ chối cookie. Đó là ước lượng, không phải đếm.
- **Hai bảng sẽ lệch nhau 30–50%**, và không bảng nào sai.

> 💡 **Khuyến nghị:** với 1–3 lead/tháng, **đừng dùng dashboard để ra quyết định.** Dùng một bảng tính, một dòng cho mỗi lead, cột `click_id` lấy từ CRM. Đối soát thủ công.
>
> Ở volume này việc đó mất 10 phút/tháng và **chính xác hơn bất kỳ công cụ attribution nào**. Tự động hoá chỉ đáng làm khi số lead vượt mức mà con người đọc hết được — tức khoảng 30–50/tháng.

---

## 6. Cách đơn giản nhất, nếu không muốn động vào code

Hai thủ thuật low-tech nhưng hiệu quả ở volume thấp:

**① Landing page riêng chỉ dùng cho ads.** Ví dụ `/nl/developer-inhuren-nu` không có link nào trỏ tới từ menu, sitemap, hay nội dung. Mọi form submit từ URL đó **chắc chắn** đến từ ads. Không cần cookie, không bị ITP, không bị consent ảnh hưởng.

> ⚠️ Đánh đổi: trang này không nhận được organic traffic, nên mất giá trị SEO. Chỉ hợp lý nếu đã có trang SEO tương đương ở URL khác. Và `noindex` nó, nếu không sẽ tạo nội dung trùng lặp.

**② Số điện thoại riêng cho ads.** Dùng một số chỉ xuất hiện trong ad extension và trên landing page ads. Mọi cuộc gọi tới số đó là từ ads.

Hai cách này không thay thế được GCLID (chúng không cho phép upload offline conversion để Smart Bidding học), nhưng chúng cho **con số sạch tuyệt đối** để đối chiếu — hữu ích chính xác ở giai đoạn đầu, khi bạn cần biết kênh này có đáng tiếp tục không.

---

## 7. Thứ tự làm

| # | Việc | Công sức | Bắt buộc? |
|---|---|---|---|
| 1 | Kiểm tra Auto-tagging đã bật | 2 phút | ✅ |
| 2 | Tách 2 conversion action, đặt `Qualified Lead` làm primary | 10 phút | ✅ |
| 3 | Cookie server-set bắt `gclid`/`wbraid`/`gbraid`, 90 ngày, first-touch | 1–2 giờ dev | ✅ |
| 4 | Hidden field trong form → CRM | 30 phút dev | ✅ |
| 5 | Consent Mode v2 (chỉ launchstudio — EU) | 1–2 giờ | ✅ pháp lý |
| 6 | Landing page riêng cho ads + số điện thoại riêng | 1 giờ | 🟡 nên |
| 7 | Offline Conversion Import (từ tháng 2) | 2–3 giờ | ✅ |
| 8 | Enhanced Conversions for Leads | 1 giờ | 🟡 nên |
| 9 | Server-side GTM | 1–2 ngày | ❌ chưa cần |

---

## Nguồn

- [Google — Set up offline conversions using GCLID](https://support.google.com/google-ads/answer/7012522)
- [Google — Offline conversion imports FAQs (cửa sổ 90 ngày)](https://support.google.com/google-ads/answer/10029210)
- [Google — Enhanced conversions for leads](https://support.google.com/google-ads/answer/13548778)
- [Safari ITP: tác động và giải pháp — giới hạn 24h với URL link-decorated](https://usehardal.com/safari-itp-guide)
- [Snowplow — tracking cookie lifetimes](https://snowplow.io/blog/tracking-cookies-length)
