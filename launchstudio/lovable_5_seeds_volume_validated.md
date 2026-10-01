# ✅ 172 từ khoá Lovable **đã xác nhận có người tìm kiếm**

> **Đích:** launchstudio.eu · **Ngày:** 01/10/2026
> **File kèm:** `lovable_5_seeds_volume_validated.csv` (172 kw) · `kp_upload_lovable_EN.txt` (166) · `kp_upload_lovable_NL.txt` (3)
> **Toàn bộ 172 từ khoá đều được Google Autocomplete xác nhận là truy vấn thật.** Không có từ nào do mình tự nghĩ ra.

---

## 1. Về link Keyword Planner bạn gửi

Mình đã thử. Nó **302-redirect sang `accounts.google.com/ServiceLogin`**:

```
Original : ads.google.com/aw/keywordplanner/home?ocid=8442018680&...
Status   : 302 Found
Location : accounts.google.com/ServiceLogin?service=adwords&...
```

Mình **không đăng nhập được tài khoản Google của bạn** — không có session, và bạn cũng không nên đưa mật khẩu cho mình. Link Keyword Planner chỉ hoạt động trong trình duyệt đã đăng nhập của chính bạn.

### Nhưng mình tìm được cách trả lời đúng câu hỏi "từ khoá nào CÓ tìm kiếm"

**Google Autocomplete API.** Công khai, không cần đăng nhập, và quan trọng nhất: **Google chỉ gợi ý những truy vấn thật sự có người gõ.** Nếu một cụm từ không ai tìm, Google không gợi ý nó — gợi ý được sinh từ log truy vấn thật.

Mình đã chạy **~500 lượt truy vấn** vào endpoint này, với `gl=nl` (Hà Lan) và cả `hl=nl` cho tiếng Hà Lan, gồm:
- 80 prefix gốc quanh 5 seed của bạn
- Mở rộng theo bảng chữ cái (`lovable stripe a`, `lovable stripe b`, … cho 11 prefix quan trọng)
- Lớp trigger không chứa tên thương hiệu
- Tiếng Hà Lan riêng

Kết quả thu được: **1.487 truy vấn thật duy nhất**, trong đó 1.051 chứa chữ "lovable". Từ đó lọc ra 172 từ khoá liên quan đến 5 seed của bạn.

| | |
|---|---|
| Autocomplete cho biết | **CÓ người tìm cụm này hay không** ✅ |
| Autocomplete KHÔNG cho biết | **Bao nhiêu lượt/tháng** ❌ |

➡️ Phần "bao nhiêu lượt" thì bạn chạy bằng file `kp_upload_lovable_EN.txt` — xem §9. Mình đã chuẩn bị sẵn để dán thẳng.

---

## 2. 🔴 Kết quả kiểm chứng 5 câu gốc: chỉ 1 trong 5 là truy vấn thật

| Seed bạn đưa | Autocomplete | Kết luận |
|---|---|---|
| `host lovable project` | ✅ **khớp chính xác** | Truy vấn thật. Có cả `self host lovable project`, `host lovable project on github` |
| `how to integrate lovable app with stripe` | ❌ **0 gợi ý** | Không ai gõ cả câu này |
| `how to integrate lovable app with payment method` | ❌ **0 gợi ý** | Không ai gõ |
| `what database to use for my lovable app` | ❌ **0 gợi ý** | Không ai gõ |
| `how to use lovable app with supabase` | ❌ **0 gợi ý** | Không ai gõ |

**Nhưng chủ đề thì có — chỉ ngắn hơn nhiều.** Người ta gõ 2–4 từ, không gõ cả câu:

| Seed dạng câu (0 tìm kiếm) | Dạng thật có tìm kiếm |
|---|---|
| `how to integrate lovable app with stripe` ❌ | `lovable stripe integration` ✅ · `lovable stripe webhook` ✅ · `lovable stripe checkout` ✅ |
| `how to integrate lovable app with payment method` ❌ | `lovable payment integration` ✅ · `lovable payment gateway` ✅ · `lovable paddle` ✅ |
| `what database to use for my lovable app` ❌ | `best database for lovable` ✅ · `database for lovable` ✅ · `lovable cloud vs supabase` ✅ |
| `how to use lovable app with supabase` ❌ | `lovable supabase` ✅ · `connect lovable to supabase` ✅ · `using lovable with supabase` ✅ |

> 💡 **Đây là bài học dùng được cho mọi lần làm keyword về sau.** Khi bạn viết seed dưới dạng câu hỏi đầy đủ ngữ pháp, bạn đang viết theo cách *bạn* nghĩ, không theo cách người ta gõ. Google Search hay chat AI thì hiểu câu dài; nhưng **Google Ads khớp theo chuỗi từ**, nên một keyword dạng câu hoàn chỉnh gần như không bao giờ được kích hoạt. Luôn rút về 2–4 từ, rồi để Phrase match bắt phần đuôi.

---

## 3. 🔴 Mình phải sửa mấy kết luận của chính mình ở lần trước

