# 🇳🇱 Google Search Ads — Plan 3 Thương Hiệu AI, Toàn Bộ Tiếng Hà Lan
## B1 Lovable · B2 Bolt · B3 Replit → launchstudio.eu

> **Phạm vi:** Cùng cấu trúc 3 campaign / 8 ad group như bản tiếng Anh, nhưng **85 keyword đã dịch sang tiếng Hà Lan** và **toàn bộ quảng cáo viết bằng tiếng Hà Lan**.
> **Ngày:** 2026-09-28 · **Thị trường:** Netherlands · **Ngôn ngữ campaign:** Dutch
> **Tài liệu này tự chứa.** Keyword, RSA, extension, negative và lộ trình đều nằm trong đây.

> 🇳🇱 **Quy ước:** mọi keyword và nội dung quảng cáo giữ nguyên tiếng Hà Lan vì đó là thứ dán thẳng vào Google Ads. Nghĩa tiếng Anh nằm ở cột kế bên. **Không dịch khi nhập vào Google Ads.**

---

> # 🔴 ĐỌC TRƯỚC — GIẢ ĐỊNH MÀ PLAN NÀY DỰA VÀO
>
> Plan này được làm theo đúng yêu cầu: dịch 85 keyword của B1/B2/B3 sang tiếng Hà Lan và viết quảng cáo tiếng Hà Lan.
>
> **Nhưng dữ liệu đo được ngày 25/09/2026 nói ngược lại.** Trong đợt Keyword Planner trước, 24 keyword tiếng Hà Lan gắn tên công cụ AI (`lovable app laten afmaken`, `replit app live zetten`, `bolt new app laten afmaken`…) cho **tổng cộng 10 lượt tìm/tháng, 23/24 từ bằng 0**. Ba ad group `AG-NL-Lovable`, `AG-NL-Replit`, `AG-NL-AI-Afmaken` đều bằng 0 tuyệt đối.
>
> Lý do đã xác minh: **người Hà Lan gõ chuỗi lỗi kỹ thuật bằng tiếng Anh**, vì thông báo lỗi bản thân nó là tiếng Anh và dev copy-paste nguyên văn. Tìm nội dung tiếng Hà Lan về ba công cụ này chỉ trả về kết quả tiếng Anh.
>
> **Vì vậy plan này nên được coi là:**
> - ✅ **Một phép thử giá rẻ để chiếm chỗ** — nếu volume thật là 0 thì CPC ở mức sàn, chi phí giữ chỗ gần bằng không. Ngân sách đề xuất €90–150/tháng cho cả ba campaign.
> - ✅ **Tài sản sẵn sàng cho tương lai** — nếu nội dung tiếng Hà Lan về vibe coding phát triển trong 12–24 tháng tới, bạn đã có sẵn bộ keyword và quảng cáo.
> - ❌ **Không phải kênh chính.** Đừng cấp ngân sách như thể nó có volume. Verify bằng Keyword Planner (geo Netherlands, language Dutch) trước khi bật — xem §10.
>
> **Việc bắt buộc làm trước khi bật:** chạy Keyword Planner cho 85 keyword ở file `kp_upload_NL_translated.txt`. Nếu tổng volume < 100/tháng, chỉ bật B1 ở €50/tháng và bỏ B2/B3.

---

## 📑 Mục lục

