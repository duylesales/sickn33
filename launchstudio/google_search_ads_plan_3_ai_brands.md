# 🎯 Google Search Ads — Plan 3 Thương Hiệu AI
## Lovable · Bolt · Replit → launchstudio.eu

> **Phạm vi:** Chỉ Google Search, chỉ 3 tên thương hiệu công cụ AI. Đây là **kế hoạch nhắm thương hiệu bên thứ ba** — luật chơi khác với keyword thông thường.
> **Ngày:** 2026-09-25 · **Thị trường:** EU-EN (chính) + NL/BE (phụ — xem §2.2)
> **Keyword:** 157 từ — 85 tiếng Anh (8 ad group) + 72 tiếng Hà Lan (10 ad group). Liệt kê đầy đủ kèm volume đo được tại §2.3, §5.1, §6.2, §7.2 và §8.2.
> **Tài liệu này tự chứa.** Mọi số liệu, danh sách negative và lập luận cần thiết đều nằm trong đây, không cần mở file khác.

---

> # 🔴 CẢNH BÁO — PLAN NÀY ĐÃ CÓ DỮ LIỆU VOLUME THẬT (25/09/2026)
>
> Keyword Planner đã chạy cho cả 157 keyword. Kết quả **phủ định phần lớn giả định của plan này**:
>
> - **Luận điểm cốt lõi "làm nốt prototype AI" có 10 lượt tìm/tháng** trên tổng 27 keyword — 26/27 bằng 0
> - **106/157 keyword (68%) có volume bằng 0**; 4/18 ad group chết hoàn toàn
> - **Ngân sách đang phân bổ ngược**: nhánh EN được cấp 550€ nhưng chỉ tiêu được 143€; nhánh NL được cấp 300€ nhưng tiêu được 724€
> - Nhận định ở §8.3 rằng `N2-NL-AI-Tools` là "tài sản rẻ nhất" **là sai** — campaign đó có 10 volume
>
> **Đọc §2 trước khi dùng bất kỳ con số ngân sách nào trong tài liệu này.**
> Cấu trúc campaign, negative list, RSA và quy tắc thương hiệu ở đây vẫn dùng được. Ngân sách và thứ tự ưu tiên thì không.

---

## 📑 Mục lục