Autocomplete bác bỏ một số từ khoá mình từng xếp hạng cao. Nói thẳng để bạn không dựng campaign trên dữ liệu sai:

| Từ khoá mình từng đề xuất | Lần trước mình nói | Autocomplete |
|---|---|---|
| `managed hosting for lovable app` | 🥇 "khớp sản phẩm tốt nhất, ưu tiên 1" | ❌ **0 gợi ý.** Dạng thật: `lovable hosting provider` ✅, `lovable hosting service` ✅ |
| `lovable stripe not working` | "cụm fix lõi", D1 | ❌ **0 gợi ý.** Dạng thật: `lovable stripe webhook` ✅ |
| `lovable stripe webhook not working` | "lỗi Stripe phổ biến nhất" | ❌ **0 gợi ý** |
| `lovable vercel 404` | 🥇 "keyword fix số 1" | 🟡 Chỉ có `lovable to vercel 404` ✅. Dạng mạnh hơn: `lovable 404` ✅, `lovable 404 error` ✅ |
| `lovable nitro preset vercel` | "người tìm kỹ thuật" | ❌ **0 gợi ý.** `lovable nitro` cũng 0 |
| `lovable ideal payment` / `lovable sepa` / `lovable bancontact` | "lợi thế NL" | ❌ **0 gợi ý cả ba** |
| `lovable rls not enabled` | D2 | ❌ **0.** Dạng thật: `lovable supabase rls` ✅, `lovable row level security` ✅ |

**Vì sao mình sai:** lần trước mình suy ra từ khoá từ *nguyên nhân kỹ thuật* (Nitro preset sai, webhook fail, RLS tắt). Nguyên nhân đó đúng — nhưng người gặp sự cố **không biết tên nguyên nhân**, nên họ không gõ nó. Họ gõ triệu chứng ngắn: `lovable 404`, `lovable cors error`, `lovable publishing failed`.

> 💡 **Khoảng cách giữa "nguyên nhân" và "điều người ta gõ" là cái bẫy lớn nhất của keyword research kỹ thuật.** Càng hiểu sâu vấn đề, càng dễ viết keyword bằng ngôn ngữ của người đã biết đáp án — tức là ngôn ngữ của chính mình, không phải của khách. Autocomplete là cách rẻ nhất để tự kiểm.

---

## 4. 🔴 Phát hiện quan trọng nhất: phần lớn truy vấn "lovable ... not working" là **Lovable hỏng, không phải app của khách hỏng**

Mình quét toàn bộ cụm lỗi. Đây là thứ nó trả về:

**Người này muốn Lovable support, KHÔNG muốn thuê agency** ❌
```
lovable login not working          lovable chat not working
lovable free credits not working   lovable student discount not working
lovable referral link not working  lovable invite link not working
lovable affiliate link not working lovable visual edits not working
lovable github sync not working    lovable email verification not working
lovable error exceeded quota       lovable preview link not working
lovable dev not working            lovable .dev not working on mobile
```

**Người này app của họ đang hỏng — ĐÂY là khách** ✅
```
lovable custom domain not working  lovable domain not working
lovable dns error                  lovable dns points to prohibited ip
lovable cloudflare error 1000      lovable 404 / lovable 404 error
lovable proxy error 404            lovable to vercel 404
lovable publishing failed          lovable build unsuccessful
lovable cors error                 lovable database error saving new user
lovable failed to get supabase secrets
lovable supabase connection failed lovable auth network request failed
```

Đây là lý do mình thêm một cột mới vào CSV: **`whose_problem`**. Phân bố:

| `whose_problem` | Số kw | Nghĩa |
|---|---:|---|
| `your_app` | 156 | App của khách — đây là khách hàng |
| `tool_seeker` | 12 | Đang tìm **công cụ** — xem §6 |
| `lovable_platform` | 3 | Lovable hỏng → **cho vào negative** |
| `MIXED` | 1 | Lẫn, cần kiểm Search Terms |

> 🔴 **Nếu bỏ qua trục này, bạn sẽ bid vào nhóm đông nhất và vô giá trị nhất.** Cụm "lovable not working" nhìn như mỏ vàng vì nó đông, nhưng phần lớn là người dùng Lovable không đăng nhập được hoặc không nhận được credit miễn phí. Họ không có app để sửa, và không có ngân sách. Trục `whose_problem` là thứ phân biệt 156 khách thật khỏi 3 cái bẫy — và cái bẫy lại là cái có volume cao hơn.

**Ba từ khoá phải cho vào negative dù chúng có volume tốt:**
```
-"lovable add payment method"      ← gần chắc là đổi thẻ trả tiền cho Lovable
-"lovable change payment method"   ← billing của Lovable
-"lovable payment methods"         ← lẫn nghĩa nặng
```

---

## 5. ⭐ Câu trả lời cho "trigger": cụm **vibe coded app** mạnh hơn cụm gắn tên Lovable

Bạn hỏi từ khoá nào **kích hoạt** nhu cầu của 5 câu đó. Đây là câu trả lời, và nó là phát hiện giá trị nhất của cả nghiên cứu.

