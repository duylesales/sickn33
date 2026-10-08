# 🌉 Landing page `/ai-app-to-production` (NL) — Content brief + Lovable prompt

> **Ngày:** 08/10/2026 · **Ngôn ngữ trang:** 🇳🇱 Tiếng Hà Lan
> **Keyword:** `ai app laten bouwen` · `mvp laten bouwen` · `prototype naar productie` · `ai app laten afmaken` · `prototype live zetten` · `app productieklaar maken`
> **Liên quan:** `google_ads_rsa_nl_rescue_headlines.md` (3 ad group + RSA copy) · `google_search_ads_plan_3_ai_brands.md` §2.7 (volume, ICP) · `launchstudio_info.md` (dữ kiện, testimonial) · `landing_ai_app_into_production_brief.md` (bản EN)
> **Thương hiệu:** giữ màu, font, gradient của `launchstudio.eu` · **Phong cách:** tiết chế, một loại minh hoạ duy nhất

---

## 1. ⚠️ Bốn điều cần biết trước khi build

### ① Sáu keyword = ba ý định khác nhau → dùng **một URL, H1 đổi theo ad group**

`google_ads_rsa_nl_rescue_headlines.md` §1.2 đã tách đúng:

| Ad group | Keyword | Khách đang ở đâu |
|---|---|---|
| `AG-NL-Live` | `prototype naar productie`, `prototype live zetten` | Có prototype chạy được, kẹt ở bước đưa lên live |
| `AG-NL-Afmaken` | `ai app laten afmaken`, `app productieklaar maken` | App dở dang, thiếu phần cuối |
| `AG-NL-Bouwen` | `ai app laten bouwen`, `mvp laten bouwen` | **Chưa có gì**, đang tìm người làm |

Ba trang riêng thì quá tốn công cho volume này. **Giải pháp:** cùng một trang, nhưng **pill phía trên H1, H1 và sub tự đổi** theo tham số `ag` trong Final URL của từng ad group:

```
AG-NL-Live     → Final URL suffix: ag=live
AG-NL-Afmaken  → Final URL suffix: ag=afmaken
AG-NL-Bouwen   → Final URL suffix: ag=bouwen
```

H1 chứa đúng keyword của nhóm quảng cáo → khớp thông điệp, tốt cho Landing Page Experience. Không có `ag` (organic) thì trang hiển thị bản mặc định (`live`).

### ② 🔴 Nhóm `bouwen` là người "ICP lệch"

`google_search_ads_plan_3_ai_brands.md` §2.7: phần lớn volume kiểu `laten bouwen` là người muốn **xây mới**, không phải người có prototype dở dang. Vì vậy:
- Pain ở hero vẫn nhắm **người đã có prototype** (4/6 keyword, đúng ICP).
- Thêm section **"Twee startpunten"** (S4) để người chưa có gì tự nhận ra mình và đi đúng đường, thay vì bỏ trang.
- Khi `ag=bouwen`, thẻ "Ik begin bij nul" được đưa lên trước và highlight.

### ③ Khớp thông điệp với quảng cáo đang chạy

RSA hiện hứa: `Gratis Code-Review Vooraf` · `Live Binnen 1-3 Weken` · `Geen Herbouw` · `100% Eigendom Van Je Code` · `11+ Jaar Engineering Ervaring` · **`Vaste Prijs Vanaf €800`**.

Trang dưới đây có đủ các lời hứa trên, **trừ con số €800**, vì yêu cầu không có phần giá. ⚠️ Quảng cáo nói €800 mà trang không nhắc tới thì người click sẽ thấy hụt. **Chọn một trong hai:**
- (a) Thêm một chip `Vaste prijs vanaf €800` ở hàng trust của hero (prompt đã để sẵn comment), **hoặc**
- (b) Bỏ các headline có €800 (H3/H7 Bouwen, H3/H10 Afmaken, H5/H10 Live).

### ④ URL

- Root `launchstudio.eu/` là namespace **NL**, nên slug tiếng Anh `/ai-app-to-production` cạnh `/en/ai-app-into-production` dễ gây nhầm ("to" và "into"). Plan RSA lại đang trỏ tới `/nl/van-prototype-naar-productie`.
- **Đề xuất:** dùng slug NL chứa keyword, ví dụ `launchstudio.eu/van-prototype-naar-productie`, gắn hreflang với bản EN `/en/ai-app-into-production`, và cập nhật Final URL của 3 ad group cho thống nhất.
- Nếu vẫn giữ `/ai-app-to-production` thì vẫn cần hreflang với bản EN.

