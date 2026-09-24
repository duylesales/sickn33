# 🔭 Playbook: Cách Tìm Thêm Keyword & Ý Tưởng

> **Mục đích:** 20 phương pháp tìm keyword mới cho LaunchStudio — xếp theo giá trị thực tế, không theo lý thuyết.
> **Kèm theo:** 78 keyword mới mình tìm được khi áp dụng chính các phương pháp này (§B).
> **Ngày:** 2026-09-24
> **Liên quan:** [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md) · [`keyword_seeds_google_ads_3_clusters.csv`](keyword_seeds_google_ads_3_clusters.csv)

---

# PHẦN A — 20 PHƯƠNG PHÁP

## 🥇 Nhóm 1 — Có dữ liệu thật, miễn phí, làm được hôm nay

### 1. Google Search Console — mỏ vàng rẻ nhất, bạn đang ngồi trên nó

Bạn có **71 bài đang live** trên `/insights/`. GSC đã ghi nhận mọi truy vấn mà chúng xuất hiện.

**Cách làm:** GSC → Performance → Search results → tab Queries → lọc `Impressions > 10` và `Position 8–30`.

Đây là truy vấn Google **đã coi bạn liên quan** nhưng bạn chưa đủ mạnh để lên top. Rẻ hơn mọi keyword mới vì bạn đã có nội dung.

**Ba lát cắt đáng xem:**
- `Position 11–20` + impression cao → sửa bài cũ là lên trang 1
- `CTR < 1%` nhưng position < 10 → title/meta sai, không phải keyword sai
- Lọc country = Netherlands riêng → truy vấn NL thật, không phải đoán

> 💡 Đây cũng là nguồn duy nhất cho bạn biết **người Hà Lan thật sự gõ gì**, thay vì dịch từ tiếng Anh.

### 2. Search Terms Report (sau khi chạy ads)

Truy vấn thật đã kích hoạt quảng cáo. Khác keyword bạn đặt — đây là ngôn ngữ người dùng.

**Cách làm:** Google Ads → Campaigns → Insights → Search terms. Lọc theo conversion > 0 → đó là keyword nên tách ra ad group riêng.

Với tài khoản volume thấp, kiểm **mỗi 2 ngày trong 4 tuần đầu**.

### 3. 🆓 Bing Webmaster Tools — công cụ keyword miễn phí có volume thật

Ít người biết: Bing Webmaster Tools có **Keyword Research** cho volume thật, **không cần chi tiền quảng cáo**, không giới hạn như Ahrefs/Semrush free tier.

**Cách làm:** Đăng ký BWT (miễn phí) → verify domain → Keyword Research → nhập seed.

Volume Bing thấp hơn Google (~1/5–1/10 thị phần EU) nhưng **tỉ lệ tương đối giữa các keyword thì đáng tin**. Dùng để xếp hạng ưu tiên khi chưa có GKP.

### 4. Keyword Planner — seed bằng URL **đối thủ**, không phải URL của mình

Đây là lỗi đã mắc trong repo: [`keyword-planner-...csv`](keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv) được seed bằng `launchstudio.eu/en/` và trả về rác (`day ai` 201.000/tháng, 94% tổng volume).

**Cách đúng:** seed bằng URL đối thủ đang rank tốt:
```
https://redwerk.com/services/vibe-code-cleanup/
https://www.instinctools.com/vibe-code-audit-cleanup/
https://www.pragmaticcoders.com/services/ai-software-development-services/vibe-coding-rescue
https://appfront.nl/diensten/software-ontwikkeling/metaalbewerking-software-laten-maken
https://nextlovable.com/migrate-lovable-tanstack
https://www.appstuck.com/blog
```
Google sẽ trả về keyword nó cho là trang đó nhắm tới — tức là **thị trường của đối thủ, không phải của bạn hiện tại**.

---

## 🥈 Nhóm 2 — Đào đối thủ

### 5. Sitemap mining — lấy toàn bộ cấu trúc nội dung đối thủ

Nhanh nhất để lấy hàng trăm keyword đã được validate.

```bash
curl -s https://www.appstuck.com/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' | sed 's|.*/||'
curl -s https://www.rapidevelopers.com/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' | grep lovable
```

Mỗi URL slug = một keyword họ đang nhắm. Nếu họ viết 31 bài troubleshooting thì có 31 keyword có nhu cầu.

**Đối thủ đáng đào:** appstuck.com · rapidevelopers.com/lovable-issues · afterbuildlabs.com · nextlovable.com · vibeappscanner.com · ship-safe.co · lovable.club

### 6. 🆓 Google Ads Transparency Center — xem đối thủ chạy quảng cáo gì

`adstransparency.google.com` → tìm tên đối thủ → xem **toàn bộ quảng cáo họ đang chạy**, kèm thời gian và khu vực.