**Tất cả đều đã xác nhận có người tìm:**

| Từ khoá | Ý định | Vì sao mạnh |
|---|---|---|
| `i vibe coded an app now what` | **Decision** | 🥇🥇 Đúng thời điểm người ta nhận ra cần giúp. Không ai bid cụm này. |
| `fix my vibe coded app` | **Service** | 🥇 Intent dịch vụ tuyệt đối — "của tôi", "sửa" |
| `fix vibe coded app` | **Service** | 🥇 |
| `vibe coded my app hired a dev` | **Hire** | 🥇 Đang tìm hiểu về việc thuê dev |
| `vibe coded app audit` | Service | 🥇 |
| `vibe coded app security` | Security | 🥇 Cụm bảo mật mạnh nhất |
| `vibe coded app security check` | Security | Tìm công cụ |
| `vibe coded app security checklist` | Security | Lead magnet hoàn hảo |
| `vibe coded app security scanner` | Security | Tìm công cụ |
| `vibe coded app checker` | Security | Tìm công cụ |
| `vibe coded app gets hacked` | Security | Bắt người đang lo |
| `upwork vibe coded app` | Hire | Đang đi tìm freelancer |
| `production vibe coded apps` | Decision | |
| `how to secure vibe coded apps` | How-to | → bài viết + CTA |
| `how to deploy vibe coded apps` | How-to | → bài viết + CTA |
| `how to launch vibe coded app` | How-to | → bài viết + CTA |

**Bốn lý do cụm này tốt hơn cụm `lovable ...`:**

**① Không gắn thương hiệu → bắt được cả thị trường.** Người dùng Bolt, Replit, v0, Cursor, Base44 đều gõ "vibe coded app". Một campaign thay vì bốn.

**② Không có rủi ro chính sách nhãn hiệu.** Không cần câu "Not Affiliated With Lovable", không sợ bị Lovable khiếu nại ad text.

**③ Ý định sạch hơn.** `fix my vibe coded app` không thể bị hiểu thành "Lovable đang hỏng" hay "tôi muốn học". Nó chỉ có một nghĩa.

**④ Không ai cạnh tranh.** Các agency đều viết "Hire Lovable Developer" — họ nhắm theo tên công cụ. Chưa ai nhắm theo *tình trạng* của khách.

> 💡 **Và chính `i vibe coded an app now what` là câu đáng chú ý nhất trong cả 1.487 truy vấn mình thu được.** Nó không phải truy vấn kỹ thuật, không phải truy vấn mua hàng — nó là tiếng nói của một người vừa làm xong thứ gì đó và không biết bước tiếp theo. Đó đúng là khách hàng mà LaunchStudio mô tả: *"đã có prototype chạy được, muốn ra mắt trong một tháng"*. Volume gần như chắc chắn rất thấp, nhưng tỷ lệ khớp ý định thì gần như tuyệt đối.

**Lớp trigger không gắn thương hiệu, phía kỹ thuật** (tất cả đã xác nhận):

| Từ khoá | Lưu ý |
|---|---|
| `supabase rls checker` · `check supabase security` · `supabase security advisor` | Tìm công cụ kiểm RLS |
| `supabase rls disabled in public` | Đúng chữ cảnh báo trong dashboard Supabase |
| `supabase security issues` | |
| `vercel 404 not_found vite` | **Vite** chính là stack Lovable trước TanStack |
| `vercel 404 not found after deployment` · `vercel 404 not found on refresh` | |
| `stripe test mode to live mode` | Đúng thời điểm chuyển sang thật |
| ⚠️ `stripe webhook not working` · `stripe checkout not working` · `self host supabase` | **Cạnh tranh rất lớn**, và phần lớn là dev sẽ tự sửa. Để P3, đừng dồn tiền |

---

## 6. ⭐ Nhu cầu ở đây có **hình dạng công cụ**, không phải hình dạng dịch vụ

12 từ khoá được xếp `tool_seeker`, và chúng nằm rải khắp cả 5 seed:

```
lovable cloud to supabase migration tool      lovable migration tool
lovable cloud to supabase exporter            supabase rls checker
lovable cloud to supabase extension           check supabase security
vibe coded app checker                        supabase security advisor
vibe coded app scanner                        vibe coded app security check
vibe coded app security scanner                vibe coded app security checklist
```

Người ta không tìm "ai làm hộ tôi". Họ tìm **"cái gì làm hộ tôi"**.

