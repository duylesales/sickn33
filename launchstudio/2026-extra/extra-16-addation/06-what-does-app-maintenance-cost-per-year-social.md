🗓️ ONE MONTH, AFTER FOURTEEN QUIET ONES

For over a year, Lotte Vermeer's platform ran without a single change. She built Vrijwilligersbank with Bolt and Supabase so local foundations can match volunteers with tasks. She considered it finished.

Then, in the same month:

💳 Stripe donations stopped being recorded, after an API change her webhook handler didn't support
📧 Password reset emails started landing in spam, after email authentication requirements tightened
⚠️ A dependency alert warned of a critical vulnerability in a package used for file uploads

Fixing it all in an emergency cost more than a year of planned maintenance would have. No tests, so every update broke something else. A framework two major versions behind, with several packages no longer compatible. And nobody knew whether the backups worked.

What LaunchStudio did (10 business days, €3,900):

FIRST, STABILISE
✓ The webhook handler updated, and missed donation events replayed
✓ SPF, DKIM and DMARC for a transactional email provider
✓ The vulnerable package patched

THEN, FOUNDATIONS
✓ Tests for donations, volunteer matching and access control
✓ Automated dependency updates with CI
✓ A framework upgrade
✓ A restore test of the backups
✓ Monitoring for errors and uptime
✓ Managed hosting with monthly maintenance

THE NEXT TWELVE MONTHS
A few hours of routine maintenance a month, with dependency updates merged automatically when tests pass. Two later platform changes, a payment API update and an authentication change, were handled before any user noticed.

"I thought finished software stays finished. It turns out the world around it keeps changing, and the app has to keep up." - Lotte Vermeer

https://launchstudio.eu/en/blog/what-does-app-maintenance-cost-per-year

#Maintenance #Bolt #Supabase #SaaS #AIFounder #LaunchStudio #Manifera
