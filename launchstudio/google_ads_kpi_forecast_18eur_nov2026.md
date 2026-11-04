# 📈 Dự báo KPI conversion Google Search - ngân sách €18/ngày

> **Ngày lập:** 04/11/2026 · **Thị trường:** NL (campaign N1-NL-Service là chính)
> **Bối cảnh:** campaign đã chạy chiến lược giá thầu "Max CPC" (Tối đa hoá lượt nhấp, có giới hạn CPC) được 2 tháng
> **Nguồn:** `volume_analysis_results.md` (Keyword Planner 25/09/2026) · `google_search_ads_master_plan.md` §2.3, §10 · `google_ads_conversion_fix.md` · quét website launchstudio.eu ngày 04/11/2026
> ⚠️ `launchstudio.ru` không truy cập được (máy chủ từ chối kết nối). Dự báo dùng **launchstudio.eu**.

---

## 1. Kết luận nhanh

| Chỉ số / tháng | 🔴 Thận trọng | 🟡 Cơ sở | 🟢 Lạc quan |
|---|---:|---:|---:|
| Chi tiêu | €548 | €548 | €548 |
| CPC trung bình | €10 | €8 | €6,50 |
| Lượt nhấp | 55 | 68 | 84 |
| Lượt hiển thị | ~1.370 | ~1.370 | ~1.400 |
| CTR | 4% | 5% | 6% |
| Tỉ lệ chuyển đổi trang đích | 2,5% | 4% | 6% |
| **Conversion (lead)** | **1,4** | **2,7** | **5,1** |
| **CPL** (chi phí mỗi lead) | **€400** | **€200** | **€108** |
| Tỉ lệ chốt deal | 10% | 15% | 25% |
| Khách hàng mới | 0,14 | 0,41 | 1,26 |
| **CAC** (chi phí có 1 khách) | €4.000 | €1.333 | €433 |

**Trong 90 ngày tới (kịch bản cơ sở):** ~€1.643 chi tiêu · ~205 lượt nhấp · **~8 lead** · ~1 khách hàng.

**Ba điều quan trọng nhất:**

1. **€18/ngày là mức vừa đúng.** Trần chi tiêu thật của N1-NL-Service khoảng €553-691/tháng (`volume_analysis_results.md` §3). €548/tháng gần chạm trần ở CPC €8. Tăng ngân sách gần như không thêm được lượt nhấp có chất lượng, chỉ làm CPC tăng hoặc Google mở rộng sang truy vấn rác.
2. **Dữ liệu conversion của 2 tháng qua không dùng được.** Trước khi sửa (02/11/2026), hàm `gtag_report_conversion()` không tồn tại, nên Google Ads gần như không ghi nhận conversion nào. Chỉ dữ liệu **lượt nhấp, CPC, CTR, search terms** của 2 tháng là đáng tin. Mọi con số conversion ở trên là ước tính, chưa phải số đo.
3. **Chưa thể chuyển sang Smart Bidding.** Ở ~3 conversion/tháng, cần khoảng 5 tháng mới có 15 conversion, mức tối thiểu Google khuyến nghị cho tCPA. Giữ **Max CPC (Tối đa hoá lượt nhấp + giới hạn CPC) hoặc Manual CPC**.

---

## 2. Giả định đầu vào

| Giả định | Giá trị | Nguồn / lý do |
|---|---|---|
| Ngân sách | €18 × 30,42 ngày = **€547,56/tháng** | Google có thể tiêu tới 2× trong 1 ngày, nhưng không vượt tổng tháng |
| Volume tìm kiếm N1 | ~1.280 lượt/tháng | Keyword Planner, top: `app laten maken` 480 · `webapplicatie laten maken` 260 · `app laten bouwen` 140 |
| Lượt hiển thị khả dụng | ~1.380/tháng | 1.280 × 1,8 (phrase mở rộng) × 60% IS |
| CPC | €6,50-10 | Repo benchmark NL €8-14. Tối đa hoá lượt nhấp thường kéo CPC xuống thấp hơn Manual CPC |
| LP conversion | 2,5-6% | Mục tiêu sống còn trong master plan là ≥5% |
| Tỉ lệ chốt | 10-25% | Thấp vì phần lớn volume là "xây app mới", không phải "đã có prototype" (`volume_analysis_results.md` §5) |
| Giá trị deal trung bình | ~€2.000 | Giữa khoảng Launch Ready €800-3.500 |
| Biên lợi nhuận gộp | ~40% | **Giả định**, cần xác nhận. CAC hoà vốn ≈ €800 |

---

## 3. Website: những gì ảnh hưởng tới tỉ lệ chuyển đổi

Quét launchstudio.eu ngày 04/11/2026:

**Điểm cộng cho conversion**
- Hero rõ ràng cho đúng ICP: "Jij bouwde het met AI. Wij maken het launch-ready." (Lovable, Bolt, Cursor)
- Hai CTA: "Bekijk wat het kost" (máy tính giá) và "Vraag een gratis offerte aan"
- Có lead magnet: checklist 20 mục "Launch readiness"
- Tín hiệu tin cậy: 11+ năm, 160+ dự án, 1-3 tuần, giá cố định €800-7.500, trích dẫn CEO Manifera Herre Roelevink
- Quy trình 3 bước, có cuộc gọi 15 phút

