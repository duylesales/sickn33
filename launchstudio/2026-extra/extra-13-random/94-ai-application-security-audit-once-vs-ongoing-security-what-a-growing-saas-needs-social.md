🏷️ SECURITY AUDIT
Issued: last year
Best before: the next code change

Laurens Dijkman, founder of Vloerwijzer in Heemskerk, built a SaaS with Cursor for flooring retailers: in-store staff measure rooms on a tablet, generate quotes with material and labour costs, and customers sign and pay deposits online. A freelancer had audited it the previous year, and Laurens considered security "done." Forty retailers used it.

Eleven months and roughly 300 Cursor-assisted changes later, a retailer's IT consultant found that staff at one retailer could see another retailer's quotes and margins, through a new reporting endpoint. 🪵

The audit had been accurate the day it was written. The codebase just didn't stay the same codebase.

LaunchStudio reviewed every change since the audit, and found four regressions:
⚠️ The new reporting endpoint, with no tenant checks
⚠️ A database policy loosened during a debugging session
⚠️ A mapping API key, back in the frontend bundle
⚠️ Two dependencies with published vulnerabilities
None had been caught, because nothing was checking for them.

Security with no expiry date (8 business days, €2,400, plus €49/month):
✓ All four fixed
✓ 38 negative authorisation tests, covering every role and tenant boundary
✓ Secret and dependency scanning in CI
✓ Alerts on any database policy change
✓ A quarterly light-review schedule
✓ Managed hosting for updates, backups and monitoring

The next year, CI blocked six changes that would have brought back cross-tenant access or secrets, and two quarterly reviews found only minor issues. Vloerwijzer grew to 64 retailers, and now answers security questionnaires from a security page that's always current.

"The audit was accurate the day it was written. My codebase just didn't stay the same codebase." - Laurens Dijkman

https://launchstudio.eu/en/blog/ai-application-security-audit-once-vs-ongoing-security-what-a-growing-saas-needs

#SecurityAudit #DevSecOps #SaaS #Cursor #LaunchStudio #Manifera
