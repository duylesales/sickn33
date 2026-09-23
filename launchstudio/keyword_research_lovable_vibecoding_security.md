# 🔍 Keyword Research — 3 Cụm Từ Khoá Mới cho LaunchStudio

> **Phạm vi:** 3 nhóm theo yêu cầu —
> ① Lovable issues (hosting, domain, Supabase, Stripe, export)
> ② Vibe coding assistance (Lovable, Bolt, Cursor, Replit)
> ③ Security & cleanup (gắn với service page)
>
> **Ngày:** 2026-09-23 · **Thị trường:** NL (chính) + EU-EN (phụ)
> **Liên quan:** [`launchstudio_info.md`](launchstudio_info.md) · [`seo_geo_plan_production_keywords.md`](seo_geo_plan_production_keywords.md) · [`extra-keywords.md`](extra-keywords.md)

---

## ⚠️ 0. Đọc trước: Dữ liệu này đáng tin đến đâu

**Điều mình KHÔNG làm được:** lấy volume tìm kiếm chính xác theo tháng. Việc đó cần Google Keyword Planner (tài khoản Ads đang chạy), Ahrefs hoặc Semrush. Mình không có quyền truy cập các công cụ đó.

**Điều mình ĐÃ làm:** xác minh nhu cầu bằng bằng chứng gián tiếp — mạnh hơn "đoán", yếu hơn số liệu thật:

| Bằng chứng | Ý nghĩa |
|---|---|
| Có ≥2 site thương mại xây trang riêng cho đúng truy vấn đó | Có người bỏ tiền/công đi rank → gần như chắc chắn có volume |
| Có gig Fiverr/Upwork bán đúng dịch vụ đó | Có nhu cầu thương mại thật, người mua đang tìm |
| Có trong tài liệu chính thức / FAQ của Lovable | Người dùng hỏi đủ nhiều để vendor phải viết |
| Chỉ suy ra từ pattern long-tail | Cần verify trước khi đầu tư |

**Ba tier trong các bảng dưới:**

- **🔴 A — Đã được xác minh:** nhiều đối thủ thương mại đang rank, hoặc có marketplace gig. Ưu tiên cao nhất.
- **🟡 B — Có tín hiệu:** 1–2 blog chuyên ngành hoặc tài liệu vendor đề cập. Nên làm.
- **🟢 C — Long-tail suy luận:** hợp lý về ngữ nghĩa nhưng chưa xác minh. Gom vào bài lớn, đừng làm bài riêng.

**Nguồn đã quét:** rapidevelopers.com/lovable-issues, afterbuildlabs.com/platforms/lovable-developer/problems, appstuck.com/blog (31 bài troubleshooting), docs.lovable.dev, lovable.dev/faq/domains, redwerk.com/services/vibe-code-cleanup, instinctools.com/vibe-code-audit-cleanup, pragmaticcoders.com vibe-coding-rescue, superblocks.com/blog/lovable-vulnerabilities, vibeappscanner.com, Fiverr/Upwork gigs.

---

## 📌 1. Ba phát hiện quan trọng trước khi chọn từ khoá

### 1.1. Volume nằm ở tên tool, không nằm ở từ trừu tượng

Đây là dữ liệu **thật** từ file [`keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv`](keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv) đã có sẵn trong repo (Google Keyword Planner, 2026-06-15):

| Keyword | Volume/tháng | Competition |
|---|---|---|
| `ai coding` | 1.600 | Medium |
| **`bolt ai`** | **1.300** | Medium |
| `ai secure` | 140 | Medium |
| `ai database` | 110 | Low |
| `ai prototype` | 20 | Medium |
| `ai security vulnerabilities` | 10 | Medium |
| `ai vulnerabilities` | 10 | High |
| `security for ai` | 10 | High |

**Kết luận rút ra:** từ khoá bảo mật trừu tượng (`ai security`, `ai vulnerabilities`) gần như **không có volume** — 10/tháng. Trong khi tên tool (`bolt ai` 1.300) thì có.

