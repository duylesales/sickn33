# 🔍 Unico Connect — Phân nhóm keyword cho Google Search Ads

> **Website:** https://unicoconnect.com/ · Khảo sát ngày **2026-10-02**
> **Nguồn:** trang chủ, `/services`, `/hire` (đọc trực tiếp từ site, không phải giả định)

---

## 1. Doanh nghiệp bán gì

| | |
|---|---|
| **Định vị** | "Your AI-Native Technology Partner" — "From AI strategy to product in weeks" |
| **Dịch vụ chính** | AI development & AI agents, custom software, mobile/web app, no-code & low-code, cloud & DevOps, data analytics & BI |
| **No-code stack** | Xano, WeWeb, Webflow, Bubble, FlutterFlow, Supabase, Lovable |
| **Code stack** | React, Next.js, Node.js, Angular, Python, Java Spring Boot, Flutter, React Native, Swift, Kotlin, Shopify, WordPress |
| **AI stack** | LangChain, ChatGPT, Claude, Whisper |
| **Ngành** | Fintech, Healthcare, Real Estate, Travel, Education, Hospitality, E-Commerce, Legal Tech |
| **Vị trí** | HQ Mumbai (India) · Office Chicago (USA) · hoạt động 13+ quốc gia |
| **Giá** | Standard $25–50/giờ · AI/ML $30–60/giờ · Xano $30–50/giờ · Fixed scope tối thiểu **$10.000** · retainer tối thiểu 3 tháng |

### 🎯 Tín hiệu quan trọng nhất

Site **đã có landing page riêng cho từng role**: `/hire/xano-developer`, `/hire/lovable-developer`,
`/hire/weweb-developer`, `/hire/flutterflow-developer`… và từng service: `/services/mvp-development`,
`/services/agentic-ai`.

Đây là yếu tố quyết định nên chạy cụm nào — **cụm nào có trang đích khớp sẵn thì chạy được ngay**,
không phải chờ build landing page.

---

## 2. Bảng phân nhóm

| Nhóm | Keyword tiêu biểu | Intent | Cạnh tranh | Có LP sẵn | Kết luận |
|---|---|---|---|:---:|---|
| **A · No-code specialist** | `xano developer`, `hire weweb developer`, `bubble.io developer`, `flutterflow developer`, `hire webflow developer` | Mua, rất rõ | 🟢 Rất thấp | ✅ | ✅ **Chạy đầu tiên** |
| **B · MVP rescue / build** | `mvp development company`, `mvp development services`, `mvp rescue`, `fix my mvp`, `failed mvp` | Mua | 🟢 Thấp | ✅ | ✅ **Chạy** |
| **C · AI agent / GenAI** | `ai agent development company`, `agentic ai development`, `generative ai development company`, `langchain developer` | Mua, đang lên | 🟡 Trung–cao | ✅ | 🟡 Test nhỏ |
| **D · Industry app** | `fintech app development company`, `healthcare app development company`, `real estate app development company` | Mua | 🔴 Cao | ✅ | 🟡 Chỉ test 1 ngành |
| **E · Staff augmentation** | `hire react developer`, `dedicated development team`, `offshore development team`, `staff augmentation services` | Mua | 🔴 Rất cao | ✅ | ⛔ Khoan chạy |
| **F · Generic agency** | `app development company`, `software development company`, `mobile app development` | Mua nhưng loãng | 🔴 Cực cao | ✅ | ⛔ Tránh |
| **G · Brand** | `unico connect`, `unicoconnect` | Điều hướng | 🟢 Rất thấp | ✅ | ✅ Chạy phòng vệ |
| **H · SEO-only** | `chatgpt developer`, `claude developer`, `whisper developer`, `google workspace partner` | Gần như không có | — | ✅ | ⛔ Không chạy ads |

---

## 3. Vì sao A là cụm đáng chạy nhất

Volume tuyệt đối nhỏ, nhưng bốn yếu tố cộng lại thành cụm tốt nhất:

1. **Intent cực cao** — người gõ `hire xano developer` đã biết chính xác mình cần gì, không còn đang nghiên cứu
2. **Gần như không ai bid** — CPC thấp, không phải đấu với ngân sách triệu đô
3. **Specialist thật** — Unico làm đúng platform đó, không phải agency generic nhận mọi thứ
4. **Landing page khớp 1:1** — `/hire/xano-developer` cho đúng truy vấn `hire xano developer`

Ngược lại, cụm **E** và **F** là nơi Toptal, Turing, Arc, Upwork, Andela đang chi tiền lớn.
Lợi thế giá $25–50/giờ không cứu được auction đó: CPC ở US cho nhóm `hire <stack> developer`
nằm ở vùng hai chữ số, lead loãng, và người click thường đang so sánh 5 nhà cùng lúc.

---

## 4. Cấu trúc campaign đề xuất cho giai đoạn 1

