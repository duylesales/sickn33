💬 A support conversation with nothing to say (dramatized)

LANDSCAPER: I saved a €14,000 quotation. It's gone. I spent forty minutes on it.
FOUNDER: I'm so sorry. Let me look.
FOUNDER: (the logs are unstructured text, kept for 24 hours, and your report arrived four days later)
LANDSCAPER: Did it save? Did it fail? Was it something I did?
FOUNDER: ...I can't tell you.
LANDSCAPER: I rebuilt it. A competitor quoted first. I'm thinking about leaving.

Willemijn Stoffels built Prijsopgave in Lovable: quotation software for garden landscaping and paving companies, 52 firms, around 1,100 quotations a month. The landscaper was in Alphen aan den Rijn. And not being able to tell him anything was worse for the relationship than the defect itself.

What LaunchStudio built (2 business days, €2,000):
✓ Structured logging everywhere: event, severity, timestamp, request ID, user and account on every entry
✓ Request IDs carried into database operations, the PDF generation service and background jobs
✓ Log levels, so production records errors, warnings and business events, not chatter
✓ Fields scrubbed by name before sending, since the old setup logged full form bodies, customers' addresses included
✓ 30-day log retention, plus sign-ins, permission changes, quotation status changes and exports in an audit table in her own database, kept for two years
✓ Error tracking with release, user and request context
✓ A short reference code on every user-facing error message

Three weeks later, the same failure happened again, and this time it was captured in full: a PDF generation timeout that told the browser "success" while the save was rolled back. Fixed in an afternoon.

The same conversation, now:
LANDSCAPER: Something went wrong. The screen shows reference X7K2.
FOUNDER: Found it. Here's exactly what happened, and it's fixed.

The landscaper stayed, mostly because he got a specific explanation and a reference number, not just an apology.

"A customer lost forty minutes of work and I could not tell him anything. Not what went wrong, not whether it was his mistake or mine. That conversation was the expensive part, not the bug." - Willemijn Stoffels

https://launchstudio.eu/en/blog/lovable-hosting-logs-you-can-search-when-it-matters

#Logging #Observability #SaaS #Lovable #LaunchStudio #Manifera
