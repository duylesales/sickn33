---
Title: "AI Application Scalability Before and After Image Optimisation"
Keywords: ai application scalability, image optimisation, core web vitals, cdn images, v0 website performance, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Application Scalability Before and After Image Optimisation

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Application Scalability Before and After Image Optimisation",
  "description": "Images are often the heaviest part of AI-built sites and apps. A before-and-after look at how unoptimised images hurt AI application scalability, page speed, costs and search — and how resizing, modern formats, lazy loading and CDNs fix it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-25",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-application-scalability-before-and-after-image-optimisation" }
}
</script>

When founders think about AI application scalability, they picture databases and servers. For many AI-built websites and apps, though, the heaviest thing on every page is much more ordinary: images. A holiday rental site, a webshop, a portfolio or a marketplace can serve several megabytes of photos per visit. With a handful of visitors, nobody notices. With thousands, images drive slow pages, high bandwidth bills and weaker search rankings — and they are among the easiest problems to fix.

## Before: How AI-Built Sites Handle Images

Tools like v0, Lovable and Bolt produce good-looking layouts, and founders fill them with the best photos they have — straight from a camera or phone. The typical result:

- **Original files served as-is,** often 3–8 MB each, at 4000+ pixels wide, displayed in a 400-pixel card.
- **Old formats only** (JPEG and PNG), with no modern formats like WebP or AVIF.
- **Everything loads at once,** including images far down the page.
- **No dimensions declared,** so the page jumps as images load.
- **Served from the app's storage,** not from a CDN close to visitors.
- **User uploads stored as uploaded,** including location metadata.

## What Unoptimised Images Cost AI Application Scalability

**Speed.** On mobile connections, a page with ten full-size photos can take many seconds to show its main image. Google's Largest Contentful Paint measure — how quickly the main content appears — suffers directly.

**Layout stability.** Images without declared dimensions push content around while loading, hurting Cumulative Layout Shift and annoying users who tap the wrong button.

**Bandwidth and storage.** Serving megabytes per page view multiplies hosting and storage bills as traffic grows.

**Conversion.** Slow pages lose visitors before they see what you offer.

**Search.** Core Web Vitals are part of Google's ranking signals; slow, unstable pages are at a disadvantage.

**Privacy.** Photos uploaded by users can reveal where they were taken.

## After: The Optimisation Checklist

1. **Resize on upload** into several widths (for example 400, 800, 1600 pixels).
2. **Serve modern formats** (WebP or AVIF) with fallbacks.
3. **Use responsive images** so each device downloads an appropriate size.
4. **Lazy-load** images below the fold; load the main image eagerly.
5. **Declare width and height** (or aspect ratio) to prevent layout shifts.
6. **Serve through a CDN** with long cache lifetimes.
7. **Strip metadata** from user uploads.
8. **Compress sensibly** — good quality at a fraction of the size.
9. **Process in the background** so uploads stay fast.

Frameworks like Next.js include image components that handle much of this; managed image services and storage providers offer on-the-fly transformation. The main work is wiring it in consistently.

## Before and After, Typically

| | Before | After |
| --- | --- | --- |
| Image weight per page | Several MB | A few hundred KB |
| Main image on mobile | Seconds | Around a second or less |
| Layout shifts | Frequent | Minimal |
| Bandwidth cost | High, grows with traffic | Low, mostly cached at CDN |
| User photo metadata | Kept | Removed |

The exact numbers depend on the site, but reductions of 70–90% in image weight are common.

## An Image Pipeline, Step by Step

For AI application scalability, a production image pipeline for user uploads and content images looks like this:

1. **Upload directly to storage** via a short-lived signed URL, so large files do not pass through your application servers.
2. **Trigger processing** in a background job when the upload completes.
3. **Validate** the file: actual type, dimensions, size limits.
4. **Strip metadata**, including GPS location and camera details.
5. **Generate variants**: for example 400, 800, 1200 and 1600 pixels wide, in AVIF and WebP, plus a JPEG fallback if needed.
6. **Store variants** with predictable, versioned names.
7. **Record** dimensions and variant URLs in the database for rendering.
8. **Serve through a CDN** with long cache lifetimes.

Many providers — image CDNs, Supabase storage transformations, Cloudinary-style services — can handle steps 3 to 8 on the fly. The important part is that originals are never served directly to visitors.

## Responsive Images in Practice

With variants in place, the page lets the browser choose the right size:

```html
<img
  src="/img/house-800.webp"
  srcset="/img/house-400.webp 400w, /img/house-800.webp 800w, /img/house-1600.webp 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  width="1600" height="1067"
  alt="Holiday home with garden and view of the South Limburg hills"
  loading="lazy" decoding="async">
```

