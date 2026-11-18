🍽️ Imagine a restaurant where the waiter cooks every order at your table, while you wait, and starts over each time you call out "Is it ready?"

That's how Fotofactuur handled its heaviest work.

Tessa Huisman, a wedding photographer in Veenendaal, built Fotofactuur in Bolt: photographers deliver online galleries to clients, sell prints and send invoices. About 180 photographers used it, with galleries of up to 2,000 high-resolution photos. And the busiest photographers had the worst experience.

AT THE TABLE, before
📦 Full-gallery ZIP downloads were built inside the request, and failed above roughly 300 photos. Clients clicked again and again, each click starting a new ZIP, until the function crashed.
🖼️ Uploading a wedding gallery processed thumbnails and watermarks synchronously. Photographers kept the browser open for up to forty minutes, and a dropped connection meant starting over.
✉️ Monthly invoice emails went out in one loop that stopped partway when the email provider rate-limited it, without recording who'd received theirs.

THE KITCHEN, after (LaunchStudio, Launch & Grow, 11 business days, €3,300, plus €49/month)
✓ A managed job queue for the slow work
✓ ZIP exports as chunked background jobs, one per gallery, so extra clicks return the existing job, plus an email with a download link when it's ready
✓ Uploads straight to storage, with thumbnails and watermarks processed in the background, resumable if interrupted
✓ Invoice emails as one idempotent job per invoice, with retries and backoff
✓ A job dashboard showing Tessa every job's status, and heartbeat monitoring on the scheduled invoice run

Full-gallery downloads of 2,000 photos now finish reliably in a few minutes. Photographers upload a wedding and close the laptop. Monthly invoicing reaches every client. And Fotofactuur grew to 290 photographers within the year, several switching from larger platforms because of download reliability.

"My biggest customers were the ones the app failed most. Moving the slow work to the background fixed it for exactly the people I most needed to keep." - Tessa Huisman

https://launchstudio.eu/en/blog/ai-application-scalability-background-jobs-and-queues-for-slow-tasks

#BackgroundJobs #Queues #Scalability #Bolt #LaunchStudio #Manifera