Ad copy tiết lộ keyword họ bid và góc bán họ dùng. Nếu một đối thủ chạy cùng một ad **liên tục 6 tháng** thì ad đó đang có lãi — copy góc đó.

### 7. Trang pricing & service của đối thủ

Cách họ **đặt tên dịch vụ** chính là keyword. Redwerk gọi là "vibe code cleanup", instinctools gọi là "vibe code audit", Pragmatic Coders gọi là "vibe coding rescue" — ba tên cho cùng một dịch vụ, cả ba đều là keyword.

### 8. Fiverr / Upwork gig titles — ngôn ngữ người mua, nguyên văn

Gig title được tối ưu cho công cụ tìm kiếm nội bộ, tức là **đúng từ người mua gõ**.

Ví dụ đã tìm thấy: *"I will fix deploy replit lovable cursor ai bolt new base44 supabase oauth vercel stripe"* — mỗi từ trong đó là một keyword.

---

## 🥇 Nhóm 3 — Nguồn sản phẩm (giá trị cao nhất, ít người làm)

### 9. ⭐ Changelog của tool — cách tốt nhất để tìm keyword chưa ai chiếm

**Đây là phương pháp có ROI cao nhất trong toàn bộ danh sách.**

Logic: tính năng mới → người dùng gặp vấn đề mới → tìm kiếm mới → **chưa ai viết nội dung**. Bạn có cửa sổ 1–6 tháng trước khi đối thủ nhận ra.

**Cách làm:** đọc `docs.lovable.dev/changelog` mỗi tháng. Với mỗi tính năng mới, hỏi: *người dùng sẽ gặp vấn đề gì?*

Mình đã làm việc này và tìm được **78 keyword mới** — xem §B. Phát hiện lớn nhất: Lovable đã đổi stack từ React+Vite sang TanStack Start và **không tự động migrate dự án cũ**. Đã có đối thủ bán audit $199–299 cho đúng việc này.

**Làm tương tự với:** Bolt, Cursor, Replit, Supabase, Stripe, Vercel changelog.

### 10. Docs & FAQ của tool

Vendor chỉ viết FAQ cho câu hỏi được hỏi nhiều. Lovable có hẳn trang `/faq/domains/ssl` → nghĩa là SSL domain là vấn đề phổ biến.

### 11. Status page & lịch sử sự cố

`status.lovable.dev`, `status.supabase.com`. Mỗi sự cố lớn tạo ra một đợt tìm kiếm. Cũng cho biết thành phần nào hay hỏng.

### 12. Community forum, Discord, Reddit

Ngôn ngữ thật của người dùng, thường khác cách vendor gọi.

**Nguồn:** Lovable Discord · r/lovable · r/nocode · r/SaaS · r/vibecoding · Lovable feedback board

Tìm bài nhiều upvote nhất trong 90 ngày → đó là nỗi đau lớn nhất hiện tại.

### 13. GitHub issues

Với công cụ open-source hoặc có repo công khai. Issue title = mô tả vấn đề bằng từ kỹ thuật chính xác.

---

## 🥉 Nhóm 4 — Mở rộng ngữ nghĩa

### 14. Autocomplete + People Also Ask + Related searches

Gõ keyword gốc + từng chữ cái a–z vào Google. Miễn phí, nhanh, và phản ánh truy vấn thật.

Cộng thêm hộp "People also ask" và "Related searches" ở cuối SERP.

### 15. Google Trends — truy vấn đang tăng

`trends.google.com` → nhập keyword → phần **Related queries → Rising**. Truy vấn "Breakout" = tăng >5000%, thường là tính năng mới hoặc sự cố mới.

Đặt geo = Netherlands để thấy xu hướng NL riêng.

### 16. AnswerThePublic / AlsoAsked (bản miễn phí)

Sinh câu hỏi theo cấu trúc: what/how/why/can/is + keyword. Giới hạn vài lượt/ngày nhưng đủ dùng.

### 17. Ma trận modifier — sinh hàng trăm keyword có hệ thống

Phương pháp cơ học nhưng hiệu quả. Nhân các cột với nhau:

| Tool | × Thành phần | × Vấn đề | × Hành động |
|---|---|---|---|
| lovable | supabase | not working | fix |
| bolt | stripe | error | how to |
| cursor | domain | failed | setup |
| replit | auth | stuck | migrate |
| v0 | deploy | slow | export |
| base44 | database | broken | debug |

6 × 6 × 5 × 5 = **900 tổ hợp**. Đa số vô nghĩa, nhưng lọc qua Keyword Planner sẽ còn 50–100 cái có volume.