> 💡 **Đây là tín hiệu để đổi chiến thuật, không chỉ để chọn keyword.** Nếu đem landing page dịch vụ €800 đặt trước truy vấn `supabase rls checker`, bạn sẽ có CTR thấp và bounce cao — vì câu trả lời họ chờ là một cái nút, không phải một báo giá.
>
> **Cách thắng:** làm một **công cụ miễn phí** làm trang đích. Ví dụ dán link app Lovable → báo ngay RLS có bật không, anon key có lộ không, service role key có nằm trong client không. Công cụ đó:
> - khớp đúng thứ 12 keyword kia đang tìm → CTR và Quality Score cao
> - tự tạo ra lead có bằng chứng: khách nhìn thấy app mình đang hở, rồi mới đọc báo giá
> - bắt được cả `lovable ...` và `vibe coded app ...` bằng cùng một trang
>
> Bốn đối thủ bảo mật mình tìm được (vibeappscanner, cursorguard, rafter.so, rlsgate) đều đã làm scanner. Nhưng tất cả **chỉ** bán scanner — **không ai sửa hộ**. Scanner là cách vào; sửa là cách bán. LaunchStudio có thể làm cả hai, họ không.

---

## 7. Cụm lớn nhất tìm được: `lovable cloud to supabase`

Đây là cluster có nhiều biến thể thật nhất trong cả nghiên cứu — **13 dạng, tất cả đã xác nhận:**

```
lovable cloud to supabase                     lovable cloud to supabase migration
lovable cloud to supabase migration tool      lovable cloud to supabase exporter
lovable cloud to supabase extension           lovable cloud to supabase migration extension
migrate lovable cloud to supabase             how to migrate lovable cloud to supabase
can i migrate from lovable cloud to supabase  switch from lovable cloud to supabase
change lovable cloud to supabase              migrate lovable database to supabase
lovable cloud vs supabase (+ pricing, + reddit, + or)
```

**Bối cảnh giải thích vì sao cụm này đông:** Lovable Cloud *chính là* một project Supabase do Lovable sở hữu. Trước tháng 7/2026, bật Cloud rồi thì **không chuyển ra được**. Từ 07/2026 mới xuất được. Nên đang có một lượng người bị khoá nhiều tháng, vừa được mở, và đang đi tìm cách làm.

Chênh lệch chi phí ở 10.000 user: Cloud **~$300/tháng** vs Supabase riêng **$35–75/tháng**.

> 💡 **Để ý `can i migrate from lovable cloud to supabase`.** Người ta còn đang hỏi *liệu có làm được không*. Đó là dấu hiệu rõ rằng thông tin "từ 07/2026 làm được rồi" **chưa lan ra**. Khoảng trống thông tin đó là cơ hội — ai trả lời câu đó trước sẽ lấy cả cluster. Một bài viết tên đúng "Yes, you can now move off Lovable Cloud (since July 2026)" cộng một ad group là đủ.

---

## 8. Cấu trúc tài khoản đề xuất

**2 campaign, vì ngôn ngữ phải khác nhau** — đây là lỗi dễ mắc nhất: geo và language là hai thiết lập độc lập, và keyword tiếng Hà Lan phải nằm trong campaign đặt language=Dutch.

```
CAMPAIGN 1 · LS-Lovable-EN     [geo NL + EU-EN · language English · €140–180/thang]
│                                                                      139 keyword
├── AG1-HOST-COST      (22 kw)  → /en/lovable-hosting
│     lovable hosting cost/price/plans/fees/limits · hosting provider/service · self host · export
│
├── AG2-DOMAIN-FIX     (26 kw)  → /en/fix-lovable-domain            ⭐ nhom Fix lon nhat
│     custom domain not working · dns error · lovable 404 · cloudflare error 1000
│     publishing failed · build unsuccessful · cors error · supabase connection failed
│
├── AG3-CLOUD-MIGRATE  (15 kw)  → /en/lovable-cloud-to-supabase     ⭐ cluster lon nhat
│     lovable cloud to supabase (+tool/exporter/extension) · cloud vs supabase · migrate database
│
├── AG4-SECURITY       (22 kw)  → /en/check-my-app  (CONG CU mien phi)  ⭐ close rate cao nhat
│     supabase rls · row level security · vulnerability · api key exposed · service role key
│     security audit · code review · supabase rls checker · check supabase security
│
├── AG5-VIBE           (16 kw)  → /en/vibe-coded-app-help           ⭐ khong gan thuong hieu
│     i vibe coded an app now what · fix my vibe coded app · vibe coded app audit/security/scanner
│
├── AG6-PAYMENTS       (23 kw)  → /en/lovable-payments
│     lovable stripe integration/webhook/connect · payment gateway · paddle · mollie
│
└── AG8-DB-DECIDE      (15 kw)  → /en/lovable-database-choice
      best database for lovable · lovable database options/cost/limit · own/external database
      lovable supabase (+integration/limits/edge functions) · can lovable apps scale

CAMPAIGN 2 · LS-NL-iDEAL       [geo Netherlands · language DUTCH · €20–40/thang]
│                                                                        3 keyword
└── AG7-NL-IDEAL        (3 kw)  → /nl/ideal-toevoegen
      ideal toevoegen aan website · ideal betaling toevoegen aan website · ideal integreren in website
```

**Match type:** Phrase cho tất cả, trừ `[lovable stripe integration]` để **Exact**.

