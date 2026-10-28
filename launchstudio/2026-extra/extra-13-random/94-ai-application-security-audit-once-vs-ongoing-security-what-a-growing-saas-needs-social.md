🚨 Laurens Dijkman, founder of Vloerwijzer in Heemskerk, built a SaaS with Cursor for flooring retailers: staff measure rooms on a tablet, generate quotes with material and labour costs, and customers sign and pay deposits online. After a freelancer's security audit the year before, Laurens considered security "done". Forty retailers used it. Eleven months and about 300 Cursor-assisted changes later, a retailer's IT consultant found something. 😳

Staff at one retailer could see another retailer's quotes and margins through a new reporting endpoint. The review of changes since the audit found four regressions: that endpoint without tenant checks, a database policy loosened during debugging, a maps API key back in the frontend bundle, and two dependencies with published vulnerabilities. Nothing had caught them, because nothing was checking. Here's one-off audit vs ongoing security for a growing AI-built SaaS: 🧠

❌ A clean report that aged with every change
❌ Regenerated code silently removing access checks
❌ Policies loosened "temporarily" and never restored
❌ Secrets and vulnerable packages creeping back in

✅ All four regressions fixed
✅ 38 negative authorisation tests covering every role and tenant boundary
✅ Secret and dependency scanning in CI, plus alerts on database policy changes
✅ A quarterly light-review schedule and managed hosting for updates, backups and monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, our audits leave guardrails behind - so findings stay fixed while you keep shipping. ⚙️

His result: €2,400 over eight business days, plus €49/month. In the next year CI blocked six changes that would have reintroduced cross-tenant access or secrets, quarterly reviews found only minor issues, and Vloerwijzer grew to 64 retailers. 🚀

👉 AI application security audit once vs ongoing security: what a growing SaaS needs: https://launchstudio.eu/en/blog/ai-application-security-audit-once-vs-ongoing-security-what-a-growing-saas-needs

#SecurityAudit #DevSecOps #SaaS #Cursor #LaunchStudio #Manifera
