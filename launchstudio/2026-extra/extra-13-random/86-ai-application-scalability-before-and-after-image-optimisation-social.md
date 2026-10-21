🚨 Vera Lammers rents out four holiday homes near Valkenburg and built Vakantiehuisje with v0 and a simple booking backend: full-width galleries of each home and the South Limburg hills, with direct booking to avoid platform commissions. The photos came straight from a professional photographer — 6 to 10 MB each. The homepage weighed 48 MB. 😳

On mobile, the first photo took about nine seconds to appear. Search Console flagged most pages "poor" for Core Web Vitals. Most visitors arrived from Instagram on their phones and left before the page finished loading. The hosting bandwidth limit was exceeded twice in the spring holiday, and guest review photos kept their GPS data. Here's AI application scalability before and after image optimisation: 🧠

❌ Original camera files served in 400-pixel cards
❌ Everything loading at once, with no dimensions declared
❌ No CDN, no modern formats
❌ Location metadata kept in guest photos

✅ An upload pipeline generating AVIF and WebP variants in four sizes
✅ Responsive galleries with lazy loading below the fold and eager loading for the hero image
✅ Declared image dimensions and CDN delivery with long cache lifetimes
✅ Metadata stripped from existing and new uploads, and the whole photo library reprocessed

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we change your pages' weight — never the design your visitors love. ⚙️

Her result: €1,400, five business days. The homepage dropped from 48 MB to about 1.9 MB, the main image appears in roughly a second on 4G, most pages moved to "good", direct bookings rose by about a quarter — and bandwidth fell below the plan's limit. 🚀

👉 AI application scalability: before and after image optimisation: https://launchstudio.eu/en/blog/ai-application-scalability-before-and-after-image-optimisation

#WebPerformance #CoreWebVitals #v0 #HolidayRental #LaunchStudio #Manifera
