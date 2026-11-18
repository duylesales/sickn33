🗺️ An employee's data, mapped. Seven places.

📍 1. The Supabase database, hosted outside the EU
📍 2. A public storage bucket, with contracts and sick notes
📍 3. The email provider
📍 4. The error tracker, which received full request bodies, medical notes included
📍 5. The analytics tool, tracking URLs that contained employee names
📍 6. The AI provider, used to summarise leave requests
📍 7. Spreadsheets exported by admins

Eline Mertens runs a small HR consultancy in Den Bosch and built Verlofwijs with Claude Code and Supabase: small employers manage leave, sick days and employee documents. Her first business customer, with 80 employees, asked for a processing agreement, a subprocessor list and confirmation that employee data could be deleted when someone leaves. Eline couldn't answer with confidence. The map above is why.

And two more findings: deletion only removed the login, and every admin could see every employee across all companies.

What LaunchStudio changed (9 business days, €3,200):
✓ Database and storage moved to an EU region
✓ Storage made private, with signed links
✓ Company and role-based access enforced with Row Level Security
✓ Error tracking set to strip request bodies
✓ Analytics URLs switched to IDs
✓ The AI feature sending only leave dates and type, never medical notes
✓ A deletion function that removes or anonymises an employee's data across database, storage and email tool
✓ Retention jobs removing sick notes after the period Eline's lawyer advised
✓ Documentation of data flows and subprocessors

Eline's lawyer drafted the processing agreement, with a technical annex based on that documentation. The customer signed within two weeks. Two more employers used the same documents in their own assessments, with no extra questions.

"I thought GDPR was a document problem. It turned out to be a product problem, and now the product actually does what the documents say." - Eline Mertens

https://launchstudio.eu/en/blog/gdpr-compliance-implementation-service-for-saas

#GDPR #Privacy #SaaS #ClaudeCode #AIFounder #LaunchStudio #Manifera