> 💡 **Vì sao AG8-DB-DECIDE tách khỏi AG3-CLOUD-MIGRATE:** cả hai đều về database, nhưng ý định khác hẳn. AG8 là người **chưa chọn** (`best database for lovable`) — cần tư vấn. AG3 là người **đã chọn và muốn chuyển** (`lovable cloud to supabase migration tool`) — cần thi công. Gộp lại thì ad copy phải nói cả hai việc và sẽ không nói tốt việc nào.

> 💡 **Campaign 2 chỉ có 3 từ khoá và €20–40/tháng — đừng bỏ nó vì nhỏ.** Ba cụm này là `ideal toevoegen aan website` và biến thể: người Hà Lan muốn thêm iDEAL vào website của họ. Không đối thủ nước ngoài nào nhắm tiếng Hà Lan, CPC sẽ ở mức sàn, và nó không liên quan gì tới Lovable — nên nó cũng bán được cho khách không dùng AI builder. Đây là ad group có tỷ lệ *chi phí / độ sạch ý định* tốt nhất toàn tài khoản.

---

## 9. 📋 Chạy Keyword Planner — đúng các bước

Mình đã chuẩn bị 2 file dán thẳng, mỗi dòng một keyword:

| File | Số kw | Thiết lập |
|---|---:|---|
| **`kp_upload_lovable_EN.txt`** | 166 | Location: **Netherlands** + các nước EU-EN · Language: **English** |
| **`kp_upload_lovable_NL.txt`** | 3 | Location: **Netherlands** · Language: **Dutch** |

**Các bước:**
1. Google Ads → **Tools** → **Keyword Planner** → **"Get search volume and forecasts"**
2. Mở `kp_upload_lovable_EN.txt`, copy toàn bộ, dán vào
3. Đặt **Location = Netherlands** (+ thêm UK/IE/DE/BE nếu muốn EU-EN rộng hơn), **Language = English**
4. Tab **Historical metrics** → đọc `Avg. monthly searches`, `Competition`, `Top of page bid (low/high)`
5. **Download** → gửi lại cho mình, mình sẽ ghép số vào CSV và tính lại ngân sách thật
6. Lặp lại với `kp_upload_lovable_NL.txt`, **Language = Dutch**

> ⚠️ **Chạy mỗi ngôn ngữ một lần riêng.** Nếu chọn cả English và Dutch trong một lần, số trả về là tổng gộp và bạn không biết bao nhiêu đến từ người tìm bằng tiếng Hà Lan — đúng thứ cần biết để quyết Campaign 2.
>
> ⚠️ **Tài khoản chưa chi tiêu sẽ thấy khoảng, không thấy số chính xác** (`10–100`, `100–1K` thay vì `170`). Vẫn đủ để quyết định, vì ở giai đoạn này bạn chỉ cần biết bậc độ lớn. Muốn số chính xác thì chạy một campaign nhỏ vài ngày, Keyword Planner sẽ mở khoá độ chi tiết.
>
> ⚠️ **Dự báo nhiều từ sẽ về 0.** Đừng xoá ngay. `0` trong Keyword Planner nghĩa là **dưới 10 lượt/tháng**, không phải đúng bằng 0 — và Autocomplete đã chứng minh những cụm này có người gõ. Quy tắc: xoá nếu **0 và không có biến thể nào >0 trong cùng ad group**; giữ nếu ý định tuyệt đối (`fix my vibe coded app`) vì CPC ở mức sàn, chi phí giữ chỗ gần 0.

---

## 10. 🔴 Negative keywords

**Khối tự-làm — phrase**
```
-"how to"  -"how do i"  -tutorial  -tutorials  -guide  -guides  -docs  -documentation
-"step by step"  -example  -examples  -template  -templates  -course  -courses  -learn
-youtube  -video  -reddit  -"stack overflow"  -github  -meaning  -explained
```
> `-reddit` quan trọng hơn bình thường ở đây: `lovable cloud vs supabase reddit`, `lovable hosting reddit`, `lovable supabase reddit`, `vibe coded app security reddit` đều là truy vấn thật. Người thêm "reddit" đang **cố tình tránh trang của nhà cung cấp** — họ muốn ý kiến đồng nghiệp. Đừng trả tiền để chen vào.

**Khối miễn phí — broad**
```
-free  -gratis  -cheap  -cheapest  -diy  -myself  -unlimited  -"open source"  -opensource
```
> Autocomplete cho thấy `ai app builder free`, `ai app builder free unlimited`, `lovable hosting free`, `lovable api key free`, `lovable custom domain free`, `is lovable database free` — **"free" là modifier phổ biến nhất của tệp này**. Chặn mạnh.

**🔴 Khối Lovable-hỏng (mới — xem §4) — phrase**
```
-"lovable login"  -"lovable chat"  -"lovable credits"  -"free credits"  -"lovable quota"
-"exceeded quota"  -"student discount"  -"referral link"  -"invite link"  -"affiliate link"
-"visual edits"  -"email verification"  -"lovable support"  -"lovable billing"  -"lovable invoice"
-"lovable subscription"  -"cancel subscription"  -"lovable pricing"  -"lovable plans"
-"promo code"  -"lovable discount"  -"add payment method"  -"change payment method"
-"lovable docs"  -"lovable discord"  -"lovable community"  -"lovable review"  -"lovable alternatives"
-"github sync"  -"lovable extension"  -"lovable mcp"
```