➡️ **Cụm ③ Security phải neo vào tên tool** (`lovable security`, `supabase rls`, `vibe coding security`), **không** neo vào `ai security audit`. Đây là lỗi mà plan cũ đang mắc: 14 keyword trong `extra-keywords.md` phần lớn là dạng trừu tượng volume thấp.

### 1.2. Chưa có service page để cụm ③ trỏ về

Mình đã kiểm tra `launchstudio.eu/en/` hôm nay: site vẫn là **one-page + anchor** (`#process`, `#calculator`, `#packages`, `#proof`, `#contact`) cộng blog `/insights/`. **Không có URL riêng nào** cho security, code audit, hay cleanup.

➡️ Yêu cầu của bạn "linked to the live service page" **hiện chưa thực hiện được** — page đó chưa tồn tại. Đây đúng là vấn đề mà [`seo_geo_plan_production_keywords.md`](seo_geo_plan_production_keywords.md) §1 đã nêu. Cụm ③ là cụm thương mại nhất trong 3 cụm, và nó đang không có đích đến. **Phải tạo page trước, viết bài sau** — nếu không thì backlink nội bộ và schema `Service` đều không có chỗ bám.

### 1.3. Kho bài hiện tại thiếu đúng loại intent đang có nhu cầu

Quét 1.522 slug tiếng Anh (đã bỏ bản social/Dutch) trong `2026/` + `2026-extra/`:

| Chủ đề | Số slug đã có | Nhận xét |
|---|---|---|
| security (chung) | 119 | Rất nhiều — nhưng **giáo dục**, không phải troubleshooting |
| lovable | 52 | Tốt |
| supabase | 25 | Tốt |
| bolt / cursor / replit | 23 / 18 / 16 | Tốt |
| hosting / deploy | 18 / 18 | Tốt |
| stripe | 13 | Ổn |
| domain | 9 | Mỏng |
| **rls** | **3** | Mỏng — trong khi đây là lỗ hổng nổi tiếng nhất của Lovable |
| **export** | **2** | Rất mỏng |
| **credits** | **0** | Trống hoàn toàn |
| slug dạng lỗi (`fix` / `broken` / `error`) | 37 | Đa số là "fixed price", không phải "fix lỗi" |

➡️ **Gap thật sự không phải thiếu bài, mà thiếu bài dạng "X không chạy — sửa thế nào".** Đối thủ (appstuck, rapidevelopers, afterbuildlabs, vibeappscanner) đang chiếm trọn mảng này. Đó là intent gần chuyển đổi nhất: người đang bị kẹt, đang cần thuê người sửa.

---

## 🧩 2. CỤM ① — Lovable Issues

> **Intent chủ đạo:** Troubleshooting (người dùng đang kẹt). **Giá trị:** cao — người tìm những từ này là khách hàng tiềm năng đang có prototype dở dang.
> **Loại trang:** bài blog dạng fix-guide → CTA sang service page.

### 2.1. Hosting & Deployment

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 1 | `lovable works in preview but not production` | 🔴 A | Fix | ❌ | Bài #1 nên làm. Đối thủ: appstuck, afterbuildlabs |
| 2 | `lovable environment variables not working` | 🔴 A | Fix | ❌ | appstuck có bài riêng. Nguyên nhân #1 của app AI chết khi deploy |
| 3 | `lovable deployment failed` | 🔴 A | Fix | ❌ | |
| 4 | `lovable hosting costs` | 🔴 A | Research | ⚠️ một phần | rapidevelopers có bài riêng. Gắn với €49/mo của LaunchStudio |
| 5 | `lovable deploy to vercel` | 🔴 A | How-to | ❌ | |
| 6 | `where are lovable apps hosted` | 🟡 B | Research | ✅ `01-where-lovable-apps-run-hosting-explained` | Đã có — cập nhật thêm |
| 7 | `lovable blank page after deploy` | 🟡 B | Fix | ❌ | |
| 8 | `lovable app slow in production` | 🟡 B | Fix | ❌ | appstuck: "Fixing Lovable Performance in Production" |
| 9 | `lovable build failed` | 🟡 B | Fix | ❌ | |
| 10 | `lovable publish not updating` | 🟢 C | Fix | ❌ | |
| 11 | `self host lovable app` | 🟡 B | Decision | ⚠️ | Liên kết tốt với cụm export |
| 12 | `move lovable app to own hosting` | 🟡 B | Decision | ⚠️ | |
| 13 | `lovable broken asset paths after deploy` | 🟢 C | Fix | ❌ | rapidevelopers có bài |
| 14 | `lovable netlify deploy error` | 🟢 C | Fix | ❌ | |

