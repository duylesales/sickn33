📊 Two penetration test reports, six months apart

                     REPORT #1            REPORT #2
Preparation          none                 3 days of self-review and fixes
Cost                 €7,500               €6,200, retest included
Findings             31                   11
Critical             4                    0
High                 9                    2
Shareable with
the hospital?        no                   yes, as a one-page summary

Arnoud Steenbergen built Contractbeheer in Lovable: contract lifecycle management for facility management companies, 22 customers including three regional hospital groups. A hospital procurement needed a pentest report, so he commissioned one straight away from the first firm that answered.

What report #1 found was mostly his open front door:
• A service role key in the frontend bundle
• A public storage bucket with signed contracts
• Missing authorisation on 17 endpoints
• Row Level Security off on six tables
A systematic self-review would have surfaced all of it in a day.

Between the reports (LaunchStudio, 7 business days, €4,900):
✓ Self-review and fixes across ten categories: keys, buckets, cross-account authorisation, RLS, webhook verification, session storage, uploads, enumeration, dependencies, rate limits
✓ A staging environment with anonymised production data
✓ Documentation, and four accounts at different permission levels for the testers
✓ A second firm chosen after reading a redacted sample report, and confirming two thirds of its work was manual

What report #2 found needed a person thinking about the product for a week:
• A business logic flaw letting a contract approval step be skipped through a direct API call
• A rate limiting gap on document generation
Both fixed in four days, and retested.

The summary went to the hospital, and the contract was signed. Arnoud now runs a test every year, and says the second one was worth more for less, because the testers spent their time on his application's real logic, not on a list of defaults.

"The first report told me my front door was open. I paid seven and a half thousand euros for that. The second one found something that genuinely needed a person to think about my product for a week." - Arnoud Steenbergen

https://launchstudio.eu/en/blog/ai-app-security-preparing-for-a-penetration-test

#Pentest #AppSecurity #Procurement #Lovable #LaunchStudio #Manifera