```bash
# sinh nhanh bằng shell
for t in lovable bolt cursor replit v0; do
  for c in supabase stripe domain auth deploy database; do
    for p in "not working" "error" "failed" "setup"; do
      echo "$t $c $p"
    done
  done
done
```

---

## 🏅 Nhóm 5 — Từ khách hàng thật (ít ai làm, giá trị cao nhất)

### 18. Ghi âm sales call

Khách mô tả vấn đề bằng từ gì? Họ hiếm khi nói "production-readiness gap". Họ nói *"app chạy được trên máy tôi nhưng không ai khác vào được"*.

Đó mới là từ người ta gõ vào Google.

### 19. Email & chat inbound

Đọc lại 20 email hỏi hàng gần nhất. Tiêu đề email thường là keyword.

### 20. Hỏi thẳng: "Bạn tìm thấy chúng tôi thế nào?"

Thêm một field vào form liên hệ. Câu trả lời dạng "tôi google 'lovable app niet live'" đáng giá hơn mọi công cụ.

---

# PHẦN B — 78 KEYWORD MỚI (kết quả áp dụng phương pháp #9)

> Tất cả đều **chưa có** trong [`keyword_seeds_google_ads_3_clusters.csv`](keyword_seeds_google_ads_3_clusters.csv) hiện tại.
> Nguồn: `docs.lovable.dev/changelog` (các thay đổi 2026) + nghiên cứu SERP xác minh.
> File CSV kèm: [`keyword_ideas_round2.csv`](keyword_ideas_round2.csv)

## B1. 🔴 TanStack Start migration — cơ hội tốt nhất tìm được

**Bối cảnh:** Lovable đổi stack mặc định từ React + Vite sang **TanStack Start** (mặc định cho dự án mới từ 13/05/2026, Enterprise từ 22/06/2026). **Lovable không tự động migrate dự án cũ.**

Nghĩa là: mọi dự án Lovable tạo trước tháng 5/2026 đang chạy stack cũ, không có SSR, và chủ sở hữu có thể không biết.

**Xác minh thương mại:** `nextlovable.com` đã bán **audit $199 và $299** cho đúng việc này, với 3 landing page riêng.

| Keyword | Ghi chú |
|---|---|
| `lovable tanstack start` | |
| `lovable tanstack migration` | |
| `migrate lovable to tanstack` | |
| `upgrade lovable project tanstack` | Đúng tên trang docs của Lovable |
| `lovable react vite to tanstack` | |
| `lovable ssr` | |
| `lovable ssr upgrade` | |
| `lovable old stack` | |
| `lovable project still on vite` | |
| `lovable stack change 2026` | |
| `lovable tanstack migration service` | Intent thuê — cao nhất |
| `lovable seo ssr problem` | Nối với vấn đề SEO của app Lovable |

➡️ **Đây là cụm nên làm ngay.** Tính thời sự cao, đối thủ đã chứng minh có người trả tiền, và cửa sổ cơ hội sẽ đóng trong vài tháng.

## B2. 🔴 Lovable Payments / Paddle — hoàn toàn chưa phủ

**Bối cảnh:** Lovable ra **Lovable Payments powered by Paddle** — không chỉ Stripe nữa. Toàn bộ 8 keyword Stripe trong CSV hiện tại **bỏ sót nửa thị trường**.

| Keyword | Ghi chú |
|---|---|
| `lovable payments` | |
| `lovable paddle` | |
| `lovable payments vs stripe` | Intent so sánh, dễ viết |
| `lovable paddle checkout` | |
| `lovable paddle domain flagged` | Changelog có tính năng "resubmit flagged domain" → vấn đề thật |
| `lovable payments setup` | |
| `lovable payments not working` | |
| `lovable payments fees` | |
| `lovable subscription setup` | |
| `paddle vs stripe for saas` | Rộng hơn, volume cao hơn |

## B3. Lovable Cloud — surface hạ tầng mới

**Bối cảnh:** Lovable Cloud có database scaling, giám sát CPU/Memory/Disk, giới hạn upload tới 5GB. Đây là surface hạ tầng riêng, cạnh tranh trực tiếp với Supabase.

| Keyword | Ghi chú |
|---|---|
| `lovable cloud` | |
| `lovable cloud pricing` | |
| `lovable cloud vs supabase` | Câu hỏi quyết định quan trọng |
| `lovable database scaling` | |
| `lovable cloud storage limit` | |
| `lovable database pressure` | Đúng tên tính năng mới |
| `lovable cloud performance` | |
| `do i need lovable cloud` | |

## B4. Connector mới (15+ tích hợp ra trong Q3/2026)

Mỗi connector là một keyword `lovable + [tên]` chưa ai viết.

