🕗 THE FIRST MONDAY OF SEPTEMBER: the busiest morning of the year

08:50 · A Supabase connection issue. The product goes down.
09:00 · Enrolment opens for three organisations.
09:20 · The fourth support email arrives. Only now does Tessa know.
09:20 to 09:31 · She fixes it, with no capacity to reply to anyone.
09:31 · Back up, after 41 minutes.
11:00 · Her first message to customers.

By then: two organisations had told students to try again later, one had posted on social media that the system was down, and two cancelled within the fortnight, citing reliability.

Tessa Groenewoud built Cursusinschrijving in Lovable: course registration and payment for training providers and community colleges, 29 organisations, with enrolment peaks at the start of each term. It wasn't the downtime that did the damage. It was that for half an hour, nobody could tell customers anything.

What LaunchStudio set up (1 business day, €1,500):
✓ An external uptime check every minute, against a page that runs a real database query, with alerts to her phone after two failures in a row
✓ A health endpoint checking database, storage and job queue
✓ An alert if weekday hourly enrolments drop to zero during term-start periods
✓ A hosted status page on a separate provider, linked in the footer, the onboarding email and the support auto-reply, with subscriptions so organisations hear automatically
✓ A written procedure: a first message within ten minutes with four facts, then updates every twenty minutes
✓ Subscriptions to the status feeds of her hosting, database and payment providers
✓ A template for the closing explanation

🕗 THE FOLLOWING JANUARY: a comparable incident
Duration: 26 minutes
First status message: minute 7
Updates: two
Explanation: posted the same afternoon
Support emails: one, asking whether the status page covered payments too
Cancellations: none

"The second outage was a better experience for my customers than a normal Tuesday, which tells you how bad the first one was. It was not the downtime. It was that for half an hour nobody could tell them anything." - Tessa Groenewoud

https://launchstudio.eu/en/blog/lovable-hosting-status-pages-and-telling-customers-first

#IncidentManagement #StatusPage #SaaS #Lovable #LaunchStudio #Manifera
