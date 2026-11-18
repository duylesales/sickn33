IMPORT #1: 600 members. Stops somewhere between row 200 and row 500. Some members missing.
IMPORT #2: same file, again. Duplicates of everyone processed the first time. Stops again.
IMPORT #3: same file, again. A membership list nobody can trust.

Two clubs spent an evening deduplicating by hand. 🏑

Eva Broekhuizen built Ledenimport in Lovable: membership administration for sports associations and hobby clubs. 88 clubs, most of them importing a member list from a spreadsheet at the start of each season. Imports of 50 members worked. Imports of 600, sometimes. The function was called without waiting and processed rows in a loop, so the serverless environment terminated it once the response had already been sent.

Clubs thought the product was unreliable. They were right. They just had the wrong reason.

What LaunchStudio built (3 business days, €3,200):
✓ A jobs table with atomic claiming
✓ Imports split into one job per 50 rows, queued in the same transaction that records the upload, so an upload always has its jobs, and a rollback leaves neither
✓ Every row keyed on the club's own membership number, so re-running updates instead of inserting, and an import can safely be repeated
✓ Transient failures retried with backoff, and permanent ones (malformed rows, invalid dates) recorded with the row number and reason
✓ A maximum of three attempts, then a failed list with a daily alert
✓ A worker running every minute, with a concurrency limit of five
✓ An import status page with progress, completion and per-row errors, plus an email when a long import finishes
✓ The nightly membership-expiry job moved onto the same queue

IMPORT #1, AFTER: the largest club's 3,400-member file, which had never once succeeded. Done in four minutes, across 68 jobs.

Duplicate-member tickets went from the most common kind to none the next season. And once the expiry job was on the queue, everyone could see it hadn't run for eleven days, which nobody had noticed.

"Clubs were importing three times because it never finished, and every attempt made the data worse. They thought the product was unreliable. They were right, they just had the wrong reason." - Eva Broekhuizen

https://launchstudio.eu/en/blog/lovable-supabase-background-work-that-actually-finishes

#Supabase #BackgroundJobs #Reliability #Lovable #LaunchStudio #Manifera
