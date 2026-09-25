# 🔴 Phân tích volume thật — kết quả và hệ quả

> Dữ liệu: Keyword Planner, 157 keyword (85 EN + 72 NL) · cập nhật 25/09/2026
> Nguồn: `kp_upload_EN.txt` · `kp_upload_NL.txt` → đã nạp vào cột `volume` của hai file CSV
> Tài liệu bị ảnh hưởng: `google_search_ads_plan_3_ai_brands.md`

---

## 1. Kết luận trước, chi tiết sau

**Luận điểm cốt lõi của dịch vụ — "làm nốt prototype AI dang dở" — gần như không có ai tìm kiếm.**

27 keyword diễn đạt đúng luận điểm này (`afmaken`, `to production`, `naar productie`, `production ready`, `live zetten`, `finish`, `preview vs production`) có **tổng cộng 10 lượt tìm/tháng**. 26/27 từ bằng 0. Từ duy nhất khác 0 là `replit agent stuck` = 10.

| | Keyword | Volume/tháng |
|---|---:|---:|
| Luận điểm "làm nốt prototype AI" | 27 | **10** |
| Nhu cầu chung "xây app mới" | 12 | **1.170** |

Người ta không tìm cách làm nốt thứ đang dở. Họ tìm người xây cái mới.

Đây không phải lỗi từ khoá — mình đã viết cùng một ý bằng 6 cách khác nhau, hai thứ tiếng, cả tên thương hiệu lẫn không tên. Tất cả đều 0. **Đây là kết luận về thị trường, không phải về danh sách từ khoá.**

---

## 2. Toàn cảnh số liệu

| | Keyword | Volume/tháng | Kw = 0 |
|---|---:|---:|---:|
| Nhánh EN (B1–B3) | 85 | 530 | 52 (61%) |
| Nhánh NL (N1–N4) | 72 | 1.340 | 54 (75%) |
| **Tổng** | **157** | **1.870** | **106 (68%)** |

**68% số keyword có volume bằng 0.** Trong Keyword Planner, 0 nghĩa là dưới 10 lượt/tháng.

### Top 10 keyword có volume

| Volume | Keyword | Campaign |
|---:|---|---|
| **480** | `app laten maken` | N1-NL-Service |
| **260** | `webapplicatie laten maken` | N1-NL-Service |
| **210** | `replit agency` | B3-Replit ⚠️ nghi ngờ |
| **140** | `app laten bouwen` | N1-NL-Service |
| **110** | `software laten maken` | N1-NL-Service |
| **90** | `maatwerk software laten maken` | N1-NL-Service |
| **50** | `mvp laten maken` | N1-NL-Service |
| **40** | `technische due diligence` | N3-NL-Security |
| **30** | `mvp ontwikkeling` | N1-NL-Service |
| **20** | `developer inhuren app` | N1-NL-Service |

Chín trong mười từ thuộc **một campaign duy nhất**: N1-NL-Service. Và tất cả đều là nhu cầu "xây app mới", không phải "làm nốt app cũ".

---

## 3. Ngân sách trong plan đang ngược

Trần chi tiêu tính theo `Volume × 1,8 (phrase match mở rộng) × 60% IS × 5% CTR × CPC`:

| Campaign | Kw | Volume | Kw=0 | Plan cấp | Trần chi thật | Chênh |
|---|---:|---:|---:|---:|---:|---:|
| B1-Lovable | 32 | 110 | 21 | 250€ | **30€** | −220€ |
| B2-Bolt | 24 | 120 | 12 | 120€ | **32€** | −88€ |
| B3-Replit | 29 | 300 | 19 | 180€ | **81€** | −99€ |
| N1-NL-Service | 26 | 1.280 | 11 | 150€ | **691€** | **+541€** |
| N2-NL-AI-Tools | 24 | 10 | 23 | 60€ | **5€** | −55€ |
| N3-NL-Security | 12 | 50 | 10 | 60€ | **27€** | −33€ |
| N4-NL-Payments | 10 | 0 | 10 | 30€ | **0€** | −30€ |

| Nhánh | Plan cấp | Trần chi thật |
|---|---:|---:|
| EN (B1–B3) | 550€ | **143€** |
| NL (N1–N4) | 300€ | **724€** |

