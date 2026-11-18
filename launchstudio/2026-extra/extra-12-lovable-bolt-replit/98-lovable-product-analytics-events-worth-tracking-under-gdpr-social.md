🎙️ An interview with an analytics script (dramatized; its answers describe what it really did)

Q: You were added to find out which customers are active. Which are?
A: I can't say. I hold 140 differently named events and no reliable organisation ID.

Q: So what did you collect?
A: Everything, by default. Every click and page, with employee names in the URLs. And session replay was on.

Q: Including the absence screens?
A: Including the free-text notes where managers wrote down what employees told them about their health.

Q: Where did that go?
A: To a provider outside the EU. No processing agreement. Not in the privacy statement.

The script lived in Verzuimregistratie, the sick leave and absence registration Naomi Dekker built in Lovable for 160 small and medium businesses. It came to light when the data protection officer at a 400-employee customer asked for the subprocessor list and how health-related data was handled. 🩹

The script's replacement (LaunchStudio, 3 business days, €3,400):
✓ Session replay removed entirely, and autocapture switched off
✓ The data at the old provider deleted, with written confirmation
✓ A tracking plan of 22 server-side events, named object-and-action, carrying pseudonymous organisation and user IDs, with no names, notes or identifying URLs
✓ Events written to the product's own database and forwarded to an EU-hosted analytics tool under a processing agreement, set up to meet the Dutch Data Protection Authority's conditions for low-impact analytics
✓ An opt-out per customer organisation
✓ The processing register, subprocessor list and privacy statement updated
✓ Activation and account health views
✓ Typed event functions, with tests

With a privacy lawyer's help, the incident was reported to the Autoriteit Persoonsgegevens and affected customers were told. The DPO accepted the remediation and the customer stayed.

Then the new analytics answered the original question. The account health view flagged nine companies whose usage had dropped sharply. Naomi called each one, and seven were still customers a year later. After the onboarding step where most people stopped was redesigned, new accounts registering a first absence within a week rose from 48% to 71%.

"I added analytics to find out which customers were active. What it actually did was record managers' notes about their employees' health and send them abroad - and it still could not tell me which customers were active." - Naomi Dekker

https://launchstudio.eu/en/blog/lovable-product-analytics-events-worth-tracking-under-gdpr

#GDPR #ProductAnalytics #Privacy #SaaS #LaunchStudio #Manifera
