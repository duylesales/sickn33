🍳 RECIPE: how to rename a column while sixty drivers are on the road

First, how NOT to do it.

Ferdi Aalbersberg built Routeplanning in Lovable: delivery route planning for regional bakeries and food distributors, 24 companies, whose drivers use the app on their phones from five in the morning. A tidy-up renamed a column from adres to address, and updated the app in the same deployment. He deployed at 06:40 on a Wednesday, thinking it was trivial. 🥖

Every driver already on the road had the app open, running the previous version, which asked for a column that no longer existed. Every route refresh failed. Most drivers didn't reload, because they were driving. They called dispatchers, who called Ferdi. Around 60 drivers across nine companies, for 25 minutes. And the revert didn't work either, because the old code needed the column he'd dropped. He restored it by hand at 07:20, reading the schema under a lot of pressure.

THE RIGHT RECIPE (LaunchStudio, 1 business day, €1,600)

Day 1: Add address.
Day 1: Write to both columns, and backfill in batches of 2,000 as a resumable job.
Day 2: Switch reads to address.
Day 8: Drop adres.

KITCHEN RULES
✓ No deployment may remove or rename a column the currently running version still uses
✓ API responses change additively only, with removed endpoints kept as no-ops for 30 days
✓ The server returns a build ID, and the app shows a quiet "a new version is available" prompt, which drivers accept at their next stop
✓ A four-line deployment checklist, including a timed rollback
✓ No deployments between 05:00 and 09:00, the exact window his customers work in

SERVES
Twelve months without a deployment incident, including two more schema changes of a similar size. And the version prompt mattered as much as the migration discipline: before it, some drivers were running a three-day-old build without knowing.

"It was a rename. I have never done anything faster or more carelessly, and sixty drivers were standing next to their vans at seven in the morning because of it." - Ferdi Aalbersberg

https://launchstudio.eu/en/blog/lovable-hosting-zero-downtime-deploys-while-people-are-using-it

#DevOps #Deployment #DatabaseMigrations #Lovable #LaunchStudio #Manifera