| Campaign | Ad group | Keyword | Match | Landing page |
|---|---|---|---|---|
| `UC-Search-NoCode` | `AG-Xano` | `xano developer`, `hire xano developer`, `xano development agency`, `xano expert` | Phrase + Exact | `/hire/xano-developer` |
| | `AG-WeWeb` | `weweb developer`, `hire weweb developer`, `weweb agency` | Phrase + Exact | `/hire/weweb-developer` |
| | `AG-Bubble` | `bubble developer`, `bubble.io developer`, `hire bubble developer` | Phrase + Exact | `/hire/bubble-developer` |
| | `AG-FlutterFlow` | `flutterflow developer`, `hire flutterflow developer` | Phrase + Exact | `/hire/flutterflow-developer` |
| | `AG-Webflow` | `hire webflow developer`, `webflow development agency` | Phrase + Exact | `/hire/webflow-developer` |
| `UC-Search-Lovable` | `AG-Lovable` | `[lovable developer]`, `[hire lovable developer]`, `[lovable development agency]` | **Exact only** | `/hire/lovable-developer` |
| `UC-Search-MVP` | `AG-MVP-Build` | `mvp development company`, `mvp development services`, `hire mvp developer` | Phrase | `/services/mvp-development` |
| | `AG-MVP-Rescue` | `mvp rescue`, `fix my mvp`, `failed mvp`, `rescue failed mvp` | Phrase | `/services/mvp-development` |
| `UC-Search-Brand` | `AG-Brand` | `unico connect`, `unicoconnect` | Phrase | `/` |

**Geo:** US + UK + Canada + Australia · Ngôn ngữ English
**Match type:** không dùng broad match ở bất kỳ nhóm nào trong giai đoạn 1

---

## 5. ⚠️ Ba rủi ro phải xử lý trước khi bật

### 5.1. 🔴 `lovable` là một từ tiếng Anh thông thường

Bid phrase hay broad trên `lovable developer` sẽ ăn traffic kiểu *lovable gifts*, *most lovable dog
breeds*, *lovable characters*. Bắt buộc:

- Chỉ dùng **exact match**: `[lovable developer]`, `[hire lovable developer]`
- Tách thành **campaign riêng** để ngân sách không bị rò sang nhóm khác
- Negative: `gifts`, `dog`, `cat`, `quotes`, `meaning`, `movie`, `song`, `baby`, `names`

### 5.2. 🔴 Keyword chứa `developer` hút rất nhiều người tìm việc

Dev đang tìm job cũng gõ `xano developer`, `react developer`, `flutterflow developer`.
Đây là nguồn đốt ngân sách lớn nhất của cụm A. Shared negative list bắt buộc:

```
jobs          job           salary        career        careers
vacancy       vacancies     hiring        resume        cv
internship    intern        course        courses       tutorial
learn         learning      training      certification free
"how to become"   "remote jobs"    apply    recruitment  freelancer
```

### 5.3. 🟠 Fixed scope tối thiểu $10.000 — phải lọc người không đủ ngân sách

Retainer tối thiểu 3 tháng và fixed scope từ $10.000 nghĩa là khách nhỏ click vào là lỗ.
Nên đưa tín hiệu giá vào ad copy (ví dụ *"Projects from $10k"*) để tự lọc, và negative:
`cheap`, `cheapest`, `low cost`, `budget`, `under $500`, `free`.

---

## 6. Nhóm H — vì sao có trang nhưng không nên chạy ads

| Keyword | Lý do |
|---|---|
| `chatgpt developer`, `claude developer`, `whisper developer` | Gần như không ai search cụm này để **thuê người**. Trang tốt cho SEO, không phải mục tiêu ads. |
| `google workspace partner` | Hành trình mua khác hẳn (reseller/licensing), không khớp dịch vụ dev. |

---

## 7. ⚠️ Giới hạn của bản phân tích này

**Chưa có số volume và CPC thật.** Toàn bộ cột "Cạnh tranh" ở §2 là đánh giá định tính dựa trên
cấu trúc thị trường, **không phải số liệu đo được**. Mình cố ý không đưa con số volume tự nghĩ ra.

**Việc cần làm tiếp:** export Google Keyword Planner cho đúng geo (US/UK/CA/AU, English) với
seed list ở §4, rồi lọc theo volume + CPC thật. Khi có file CSV đó, có thể xếp hạng lại ưu tiên
và tính được trần ngân sách giống cách đã làm trong
[`../launchstudio/google_search_ads_master_plan.md`](../launchstudio/google_search_ads_master_plan.md) §2.

---

## 8. Việc tiếp theo

| # | Việc | Ai làm |
|---|---|---|
| 1 | Export Keyword Planner cho seed list §4 | Cần dữ liệu |
| 2 | Chốt ngân sách và trần CPC theo volume thật | Sau bước 1 |
| 3 | Viết RSA cho từng ad group ở §4 (15 headline + 4 description) | Làm được ngay |
| 4 | Dựng 3 shared negative list ở §5 | Làm được ngay |
| 5 | Kiểm tra conversion tracking trên site | Cần quyền truy cập |
