🚥 One page, three colours: a production review before a 40-school deal

🔴 ACCESS
Six tables with pupil data had policies letting any authenticated teacher read other schools' records through the API. The interface never showed them. The API did.

🔴 BACKUPS
Never restored. Uploaded support plans sat in one storage bucket with no copy anywhere else.

🔴 PRIVACY PAPERWORK
No processing agreement template, no subprocessor list, no retention periods, for a product holding data about children, including special educational needs.

🟠 × 9
Including untested scheduled jobs, keys shared between environments, and an analytics script with session replay switched on.

Sophie Mulder built Leerlingvolg in Lovable: pupil progress tracking, parent communication and support plans for 85 primary schools. A school board responsible for 40 schools wanted to adopt it everywhere, after a review by its information security and privacy officers. She had a 120-question questionnaire, six weeks, and no clear idea which answers would be a problem. 🏫

The review (LaunchStudio, 2 business days, €1,800) checked ten areas at code level, tested cross-organisation access and a backup restore, assessed the privacy documents, and produced the scored report with a ninety-day plan.

WEEKS 1-3: the reds first
✓ Policies rewritten and verified with a cross-school test suite
✓ Nightly encrypted exports of database and files to a second provider, with a timed restore
✓ A processing agreement, subprocessor list, records of processing and retention register, drafted with a privacy lawyer
✓ Session replay removed and environments separated in the same period

WEEK 5: the questionnaire answered, with evidence for each answer. The officers raised four minor points.

WEEK 7: the contract for 40 schools signed, roughly doubling the product's revenue.

SIX MONTHS LATER: a second review. No red areas.

"I knew there would be questions I could not answer. I did not know that teachers could read other schools' pupil files through the API. Two days of review told me exactly where to start." - Sophie Mulder

https://launchstudio.eu/en/blog/lovable-bolt-and-replit-a-production-architecture-review-in-one-page

#Lovable #Bolt #Replit #ProductionReady #LaunchStudio #Manifera
