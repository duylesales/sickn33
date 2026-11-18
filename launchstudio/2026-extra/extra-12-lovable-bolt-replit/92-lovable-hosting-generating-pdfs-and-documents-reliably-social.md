🔍 Spot the difference: the same signed quote, downloaded twice

JANUARY DOWNLOAD
Signed by the homeowner. Prices from the January price list.

APRIL DOWNLOAD
Same quote, same customer. Prices from the April price list. €2,300 apart.

Why? Every download rendered the quote again, from whatever was in the database at that moment. The installer had updated their price list. The homeowner had the April PDF. The installer had nothing showing what was sent in January, so they honoured the lower price.

Hidde Brouwer built Offertetool in Lovable: quotes and order confirmations for kitchen and bathroom installers, 38 companies whose sales staff mostly work on site, in customers' kitchens. Quotes were generated in the browser with html2canvas and jsPDF. Other differences you could spot: table rows cut in half at page breaks, text you couldn't select, and on phones, where most quotes were made, anything over three pages failing without an error. 🛁

No more differences (LaunchStudio, 4 business days, €3,900):
✓ Rendering moved to a headless Chromium container behind a job queue, with document records, retries and alerting
✓ Quotes and confirmations generated once, when sent, and stored with a snapshot of line items and prices, the template version and a SHA-256 checksum
✓ Revisions issued as new versions, with earlier ones kept and visible
✓ A4 print CSS: repeated table headers, rows that never split, page numbers, the installer's details on every page, embedded fonts
✓ Output as PDF/A-2b
✓ User content escaped, with network access and JavaScript disabled in the renderer
✓ Private storage with signed links
✓ Text and visual snapshot tests for one-page and forty-page quotes and long product descriptions

A forty-page quote now renders in about six seconds from any phone, because the phone no longer does the work. Every quote sent since can be shown exactly as sent, checksum included. Two installers have already used stored versions to settle disagreements in their favour within a day.

"The customer had a PDF of our quote with prices we never offered. We had generated it ourselves, three months later, from the new price list." - Hidde Brouwer

https://launchstudio.eu/en/blog/lovable-hosting-generating-pdfs-and-documents-reliably

#Lovable #PDF #SaaS #WebDevelopment #LaunchStudio #Manifera
