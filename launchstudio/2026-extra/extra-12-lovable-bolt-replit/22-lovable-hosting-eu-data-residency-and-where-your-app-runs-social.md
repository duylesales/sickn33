🌍 "Where is personal data stored and processed?"

That's what a municipality's procurement questionnaire asked. Hidde's honest answer took a fortnight to find:

Database ........................ 🇪🇺 Frankfurt (fine)
Serverless functions ............ 🌍 whichever region was closest to the visitor, so queries arrived from three continents
Error tracking .................. 🇺🇸 full request bodies, reporters' names and addresses included, no scrubbing
Photos of reported problems ..... 🇺🇸 a US-region bucket, chosen by a default nobody had looked at
AI summaries .................... 🌐 full report text, names included, sent to a model API without a data processing agreement

Hidde Vermaas built Meldpunt in Lovable: municipalities receive and track public reports about street furniture, lighting and green space maintenance. Eleven smaller municipalities used it. Then a larger one started a procurement. Every one of those defaults had been chosen by clicking through a setup screen in an afternoon. None was a decision. All four were on the questionnaire.

What LaunchStudio changed (6 business days, €4,200):
✓ A complete service inventory, with processing, storage and backup locations documented
✓ Functions pinned to Frankfurt, which also cut average response time by 240 milliseconds
✓ Error tracking moved to an EU-hosted provider, with request body scrubbing so personal data never leaves
✓ 34,000 photos migrated to an EU storage region, with URL generation rewritten and old links redirected
✓ The summarisation feature on an EU-region model endpoint, under a data processing agreement, and sending only the description text, not the whole record
✓ A published subprocessor and data location page
✓ A process requiring a residency check before any new service is added

Database ........................ 🇪🇺
Functions ....................... 🇪🇺
Error tracking .................. 🇪🇺
Photos .......................... 🇪🇺
AI summaries .................... 🇪🇺

The questionnaire was answered from the published page, plus two clarifying sentences, and the contract was awarded. Three of the eleven existing municipalities asked for the same document within a month. Hidde now sends the link before anyone asks.

"Every one of those defaults was chosen by clicking through a setup screen in an afternoon. None of them was a decision, and all four of them were on the questionnaire." - Hidde Vermaas

https://launchstudio.eu/en/blog/lovable-hosting-eu-data-residency-and-where-your-app-runs

#GDPR #DataResidency #GovTech #Lovable #LaunchStudio #Manifera
