🖨️ A photocopy, or a second print from the same file?

Make a photocopy, and you have two documents that start drifting apart the moment someone edits one of them. Print twice from the same file, and every edit shows up on both.

Victor Hamers almost made a photocopy.

He built Inspectieloket in Bolt and Supabase: an inspection and compliance tool for property maintenance companies. Multi-tenant, 25 customers. Then a national housing corporation wanted to sign, on one condition: a dedicated database, in an EU region of its choosing, with its own backup schedule.

Victor's first instinct was to copy the project by hand. That would have meant a second product, and every feature built twice.

The "same file, printed twice" approach (LaunchStudio, 14 business days, €5,200):
✓ First, the multi-tenant setup hardened, with organisation-based RLS and automated isolation tests
✓ Then, a dedicated Supabase project for the housing corporation, deployed from the same codebase
✓ A GitHub Actions workflow that applies migrations and edge functions to the shared project and the dedicated one in sequence, so both stay identical
✓ Documentation for both environments

The housing corporation signed at an enterprise price that covered the extra instance. Every feature released since has reached both environments on the same day.

"I almost created a second product by copying the first. One codebase deployed twice was the answer." - Victor Hamers

https://launchstudio.eu/en/blog/single-tenant-vs-multi-tenant-for-b2b-saas

#SaaS #MultiTenant #Supabase #B2B #LaunchStudio #Manifera