| Keyword | Keyword |
|---|---|
| `lovable whatsapp business` | `lovable posthog` |
| `lovable power bi` | `lovable xero` |
| `lovable cloudflare integration` | `lovable google analytics` |
| `lovable mapbox` | `lovable gitlab sync` |
| `lovable firebase messaging` | `lovable bitbucket sync` |
| `lovable apollo.io` | `lovable clickhouse` |
| `lovable figma plugin` | `lovable tally forms` |

➡️ Volume từng cái nhỏ, nhưng **cạnh tranh gần bằng 0** và intent rất cụ thể. Gom thành một bài "Lovable integrations: cái nào dùng được thật" rồi tách bài riêng cho cái nào có tín hiệu.

## B5. MCP & Agents — surface hoàn toàn mới

| Keyword | Ghi chú |
|---|---|
| `lovable mcp server` | |
| `lovable mcp setup` | |
| `lovable agent integrations` | |
| `publish lovable app as mcp` | |
| `lovable slack integration` | "Lovable in Slack" ra 26/08 |
| `lovable goal command` | Tính năng `/goal` chạy liên tục 10 tiếng |

## B6. Enterprise & bảo mật (nối với cụm ③)

| Keyword | Ghi chú |
|---|---|
| `lovable sso setup` | |
| `lovable scim` | |
| `lovable 2fa enforcement` | Bắt buộc từ 11/09 |
| `lovable trust center` | `/.well-known/trust.json` |
| `lovable enterprise security` | |
| `lovable api key revoked` | Tự động thu hồi key GitHub bị lộ |
| `lovable security insights` | |

## B7. Từ FAQ cộng đồng (phương pháp #10, #12)

| Keyword | Ghi chú |
|---|---|
| `lovable favicon` | Được ghi nhận là FAQ phổ biến nhất |
| `lovable mobile layout broken` | |
| `lovable drafts` | Tính năng mới 09/09 |
| `lovable chat mode` | |
| `lovable preview slow` | Có toggle tắt preview cho dự án lớn |
| `lovable project won't load` | |

## B8. Công cụ khác chưa phủ trong CSV

CSV hiện chỉ có Lovable/Bolt/Cursor/Replit. Thị trường đã rộng hơn.

| Keyword | Ghi chú |
|---|---|
| `base44 export code` | Xuất hiện trong gig Fiverr cùng nhóm |
| `base44 to production` | |
| `v0 to production` | |
| `v0 export nextjs` | |
| `rocket new app` | |
| `windsurf production code` | |
| `firebase studio deploy` | |
| `claude code production ready` | |
| `replit agent 3` | |
| `figma make to production` | |

## B9. Đối thủ trực tiếp (phương pháp #5, #7)

| Keyword | Ghi chú |
|---|---|
| `nextlovable` | Đối thủ bán audit $199–299 |
| `nextlovable alternative` | |
| `lovable audit service` | |
| `lovable migration service` | |
| `vibeappscanner` | Công cụ quét bảo mật Lovable |
| `lovable security scanner` | |

---

# PHẦN C — Quy trình lặp hàng tháng

Đừng làm keyword research một lần rồi thôi. Đây là nhịp 90 phút/tháng:

| Phút | Việc | Phương pháp |
|---:|---|---|
| 0–20 | GSC: lọc query position 11–20, impression > 10 | #1 |
| 20–35 | Search Terms Report: thêm negative + tách keyword tốt | #2 |
| 35–55 | Đọc changelog Lovable/Bolt/Cursor/Supabase tháng qua | #9 |
| 55–70 | Quét sitemap 2 đối thủ, so với danh sách của mình | #5 |
| 70–80 | Google Trends → Rising queries, geo = NL | #15 |
| 80–90 | Cập nhật CSV, đánh dấu cái nào đáng test | |

**Nguyên tắc:** mỗi tháng thêm tối đa 10 keyword vào campaign. Thêm nhiều hơn thì không đủ volume để đánh giá cái nào hiệu quả.

---

## ⚠️ Lưu ý về 78 keyword ở Phần B

- **Chưa có volume.** Tất cả cần verify bằng Keyword Planner hoặc Bing Webmaster Tools trước khi đưa vào campaign.
- **Nhiều cái rất mới** (tính năng ra tháng 7–9/2026) → volume có thể còn rất thấp, nhưng cũng nghĩa là **chưa ai cạnh tranh**. Với SEO thì nên viết ngay; với Ads thì đợi verify volume.
- **Ưu tiên rõ ràng: B1 (TanStack) và B2 (Paddle).** Hai cụm này vừa mới, vừa có bằng chứng thương mại, vừa khớp đúng dịch vụ LaunchStudio đang bán.

---

*Playbook này áp dụng được cho mọi dự án, không riêng LaunchStudio. Phương pháp #9 (changelog mining) là cái đáng đầu tư nhất.*