**Plan đang cấp 550€ cho nhánh chỉ tiêu được 143€, và 300€ cho nhánh tiêu được 724€.** Ngược hoàn toàn.

### Bốn ad group không có volume nào

| Campaign | Ad group | Kw | Volume |
|---|---|---:|---:|
| N2-NL-AI-Tools | `AG-NL-AI-Afmaken` | 8 | 0 |
| N2-NL-AI-Tools | `AG-NL-Lovable` | 6 | 0 |
| N2-NL-AI-Tools | `AG-NL-Replit` | 6 | 0 |
| N4-NL-Payments | `AG-NL-Payments` | 10 | 0 |

> 🔴 **Nhận định ở §7.3 của plan là sai.** Mình viết *"N2-NL-AI-Tools là tài sản rẻ nhất trong toàn tài khoản — sở hữu trọn nhóm với €60/tháng"*. Thực tế cả campaign có 10 lượt tìm/tháng. Không phải tài sản rẻ — là không có gì để sở hữu.

---

## 4. Phương pháp `evidence` của mình: đúng ở NL, sai hẳn ở EN

| File | Tier | Kw | Tổng volume | Tỉ lệ có volume > 0 | Max |
|---|---|---:|---:|---:|---:|
| **EN** | A | 34 | 120 | 35% | 10 |
| | B | 34 | 140 | 41% | 10 |
| | C | 17 | **270** | 41% | **210** |
| **NL** | A | 6 | **810** | **83%** | **480** |
| | B | 17 | 470 | 52% | 260 |
| | C | 49 | 60 | **8%** | 20 |

**Bộ NL: thang Tier dự đoán chính xác.** A 83% → B 52% → C 8%, đơn điệu giảm, tổng volume giảm theo đúng thứ tự.

**Bộ EN: thang Tier vô giá trị.** Tier A (mức tin cậy cao nhất của mình) có tỉ lệ trúng *thấp hơn* Tier C, và từ có volume cao nhất toàn bộ nhánh EN lại nằm ở Tier C.

Lý do khác biệt nằm ở loại tín hiệu mình dùng:

| Bộ | Tín hiệu dùng để xếp Tier | Bản chất | Kết quả |
|---|---|---|---|
| NL | "Có bureau nào làm landing page / chạy ads cho cụm này không?" | Tín hiệu **cầu** — có người trả tiền để xuất hiện | ✅ Dự đoán tốt |
| EN | "Có gig Fiverr / bài thảo luận / nội dung về cụm này không?" | Tín hiệu **cung** — có người tạo nội dung | ❌ Không liên quan volume |

Nội dung tồn tại không chứng minh có người tìm. Cạnh tranh trả tiền thì có. Lần sau chỉ dùng tín hiệu cầu.

---

## 5. Kinh tế của campaign duy nhất còn sống

N1-NL-Service: 1.280 volume → ~69 click/tháng.

| CPC | Chi/tháng | Kịch bản | Khách/tháng | CAC |
|---:|---:|---|---:|---:|
| €8 | 553€ | ICP khớp (LP 5% · chốt 25%) | 0,86 | **640€** |
| €8 | 553€ | ICP lệch (LP 5% · chốt 10%) | 0,35 | **1.600€** |
| €10 | 691€ | ICP khớp | 0,86 | **800€** |
| €10 | 691€ | ICP lệch | 0,35 | **2.000€** |
| €14 | 968€ | ICP lệch | 0,35 | **2.800€** |

Đối chiếu gói dịch vụ: **Launch Ready €800–3.500** · **Launch & Grow €2.500–7.500**.

> ⚠️ **Kịch bản "ICP lệch" mới là kịch bản mặc định, không phải ngoại lệ.** 1.080/1.280 volume của N1 đến từ `app laten maken`, `webapplicatie laten maken`, `app laten bouwen`, `software laten maken` — toàn bộ là người muốn **xây mới**. Tỉ lệ chốt 25% chỉ đúng nếu người tìm đã có prototype dang dở. Họ không có.
>
> Ở CAC €1.600–2.000, gói €800 lỗ nặng. Chỉ gói Launch & Grow €2.500–7.500 mới chịu được, mà đó là gói khó bán cho khách đến từ truy vấn chung.

---

## 6. Đề xuất