> 💡 Volume thật của nhóm `afmaken / naar productie / live zetten` gần bằng 0 (§2.7). Trang này sống chủ yếu nhờ **ads** và **GEO**, không nhờ organic. FAQ ở S8 viết dạng câu hỏi người Hà Lan hay hỏi ChatGPT.

---

## 2. 🎨 Phong cách: "Dutch calm" + một hình minh hoạ: **cây cầu kéo (ophaalbrug) bị kẹt**

### Giữ (nhận diện thương hiệu)

```css
:root{
  --navy:#0B1D35; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
}
```

### Minh hoạ: cây cầu kéo kiểu Hà Lan

**Một loại minh hoạ duy nhất cho cả trang:** flat vector, nét navy 2px, mảng màu gradient thương hiệu, nhiều khoảng trắng.

| Vị trí | Trạng thái của cây cầu | Ý nghĩa |
|---|---|---|
| **Hero** | Cầu **kẹt ở thế dựng đứng**, cố hạ xuống rồi bật lên lại. Đèn báo trên cầu chớp đỏ/vàng. Bờ trái ghi `Prototype`, bờ phải ghi `Live · echte klanten`. Có 4 tấm ván thiếu: *Inloggen · Betalingen · Beveiliging · Hosting* | "De brug naar live staat open": app có rồi nhưng không qua được |
| **Solution** | Cầu **hạ xuống**, 4 tấm ván khớp vào và chuyển xanh, một chiếc xe nhỏ "Jouw app" chạy sang bờ Live | LaunchStudio hoàn thiện phần còn thiếu |
| **CTA cuối** | Bản nhỏ, cầu đã hạ, xe qua lại đều đặn | Trạng thái mong muốn |

> 💡 **Vì sao chọn cây cầu kéo:** người Hà Lan thấy *ophaalbrug* hằng ngày, và câu *"de brug staat open"* (cầu đang mở = không qua được) là trải nghiệm ai cũng hiểu. Hình ảnh mang tính địa phương này các đối thủ quốc tế không có, và nó diễn tả đúng nỗi đau "chỉ còn một đoạn cuối mà không qua được".

### "Tiết chế" nghĩa là

- Nền trắng / `--bg`. **Không** nền tối, lưới, kính mờ, mảng pastel, hay font mono (khác cả 4 trang trước).
- Chỉ **hero, solution và CTA cuối** có animation, và đều là cùng cây cầu. Các section khác tĩnh, chỉ fade nhẹ khi cuộn tới.
- Heading dùng **sentence case** (chuẩn tiếng Hà Lan), không Title Case.
- Gradient chỉ dùng cho nút chính, mặt nước và một từ nhấn.

| | Vibe-coding | Into-production | Security | Integrations | **To-production (NL)** |
|---|---|---|---|---|---|
| Không khí | Tối, chat | Editorial, đếm ngược | Kính, X-ray | Pastel, dây dẫn | **Trắng, tĩnh, minh hoạ phẳng** |
| Hình chính | Khung chat AI | Bảng Launch Control | Thấu kính | Sơ đồ đồng xu | **Cây cầu kéo Hà Lan** |

---

## 3. 📝 Cấu trúc — Pain ngay section đầu → Solution → bổ trợ → CTA

Không có giá, không có form. CTA trỏ ra trang liên hệ NL.

| # | Section | Vai trò | Thông điệp |
|---|---|---|---|
| S1 | **Hero = Pain** (chữ trái, cầu phải, ngang nhau) | 🪝😬 | `Je prototype werkt. De brug naar live staat open.` (đổi theo `ag`) |
| S2 | Herken je dit? | 😬 Đào sâu | 4 câu founder hay tự nói, bắt đầu từ `"Nog één prompt en dan werkt het."` |
| S3 | **Wij maken de brug af** | ✅ Solution | Cầu hạ xuống, 4 ván khớp vào · Wat blijft / wat we toevoegen |
| S4 | Twee startpunten | Phân luồng | "Ik heb al een prototype" / "Ik begin bij nul" (cho nhóm `bouwen`) |
| S5 | Werkwijze | Bổ trợ | Gratis code-review → vaste scope → live in 1–3 weken |
| S6 | Vergelijking | Bổ trợ | Bureau / freelancer / LaunchStudio, không có giá |
| S7 | Bewijs | Bổ trợ | Manifera 11+ jaar, 160+ projecten · testimonial Marieke, Jasper |
| S8 | FAQ | Bổ trợ + GEO | 5 câu chứa keyword |
| S9 | **Final CTA** | 🎯 | Cầu đã hạ: `Zet je prototype live.` |

