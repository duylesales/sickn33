🧮 The math of doing the steps in the right order

ROUTE 1: pentest first
€12,000 for a penetration test and report
+ a seven-week wait to start
+ fixes, not included
= an expensive way to discover the first four problems

ROUTE 2: review first, pentest later (the one Stefan took)
€2,900 for a review with fixes, authorisation tests and a report (10 business days)
+ a pilot two months earlier
+ a formal pentest six months later, at roughly 40% less than the original quote, thanks to a smaller scope
= two low-severity findings in the final report

Stefan Hulshof, founder of Zonwijzer in Houten, built a customer portal with Cursor for solar panel installers: homeowners follow their installation, see yield data from their inverters and get maintenance reminders, and installers manage projects. Thirty installers used it. Then a national energy company, considering Zonwijzer for its installer network, asked for an independent security assessment.

What the review found first, and LaunchStudio fixed:
🔴 Homeowners could view other homeowners' addresses and yield data through the API
🔴 Inverter integration tokens were stored in plain text, visible to all installers
🔴 Installer admins could edit other installers' projects
🔴 No rate limiting on login
✓ All four fixed, tokens encrypted, authorisation tests added to CI, and a report with evidence

The energy company accepted the LaunchStudio report for the pilot phase, and asked for a formal penetration test before full rollout. Stefan commissioned the security firm six months later, and with the basics already fixed, the scope was smaller.

"The big-name report was right for the final step. It would have been an expensive way to discover the first four problems." - Stefan Hulshof

https://launchstudio.eu/en/blog/ai-application-security-audit-large-consultancy-vs-hands-on-specialist

#SecurityAudit #Pentest #CleanTech #Cursor #LaunchStudio #Manifera