The `sizes` attribute tells the browser how wide the image will be displayed; the browser picks the smallest variant that looks sharp. `width` and `height` prevent layout shifts. For the main hero image, use `loading="eager"` and consider `fetchpriority="high"` so it appears as quickly as possible. Frameworks such as Next.js generate much of this automatically with their image components.

## Choosing Formats and Quality

| Format | Strength | Use for |
| --- | --- | --- |
| AVIF | Smallest files at high quality | Photos, where supported |
| WebP | Good compression, wide support | Photos and graphics, general fallback |
| JPEG | Universal | Final fallback for older clients |
| PNG | Lossless, transparency | Logos, icons with transparency |
| SVG | Vector, scalable | Icons, simple illustrations |

Quality settings around 60–80 for AVIF/WebP usually look indistinguishable from originals on screens. Test visually with your own photos; product and property images deserve a slightly higher setting than background decorations.

## Measuring the Impact

Before optimising, record: total image weight on key pages, Largest Contentful Paint on mobile (from Search Console or real-user monitoring), bandwidth usage and hosting costs. After optimising, compare. Improvements of several seconds on mobile LCP and large bandwidth reductions are common for image-heavy sites. Share the before-and-after with stakeholders; it makes the value of performance work tangible.

## Content Workflow After Launch

Optimisation must survive new content. Whoever uploads images later — staff, property owners, sellers — should use the same pipeline, never bypassing it by pasting links to large originals. Provide upload guidance (minimum and recommended sizes, landscape versus portrait), require alt text for important images, and review new pages periodically with a quick performance check.

## Accessibility and SEO for Images

Descriptive alt text helps screen-reader users and search engines understand images; decorative images should have empty alt text so they are skipped. Use meaningful file names, include images in structured data where relevant (for example products or accommodations) and provide captions where context helps. Image search can be a meaningful traffic source for visual businesses such as holiday rentals, restaurants and shops.

## Costs and Storage Management

Storing multiple variants increases storage slightly but reduces bandwidth dramatically, which is usually the larger cost. Apply lifecycle rules: delete variants of removed images, archive originals you no longer need and avoid keeping unused uploads. Monitor storage growth monthly, especially on platforms where users upload freely.

## Common Image Mistakes in AI-Built Sites

AI tools often generate image markup that looks correct but performs poorly: `<img>` tags without width and height, CSS background images for important content (which cannot be lazy-loaded or described with alt text), carousels that load every slide immediately, icons as large PNGs instead of SVG, and hero images marked as lazy-loaded (delaying the most important visual). A quick review of image markup on your top pages usually reveals several of these, each fixable in minutes.

## Caching Headers for Images

Images rarely change once published. Serve them with long cache lifetimes (for example `Cache-Control: public, max-age=31536000, immutable`) and change the file name or add a version parameter when an image is replaced. Returning visitors then load images instantly from their browser cache, and the CDN serves repeat requests without reaching your storage — reducing both latency and costs.

## Mobile-First Considerations

Most visitors to consumer sites arrive on phones, often via social media on mobile networks. Design image layouts mobile-first: smaller variants for small screens, cropped compositions that work vertically, and fewer large images above the fold. Test on a mid-range Android phone with network throttling in the browser's developer tools; if the main image appears within about a second or two on a simulated 4G connection, you are in a good position.

## Video and Animated Content

If your site uses video or animated images, the same principles apply more strongly: never autoplay large videos on mobile, use poster images, serve adaptive streaming for longer videos, and replace animated GIFs with compressed video formats, which are often a fraction of the size. Heavy video is one of the fastest ways to undo image optimisation gains.

## Prioritising Pages to Optimise

Start where traffic and conversions meet: the homepage, the most visited listing or product pages and the booking or checkout flow. Improving these few pages often produces most of the benefit. Then extend the pipeline to all new content, and gradually reprocess older images in the background.

## A Quick Audit You Can Do Today

Open your most important page on your phone, then on a laptop with developer tools, and check the network panel sorted by size. Note any image larger than a few hundred kilobytes, any image without width and height and any image loaded far below the visible area immediately. Those three lists are your optimisation backlog — and usually the fastest performance wins available for an AI-built site.

## Why Images Deserve Engineering Attention

Images are often treated as content rather than engineering, left to whoever uploads them. For visual businesses — rentals, shops, restaurants, portfolios, marketplaces — they are the product's first impression and its heaviest technical burden at the same time. A pipeline that resizes, converts, strips metadata and serves through a CDN turns that burden into an asset: pages that load quickly on any phone, rank better in search, cost less to serve and protect the privacy of people who upload photos. Because the work is mostly one-off infrastructure with a lasting effect, it is one of the most cost-effective improvements an AI-built site can receive.

