🚨 Tessa Huisman, a wedding photographer in Veenendaal, built Fotofactuur in Bolt: photographers deliver online galleries, sell prints and send invoices. About 180 photographers, galleries of up to 2,000 high-res photos. And the busiest photographers - her best customers - had the worst experience. 😳

Full-gallery ZIPs were built inside the request and failed above roughly 300 photos; clients kept clicking, each click starting a new ZIP until the function crashed. Uploads processed thumbnails and watermarks synchronously, so photographers kept the browser open for up to forty minutes - and a dropped connection meant starting over. Monthly invoice emails ran in one loop that stopped when the email provider rate-limited it, with no record of who'd been sent theirs. Here's what background jobs and queues do for AI application scalability: 🧠

❌ Slow work done inside the request
❌ Duplicate clicks multiplying the load
❌ Uploads that die with the browser tab
❌ Bulk emails with no retries or record

✅ A managed job queue: chunked ZIP exports, one job per gallery, and an email with a download link when ready
✅ Uploads straight to storage, with thumbnails and watermarks processed in the background and resumable
✅ One idempotent job per invoice email, with retries and backoff
✅ A job dashboard for Tessa and heartbeat monitoring on the scheduled invoice run

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we move slow work out of the request so your biggest customers stop being your unhappiest. ⚙️

Her result: €3,300 over eleven business days, plus €49/month. 2,000-photo downloads now complete in minutes, photographers upload and close the laptop, invoices reach every client - and Fotofactuur grew to 290 photographers. 🚀

👉 AI application scalability: background jobs and queues for slow tasks: https://launchstudio.eu/en/blog/ai-application-scalability-background-jobs-and-queues-for-slow-tasks

#BackgroundJobs #Queues #Scalability #Bolt #LaunchStudio #Manifera