### H1 động theo `ag`

| `ag` | Pill | H1 | Sub (câu đầu) |
|---|---|---|---|
| `live` (mặc định) | `Prototype naar productie?` | Je prototype werkt. De brug naar live staat open. | In de preview werkt alles. Maar echte klanten vragen om inloggen, betalingen, beveiliging en hosting — en daar loopt het vast. |
| `afmaken` | `AI-app laten afmaken?` | 80% is gebouwd. De laatste 20% houdt je tegen. | Je app is bijna af, maar "bijna" kun je niet lanceren. |
| `bouwen` | `AI-app of MVP laten bouwen?` | Snel bouwen kan iedereen. Productieklaar is het echte werk. | Een AI-tool bouwt in een weekend een demo. Voor echte klanten heb je inloggen, betalingen, beveiliging en hosting nodig. |

---

## 4. 🤖 Prompt cho Lovable.dev

> Paste nguyên khối. Hướng dẫn bằng tiếng Anh (Lovable xử lý tốt hơn), **nội dung trang bằng tiếng Hà Lan**.

```
Build a single, self-contained landing page as ONE static `index.html` file: all CSS in
one inline <style> block, all JS in one inline <script> block. No React, no build step,
no router, no external dependencies except the three font links below. It will be
pasted into a WordPress page template, so it must work standalone.
The page language is DUTCH: <html lang="nl">. All visible copy below is final Dutch
copy — use it exactly as written. Headings use Dutch sentence case, not Title Case.

WHAT THIS PAGE IS
LaunchStudio (backed by Manifera, 11+ years of software engineering) takes apps and
prototypes built with AI tools — Lovable, Bolt, Replit, Cursor, v0 — and makes them
production-ready: login, payments, security, hosting on the client's own domain. No
rebuild: the frontend stays. Live in 1–3 weeks at a fixed scope. LaunchStudio also
builds MVPs from scratch, production-ready from day one.
Audience: Dutch founders whose prototype works in the preview but cannot go live.
The PAIN is the very first thing on the page. Arc: PAIN → SOLUTION → short supporting
sections → final CTA. Tone: calm, direct, warm, no hype, never mocking AI tools.
There is NO pricing section and NO form; every CTA links out.

ONE ILLUSTRATION, THE WHOLE PAGE: a Dutch bascule drawbridge (ophaalbrug) over a canal.
"De brug staat open" — the bridge is up, so you cannot cross to "Live". The hero shows
it stuck; the solution shows it lowering; the final CTA shows traffic crossing.

=== BRAND — KEEP EXACTLY ===
:root{
  --navy:#0B1D35; --bg:#F8FAFE; --white:#FFF;
  --ok:#0D9668; --red:#DC2626; --amb:#D97706;
  --gs:#2F80ED; --ge:#14B8A6;
  --grd:linear-gradient(135deg,#2F80ED 0%,#14B8A6 100%);
  --text:#0B1D35; --ts:#384860; --tm:#64748B; --tf:#94A3B8;
  --bd:#E2E8F0; --bs:#EEF2F7;
  --fh:'Satoshi',system-ui,sans-serif;
  --fb:'Inter',system-ui,sans-serif;
  --fa:'Instrument Serif',Georgia,serif;
  --rp:999px; --rs:12px; --rl:20px;
  --t:.3s; --ease:cubic-bezier(.22,1,.36,1);
}
FONTS — exactly these three. Satoshi is from Fontshare, NOT Google Fonts. Never
substitute:
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">

=== STYLE — "DUTCH CALM" (restrained) ===
- White and var(--bg) backgrounds only. NO dark sections, NO background grids, NO
  glassmorphism, NO pastel section washes, NO monospace font, NO marquee, NO
  parallax. Lots of whitespace. Sections separated by space and a single 1px var(--bd)
  hairline at most.
- Typography: h1 var(--fh) 900, clamp(38px,5.2vw,64px), line-height 1.04,
  letter-spacing -2px · h2 var(--fh) 700, clamp(28px,3.6vw,44px), line-height 1.1,
  letter-spacing -1px · h3 var(--fh) 700, 19px · body var(--fb) 17px/1.7, var(--ts).
  Tight negative letter-spacing on headings is the brand signature.
- Small labels: 13px var(--fh) 600, var(--gs), no uppercase.
- var(--fa) italic for at most 2 emphasis phrases on the page.
- Cards: white, 1px solid var(--bd), radius var(--rl), shadow
  0 1px 2px rgba(11,29,53,.04), 0 8px 24px rgba(11,29,53,.05). No hover tricks beyond a
  1px border colour change to rgba(47,128,237,.3).
- Primary button: var(--grd), white, radius var(--rp), padding 16px 30px, var(--fh) 700,
  arrow slides 3px on hover, hover lift 2px + shadow 0 14px 32px rgba(47,128,237,.25).
  Secondary: transparent, 1px solid var(--bd), var(--navy), radius var(--rp).
- Only three animated places on the page, all the same drawbridge: S1, S3, S9.
  Everything else is static apart from a gentle 400ms fade-up when it enters view.
- Max width 1160px, 24px side padding (16px under 768px). Sections 104px 0 desktop,
  72px 0 mobile.

ILLUSTRATION SPEC (inline SVG, flat vector):
- Line style: 2px var(--navy) strokes, round caps. Fills: white, var(--bs) for stone and
  buildings, the brand gradient for the canal water (at 25% opacity, with 2–3 lighter
  wave lines), var(--grd) for small accents.
- Scene, left to right: LEFT BANK with a small modest building and a laptop-shaped sign
  "Prototype" plus a tiny URL tag "preview"; the CANAL in the middle; the DRAWBRIDGE: a
  classic Dutch double-pole white ophaalbrug (two upright posts, a top beam, the
  counterweight frame and the deck that pivots at the right-hand side); RIGHT BANK with
  a row of three narrow Dutch canal-house facades and a small group of simple people
  icons, labelled "Live · echte klanten".
- The deck has FOUR plank slots labelled in 11px var(--fh) 600: "Inloggen",
  "Betalingen", "Beveiliging", "Hosting". In the stuck state the slots are dashed
  outlines with small amber "!" markers.
- On the left bank, a small rounded van with "Jouw app" on its side waits at a red/white
  barrier (slagboom).
- Two small warning lights on the bridge posts.
- No people faces, no text other than the labels above, no emoji.

=== SECTIONS, IN ORDER ===

S1 HERO = PAIN. Background var(--bg). TWO EQUAL COLUMNS SIDE BY SIDE (CSS grid
1fr 1fr, gap 56px, vertically centred): copy LEFT, illustration RIGHT. On mobile: copy
first, illustration directly below at full width.
LEFT (default copy = variant "live"; see DYNAMIC COPY below):
- Pill (white, 1px var(--bd), radius var(--rp), 14px var(--fh) 600, small gradient dot):
  id="kw-pill" → "Prototype naar productie?"
- H1 id="kw-h1": 'Je prototype werkt. <em>De brug naar live staat open.</em>'
  (em = var(--fa) italic weight 400, gradient text fill)
- Sub id="kw-sub", 18px, max 520px: "In de preview van Lovable, Bolt of Cursor werkt
  alles. Maar echte klanten vragen om inloggen, betalingen, beveiliging en hosting — en
  daar loopt het vast. Wij maken je app productieklaar, zonder opnieuw te bouwen."
- Three pain rows, each: a 32px circle with a small amber warning icon, and one line in
  16px var(--navy) var(--fb) 500. Each row has data-plank pointing to a plank on the
  bridge; hover/focus on the row makes that plank's "!" pulse.
    "Het werkt in de preview, maar niet op je eigen domein."      → Hosting
    "Elke fix via een prompt breekt weer iets anders."             → Inloggen
    "Je weet niet of klantdata en betalingen veilig zijn."         → Beveiliging + Betalingen
- Buttons: primary "Vraag een gratis code-review aan" (data-cta), secondary
  "Zo maken wij het af" (href #oplossing).
- Trust row, 14px var(--tm), separated by small dots, with tiny check SVGs:
  "Geen herbouw" · "Code 100% van jou" · "Live in 1–3 weken"
  <!-- OPTIONAL: add "Vaste prijs vanaf €800" here if the Google Ads keep the €800
  headlines (message match) -->
RIGHT — THE STUCK BRIDGE (animated SVG, no card frame; it sits on the page):
- The deck is raised at about 70°. Every 4 seconds it tries to lower: it rotates down
  to about 45° over 900ms with an ease-out, shudders (two tiny ±1.5° wobbles), then
  swings back up to 70°. During the attempt the two warning lights blink var(--amb),
  then glow var(--red) when it swings back.
- The van behind the barrier inches forward 6px during each attempt and rolls back.
- The water lines drift slowly left to right (8s loop).
- A small caption under the illustration, 13px var(--tm), centred:
  "De brug staat open. Je app kan niet naar de overkant."
- prefers-reduced-motion: static, deck raised at 70°, lights red.

S2 PAIN — "HERKEN JE DIT?" Background white.
- Label: "Herken je dit?"
- H2: "De laatste 20% kost meer tijd dan de eerste 80%."
- Four cards in a 2x2 grid (1 column on mobile). Each card: the quote as h3 in
  var(--navy) with typographic Dutch quotes „…", then one line below in var(--ts).
    „Nog één prompt en dan werkt het." — "Drie weken later zit je nog steeds in
     dezelfde loop."
    „Een freelancer snapt mijn AI-code niet." — "Eerst weken inlezen, of alles
     herschrijven."
    „Een bureau wil helemaal opnieuw beginnen." — "Maanden werk en een offerte van
     tienduizenden euro's, voor iets wat al bijna af is."
    „Wat als het misgaat met echte klanten?" — "Gelekte data of mislukte betalingen
     kosten meer dan een late lancering."

S3 SOLUTION — id="oplossing". Background var(--bg). TWO EQUAL COLUMNS, MIRRORED:
illustration LEFT, copy RIGHT.
LEFT — the SAME bridge scene. When the section scrolls into view (once):
  1. the deck lowers smoothly from 70° to 0° (1.4s, ease-in-out);
  2. the four plank slots fill one by one (200ms apart): dashed outline → solid white
     plank with a gradient top edge, and each label gets a small green check;
  3. warning lights turn var(--ok);
  4. the barrier lifts and the "Jouw app" van drives across to the right bank, where a
     tiny green check appears above the people icons.
  prefers-reduced-motion: show the final state.
RIGHT:
- Label: "De oplossing"
- H2: "Wij maken de brug af."
- Sub: "We behouden wat je gebouwd hebt, fixen alleen wat live gaan blokkeert, en zetten
  je app op je eigen domein."
- Two short lists side by side (stack on mobile), each with small icons:
  "Wat blijft" (check icons, var(--ok)): Je ontwerp en frontend · Je logica en
   functies · Je data · Het werk dat je al gedaan hebt
  "Wat wij toevoegen" (plus icons, var(--gs)): Inloggen en accounts · Betalingen
   (Stripe, iDEAL) · Beveiliging · Hosting op je eigen domein
- Primary button "Vraag een gratis code-review aan" (data-cta).

S4 TWEE STARTPUNTEN — id="startpunt". Background white.
- H2: "Waar sta jij?"
- Two cards side by side, equal width:
  Card "prototype" — h3 "Ik heb al een prototype" — text: "Gebouwd met Lovable, Bolt,
   Replit, Cursor of v0? Wij maken het af en zetten het live." — link-button "Gratis
   code-review" (data-cta, adds start=prototype)
  Card "nul" — h3 "Ik begin bij nul" — text: "AI-app of MVP laten bouwen? Wij bouwen met
   de snelheid van AI en leveren meteen productieklaar op: accounts, betalingen,
   beveiliging en hosting vanaf dag één." — link-button "Plan een kennismaking"
   (data-cta, adds start=nul)
- The card matching the current variant gets a 1px var(--gs) border and a small pill
  "Dit ben jij" (variant bouwen → card "nul" first and highlighted; otherwise card
  "prototype" first and highlighted).

S5 WERKWIJZE. Background var(--bg).
- H2: "Van prototype naar productie in drie stappen."
- Three steps in a row (stack on mobile), each with a large step number in gradient
  text (var(--fh) 900 40px), h3 and one line. A thin 1px var(--bd) line connects them.
  1 "Gratis code-review" — "Stuur je prototype-link of repo. Binnen één werkdag weet je
    wat live gaan blokkeert."
  2 "Vaste scope, vaste prijs" — "Je weet vooraf precies wat we doen, hoe lang het duurt
    en wat het kost."
  3 "Live in 1–3 weken" — "Getest, op je eigen domein, met 48 uur support na de
    lancering. De code is van jou."

S6 VERGELIJKING. Background white.
- H2: "Waarom niet een bureau of een freelancer?"
- A real <table>, max 860px, columns: (empty) | "Traditioneel bureau" | "Freelancer" |
  "LaunchStudio" (last column header with a small gradient underline, cells in
  var(--navy) 600).
  "Opnieuw bouwen?"        — "Meestal wel" | "Soms" | "Nee, we bouwen door"
  "Begrijpt AI-code?"      — "Zelden" | "Vaak niet" | "Ja, dagelijks werk"
  "Doorlooptijd"           — "3–12 maanden" | "Onvoorspelbaar" | "1–3 weken"
  "Prijs vooraf vast?"     — "Zelden" | "Soms" | "Altijd"
- No prices in the table.

S7 BEWIJS. Background var(--bg).
- H2: "Gebouwd door engineers, niet door prompts."
- Two stats in gradient text, var(--fh) 900 52px, labels 14px var(--tm):
  "11+" — "jaar engineering via Manifera" · "160+" — "projecten opgeleverd"
- Two testimonial cards: quote in var(--fa) italic 21px, then name and role 14px
  var(--tm):
  „Ik heb drie maanden lang heen en weer gecommuniceerd met een freelancer die mijn
   Cursor-code niet begreep. LaunchStudio heeft mijn MVP binnen 10 dagen live gezet."
   — Marieke, oprichter SaaS voor personal trainers
  „Als SaaS-oprichter wil je snel en tegen lage kosten testen en lanceren. Het kost me
   slechts 20% van wat ik normaal aan ontwikkeltijd zou uitgeven."
   — Jasper, oprichter Wisey
  <!-- VERIFY both quotes word for word against launchstudio.eu before publishing -->
- Do NOT add client logos, certification badges or award seals.

S8 FAQ. Background white. <details>/<summary> accordion, max 780px, plus icon
rotating 45°. Mark up with FAQPage JSON-LD in a <script type="application/ld+json">.
- H2: "Veelgestelde vragen"
  "Kunnen jullie mijn AI-app afmaken zonder alles opnieuw te bouwen?" — "Ja. We
   behouden je frontend en je logica, en voegen toe wat ontbreekt om live te gaan:
   inloggen, betalingen, beveiliging en hosting."
  "Hoe snel kan mijn prototype live staan?" — "Meestal binnen 1 tot 3 weken. De
   precieze planning leggen we vooraf vast, samen met de scope."
  "Met welke tools werken jullie?" — "Lovable, Bolt, Replit, Cursor, v0 en gewone
   codebases in bijvoorbeeld React, Next.js of Supabase."
  "Kunnen jullie ook een MVP vanaf nul bouwen?" — "Ja. We bouwen met AI-snelheid,
   maar leveren meteen productieklaar op, zodat je niet later alsnog vastloopt."
  "Van wie is de code?" — "Van jou. Altijd. Je repo, je accounts, je domein."

S9 FINAL CTA. Background var(--bg). Centred, max 760px.
- A smaller version of the bridge scene (max 560px wide), deck DOWN, planks complete,
  lights green; small vans drive across from left to right in a slow loop (one every
  3s). Static under reduced motion.
- H2: 'Zet je prototype <span class=grad>live.</span>'
- Sub: "Gratis code-review. Binnen één werkdag weet je waar je staat."
- Primary button, larger: "Vraag een gratis code-review aan" (data-cta)
- Small line, 14px var(--tm): "Of plan een kennismaking van 15 minuten." (data-cta,
  adds type=call)

FOOTER: one slim row, 13px var(--tm): "© LaunchStudio · onderdeel van Manifera ·
launchstudio.eu"

=== DYNAMIC COPY (message match with Google Ads) ===
Read the `ag` query parameter (values: live, afmaken, bouwen; default live) and set
the hero pill, H1 and sub, and the S4 card order:
- live:
  pill "Prototype naar productie?"
  H1 'Je prototype werkt. <em>De brug naar live staat open.</em>'
  sub (as in S1)
- afmaken:
  pill "AI-app laten afmaken?"
  H1 '80% is gebouwd. <em>De laatste 20% houdt je tegen.</em>'
  sub "Je app is bijna af, maar „bijna" kun je niet lanceren. Wij maken hem
  productieklaar — inloggen, betalingen, beveiliging en hosting — zonder opnieuw te
  bouwen."
- bouwen:
  pill "AI-app of MVP laten bouwen?"
  H1 'Snel bouwen kan iedereen. <em>Productieklaar is het echte werk.</em>'
  sub "Een AI-tool bouwt in een weekend een demo. Voor echte klanten heb je inloggen,
  betalingen, beveiliging en hosting nodig. Wij bouwen je MVP direct productieklaar —
  of maken af wat je al hebt."
Also set document.title accordingly (e.g. "AI-app laten afmaken | LaunchStudio").
The static HTML must contain the "live" variant so the page works without JS.

=== JS (vanilla, small) ===
- const CTA_URL = "https://launchstudio.eu/#contact"; // REPLACE with the real Dutch
  contact or booking URL. Every [data-cta] gets href = CTA_URL + query params.
- Attribution: copy gclid, gbraid, wbraid, utm_source, utm_medium, utm_campaign,
  utm_term, utm_content and ag from location.search onto every data-cta link, plus
  landing=ai-app-to-production and any per-button params (start, type).
- Bridge animations: CSS transforms on SVG groups (transform-box: fill-box;
  transform-origin at the deck's hinge), driven by classes; pause the hero loop when it
  is off-screen (IntersectionObserver) or the tab is hidden. S3 sequence runs once.
- Pain row ↔ plank highlight.

=== TECHNICAL REQUIREMENTS ===
- Semantic HTML, exactly one <h1>, <section aria-labelledby>, <button> for actions,
  <a> for links. The illustrations are decorative (aria-hidden) with a visually-hidden
  Dutch description: "Illustratie: een ophaalbrug die openstaat, zodat de app niet
  naar de kant met echte klanten kan."
- Two-column sections use CSS grid 1fr 1fr with vertical centring on desktop and a
  single column under 768px. No horizontal scroll at 360px; the bridge scales to full
  width and its labels stay legible (min 11px).
- Contrast at least 4.5:1. Visible focus rings (2px solid var(--ge), 3px offset).
- prefers-reduced-motion: all bridge scenes static in their final state for that
  section (S1 raised, S3 and S9 lowered).
- One HTML file, inline CSS and JS, only the three font links external.
```

