🚨 Charlotte Meijer, a former language teacher in Amstelveen, built PraatMaat with Cursor and a freelance developer: a platform matching adult learners with Dutch conversation tutors. By autumn, 380 learners and 45 tutors were active. In February the freelancer took a job abroad. Two weeks later, password resets broke. 😳

She asked Cursor to fix it. The fix worked — and silently removed an access check on tutors' progress notes. The Mollie API key sat in the freelancer's personal account, the domain renewal was on his credit card, and there were no docs, no tests and no record of what had changed. Here's who really maintains AI-generated code after launch: 🧠

❌ Critical accounts owned by someone who has left
❌ AI "fixes" that break security without anyone noticing
❌ No tests to catch regressions
❌ No documentation for the next developer

✅ Repository, hosting, database, Mollie and domain moved to company accounts with 2FA — and the key rotated
✅ The access check restored and password resets repaired properly
✅ Tests for signup, login, reset, booking and payment
✅ A README, a maintenance log, updated dependencies and a managed plan for hosting, monitoring and security updates

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure your app has an owner after launch — not just a builder before it. ⚙️

Her result: €2,000, eight business days, then €49/month. PraatMaat has run fourteen months without an unplanned outage, the tests blocked three Cursor regressions, and a new part-time developer onboarded in two days. 🚀

👉 AI generated code in production: who maintains it after launch?: https://launchstudio.eu/en/blog/ai-generated-code-in-production-who-maintains-it-after-launch

#Maintenance #Cursor #SaaS #EdTech #LaunchStudio #Manifera
