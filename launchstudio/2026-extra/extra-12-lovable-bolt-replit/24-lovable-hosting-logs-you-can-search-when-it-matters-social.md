🚨 Willemijn Stoffels's Prijsopgave produces about 1,100 quotations a month for 52 landscaping and paving firms. A landscaper in Alphen aan den Rijn reported that a €14,000 quotation vanished after he saved it. He rebuilt it, lost the job to a competitor — and said he was thinking of leaving. 😳

She couldn't investigate. Logs were unstructured text, kept for 24 hours, and the report arrived four days later. Here's why most logs can't answer the question that matters: 🧠

❌ Print statements instead of structured log entries
❌ No request ID — no way to find one customer's afternoon
❌ 24-hour retention, shorter than the time it takes a customer to report a problem
❌ Full form bodies logged, including customers' addresses

✅ Structured logs with event, severity, request ID, user and account on every entry
✅ Request IDs carried through database calls, PDF generation and background jobs
✅ Sensitive fields scrubbed by name, 30-day retention, and a two-year audit table for sign-ins, status changes and exports
✅ Error tracking with release, user and request context — and a short reference code in every user-facing error

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure you can investigate what happened last week. 🔎

Her result: two business days and €2,000 later, an identical failure three weeks on was captured in full — a PDF timeout returning "success" while the save was rolled back — and fixed in an afternoon. The landscaper stayed, because he got a specific explanation and a reference number. 🚀

👉 Logs you can search when it matters: https://launchstudio.eu/en/blog/lovable-hosting-logs-you-can-search-when-it-matters

#Logging #Observability #SaaS #Lovable #LaunchStudio #Manifera