### 6.1. Việc phải làm ngay

| # | Việc | Lý do |
|---|---|---|
| 1 | **Tắt N4-NL-Payments** | 0 volume trên toàn bộ 10 keyword |
| 2 | **Tắt N2-NL-AI-Tools** như campaign riêng | 10 volume. Gộp 24 keyword vào một ad group dự phòng trong campaign khác, ngân sách 0 riêng |
| 3 | **Gộp B1 + B2 + B3 thành một campaign** `LS-EN-AI-Tools`, ngân sách **€100–140** | 530 volume không nuôi nổi 3 campaign. Ba ngân sách riêng chỉ tạo ba lần chi phí quản lý |
| 4 | **Nâng N1-NL-Service lên €400–550** | Campaign duy nhất có volume thật, đang bị cấp thiếu 541€ |
| 5 | **Giữ N3-NL-Security ở €40** | `technische due diligence` 40/tháng là truy vấn giá trị cao, đáng giữ dù nhỏ |
| 6 | **Kiểm tra `replit agency` = 210** | Bất thường. Truy vấn này nghĩa là gì chưa rõ — có thể người tìm chương trình agency của chính Replit. Chạy Exact match riêng, đọc Search Terms 1 tuần trước khi tin |

**Ngân sách mới: ~€600–730/tháng** thay vì €850, và phân bổ ngược lại so với plan hiện tại.

### 6.2. Quyết định lớn hơn — cần bạn chọn

Vấn đề không nằm ở cấu hình campaign. Nó nằm ở chỗ **Google Search Ads chỉ bắt được nhu cầu đã tồn tại**, mà nhu cầu "làm nốt prototype AI" thì chưa tồn tại ở mức đo được — cả tiếng Anh lẫn tiếng Hà Lan.

Hai hướng:

**Hướng A — Đi theo volume.** Chạy N1-NL-Service vào thị trường "xây app mới", cạnh tranh với bureau full-service. Landing page phải chuyển hoá được người đến với ý định "xây mới" thành "à, tôi có prototype rồi". Có volume, nhưng CAC €1.600–2.000 và phải thắng ở khâu thông điệp.

**Hướng B — Không dùng Search Ads cho luận điểm này.** Nhu cầu chưa tồn tại thì phải **tạo ra**, không mua được: nội dung/SEO, LinkedIn, cộng đồng nơi người dùng Lovable/Bolt/Replit tụ tập (Discord, r/vibecoding), hợp tác. Giữ Search Ads ở mức tối thiểu €100–150/tháng để hứng vài truy vấn thật hiếm hoi.

**Đề xuất của mình: B là chính, A là phép thử có kiểm soát.** Chạy N1 ở €400 trong 8 tuần với chỉ số quyết định duy nhất là **tỉ lệ lead đã có prototype sẵn**. Dưới 30% thì dừng A, dồn toàn bộ vào B.

> 💡 Tin tốt duy nhất trong bộ dữ liệu: **nhu cầu tiếng Hà Lan có thật và gấp 2,5 lần nhánh tiếng Anh** (1.340 vs 530). Quyết định làm bộ keyword tiếng Hà Lan là đúng. Chỉ có điều nhu cầu đó nằm ở chỗ khác với chỗ plan đang nhắm.

---

## 7. Cảnh báo khi đọc số này

- **0 nghĩa là < 10/tháng**, không phải đúng bằng 0. Một từ 0 vẫn có thể có 3–8 lượt/tháng.
- **Volume là của cụm chính xác.** Phrase match bắt được nhiều hơn — hệ số 1,8× dùng ở §3 là ước lượng, chưa verify.
- **Số đã làm tròn theo bậc của Google** (10, 20, 30, 50, 90, 110, 140, 210, 260, 480). Đây là dữ liệu thật chứ không phải khoảng, nhưng độ chính xác chỉ tới bậc.
- **CPC vẫn chưa có.** Toàn bộ tính toán ở §5 dùng CPC ước lượng €8–14 từ nghiên cứu trước. Cần chạy lại Keyword Planner lấy cột `Top of page bid` để chốt.

---

*157 keyword · 1.870 volume/tháng · 106 keyword bằng 0 · 4/18 ad group chết · Luận điểm cốt lõi: 10 lượt tìm/tháng*
