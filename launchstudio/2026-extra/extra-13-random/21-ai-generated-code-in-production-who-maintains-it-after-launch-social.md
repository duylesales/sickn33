🚌 What's your app's bus factor?

The bus factor: how many people would need to leave before nobody knows how your app works.

For PraatMaat, the answer was one. And in February, that one person took a full-time job abroad. 🗣️

Charlotte Meijer, a former language teacher in Amstelveen, built PraatMaat with Cursor and the help of a freelance developer: a platform that matches adult learners with Dutch conversation tutors, with scheduling, video-call links, subscriptions and progress notes. By autumn: 380 learners and 45 tutors.

What left with the freelancer:
• The Mollie API key, in his personal account
• The domain's auto-renewal, tied to his credit card
• Every bit of knowledge about the code: no documentation, no tests, no record of what had changed or why

Two weeks later, a Supabase SDK update Charlotte applied through Cursor broke password resets. She asked Cursor to fix it. The fix worked, and, it later turned out, removed an access check on tutors' progress notes.

Raising the bus factor (LaunchStudio, 8 business days, €2,000):
✓ Repository, hosting, database, Mollie and domain moved to Charlotte's company accounts, with two-factor authentication
✓ The Mollie key rotated
✓ The access check on progress notes restored
✓ Password resets repaired properly
✓ Tests for signup, login, reset, booking and payment
✓ A README and a maintenance log
✓ Outdated dependencies with known vulnerabilities updated
Then Charlotte moved to the Launch & Grow managed plan, at €49 a month, for hosting, monitoring, backups and security updates.

Fourteen months since: no unplanned outages. The tests have blocked three regressions from Cursor edits. And when Charlotte hired a part-time developer the following year, onboarding took two days instead of weeks.

"I owned the code in theory. In practice, the only person who understood it had just moved to Berlin." - Charlotte Meijer

https://launchstudio.eu/en/blog/ai-generated-code-in-production-who-maintains-it-after-launch

#Maintenance #Cursor #SaaS #EdTech #LaunchStudio #Manifera
