🩺 PATIENT FILE: Aanbestedingsradar

Patient: a Bolt-built service that monitors Dutch public tender publications and alerts 90 subscribing companies to relevant opportunities, at €79 a month. Founder: Ties Grootveld.

Complaints:
1. "My marketing pages don't rank."
2. "The product feels slow."

Second opinion received from everyone: "Move to Next.js." Estimated treatment: three weeks.

EXAMINATION
Complaint 1: the marketing pages were a single-page application serving an empty document. That's why none of his eleven articles were indexed. Server rendering genuinely needed.
Complaint 2: an unrelated condition. The tender list fetched every row a company had ever been matched with, then paginated in the browser. For the largest subscriber, that meant 41,000 rows. A framework change would not have touched it.

DIAGNOSIS
Two problems, two treatments, one of which was a framework.

TREATMENT (LaunchStudio, 1 business day, €2,400) 🗂️
✓ Marketing site and blog rebuilt as a statically generated application serving real HTML at the domain root
✓ The existing Bolt app moved to /app and excluded from indexing
✓ Canonical URLs and a sitemap
✓ The tender list moved to cursor pagination, with an index on the matching table: the largest subscriber's list went from 9 seconds to 210 milliseconds
✓ A written note: a full framework migration stays available if server-side logic ever justifies it

FOLLOW-UP
Nine of eleven articles indexed within a month. Organic enquiries started arriving for the first time. The slow screen was fixed by an index and a query change. Two years on, the application hasn't been migrated, and hasn't needed to be.

"Everyone told me the framework was the problem. The marketing pages did need fixing. The slow screen was a query that fetched forty-one thousand rows, and it would have been just as slow in Next.js." - Ties Grootveld

https://launchstudio.eu/en/blog/bolt-to-next-js-moving-onto-a-framework-you-control

#NextJS #Bolt #SEO #WebDevelopment #LaunchStudio #Manifera
