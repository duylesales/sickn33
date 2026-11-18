📝 REPORT CARD: Cursusplein, a course marketplace with 210 providers

Laptop page speed score .......... 88 (the grade the founder trusted)

Field data, 75th percentile, real visitors:
LCP (largest element visible) .... 5.8 s ❌
INP (response to taps) ........... 410 ms ❌
CLS (layout shift) ............... 0.34 ❌

Visitors on phones ............... roughly 70%
Mobile booking conversion ........ a third of desktop

Teacher's comment: "Assumed to be a behaviour difference. It was performance."

Nienke Brandts built Cursusplein in Lovable, where learners search, compare and book training courses. Her customers weren't on laptops. They were on phones, on trains. 🚆

The tutoring (LaunchStudio, 2 business days, €2,900):
✓ Listing and detail pages statically generated with server-rendered HTML, which alone moved LCP from 5.8 to 2.1 s
✓ The listing hero image given explicit dimensions and taken out of lazy loading, which had been delaying the largest element on purpose
✓ Thumbnails in modern formats at display size: a listing page from 3.8 MB to 340 KB
✓ JavaScript split by route, with three libraries removed from the public bundle (a date library, a charting library used on one admin screen, and a component library used for two buttons): 780 KB to 190 KB
✓ Two fonts self-hosted, one preloaded, with a fallback stack, replacing a third-party import
✓ The chat widget kept only in the booking flow
✓ Space reserved for the provider logo and availability banner, which had caused most of the shift
✓ Everything tested on a four-year-old Android phone on a throttled connection

THE NEW REPORT CARD
LCP .............................. 1.9 s ✅
INP .............................. 140 ms ✅
CLS .............................. 0.02 ✅
Mobile booking conversion ........ 1.1% ➜ 2.9% over two months
Worth ............................ roughly €4,100 a month in commission

Rankings improved modestly. The conversion change was the one that mattered.

"My score on a laptop was 88 and I thought I was finished. My actual customers were on phones on trains, and for them the site took six seconds and then moved while they were tapping." - Nienke Brandts

https://launchstudio.eu/en/blog/lovable-seo-core-web-vitals-in-an-ai-built-frontend

#CoreWebVitals #WebPerformance #SEO #Lovable #LaunchStudio #Manifera