## How LaunchStudio Approaches Image Work

In practice, image optimisation is usually part of a broader launch or performance project: an audit of the heaviest pages, a processing pipeline, markup fixes for responsive and lazy loading, cache headers, metadata stripping and a reprocessing job for existing images. The design stays exactly as it is; only its weight changes. For many image-heavy sites, this work is completed within a week and pays for itself through better conversion and lower bandwidth costs.

## First Step

Measure the total image weight of your homepage today. If it is above a few megabytes, image optimisation is likely your fastest win.

## Remember

The fastest page is the one that sends the fewest bytes. For most AI-built sites, those bytes are images — and they are the easiest ones to remove without changing anything visitors see or love about the design.

## In Short

Resize, convert, lazy-load and cache — then measure again.

## Where LaunchStudio Fits

Image optimisation is often part of LaunchStudio's performance and launch work: upload processing with resizing and metadata stripping, modern formats, responsive and lazy loading, CDN caching and layout fixes — without changing the design you built. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, working from Amsterdam (Herengracht 420), Singapore and Ho Chi Minh City. See [Manifera's web app development](https://www.manifera.com/services/web-app-develop/); [web.dev's guide to optimising images](https://web.dev/learn/performance/image-performance) explains the techniques in detail.

[Send us your site link](https://launchstudio.eu/en/#contact) and we will tell you how much your images weigh.

## Real example

### An AI-Native Founder in Action: A Holiday Home Site Built for Photos

Vera Lammers, who rents out four holiday homes near Valkenburg, built Vakantiehuisje with v0 and a simple booking backend: beautiful full-width galleries of each home, the South Limburg hills and nearby attractions, with direct booking to avoid platform commissions. The photos came straight from a professional photographer — 6 to 10 MB each.

The homepage weighed 48 MB. On mobile, the first photo took around nine seconds to appear, and Google Search Console flagged most pages as "poor" for Core Web Vitals. Most visitors came from phones via Instagram and left before the page finished loading. Her hosting plan's bandwidth limit was exceeded twice during the spring holiday. Guest reviews with photos were stored with GPS data.

Over five business days, LaunchStudio's engineers set up an upload pipeline that generated AVIF and WebP variants in four sizes, switched galleries to responsive images with lazy loading below the fold and eager loading for the hero image, declared image dimensions, served everything through a CDN with long cache lifetimes, stripped metadata from existing and new uploads, and reprocessed the existing photo library.

**Result:** The homepage dropped from 48 MB to about 1.9 MB, and the main image now appears in around a second on 4G. Search Console moved most pages to "good," direct bookings rose by roughly a quarter in the following summer, and bandwidth costs fell below the plan's limit.

> *"The photos were the reason people booked. They were also the reason people left before they saw them."*
> — **Vera Lammers, Founder, Vakantiehuisje (Valkenburg)**

**Cost & Timeline:** €1,400 (Launch Ready package: image pipeline, CDN, responsive loading and metadata removal) — completed in 5 business days.

## Frequently Asked Questions

### How much do images affect page speed in AI-built sites?

Often more than anything else. Full-size photos can make up most of a page's weight, delaying the main content and hurting Core Web Vitals.

### Which image formats should my site use?

Modern formats such as AVIF and WebP, with fallbacks, in several sizes so each device downloads what it needs.

### Do I need to redesign my site to optimise images?

No. Optimisation happens in how images are processed and delivered; the design can stay the same.

### How does Manifera approach performance work?

By measuring real-user performance, then fixing the biggest contributors first — frequently images, queries and caching — as part of production readiness.

### Does image optimisation help SEO and AI visibility?

Yes. Faster pages improve Core Web Vitals, and descriptive alt text and structured data help both search engines and AI answer engines understand your images and pages.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How much do images affect page speed in AI-built sites?", "acceptedAnswer": { "@type": "Answer", "text": "Often more than anything else; full-size photos dominate page weight and hurt Core Web Vitals." } },
    { "@type": "Question", "name": "Which image formats should my site use?", "acceptedAnswer": { "@type": "Answer", "text": "AVIF and WebP with fallbacks, in several sizes." } },
    { "@type": "Question", "name": "Do I need to redesign my site to optimise images?", "acceptedAnswer": { "@type": "Answer", "text": "No; processing and delivery change, the design stays." } },
    { "@type": "Question", "name": "How does Manifera approach performance work?", "acceptedAnswer": { "@type": "Answer", "text": "Measure real-user performance and fix the biggest contributors first." } },
    { "@type": "Question", "name": "Does image optimisation help SEO and AI visibility?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, through better Core Web Vitals, alt text and structured data." } }
  ]
}
</script>