### 2.2. Custom Domain & DNS/SSL

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 15 | `lovable custom domain not working` | 🔴 A | Fix | ⚠️ gần | **≥5 site đang rank**: appstuck, melleprise, afterbuildlabs, mcstarters, rapidevelopers. Đây là keyword nóng nhất cụm ① |
| 16 | `lovable custom domain dns records` | 🔴 A | How-to | ✅ `02-lovable-custom-domain-dns-ssl-pitfalls` | Có rồi — nên tách bài riêng về DNS record cụ thể |
| 17 | `lovable ssl certificate not issued` | 🔴 A | Fix | ⚠️ | Lovable FAQ có trang riêng `/faq/domains/ssl` → nhu cầu đã được vendor xác nhận |
| 18 | `lovable cloudflare proxy dns only` | 🟡 B | Fix | ❌ | Nguyên nhân rất phổ biến: bật proxy cam thay vì DNS-only |
| 19 | `lovable a record 185.158.133.1` | 🟡 B | Fix | ❌ | Long-tail cực chính xác — người copy IP từ lỗi vào Google |
| 20 | `lovable domain verification failed` | 🟡 B | Fix | ❌ | |
| 21 | `lovable delete aaaa record` | 🟢 C | Fix | ❌ | |
| 22 | `lovable https not working` | 🟡 B | Fix | ❌ | |
| 23 | `connect godaddy domain to lovable` | 🟢 C | How-to | ❌ | Nhân bản theo registrar: GoDaddy / Namecheap / **TransIP / Versio / Hostnet** (NL) |
| 24 | `lovable dns propagation how long` | 🟢 C | Research | ❌ | |
| 25 | `transfer domain away from lovable` | 🟢 C | How-to | ⚠️ `lovable-custom-domain-migrating-a-live-domain-safely` | |

> 💡 **Ý tưởng NL-specific:** `lovable domein koppelen TransIP` / `Versio` / `Hostnet`. Ba registrar này chiếm thị phần lớn ở Hà Lan và **chưa ai viết**. Volume nhỏ nhưng cạnh tranh gần như bằng 0, và đúng thị trường chính của LaunchStudio.

### 2.3. Supabase (database / auth / RLS)

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 26 | `lovable supabase errors` | 🔴 A | Fix | ❌ | appstuck có bài tổng hợp |
| 27 | `lovable login not working after deploy` | 🔴 A | Fix | ❌ | afterbuildlabs liệt kê là problem riêng |
| 28 | `lovable oauth redirecting to localhost` | 🔴 A | Fix | ❌ | Lỗi kinh điển, rất dễ viết, rất dễ rank |
| 29 | `lovable supabase rls not enabled` | 🔴 A | Fix/Security | ⚠️ | **Cầu nối cụm ① ↔ ③** |
| 30 | `lovable supabase auth not working` | 🟡 B | Fix | ⚠️ | |
| 31 | `lovable database not saving data` | 🟡 B | Fix | ❌ | |
| 32 | `lovable supabase connection error` | 🟡 B | Fix | ❌ | |
| 33 | `lovable supabase migration error` | 🟡 B | Fix | ✅ `lovable-supabase-migrations-after-launch` | |
| 34 | `lovable edge function error` | 🟢 C | Fix | ❌ | |
| 35 | `lovable supabase storage upload not working` | 🟢 C | Fix | ❌ | |
| 36 | `connect lovable to external database` | 🟢 C | How-to | ❌ | rapidevelopers có bài |
| 37 | `lovable supabase realtime not working` | 🟢 C | Fix | ❌ | |

