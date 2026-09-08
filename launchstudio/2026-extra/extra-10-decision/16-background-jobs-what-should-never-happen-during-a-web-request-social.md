🚨 Vasil's invoicing tool triggered two payouts for one payment. Stripe had simply delivered the same webhook event twice, exactly as its own docs warn it might. 😳

Retries aren't an edge case in background jobs — they're the entire point, and most prototypes were never built to survive one: 🧠

❌ The webhook handler ran the payout logic inline, with no check for whether that event ID had already been processed
❌ A job that says "charge this card €50" isn't idempotent by default — run it twice, the card is charged €100
❌ Retrying a failed call immediately, instead of with backoff, adds load to a downstream service that's already struggling
❌ An in-memory job running inside the main server dies mid-execution on every deploy, with zero trace it was interrupted

✅ Record every processed Stripe event ID in a table, checked before any side effect runs
✅ Move payout logic into a proper background job with exponential backoff and jitter, not a fixed short delay
✅ Give failed jobs a dead-letter path with an alert instead of a silent, buried log line
✅ Externalize job state to a durable store so a deploy can't kill work with no record it ever happened

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we harden the webhook and job logic that only breaks the day a deploy lands mid-request. ⚙️

His result: the double-payout bug became structurally impossible, and two near-miss duplicate webhook deliveries the following month were silently absorbed with zero customer impact. 🚀

👉 See what your background jobs do the second time they run: https://launchstudio.eu/en/blog/background-jobs-what-should-never-happen-during-a-web-request

#IndieHacker #Stripe #ProductionReady #SaaS #LaunchStudio #Manifera
