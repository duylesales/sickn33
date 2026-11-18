⏱️ The 72-hour clock, as it ran for one small SaaS

SATURDAY MORNING
An email arrives. An employee of a bakery chain changed a number in a download link on Loonstrookportaal and saw a colleague's payslip. Then a payslip from a different company.

Mark Wouters built Loonstrookportaal with Bolt and Supabase: a portal where small accounting firms share payslips and annual statements with their clients' employees.

THE FIRST INSTINCT
Patch the link and say nothing. Instead, Mark called LaunchStudio.

WITHIN THE HOUR
• Document storage made private
• All existing download links revoked
• Storage and API logs preserved

THE ANALYSIS
Documents had been served from a public bucket through predictable URLs for seven months. Storage access logs had never been enabled, so nobody could prove which documents had or hadn't been opened. Over 9,000 payslips from 41 accounting firms were potentially exposed.

THE SAME AFTERNOON
As a processor, Mark notified all 41 firms: a factual message, a list of affected documents per firm, a contact number. LaunchStudio provided a technical summary for the firms' own notifications to the Autoriteit Persoonsgegevens.

THE FOLLOWING DAYS (full remediation in 8 business days, €4,200)
• Private storage with signed links that expire after five minutes
• Row Level Security rebuilt per firm and per employee
• Access logging on storage and database
• Negative authorisation tests on every document route
• A written incident procedure with customer notification templates

72 HOURS
All 41 firms met their deadline with the information provided.

AFTERWARDS
Two firms left. 39 stayed, several naming the speed and honesty of the notification as the reason. No further exposure since.

"Patching the link quietly would have felt easier for a day. Telling my customers within hours is the only reason I still have a business." - Mark Wouters

https://launchstudio.eu/en/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas

#DataBreach #GDPR #AVG #IncidentResponse #AIFounder #LaunchStudio #Manifera