### 2.4. Stripe & Payments

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 38 | `lovable stripe integration not working` | 🔴 A | Fix | ⚠️ | appstuck: "Lovable Stripe Integration Stuck". afterbuildlabs: "Lovable Stripe integration broken?" |
| 39 | `add stripe to lovable app` | 🔴 A | How-to | ✅ `02-how-to-add-stripe-payments-ai-app` | Có rồi nhưng generic — nên có bản Lovable-specific |
| 40 | `lovable stripe webhook not firing` | 🟡 B | Fix | ❌ | Lỗi rất hay gặp, cực kỳ hợp LaunchStudio |
| 41 | `lovable stripe test mode to live` | 🟡 B | How-to | ❌ | |
| 42 | `lovable stripe checkout not working` | 🟡 B | Fix | ❌ | |
| 43 | `lovable payments vs stripe` | 🟡 B | Decision | ❌ | Lovable đã ra "Lovable Payments" built-in (yêu cầu Pro + Lovable Cloud) → so sánh là bài mới, chưa ai làm kỹ |
| 44 | `lovable stripe secret key exposed` | 🔴 A | Security | ❌ | **Cầu nối ① ↔ ③.** Có nguồn ghi nhận builder dán nhầm secret key thay vì publishable key |
| 45 | `lovable subscription billing setup` | 🟢 C | How-to | ⚠️ | |
| 46 | `lovable mollie integration` | 🟡 B | How-to | ❌ | **NL-specific.** Mollie là PSP chủ đạo ở Hà Lan, Lovable không hỗ trợ sẵn → khoảng trống rõ ràng, đúng thị trường |
| 47 | `lovable ideal payment` | 🟡 B | How-to | ❌ | **NL-specific.** iDEAL là phương thức thanh toán số 1 ở NL |

> 💡 **Đề xuất mạnh nhất của cụm này:** cặp `lovable mollie` + `lovable ideal`. Không đối thủ quốc tế nào viết (họ không quan tâm thị trường NL), nhưng mọi founder Hà Lan bán hàng đều cần iDEAL. Đây là lợi thế địa phương thuần tuý.

### 2.5. Export, GitHub & Lock-in

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 48 | `lovable export code` | 🔴 A | How-to | ❌ | rapidevelopers có bài. **Chỉ 2 slug trong kho có chữ "export"** → gap lớn |
| 49 | `lovable github sync not working` | 🔴 A | Fix | ❌ | appstuck có bài riêng |
| 50 | `how to download lovable project` | 🔴 A | How-to | ❌ | |
| 51 | `migrate off lovable` | 🔴 A | Decision | ✅ `migrate-lovable-production-grade-architecture` | afterbuildlabs: "How to migrate off Lovable to Next.js" |
| 52 | `lovable to nextjs` | 🟡 B | How-to | ⚠️ | |
| 53 | `lovable github integration` | 🟡 B | How-to | ❌ | |
| 54 | `do you own your lovable code` | 🟡 B | Research | ⚠️ | Gắn trực tiếp USP "100% code ownership" |
| 55 | `lovable vendor lock in` | 🟡 B | Decision | ⚠️ `no-code-lock-in-deciding-when-to-get-out` | |
| 56 | `lovable credits running out` | 🔴 A | Cost | ❌ | afterbuildlabs: "Lovable burning through credits with no progress?" — **0 slug trong kho nhắc "credits"** |
| 57 | `lovable pricing too expensive alternative` | 🟡 B | Decision | ⚠️ | |
| 58 | `lovable rollback to previous version` | 🟢 C | How-to | ❌ | |
| 59 | `lovable git version control` | 🟢 C | How-to | ❌ | |

---

## 🧩 3. CỤM ② — Vibe Coding Assistance (Lovable, Bolt, Cursor, Replit)

> **Intent chủ đạo:** hỗn hợp — nghiên cứu, so sánh, và tìm người giúp. **Loại trang:** blog (so sánh/giáo dục) + service page (intent thuê người).

