🗓️ THE RELEASE CALENDAR, before

MON-THU: Publish straight from Lovable, and hope.
FRIDAY: Don't. (An informal rule, after too many weekends of broken features.)

What "hope" had cost:
• A new "skip a month" feature accidentally skipped billing for every annual subscriber, for a month
• A redesigned reminder schedule broke notifications for customers in another time zone
• Reverting through Lovable produced a version that differed from the original
• No staging, anywhere

Isabel Moreno moved from Madrid to Amsterdam Oost to start a plant business, and built Plantenpost in Lovable: monthly houseplant deliveries, a care-reminder app, plant health diagnosis from photos, and a marketplace for extra pots and plants. About 2,300 subscribers and three part-time staff. A growing company, releasing like a weekend project.

What LaunchStudio set up (Launch & Grow, 15 business days, €5,400, plus €49/month):
✓ A staging environment with anonymised, production-like data, plus Mollie and email in test mode
✓ A Git-based deployment pipeline from the Lovable project, with one-click rollback
✓ A simple server-side feature-flag system, supporting percentages and specific customers
✓ Migration guidelines using expand-and-contract
✓ Automated checks on signup, subscription changes, billing and reminders
✓ The billing error corrected, with affected annual subscribers charged correctly and told clearly why

🗓️ THE RELEASE CALENDAR, after
MON-FRI: Several releases a week. Fridays included.

In the next quarter, two releases were switched off by flag within minutes after early error spikes, with only a few percent of customers exposed. No release has caused a billing incident since, and subscribers grew to 3,400.

"We were a growing company releasing like a weekend project. Now a bad change affects a few customers for a few minutes, instead of everyone for a weekend." - Isabel Moreno

https://launchstudio.eu/en/blog/ai-application-production-ready-for-scale-ups-staging-feature-flags-and-rollbacks

#FeatureFlags #ScaleUp #SaaS #Lovable #LaunchStudio #Manifera
