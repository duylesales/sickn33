🚨 Hidde Brouwer's Offertetool produces quotes for 38 kitchen and bathroom installers, mostly on site in customers' kitchens. Quotes were rendered in the browser from whatever was in the database at the time of download. Then an installer updated their price list - and a homeowner who'd signed in January downloaded the quote again in April. 😳

The April PDF showed different prices - €2,300 lower - and the installer had nothing to prove what had been sent in January. They honoured the lower price. Here's how to generate PDFs and documents that hold up: 🧠

❌ Quotes made with html2canvas and jsPDF: screenshots, unselectable text, rows cut at page breaks
❌ Quotes over three pages silently failing on phones
❌ Every download re-rendered from current data, so sent quotes changed
❌ No record of what was actually sent

✅ Server-side rendering with headless Chromium behind a job queue, with retries and alerting
✅ Documents generated once when sent, stored with a data snapshot, template version and SHA-256 checksum - revisions as new versions
✅ A4 print templates with repeated table headers, unbroken rows, page numbers, embedded fonts and PDF/A output
✅ User content escaped, network and JavaScript disabled in the renderer, signed links and snapshot tests

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build document generation for the part of your product customers forward to their own customers. ⚙️

His result: €3,900, four business days. Forty-page quotes render in about six seconds from any phone, and every quote can be shown exactly as sent. Two installers have since settled disagreements in their favour within a day. 🚀

👉 Lovable hosting: generating PDFs and documents reliably: https://launchstudio.eu/en/blog/lovable-hosting-generating-pdfs-and-documents-reliably

#Lovable #PDF #SaaS #WebDevelopment #LaunchStudio #Manifera
