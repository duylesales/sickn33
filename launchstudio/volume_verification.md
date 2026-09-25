# 📊 Volume search — vì sao chưa có, và cách lấy

> Trả lời cho câu hỏi: *"tại sao các keyword không có volume search?"*
> Liên quan: `keyword_seeds_3_ai_brands.csv` · `keyword_seeds_3_ai_brands_NL.csv`

---

## 1. Câu trả lời ngắn

**Vì mình không truy cập được Google Keyword Planner.** Keyword Planner yêu cầu đăng nhập tài khoản Google Ads thật — không có API công khai miễn phí nào trả về volume chính xác.

Cột cũ tên là `volume_signal` nhưng chứa `Tier A/B/C` (file EN trước đây còn ghi thẳng `Unverified-A/B/C`). Đó **không phải volume** — đó là mức độ bằng chứng mình quan sát được. Tên cột gây hiểu nhầm nên đã đổi thành **`evidence`**, và thêm 4 cột rỗng để điền số thật:

```
campaign,brand,ad_group,keyword,match_type,intent,priority,evidence,notes,volume,competition,cpc_low,cpc_high
                                                            ^^^^^^^^        ^^^^^^ ^^^^^^^^^^^ ^^^^^^^ ^^^^^^^^
                                                            bằng chứng      ← 4 cột chờ điền từ Keyword Planner
```

Mình cố tình **không bịa số**. Một con số volume sai còn tệ hơn ô trống, vì nó sẽ được dùng để chốt ngân sách.

---

## 2. `evidence` Tier A/B/C nghĩa là gì

| Tier | Định nghĩa | Ví dụ |
|---|---|---|
| **A** | Có bên khác **đang bán hoặc đang bid** đúng cụm này. Cạnh tranh tồn tại ⇒ volume tồn tại | `mvp laten maken` — 5+ bureau NL có landing page riêng |
| **B** | Có nội dung/thảo luận tồn tại, hoặc là biến thể trực tiếp của một cụm Tier A | `webapp laten bouwen` — biến thể của `app laten maken` |
| **C** | Suy luận từ cấu trúc ngôn ngữ và ngành, **chưa quan sát được bằng chứng** | `replit app live zetten` — đúng ngữ pháp NL, đúng intent, nhưng chưa thấy ai dùng |

Phân bố hiện tại:

| File | Tier A | Tier B | Tier C |
|---|---:|---:|---:|
| `keyword_seeds_3_ai_brands.csv` (85 EN) | 34 | 34 | 17 |
| `keyword_seeds_3_ai_brands_NL.csv` (72 NL) | 6 | 17 | 49 |

> ⚠️ **Bộ NL có 49/72 ở Tier C.** Đây là bộ rủi ro nhất trong toàn plan về mặt volume. Phần lớn là tiếng Hà Lan ghép với tên công cụ AI — hợp lý về logic nhưng chưa có gì chứng minh có người gõ. Verify bộ NL **trước** bộ EN.

---

## 3. Dữ liệu thật đã có trong repo — và vì sao không dùng được

File `keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv` có **123 keyword với volume thật**. Mình đã join với 157 keyword của plan:

| | Khớp chính xác | Khớp một phần |
|---|---:|---:|
| 85 keyword EN | **0** | 0 |
| 72 keyword NL | **0** | 1 (`ai prototype` — 20/tháng, bid $1,49–6,59) |

**Không dùng được, vì export đó được seed từ URL `launchstudio.eu/en/`**, nên Google trả về từ khoá mô tả *trang web hiện tại* (`day ai` 201.000, `user ai`, `ai coding`…), không phải từ khoá theo ý định thuê dịch vụ mà plan nhắm tới. Đây cũng là file có `day ai` chiếm 201.000/214.280 = **94% nhiễu** đã ghi ở `google_search_ads_master_plan.md`.

➡️ Phải chạy Keyword Planner lại, lần này seed bằng **danh sách keyword**, không phải URL.

---

## 4. Quy trình lấy số thật — khoảng 15 phút

Hai file đã tạo sẵn để dán thẳng, mỗi dòng một keyword:

| File | Số kw | Cài đặt trong Keyword Planner |
|---|---:|---|
| **`kp_upload_EN.txt`** | 85 | Location: Netherlands + các nước EU-EN · **Language: English** |
| **`kp_upload_NL.txt`** | 72 | Location: **Netherlands** · **Language: Dutch** |

**Các bước:**