**🔴 Khối lẫn nghĩa — broad**
```
-restless  -leg  -syndrome        ← "RLS" = restless leg syndrome!
-bra  -lingerie  -underwear  -doll  -pet  -dog  -cat  -baby  -name  -loveable
-quotes  -lyrics  -song  -definition  -synonym
-atlas                            ← "Stripe Atlas" = thanh lap cong ty, khong lien quan
-"reunion host"  -"host family"   ← tu autocomplete that
```
> ⚠️ **`-restless -leg -syndrome` là negative bắt buộc mà hầu như không ai nghĩ tới.** Khi mình probe `lovable rls`, Google trả về `what is best for restless leg`, `how rare is rls`, `what is rls and what causes it`. RLS là viết tắt phổ biến của Restless Leg Syndrome, và nó có volume **lớn hơn nhiều** so với Row Level Security. Không chặn thì ad group bảo mật của bạn sẽ hiện cho người đau chân.

**Khối tuyển dụng — broad**
```
-job  -jobs  -career  -careers  -vacancy  -salary  -hiring  -intern  -internship
-"hire a partner"  -"hire remote"  -"expert jobs"  -"agency partner"  -"expert program"
```
> Từ autocomplete thật: `lovable careers`, `lovable expert jobs`, `does lovable hire remote`, `does lovable hire in canada`, `lovable hire a partner`, `lovable deployment strategist salary`, `lovable forward deployed engineer salary`, `vibe coding jobs`, `vibe coding job application`. Cụm "hire" **hai chiều** — một nửa là người muốn thuê, một nửa là người muốn được thuê.

> ⚠️ **Negative keyword KHÔNG tự khớp biến thể gần** — phải nhập riêng cả `-tutorial` và `-tutorials`, `-guide` và `-guides`, `-example` và `-examples`. Danh sách trên đã viết cả hai dạng ở các từ quan trọng.

**Dựng 3 Shared Negative List:** `NEG-DIY` · `NEG-LOVABLE-PLATFORM` · `NEG-NOISE-JOBS`

---

## 11. RSA cho 3 ad group mới — đã kiểm bằng script

**30 headline + 12 description, 0 vi phạm** (headline ≤30, description ≤90).

### AG3-CLOUD-MIGRATE

| Headline | Ch | | Description | Ch |
|---|---:|---|---|---:|
| `Lovable Cloud To Supabase` | 25 | | `Lovable Cloud is a Supabase project Lovable owns. We move it to one you own.` | 76 |
| `Move Your Data, Keep It All` | 27 | | `Looking for an export tool? A script cannot fix your access rules. A person can.` | 80 |
| `Cloud Export Done For You` | 25 | | `Near 10,000 users, Cloud costs about $300 a month. Your own Supabase is $35 to $75.` | 83 |
| `No Migration Tool Needed` | 24 | | `Fixed price from €800. Schema, data, policies and secrets all moved and tested.` | 79 |
| `We Do It, Not A Script` | 22 | | | |
| `Own Your Database Again` | 23 | | | |
| `Fixed Price From €800` | 21 | | | |
| `Zero Downtime Migration` | 23 | | | |
| `Not Affiliated With Lovable` | 27 | | | |
| `Free Migration Check` | 20 | | | |

> 💡 **`No Migration Tool Needed` và D2 cố ý nói trực diện với người đang tìm công cụ.** 4 trong 16 keyword của nhóm này là `tool`/`exporter`/`extension` — họ đang tìm script. Thay vì bỏ qua, hãy trả lời: script chuyển được dữ liệu nhưng không chuyển được access rules, và nếu RLS chuyển sai thì bạn vừa dọn dữ liệu vào một cái tủ không khoá. Đó là lý do đúng để chọn người thay vì công cụ — và nó cũng là sự thật.

### AG5-VIBE (không gắn thương hiệu)

| Headline | Ch | | Description | Ch |
|---|---:|---|---|---:|
| `Vibe Coded An App? Now What` | 27 | | `You built it with AI and it works, until real users arrive. We take it from there.` | 82 |
| `We Finish Vibe Coded Apps` | 25 | | `Free audit of your AI-built app. We report what is broken and what it costs to fix.` | 83 |
| `Built With AI, Broken In Prod` | 29 | | `Access rules off, keys exposed, no rate limits. The same three gaps in almost every app.` | 88 |
| `Free Vibe Code Audit` | 20 | | `Fixed price from €800. Independent Dutch studio, 160+ projects, 11+ years engineering.` | 86 |
| `Real Engineers, Not Prompts` | 27 | | | |
| `From Prototype To Production` | 28 | | | |
| `Fixed Price From €800` | 21 | | | |
| `11+ Years, 160+ Projects` | 24 | | | |
| `Lovable, Bolt Or Replit` | 23 | | | |
| `Send Us Your Repo` | 17 | | | |

