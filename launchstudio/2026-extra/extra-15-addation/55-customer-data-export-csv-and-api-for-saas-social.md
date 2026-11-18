💔 How to break up with a SaaS (and why it should be easy)

Gijs van Beek built Ledenbeheer Plus with Lovable and Supabase: membership administration for associations and foundations, covering members, contributions, events and communications. A national federation of sports associations wanted to recommend it to its clubs. Its procurement checklist had one clause Gijs hadn't thought about: a complete data export in a documented format, and an exit procedure.

In other words: if a club ever wants to leave, can it take everything with it?

What leaving looked like before:
• One "Export" button on the members list
• It exported only the 50 members on the current page
• The CSV was built in the browser and opened in one column in Dutch Excel
• Accented names came out garbled
• No export for contributions, events or uploaded documents
• And a member could put a formula in their name field that would run when an admin opened the file

What leaving looks like now (LaunchStudio, 9 business days, €3,300):
✓ List exports built on the server, covering all filtered rows within the user's permissions
✓ XLSX and Dutch-friendly CSV, UTF-8 with byte order mark, ISO dates, and protection against CSV injection
✓ A full account export as a background job: a ZIP with CSV and JSON for every entity, uploaded documents in folders and a data dictionary
✓ Delivered by a signed link valid for 24 hours, deleted after seven days
✓ Admin role and MFA confirmation required, with every export in the audit log
✓ A written offboarding procedure for Gijs's terms

The plot twist: the federation approved Ledenbeheer Plus and put it on its recommended list. Around 60 clubs joined the next season. Two clubs that later switched systems exported everything without contacting support.

"Being easy to leave turned out to be one of the reasons clubs chose to join." - Gijs van Beek

https://launchstudio.eu/en/blog/customer-data-export-csv-and-api-for-saas

#DataPortability #SaaS #Procurement #NonProfit #AIFounder #LaunchStudio #Manifera
