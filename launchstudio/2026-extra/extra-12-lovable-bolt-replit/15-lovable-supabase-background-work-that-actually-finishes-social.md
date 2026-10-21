🚨 Eva Broekhuizen's Ledenimport handles membership administration for 88 sports and hobby clubs, most of whom import a member list at the start of each season. 50 members worked. 600 sometimes worked. The import was cut off somewhere between row 200 and row 500 — after the user had already been told it was done. 😳

Clubs noticed missing members and imported again. And again. Two spent an evening deduplicating by hand. Here's why "fire and forget" isn't background work: 🧠

❌ A slow function called without waiting — killed when the serverless response was sent
❌ No retries, no record of what was attempted, no limit on concurrency
❌ Re-running an import inserted duplicates instead of updating
❌ A nightly job that silently stopped — and nobody noticed for eleven days

✅ A jobs table in Postgres with atomic claiming, enqueued in the same transaction as the upload
✅ Imports split into batches of 50, each row keyed on the club's own membership number so re-runs are safe
✅ Backoff for transient failures, per-row errors for bad data, max three attempts, then a failed-job alert
✅ A progress page with per-row errors, an email when long imports finish, and scheduled work on the same queue

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we replace "started and hoped" with work that actually finishes. ⚙️

Her result: three business days and €3,200 later, imports of any size complete — the largest club's 3,400-member file, which had never succeeded, ran in four minutes across 68 jobs. Duplicate-member tickets went from the top category to none. 🚀

👉 Background work that actually finishes: https://launchstudio.eu/en/blog/lovable-supabase-background-work-that-actually-finishes

#Supabase #BackgroundJobs #Reliability #Lovable #LaunchStudio #Manifera
