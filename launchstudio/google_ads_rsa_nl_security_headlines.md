# 🇳🇱 RSA Headlines — `AG-NL-Security` · Nâng Ad Strength lên Good+

> **Phạm vi:** 6 keyword của ad group `AG-NL-Security` trong campaign C1 `LS-Search-NL-Service`
> (xem [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md) §5.1 — Max CPC €7,00 · €2,50/ngày · LP `/nl/beveiligingsaudit-ai-app`)
>
> `"beveiligingsaudit webapplicatie"` · `"code audit laten uitvoeren"` · `"security audit software laten doen"`
> `"avg compliance app"` · `"pentest webapplicatie"` · `"applicatie beveiliging laten testen"`
>
> **Giới hạn:** Headline ≤ **30** ký tự · Description ≤ **90** ký tự. Toàn bộ copy đã đếm sẵn.
> **File anh em:** [`google_ads_rsa_nl_rescue_headlines.md`](google_ads_rsa_nl_rescue_headlines.md) (cụm `AG-NL-Rescue`)

---

## 1. Chẩn đoán

Khác với `AG-NL-Rescue`, cụm này **đã có sẵn bản nháp NL**: mục `🇳🇱 AG4 — Beveiligingsaudit`
trong [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) (~dòng 598)
— 12 headline, 4 description, dùng **ngôi trang trọng `u`**. Đó là điểm khởi đầu tốt, nhưng còn ba lỗ hổng.

### 1.1. 🔴 Độ phủ keyword: chỉ 1/6 khớp nguyên văn

| Keyword | Trạng thái | Headline AG4 hiện có |
|---|:---:|---|
| `pentest webapplicatie` | ✅ khớp | `Pentest Webapplicatie` |
| `beveiligingsaudit webapplicatie` | ⚠️ một phần | `Beveiligingsaudit Software` (sai danh từ) |
| `security audit software laten doen` | ⚠️ một phần | `Security Audit Applicatie` |
| `avg compliance app` | ⚠️ một phần | `AVG & Enterprise-proof` |
| `code audit laten uitvoeren` | ❌ | — |
| `applicatie beveiliging laten testen` | ❌ | — |

> ⚠️ Riêng `beveiligingsaudit webapplicatie` **không thể viết nguyên cụm vào headline**:
> `Beveiligingsaudit Webapplicatie` = **31 ký tự**, vượt 1 ký tự. Cách xử lý ở §3: tách thành
> `Beveiligingsaudit Webapp` (24) + `Audit Van Uw Webapplicatie` (26), và đưa nguyên cụm vào description.

### 1.2. 🟠 Mới có 12/15 headline

Thiếu 3 slot. Đây là recommendation *"Add more headlines"* — dễ sửa nhất trong toàn bộ danh sách.

### 1.3. 🟠 Sáu keyword là bốn intent, không phải một

| Intent | Keyword | Khách đang muốn gì |
|---|---|---|
| **Audit dịch vụ** | `beveiligingsaudit webapplicatie`, `security audit software laten doen` | Muốn thuê bên ngoài audit toàn bộ ứng dụng |
| **Code-level** | `code audit laten uitvoeren`, `applicatie beveiliging laten testen` | Đã nghi ngờ code, muốn review/test kỹ thuật |
| **Compliance** | `avg compliance app` | Lo pháp lý AVG/GDPR, không hẳn lo kỹ thuật |
| **Pentest** | `pentest webapplicatie` | Cần một bài test xâm nhập, thường để đưa cho bên thứ ba |

`google_ads_production_keywords_plan_nl.md` §rủi ro (~dòng 956) **đã tự ghi**: *"Separate ad group
with its own bid cap; never merge into AG3"* cho `pentest`. Mình làm đúng theo khuyến nghị đó.

---

## 2. Giải pháp: tách 1 ad group → 4

| Ad group mới | Keyword | Max CPC đề xuất | Ghi chú |
|---|---|---:|---|
| `AG-NL-Sec-Audit` | `"beveiligingsaudit webapplicatie"`, `"security audit software laten doen"` | €7,00 | Giữ nguyên bid |
| `AG-NL-Sec-Code` | `"code audit laten uitvoeren"`, `"applicatie beveiliging laten testen"` | €7,00 | Giữ nguyên bid |
| `AG-NL-Sec-AVG` | `"avg compliance app"` | €5,00 | Intent pháp lý, hạ bid |
| `AG-NL-Sec-Pentest` | `"pentest webapplicatie"` | €9,00 | **Bid cap riêng** — CPC cụm này cao nhất |

Landing page: cả bốn dùng `/nl/beveiligingsaudit-ai-app`. Tổng ngân sách cụm giữ nguyên €2,50/ngày.