**Rủi ro cho conversion**
- Thông điệp nhắm người **đã có prototype**, nhưng 85% volume N1 là người **muốn xây mới** (`app laten maken`). Đây là lý do kịch bản cơ sở chỉ để LP conversion 4%, không phải 5%.
- Trang `/ai-app-beveiliging/` không có thẻ `<form>` trong HTML trả về, cần kiểm tra form có hiển thị không.

**Trạng thái tracking (quét lại 04/11/2026)**

| Hạng mục trong `google_ads_conversion_fix.md` | Trạng thái |
|---|---|
| Bước 1: hàm `gtag_report_conversion()` trong `<head>` | ✅ Có trên cả 6 trang |
| Bước 3: xoá `onclick` trên nút | ✅ Không còn `onclick` nào |
| Bước 2: gọi conversion khi form gửi thành công | ⚠️ Chỉ xác nhận được **popup `qqContactForm`** trong `main.js`. Các form `cContactForm`, `quote-form`, `lsContactForm`, `security-quote`, `launchInquiry` chưa thấy lệnh gọi trong mã nguồn đã quét |
| Link `mailto:` | ✅ Có ghi nhận conversion |

> 🔴 **Nếu các form còn lại chưa gọi conversion, số conversion đo được sẽ thấp hơn thực tế khoảng 50-80%.** Kiểm tra bằng Tag Assistant (gửi thử từng form) trước khi đánh giá KPI.

---

## 4. Lộ trình 90 ngày và ngưỡng quyết định

| Giai đoạn | Mục tiêu | Việc làm |
|---|---|---|
| **Tuần 0** (04-10/11) | Tracking sạch | Kiểm tra 7 form bằng Tag Assistant · xuất báo cáo 2 tháng (CPC, CTR, IS, search terms) · thêm negative từ search terms rác · kiểm tra **AI Max đang tắt** |
| **Tháng 1** (11/11-10/12) | Đo baseline | Không đổi giá thầu. Ghi nhận CPL thật đầu tiên |
| **Tháng 2** (11/12-10/01) | Chấp nhận sụt mùa vụ | Cuối tháng 12, B2B NL giảm mạnh (kỳ nghỉ). Dự kiến -30% lượt nhấp và lead trong 2 tuần cuối năm. Không kết luận dựa vào giai đoạn này |
| **Tháng 3** (11/01-10/02) | Quyết định | So CPL và tỉ lệ lead "đã có prototype" với ngưỡng bên dưới |

### Bảng KPI theo dõi hàng tuần

| KPI | Mục tiêu | Ngưỡng báo động | Hành động khi chạm ngưỡng |
|---|---|---|---|
| CPC trung bình | ≤ €8 | > €12 trong 2 tuần | Hạ giới hạn CPC, xem lại search terms |
| CTR | ≥ 5% | < 2% ở 1 ad group | Viết lại RSA, không tăng giá thầu |
| LP conversion | ≥ 4% (mục tiêu 5%) | < 2% sau 150 lượt nhấp | Sửa landing page trước khi chi thêm |
| CPL | ≤ €200 | > €400 sau 60 ngày | Dừng ad group có CPL cao nhất |
| Tỉ lệ lead có prototype | ≥ 30% | < 30% sau 8 tuần | Chuyển ngân sách sang kênh tạo nhu cầu (Hướng B) |
| Search lost IS (budget) | < 20% | > 40% **và** CPL tốt | Lúc đó mới tăng ngân sách |

### Điểm hoà vốn

Với CAC hoà vốn ≈ €800, kịch bản cơ sở (2,7 lead/tháng) cần **tỉ lệ chốt ≥ 25%**. Ở 15% thì lỗ khoảng €530/khách. Tăng tỉ lệ chốt (phản hồi trong 1 giờ, báo giá trong 24 giờ) có tác động lớn hơn tối ưu giá thầu.

---

## 5. Hiệu chỉnh bằng số thật của 2 tháng

Dự báo sẽ chính xác hơn nhiều khi thay giả định bằng số thật. Lấy trong Google Ads → Campaigns, chọn 60 ngày gần nhất:

| Điền số thật | Thay vào |
|---|---|
| Avg. CPC | Lượt nhấp/tháng = €547,56 ÷ CPC |
| CTR, Impressions | Kiểm tra trần lượt hiển thị |
| Search lost IS (budget) / (rank) | Biết ngân sách hay giá thầu đang là giới hạn |
| Số lead thật từ form và email (đếm thủ công trong 2 tháng) | LP conversion = lead ÷ lượt nhấp |

```
Lead/tháng  = (547,56 ÷ CPC thật) × LP conversion
CPL         = 547,56 ÷ Lead/tháng
CAC         = CPL ÷ Tỉ lệ chốt
```

> Lead đếm thủ công (email vào `wearehereforyou@launchstudio.eu`, form trong WordPress) là nguồn duy nhất để biết conversion thật của 2 tháng qua, vì Google Ads chưa ghi nhận được.