### 3.1. Từ khoá lõi "vibe coding"

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 60 | `vibe coding` | 🔴 A | Research | ✅ nhiều | Head term, cạnh tranh cao, đã bão hoà |
| 61 | `what is vibe coding` | 🔴 A | Research | ✅ | |
| 62 | `vibe coding to production` | 🔴 A | Decision | ✅ `extra-1-from vibe coding to production/` | **Đây là định vị lõi của LaunchStudio** |
| 63 | `vibe coded app production ready` | 🔴 A | Decision | ⚠️ | |
| 64 | `vibe coding problems` | 🟡 B | Research | ⚠️ | |
| 65 | `vibe coding security risks` | 🔴 A | Security | ⚠️ | Cầu nối ② ↔ ③ |
| 66 | `hire vibe coding developer` | 🔴 A | **Thuê** | ❌ | → service page |
| 67 | `fix my vibe coded app` | 🔴 A | **Thuê** | ❌ | → service page |
| 68 | `vibe coding agency` | 🟡 B | **Thuê** | ❌ | → service page |
| 69 | `vibe coding limitations` | 🟢 C | Research | ⚠️ | |
| 70 | **`vibe coding Nederland`** | 🟡 B | Research | ❌ | NL. Đã có agency NL viết (Linku, Coding Agency, Kojac, Nordgard) → có nhu cầu tiếng Hà Lan |
| 71 | **`vibe coding beveiliging`** | 🟡 B | Security | ❌ | NL. Eenvoud.nl đã viết → tín hiệu có |
| 72 | **`prototype naar productie`** | 🟡 B | Decision | ⚠️ | NL. Từ khoá dịch vụ lõi bằng tiếng Hà Lan |

### 3.2. Bolt.new

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 73 | `bolt ai` | 🔴 A | Research | ✅ `02-bolt-ai` | **1.300/tháng (GKP thật)** — volume cao nhất trong toàn bộ nghiên cứu này |
| 74 | `bolt.new not working` | 🔴 A | Fix | ❌ | appstuck: "Fix the 10 Most Common Errors" |
| 75 | `bolt.new preview vs production` | 🔴 A | Fix | ❌ | |
| 76 | `bolt new bundle too large` | 🟡 B | Fix | ❌ | Lỗi đặc trưng của WebContainer |
| 77 | `bolt.new deploy netlify error` | 🟡 B | Fix | ❌ | |
| 78 | `bolt cors error production` | 🟡 B | Fix | ❌ | WebContainer same-origin → deploy là vỡ CORS |
| 79 | `bolt new supabase integration` | 🟡 B | How-to | ⚠️ | |
| 80 | `fix bolt app` | 🔴 A | **Thuê** | ❌ | Có site bán dịch vụ riêng (usamamoin.com/fix-bolt-app) |
| 81 | `bolt.new token limit` | 🟢 C | Cost | ❌ | |

### 3.3. Replit

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 82 | `replit not working` | 🔴 A | Fix | ❌ | appstuck có bài |
| 83 | `replit deployment failed` | 🔴 A | Fix | ⚠️ `replit-deployed-it-why-thats-not-launched` | |
| 84 | `replit agent not working` | 🔴 A | Fix | ⚠️ `replit-agent-code-review-before-you-ship` | appstuck: "Fix Stuck Loops and Errors" |
| 85 | `replit database connection error` | 🟡 B | Fix | ⚠️ `replit-and-supabase-wiring-a-database` | |
| 86 | `replit export to vercel` | 🔴 A | How-to | ⚠️ `moving-a-replit-app-to-your-own-infrastructure` | appstuck có bài riêng → nên tách |
| 87 | `replit app slow` | 🟢 C | Fix | ❌ | |
| 88 | `replit secrets not working in production` | 🟡 B | Fix | ⚠️ `replit-security-forks-secrets-and-public-projects` | |

### 3.4. Cursor

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 89 | `cursor rewriting loops` | 🔴 A | Fix | ❌ | appstuck: "Stop Agent Apply Loops" |
| 90 | `cursor not applying changes` | 🟡 B | Fix | ❌ | |
| 91 | `cursor ai code quality production` | 🟡 B | Research | ⚠️ | |
| 92 | `cursor vs lovable` | 🔴 A | So sánh | ✅ `02-lovable-vs-bolt-vs-cursor` | |
| 93 | `cursor agent security review` | 🟢 C | Security | ❌ | |