**Ngôi xưng:** toàn bộ copy dưới đây dùng **`u` trang trọng**, khớp bản AG4 sẵn có và đúng với
đối tượng (doanh nghiệp, due diligence). ⚠️ Lưu ý: file `AG-NL-Rescue` dùng **`je` thân mật**.
Hai cụm nằm chung một campaign nhưng khác ngôi — đây là chủ ý theo đối tượng, không phải lỗi,
nhưng cần thống nhất ghi lại để người review NL không "sửa nhầm".

---

## 3. `AG-NL-Sec-Audit` — 15 headlines

**Keyword:** `"beveiligingsaudit webapplicatie"` · `"security audit software laten doen"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword |
|---|---|---:|---|:---:|
| H1 | `Beveiligingsaudit Webapp` | 24 | Service | 🎯 |
| H2 | `Beveiligingsaudit Nodig?` | 24 | Question | 🎯 |
| H3 | `Security Audit Software` | 23 | Service | 🎯 |
| H4 | `Security Audit Applicatie` | 25 | Service | 🎯 |
| H5 | `Audit Van Uw Webapplicatie` | 26 | Keyword biến thể | 🎯 |
| H6 | `Laat Uw Software Auditen` | 24 | Keyword biến thể | 🎯 |
| H7 | `Vaste Prijs, Geen Nacalc.` | 25 | Pricing model | |
| H8 | `Rapport Met Prioriteiten` | 24 | Deliverable | |
| H9 | `Audit Én Herstel In Één` | 23 | Differentiator | |
| H10 | `11+ Jaar Security-Ervaring` | 26 | Trust | |
| H11 | `Vodafone, TNO En CFLW` | 21 | Social proof | |
| H12 | `Klaar Voor Due Diligence` | 24 | Outcome | |
| H13 | `Ook Voor AI-Gebouwde Apps` | 25 | Qualifier | |
| H14 | `Offerte Binnen 1 Werkdag` | 24 | CTA | |
| H15 | `Plan Een Gratis Gesprek` | 23 | CTA | |

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `Onafhankelijke beveiligingsaudit van uw webapplicatie. Vaste prijs, geen nacalculatie.` | 86 |
| D2 | `U krijgt een rapport met prioriteiten en een vaste offerte om de gaten te dichten.` | 82 |
| D3 | `Uitgevoerd door engineers met 11+ jaar ervaring. Vodafone, TNO en CFLW gingen u voor.` | 85 |
| D4 | `Ook geschikt voor apps die met AI-tools zijn gebouwd. Plan een gratis gesprek.` | 78 |

---

## 4. `AG-NL-Sec-Code` — 15 headlines

**Keyword:** `"code audit laten uitvoeren"` · `"applicatie beveiliging laten testen"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword |
|---|---|---:|---|:---:|
| H1 | `Code Audit Laten Uitvoeren` | 26 | Keyword nguyên cụm | 🎯 |
| H2 | `Code Audit Nodig?` | 17 | Question | 🎯 |
| H3 | `Applicatie Laten Testen` | 23 | Keyword nguyên cụm | 🎯 |
| H4 | `Beveiliging Laten Testen` | 24 | Keyword nguyên cụm | 🎯 |
| H5 | `Uw Code Onafhankelijk Getest` | 28 | Value prop | 🎯 |
| H6 | `Wij Testen Uw Applicatie` | 24 | Solution | 🎯 |
| H7 | `Code Review Door Engineers` | 26 | Credibility | |
| H8 | `Vaste Prijs, Geen Uurtarief` | 27 | Pricing model | |
| H9 | `Rapport In Heldere Taal` | 23 | Deliverable | |
| H10 | `Audit Én Herstel In Één` | 23 | Differentiator | |
| H11 | `11+ Jaar Security-Ervaring` | 26 | Trust | |
| H12 | `Vodafone, TNO En CFLW` | 21 | Social proof | |
| H13 | `Ook Voor AI-Gebouwde Code` | 25 | Qualifier | |
| H14 | `Offerte Binnen 1 Werkdag` | 24 | CTA | |
| H15 | `Plan Een Gratis Gesprek` | 23 | CTA | |

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `Code audit laten uitvoeren? Onafhankelijke review van uw codebase tegen vaste prijs.` | 84 |
| D2 | `Wij testen toegangsrechten, encryptie en logging. Rapport in begrijpelijke taal.` | 80 |
| D3 | `Audit en herstel in één traject. U kiest zelf of wij de gaten ook dichten.` | 74 |
| D4 | `11+ jaar engineering van Manifera. Vodafone, TNO en CFLW gingen u voor.` | 71 |

---

## 5. `AG-NL-Sec-AVG` — 15 headlines

**Keyword:** `"avg compliance app"`

