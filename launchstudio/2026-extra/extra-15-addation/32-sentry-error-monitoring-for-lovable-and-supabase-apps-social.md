📟 THE FIRST 48 HOURS OF A NEW ERROR DASHBOARD

BEFORE HOUR 0
Kim Janssen built Declaratiedesk with Lovable and Supabase: employees photograph receipts and submit expense claims, managers approve them. 18 companies after launch. Sign-ups kept coming, but usage at several customers dropped sharply. Only one customer complained: "it sometimes doesn't work." There was no error monitoring at all.

HOUR 0
LaunchStudio adds Sentry to the frontend and edge functions, with source maps uploaded through a new GitHub deployment pipeline.

WITHIN 48 HOURS, THREE ISSUES SURFACE
1. On iOS Safari, receipt photos in HEIC format failed to upload. The compression step didn't support HEIC. The error went to the console, while the interface showed a successful submission.
2. Amounts typed with a comma as decimal separator, as Dutch users naturally do, broke claims.
3. An edge function timed out generating monthly reports for larger companies.

THE FOLLOWING DAYS (7 business days, €2,200)
✓ HEIC conversion with a fallback
✓ Number parsing fixed for Dutch input
✓ Report generation moved to a background job
✓ Error boundaries around the main areas, and clear messages instead of swallowed errors
✓ Privacy settings: no PII collection, masked replays, amounts and IBANs scrubbed
✓ Alerts for new issues and for any error in submission and approval flows

TWO WEEKS LATER
Failed submissions close to zero. Usage at the affected customers recovered. And one uncomfortable discovery: around 30% of iPhone submissions had silently failed since launch.

EVERY MONDAY SINCE
Kim opens the Sentry dashboard.

"My customers weren't complaining. They were just quietly giving up. Sentry showed me in two days what I'd missed for two months." - Kim Janssen

https://launchstudio.eu/en/blog/sentry-error-monitoring-for-lovable-and-supabase-apps

#Sentry #ErrorMonitoring #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