| § | Nội dung |
|---|---|
| [1](#1) | Đọc trước: 4 rủi ro đặc thù của plan này |
| [2](#2) | **Dữ liệu volume thật — và hệ quả** |
| [3](#3) | Rủi ro nhãn hiệu & rủi ro trùng tên |
| [4](#4) | Kiến trúc: 7 campaign riêng, không gộp |
| [5](#5) | B1 · Lovable |
| [6](#6) | B2 · Bolt — campaign nguy hiểm nhất |
| [7](#7) | B3 · Replit — campaign sạch nhất |
| [8](#8) | **N1–N4 · Bốn campaign tiếng Hà Lan** |
| [9](#9) | Negative keywords theo từng thương hiệu |
| [10](#10) | Landing page |
| [11](#11) | Ngân sách & lộ trình |
| [12](#12) | KPI & ngưỡng dừng |
| [13](#13) | Checklist trước khi bật |

---

<a id="1"></a>
## 1. Đọc trước: 4 rủi ro đặc thù của plan này

Plan này khác mọi plan trước vì **toàn bộ keyword đều là tên thương hiệu của công ty khác**. Ba điều phải xử lý trước khi nghĩ tới ngân sách.

### ⚠️ Rủi ro 1 — "Bolt" ở Hà Lan là hãng taxi, không phải công cụ code

**Bolt là thương hiệu gọi xe lớn thứ hai ở Hà Lan**, hoạt động tại Amsterdam, Rotterdam, Den Haag và Utrecht. Người Hà Lan gõ "bolt" gần như chắc chắn đang tìm ứng dụng taxi.

Thêm vào đó `bolt` còn là: bu lông/ốc vít · Usain Bolt · tia chớp · Bolt Threads (vật liệu sinh học) · xe scooter điện Bolt.

➡️ **Hệ quả:** `bolt ai` = 1.300 lượt/tháng (Keyword Planner, 15/06/2026) từng là con số volume cao nhất xác minh được trong toàn bộ nghiên cứu — nhưng phải giả định nó bị nhiễm nặng bởi truy vấn taxi. Lần đo mới nhất (§2) cho thấy toàn bộ campaign B2-Bolt chỉ còn **120 lượt/tháng** khi dùng keyword có kèm `new` — tức là **~90% volume của "bolt" là nhiễu**, đúng như nghi ngờ ban đầu.

### ⚠️ Rủi ro 2 — Dùng tên thương hiệu trong nội dung quảng cáo bị hạn chế

Theo chính sách nhãn hiệu của Google Ads:

| | Được phép? |
|---|---|
| Dùng nhãn hiệu làm **keyword** | ✅ Google **không** hạn chế |
| Dùng nhãn hiệu trong **ad text** | ⚠️ Bị hạn chế nếu là **đối thủ trực tiếp**, hoặc nếu gây **nhầm lẫn/hiểu sai** |
| Dùng nhãn hiệu trong **display URL** (tên miền cấp 2) | ✅ Không bị hạn chế |

**Vị thế của LaunchStudio thuận lợi hơn trường hợp thông thường:** LaunchStudio **không phải đối thủ** của Lovable/Bolt/Replit — mà là dịch vụ bổ trợ, giúp người dùng của chính các công cụ đó đưa app lên production. Đây là vị thế an toàn hơn nhiều so với bid vào tên đối thủ.

Nhưng điều kiện "gây nhầm lẫn" vẫn áp dụng. Quảng cáo **không được ngụ ý là đối tác chính thức**. Xem §3.1 để biết cách xử lý.

### ⚠️ Rủi ro 3 — Mật độ keyword giữa 3 thương hiệu rất lệch

Kiểm kho keyword hiện có trong repo:

| Thương hiệu | Keyword đã có | Hợp ads |
|---|---:|---:|
| Lovable | 123 | 31 |
| Bolt | 7 | 2 |
| Replit | 7 | 2 |

➡️ Bolt và Replit gần như chưa được khai thác. Plan này bổ sung lên **85 keyword** chia đều hơn (Lovable 32 · Bolt 24 · Replit 29), nhưng **chênh lệch volume thật giữa ba thương hiệu vẫn chưa đo được** — đã đo, xem §2.

### ⚠️ Rủi ro 4 — Ngôn ngữ keyword phải khớp ngôn ngữ quảng cáo

Bản đầu của plan này mắc lỗi: keyword tiếng Anh nhưng quảng cáo song ngữ Anh/Hà Lan. **Quảng cáo tiếng Hà Lan gắn vào keyword tiếng Anh gần như không bao giờ được phục vụ**, và người Hà Lan gõ tiếng Hà Lan thì không khớp keyword tiếng Anh nào. Nửa tiền đổ vào phần không bao giờ chạy.

Đã sửa bằng cách tách làm hai nhóm campaign:

| Nhóm | Keyword | Quảng cáo | Ngôn ngữ campaign | Geo |
|---|---|---|---|---|
| **B1–B3** (§5–§7) | Tiếng Anh, 85 kw | **Chỉ tiếng Anh** | English | EU-EN + NL (người NL vẫn gõ lỗi kỹ thuật bằng tiếng Anh) |
| **N1–N4** (§8) | Tiếng Hà Lan, 72 kw | **Chỉ tiếng Hà Lan** | Dutch | Netherlands |

Bộ Hà Lan **không phải bản dịch** của bộ tiếng Anh — phân bố ý định khác hẳn. Lý do đầy đủ ở §8.1.

---

<a id="2"></a>
## 2. Dữ liệu volume thật — và hệ quả của nó

> Keyword Planner đã chạy cho cả 157 keyword (25/09/2026). Toàn bộ số trong mục này là số đo, không phải ước tính.

### 2.1. Kết luận trước, chi tiết sau

**Luận điểm cốt lõi của dịch vụ — "làm nốt prototype AI dang dở" — gần như không có ai tìm kiếm.**

27 keyword diễn đạt đúng luận điểm này (`afmaken`, `to production`, `naar productie`, `production ready`, `live zetten`, `finish`, `preview vs production`) có **tổng cộng 10 lượt tìm/tháng**. 26/27 bằng 0. Từ duy nhất khác 0 là `replit agent stuck` = 10.

```
take my lovable app to production = 0      app laten afmaken             = 0
lovable app production ready      = 0      prototype laten afmaken       = 0
finish my lovable app             = 0      onafgemaakte app afmaken      = 0
lovable preview vs production     = 0      ai app laten afmaken          = 0
bolt new to production            = 0      ai gebouwde app laten afmaken = 0
bolt new app production ready     = 0      ai prototype naar productie   = 0
bolt new preview vs production    = 0      van prototype naar productie  = 0
replit app to production          = 0      app productieklaar maken      = 0
replit production ready           = 0      prototype niet live krijgen   = 0
lovable app laten afmaken         = 0      no code app laten afmaken     = 0
lovable app live zetten           = 0      bolt new app laten afmaken    = 0
replit app laten afmaken          = 0      bolt new app live zetten      = 0
replit app live zetten            = 0      app afmaken freelancer        = 0
```

| | Keyword | Volume/tháng |
|---|---:|---:|
| Luận điểm "làm nốt prototype AI" | 27 | **10** |
| Nhu cầu chung "xây app mới" | 12 | **1.170** |

Người ta không tìm cách làm nốt thứ đang dở. Họ tìm người xây cái mới.

Cùng một ý đã được viết bằng 6 cách khác nhau, hai thứ tiếng, cả có lẫn không có tên thương hiệu. Tất cả đều 0. **Đây là kết luận về thị trường, không phải về danh sách từ khoá.**

### 2.2. Toàn cảnh số liệu

| | Keyword | Volume/tháng | Kw = 0 |
|---|---:|---:|---:|
| Nhánh EN (B1–B3) | 85 | 530 | 52 (61%) |
| Nhánh NL (N1–N4) | 72 | 1.340 | 54 (75%) |
| **Tổng** | **157** | **1.870** | **106 (68%)** |

**68% số keyword có volume bằng 0.** Trong Keyword Planner, 0 nghĩa là dưới 10 lượt/tháng.

### 2.3. Toàn bộ keyword có volume > 0

| Volume | Keyword | Campaign |
|---:|---|---|
| **480** | `app laten maken` | N1-NL-Service |
| **260** | `webapplicatie laten maken` | N1-NL-Service |
| **210** | `replit agency` | B3-Replit |
| **140** | `app laten bouwen` | N1-NL-Service |
| **110** | `software laten maken` | N1-NL-Service |
| **90** | `maatwerk software laten maken` | N1-NL-Service |
| **50** | `mvp laten maken` | N1-NL-Service |
| **40** | `technische due diligence` | N3-NL-Security |
| **30** | `mvp ontwikkeling` | N1-NL-Service |
| **20** | `developer inhuren app` | N1-NL-Service |
| **20** | `app laten maken rotterdam` | N1-NL-Service |
| **20** | `app laten maken eindhoven` | N1-NL-Service |
| **20** | `app laten maken amsterdam` | N1-NL-Service |
| **10** | `webapp laten bouwen` | N1-NL-Service |
| **10** | `web applicatie laten bouwen` | N1-NL-Service |
| **10** | `self host lovable app` | B1-Lovable |
| **10** | `replit security` | B3-Replit |
| **10** | `replit not working` | B3-Replit |
| **10** | `replit hosting cost` | B3-Replit |
| **10** | `replit export code` | B3-Replit |
| **10** | `replit deployment cost` | B3-Replit |
| **10** | `replit custom domain` | B3-Replit |
| **10** | `replit agent stuck` | B3-Replit |
| **10** | `replit agent not working` | B3-Replit |
| **10** | `pentest webapplicatie` | N3-NL-Security |
| **10** | `mvp laten ontwikkelen` | N1-NL-Service |
| **10** | `lovable to nextjs` | B1-Lovable |
| **10** | `lovable stripe integration` | B1-Lovable |
| **10** | `lovable not working` | B1-Lovable |
| **10** | `lovable freelancer` | B1-Lovable |
| **10** | `lovable export code` | B1-Lovable |
| **10** | `lovable developer` | B1-Lovable |
| **10** | `lovable custom domain not working` | B1-Lovable |
| **10** | `lovable alternative` | B1-Lovable |
| **10** | `is lovable secure` | B1-Lovable |
| **10** | `hire replit developer` | B3-Replit |
| **10** | `hire lovable developer` | B1-Lovable |
| **10** | `bolt new token limit` | B2-Bolt |
| **10** | `bolt new supabase` | B2-Bolt |
| **10** | `bolt new stripe` | B2-Bolt |
| **10** | `bolt new security` | B2-Bolt |
| **10** | `bolt new not working` | B2-Bolt |
| **10** | `bolt new export code` | B2-Bolt |
| **10** | `bolt new environment variables` | B2-Bolt |
| **10** | `bolt new developer` | N2-NL-AI-Tools |
| **10** | `bolt new developer` | B2-Bolt |
| **10** | `bolt new deployment` | B2-Bolt |
| **10** | `bolt new custom domain` | B2-Bolt |
| **10** | `bolt new blank page` | B2-Bolt |
| **10** | `bolt app developer` | B2-Bolt |
| **10** | `app laten maken utrecht` | N1-NL-Service |

Chín trong mười từ có volume cao nhất thuộc **một campaign duy nhất**: N1-NL-Service. Và tất cả đều là nhu cầu "xây app mới", không phải "làm nốt app cũ".

> ⚠️ **`replit agency` = 210 là con số bất thường.** Truy vấn này nghĩa là gì chưa rõ — có thể người tìm chương trình agency của chính Replit chứ không phải tìm dịch vụ sửa app. Chạy Exact match riêng và đọc Search Terms 1 tuần trước khi tin con số này.

### 2.4. Ngân sách trong plan đang ngược

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

### 2.5. Bốn ad group không có volume nào

| Campaign | Ad group | Kw | Volume |
|---|---|---:|---:|
| N2-NL-AI-Tools | `AG-NL-AI-Afmaken` | 8 | 0 |
| N2-NL-AI-Tools | `AG-NL-Lovable` | 6 | 0 |
| N2-NL-AI-Tools | `AG-NL-Replit` | 6 | 0 |
| N4-NL-Payments | `AG-NL-Payments` | 10 | 0 |

### 2.6. Phương pháp `evidence` Tier A/B/C: đúng ở NL, sai hẳn ở EN

| File | Tier | Kw | Tổng volume | Tỉ lệ có volume > 0 | Max |
|---|---|---:|---:|---:|---:|
| **EN** | A | 34 | 120 | 35% | 10 |
| **EN** | B | 34 | 140 | 41% | 10 |
| **EN** | C | 17 | 270 | 41% | 210 |
| **NL** | A | 6 | 810 | 83% | 480 |
| **NL** | B | 17 | 470 | 52% | 260 |
| **NL** | C | 49 | 60 | 8% | 20 |

**Bộ NL: thang Tier dự đoán chính xác** — A 83% → B 52% → C 8%, đơn điệu giảm.
**Bộ EN: thang Tier vô giá trị** — Tier A (mức tin cậy cao nhất) trúng *thấp hơn* Tier C, và từ có volume cao nhất toàn nhánh EN lại nằm ở Tier C.

Lý do nằm ở loại tín hiệu được dùng để xếp Tier:

| Bộ | Tín hiệu dùng | Bản chất | Kết quả |
|---|---|---|---|
| NL | "Có bureau nào làm landing page / chạy ads cho cụm này không?" | Tín hiệu **cầu** — có người trả tiền để xuất hiện | ✅ Dự đoán tốt |
| EN | "Có gig Fiverr / bài thảo luận / nội dung về cụm này không?" | Tín hiệu **cung** — có người tạo nội dung | ❌ Không liên quan volume |

Nội dung tồn tại không chứng minh có người tìm. Cạnh tranh trả tiền thì có. Từ nay chỉ dùng tín hiệu cầu.

### 2.7. Kinh tế của campaign duy nhất còn sống

N1-NL-Service: 1.280 volume → ~69 click/tháng.

| CPC | Chi/tháng | Kịch bản | Khách/tháng | CAC |
|---:|---:|---|---:|---:|
| €8 | 553€ | ICP khớp (LP 5% · chốt 25%) | 0,86 | **640€** |
| €8 | 553€ | ICP lệch (LP 5% · chốt 10%) | 0,35 | **1.600€** |
| €10 | 691€ | ICP khớp | 0,86 | **800€** |
| €10 | 691€ | ICP lệch | 0,35 | **2.000€** |
| €14 | 968€ | ICP lệch | 0,35 | **2.800€** |

Đối chiếu gói dịch vụ: **Launch Ready €800–3.500** · **Launch & Grow €2.500–7.500**.

> ⚠️ **Kịch bản "ICP lệch" mới là mặc định, không phải ngoại lệ.** 1.080/1.280 volume của N1 đến từ `app laten maken`, `webapplicatie laten maken`, `app laten bouwen`, `software laten maken` — toàn bộ là người muốn **xây mới**. Tỉ lệ chốt 25% chỉ đúng nếu người tìm đã có prototype dang dở. Họ không có.
>
> Ở CAC €1.600–2.000, gói €800 lỗ nặng. Chỉ gói Launch & Grow €2.500–7.500 mới chịu được, mà đó là gói khó bán cho khách đến từ truy vấn chung.

### 2.8. Đề xuất

| # | Việc | Lý do |
|---|---|---|
| 1 | **Tắt N4-NL-Payments** | 0 volume trên toàn bộ 10 keyword |
| 2 | **Tắt N2-NL-AI-Tools** như campaign riêng | 10 volume. Gộp 24 keyword vào một ad group dự phòng, ngân sách 0 riêng |
| 3 | **Gộp B1 + B2 + B3 thành một campaign** `LS-EN-AI-Tools`, ngân sách **€100–140** | 530 volume không nuôi nổi 3 campaign. Ba ngân sách riêng chỉ tạo ba lần chi phí quản lý |
| 4 | **Nâng N1-NL-Service lên €400–550** | Campaign duy nhất có volume thật, đang bị cấp thiếu 541€ |
| 5 | **Giữ N3-NL-Security ở €40** | `technische due diligence` 40/tháng là truy vấn giá trị cao, đáng giữ dù nhỏ |
| 6 | **Kiểm tra `replit agency` = 210** | Bất thường — xem cảnh báo ở §2.3 |

**Ngân sách mới: ~€540–730/tháng** thay vì €850, phân bổ ngược lại so với plan gốc.

#### Quyết định lớn hơn — cần chọn

Vấn đề không nằm ở cấu hình campaign. Nó nằm ở chỗ **Google Search Ads chỉ bắt được nhu cầu đã tồn tại**, mà nhu cầu "làm nốt prototype AI" thì chưa tồn tại ở mức đo được — cả tiếng Anh lẫn tiếng Hà Lan.

**Hướng A — Đi theo volume.** Chạy N1-NL-Service vào thị trường "xây app mới", cạnh tranh với bureau full-service. Landing page phải chuyển hoá người đến với ý định "xây mới" thành "à, tôi có prototype rồi". Có volume, nhưng CAC €1.600–2.000 và phải thắng ở khâu thông điệp.

**Hướng B — Không dùng Search Ads cho luận điểm này.** Nhu cầu chưa tồn tại thì phải **tạo ra**, không mua được: nội dung/SEO, LinkedIn, cộng đồng nơi người dùng Lovable/Bolt/Replit tụ tập (Discord, r/vibecoding), hợp tác. Giữ Search Ads ở mức tối thiểu €100–150/tháng để hứng vài truy vấn thật hiếm hoi.

**Đề xuất: B là chính, A là phép thử có kiểm soát.** Chạy N1 ở €400 trong 8 tuần với chỉ số quyết định duy nhất là **tỉ lệ lead đã có prototype sẵn**. Dưới 30% thì dừng A, dồn toàn bộ vào B.

> 💡 Tin tốt duy nhất trong bộ dữ liệu: **nhu cầu tiếng Hà Lan có thật và gấp 2,5 lần nhánh tiếng Anh** (1.340 vs 530). Quyết định làm bộ keyword tiếng Hà Lan là đúng. Chỉ có điều nhu cầu đó nằm ở chỗ khác với chỗ plan đang nhắm.

### 2.9. Cảnh báo khi đọc những con số này

- **0 nghĩa là < 10/tháng**, không phải đúng bằng 0. Một từ 0 vẫn có thể có 3–8 lượt/tháng.
- **Volume là của cụm chính xác.** Phrase match bắt được nhiều hơn — hệ số 1,8× dùng ở §2.4 là ước lượng, chưa verify.
- **Số đã làm tròn theo bậc của Google** (10, 20, 30, 50, 90, 110, 140, 210, 260, 480). Đây là dữ liệu thật chứ không phải khoảng, nhưng độ chính xác chỉ tới bậc.
- **CPC vẫn chưa có.** Toàn bộ tính toán ở §2.7 dùng CPC ước lượng €8–14. Cần chạy lại Keyword Planner lấy cột `Top of page bid` để chốt.
- **Tài khoản chưa chi tiêu chỉ thấy khoảng** (`10–100`, `100–1K`) chứ không thấy số chính xác. Muốn số chính xác thì chạy một campaign nhỏ vài ngày, Keyword Planner sẽ mở khoá độ chi tiết.

---

<a id="3"></a>
## 3. Rủi ro nhãn hiệu & rủi ro trùng tên

### 3.1. Ba tầng phòng vệ cho nội dung quảng cáo

Vì toàn bộ plan dựa trên tên thương hiệu bên thứ ba, mỗi ad group cần **hai bộ RSA sẵn sàng**:

| Bộ | Nội dung | Khi nào dùng |
|---|---|---|
| **A — có tên brand** | Headline chứa `Lovable` / `Bolt.new` / `Replit` | Mặc định. CTR cao hơn rõ rệt vì khớp truy vấn |
| **B — không tên brand** | Thay bằng `AI App`, `AI-Built App`, `AI Builder` | Kích hoạt **ngay** nếu Google hạn chế ad text sau khiếu nại |

**Ba nguyên tắc bắt buộc trong mọi ad text:**

1. **Không ngụ ý quan hệ chính thức.** Không dùng `official`, `partner`, `certified`, `authorized`, `powered by`.
2. **Không dùng logo hay ký tự đặc biệt của thương hiệu.**
3. **Nêu rõ tính độc lập ở ít nhất một headline.** Ví dụ `Not Affiliated With Lovable` (27 ký tự) — vừa giảm rủi ro chính sách, vừa tăng tin cậy với người đọc.

> 💡 Nguyên tắc 3 hơi phản trực giác nhưng đáng làm: nói thẳng "chúng tôi không phải đối tác của Lovable" loại bỏ đúng cái mà chính sách Google lo ngại — sự nhầm lẫn.

### 3.2. Bảng rủi ro trùng tên theo từng thương hiệu

| Thương hiệu | Mức nhiễu | Nghĩa khác | Xử lý |
|---|---|---|---|
| **Bolt** | 🔴 **Rất cao** | Hãng taxi số 2 Hà Lan · bu lông · Usain Bolt · tia chớp · scooter điện · Bolt Threads | **Chỉ bid `bolt.new` / `bolt new`, không bao giờ bid `bolt` đơn lẻ.** Loại NL/BE khỏi geo ở giai đoạn 1 |
| **Lovable** | 🟠 Cao | Tính từ tiếng Anh · thương hiệu đồ lót toàn cầu · lời bài hát · tên thú cưng | Negative list §9.1. Không bao giờ dùng broad match |
| **Replit** | 🟢 **Thấp** | Gần như không có nghĩa khác | Ít negative nhất. **Đây là thương hiệu sạch nhất để bắt đầu** |

➡️ **Kết luận quan trọng về thứ tự triển khai:** đừng bật cả ba cùng lúc. Bắt đầu bằng **Replit** (sạch nhất), rồi **Lovable** (nhiều keyword nhất), cuối cùng mới **Bolt** (nguy hiểm nhất). Xem §11.2.

---

<a id="4"></a>
## 4. Kiến trúc: 7 campaign riêng, không gộp

### 4.1. Vì sao phải tách campaign

Nếu gộp ba thương hiệu vào một campaign:

1. **Bolt sẽ nuốt ngân sách.** `bolt ai` có volume cao nhất trong tập dữ liệu — phần lớn là nhiễu. Chung ngân sách nghĩa là tiền chảy vào truy vấn taxi.
2. **Negative list khác nhau hoàn toàn.** Negative của Bolt (taxi, bu lông) vô nghĩa với Replit và ngược lại.
3. **Geo khác nhau.** Bolt cần loại NL/BE; Lovable và Replit thì không.
4. **Không so sánh được hiệu quả** giữa ba thương hiệu nếu chung ngân sách.

### 4.2. Sơ đồ

```
TÀI KHOẢN LaunchStudio — nhánh 3 thương hiệu AI
│
├── B1 · LS-Brand-Lovable            [EU-EN + NL · €250/thg]
│   ├── AG-LOV-Hire      (12 kw) → /en/fix-lovable-app
│   ├── AG-LOV-Problem   (11 kw) → /en/fix-lovable-app
│   └── AG-LOV-Migrate    (9 kw) → /en/lovable-tanstack-migration
│
├── B2 · LS-Brand-Bolt               [EU-EN · KHÔNG NL/BE · €120/thg]
│   ├── AG-BOLT-Hire      (8 kw) → /en/fix-bolt-app
│   └── AG-BOLT-Problem  (16 kw) → /en/fix-bolt-app
│
├── B3 · LS-Brand-Replit             [EU-EN + NL · €180/thg]
│   ├── AG-REP-Hire       (7 kw) → /en/fix-replit-app
│   ├── AG-REP-Problem   (12 kw) → /en/fix-replit-app
│   └── AG-REP-Cost      (10 kw) → /en/replit-hosting-costs
│
├── N1 · LS-NL-Service               [NL · tiếng Hà Lan · €150/thg]
│   ├── AG-NL-MVP         (6 kw) ┐
│   ├── AG-NL-App         (8 kw) ├→ /nl/mvp-laten-afmaken
│   ├── AG-NL-Afmaken     (6 kw) │
│   └── AG-NL-Geo         (6 kw) ┘
│
├── N2 · LS-NL-AI-Tools              [NL · tiếng Hà Lan · €60/thg]
│   ├── AG-NL-AI-Afmaken  (8 kw) ┐
│   ├── AG-NL-Lovable     (6 kw) ├→ /nl/ai-app-laten-afmaken
│   ├── AG-NL-Bolt        (4 kw) │
│   └── AG-NL-Replit      (6 kw) ┘
│
├── N3 · LS-NL-Security              [NL · tiếng Hà Lan · €60/thg]
│   └── AG-NL-Security   (12 kw) → /nl/security-audit
│
└── N4 · LS-NL-Payments              [NL · tiếng Hà Lan · €30/thg]
    └── AG-NL-Payments   (10 kw) → /nl/betalingen-koppelen
```

**Tổng: €850/tháng** ở cấu hình đầy đủ — €550 nhánh tiếng Anh + €300 nhánh tiếng Hà Lan.

> ⚠️ **B1–B3 vẫn nhắm geo Hà Lan, nhưng đặt ngôn ngữ campaign là English.** Đây không mâu thuẫn: người Hà Lan gõ `lovable deployment failed` bằng tiếng Anh vẫn phải thấy quảng cáo tiếng Anh. Geo và ngôn ngữ là hai thiết lập độc lập — đó chính là thứ bản plan đầu làm sai.

### 4.3. Cài đặt chung cho cả bảy

| Thiết lập | Giá trị | Lý do |
|---|---|---|
| Match type | **Phrase** là chính, **Exact** cho `[hire X developer]` | Broad match tuyệt đối không dùng — xem §2.2 |
| Bid strategy | **Manual CPC** trong 8 tuần đầu | Volume quá thấp cho Smart Bidding |
| Location targeting | **"Presence"**, không phải "Presence or interest" | "Interest" sẽ kéo truy vấn từ ngoài thị trường |
| Ad rotation | **"Do not optimize"** 4 tuần đầu | Để so sánh công bằng bộ RSA A và B |
| Ad schedule | Cả tuần trong 4 tuần đầu | Thu dữ liệu trước khi cắt khung giờ |
| **Ngôn ngữ** | **B1–B3: English · N1–N4: Dutch** | **Không campaign nào chọn cả hai** — xem Rủi ro 4 |

---

<a id="5"></a>
## 5. B1 · `LS-Brand-Lovable` — €250/tháng (€8,20/ngày)

### 5.1. Ad group & keyword

| Ad group | Keyword chính | Max CPC | Ngày | Landing page |
|---|---|---:|---:|---|
| `AG-LOV-Hire` (12) | `"fix lovable app"`, `"lovable developer for hire"`, `[hire lovable developer]`, `"lovable developer"`, `"lovable app development service"`, `"take my lovable app to production"`, `"lovable app production ready"`, `"lovable audit service"`, `"lovable security audit"` … | €12,00 | €3,50 | `/en/fix-lovable-app` |
| `AG-LOV-Problem` (11) | `"lovable app not working"`, `"lovable deployment failed"`, `"lovable preview vs production"`, `"lovable custom domain not working"`, `"lovable stripe integration"`, `"lovable login not working"`, `"lovable supabase rls"`, `"is lovable secure"` … | €9,00 | €2,50 | `/en/fix-lovable-app` |
| `AG-LOV-Migrate` (9) | `"migrate off lovable"`, `"lovable migration service"`, `"lovable tanstack migration"`, `"migrate lovable to tanstack"`, `"lovable ssr upgrade"`, `"lovable export code"`, `"self host lovable app"` … | €11,00 | €2,20 | `/en/lovable-tanstack-migration` |

#### Danh sách keyword đầy đủ — B1 Lovable

**`AG-LOV-Hire`** — 12 keyword · volume 30/tháng · 3 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `hire lovable developer` | Exact | Hire | P1 | **10** |
| `lovable developer` | Phrase | Hire | P1 | **10** |
| `lovable freelancer` | Phrase | Hire | P2 | **10** |
| `fix lovable app` | Phrase | Hire | P1 | 0 |
| `lovable developer for hire` | Phrase | Hire | P1 | 0 |
| `lovable app development service` | Phrase | Hire | P1 | 0 |
| `lovable app agency` | Phrase | Hire | P2 | 0 |
| `take my lovable app to production` | Phrase | Hire | P1 | 0 |
| `lovable app production ready` | Phrase | Hire | P1 | 0 |
| `finish my lovable app` | Phrase | Hire | P2 | 0 |
| `lovable audit service` | Phrase | Service | P1 | 0 |
| `lovable security audit` | Phrase | Service | P1 | 0 |

**`AG-LOV-Problem`** — 11 keyword · volume 40/tháng · 4 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `lovable not working` | Phrase | Fix | P2 | **10** |
| `lovable custom domain not working` | Phrase | Fix | P2 | **10** |
| `lovable stripe integration` | Phrase | Fix | P1 | **10** |
| `is lovable secure` | Phrase | Research | P2 | **10** |
| `lovable app not working` | Phrase | Fix | P2 | 0 |
| `lovable deployment failed` | Phrase | Fix | P2 | 0 |
| `lovable preview vs production` | Phrase | Fix | P2 | 0 |
| `lovable stripe not working` | Phrase | Fix | P1 | 0 |
| `lovable login not working` | Phrase | Fix | P2 | 0 |
| `lovable supabase rls` | Phrase | Security | P2 | 0 |
| `lovable security vulnerabilities` | Phrase | Research | P2 | 0 |

**`AG-LOV-Migrate`** — 9 keyword · volume 40/tháng · 4 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `lovable export code` | Phrase | How-to | P2 | **10** |
| `self host lovable app` | Phrase | Decision | P2 | **10** |
| `lovable to nextjs` | Phrase | How-to | P2 | **10** |
| `lovable alternative` | Phrase | Decision | P2 | **10** |
| `migrate off lovable` | Phrase | Decision | P1 | 0 |
| `lovable migration service` | Phrase | Service | P1 | 0 |
| `lovable tanstack migration` | Phrase | Service | P1 | 0 |
| `migrate lovable to tanstack` | Phrase | Service | P1 | 0 |
| `lovable ssr upgrade` | Phrase | Service | P1 | 0 |

> 💡 **`AG-LOV-Migrate` — cơ hội TanStack, và vì sao nó vẫn đáng chú ý dù volume bằng 0**
>
> Lovable đổi stack mặc định từ **React + Vite → TanStack Start**: mặc định cho dự án mới từ **13/05/2026**, Enterprise từ **22/06/2026**. Lovable **không tự động migrate dự án cũ**. Ba hệ quả tạo ra nhu cầu:
>
> 1. Mọi dự án tạo trước 05/2026 vẫn chạy stack cũ — và chủ sở hữu thường **không biết điều đó**
> 2. Stack cũ không có SSR → ảnh hưởng trực tiếp tới SEO, nỗi đau nhiều founder đã cảm thấy nhưng chưa biết nguyên nhân
> 3. Migration là việc kỹ thuật, không phải prompt — đúng định nghĩa "last-mile" của LaunchStudio
>
> **Xác minh thương mại:** `nextlovable.com` bán audit **$199** (`/lovable-tanstack-ssr`) và **$299** (`/migrate-lovable-tanstack`), cộng một trang `/migration-guide`. Ba landing page cho một vấn đề = họ đang kiếm được tiền từ nó.
>
> ⏳ **Tính thời sự:** cửa sổ này sẽ đóng khi Lovable tự migrate hoặc khi dự án cũ chết dần. Ước tính còn **6–12 tháng**.
>
> ⚠️ **Nhưng đo được volume = 0 cho cả 9 keyword của nhóm này** (§2.4). Nhu cầu có thật về mặt kỹ thuật nhưng người dùng **chưa biết để tìm** — họ không biết stack của mình cũ. Đây là nhu cầu phải **tạo ra bằng nội dung**, không mua được bằng Search Ads.

### 5.2. RSA — bộ A (có tên thương hiệu)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Lovable App Stuck in Preview?` | 29 | **P1** |
| H2 | `We Finish Lovable Builds` | 24 | **P2** |
| H3 | `Security, Stripe & Hosting` | 26 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Your Frontend Stays` | 19 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Not Affiliated With Lovable` | 27 | |
| H10 | `Get a Free Code Review` | 22 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Built it with Lovable but cannot go live? We fix security, payments and hosting.` | 80 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

### 5.3. RSA — bộ B (không tên thương hiệu, dùng khi bị hạn chế)

| # | Headline (English) | Ch |
|---|---|---:|
| H1 | `AI App Stuck in Preview?` | 24 |
| H2 | `We Finish AI-Built Apps` | 23 |
| H3 | `Security, Stripe & Hosting` | 26 |
| D1 | `Built it with an AI builder but cannot go live? We fix security, payments, hosting.` | 83 |

> Các headline H4–H8, H10 và description D2–D3 ở bộ A **không chứa tên thương hiệu** nên dùng lại nguyên cho bộ B.

---

<a id="6"></a>
## 6. B2 · `LS-Brand-Bolt` — €120/tháng (€4/ngày) — CAMPAIGN NGUY HIỂM NHẤT

### 6.1. 🔴 Năm quy tắc bắt buộc

Đây là campaign duy nhất trong toàn bộ tài khoản có khả năng đốt sạch ngân sách trong một ngày.

1. **Không bao giờ bid `bolt` đơn lẻ.** Chỉ `bolt.new` hoặc `bolt new`.
2. **Loại NL/BE khỏi geo ở giai đoạn 1.** Bolt là hãng taxi số 2 Hà Lan, hoạt động tại đúng bốn thành phố mục tiêu của LaunchStudio: Amsterdam, Rotterdam, Den Haag, Utrecht.
3. **Negative list §9.2 phải áp trước khi campaign chạy phút đầu tiên.**
4. **Ngân sách thấp nhất trong ba campaign** cho tới khi Search Terms Report sạch trong 2 tuần liên tiếp.
5. **Kiểm Search Terms mỗi ngày** trong 3 tuần đầu — không phải 2 ngày/lần như các campaign khác.

### 6.2. Ad group & keyword

| Ad group | Keyword chính | Max CPC | Ngày | Landing page |
|---|---|---:|---:|---|
| `AG-BOLT-Hire` (8) | `"fix bolt app"`, `"fix bolt new app"`, `"bolt new developer"`, `[hire bolt new developer]`, `"bolt new to production"`, `"bolt new app production ready"` … | €10,00 | €2,20 | `/en/fix-bolt-app` |
| `AG-BOLT-Problem` (16) | `"bolt new not working"`, `"bolt new preview vs production"`, `"bolt new production error"`, `"bolt new deployment"`, `"bolt new environment variables"`, `"bolt new cors error"`, `"bolt new bundle too large"`, `"bolt new netlify deploy"` … | €8,00 | €1,80 | `/en/fix-bolt-app` |

> ⚠️ **Keyword `"bolt app developer"` trong CSV được đánh dấu rủi ro.** Không có chữ "new" nên dễ khớp truy vấn về ứng dụng taxi Bolt. Để **Exact** hoặc bỏ hẳn ở giai đoạn 1.

#### Danh sách keyword đầy đủ — B2 Bolt

**`AG-BOLT-Hire`** — 8 keyword · volume 20/tháng · 2 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `bolt new developer` | Phrase | Hire | P1 | **10** |
| `bolt app developer` | Phrase | Hire | P2 | **10** |
| `fix bolt app` | Phrase | Hire | P1 | 0 |
| `fix bolt new app` | Phrase | Hire | P1 | 0 |
| `hire bolt new developer` | Exact | Hire | P1 | 0 |
| `bolt new to production` | Phrase | Service | P1 | 0 |
| `bolt new app production ready` | Phrase | Service | P1 | 0 |
| `bolt new agency` | Phrase | Hire | P2 | 0 |

**`AG-BOLT-Problem`** — 16 keyword · volume 100/tháng · 10 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `bolt new not working` | Phrase | Fix | P2 | **10** |
| `bolt new deployment` | Phrase | Fix | P2 | **10** |
| `bolt new environment variables` | Phrase | Fix | P2 | **10** |
| `bolt new supabase` | Phrase | How-to | P3 | **10** |
| `bolt new stripe` | Phrase | How-to | P3 | **10** |
| `bolt new custom domain` | Phrase | Fix | P3 | **10** |
| `bolt new blank page` | Phrase | Fix | P3 | **10** |
| `bolt new export code` | Phrase | How-to | P2 | **10** |
| `bolt new token limit` | Phrase | Cost | P3 | **10** |
| `bolt new security` | Phrase | Security | P2 | **10** |
| `bolt new preview vs production` | Phrase | Fix | P2 | 0 |
| `bolt new production error` | Phrase | Fix | P2 | 0 |
| `bolt new deploy error` | Phrase | Fix | P2 | 0 |
| `bolt new cors error` | Phrase | Fix | P3 | 0 |
| `bolt new bundle too large` | Phrase | Fix | P3 | 0 |
| `bolt new netlify deploy` | Phrase | Fix | P3 | 0 |

### 6.3. Góc bán đặc thù của Bolt

Bolt.new chạy trên WebContainer — môi trường trong trình duyệt. Điều này tạo ra một loại lỗi rất đặc trưng: **preview chạy hoàn hảo, production vỡ ngay**. Nguyên nhân thường là:

- Biến môi trường trong Secrets của Bolt **không tự chuyển** sang Netlify/Vercel → build chạy với biến `undefined`
- Toàn bộ traffic trong WebContainer là same-origin → **lỗi CORS chỉ xuất hiện khi deploy thật**
- Bundle vượt giới hạn kích thước

➡️ Ad copy nên nói đúng cái này: *"Preview Works, Live Breaks?"* — người gặp đúng vấn đề sẽ nhận ra mình ngay.

### 6.4. RSA — bộ A (có tên thương hiệu)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Bolt.new App Not Deploying?` | 27 | **P1** |
| H2 | `Preview Works, Live Breaks?` | 27 | **P2** |
| H3 | `We Fix CORS, Env & Build` | 24 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Your Frontend Stays` | 19 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Get a Free Build Review` | 23 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Bolt.new preview is not production. We fix env vars, CORS and build failures.` | 77 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

> 💡 **Viết `Bolt.new` có dấu chấm, không viết `Bolt` đơn lẻ trong ad text.** Vừa giảm nhầm lẫn với hãng taxi, vừa khớp chính xác hơn với truy vấn của người dùng công cụ.

---

<a id="7"></a>
## 7. B3 · `LS-Brand-Replit` — €180/tháng (€5,90/ngày) — CAMPAIGN SẠCH NHẤT

### 7.1. Vì sao nên bắt đầu từ đây

- **Tên riêng gần như không có nghĩa khác** → ít nhiễu nhất trong ba thương hiệu
- **Negative list ngắn nhất** → ít rủi ro vận hành
- **Có một pain point thương mại rõ ràng mà hai thương hiệu kia không có:** chi phí hosting bất ngờ

Replit có ba kiểu deployment với cấu trúc giá khác nhau — Static, Autoscale (trả theo dùng, về 0 khi rảnh), và Reserved VM (luôn bật, tính phí cố định hàng tháng bất kể có ai truy cập hay không). Chi phí Reserved VM là khoản **âm thầm tích lũy** và là nguyên nhân phổ biến khiến người dùng đi tìm phương án khác.

➡️ `AG-REP-Cost` khai thác đúng thời điểm đó: người vừa nhận hoá đơn và đang tìm đường ra.

### 7.2. Ad group & keyword

| Ad group | Keyword chính | Max CPC | Ngày | Landing page |
|---|---|---:|---:|---|
| `AG-REP-Hire` (7) | `"fix replit app"`, `"replit developer for hire"`, `[hire replit developer]`, `"replit app to production"`, `"replit production ready"` … | €11,00 | €2,00 | `/en/fix-replit-app` |
| `AG-REP-Problem` (12) | `"replit app not working"`, `"replit deployment failed"`, `"replit deployment error"`, `"replit database connection error"`, `"replit agent not working"`, `"replit secrets not working"`, `"replit security"` … | €8,00 | €1,90 | `/en/fix-replit-app` |
| `AG-REP-Cost` (10) | `"replit reserved vm cost"`, `"replit autoscale vs reserved vm"`, `"replit deployment cost"`, `"replit pricing too expensive"`, `"migrate off replit"`, `"replit export to vercel"`, `"move replit app to own server"` … | €10,00 | €2,00 | `/en/replit-hosting-costs` |

#### Danh sách keyword đầy đủ — B3 Replit

**`AG-REP-Hire`** — 7 keyword · volume 220/tháng · 2 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `replit agency` | Phrase | Hire | P2 | **210** |
| `hire replit developer` | Exact | Hire | P1 | **10** |
| `fix replit app` | Phrase | Hire | P1 | 0 |
| `replit developer for hire` | Phrase | Hire | P1 | 0 |
| `replit app to production` | Phrase | Service | P1 | 0 |
| `replit app developer` | Phrase | Hire | P2 | 0 |
| `replit production ready` | Phrase | Service | P1 | 0 |

**`AG-REP-Problem`** — 12 keyword · volume 50/tháng · 5 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `replit not working` | Phrase | Fix | P3 | **10** |
| `replit agent not working` | Phrase | Fix | P3 | **10** |
| `replit agent stuck` | Phrase | Fix | P3 | **10** |
| `replit custom domain` | Phrase | Fix | P3 | **10** |
| `replit security` | Phrase | Security | P2 | **10** |
| `replit app not working` | Phrase | Fix | P2 | 0 |
| `replit deployment failed` | Phrase | Fix | P2 | 0 |
| `replit deployment error` | Phrase | Fix | P2 | 0 |
| `replit database connection error` | Phrase | Fix | P2 | 0 |
| `replit secrets not working` | Phrase | Fix | P3 | 0 |
| `replit app slow` | Phrase | Fix | P3 | 0 |
| `replit app crashes` | Phrase | Fix | P3 | 0 |

**`AG-REP-Cost`** — 10 keyword · volume 30/tháng · 3 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `replit deployment cost` | Phrase | Cost | P1 | **10** |
| `replit hosting cost` | Phrase | Cost | P2 | **10** |
| `replit export code` | Phrase | How-to | P2 | **10** |
| `replit reserved vm cost` | Phrase | Cost | P1 | 0 |
| `replit autoscale vs reserved vm` | Phrase | Decision | P1 | 0 |
| `replit pricing too expensive` | Phrase | Cost | P1 | 0 |
| `migrate off replit` | Phrase | Decision | P1 | 0 |
| `replit export to vercel` | Phrase | How-to | P2 | 0 |
| `replit alternative production` | Phrase | Decision | P2 | 0 |
| `move replit app to own server` | Phrase | Service | P1 | 0 |

### 7.3. RSA — bộ A (có tên thương hiệu)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Replit App Not Deploying?` | 25 | **P1** |
| H2 | `Autoscale or Reserved VM?` | 25 | **P2** |
| H3 | `We Move Replit to Prod` | 22 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Stop Surprise Hosting Bills` | 27 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Get a Free Deploy Review` | 24 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Replit deploy failing or costing too much? We move it to hosting you control.` | 77 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

---

<a id="8"></a>
## 8. N1–N4 · Bốn campaign tiếng Hà Lan

### 8.1. Vì sao phần này tồn tại — và vì sao nó không phải bản dịch

Bản plan đầu tiên có lỗi logic: **85 keyword tiếng Anh nhưng quảng cáo song ngữ Anh/Hà Lan.** Quảng cáo tiếng Hà Lan chỉ hiển thị khi truy vấn là tiếng Hà Lan; gắn nó vào keyword tiếng Anh thì nó gần như không bao giờ được phục vụ. Ngược lại, người Hà Lan gõ tiếng Hà Lan sẽ không khớp keyword tiếng Anh nào cả. Hai nửa không gặp nhau.

Cách sửa **không phải** dịch 85 keyword sang tiếng Hà Lan. Dữ liệu thị trường cho thấy nhu cầu tiếng Hà Lan phân bố rất khác:

| Loại truy vấn | Người Hà Lan gõ bằng | Bằng chứng |
|---|---|---|
| Chuỗi lỗi kỹ thuật (`deployment failed`, `RLS`, `CORS`) | **Tiếng Anh** | Thông báo lỗi bản thân nó là tiếng Anh; dev copy-paste nguyên văn vào Google |
| Tên công cụ (`Lovable`, `Bolt`, `Replit`) | **Tiếng Anh** | Tìm kiếm nội dung tiếng Hà Lan về 3 công cụ này chỉ trả về kết quả tiếng Anh — nội dung bản địa rất mỏng |
| Ý định thuê dịch vụ | **Tiếng Hà Lan** | ≥5 bureau NL có landing page riêng cho `mvp laten maken` (Wiwi, Appfront, Agency 6, Zedrox, Creatix Code) — có cạnh tranh nghĩa là có volume |
| Tuân thủ pháp lý | **Tiếng Hà Lan** | Người NL gõ `AVG`, không gõ `GDPR` |
| Thanh toán | **Tiếng Hà Lan + tên PSP bản địa** | `iDEAL`, `Mollie` — đối thủ nước ngoài không nhắc tới |

Nên bộ keyword Hà Lan **hẹp hơn nhưng thương mại hơn**. So sánh phân bố ý định:

| Ý định | Bộ EN (85 kw) | Bộ NL (72 kw) |
|---|---:|---:|
| Fix (sửa lỗi) | 30 | **1** |
| Hire + Service (thuê) | 32 | **60** |
| Cost / Decision | 11 | 4 |
| Compliance | 0 | 3 |

> ⚠️ **Đây là chênh lệch có chủ đích, không phải thiếu sót.** Bộ NL gần như không có keyword sửa lỗi vì người Hà Lan không gõ lỗi kỹ thuật bằng tiếng Hà Lan. Nếu bạn thấy ai đó đề xuất `lovable implementatie mislukt`, đó là dịch máy — không ai gõ như vậy.

**Quy tắc bất biến từ đây trở đi: keyword tiếng nào, quảng cáo tiếng đó.** B1–B3 (§5–§7) giờ chỉ còn RSA tiếng Anh. N1–N4 chỉ dùng RSA tiếng Hà Lan. Không campaign nào trộn hai thứ tiếng.

### 8.2. Kiến trúc bốn campaign NL

72 keyword, 4 campaign, 10 ad group.

```
N1-NL-Service    €150/thg   26 kw   Ý định thuê chung (MVP/app laten maken)
  ├─ AG-NL-MVP        6     mvp laten maken / bouwen / ontwikkeling
  ├─ AG-NL-App        8     app / webapp / saas laten bouwen
  ├─ AG-NL-Afmaken    6     app + prototype laten afmaken  ← khớp pitch nhất
  └─ AG-NL-Geo        6     + amsterdam / rotterdam / utrecht / eindhoven

N2-NL-AI-Tools    €60/thg   24 kw   Tiếng Hà Lan + tên công cụ AI
  ├─ AG-NL-AI-Afmaken 8     ai app laten afmaken, app productieklaar maken
  ├─ AG-NL-Lovable    6     lovable app laten afmaken / live zetten / beveiligen
  ├─ AG-NL-Bolt       4     LUÔN kèm "new" — xem §6.1
  └─ AG-NL-Replit     6     replit kosten te hoog, naar eigen server

N3-NL-Security    €60/thg   12 kw   Beveiliging + AVG
  └─ AG-NL-Security  12     beveiligingsaudit, avg proof, technische due diligence

N4-NL-Payments    €30/thg   10 kw   iDEAL / Mollie / Stripe
  └─ AG-NL-Payments  10     ideal betaling toevoegen, mollie koppelen app
```

**Tổng NL: €300/tháng.** Cộng với €550 của B1–B3 → **€850/tháng.**

Cài đặt chung: Netherlands only · **ngôn ngữ Dutch** (không thêm English — đây là điểm khác biệt duy nhất so với B1–B3) · Manual CPC hoặc Maximize Clicks có trần · Search only, tắt Display & Search Partners.

#### Danh sách keyword đầy đủ — N1–N4 tiếng Hà Lan

**`AG-NL-MVP`** — 6 keyword · volume 90/tháng · 3 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `mvp laten maken` | Phrase | Hire | P1 | **50** |
| `mvp ontwikkeling` | Phrase | Hire | P1 | **30** |
| `mvp laten ontwikkelen` | Phrase | Hire | P1 | **10** |
| `mvp laten bouwen` | Phrase | Hire | P1 | 0 |
| `mvp bureau` | Phrase | Hire | P2 | 0 |
| `minimum viable product laten maken` | Phrase | Hire | P2 | 0 |

**`AG-NL-App`** — 8 keyword · volume 1100/tháng · 7 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `app laten maken` | Phrase | Hire | P1 | **480** |
| `webapplicatie laten maken` | Phrase | Hire | P2 | **260** |
| `app laten bouwen` | Phrase | Hire | P1 | **140** |
| `software laten maken` | Phrase | Hire | P2 | **110** |
| `maatwerk software laten maken` | Phrase | Hire | P2 | **90** |
| `webapp laten bouwen` | Phrase | Hire | P1 | **10** |
| `web applicatie laten bouwen` | Phrase | Hire | P2 | **10** |
| `saas laten bouwen` | Phrase | Hire | P1 | 0 |

**`AG-NL-Afmaken`** — 6 keyword · volume 20/tháng · 1 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `developer inhuren app` | Phrase | Hire | P2 | **20** |
| `app laten afmaken` | Phrase | Service | P1 | 0 |
| `prototype laten afmaken` | Phrase | Service | P1 | 0 |
| `onafgemaakte app afmaken` | Phrase | Service | P2 | 0 |
| `app afmaken freelancer` | Phrase | Hire | P2 | 0 |
| `freelance developer nederland` | Phrase | Hire | P3 | 0 |

**`AG-NL-Geo`** — 6 keyword · volume 70/tháng · 4 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `app laten maken amsterdam` | Phrase | Hire | P1 | **20** |
| `app laten maken rotterdam` | Phrase | Hire | P2 | **20** |
| `app laten maken eindhoven` | Phrase | Hire | P2 | **20** |
| `app laten maken utrecht` | Phrase | Hire | P2 | **10** |
| `softwarebureau amsterdam` | Phrase | Hire | P2 | 0 |
| `mvp laten maken amsterdam` | Phrase | Hire | P1 | 0 |

**`AG-NL-AI-Afmaken`** — 8 keyword · volume 0/tháng · 0 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `ai app laten afmaken` | Phrase | Service | P1 | 0 |
| `ai gebouwde app laten afmaken` | Phrase | Service | P1 | 0 |
| `ai prototype naar productie` | Phrase | Service | P1 | 0 |
| `van prototype naar productie` | Phrase | Decision | P1 | 0 |
| `app productieklaar maken` | Phrase | Service | P1 | 0 |
| `prototype niet live krijgen` | Phrase | Fix | P2 | 0 |
| `vibe coding uitbesteden` | Phrase | Service | P2 | 0 |
| `no code app laten afmaken` | Phrase | Service | P2 | 0 |

**`AG-NL-Lovable`** — 6 keyword · volume 0/tháng · 0 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `lovable app laten maken` | Phrase | Hire | P1 | 0 |
| `lovable app laten afmaken` | Phrase | Service | P1 | 0 |
| `lovable developer nederland` | Phrase | Hire | P2 | 0 |
| `lovable app beveiligen` | Phrase | Security | P1 | 0 |
| `lovable app live zetten` | Phrase | Service | P1 | 0 |
| `lovable alternatief` | Phrase | Decision | P3 | 0 |

**`AG-NL-Bolt`** — 4 keyword · volume 10/tháng · 1 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `bolt new developer` | Phrase | Hire | P2 | **10** |
| `bolt new app laten afmaken` | Phrase | Service | P1 | 0 |
| `bolt new app live zetten` | Phrase | Service | P1 | 0 |
| `app gebouwd met bolt` | Phrase | Service | P2 | 0 |

**`AG-NL-Replit`** — 6 keyword · volume 0/tháng · 0 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `replit app laten afmaken` | Phrase | Service | P1 | 0 |
| `replit app live zetten` | Phrase | Service | P1 | 0 |
| `replit kosten te hoog` | Phrase | Cost | P1 | 0 |
| `weg van replit` | Phrase | Decision | P2 | 0 |
| `replit app naar eigen server` | Phrase | Service | P1 | 0 |
| `replit developer nederland` | Phrase | Hire | P2 | 0 |

**`AG-NL-Security`** — 12 keyword · volume 50/tháng · 2 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `technische due diligence` | Phrase | Service | P1 | **40** |
| `pentest webapplicatie` | Phrase | Service | P2 | **10** |
| `ai app beveiligen` | Phrase | Security | P1 | 0 |
| `beveiligingsaudit webapplicatie` | Phrase | Service | P1 | 0 |
| `security audit laten uitvoeren` | Phrase | Service | P1 | 0 |
| `code audit laten uitvoeren` | Phrase | Service | P2 | 0 |
| `app avg proof maken` | Phrase | Compliance | P1 | 0 |
| `avg compliance webapp` | Phrase | Compliance | P1 | 0 |
| `persoonsgegevens beveiligen app` | Phrase | Compliance | P2 | 0 |
| `datalek voorkomen app` | Phrase | Security | P2 | 0 |
| `supabase beveiliging` | Phrase | Security | P2 | 0 |
| `due diligence software audit` | Phrase | Service | P1 | 0 |

**`AG-NL-Payments`** — 10 keyword · volume 0/tháng · 0 từ có volume > 0

| Keyword | Match | Ý định | Ưu tiên | Volume |
|---|---|---|---|---:|
| `ideal betaling toevoegen app` | Phrase | Service | P1 | 0 |
| `ideal koppelen webshop` | Phrase | Service | P2 | 0 |
| `mollie koppelen app` | Phrase | Service | P1 | 0 |
| `mollie integratie laten bouwen` | Phrase | Hire | P1 | 0 |
| `stripe koppelen app` | Phrase | Service | P1 | 0 |
| `stripe integratie nederland` | Phrase | Hire | P2 | 0 |
| `betalingen toevoegen aan app` | Phrase | Service | P1 | 0 |
| `abonnementen in app bouwen` | Phrase | Service | P2 | 0 |
| `inlogsysteem laten bouwen` | Phrase | Service | P2 | 0 |
| `gebruikersbeheer app bouwen` | Phrase | Service | P3 | 0 |

### 8.3. Ba nhận định quan trọng về bộ NL

**① ~~`N2-NL-AI-Tools` là tài sản rẻ nhất trong toàn tài khoản.~~ ❌ SAI — đã bị dữ liệu phủ định.**
Nhận định gốc: *"gần như chắc chắn không ai bid, CPC ở mức sàn, sở hữu trọn nhóm với vài chục euro"*. **Keyword Planner cho kết quả: cả campaign 24 keyword có 10 lượt tìm/tháng, 23/24 từ bằng 0.** Ba ad group `AG-NL-AI-Afmaken`, `AG-NL-Lovable`, `AG-NL-Replit` đều 0 tuyệt đối. Không có gì để sở hữu. Xem §2.5.

**② `N1-NL-Service` là campaign duy nhất có thể mở rộng — và cũng rủi ro nhất về ICP.**
`mvp laten maken` có cạnh tranh thật từ bureau full-service báo giá €25.000–50.000. Họ sẽ đẩy CPC lên €8–15. Người bấm vào có thể đang tìm đối tác xây mới từ đầu, không phải người cần **làm nốt** một prototype đã có. Landing page phải nói rõ điều này ở màn hình đầu tiên, nếu không CPL sẽ rất tệ.

**③ `app laten maken` cần negative chống lẫn app mobile.**
Ở Hà Lan "app" mặc định gợi đến ứng dụng điện thoại. Bắt buộc negative: `ios`, `android`, `native`, `app store`, `google play`, `flutter`, `react native`, `iphone app`, `android app`. Nếu không, khoảng một phần ba truy vấn sẽ là người tìm làm app native — ngoài phạm vi dịch vụ.

### 8.4. RSA — N1-NL-Service (chỉ tiếng Hà Lan)

| # | Headline (Nederlands) | Ch | Pin |
|---|---|---:|---|
| H1 | `MVP Laten Bouwen?` | 17 | **P1** |
| H2 | `Van Prototype Naar Live` | 23 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | 22 | |
| H4 | `Live Binnen 1-3 Weken` | 21 | |
| H5 | `Geen Herbouw Nodig` | 18 | |
| H6 | `Wij Fixen Alleen Wat Moet` | 25 | |
| H7 | `11+ Jaar Ervaring` | 17 | |
| H8 | `100% Eigendom Van Je Code` | 25 | |
| H9 | `Security, Betalingen, Hosting` | 29 | |
| H10 | `Gratis Offerte In 1 Dag` | 23 | **P3** |

| # | Description (Nederlands) | Ch |
|---|---|---:|
| D1 | `Prototype klaar maar niet live? Wij regelen security, betalingen en hosting.` | 76 |
| D2 | `Vaste prijs vanaf €800, live in 1-3 weken. Alle code blijft 100% van jou.` | 73 |
| D3 | `Bureau rekent €50.000 voor herbouw? Wij behouden je frontend en fixen wat nodig is.` | 83 |

> 💡 **H5 `Geen Herbouw Nodig` và D3 là hai mẩu quan trọng nhất của campaign này.** Chúng tấn công trực diện điểm yếu của bureau full-service đang bid cùng keyword: họ bán dự án xây lại từ đầu, LaunchStudio bán việc làm nốt phần còn thiếu. Đây là thứ phân biệt bạn ngay trên trang kết quả, trước khi người dùng bấm.

### 8.5. RSA — N2-NL-AI-Tools (chỉ tiếng Hà Lan)

| # | Headline (Nederlands) | Ch | Pin |
|---|---|---:|---|
| H1 | `AI-App Niet Live Te Krijgen?` | 28 | **P1** |
| H2 | `Wij Maken Je AI-App Af` | 22 | **P2** |
| H3 | `Gebouwd Met Lovable Of Bolt?` | 28 | |
| H4 | `Vaste Prijs Vanaf €800` | 22 | |
| H5 | `Live Binnen 1-3 Weken` | 21 | |
| H6 | `Je Frontend Blijft Staan` | 24 | |
| H7 | `11+ Jaar Engineering Ervaring` | 29 | |
| H8 | `100% Eigendom Van Je Code` | 25 | |
| H9 | `Gratis Code Review` | 18 | **P3** |

| # | Description (Nederlands) | Ch |
|---|---|---:|
| D1 | `Met een AI-tool gebouwd maar niet live? Wij fixen security, betalingen en hosting.` | 82 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je frontend blijft, code 100% van jou.` | 81 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | 78 |

> ⚠️ **H3 chứa tên thương hiệu.** Áp dụng đúng ba tầng phòng vệ ở §3.1. Nếu bị Google hạn chế, thay H3 bằng `Gebouwd Met Een AI-Tool?` (24) và bỏ mọi tên thương hiệu khỏi bộ này. Ad group `AG-NL-Bolt` **không** được dùng H3 chứa chữ "Bolt" đứng một mình — xem §6.1.

### 8.6. RSA — N3-NL-Security (chỉ tiếng Hà Lan)

| # | Headline (Nederlands) | Ch | Pin |
|---|---|---:|---|
| H1 | `Is Je AI-App Wel Veilig?` | 24 | **P1** |
| H2 | `Security Audit Vaste Prijs` | 26 | **P2** |
| H3 | `45% AI-Code Heeft Lekken` | 24 | |
| H4 | `Wachtwoorden, Keys, Rechten` | 27 | |
| H5 | `Rapport In Dagen` | 16 | |
| H6 | `11+ Jaar Cybersecurity` | 22 | |
| H7 | `AVG-Proof Opgeleverd` | 20 | |
| H8 | `Klaar Voor Due Diligence` | 24 | |
| H9 | `Vraag Gratis Scan Aan` | 21 | **P3** |

| # | Description (Nederlands) | Ch |
|---|---|---:|
| D1 | `Open keys, geen rechten, geen limieten. Wij vinden wat AI-code achterlaat.` | 74 |
| D2 | `Vaste prijs voor een audit van je AI-app. Helder rapport met prioriteiten, in dagen.` | 84 |
| D3 | `11+ jaar security-engineering, vertrouwd door Vodafone, TNO en CFLW. Gratis offerte.` | 84 |

> ⚠️ **H3 `45% AI-Code Heeft Lekken` là một tuyên bố số liệu.** Landing page bắt buộc phải dẫn nguồn nghiên cứu cho con số này, nếu không sẽ vi phạm chính sách Misrepresentation của Google. Nếu không dẫn được nguồn, thay bằng `AI-Code Laat Gaten Achter` (25).

### 8.7. RSA — N4-NL-Payments (chỉ tiếng Hà Lan)

| # | Headline (Nederlands) | Ch | Pin |
|---|---|---:|---|
| H1 | `Betalingen In Je App?` | 21 | **P1** |
| H2 | `Stripe, Mollie Of iDEAL` | 23 | **P2** |
| H3 | `Wij Koppelen Het Goed` | 21 | |
| H4 | `Vaste Prijs Vanaf €800` | 22 | |
| H5 | `Live Binnen 1-3 Weken` | 21 | |
| H6 | `Webhooks Die Wél Werken` | 23 | |
| H7 | `Abonnementen Of Eenmalig` | 24 | |
| H8 | `11+ Jaar Ervaring` | 17 | |
| H9 | `Gratis Adviesgesprek` | 20 | **P3** |

| # | Description (Nederlands) | Ch |
|---|---|---:|
| D1 | `Betalingen werken niet in je app? Wij koppelen Stripe, Mollie of iDEAL correct.` | 79 |
| D2 | `Vaste prijs vanaf €800. Abonnementen, eenmalig of op gebruik. Live in 1-3 weken.` | 80 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | 78 |

> 💡 **`iDEAL` là lợi thế bản địa không ai ở nước ngoài dùng.** iDEAL chiếm phần lớn thanh toán trực tuyến tại Hà Lan. Một founder Hà Lan xây app bằng Lovable sẽ phát hiện Stripe không hỗ trợ iDEAL đầy đủ như họ tưởng — đó chính là lúc họ tìm kiếm. Giữ `iDEAL` viết đúng chuẩn chữ thường-hoa.

### 8.8. Kiểm tra giới hạn ký tự

Toàn bộ 49 mẩu RSA tiếng Hà Lan ở §8.4–§8.7 đã được đếm bằng script:

| Loại | Giới hạn Google | Dài nhất trong bộ NL | Kết quả |
|---|---:|---:|---|
| Headline | 30 | 29 (`Security, Betalingen, Hosting` · `11+ Jaar Engineering Ervaring`) | ✅ 0 vi phạm |
| Description | 90 | 84 (`...Helder rapport met prioriteiten, in dagen.` · `...Gratis offerte.`) | ✅ 0 vi phạm |

> ⚠️ **Ký tự `€` và chữ có dấu (`Wél`) tính là 1 ký tự** trong Google Ads, không phải 2. Các số đếm ở trên đã theo quy ước này. Nếu bạn sửa copy, đếm lại bằng script chứ đừng ước lượng — lần kiểm tra trước đã phát hiện một headline 33 ký tự bị khai nhầm là 30.

### 8.9. Negative keyword riêng cho nhóm NL

Ngoài các danh sách ở §9, nhóm NL cần thêm:

| Khối | Từ khoá phủ định | Lý do |
|---|---|---|
| **App native** (broad) | `ios`, `android`, `native`, `flutter`, `iphone`, `ipad`, `smartphone`, `play store` | "app" ở NL mặc định là app điện thoại |
| **Webshop** (phrase) | `webshop laten maken`, `woocommerce`, `shopify`, `magento`, `lightspeed` | `ideal koppelen` kéo rất nhiều traffic e-commerce |
| **Học nghề** (broad) | `cursus`, `opleiding`, `leren`, `stage`, `vacature`, `salaris`, `zzp tarief` | Ý định học/tìm việc, không phải thuê dịch vụ |
| **Miễn phí** (broad) | `gratis`, `zelf`, `template`, `voorbeeld`, `handleiding` | Trừ `gratis offerte` — nếu cần giữ thì dùng phrase `gratis offerte` làm keyword dương |
| **Sản xuất** (phrase + broad) | Toàn bộ danh sách 218 từ ở §9.6 bên dưới | `van prototype naar productie` trùng hoàn toàn thuật ngữ ngành cơ khí NL |

> 🔴 **Khối "Sản xuất" là bắt buộc, không phải tuỳ chọn.** `van prototype naar productie` là cách nói chuẩn trong ngành gia công kim loại/CNC ở Hà Lan. Không áp danh sách 218 từ đó, campaign N2 sẽ tiêu tiền vào người tìm xưởng gia công nhôm.

### 8.10. Landing page cho nhóm NL

Bốn trang tiếng Anh ở §10 **không dùng lại được** cho nhóm NL. Quảng cáo tiếng Hà Lan dẫn sang trang tiếng Anh làm tỉ lệ chuyển đổi sụt và Quality Score giảm.

| Campaign | Trang cần có | Ghi chú |
|---|---|---|
| `N1-NL-Service` | `/nl/mvp-laten-afmaken` | Trang quan trọng nhất. Phải nói rõ "làm nốt ≠ xây lại" ngay màn hình đầu |
| `N2-NL-AI-Tools` | `/nl/ai-app-laten-afmaken` | Nêu tên Lovable/Bolt/Replit trong phần nội dung, kèm disclaimer không liên kết |
| `N3-NL-Security` | `/nl/security-audit` | Dẫn nguồn cho con số 45%. Nhắc AVG chứ không nhắc GDPR |
| `N4-NL-Payments` | `/nl/betalingen-koppelen` | Nêu iDEAL trước Stripe |

Form liên hệ, email tự động và người trả lời đều phải bằng tiếng Hà Lan. Một lead Hà Lan nhận email trả lời tiếng Anh là lead gần như mất.

> ⚠️ **Nếu chưa có bốn trang tiếng Hà Lan này thì chưa bật nhóm N.** Bật B1–B3 trước (§11.2), làm trang NL song song, bật N sau.

---

<a id="9"></a>
## 9. Negative keywords theo từng thương hiệu

### 9.1. B1 Lovable — chống nhầm với từ điển & đồ lót

```
-bra          -bras         -lingerie     -underwear    -intimates
-panties      -meaning      -definition   -synonym      -synonyms
-antonym      -quotes       -quote        -song         -songs
-lyrics       -lyric        -movie        -film         -book
-novel        -doll         -plush        -toy          -baby
-babies       -pet          -pets         -dog          -cat
-name         -names        -spelling     -loveable
```

### 9.2. 🔴 B2 Bolt — danh sách quan trọng nhất trong toàn bộ plan

**Taxi / gọi xe / giao hàng** *(nguyên nhân nhiễu lớn nhất ở thị trường NL)*
```
-taxi         -rit          -ritje        -rides        -ride
-driver       -chauffeur    -bestuurder   -uber         -lyft
-food         -eten         -bezorging    -delivery     -courier
-scooter      -step         -fiets        -bike         -ebike
-rental       -huren        -verhuur      -promo code   -kortingscode
-fare         -tarief       -app store    -play store   -download app
```

**Phần cứng / bu lông / ốc vít**
```
-screw        -nut          -washer       -anchor       -fastener
-schroef      -moer         -bout         -m8           -m10
-stainless    -galvanized   -hex          -thread       -torque
-hardware store             -bouwmarkt    -gereedschap
```

**Người & thương hiệu khác**
```
-usain        -sprint       -olympic      -athletics    -record
-lightning    -thunder      -threads      -fabric       -mushroom
-disney       -cartoon      -movie        -game
```

**Xe điện & năng lượng**
```
-ev           -charger      -charging     -battery      -motorcycle
-motor        -vehicle      -car
```

### 9.3. B3 Replit — danh sách ngắn nhất

```
-tutorial     -course       -cursus       -learn        -teach
-classroom    -education    -student      -school       -homework
-python tutorial            -free hosting -100 days     -curriculum
```

### 9.4. Áp cho cả ba campaign

```
-free         -gratis       -crack        -cracked      -torrent
-jobs         -job          -vacature     -salary       -career
-reddit       -youtube      -github       -docs         -documentation
-alternative to             -vs           -review       -download
```

> ⚠️ **Cân nhắc `-vs` và `-review`.** Hai từ này chặn truy vấn so sánh, vốn có thể là khách tiềm năng ở giai đoạn cân nhắc. Nếu `AG-LOV-Migrate` cho tín hiệu tốt thì bỏ `-vs` ra khỏi B1.

### 9.5. Lưu ý kỹ thuật

1. **Negative keyword không tự khớp biến thể gần.** Phải nhập riêng `-taxi` **và** `-taxis`, `-rit` **và** `-ritten`.
2. **Từ đơn → negative broad · cụm nhiều từ → negative phrase.**
3. **Negative broad yêu cầu tất cả các từ cùng xuất hiện.** `-promo code` dạng broad chỉ chặn truy vấn có cả hai từ.
4. **Tạo 3 Shared Negative List riêng** (Lovable / Bolt / Replit) cộng 1 list chung, gắn đúng campaign. Đừng gộp — negative của Bolt gắn nhầm vào Replit sẽ chặn nhầm.

---

### 9.6. 🔴 Danh sách negative Sản xuất / Gia công — 218 từ

#### Vì sao cần danh sách này

Đây không phải negative "cho chắc". Định vị cốt lõi của LaunchStudio **trùng trực tiếp** với thuật ngữ chuẩn của ngành sản xuất:

| Từ trong keyword của bạn | Nghĩa trong phần mềm | Nghĩa trong sản xuất |
|---|---|---|
| **prototype** | bản dựng app bằng AI | mẫu vật lý: 3D print, CNC, mockup |
| **production** / **productie** | môi trường chạy thật | dây chuyền sản xuất hàng loạt |
| **prototype to production** | đưa app lên live | **NPI/DFM — đưa sản phẩm vật lý vào sản xuất loạt** |
| **build** / **bouwen** | lập trình | chế tạo, xây dựng |
| **custom / op maat** | phần mềm riêng | gia công theo đơn |
| **launch** | ra mắt app | ra mắt sản phẩm vật lý |

`prototype naar productie` và `prototype to production` là **cụm từ chuẩn trong ngành hardware**. Người tìm chúng có thể đang cần xưởng CNC, dịch vụ in 3D, hoặc nhà máy gia công hợp đồng, chứ không cần ai sửa app Lovable.

Với tài khoản chỉ mua được **69 click/tháng ở campaign lớn nhất** (§2.4), vài click lệch ở CPC €10–14 đã là 2–5% ngân sách tháng. Đây là danh sách có tác động lớn nhất trong §9.

#### 9.6.1. Vật liệu

```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```

#### 9.6.2. Gia công & chế tạo

```
-cnc          -frezen       -freesmachine -milling      -draaien
-draaibank    -turning      -verspanen    -verspaning   -machining
-lasersnijden -laser        -waterjet     -plasma       -zetten
-kanten       -bending      -buigen       -lassen       -welding
-laswerk      -plaatwerk    -sheet        -metaalbewerking
-gieten       -casting      -spuitgieten  -injection    -molding
-moulding     -extrusie     -extrusion    -matrijs      -matrijzen
-mold         -mould        -tooling      -stansen      -stamping
-ponsen       -slijpen      -grinding     -polijsten    -anodiseren
-anodizing    -poedercoaten -coating      -galvaniseren -stralen
-fabricage    -fabrication  -fabricatie
```

#### 9.6.3. In 3D / additive

```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```

> ⚠️ **Cân nhắc `-3d` ở dạng broad.** Nó chặn cả `3d` đứng một mình. Nếu LaunchStudio có khách làm app có mô hình 3D (configurator, viewer), thì bỏ `-3d` và chỉ giữ các cụm 2 từ.

#### 9.6.4. Prototyping vật lý — khối quan trọng nhất

```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```

#### 9.6.5. Doanh nghiệp sản xuất

```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```

#### 9.6.6. Mua/thuê máy móc

```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```

#### 9.6.7. Phần mềm CAD/CAM (danh mục phần mềm khác)

```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

#### 9.6.8. Nhà cung cấp ERP ngành (người tìm đối thủ, không phải tìm bạn)

```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```

#### 9.6.9. Xây dựng & gevelbouw

```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```

#### 9.6.10. Lưu ý kỹ thuật khi nhập vào Google Ads

1. **Negative keyword KHÔNG tự khớp biến thể gần.** Khác với keyword thường, negative không tự bắt số nhiều, lỗi chính tả hay dấu. Phải nhập riêng: `-machine` **và** `-machines`, `-matrijs` **và** `-matrijzen`.
2. **Từ đơn → negative broad; cụm nhiều từ → negative phrase.** `-cnc` để broad sẽ chặn mọi truy vấn có "cnc". `"-rapid prototyping"` để phrase.
3. **Negative broad yêu cầu tất cả các từ cùng xuất hiện.** `-machine kopen` dạng broad chỉ chặn truy vấn có **cả hai** từ. Muốn chặn chắc thì để phrase.
4. **Áp ở cấp tài khoản** (Shared Library → Negative keyword lists), không phải từng campaign — vì rủi ro `prototype`/`production` áp dụng cho mọi campaign.
5. **Kiểm tra trước khi áp:** dùng Search Terms Report để chắc chắn không có negative nào chặn nhầm truy vấn tốt. Ví dụ `-coating` có thể chặn `coating software` — nếu đó là khách tiềm năng thì bỏ.

---

<a id="10"></a>
## 10. Landing page

### 10.1. Bốn trang cần có

| URL | Cho campaign | Bắt buộc? |
|---|---|---|
| `/en/fix-lovable-app` | B1 (Hire + Problem) | **Bắt buộc** |
| `/en/fix-bolt-app` | B2 | **Bắt buộc** |
| `/en/fix-replit-app` | B3 (Hire + Problem) | **Bắt buộc** |
| `/en/replit-hosting-costs` | B3 (Cost) | Nên có |
| `/en/lovable-tanstack-migration` | B1 (Migrate) | Nên có |

### 10.2. Vì sao không dùng chung một trang

Với keyword thương hiệu, **message match quyết định tất cả**. Người gõ `fix replit app` bấm vào quảng cáo nói "Replit" rồi rơi vào trang chung nói "AI prototype to production" sẽ thoát ngay. Điều đó kéo cả Quality Score lẫn tỉ lệ chuyển đổi xuống.

Ba trang này **không cần viết lại từ đầu** — dùng chung khung, chỉ đổi:
- H1 và đoạn mở đầu nhắc đúng tên công cụ
- Phần "vấn đề thường gặp" liệt kê đúng lỗi của công cụ đó (§6.3 cho Bolt, §7.1 cho Replit)
- Một câu nêu rõ tính độc lập: *"LaunchStudio is an independent studio and is not affiliated with [tool]."*

### 10.3. Khung nội dung mỗi trang

| Phần | Nội dung |
|---|---|
| H1 | Nêu đúng vấn đề của công cụ đó |
| Đoạn mở | Bạn đã xây gì · vì sao nó chưa live được |
| Danh sách | 5–6 lỗi cụ thể của công cụ đó |
| Quy trình | 3 bước · thời gian 1–3 tuần |
| Giá | Từ €800, giá cố định |
| Tuyên bố độc lập | Một câu, rõ ràng |
| CTA | Báo giá miễn phí / code review miễn phí |

---

<a id="11"></a>
## 11. Ngân sách & lộ trình

### 11.1. Ngân sách

| | Tier A — Thăm dò | Tier B — Đề xuất | Tier C — Trần |
|---|---:|---:|---:|
| B1 Lovable | €150 | €250 | €400 |
| B2 Bolt | €60 | €120 | €200 |
| B3 Replit | €120 | €180 | €280 |
| *Cộng nhánh tiếng Anh* | *€330* | *€550* | *€880* |
| N1 NL Service | €100 | €150 | €300 |
| N2 NL AI-Tools | €40 | €60 | €90 |
| N3 NL Security | €40 | €60 | €120 |
| N4 NL Payments | €20 | €30 | €60 |
| *Cộng nhánh tiếng Hà Lan* | *€200* | *€300* | *€570* |
| **Tổng/tháng** | **€530** | **€850** | **€1.450** |

> 🔴 **BẢNG TRÊN ĐÃ LỖI THỜI — dữ liệu volume thật cho kết quả khác hẳn.** Trần chi tiêu thực tế tính từ volume đo được:
>
> | Campaign | Volume thật | Bảng trên cấp | Trần chi thật | Đề xuất mới |
> |---|---:|---:|---:|---:|
> | B1-Lovable | 110 | €250 | €30 | ┐ |
> | B2-Bolt | 120 | €120 | €32 | ├ gộp làm 1 campaign **€100–140** |
> | B3-Replit | 300 | €180 | €81 | ┘ |
> | N1-NL-Service | **1.280** | €150 | **€691** | **€400–550** |
> | N2-NL-AI-Tools | 10 | €60 | €5 | **tắt** |
> | N3-NL-Security | 50 | €60 | €27 | €40 |
> | N4-NL-Payments | **0** | €30 | €0 | **tắt** |
>
> **Tổng đề xuất mới: €540–730/tháng**, dồn vào nhánh tiếng Hà Lan. Lý do đầy đủ ở §2.8.

**Vì sao Bolt ngân sách thấp nhất dù volume cao nhất:** vì volume đó chưa được chứng minh là volume thật của bolt.new. Nâng ngân sách Bolt **chỉ sau khi** Search Terms Report sạch trong 2 tuần liên tiếp.

**Vì sao N1 là campaign NL duy nhất có trần cao (€300):** đây là nhóm duy nhất có cạnh tranh thật từ bureau Hà Lan, nghĩa là có volume thật để tiêu. N2–N4 volume rất thấp — đổ thêm tiền vào cũng không mua được thêm lượt hiển thị. Nếu `IS lost (budget)` của N2–N4 gần 0% thì ngân sách đã dư, đừng nâng.

> ⚠️ **Tier C €1.450/tháng vượt xa trần volume thật của tài khoản.** Trần chi tiêu tính bằng:
>
> ```
> Chi tiêu tối đa/tháng = Volume × %kw-hợp-ads × IS × CTR × CPC
>
> (IS = Impression Share — thị phần hiển thị · CTR = Click-Through Rate — tỉ lệ nhấp
>  CPC = Cost Per Click — chi phí mỗi lượt nhấp)
> ```
>
> Với volume đã đo được (§2.4), toàn bộ 157 keyword chỉ mua được **~100 click/tháng**, tương đương **€540–730/tháng**. Đặt cao hơn thì tiền không tiêu được — tài khoản này bị chặn bởi **volume**, không phải bởi ngân sách. Muốn tiêu nhiều hơn phải **mở rộng bề mặt keyword** (thêm cụm, thêm geo), chứ không phải tăng bid.
>
> Hệ quả thứ hai: với ~100 click/tháng, **đừng dùng Maximize Conversions**. Google cần 3–6 tháng mới đủ dữ liệu học. Dùng Manual CPC hoặc Maximize Clicks có trần.

### 11.2. Lộ trình 8 tuần — bật lần lượt, không bật cùng lúc

| Tuần | Việc |
|---|---|
| **0** | Chạy Keyword Planner cho 85 keyword, geo = EU-EN và NL riêng. **Cập nhật lại §11.1 bằng số thật.** Dựng 3 landing page. Tạo 4 Shared Negative List |
| **1** | Bật **B3 Replit** ở Tier A. Chỉ một campaign. Manual CPC |
| **2** | Kiểm Search Terms 2 ngày/lần, bổ sung negative. Đánh giá chất lượng truy vấn Replit |
| **3** | Bật **B1 Lovable** ở Tier A. Chạy song song bộ RSA A và B để so sánh |
| **4** | **Review 1.** So sánh Replit vs Lovable: CPC, CTR, chất lượng truy vấn. Nâng Tier A→B cho campaign nào có tín hiệu tốt |
| **5** | Bật **B2 Bolt** ở Tier A, **loại NL/BE khỏi geo**. Kiểm Search Terms **hàng ngày** |
| **6** | Đánh giá độ sạch truy vấn Bolt. Nếu > 30% truy vấn là taxi/bu lông → thắt chặt keyword về Exact hoặc tắt |
| **7** | Nếu Bolt sạch 2 tuần liên tiếp → cân nhắc mở lại geo NL/BE với negative đầy đủ |
| **8** | **Review 2.** Tính CPL thật cho từng thương hiệu. Dồn ngân sách vào thương hiệu thắng, cắt thương hiệu thua |

#### Nhánh tiếng Hà Lan — tuần 9–14

Nhóm N **không bật cùng nhánh tiếng Anh**, vì cần bốn landing page tiếng Hà Lan chưa tồn tại (§8.10).

| Tuần | Việc |
|---|---|
| **1–8** | *(song song)* Dựng 4 trang `/nl/…`. Chạy Keyword Planner cho 72 keyword NL, geo = Netherlands, ngôn ngữ = Dutch. Chuẩn bị email trả lời tự động bằng tiếng Hà Lan |
| **9** | Bật **N2-NL-AI-Tools** trước ở Tier A. Rẻ nhất, sạch nhất, không cạnh tranh — dùng để kiểm chứng toàn bộ đường dẫn NL (quảng cáo → trang → form → email) hoạt động |
| **10** | Bật **N3-NL-Security** và **N4-NL-Payments** ở Tier A. Kiểm Search Terms 2 ngày/lần — chú ý traffic webshop lọt vào N4 |
| **11** | Bật **N1-NL-Service** ở Tier A. Đây là campaign NL đắt nhất — kiểm Search Terms **hàng ngày** trong tuần đầu |
| **12** | **Review 3.** Đo tỉ lệ truy vấn "làm nốt" vs "xây mới" trong N1. Nếu > 70% là người muốn xây mới từ đầu → sửa landing page trước, đừng vội tắt |
| **13–14** | So sánh CPL nhánh EN vs nhánh NL. Dồn ngân sách về nhánh thắng |

> 💡 **Vì sao N2 bật trước dù volume thấp nhất:** nó rẻ đến mức lỗi vận hành không tốn tiền. Nếu form tiếng Hà Lan hỏng hoặc email trả lời ra tiếng Anh, bạn phát hiện ở campaign €40/tháng chứ không phải ở campaign €150/tháng.

### 11.3. Vì sao bật lần lượt chứ không cùng lúc

1. **Cô lập được nguyên nhân.** Nếu bật cả ba mà CPL xấu, bạn không biết thương hiệu nào gây ra.
2. **Học negative từ campaign sạch trước.** Replit dạy bạn cách đọc Search Terms trước khi đụng vào Bolt.
3. **Bảo vệ ngân sách.** Bolt là campaign duy nhất có thể đốt tiền nhanh — bật cuối cùng, khi đã quen quy trình.

---

<a id="12"></a>
## 12. KPI & ngưỡng dừng

### 12.1. Bảng KPI riêng cho plan thương hiệu

| Chỉ số | Tuần 4 | Tuần 8 | Ngưỡng dừng |
|---|---|---|---|
| **CPC** (Cost Per Click — chi phí mỗi lượt nhấp) | ≤ €12 | ≤ €10 | > €16 kéo dài 2 tuần |
| **CTR** (Click-Through Rate — tỉ lệ nhấp) | ≥ 5% | ≥ 8% | < 3% ở ad group nào đó |
| **Tỉ lệ truy vấn liên quan** | ≥ 70% | ≥ 85% | **< 50% ở B2 Bolt = tắt ngay** |
| **LP conversion** (tỉ lệ chuyển đổi trang đích) | ≥ 3% | ≥ 5% | < 2% sau 1 lần sửa |
| **CPL** (Cost Per Lead — chi phí mỗi khách tiềm năng) | ≤ €400 | ≤ €300 | > €500 |
| **QS** (Quality Score — điểm chất lượng) | ≥ 5 | ≥ 6 | < 4 = sửa landing page |

> **CTR kỳ vọng cao hơn plan thông thường** (8% thay vì 6–7%) vì keyword thương hiệu khớp truy vấn rất sát. Nếu CTR dưới 5% ở keyword thương hiệu thì gần như chắc chắn ad copy không nhắc đúng tên công cụ.

### 12.2. Chỉ số riêng của plan này: tỉ lệ truy vấn liên quan

Đây là chỉ số **không có trong Google Ads**, phải tính tay từ Search Terms Report:

```
Tỉ lệ truy vấn liên quan = Số truy vấn đúng về công cụ AI ÷ Tổng truy vấn
```

Với B2 Bolt đây là chỉ số sống còn. Cách tính hàng tuần:
1. Tải Search Terms Report của B2
2. Đánh dấu mỗi truy vấn: liên quan / taxi / bu lông / khác
3. Nếu nhóm "liên quan" < 50% → **tắt campaign**, không phải thêm negative

### 12.3. Quy tắc quyết định

| Tình huống | Hành động |
|---|---|
| B2 Bolt có < 50% truy vấn liên quan sau 2 tuần | **Tắt campaign.** Thêm negative không cứu được vấn đề cấu trúc |
| Ad group chi > €120, 0 conversion, sau 4 tuần | Tắt ad group |
| Bộ RSA B (không tên brand) có CTR cao hơn bộ A | Giữ bộ B, bỏ bộ A — tiết kiệm rủi ro chính sách |
| Google hạn chế ad text vì khiếu nại nhãn hiệu | Chuyển sang bộ RSA B **trong 24 giờ** |
| Một thương hiệu có CPL < €250, hai cái kia > €450 | Dồn toàn bộ ngân sách vào thương hiệu thắng |
| QS < 4 ở keyword thương hiệu | Landing page không khớp — sửa trang, đừng tăng bid |

---

<a id="13"></a>
## 13. Checklist trước khi bật

### Nghiên cứu & pháp lý

- [x] ~~Chạy Keyword Planner cho 157 keyword~~ — **đã xong 25/09/2026, kết quả ở §2**
- [ ] Chạy lại Keyword Planner lấy cột `Top of page bid (low/high)` — **CPC vẫn chưa có**, toàn bộ tính toán ở §2.7 đang dùng ước lượng €8–14
- [ ] Áp dụng 6 đề xuất tái cấu trúc ở §2.8 trước khi tạo campaign: tắt N4, tắt N2, gộp B1+B2+B3, nâng N1 lên €400–550
- [ ] Quyết định Hướng A hay Hướng B (§2.8) — đây là quyết định chiến lược, không phải cấu hình
- [ ] Xác minh `replit agency` = 210 bằng Exact match + Search Terms 1 tuần (§2.3)
- [ ] Chạy riêng geo **Netherlands** và geo **EU-EN** — so sánh để thấy mức nhiễu của Bolt
- [ ] **Cập nhật §11.1 bằng volume thật**
- [ ] Đối chiếu volume `mvp laten maken` vs `app laten maken` — nếu cả hai đều < 50/tháng thì hạ N1 về Tier A và giữ nguyên
- [ ] Đọc lại chính sách nhãn hiệu Google Ads bản hiện hành
- [ ] Xác nhận với luật sư/tư vấn nếu có ngân sách: vị thế "dịch vụ bổ trợ, không phải đối thủ" có đủ an toàn cho thị trường mục tiêu không

### Landing page

- [ ] `/en/fix-replit-app` đã live *(bật đầu tiên)*
- [ ] `/en/fix-lovable-app` đã live
- [ ] `/en/fix-bolt-app` đã live
- [ ] Mỗi trang có **một câu tuyên bố độc lập** rõ ràng

### Landing page tiếng Hà Lan *(chỉ cần trước tuần 9)*

- [ ] `/nl/ai-app-laten-afmaken` đã live *(bật đầu tiên trong nhánh NL)*
- [ ] `/nl/security-audit` đã live — **có dẫn nguồn cho con số 45%**
- [ ] `/nl/betalingen-koppelen` đã live — nêu iDEAL trước Stripe
- [ ] `/nl/mvp-laten-afmaken` đã live — nói rõ **"làm nốt ≠ xây lại"** ngay màn hình đầu
- [ ] Toàn bộ nội dung 4 trang là tiếng Hà Lan bản ngữ, **không phải dịch máy**
- [ ] Form liên hệ bằng tiếng Hà Lan
- [ ] Email trả lời tự động bằng tiếng Hà Lan
- [ ] Có người trả lời được tiếng Hà Lan khi lead phản hồi
- [ ] Dùng **AVG**, không dùng **GDPR**, trên toàn bộ trang NL
- [ ] Mỗi trang liệt kê **lỗi cụ thể của đúng công cụ đó**, không dùng chung một danh sách

### Trong Google Ads

- [ ] Tạo **6 Shared Negative List** trước khi tạo campaign: Lovable · Bolt · Replit · Chung · **NL-Chung** · **Sản xuất (218 từ, §9.6)**
- [ ] Gắn đúng list vào đúng campaign — **không gộp**
- [ ] **Ngôn ngữ campaign: B1–B3 = English · N1–N4 = Dutch.** Không campaign nào chọn cả hai
- [ ] N1: negative khối "App native" (`ios`, `android`, `native`…) — nếu không, ~1/3 truy vấn là app điện thoại
- [ ] N4: negative khối "Webshop" (`shopify`, `woocommerce`…) — `ideal koppelen` kéo rất nhiều traffic e-commerce
- [ ] N2: gắn list **Sản xuất** — `van prototype naar productie` trùng thuật ngữ ngành cơ khí Hà Lan
- [ ] `AG-NL-Bolt`: mọi keyword đều kèm chữ `new` hoặc `gebouwd met` — **không có keyword `bolt` đứng một mình**
- [ ] B2 Bolt: **loại NL, BE khỏi geo**
- [ ] Location targeting = **"Presence"**, không phải "Presence or interest"
- [ ] Bid strategy = **Manual CPC**
- [ ] Match type: Phrase là chính, Exact cho `[hire X developer]`. **Không có broad match nào**
- [ ] Ad rotation = **"Do not optimize"**
- [ ] Nạp **cả hai bộ RSA** (A và B) — bộ B tạm dừng, sẵn sàng bật
- [ ] Đặt lịch: Search Terms **hàng ngày cho B2 và N1**, 2 ngày/lần cho các campaign còn lại

---

## 📌 Tóm tắt

> **Hai nhánh ngôn ngữ, bảy campaign riêng, bật lần lượt — không bao giờ cùng lúc.**
>
> **Nhánh tiếng Anh (B1–B3)** bắt keyword lỗi kỹ thuật và tên công cụ — thứ người Hà Lan cũng gõ bằng tiếng Anh. **Nhánh tiếng Hà Lan (N1–N4)** bắt ý định thuê dịch vụ, tuân thủ AVG và thanh toán iDEAL — thứ chỉ tồn tại bằng tiếng Hà Lan. Mỗi campaign một thứ tiếng duy nhất cho cả keyword lẫn quảng cáo.
>
> Bắt đầu bằng **Replit** vì tên riêng sạch nhất và có pain point thương mại rõ (chi phí Reserved VM). Rồi **Lovable** vì nhiều keyword nhất và có cơ hội TanStack migration. **Bolt cuối cùng**, ngân sách thấp nhất, loại Hà Lan khỏi geo — vì ở thị trường chính của LaunchStudio, "Bolt" là hãng taxi lớn thứ hai.
>
> Mỗi ad group chuẩn bị **hai bộ RSA**: có tên thương hiệu để chạy, không tên thương hiệu để dự phòng nếu Google hạn chế. Google cho phép bid nhãn hiệu làm keyword; dùng trong ad text mới là chỗ có rủi ro.
>
> Chỉ số quyết định không phải CPC hay CTR mà là **tỉ lệ truy vấn liên quan**. Dưới 50% ở Bolt thì tắt, đừng cố cứu bằng negative.
>
> Bộ keyword Hà Lan **hẹp hơn có chủ đích**: 1 keyword sửa lỗi so với 30 ở bộ tiếng Anh, nhưng 60 keyword thuê dịch vụ so với 32. Người Hà Lan gõ lỗi bằng tiếng Anh và gõ nhu cầu bằng tiếng Hà Lan — bộ từ khoá phản ánh đúng điều đó chứ không dịch máy.

---

*157 keyword (85 EN + 72 NL) · 7 campaign · 18 ad group · 90 mục RSA (41 EN + 49 NL) đã kiểm giới hạn ký tự Google Ads bằng script (headline ≤ 30, description ≤ 90) — 0 vi phạm · Mỗi campaign một ngôn ngữ duy nhất · Volume cần verify bằng Keyword Planner trước khi chốt ngân sách*

*Toàn bộ keyword liệt kê đầy đủ trong tài liệu này: §5.1 (B1) · §6.2 (B2) · §7.2 (B3) · §8.2 (N1–N4) · §2.3 (những từ có volume > 0)*

*⚠️ **Volume đã đo (25/09/2026): 1.870 lượt/tháng cho cả 157 keyword, 106 từ bằng 0.** Luận điểm cốt lõi "làm nốt prototype AI" chỉ có 10 lượt/tháng. Ngân sách và thứ tự ưu tiên trong §11 đã lỗi thời — dùng §2.8 thay thế. CPC vẫn chưa đo.*