| # | 🇳🇱 Headline | Ch | Angle | Keyword |
|---|---|---:|---|:---:|
| H1 | `AVG Compliance Voor Uw App` | 26 | Keyword nguyên cụm | 🎯 |
| H2 | `Is Uw App AVG-Proof?` | 20 | Question | 🎯 |
| H3 | `AVG-Risico's In Kaart` | 21 | Deliverable | 🎯 |
| H4 | `Persoonsgegevens Veilig?` | 24 | Pain point | |
| H5 | `Datalek Voorkomen` | 17 | Pain point | |
| H6 | `AVG-Check Voor Webapps` | 22 | Service | 🎯 |
| H7 | `Toegangsrechten Getest` | 22 | Technical | |
| H8 | `Encryptie En Logging Check` | 26 | Technical | |
| H9 | `Rapport Met Prioriteiten` | 24 | Deliverable | |
| H10 | `Vaste Prijs, Geen Nacalc.` | 25 | Pricing model | |
| H11 | `11+ Jaar Security-Ervaring` | 26 | Trust | |
| H12 | `Vodafone, TNO En CFLW` | 21 | Social proof | |
| H13 | `Ook Voor AI-Gebouwde Apps` | 25 | Qualifier | |
| H14 | `Offerte Binnen 1 Werkdag` | 24 | CTA | |
| H15 | `Plan Een Gratis Gesprek` | 23 | CTA | |

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `Is uw app AVG-proof? Wij brengen de risico's rond persoonsgegevens in kaart.` | 76 |
| D2 | `Toegangsrechten, encryptie en logging getest. Rapport met prioriteiten en offerte.` | 82 |
| D3 | `Wij zijn geen juristen: u krijgt de technische AVG-risico's, concreet en oplosbaar.` | 83 |
| D4 | `Vaste prijs, geen nacalculatie. Offerte binnen 1 werkdag. Plan een gratis gesprek.` | 82 |

> **Vì sao D3 chủ động nói "wij zijn geen juristen":** xem cảnh báo §8.2. Đây là câu bảo vệ bạn,
> không phải câu bán hàng — nhưng nó lọc đúng người và tránh kỳ vọng sai ngay từ trước khi click.

---

## 6. `AG-NL-Sec-Pentest` — 15 headlines

**Keyword:** `"pentest webapplicatie"` · ⚠️ **đọc §8.1 trước khi bật ad group này**

| # | 🇳🇱 Headline | Ch | Angle | Keyword |
|---|---|---:|---|:---:|
| H1 | `Pentest Webapplicatie` | 21 | Keyword nguyên cụm | 🎯 |
| H2 | `Pentest Voor Uw Webapp` | 22 | Keyword biến thể | 🎯 |
| H3 | `Webapplicatie Laten Testen` | 26 | Keyword biến thể | 🎯 |
| H4 | `Security Test Webapplicatie` | 27 | Service | 🎯 |
| H5 | `Kwetsbaarheden Opsporen` | 23 | Outcome | |
| H6 | `Testen Vóór De Lancering` | 24 | Timing | |
| H7 | `Rapport Met Prioriteiten` | 24 | Deliverable | |
| H8 | `Audit Én Herstel In Één` | 23 | Differentiator | |
| H9 | `Vaste Prijs, Geen Nacalc.` | 25 | Pricing model | |
| H10 | `11+ Jaar Security-Ervaring` | 26 | Trust | |
| H11 | `Vodafone, TNO En CFLW` | 21 | Social proof | |
| H12 | `Ook Voor AI-Gebouwde Apps` | 25 | Qualifier | |
| H13 | `Klaar Voor Due Diligence` | 24 | Outcome | |
| H14 | `Offerte Binnen 1 Werkdag` | 24 | CTA | |
| H15 | `Plan Een Gratis Gesprek` | 23 | CTA | |

| # | 🇳🇱 Description | Ch |
|---|---|---:|
| D1 | `Webapplicatie laten testen op kwetsbaarheden. Vaste prijs, rapport met prioriteiten.` | 84 |
| D2 | `Wij sporen lekken op in toegangsrechten, API's en database. Herstel ook mogelijk.` | 81 |
| D3 | `Uitgevoerd door engineers met 11+ jaar ervaring. Vodafone, TNO en CFLW gingen u voor.` | 85 |
| D4 | `Ook voor apps die met AI-tools zijn gebouwd. Offerte binnen 1 werkdag.` | 70 |

---

## 7. Độ phủ keyword sau khi sửa

| Keyword | Headline phủ | Ad group | Số lượng |
|---|---|---|:---:|
| `beveiligingsaudit webapplicatie` | H1, H2, H5 (+ nguyên cụm trong D1) | `Sec-Audit` | 3 + D1 |
| `security audit software laten doen` | H3, H4, H6 | `Sec-Audit` | 3 |
| `code audit laten uitvoeren` | H1, H2 (+ nguyên cụm trong D1) | `Sec-Code` | 2 + D1 |
| `applicatie beveiliging laten testen` | H3, H4, H5, H6 | `Sec-Code` | 4 |
| `avg compliance app` | H1, H2, H3, H6 | `Sec-AVG` | 4 |
| `pentest webapplicatie` | H1, H2, H3, H4 | `Sec-Pentest` | 4 |