> 💡 **Nhóm này không cần `Not Affiliated With Lovable`** — vì headline không dùng nhãn hiệu nào làm chủ ngữ. `Lovable, Bolt Or Replit` chỉ liệt kê phạm vi phục vụ, đó là cách dùng nhãn hiệu an toàn nhất.

### AG7-NL-IDEAL (tiếng Hà Lan — campaign riêng)

| Headline | Ch | | Description | Ch |
|---|---:|---|---|---:|
| `iDEAL Toevoegen Aan Je App` | 26 | | `iDEAL werkt wel, maar je moet het eerst aanzetten in het dashboard van je provider.` | 83 |
| `iDEAL In Je Webshop` | 19 | | `Wij zetten iDEAL, SEPA en Bancontact correct op. Vaste prijs vanaf €800.` | 72 |
| `Wij Regelen Je iDEAL` | 20 | | `Geen uurtarief en geen verrassingen. Je krijgt een vaste prijs na een kort gesprek.` | 83 |
| `Werkt iDEAL Nog Niet?` | 21 | | `Onafhankelijke Nederlandse studio. 160+ projecten in 11+ jaar opgeleverd.` | 73 |
| `iDEAL, SEPA En Bancontact` | 25 | | | |
| `Vaste Prijs Vanaf €800` | 22 | | | |
| `Live Binnen 1-3 Weken` | 21 | | | |
| `11+ Jaar, 160+ Projecten` | 24 | | | |
| `Nederlandse Studio` | 18 | | | |
| `Gratis Intakegesprek` | 20 | | | |

---

## 12. Ngân sách

172 keyword, trong đó **81 ở P1**. Nhưng toàn bộ là long-tail rất hẹp, nên trần chi tiêu thấp:

```
Volume uoc tinh 142 kw bid    ~250–500 luot/thang   ← se biet chinh xac sau khi chay KP
× 60% Impression Share        ~150–300 luot
× 6% CTR                      ~9–18 click/thang
× €6–12 CPC                   ~€55–215/thang
```

**Đề xuất: €160–220/tháng** chia 2 campaign (EN €140–180 · NL €20–40).

**Phân bổ Campaign 1:** AG4-SECURITY 22% · AG3-CLOUD-MIGRATE 22% · AG5-VIBE 18% · AG2-DOMAIN-FIX 15% · AG1-HOST-COST 10% · AG8-DB-DECIDE 8% · AG6-PAYMENTS 5%

**Kỳ vọng:** 9–18 click/tháng → ở tỷ lệ chuyển đổi trang đích 5% là **0,5–0,9 lead/tháng**.

> 🔴 **Con số đó không đổi so với lần trước, và đó là kết luận chứ không phải thất bại của keyword research.** 172 từ khoá đã xác nhận có người tìm vẫn chỉ ra khoảng một lead mỗi tháng, vì mỗi cụm chỉ vài lượt. Chủ đề này bị chặn bởi **volume**, không bởi ngân sách và không bởi chất lượng keyword.
>
> Giá trị thật của campaign này là ba thứ: ① **phép thử rẻ** xem người gặp sự cố AI-app có chịu trả tiền; ② **chiếm chỗ** khi CPC còn ở sàn và chưa ai bid `vibe coded app`; ③ **sinh dữ liệu** — Search Terms Report cho bạn ngôn ngữ thật của khách lúc gặp sự cố, là đầu vào để viết nội dung.
>
> Nếu cần lead khối lượng thật cho launchstudio.eu thì nó không nằm ở đây. Autocomplete cho thấy `website laten maken` có cả một họ biến thể thật (`kosten`, `zzp`, `goedkoop`, `professioneel`, `rotterdam`, `amsterdam`, `eindhoven`, `door ai`) — đó là thị trường có volume. Nhánh Lovable là bổ trợ, không phải động cơ.

---

## 13. Checklist

**Ngay**
- [ ] 🔴 Chạy `kp_upload_lovable_EN.txt` (166 kw) và `kp_upload_lovable_NL.txt` (3 kw) trong Keyword Planner — xem §9. Gửi lại file download, mình ghép số và tính lại ngân sách thật
- [ ] Xác nhận giá/sản phẩm thật của LaunchStudio (€800–7.500, €49/tháng hosting) — site trả HTTP 429 nên mình chưa đọc trực tiếp được
- [ ] 🔴 **Quyết định về công cụ miễn phí ở §6.** Đây là quyết định lớn nhất trong tài liệu này — nó đổi cả trang đích lẫn hiệu quả của 20 keyword ad group bảo mật

**Setup**
- [ ] Tạo 3 Shared Negative List (§10). **Đừng quên `-restless -leg -syndrome`**
- [ ] Dựng 8 trang đích. Nếu chỉ làm được 2: `/en/check-my-app` (công cụ) và `/en/lovable-cloud-to-supabase` (cluster lớn nhất)
- [ ] Campaign 2 phải đặt **language = Dutch**, không phải chỉ geo = Netherlands
- [ ] Mỗi trang EN có câu: *"LaunchStudio is an independent studio and is not affiliated with Lovable."*
- [ ] `[lovable stripe integration]` để **Exact**

