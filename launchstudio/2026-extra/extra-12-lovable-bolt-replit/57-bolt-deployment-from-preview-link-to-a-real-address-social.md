🟠 STATUS: Zwemlesplanner is unavailable
Cause: a platform incident at the prototyping tool
Our action: none possible
Status page: none
Estimated recovery: unknown

(Illustrative. No such notice existed, which was the problem.)

For five months, a real business ran on a preview link. Renske Bouhuijs built Zwemlesplanner with Bolt, scheduling lessons and attendance for swimming schools. Three schools started using it within a month, because it solved a real problem. Parents got links to the preview address. The schools bookmarked it. Renske invoiced €45 a month per school. 🏊

Then, in one week:
• The preview was down for several hours during a platform incident, and she had nothing to point anyone to and nothing she could do
• A school asked for her company website before renewing. There wasn't one, because the product had no address of its own

🟢 STATUS: Moved to its own address (LaunchStudio, 1 business day, €1,900)
✓ The project exported into a repository under her own account. An environment file holding live database credentials was removed, and the credentials rotated
✓ Deploys from a branch push, with functions in the same region as her Supabase project, which also removed a noticeable delay on every page
✓ Three environments with separate databases and credentials, replacing one shared setup where she'd been testing against live data
✓ Staging behind access protection and kept out of search indexes
✓ A .nl domain with SSL, with www redirecting to the bare domain
✓ SPF, DKIM and DMARC set up before the first lesson reminder went out from the new domain
✓ Rollback tested and timed at 35 seconds
✓ Uptime monitoring against a page that runs a real database query

All three schools renewed, and two more joined within a quarter, partly, Renske thinks, because the product now had an address that looked like a company. The separate environments also ended a habit she hadn't seen as dangerous: testing on the live database had twice caused visible oddities during a school's lesson hours.

"Parents were bookmarking a preview link. When it went down for four hours I had nothing to tell anyone, because the product did not really exist anywhere I controlled." - Renske Bouhuijs

https://launchstudio.eu/en/blog/bolt-deployment-from-preview-link-to-a-real-address

#Bolt #Deployment #Hosting #Startup #LaunchStudio #Manifera