1. Google Ads → Tools → **Keyword Planner** → **"Get search volume and forecasts"**
2. Dán nội dung `kp_upload_NL.txt` (làm bộ NL trước — rủi ro cao hơn)
3. Đặt **Location = Netherlands**, **Language = Dutch**. Hai thiết lập này độc lập, đừng bỏ qua Language
4. Xem tab **"Historical metrics"** → cột `Avg. monthly searches`, `Competition`, `Top of page bid (low/high)`
5. Download → điền vào 4 cột `volume`, `competition`, `cpc_low`, `cpc_high`
6. Lặp lại với `kp_upload_EN.txt`, Language = English

> 💡 **Chạy mỗi ngôn ngữ một lần riêng.** Nếu chọn cả English và Dutch trong một lần chạy, số trả về là tổng gộp và không cho biết bao nhiêu đến từ người tìm bằng tiếng Hà Lan — đúng thứ cần biết để chốt ngân sách nhánh N.

---

## 5. ⚠️ Cảnh báo: tài khoản mới sẽ thấy khoảng, không thấy số chính xác

Google giới hạn độ chi tiết của Keyword Planner theo mức chi tiêu của tài khoản:

| Tình trạng tài khoản | Kết quả nhận được |
|---|---|
| Chưa chi tiêu / chi rất ít | Khoảng rộng: `10–100`, `100–1K`, `1K–10K` |
| Đang chạy quảng cáo có chi tiêu | Số cụ thể: `170`, `2.400` |

Tài khoản LaunchStudio nếu chưa chạy sẽ rơi vào nhóm đầu. **Vẫn đủ dùng để quyết định**, vì thứ cần biết ở giai đoạn này là bậc độ lớn:

- `10–100` → giữ, ngân sách tối thiểu
- `100–1K` → nhóm chính, dồn ngân sách
- `1K–10K` trở lên ở nhóm này → **nghi ngờ nhiễu**, kiểm tra kỹ trước khi mừng

Muốn có số chính xác: chạy một campaign nhỏ vài ngày với ngân sách thấp, Keyword Planner sẽ mở khoá độ chi tiết.

---

## 6. Ba nguồn miễn phí để đối chiếu chéo

| Nguồn | Được gì | Hạn chế |
|---|---|---|
| **Bing Webmaster Tools** → Keyword Research | Số **chính xác**, miễn phí, không cần chi tiêu | Volume Bing ≈ 1/10–1/5 Google. Dùng để so sánh **tương quan** giữa các keyword, không dùng con số tuyệt đối |
| **Google Trends** | So sánh tương đối, tách được theo vùng NL | Không ra con số tuyệt đối. Keyword volume thấp sẽ hiện phẳng bằng 0 |
| **Google Search Console** | Truy vấn **thật** đang dẫn người vào launchstudio.eu | Chỉ thấy từ khoá site đã rank — không thấy nhu cầu chưa chạm tới |

> 💡 **Bing Webmaster Tools là cách nhanh nhất để kiểm chứng 49 keyword Tier C của bộ NL.** Nếu Bing báo 0 cho `replit app live zetten` thì gần như chắc chắn Google cũng gần 0 — nhưng như §7.3 của plan đã nói, keyword loại này vẫn nên giữ vì chi phí giữ chỗ gần bằng không.

---

## 7. Quyết định sau khi có số

| Kết quả | Hành động |
|---|---|
| Volume 0, không có biến thể nào có volume | **Xoá** khỏi bộ |
| Volume < 10/tháng nhưng intent tuyệt đối (`lovable app laten afmaken`) | **Giữ.** CPC sẽ ở mức sàn, chi phí giữ chỗ gần 0 |
| Volume cao nhưng intent lệch (`lovable`, `vibe coding`) | **Chuyển sang negative**, không dùng làm keyword dương |
| Volume cao + intent đúng + competition High | Giữ, nhưng tính lại CAC trước — xem công thức bên dưới |

**Hai công thức bắt buộc chạy lại sau khi có số thật:**

```
Trần chi tiêu/tháng = Volume × %kw hợp ads × Impression Share × CTR × CPC
CAC                 = CPC ÷ (tỉ lệ chuyển đổi trang đích × tỉ lệ chốt)
```

Nếu tổng trần chi tiêu tính ra thấp hơn ngân sách Tier B €850/tháng ở §10.1 của plan, **hạ ngân sách xuống bằng trần** — tiền vượt trần sẽ nằm không chứ không tiêu được. Đây là lý do `google_search_ads_master_plan.md` §2 kết luận tài khoản này bị chặn bởi **volume**, không phải bởi ngân sách.

---

*Cập nhật 25/09/2026 · 157 keyword chờ verify (85 EN + 72 NL) · 0 keyword có volume thật tính đến thời điểm này*