---

## 5. ✅ Việc cần làm sau khi Lovable trả kết quả

| # | Việc | Ghi chú |
|---|---|---|
| 1 | 🔴 **Người Hà Lan bản xứ đọc lại toàn bộ copy** | Đặc biệt: `De brug naar live staat open`, `Snel bouwen kan iedereen`, `Wij maken de brug af`. Yêu cầu này đã có trong `google_ads_rsa_nl_rescue_headlines.md` §8.4 |
| 2 | 🔴 **Gắn `ag=live / afmaken / bouwen` vào Final URL suffix** của 3 ad group | Không gắn thì H1 động không chạy, mọi người đều thấy bản `live` |
| 3 | 🔴 **Quyết định €800** (§1③) | Thêm chip vào hero, hoặc bỏ các headline €800 khỏi RSA |
| 4 | 🔴 **Thay `CTA_URL`** | Đang để `https://launchstudio.eu/#contact`. Kiểm tra `gclid`, `utm_*`, `ag`, `start` có đi theo |
| 5 | Xác minh nguyên văn testimonial Marieke và Jasper | Mình lấy từ `launchstudio_info.md` §6.1; câu của Marieke trong file bị cắt "…" |
| 6 | Xác minh "binnen één werkdag", "48 uur support", "1–3 weken" | Lấy từ `launchstudio_info.md`; phải khớp gói đang bán |
| 7 | **Chốt URL + hreflang** (§1④) | Đề xuất `/van-prototype-naar-productie` ↔ `/en/ai-app-into-production`, cập nhật Final URL của RSA |
| 8 | Kiểm tra cây cầu trên mobile 360px | Nhãn ván phải đọc được, animation không giật |
| 9 | Index | Nên `index`: FAQ có schema `FAQPage`, phục vụ GEO tiếng Hà Lan |
| 10 | Middleware cookie `ls_click` | `conversion_attribution_setup.md` §2②, ghi nhận ở trang liên hệ |