**6/6 keyword được phủ** (trước: 1/6 khớp nguyên văn). Tổng: **60 headline + 16 description**.

---

## 8. ⚠️ Hai rủi ro về nội dung phải quyết trước khi chạy

### 8.1. 🔴 `pentest webapplicatie` — LaunchStudio có thật sự bán pentest không?

Đây là vấn đề nghiêm trọng nhất trong cả cụm, và nó **không phải vấn đề copywriting**.

Đối chiếu [`launchstudio_info.md`](launchstudio_info.md): sản phẩm là gói *Launch Ready* €800–3.500
và *Launch & Grow* €2.500–7.500, trong đó **Security là add-on +€500**. Không có chỗ nào mô tả một
**penetration test** đúng nghĩa (scope có cấu trúc, phương pháp, báo cáo để nộp cho khách hàng /
bảo hiểm / due diligence).

Người Hà Lan gõ `pentest webapplicatie` thường đang cần **một bản báo cáo pentest để đưa cho bên
thứ ba**. Nếu họ click, gọi điện, rồi phát hiện đây là code audit + fix, bạn mất tiền click và
mất uy tín.

**Ba lựa chọn, phải chọn một:**

| | Phương án | Khi nào chọn |
|---|---|---|
| **A** | Xác nhận có bán pentest → giữ nguyên ad group, bổ sung mô tả scope lên landing page | Nếu Manifera thật sự làm được |
| **B** | Đổi keyword sang `"security audit webapplicatie"`, tắt `pentest` | Nếu không làm pentest chính thức |
| **C** | Giữ `pentest` nhưng làm rõ ngay trên landing page: *"geen gecertificeerde pentest, wel een grondige security audit met herstel"* | Nếu muốn thử nghiệm nhưng không muốn hứa sai |

Mình **không** viết disclaimer đó vào ad copy — 90 ký tự là chỗ quá chật cho một câu phủ định,
và nó giết CTR. Chỗ đúng của nó là landing page.

### 8.2. 🟠 `avg compliance app` — đừng hứa "AVG-compliant"

AVG (Algemene verordening gegevensbescherming) là nghĩa vụ **pháp lý**, không phải trạng thái kỹ
thuật mà một agency có thể cấp cho khách. Không ai "làm cho app của bạn AVG-compliant" được, vì
compliance còn gồm verwerkersovereenkomst, bewaartermijnen, grondslag verwerking — việc của jurist.

Vì vậy mọi headline nhóm này đều nói về **rủi ro kỹ thuật**, không nói về trạng thái tuân thủ:
`AVG-Risico's In Kaart`, `Toegangsrechten Getest`, `Encryptie En Logging Check`. Bản AG4 cũ có
`AVG & Enterprise-proof` — cụm "proof" này hứa hơi quá, mình đã bỏ.

---

## 9. Checklist import

| # | Việc | Tác động |
|---|---|---|
| 1 | Nạp **15/15 headline + 4/4 description** cho cả bốn ad group | Quantity |
| 2 | Tách `AG-NL-Security` → 4 ad group theo §2, bid riêng cho `Sec-Pentest` (€9) và `Sec-AVG` (€5) | Relevance + CPC control |
| 3 | **Không pin** ở lần chạy đầu | Thường là bước cuối để lên Excellent |
| 4 | Bỏ ký tự `·` trong `Vodafone · TNO · CFLW` → đã đổi thành `Vodafone, TNO En CFLW` | Tránh disapproval |
| 5 | Quyết §8.1 trước khi bật `Sec-Pentest` | Rủi ro thật, không phải rủi ro điểm số |
| 6 | Người Hà Lan bản xứ review — soi kỹ `Vaste Prijs, Geen Nacalc.` (viết tắt) và `Rapport In Heldere Taal` | Chất lượng ngôn ngữ |

> **Nhắc lại:** Ad Strength **không phải yếu tố xếp hạng**, không đi vào Ad Rank. Nó là thước đo
> định hướng. Cái thật sự đáng theo đuổi là relevance — điểm số sẽ lên theo.

---

## 10. Nguồn tham chiếu

- [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md) §5.1 — campaign C1, bid & landing page
- [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) — bản nháp AG4 NL, CPC ước tính, ghi chú rủi ro pentest
- [`launchstudio_info.md`](launchstudio_info.md) — gói dịch vụ & giá, dùng để kiểm chứng §8.1
- [`google_ads_rsa_nl_rescue_headlines.md`](google_ads_rsa_nl_rescue_headlines.md) — cụm `AG-NL-Rescue` (ngôi `je`)
