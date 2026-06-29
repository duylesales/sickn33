# Social Media Post: Background Job Processing for AI Workloads with BullMQ and Redis

Vercel API routes have a 10-60 second timeout limit.
If your AI app is analyzing a 2-hour video, transcribing audio, or scraping a company's entire website, the HTTP request will crash, and your user will see a 504 Gateway Timeout.

You cannot run heavy AI workloads synchronously.

You must build an asynchronous queuing architecture:
1️⃣ The User clicks "Analyze".
2️⃣ Next.js drops a job payload into an **Upstash Redis** queue and instantly returns `{"status": "processing"}` to the frontend.
3️⃣ A long-running Docker container (hosted on Fly.io) running a **BullMQ** Worker pulls the job. It works for 25 minutes with no timeouts.
4️⃣ If OpenAI throws a `429 Too Many Requests` error, BullMQ automatically handles exponential retries. 

Stop crashing your users' browsers. Read our full technical guide on the LaunchStudio blog.

#LaunchStudio #Redis #BullMQ #AISaaS #Nextjs #Vercel #Architecture