| § | Nội dung |
|---|---|
| [1](#1) | Nguyên tắc dịch keyword — cái gì dịch, cái gì không |
| [2](#2) | Kiến trúc 3 campaign · 8 ad group |
| [3](#3) | Rủi ro riêng của bản tiếng Hà Lan |
| [4](#4) | Trùng lặp với bộ keyword NL đã có |
| [5](#5) | B1 · Lovable — keyword & RSA đầy đủ |
| [6](#6) | B2 · Bolt — keyword & RSA đầy đủ |
| [7](#7) | B3 · Replit — keyword & RSA đầy đủ |
| [8](#8) | Extension tiếng Hà Lan |
| [9](#9) | Negative keywords |
| [10](#10) | Ngân sách, lộ trình & KPI |
| [11](#11) | Checklist trước khi bật |

---

<a id="1"></a>
## 1. Nguyên tắc dịch keyword — cái gì dịch, cái gì không

Không phải từ nào cũng dịch. Dev Hà Lan trộn hai thứ tiếng theo quy luật rõ ràng:

| Loại từ | Xử lý | Ví dụ |
|---|---|---|
| **Động từ, tính từ, danh từ thường** | ✅ Dịch | `not working` → `werkt niet` · `failed` → `mislukt` · `cost` → `kosten` · `too expensive` → `te duur` |
| **Hành vi thương mại** | ✅ Dịch, ưu tiên cách nói NL | `for hire` → `inhuren` · `agency` → `bureau` · `development service` → `laten ontwikkelen` |
| **Tên sản phẩm & thương hiệu** | ❌ Giữ nguyên | `Lovable`, `Bolt.new`, `Replit`, `Supabase`, `Stripe`, `Netlify`, `Vercel`, `Next.js`, `TanStack` |
| **Thuật ngữ kỹ thuật dev không dịch** | ❌ Giữ nguyên | `deployment`, `RLS`, `SSR`, `CORS`, `secrets`, `agent`, `token`, `hosting`, `upgrade` |
| **Tên gói dịch vụ** | ❌ Giữ nguyên | `Reserved VM`, `Autoscale` |
| **Thuật ngữ nửa-nửa** | ⚠️ Cả hai đều dùng — chọn dạng NL nhưng ghi nhớ dạng EN | `environment variables` ↔ `omgevingsvariabelen` · `error` ↔ `foutmelding` |

**Ba cách dịch đáng chú ý:**

1. **`blank page` → `witte pagina`** (*white page*). Người Hà Lan nói "trang trắng" chứ không nói "trang trống". Dịch máy sẽ cho `blanco pagina` — không ai gõ thế.
2. **`agent stuck` → `agent loopt vast`** (*agent runs stuck*). `loopt vast` là thành ngữ chuẩn cho treo/đứng máy. `agent vast` là dịch máy.
3. **`fix` → `repareren` / `fixen`.** Dev Hà Lan dùng cả hai; `fixen` phổ biến hơn trong hội thoại, `repareren` phổ biến hơn khi gõ tìm kiếm. Keyword dùng `repareren`, quảng cáo dùng `fixen`.

> ⚠️ **Một keyword bị thay hẳn thay vì dịch.** `fix bolt app` không dịch thành `bolt app repareren` — cụm đó gần như chắc chắn khớp truy vấn về ứng dụng taxi Bolt. Đã thay bằng `app gebouwd met bolt new laten afmaken` (*have an app built with Bolt.new finished*): dài hơn, volume thấp hơn, nhưng không thể lẫn.

---

<a id="2"></a>
## 2. Kiến trúc 3 campaign · 8 ad group

```
TÀI KHOẢN LaunchStudio — nhánh tiếng Hà Lan cho 3 thương hiệu AI
│                                    [Toàn bộ: geo Netherlands · language Dutch]
├── B1 · LS-NL-Lovable                                    32 keyword
│   ├── AG-LOV-NL-Hire      (12) → /nl/lovable-app-laten-afmaken
│   ├── AG-LOV-NL-Problem   (11) → /nl/lovable-app-werkt-niet
│   └── AG-LOV-NL-Migrate    (9) → /nl/lovable-tanstack-migratie
│
├── B2 · LS-NL-Bolt                                       24 keyword
│   ├── AG-BOLT-NL-Hire      (8) → /nl/bolt-new-app-laten-afmaken
│   └── AG-BOLT-NL-Problem  (16) → /nl/bolt-new-deployt-niet
│
└── B3 · LS-NL-Replit                                     29 keyword
    ├── AG-REP-NL-Hire       (7) → /nl/replit-app-laten-afmaken
    ├── AG-REP-NL-Problem   (12) → /nl/replit-app-werkt-niet
    └── AG-REP-NL-Cost      (10) → /nl/replit-hosting-kosten
```

Cấu trúc giữ nguyên 1:1 so với bản tiếng Anh để so sánh được hiệu quả giữa hai ngôn ngữ trên cùng một ý định.

| Thiết lập | Giá trị | Lý do |
|---|---|---|
| Location | **Netherlands**, chế độ "Presence" | Không dùng "Presence or interest" |
| **Language** | **Dutch — chỉ Dutch** | Không thêm English, nếu không sẽ cạnh tranh nội bộ với nhánh EN |
| Match type | **Phrase** là chính · **Exact** cho 4 keyword rủi ro | Không có broad match nào |
| Bid strategy | **Manual CPC** | Volume dự kiến quá thấp cho Smart Bidding |
| Ad rotation | "Do not optimize" 4 tuần đầu | Thu dữ liệu công bằng |
| Networks | Search only | Tắt Display & Search Partners |

**Phân bố ý định** (giống bản tiếng Anh vì dịch 1:1):

| Ý định | Số keyword |
|---|---:|
| Fix (sửa lỗi) | 30 |
| Hire (thuê) | 17 |
| Service (dịch vụ) | 15 |
| How-to | 7 |
| Decision | 6 |
| Cost | 5 |
| Security | 3 |
| Research | 2 |

> ⚠️ **30/85 keyword là ý định Fix.** Đây chính là nhóm mà dữ liệu nói người Hà Lan gõ bằng tiếng Anh. Nếu sau 4 tuần nhóm `*-Problem` không có impression nào, tắt chúng và giữ lại chỉ nhóm `Hire` + `Cost` + `Migrate`.

---

<a id="3"></a>
## 3. Rủi ro riêng của bản tiếng Hà Lan

### 3.1. `gezocht` lẫn với tin tuyển dụng

`lovable developer gezocht` và `replit developer gezocht` (*developer wanted*) là **đúng cách viết tiêu đề tin tuyển dụng** ở Hà Lan. Người bấm vào có thể là developer đang tìm việc, không phải founder đang tìm người làm.

➡️ Cả hai để **Exact match** và bắt buộc negative: `vacature`, `vacatures`, `baan`, `werk`, `solliciteren`, `cv`, `salaris`, `zzp tarief`, `stage`, `traineeship`.

### 3.2. `bolt` vẫn là hãng taxi — kể cả trong tiếng Hà Lan

Rủi ro này **nặng hơn** ở bản tiếng Hà Lan, vì geo bắt buộc là Netherlands — chính là thị trường Bolt taxi hoạt động mạnh nhất (Amsterdam, Rotterdam, Den Haag, Utrecht). Bản tiếng Anh còn có lựa chọn loại NL/BE khỏi geo; bản này không.

➡️ **Ba quy tắc không thương lượng:**
1. Mọi keyword đều kèm `new` hoặc cụm `gebouwd met bolt new`
2. Toàn bộ negative list §9.2 áp **trước** khi campaign chạy phút đầu tiên
3. Đọc Search Terms **hàng ngày** trong 3 tuần đầu, không phải 2 ngày/lần

### 3.3. `naar productie` trùng thuật ngữ ngành cơ khí

Bốn keyword chứa `naar productie` hoặc `productieklaar`: `lovable app naar productie brengen`, `bolt new naar productie`, `replit app naar productie`, `lovable app productieklaar maken`.

`van prototype naar productie` là **cách nói chuẩn trong ngành gia công kim loại/CNC Hà Lan** (NPI/DFM). Không áp danh sách negative sản xuất, bốn keyword này sẽ kéo người tìm xưởng gia công nhôm.

➡️ **Bắt buộc gắn Shared Negative List "Sản xuất" (218 từ)** vào cả ba campaign. Toàn bộ 218 từ liệt kê đầy đủ ở §9.4 bên dưới.

### 3.4. `lovable werkt niet` — tính từ tiếng Anh trong câu tiếng Hà Lan

`lovable` vẫn là tính từ tiếng Anh nghĩa "đáng yêu" và là thương hiệu đồ lót toàn cầu. Trong câu tiếng Hà Lan `lovable werkt niet` rủi ro thấp hơn bản tiếng Anh `lovable not working`, nhưng vẫn cần negative đồ lót/từ điển ở §9.1.

---

<a id="4"></a>
## 4. Trùng lặp với bộ keyword NL đã có

Bốn keyword trong bản dịch này **đã tồn tại** trong `keyword_seeds_3_ai_brands_NL.csv` (bộ NL gốc, campaign N1–N4):

| Keyword | Trong bộ NL cũ | Trong bản dịch này | Xử lý |
|---|---|---|---|
| `lovable developer nederland` | `AG-NL-Lovable` | `AG-LOV-NL-Hire` | Giữ ở **bản dịch này**, xoá khỏi N2 |
| `lovable alternatief` | `AG-NL-Lovable` | `AG-LOV-NL-Migrate` | Giữ ở **bản dịch này** (khớp ý định Migrate hơn) |
| `weg van replit` | `AG-NL-Replit` | `AG-REP-NL-Cost` | Giữ ở **bản dịch này** (cùng nhóm với `te duur`) |
| `replit app naar eigen server` | `AG-NL-Replit` | `AG-REP-NL-Cost` | Giữ ở **bản dịch này** |

> 🔴 **Hai keyword giống nhau trong hai campaign cùng geo + cùng ngôn ngữ sẽ cạnh tranh nội bộ.** Google chọn một, thường là cái có Ad Rank cao hơn, và bạn mất quyền kiểm soát xem quảng cáo nào hiển thị. Phải xoá ở một bên trước khi bật.
>
> Vì bản dịch này bao trùm toàn bộ `AG-NL-Lovable` và `AG-NL-Replit` của bộ cũ — và hai ad group đó đo được **0 volume** — đề xuất: **tắt hẳn campaign N2-NL-AI-Tools** và để bản dịch này thay thế.

---

<a id="5"></a>
## 5. B1 · Lovable · `B1-NL-Lovable` — 32 keyword

### 5.1. `AG-LOV-NL-Hire` — 12 keyword · Max CPC €12,00

**Ý định thuê — người chủ động tìm người làm** · Landing page: `/nl/lovable-app-laten-afmaken`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `lovable app repareren` | `fix lovable app` | Phrase | Hire | P1 |
| `lovable developer inhuren` | `lovable developer for hire` | Phrase | Hire | P1 |
| `lovable developer gezocht` | `hire lovable developer` | Exact | Hire | P1 |
| `lovable developer nederland` | `lovable developer` | Phrase | Hire | P1 |
| `lovable app laten ontwikkelen` | `lovable app development service` | Phrase | Hire | P1 |
| `lovable app naar productie brengen` | `take my lovable app to production` | Phrase | Service | P1 |
| `lovable app productieklaar maken` | `lovable app production ready` | Phrase | Service | P1 |
| `mijn lovable app laten afmaken` | `finish my lovable app` | Phrase | Service | P2 |
| `lovable audit laten uitvoeren` | `lovable audit service` | Phrase | Service | P1 |
| `lovable beveiligingsaudit` | `lovable security audit` | Phrase | Service | P1 |
| `lovable app bureau` | `lovable app agency` | Phrase | Hire | P2 |
| `lovable freelancer` | `lovable freelancer` | Phrase | Hire | P2 |

#### RSA — `AG-LOV-NL-Hire` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Lovable App Laten Afmaken?` | Want your Lovable app finished? | 26 | **P1** |
| H2 | `Lovable Developer Inhuren` | Hire a Lovable developer | 25 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H4 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H5 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H6 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H7 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H8 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H9 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H10 | `Security, Stripe En Hosting` | Security, Stripe and hosting | 27 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Code Review` | Free code review | 18 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Met Lovable gebouwd maar niet live? Wij regelen security, betalingen en hosting.` | Built with Lovable but not live? We handle security, payments and hosting. | 80 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |
| D4 | `Geen uurtarief en geen verrassingen. Vraag vandaag een gratis review aan.` | No hourly rate, no surprises. Request a free review today. | 73 |

### 5.2. `AG-LOV-NL-Problem` — 11 keyword · Max CPC €9,00

**Sự cố — app không chạy được** · Landing page: `/nl/lovable-app-werkt-niet`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `lovable app werkt niet` | `lovable app not working` | Phrase | Fix | P2 |
| `lovable deployment mislukt` | `lovable deployment failed` | Phrase | Fix | P2 |
| `lovable preview versus productie` | `lovable preview vs production` | Phrase | Fix | P2 |
| `lovable eigen domein werkt niet` | `lovable custom domain not working` | Phrase | Fix | P2 |
| `lovable stripe integratie` | `lovable stripe integration` | Phrase | Fix | P1 |
| `lovable inloggen werkt niet` | `lovable login not working` | Phrase | Fix | P2 |
| `lovable supabase rls` | `lovable supabase rls` | Phrase | Security | P2 |
| `is lovable veilig` | `is lovable secure` | Phrase | Research | P2 |
| `lovable werkt niet` | `lovable not working` | Phrase | Fix | P2 |
| `lovable stripe werkt niet` | `lovable stripe not working` | Phrase | Fix | P1 |
| `lovable beveiligingslekken` | `lovable security vulnerabilities` | Phrase | Research | P2 |

#### RSA — `AG-LOV-NL-Problem` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Lovable App Werkt Niet?` | Lovable app not working? | 23 | **P1** |
| H2 | `Wij Fixen Lovable Apps` | We fix Lovable apps | 22 | **P2** |
| H3 | `Deployment Mislukt?` | Deployment failed? | 19 |  |
| H4 | `Eigen Domein Werkt Niet?` | Custom domain not working? | 24 |  |
| H5 | `Stripe Koppeling Kapot?` | Stripe connection broken? | 23 |  |
| H6 | `Inloggen Werkt Niet?` | Login not working? | 20 |  |
| H7 | `Supabase RLS Goed Ingesteld` | Supabase RLS set up properly | 27 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H12 | `Gratis Foutanalyse` | Free fault analysis | 18 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Werkt je Lovable app niet? Wij vinden de oorzaak en lossen het definitief op.` | Lovable app not working? We find the cause and fix it for good. | 77 |
| D2 | `Preview werkt maar live niet? Dat is bijna altijd configuratie, niet je code.` | Preview works but live doesn't? That's almost always config, not your code. | 77 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 5.3. `AG-LOV-NL-Migrate` — 9 keyword · Max CPC €11,00

**Rời nền tảng — TanStack, Next.js, self-host** · Landing page: `/nl/lovable-tanstack-migratie`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `weg van lovable` | `migrate off lovable` | Phrase | Decision | P1 |
| `lovable migratie laten uitvoeren` | `lovable migration service` | Phrase | Service | P1 |
| `lovable tanstack migratie` | `lovable tanstack migration` | Phrase | Service | P1 |
| `lovable naar tanstack migreren` | `migrate lovable to tanstack` | Phrase | Service | P1 |
| `lovable ssr upgrade` | `lovable ssr upgrade` | Phrase | Service | P1 |
| `lovable code exporteren` | `lovable export code` | Phrase | How-to | P2 |
| `lovable app zelf hosten` | `self host lovable app` | Phrase | Decision | P2 |
| `lovable naar nextjs` | `lovable to nextjs` | Phrase | How-to | P2 |
| `lovable alternatief` | `lovable alternative` | Phrase | Decision | P2 |

#### RSA — `AG-LOV-NL-Migrate` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Weg Van Lovable?` | Moving away from Lovable? | 16 | **P1** |
| H2 | `Lovable Naar TanStack` | Lovable to TanStack | 21 | **P2** |
| H3 | `Of Naar Next.js` | Or to Next.js | 15 |  |
| H4 | `Wij Migreren Je Code` | We migrate your code | 20 |  |
| H5 | `Zelf Hosten Zonder Lock-in` | Self-host without lock-in | 26 |  |
| H6 | `SSR Voor Betere SEO` | SSR for better SEO | 19 |  |
| H7 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H8 | `Klaar In 1-3 Weken` | Done within 1-3 weeks | 18 |  |
| H9 | `Code 100% Van Jou` | Code 100% yours | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H12 | `Gratis Migratiescan` | Free migration scan | 19 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Lovable draait sinds mei 2026 op TanStack. Oude projecten migreren niet mee.` | Lovable has run on TanStack since May 2026. Old projects don't migrate along. | 76 |
| D2 | `Geen SSR betekent slechte SEO. Wij migreren je app naar een moderne stack.` | No SSR means poor SEO. We migrate your app to a modern stack. | 74 |
| D3 | `Vaste prijs vanaf €800. Je code exporteren en zelf hosten, zonder lock-in.` | Fixed price from €800. Export your code and self-host, without lock-in. | 74 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |


---

<a id="6"></a>
## 6. B2 · Bolt · `B2-NL-Bolt` — 24 keyword

### 6.1. `AG-BOLT-NL-Hire` — 8 keyword · Max CPC €10,00

**Ý định thuê — LUÔN kèm `new`** · Landing page: `/nl/bolt-new-app-laten-afmaken`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `bolt new app repareren` | `fix bolt new app` | Phrase | Hire | P1 |
| `bolt new developer inhuren` | `hire bolt new developer` | Exact | Hire | P1 |
| `bolt new developer nederland` | `bolt new developer` | Phrase | Hire | P1 |
| `bolt new naar productie` | `bolt new to production` | Phrase | Service | P1 |
| `bolt new app productieklaar` | `bolt new app production ready` | Phrase | Service | P1 |
| `bolt new bureau` | `bolt new agency` | Phrase | Hire | P2 |
| `app gebouwd met bolt new laten afmaken` | `fix bolt app` | Phrase | Service | P1 |
| `bolt new app developer` | `bolt app developer` | Exact | Hire | P3 |

#### RSA — `AG-BOLT-NL-Hire` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Bolt.new App Laten Afmaken?` | Want your Bolt.new app finished? | 27 | **P1** |
| H2 | `Bolt.new Developer Inhuren` | Hire a Bolt.new developer | 26 | **P2** |
| H3 | `Voor Bolt.new Bouwers` | For Bolt.new builders | 21 |  |
| H4 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H5 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H6 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H7 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H8 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H9 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H10 | `Geen Partner Van Bolt.new` | Not affiliated with Bolt.new | 25 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Build Review` | Free build review | 19 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Met Bolt.new gebouwd maar niet live? Wij fixen env vars, CORS en de build.` | Built with Bolt.new but not live? We fix env vars, CORS and the build. | 74 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D3 | `Wij zijn geen partner van Bolt.new. Wel de studio die je app live krijgt.` | We're not Bolt.new's partner. We are the studio that gets your app live. | 73 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 6.2. `AG-BOLT-NL-Problem` — 16 keyword · Max CPC €8,00

**Sự cố — preview chạy, production vỡ** · Landing page: `/nl/bolt-new-deployt-niet`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `bolt new werkt niet` | `bolt new not working` | Phrase | Fix | P2 |
| `bolt new preview versus productie` | `bolt new preview vs production` | Phrase | Fix | P2 |
| `bolt new productiefout` | `bolt new production error` | Phrase | Fix | P2 |
| `bolt new deployment` | `bolt new deployment` | Phrase | Fix | P2 |
| `bolt new deploy foutmelding` | `bolt new deploy error` | Phrase | Fix | P2 |
| `bolt new omgevingsvariabelen` | `bolt new environment variables` | Phrase | Fix | P2 |
| `bolt new cors foutmelding` | `bolt new cors error` | Phrase | Fix | P3 |
| `bolt new bundel te groot` | `bolt new bundle too large` | Phrase | Fix | P3 |
| `bolt new netlify deployen` | `bolt new netlify deploy` | Phrase | Fix | P3 |
| `bolt new supabase` | `bolt new supabase` | Phrase | How-to | P3 |
| `bolt new stripe` | `bolt new stripe` | Phrase | How-to | P3 |
| `bolt new eigen domein` | `bolt new custom domain` | Phrase | Fix | P3 |
| `bolt new witte pagina` | `bolt new blank page` | Phrase | Fix | P3 |
| `bolt new code exporteren` | `bolt new export code` | Phrase | How-to | P2 |
| `bolt new token limiet` | `bolt new token limit` | Phrase | Cost | P3 |
| `bolt new beveiliging` | `bolt new security` | Phrase | Security | P2 |

#### RSA — `AG-BOLT-NL-Problem` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Bolt.new Deployt Niet?` | Bolt.new not deploying? | 22 | **P1** |
| H2 | `Preview Werkt, Live Niet?` | Preview works, live doesn't? | 25 | **P2** |
| H3 | `Wij Fixen CORS En Env` | We fix CORS and env vars | 21 |  |
| H4 | `Bundel Te Groot?` | Bundle too large? | 16 |  |
| H5 | `Witte Pagina Na Deploy?` | Blank page after deploy? | 23 |  |
| H6 | `Omgevingsvariabelen Kwijt?` | Environment variables lost? | 26 |  |
| H7 | `Netlify Of Vercel` | Netlify or Vercel | 17 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Bolt.new` | Not affiliated with Bolt.new | 25 |  |
| H12 | `Gratis Build Review` | Free build review | 19 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Bolt.new preview is geen productie. Wij fixen env vars, CORS en buildfouten.` | Bolt.new preview is not production. We fix env vars, CORS and build errors. | 76 |
| D2 | `Witte pagina na deploy? Meestal ontbrekende omgevingsvariabelen. Wij fixen het.` | Blank page after deploy? Usually missing env variables. We fix it. | 79 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |


---

<a id="7"></a>
## 7. B3 · Replit · `B3-NL-Replit` — 29 keyword

### 7.1. `AG-REP-NL-Hire` — 7 keyword · Max CPC €11,00

**Ý định thuê** · Landing page: `/nl/replit-app-laten-afmaken`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `replit app repareren` | `fix replit app` | Phrase | Hire | P1 |
| `replit developer inhuren` | `replit developer for hire` | Phrase | Hire | P1 |
| `replit developer gezocht` | `hire replit developer` | Exact | Hire | P1 |
| `replit app naar productie` | `replit app to production` | Phrase | Service | P1 |
| `replit app developer nederland` | `replit app developer` | Phrase | Hire | P2 |
| `replit bureau` | `replit agency` | Phrase | Hire | P2 |
| `replit productieklaar` | `replit production ready` | Phrase | Service | P1 |

#### RSA — `AG-REP-NL-Hire` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit App Laten Afmaken?` | Want your Replit app finished? | 25 | **P1** |
| H2 | `Replit Developer Inhuren` | Hire a Replit developer | 24 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H4 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H5 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H6 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H7 | `Security En Betalingen` | Security and payments | 22 |  |
| H8 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H9 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H10 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Deploy Review` | Free deploy review | 20 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Met Replit gebouwd maar niet live? Wij regelen deploy, security en hosting.` | Built with Replit but not live? We handle deploy, security and hosting. | 75 |
| D2 | `Van Replit Agent-prototype naar een app die je klanten echt kunnen gebruiken.` | From a Replit Agent prototype to an app your customers can actually use. | 77 |
| D3 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 7.2. `AG-REP-NL-Problem` — 12 keyword · Max CPC €8,00

**Sự cố — Agent, secrets, database** · Landing page: `/nl/replit-app-werkt-niet`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `replit app werkt niet` | `replit app not working` | Phrase | Fix | P2 |
| `replit deployment mislukt` | `replit deployment failed` | Phrase | Fix | P2 |
| `replit deployment foutmelding` | `replit deployment error` | Phrase | Fix | P2 |
| `replit database verbindingsfout` | `replit database connection error` | Phrase | Fix | P2 |
| `replit agent werkt niet` | `replit agent not working` | Phrase | Fix | P3 |
| `replit secrets werken niet` | `replit secrets not working` | Phrase | Fix | P3 |
| `replit eigen domein` | `replit custom domain` | Phrase | Fix | P3 |
| `replit beveiliging` | `replit security` | Phrase | Security | P2 |
| `replit werkt niet` | `replit not working` | Phrase | Fix | P3 |
| `replit agent loopt vast` | `replit agent stuck` | Phrase | Fix | P3 |
| `replit app is langzaam` | `replit app slow` | Phrase | Fix | P3 |
| `replit app crasht` | `replit app crashes` | Phrase | Fix | P3 |

#### RSA — `AG-REP-NL-Problem` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit App Werkt Niet?` | Replit app not working? | 22 | **P1** |
| H2 | `Wij Fixen Replit Apps` | We fix Replit apps | 21 | **P2** |
| H3 | `Agent Loopt Vast?` | Agent getting stuck? | 17 |  |
| H4 | `Deployment Mislukt?` | Deployment failed? | 19 |  |
| H5 | `Database Verbindingsfout?` | Database connection error? | 25 |  |
| H6 | `Secrets Werken Niet?` | Secrets not working? | 20 |  |
| H7 | `App Crasht Of Traag?` | App crashing or slow? | 20 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H12 | `Gratis Foutanalyse` | Free fault analysis | 18 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Werkt je Replit app niet? Wij vinden de oorzaak en lossen het definitief op.` | Replit app not working? We find the cause and fix it for good. | 76 |
| D2 | `Agent loopt vast, secrets werken niet, database valt weg? Wij fixen het.` | Agent stuck, secrets failing, database dropping out? We fix it. | 72 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 7.3. `AG-REP-NL-Cost` — 10 keyword · Max CPC €10,00

**Chi phí — Reserved VM, migration** · Landing page: `/nl/replit-hosting-kosten`

| Keyword (Nederlands) | Nghĩa / gốc tiếng Anh | Match | Ý định | Ưu tiên |
|---|---|---|---|---|
| `replit reserved vm kosten` | `replit reserved vm cost` | Phrase | Cost | P1 |
| `replit autoscale versus reserved vm` | `replit autoscale vs reserved vm` | Phrase | Decision | P1 |
| `replit deployment kosten` | `replit deployment cost` | Phrase | Cost | P1 |
| `replit te duur` | `replit pricing too expensive` | Phrase | Cost | P1 |
| `weg van replit` | `migrate off replit` | Phrase | Decision | P1 |
| `replit naar vercel exporteren` | `replit export to vercel` | Phrase | How-to | P2 |
| `replit code exporteren` | `replit export code` | Phrase | How-to | P2 |
| `replit hosting kosten` | `replit hosting cost` | Phrase | Cost | P2 |
| `replit alternatief voor productie` | `replit alternative production` | Phrase | Decision | P2 |
| `replit app naar eigen server` | `move replit app to own server` | Phrase | Service | P1 |

#### RSA — `AG-REP-NL-Cost` (toàn bộ tiếng Hà Lan)

| # | Headline (Nederlands) | Nghĩa tiếng Anh | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit Te Duur Geworden?` | Replit become too expensive? | 24 | **P1** |
| H2 | `Reserved VM Kosten Hoog?` | Reserved VM costs high? | 24 | **P2** |
| H3 | `Wij Verhuizen Je App` | We move your app | 20 |  |
| H4 | `Naar Je Eigen Server` | To your own server | 20 |  |
| H5 | `Of Naar Vercel` | Or to Vercel | 14 |  |
| H6 | `Autoscale Of Reserved?` | Autoscale or Reserved? | 22 |  |
| H7 | `Geen Verrassingen Meer` | No more surprises | 22 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Klaar In 1-3 Weken` | Done within 1-3 weeks | 18 |  |
| H10 | `Code 100% Van Jou` | Code 100% yours | 17 |  |
| H11 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H12 | `Gratis Kostenanalyse` | Free cost analysis | 20 | **P3** |

| # | Description (Nederlands) | Nghĩa tiếng Anh | Ch |
|---|---|---|---:|
| D1 | `Reserved VM rekent door terwijl niemand je app gebruikt. Dat kan anders.` | Reserved VM keeps billing while nobody uses your app. It doesn't have to. | 72 |
| D2 | `Wij verhuizen je Replit app naar hosting die je zelf beheert en betaalt.` | We move your Replit app to hosting you control and pay for yourself. | 72 |
| D3 | `Vaste prijs vanaf €800. Klaar in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Done in 1-3 weeks. Your code stays 100% yours. | 72 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

---

<a id="8"></a>
## 8. Extension tiếng Hà Lan

Dùng chung cho cả ba campaign. Giới hạn Google Ads: sitelink text ≤ 25, mỗi dòng mô tả ≤ 35, callout ≤ 25, structured snippet ≤ 25 ký tự mỗi giá trị.

**Sitelink extensions**

| # | Link text (NL) | Nghĩa | Dòng mô tả 1 (NL) | Dòng mô tả 2 (NL) |
|---|---|---|---|---|
| 1 | `Prijzen` (7) | Pricing | `Vaste prijs vanaf €800` (22) | `Geen uurtarief, geen verrassing` (31) |
| 2 | `Werkwijze` (9) | How we work | `Intake, fix en live in 1-3 weken` (32) | `Drie stappen, vaste planning` (28) |
| 3 | `Beveiligingsaudit` (17) | Security audit | `Wij vinden wat AI-code achterlaat` (33) | `Rapport binnen enkele dagen` (27) |
| 4 | `Cases` (5) | Cases | `Vodafone, TNO, CFLW en meer` (27) | `160+ projecten opgeleverd` (25) |
| 5 | `Gratis Code Review` (18) | Free code review | `Stuur je repo, wij kijken mee` (29) | `Antwoord binnen 1 werkdag` (25) |
| 6 | `Over Ons` (8) | About us | `Onafhankelijke studio, Amsterdam` (32) | `Onderdeel van Manifera` (22) |

**Callout extensions** (≤ 25 ký tự)

| Callout (NL) | Nghĩa | Ch |
|---|---|---:|
| `Vaste prijs vanaf €800` | Fixed price from €800 | 22 |
| `Live in 1-3 weken` | Live in 1-3 weeks | 17 |
| `Code 100% van jou` | Code 100% yours | 17 |
| `11+ jaar ervaring` | 11+ years experience | 17 |
| `160+ projecten` | 160+ projects | 14 |
| `Kantoor in Amsterdam` | Amsterdam office | 20 |
| `Gratis intakegesprek` | Free intake call | 20 |
| `AVG-proof opgeleverd` | Delivered GDPR-proof | 20 |

**Structured snippet** — Header: `Diensten` (Services), ≤ 25 ký tự mỗi giá trị

| Giá trị (NL) | Nghĩa | Ch |
|---|---|---:|
| `Beveiligingsaudit` | Security audit | 17 |
| `Betalingen koppelen` | Payment integration | 19 |
| `Hosting en deploy` | Hosting and deploy | 17 |
| `Code migratie` | Code migration | 13 |
| `Inlogsysteem` | Login system | 12 |
| `Database opzetten` | Database setup | 17 |
| `Performance fix` | Performance fix | 15 |
| `AVG-compliance` | GDPR compliance | 14 |
> 💡 **`AVG-proof opgeleverd` là callout đáng giá nhất trong danh sách.** AVG là tên Hà Lan của GDPR. Đối thủ nước ngoài viết "GDPR compliant" — người Hà Lan tìm "AVG". Một chữ này báo hiệu bạn là nhà cung cấp bản địa.

---

<a id="9"></a>
## 9. Negative keywords

### 9.1. B1 Lovable — chống từ điển & đồ lót

```
-bra          -bras         -lingerie     -ondergoed    -beha
-betekenis    -definitie    -synoniem     -vertaling    -uitspraak
-liedje       -songtekst    -film         -boek         -knuffel
-pop          -speelgoed    -baby         -huisdier     -hond
-kat          -naam         -namen        -loveable
```
> 🇳🇱 `ondergoed` (underwear) · `beha` (bra) · `betekenis` (meaning) · `definitie` (definition) · `synoniem` (synonym) · `vertaling` (translation) · `uitspraak` (pronunciation) · `liedje` (song) · `songtekst` (lyrics) · `boek` (book) · `knuffel` (plush toy) · `pop` (doll) · `speelgoed` (toy) · `huisdier` (pet) · `hond` (dog) · `kat` (cat) · `naam`/`namen` (name/names).

### 9.2. 🔴 B2 Bolt — danh sách quan trọng nhất

**Taxi / gọi xe / giao hàng**
```
-taxi         -taxis        -rit          -ritje        -ritten
-chauffeur    -bestuurder   -uber         -bolt driver  -rijden
-eten         -maaltijd     -bezorging    -bezorger     -koerier
-scooter      -step         -fiets        -ebike        -huren
-verhuur      -kortingscode -promocode    -tarief       -ritprijs
-app store    -play store   -app download -inloggen bolt
```
> 🇳🇱 `rit`/`ritje`/`ritten` (ride/s) · `bestuurder` (driver) · `rijden` (to drive) · `eten` (food) · `maaltijd` (meal) · `bezorging`/`bezorger` (delivery/courier) · `koerier` (courier) · `step` (kick scooter) · `fiets` (bicycle) · `huren`/`verhuur` (rent/rental) · `kortingscode` (discount code) · `tarief`/`ritprijs` (fare/ride price).

**Bu lông / ốc vít / vật liệu**
```
-schroef      -schroeven    -moer         -moeren       -bout
-bouten       -ring         -plug         -m8           -m10
-draadeind    -zeskant      -bouwmarkt    -gereedschap  -ijzerwaren
```
> 🇳🇱 `schroef`/`schroeven` (screw/s) · `moer`/`moeren` (nut/s) · `bout`/`bouten` (bolt/s) · `ring` (washer) · `plug` (wall plug) · `draadeind` (threaded rod) · `zeskant` (hex) · `bouwmarkt` (DIY store) · `gereedschap` (tools) · `ijzerwaren` (hardware).

**Người & thương hiệu khác**
```
-usain        -sprint       -olympisch    -atletiek     -record
-bliksem      -onweer       -threads      -stof         -disney
```
> 🇳🇱 `olympisch` (Olympic) · `atletiek` (athletics) · `bliksem` (lightning) · `onweer` (thunderstorm) · `stof` (fabric).

**Xe điện**
```
-ev           -laadpas      -laadstation  -opladen      -accu
-batterij     -motor        -auto         -voertuig
```
> 🇳🇱 `laadpas` (charging card) · `laadstation` (charging station) · `opladen` (to charge) · `accu`/`batterij` (battery) · `auto` (car) · `voertuig` (vehicle).

### 9.3. B3 Replit — danh sách ngắn nhất

```
-cursus       -opleiding    -leren        -les          -lessen
-tutorial     -handleiding  -school       -student      -huiswerk
-onderwijs    -gratis hosting             -100 days     -curriculum
```
> 🇳🇱 `cursus` (course) · `opleiding` (training) · `leren` (to learn) · `les`/`lessen` (lesson/s) · `handleiding` (manual) · `huiswerk` (homework) · `onderwijs` (education) · `gratis hosting` (free hosting).

### 9.4. Áp cho cả ba campaign

**Khối tuyển dụng — bắt buộc vì `gezocht` (§3.1)**
```
-vacature     -vacatures    -baan         -banen        -werk
-solliciteren -sollicitatie -cv           -salaris      -uurloon
-zzp tarief   -stage        -traineeship  -bijbaan
```
> 🇳🇱 `vacature/s` (job vacancy/ies) · `baan`/`banen` (job/s) · `werk` (work) · `solliciteren`/`sollicitatie` (to apply/application) · `salaris` (salary) · `uurloon` (hourly wage) · `zzp tarief` (freelance rate) · `stage` (internship) · `bijbaan` (side job).

**Khối miễn phí / tự làm**
```
-gratis       -zelf doen    -zelf maken   -template     -voorbeeld
-handleiding  -kraken       -gekraakt     -torrent      -download
```
> 🇳🇱 `gratis` (free) · `zelf doen`/`zelf maken` (do/make yourself) · `voorbeeld` (example) · `handleiding` (manual) · `kraken`/`gekraakt` (to crack/cracked).

**Khối nghiên cứu / so sánh**
```
-reddit       -youtube      -github       -docs         -documentatie
-forum        -review       -beoordeling  -ervaringen
```
> 🇳🇱 `documentatie` (documentation) · `beoordeling` (review/rating) · `ervaringen` (experiences).

> ⚠️ **Cân nhắc `-review` và `-ervaringen`.** Chúng chặn truy vấn so sánh, vốn có thể là khách ở giai đoạn cân nhắc. Nếu `AG-LOV-NL-Migrate` cho tín hiệu tốt thì bỏ hai từ này khỏi B1.

**Khối sản xuất — BẮT BUỘC, 218 từ**

Bốn keyword chứa `naar productie` / `productieklaar` (§3.3) trùng hoàn toàn thuật ngữ ngành cơ khí Hà Lan. Toàn bộ 218 từ chia 9 khối, gắn ở **cấp tài khoản** (Shared Library → Negative keyword lists) chứ không phải từng campaign:

##### 9.4.1. Vật liệu

```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```

##### 9.4.2. Gia công & chế tạo

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

##### 9.4.3. In 3D / additive

```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```

> ⚠️ **Cân nhắc `-3d` ở dạng broad.** Nó chặn cả `3d` đứng một mình. Nếu LaunchStudio có khách làm app có mô hình 3D (configurator, viewer), thì bỏ `-3d` và chỉ giữ các cụm 2 từ.

##### 9.4.4. Prototyping vật lý — khối quan trọng nhất

```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```

##### 9.4.5. Doanh nghiệp sản xuất

```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```

##### 9.4.6. Mua/thuê máy móc

```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```

##### 9.4.7. Phần mềm CAD/CAM (danh mục phần mềm khác)

```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

##### 9.4.8. Nhà cung cấp ERP ngành (người tìm đối thủ, không phải tìm bạn)

```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```

##### 9.4.9. Xây dựng & gevelbouw

```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```


> 🇳🇱 **Giải nghĩa các từ Hà Lan chính:** `staal` (steel) · `metaal` (metal) · `rvs` (stainless) · `koper` (copper) · `messing` (brass) · `gietijzer` (cast iron) · `kunststof` (plastic) · `hout` (wood) · `glasvezel` (fibreglass) · `frezen` (milling) · `draaien` (turning) · `verspanen` (machining) · `lasersnijden` (laser cutting) · `buigen`/`zetten`/`kanten` (bending) · `lassen`/`laswerk` (welding) · `plaatwerk` (sheet metal) · `metaalbewerking` (metalworking) · `gieten` (casting) · `spuitgieten` (injection moulding) · `matrijs`/`matrijzen` (mould/s) · `stansen`/`ponsen` (stamping/punching) · `slijpen` (grinding) · `polijsten` (polishing) · `anodiseren` (anodising) · `poedercoaten` (powder coating) · `galvaniseren` (galvanising) · `stralen` (blasting) · `fabricage`/`fabricatie` (fabrication) · `printen` (printing) · `maquette` (scale model) · `proefmodel` (test model) · `nulserie` (pre-production run) · `fabrikant`/`fabrikanten` (manufacturer/s) · `maakindustrie` (manufacturing industry) · `maakbedrijf`/`productiebedrijf` (manufacturing company) · `machinebouw` (machine building) · `machinefabriek` (machine factory) · `toeleverancier`/`toelevering` (supplier/supply) · `productielijn` (production line) · `seriematig`/`serieproductie` (series production) · `massaproductie` (mass production) · `werkplaats` (workshop) · `smederij` (forge) · `gieterij` (foundry) · `constructiebedrijf` (structural engineering firm) · `kopen` (to buy) · `te koop` (for sale) · `machinepark` (machine fleet) · `occasion`/`tweedehands` (second-hand) · `huren`/`verhuur` (rent/rental) · `onderhoud` (maintenance) · `reparatie` (repair) · `onderdelen` (parts) · `gereedschap` (tools) · `kozijncalculator` (window frame calculator) · `aannemer` (contractor) · `bouwbedrijf` (construction firm) · `verbouwing`/`renovatie` (renovation) · `bestek` (tender specification) · `staalconstructie` (steel structure) · `kozijn`/`kozijnen` (window frame/s) · `gevel`/`gevelbouw` (facade/facade building) · `dakkapel` (dormer) · `serre` (conservatory) · `beglazing` (glazing) · `ramen` (windows) · `deuren` (doors) · `schuifpui` (sliding patio door).

### 9.5. Lưu ý kỹ thuật

1. **Negative keyword KHÔNG tự khớp biến thể gần.** Tiếng Hà Lan tạo số nhiều bằng `-en` và `-s`, phải nhập riêng: `-vacature` **và** `-vacatures`, `-schroef` **và** `-schroeven`, `-rit` **và** `-ritten`.
2. **Từ đơn → negative broad · cụm nhiều từ → negative phrase.**
3. **Negative broad yêu cầu tất cả các từ cùng xuất hiện.** `-zzp tarief` dạng broad chỉ chặn truy vấn có cả hai từ.
4. **Tạo 5 Shared Negative List:** NL-Lovable · NL-Bolt · NL-Replit · NL-Chung · Sản xuất.
5. **Từ ghép tiếng Hà Lan viết liền.** `beveiligingsaudit` là một từ. Negative `-audit` sẽ **không** chặn nó, nhưng `-beveiligingsaudit` cũng không chặn `beveiliging audit` viết tách. Kiểm cả hai cách viết trong Search Terms.

---

<a id="10"></a>
## 10. Ngân sách, lộ trình & KPI

### 10.1. Ngân sách — thấp có chủ đích

| Campaign | Keyword | Tier A (phép thử) | Tier B (nếu có volume) | Trần |
|---|---:|---:|---:|---:|
| B1-NL-Lovable | 32 | €40 | €80 | €150 |
| B2-NL-Bolt | 24 | €25 | €45 | €80 |
| B3-NL-Replit | 29 | €35 | €70 | €120 |
| **Tổng/tháng** | **85** | **€100** | **€195** | **€350** |

> 🔴 **Bắt đầu ở Tier A €100/tháng, không cao hơn.** Bộ keyword NL gắn tên công cụ AI đo được 10 lượt tìm/tháng ở đợt trước. Nếu bản dịch này cũng vậy, €100 đã là dư. Chỉ nâng lên Tier B khi `IS lost (budget)` > 20% — nghĩa là thật sự có nhu cầu bị bỏ sót.

### 10.2. Lộ trình 6 tuần

| Tuần | Việc |
|---|---|
| **0** | Chạy Keyword Planner cho 85 keyword: dán `kp_upload_NL_translated.txt`, **Location = Netherlands, Language = Dutch**. Nếu tổng < 100/tháng → chỉ bật B1 ở €50 và dừng ở đó |
| **0** | Dựng 8 landing page `/nl/…` hoặc tối thiểu 3 trang (một trang mỗi campaign). Tạo 5 Shared Negative List |
| **1** | Bật **B3-NL-Replit** trước ở Tier A. Sạch nhất, không lẫn thương hiệu. Manual CPC |
| **2** | Bật **B1-NL-Lovable** ở Tier A. Kiểm Search Terms 2 ngày/lần |
| **3** | Bật **B2-NL-Bolt** ở Tier A. Kiểm Search Terms **hàng ngày**. Nếu > 30% truy vấn là taxi → tắt ngay |
| **4** | **Review 1.** Đếm impression từng ad group. Tắt mọi ad group có 0 impression sau 14 ngày |
| **5** | So sánh CTR và CPC của nhóm `*-Problem` (tiếng Hà Lan) với nhóm tương ứng ở nhánh tiếng Anh. Đây là phép thử trực tiếp cho giả định "dev Hà Lan gõ lỗi bằng tiếng Anh" |
| **6** | **Review 2.** Quyết định: giữ toàn bộ · giữ chỉ nhóm Hire/Cost/Migrate · hoặc tắt hẳn và dồn về nhánh tiếng Anh |

### 10.3. KPI — ngưỡng khác bản tiếng Anh

| Chỉ số | Tuần 3 | Tuần 6 | Ngưỡng dừng |
|---|---|---|---|
| **Impression** (số lượt hiển thị) | > 0 ở ≥ 5/8 ad group | > 50/tháng mỗi campaign | **0 impression sau 14 ngày = tắt ad group** |
| **CPC** (Cost Per Click) | ≤ €8 | ≤ €6 | > €12 — bất thường với volume thấp |
| **CTR** (Click-Through Rate) | ≥ 6% | ≥ 9% | < 4% = quảng cáo không khớp truy vấn |
| **Tỉ lệ truy vấn liên quan** | ≥ 70% | ≥ 85% | **< 50% ở B2 Bolt = tắt** |
| **QS** (Quality Score) | ≥ 5 | ≥ 6 | < 4 = landing page không phải tiếng Hà Lan bản ngữ |

> 💡 **Chỉ số quan trọng nhất ở plan này là Impression, không phải CPL.** Câu hỏi cần trả lời trước tiên không phải "có lãi không" mà là **"có ai gõ những từ này bằng tiếng Hà Lan không"**. Ad group nào 0 impression sau 14 ngày thì câu trả lời là không — tắt, đừng tăng bid.

### 10.4. Phép thử quyết định: so sánh song song hai ngôn ngữ

Đây là giá trị lớn nhất của plan này, hơn cả doanh thu nó có thể mang lại.

Chạy song song cùng một ý định ở hai ngôn ngữ và so sánh:

| Cặp so sánh | Nhánh EN | Nhánh NL (plan này) |
|---|---|---|
| Lỗi Lovable | `lovable app not working` | `lovable app werkt niet` |
| Thuê Replit | `hire replit developer` | `replit developer gezocht` |
| Chi phí Replit | `replit pricing too expensive` | `replit te duur` |
| Deploy Bolt | `bolt new not working` | `bolt new werkt niet` |

Sau 6 tuần, tỉ lệ impression NL/EN trả lời dứt điểm câu hỏi đã tranh luận suốt: **người Hà Lan gõ công cụ AI bằng tiếng nào**. Kết quả đó định hướng mọi quyết định SEO và nội dung về sau, không chỉ ads.

---

<a id="11"></a>
## 11. Checklist trước khi bật

### Verify volume — làm trước tất cả

- [ ] Dán `kp_upload_NL_translated.txt` vào Keyword Planner, **Location = Netherlands, Language = Dutch**
- [ ] Ghi tổng volume 85 keyword. **Nếu < 100/tháng → chỉ bật B1 ở €50, bỏ B2 và B3**
- [ ] So sánh volume từng cặp NL/EN ở §10.4 — đây là dữ liệu quan trọng nhất
- [ ] Lấy cột `Top of page bid (low/high)` để biết CPC thật

### Landing page

- [ ] Tối thiểu 3 trang `/nl/…`, một trang mỗi campaign. Lý tưởng là 8 trang
- [ ] Toàn bộ nội dung là **tiếng Hà Lan bản ngữ, không dịch máy** — QS phụ thuộc trực tiếp vào điều này
- [ ] Mỗi trang có **một câu tuyên bố độc lập**: *"LaunchStudio is een onafhankelijke studio en geen partner van [tool]."*
- [ ] Form liên hệ, email tự động và người trả lời đều bằng tiếng Hà Lan
- [ ] Dùng **AVG**, không dùng **GDPR**
- [ ] Trang `/nl/lovable-tanstack-migratie` giải thích mốc 13/05/2026 bằng tiếng Hà Lan

### Trong Google Ads

- [ ] **Language = Dutch, chỉ Dutch.** Không thêm English — sẽ cạnh tranh nội bộ với nhánh EN
- [ ] Location = Netherlands, chế độ **"Presence"**
- [ ] Tạo **5 Shared Negative List**: NL-Lovable · NL-Bolt · NL-Replit · NL-Chung · **Sản xuất (218 từ)**
- [ ] Gắn list **Sản xuất** vào cả ba campaign — 4 keyword chứa `naar productie` (§3.3)
- [ ] Gắn khối **tuyển dụng** (`vacature`, `baan`, `salaris`…) vào cả ba — vì `gezocht` (§3.1)
- [ ] `lovable developer gezocht` và `replit developer gezocht` để **Exact match**
- [ ] `bolt new app developer` để **Exact match** hoặc bỏ hẳn ở giai đoạn 1
- [ ] Xác nhận **không có keyword `bolt` nào đứng một mình**
- [ ] Xoá 4 keyword trùng khỏi campaign N2-NL-AI-Tools (§4) — hoặc tắt hẳn N2
- [ ] Nhập biến thể số nhiều riêng cho mọi negative (`-vacature` **và** `-vacatures`)
- [ ] Bid strategy = **Manual CPC**
- [ ] Ad rotation = **"Do not optimize"**
- [ ] Nạp đủ **12 headline + 4 description** cho mỗi ad group
- [ ] Nạp 6 sitelink · 8 callout · 1 structured snippet (§8)
- [ ] Đặt lịch Search Terms: **hàng ngày cho B2**, 2 ngày/lần cho B1 và B3

---

## 📌 Tóm tắt

> **Cùng 85 keyword, cùng 8 ad group, nhưng toàn bộ bằng tiếng Hà Lan — keyword và quảng cáo khớp ngôn ngữ tuyệt đối.**
>
> Không phải từ nào cũng dịch: động từ và hành vi thương mại dịch sang tiếng Hà Lan (`werkt niet`, `inhuren`, `te duur`, `kosten`), còn tên sản phẩm và thuật ngữ dev giữ nguyên (`deployment`, `RLS`, `SSR`, `CORS`, `Reserved VM`). Ba chỗ cần bản ngữ thật sự: `witte pagina` không phải `blanco pagina`, `agent loopt vast` không phải `agent vast`, và `fix bolt app` bị thay hẳn thành `app gebouwd met bolt new laten afmaken` vì không thể tránh lẫn với taxi.
>
> **Ngân sách khởi điểm €100/tháng, thấp có chủ đích.** Đợt đo trước cho thấy keyword tiếng Hà Lan gắn tên công cụ AI chỉ có 10 lượt tìm/tháng. Plan này là phép thử giá rẻ để chiếm chỗ, không phải kênh chính.
>
> **Chỉ số quyết định là Impression, không phải CPL.** Câu hỏi cần trả lời trước tiên là "có ai gõ những từ này bằng tiếng Hà Lan không". Ad group nào 0 impression sau 14 ngày thì tắt.
>
> Giá trị lớn nhất của plan này có thể không phải doanh thu, mà là **phép thử song song hai ngôn ngữ ở §10.4** — sau 6 tuần bạn có câu trả lời dứt điểm cho câu hỏi người Hà Lan gõ công cụ AI bằng tiếng nào, và câu trả lời đó định hướng cả SEO lẫn nội dung về sau.

---

*85 keyword tiếng Hà Lan (dịch 1:1 từ bộ tiếng Anh) · 3 campaign · 8 ad group · 162 asset quảng cáo tiếng Hà Lan đã kiểm bằng script — 96 headline (dài nhất 28/30) · 32 description (dài nhất 80/90) · 6 sitelink · 8 callout · 8 structured snippet — **0 vi phạm giới hạn ký tự Google Ads***

*File keyword: `keyword_seeds_3_ai_brands_NL_translated.csv` · File dán Keyword Planner: `kp_upload_NL_translated.txt`*

*🇳🇱 Mọi keyword và nội dung quảng cáo giữ nguyên tiếng Hà Lan, nghĩa tiếng Anh ở cột kế bên. **Không dịch khi nhập vào Google Ads.***
