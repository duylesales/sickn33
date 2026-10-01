# 📊 Dữ liệu từ khoá Google Search Ads đã được xác thực (Verified GKP Data)

> **Nguồn dữ liệu:** Trích xuất trực tiếp từ **Google Keyword Planner** (Tài khoản thực tế của bạn).  
> **Nguyên tắc:** 100% số liệu thực tế, **không có bất kỳ con số phỏng đoán hay suy diễn nào**.  
> **Tệp dữ liệu:** [`lovable_google_ads_keywords_en_nl.csv`](lovable_google_ads_keywords_en_nl.csv)

---

## 1. Bảng số liệu Tiếng Anh (English) — Hệ sinh thái Lovable

| Keyword | Volume thực tế (GKP) | Cạnh tranh | Match Type khuyên dùng | Mục đích tìm kiếm |
|---|:---:|:---:|:---:|---|
| **`lovable ai`** | **5.400** | Cao | `"Phrase"` / `[Exact]` | Head term toàn hệ thống (Cần phủ định `-free`, `-login`, `-jobs`, `-career`) |
| **`lovable dev`** | **1.300** | Vừa | `"Phrase"` / `[Exact]` | Brand term kỹ thuật (Đối tượng dev, builders) |
| **`lovable hosting`** | **30** | Thấp | `"Phrase"` | Nhu cầu tìm kiếm về Hosting cho Lovable |
| **`deploy lovable`** | **10** | Thấp | `"Phrase"` | Đưa app Lovable lên server/production |
| **`lovable custom domain`** | **10** | Thấp | `"Phrase"` | Cài đặt tên miền riêng |
| **`lovable stripe`** | **10** | Thấp | `"Phrase"` | Tích hợp Stripe cho Lovable |
| **`lovable payment`** | **10** | Thấp | `"Phrase"` | Cổng thanh toán cho Lovable |

*Lưu ý:* `host lovable` bị Google đánh dấu `—` (dưới 10 lượt/tháng), do đó từ khoá đúng để nhắm mục tiêu cho nhóm Host là **`lovable hosting`** (30 lượt).

---

## 2. Bảng số liệu Tiếng Hà Lan (Dutch) — Thanh toán & Dịch vụ phát triển

Đây là các từ khoá người dùng tại thị trường Hà Lan thực tế tìm kiếm, đã kèm theo mức đấu thầu giá nhấp chuột (Top of Page Bid):

### Nhóm Cổng thanh toán tại Hà Lan (Payments & iDEAL)
| Keyword | Volume thực tế | Cạnh tranh | Giá thầu thấp (EUR) | Giá thầu cao (EUR) | Bản chất nhu cầu |
|---|:---:|:---:|:---:|:---:|---|
| **`stripe ideal`** | **260** | Vừa | **1,85 €** | **11,92 €** | Khách hàng cần tích hợp cổng iDEAL thông qua Stripe |
| **`ideal integratie`** | **10** | Thấp | — | — | Tích hợp kỹ thuật cổng thanh toán iDEAL |
| **`ideal koppelen`** | **10** | Thấp | — | — | Kết nối cổng iDEAL vào trang web |
| **`mollie stripe`** | **10** | Thấp | — | — | So sánh / chuyển đổi giữa Mollie và Stripe |

### Nhóm Dịch vụ phát triển / Agency tại Hà Lan (Commercial High Value)
| Keyword | Volume thực tế | Cạnh tranh | Giá thầu thấp (EUR) | Giá thầu cao (EUR) | Bản chất nhu cầu |
|---|:---:|:---:|:---:|:---:|---|
| **`app laten maken`** | **480** | Vừa | **5,21 €** | **20,46 €** | Nhu cầu thuê làm app cao nhất tại Hà Lan |
| **`webapplicatie laten maken`** | **260** | Cao | **11,56 €** | **25,69 €** | Thuê làm web app, CPC cao, giá trị hợp đồng lớn |
| **`mvp laten maken`** | **50** | Vừa | — | — | Nhu cầu làm bản MVP cho startup (khớp nhất với Lovable) |
| **`software laten bouwen`** | **10** | Cao | **20,16 €** | **22,70 €** | Nhu cầu phát triển phần mềm theo yêu cầu |

---

## 3. Chiến lược áp dụng vào Google Ads

1. **Với các từ khoá volume nhỏ (10 – 30) như `lovable hosting`, `lovable stripe`:**
   * **Bắt buộc dùng `"Phrase Match"`**: Vì volume chính xác thấp, cài Phrase Match sẽ giúp tài khoản bắt được toàn bộ các biến thể mà người dùng gõ thêm (như *how to set up lovable hosting*, *lovable stripe webhook error*).
2. **Với các từ khoá volume lớn (5.400, 1.300) như `lovable ai`, `lovable dev`:**
   * Nếu chạy nhắm vào khách cần làm app: Cần tạo Ad Copy rõ ràng về dịch vụ (*"Need Help with Your Lovable App? / Turn Your Lovable Prototype into Production"*), tránh quảng cáo mơ hồ khiến người dùng muốn tìm trang chủ Lovable bấm nhầm gây tốn ngân sách.
3. **Với nhóm Hà Lan (`app laten maken`, `stripe ideal`):**
   * Đây là nhóm từ tạo ra khách hàng thật có ngân sách trả tiền cao (CPC lên tới 11€ – 25€). Khách hàng tìm `app laten maken` hay `mvp laten maken` có thể được chốt bằng giải pháp xây dựng nhanh trên Lovable với chi phí tối ưu hơn so với agency code truyền thống.