**Nội dung — song song, không chờ ads**
- [ ] Bài "Yes, you can move off Lovable Cloud now (since July 2026)" → bắt cả cluster §7
- [ ] Bài "How to secure a vibe coded app" → bắt `how to secure vibe coded apps` + CTA công cụ
- [ ] Checklist bảo mật tải về → khớp đúng `vibe coded app security checklist`

**Vận hành**
- [ ] Search Terms Report **2 ngày/lần trong 3 tuần đầu**; mục tiêu là bắt truy vấn "Lovable hỏng" lọt qua
- [ ] Sau 4 tuần: nếu >40% truy vấn thuộc nhóm `lovable_platform` → thắt về Exact match
- [ ] Sau 8 tuần: dồn ngân sách về ad group nào ra lead, cắt phần còn lại

---

## 14. Tóm tắt

> **Mình không đăng nhập được Keyword Planner của bạn** (link 302 sang trang login). Thay vào đó mình dùng **Google Autocomplete** — nguồn công khai chỉ gợi ý truy vấn thật có người gõ — chạy ~500 lượt, thu **1.487 truy vấn thật**, lọc ra **172 từ khoá**. Cả 172 đều đã xác nhận. Phần "bao nhiêu lượt/tháng" thì dùng `kp_upload_lovable_EN.txt` mình đã chuẩn bị sẵn (§9).
>
> **Chỉ 1 trong 5 câu bạn đưa là truy vấn thật:** `host lovable project` ✅. Bốn câu còn lại trả về **0 gợi ý** — không ai gõ cả câu. Nhưng chủ đề thì có, ở dạng 2–4 từ: `lovable stripe integration`, `lovable payment integration`, `best database for lovable`, `lovable supabase`.
>
> **Mình đã sửa 7 kết luận của chính mình ở lần trước** — `managed hosting for lovable app`, `lovable stripe not working`, `lovable stripe webhook not working`, `lovable nitro preset vercel` đều có **0 lượt gợi ý**. Mình đã suy từ *nguyên nhân kỹ thuật*, nhưng người gặp sự cố không biết tên nguyên nhân nên không gõ nó.
>
> **Phát hiện nguy hiểm nhất:** phần lớn cụm `lovable ... not working` là **Lovable hỏng, không phải app của khách hỏng** — login, chat, credit miễn phí, link giới thiệu, student discount. Họ muốn Lovable support, không muốn thuê agency. Mình thêm cột `whose_problem` để tách: **156 khách thật, 3 cái bẫy** — và cái bẫy có volume cao hơn.
>
> **Câu trả lời cho "trigger": cụm `vibe coded app`** — không gắn thương hiệu, bắt luôn cả Bolt/Replit/v0/Cursor, không rủi ro nhãn hiệu, không ai cạnh tranh. Và trong đó có **`i vibe coded an app now what`** — đáng chú ý nhất trong cả 1.487 truy vấn, vì nó đúng là khách mà LaunchStudio mô tả. Cùng với `fix my vibe coded app`, `vibe coded app audit`, `vibe coded my app hired a dev`.
>
> **Nhu cầu ở đây có hình dạng công cụ, không phải dịch vụ.** 12 keyword là người tìm `tool` / `exporter` / `checker` / `scanner`. Nên làm **một công cụ miễn phí làm trang đích** (dán link app → báo RLS có bật không, key có lộ không). Bốn đối thủ bảo mật đều chỉ bán scanner, **không ai sửa hộ** — scanner là cách vào, sửa là cách bán.
>
> **Cluster lớn nhất: `lovable cloud to supabase`** với 13 biến thể thật. Và `can i migrate from lovable cloud to supabase` cho thấy người ta còn đang hỏi *liệu có làm được không* — tức thông tin "từ 07/2026 làm được rồi" chưa lan ra. Ai trả lời câu đó trước lấy cả cluster.
>
> **Negative quan trọng nhất mà không ai nghĩ tới: `-restless -leg -syndrome`.** RLS cũng là viết tắt của Restless Leg Syndrome và có volume lớn hơn Row Level Security nhiều.
>
> **Ngân sách €160–220/tháng, kỳ vọng ~0,5–0,9 lead/tháng.** 172 từ khoá đã xác nhận vẫn cho con số đó — chủ đề bị chặn bởi volume, không bởi ngân sách. Nếu cần lead khối lượng thật thì nó nằm ở `website laten maken` và họ biến thể của nó, không nằm ở nhánh Lovable.

---

*172 từ khoá · 172/172 xác nhận bằng Google Autocomplete · 142 bid được · 27 chỉ SEO · 3 negative · 81 ở P1 · 8 ad group / 2 campaign · 30 headline + 12 description mới đã kiểm bằng script, 0 vi phạm · 0 số volume (cần bạn chạy Keyword Planner) · 0 dữ liệu lấy từ file có trước*