### 3.5. So sánh & intent thuê người (chuyển đổi cao nhất)

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 94 | `lovable vs bolt` | 🔴 A | So sánh | ✅ | |
| 95 | `lovable vs replit` | 🔴 A | So sánh | ✅ `bolt-cursor-or-replit-which-fits-which-founder` | |
| 96 | `best vibe coding tool 2026` | 🟡 B | So sánh | ⚠️ | |
| 97 | `lovable alternatives` | 🟡 B | So sánh | ⚠️ | |
| 98 | **`fix lovable app`** | 🔴 A | **Thuê** | ❌ | Fiverr/Upwork có hàng loạt gig đúng chữ này |
| 99 | **`lovable developer for hire`** | 🔴 A | **Thuê** | ❌ | |
| 100 | **`hire developer to finish ai app`** | 🔴 A | **Thuê** | ❌ | |
| 101 | **`take my lovable app to production`** | 🔴 A | **Thuê** | ⚠️ | |
| 102 | `lovable freelancer` | 🟡 B | **Thuê** | ❌ | |
| 103 | `bolt lovable replit deploy service` | 🟡 B | **Thuê** | ❌ | Đúng mô tả gig Fiverr đang bán |

> ⚠️ **Cảnh báo cạnh tranh:** nhóm "thuê người" (#98–103) đang bị Fiverr/Upwork chiếm SERP với giá $10–30. LaunchStudio (€800–€7.500) **không cạnh tranh bằng giá** — phải cạnh tranh bằng góc "tại sao gig $25 không sửa được lỗ hổng bảo mật" và bằng entity Manifera (11 năm, Vodafone/TNO/CFLW). Nếu viết bài dạng "so sánh thuê freelancer $25 vs studio" thì chính đối tượng này là người đọc.

---

## 🧩 4. CỤM ③ — Security & Cleanup (→ Service Page)

> **Intent chủ đạo:** thương mại. **Đây là cụm có giá trị đơn hàng cao nhất.**
> **Bắt buộc:** phải có service page trước. Xem §1.2 và §6.

### 4.1. Security neo theo tool (ưu tiên — có volume)

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 104 | `is lovable secure` | 🔴 A | Research | ⚠️ | Lovable tự viết `a-founders-guide-to-lovable-security` → vendor xác nhận nhu cầu |
| 105 | `lovable security vulnerabilities` | 🔴 A | Research | ✅ `05-lovable-security-holes-found-in-review` | ≥4 đối thủ: superblocks, shipsafe, vibeappscanner, nocode.mba |
| 106 | **`CVE-2025-48757`** | 🔴 A | Research | ❌ | **Entity keyword.** Lỗ hổng RLS của Lovable được báo cáo công khai. Volume thấp nhưng intent cực cao + giá trị entity/GEO lớn (LLM trích dẫn được) |
| 107 | `lovable rls vulnerability` | 🔴 A | Security | ⚠️ | Theo Superblocks dẫn nghiên cứu của Palmer: quét 1.645 project công khai, **170 (~10,3%) thiếu RLS**, lộ 303 endpoint |
| 108 | `supabase rls not enabled by default` | 🔴 A | Security | ⚠️ | Nguyên nhân gốc: Supabase tắt RLS mặc định khi tạo bảng |
| 109 | `supabase anon key exposed` | 🔴 A | Security | ✅ `04-supabase-service-role-key-exposure-risk` | |
| 110 | `supabase security checklist` | 🔴 A | Checklist | ⚠️ | unicoconnect, guardlayer đang rank |
| 111 | `supabase rls audit` | 🟡 B | Security | ⚠️ `rls-vs-application-layer-authorization` | **Chỉ 3 slug có "rls"** → gap |
| 112 | `lovable security scan` | 🟡 B | Tool | ❌ | vibeappscanner.com là công cụ đối thủ |
| 113 | `api key exposed in frontend` | 🟡 B | Security | ⚠️ | |
| 114 | `is my lovable app secure checklist` | 🟡 B | Checklist | ❌ | vibe-eval.com có bài |

### 4.2. Cleanup / Rescue (thương mại — xác minh mạnh nhất)

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 115 | **`vibe coding cleanup specialist`** | 🔴 A | **Dịch vụ** | ❌ | **≥4 agency có landing page riêng**: Redwerk, Suffescom, ThirdRock, AleaIT. Xác minh mạnh nhất trong toàn bộ nghiên cứu |
| 116 | **`vibe code cleanup`** | 🔴 A | **Dịch vụ** | ❌ | Redwerk + Lightning Kite có service page |
| 117 | **`vibe code audit`** | 🔴 A | **Dịch vụ** | ❌ | instinctools có service page |
| 118 | **`vibe coding rescue`** | 🔴 A | **Dịch vụ** | ❌ | Pragmatic Coders có service page |
| 119 | `clean up ai generated code` | 🟡 B | Dịch vụ | ⚠️ | |
| 120 | `ai generated code technical debt` | 🟡 B | Research | ⚠️ | |
| 121 | `refactor ai generated codebase` | 🟡 B | Dịch vụ | ⚠️ | |
| 122 | `fix ai generated codebase` | 🟡 B | Dịch vụ | ⚠️ | |
| 123 | `rescue failed mvp` | 🟡 B | Dịch vụ | ⚠️ | |
| 124 | `production readiness audit` | 🟡 B | Dịch vụ | ⚠️ | |
| 125 | `ai code review service` | 🟢 C | Dịch vụ | ⚠️ | |

### 4.3. Due diligence & compliance (đơn hàng lớn nhất)

| # | Keyword | Tier | Intent | Đã có bài? | Ghi chú |
|---|---|---|---|---|---|
| 126 | `technical due diligence ai generated code` | 🟡 B | Dịch vụ | ⚠️ | Redwerk nêu rõ: chuẩn bị cho Series A technical review |
| 127 | `code audit before investor due diligence` | 🟡 B | Dịch vụ | ⚠️ | Trigger cực mạnh — founder sắp gọi vốn |
| 128 | `enterprise security review ai app` | 🟡 B | Dịch vụ | ✅ `enterprise-vendor-onboarding-security-review-vs-package` | |
| 129 | `owasp llm top 10` | 🟡 B | Research | ⚠️ | Nguồn NL (Eenvoud, Coding Agency) đều nhắc → framework được công nhận ở NL |
| 130 | `gdpr compliance ai generated app` | 🟡 B | Compliance | ✅ nhiều | |
| 131 | **`AVG compliance AI app`** | 🟡 B | Compliance | ⚠️ | **NL.** "AVG" là tên GDPR ở Hà Lan — người Hà Lan tìm AVG chứ không tìm GDPR |
| 132 | **`beveiligingsaudit webapplicatie`** | 🟡 B | Dịch vụ | ❌ | NL |
| 133 | **`code audit laten uitvoeren`** | 🟡 B | Dịch vụ | ❌ | NL |
| 134 | **`pentest webapplicatie Nederland`** | 🟡 B | Dịch vụ | ❌ | NL — cạnh tranh với công ty pentest, nhưng góc "AI-gegenereerde app" thì trống |

---

## 🗂️ 5. Chiến lược ngôn ngữ: EN hay NL?

Dữ liệu cho thấy **hai tầng rõ rệt**, và nếu dịch máy móc toàn bộ sang tiếng Hà Lan thì sẽ lãng phí:

| Loại từ khoá | Ngôn ngữ nên dùng | Lý do |
|---|---|---|
| Lỗi kỹ thuật cụ thể (`lovable custom domain not working`) | **EN** | Founder Hà Lan copy nguyên văn thông báo lỗi tiếng Anh vào Google. Bản NL gần như 0 volume |
| Tên tool (`bolt ai`, `lovable vs cursor`) | **EN** | Tên riêng, không dịch |
| Khái niệm/giáo dục (`wat is vibe coding`) | **NL + EN** | Đã có ≥6 agency NL viết → có nhu cầu thật |
| Ý định thuê dịch vụ (`code audit laten uitvoeren`) | **NL ưu tiên** | Người mua dịch vụ ở NL tìm bằng tiếng mẹ đẻ |
| Compliance | **NL bắt buộc** | "AVG" ≠ "GDPR" trong thói quen tìm kiếm của người Hà Lan |
| Registrar/PSP địa phương (TransIP, Mollie, iDEAL) | **NL** | Không đối thủ quốc tế nào phục vụ |

➡️ **Quy tắc:** không dịch bài troubleshooting sang NL. Dịch bài dịch vụ, compliance, và bài địa phương.

---

## 🎯 6. Ưu tiên thực thi

### Bước 0 — Bắt buộc làm trước (không viết bài nào cho đến khi xong)

1. **Tạo service page thật** cho cụm ③. Đề xuất URL:
   - `launchstudio.eu/en/services/ai-app-security-audit/`
   - `launchstudio.eu/diensten/beveiligingsaudit-ai-app/` (NL)
2. Gắn schema `Service` + `Organization` + `FAQPage` (audit 2026-07-31 ghi nhận **chưa có `Organization` schema ở bất kỳ đâu**, và author schema đang là `"phu.lt"` — sửa luôn).
3. Mọi bài trong §4 trỏ nội bộ về page này.

### Bước 1 — 10 bài đầu tiên (tỉ lệ nỗ lực/kết quả tốt nhất)

| Ưu tiên | Keyword | Cụm | Lý do |
|---|---|---|---|
| 1 | `lovable custom domain not working` | ① | ≥5 đối thủ = volume chắc chắn; LaunchStudio có thể viết sâu hơn (DNS + SSL + Cloudflare + registrar NL) |
| 2 | `vibe coding cleanup specialist` | ③ | ≥4 agency có landing page; intent thương mại cao nhất |
| 3 | `lovable environment variables not working` | ① | Nguyên nhân #1 app AI chết khi deploy |
| 4 | `lovable works in preview but not production` | ① | Mô tả đúng "Last Mile Problem" của LaunchStudio |
| 5 | `lovable stripe integration not working` | ① | Trực tiếp dẫn tới gói dịch vụ payments |
| 6 | `lovable supabase rls not enabled` + `CVE-2025-48757` | ①→③ | Bài cầu nối; giá trị entity/GEO cao |
| 7 | `lovable export code` / `migrate off lovable` | ① | Kho chỉ có 2 slug "export" — gap lớn |
| 8 | `lovable credits running out` | ① | **0 slug** trong kho — gap hoàn toàn |
| 9 | `lovable mollie ideal` | ① NL | Không đối thủ, đúng thị trường NL |
| 10 | `lovable oauth redirecting to localhost` | ① | Lỗi kinh điển, dễ rank, người tìm đang rất bực |

### Bước 2 — Mở rộng

- Nhân bản mẫu "X not working — 10 lỗi thường gặp" cho **Bolt, Replit, Cursor** (mẫu đã được appstuck chứng minh hiệu quả).
- Cụm registrar NL: TransIP / Versio / Hostnet.
- Cụm due diligence (#126–128) — đơn hàng lớn nhất, ít cạnh tranh.

---

## ✅ 7. Cần verify trước khi tiêu tiền

Danh sách này dựa trên bằng chứng cạnh tranh, **không phải volume đo được**. Trước khi cam kết ngân sách lớn:

1. **Đưa 134 keyword trên vào Google Keyword Planner** (tài khoản Ads của LaunchStudio đã có — xem `google_ads_keywords_launchstudio.md`) ở chế độ *seed keywords*, không phải seed URL. File CSV hiện tại được seed bằng URL nên trả về rác (`day ai` 201.000/tháng là nhiễu, không liên quan gì đến LaunchStudio).
2. **Lọc theo geo NL + EU-EN riêng biệt** — volume EN toàn cầu sẽ đánh lừa.
3. **Đối chiếu Search Console** của 71 bài đang live: truy vấn nào đã có impression mà chưa có bài riêng → đó là mỏ vàng rẻ nhất.
4. **Kiểm tra SERP thủ công** với 10 keyword ở Bước 1: nếu top 10 toàn Fiverr/Reddit thì dễ chen vào; nếu toàn docs chính thức của Lovable thì khó.

---

*Nghiên cứu bởi: LaunchStudio content ops · Dữ liệu nền: quét web 2026-09-23 + GKP export 2026-06-15 + 1.522 slug hiện có*
