Two kinds of logs. Which one does your app write? 🪵

THE OLD KIND (illustrative)
console.log(request)
console.log(member)
→ full names, emails, phone numbers
→ no request ID
→ no line saying whether processing succeeded

THE NEW KIND (illustrative)
webhook.received · request_id · payment_id
webhook.verified
webhook.processed · result · duration_ms
→ internal IDs only
→ every step visible

Joris Peters built Leskaart with Bolt and Supabase: bookings and subscriptions for Dutch dance and yoga studios, where members buy class cards through Mollie. One studio owner noticed that several members had paid for ten-class cards, but their accounts still showed zero classes.

With the old logs, finding out why took two days. Error handling returned 200 even when the database update failed, so Mollie never retried. Retention was the platform default. In the end: a schema change had broken card crediting eleven days earlier, affecting 63 payments across five studios.

What LaunchStudio changed (7 business days, €2,400):
✓ A structured logger recording receipt, verification, result and duration, with internal IDs only
✓ A request ID for every request, returned in error messages
✓ An error status when processing fails, so Mollie retries, plus a structured error that triggers an alert
✓ A table tracking each payment's processing state, and 30-day log retention
✓ A daily job comparing Mollie payments with credited cards, alerting on mismatches
✓ The 63 payments credited and members notified

Two months later, a provider timeout caused a handful of webhook failures. The alert fired within minutes, Mollie retried successfully, and reconciliation confirmed nothing was missing. Joris had the full story from the logs in under five minutes.

"My old logs were full of my customers' phone numbers and told me nothing. Now they tell me exactly what happened, and nothing about anyone's personal life." - Joris Peters

https://launchstudio.eu/en/blog/structured-logging-for-small-saas

#Logging #Observability #Mollie #SaaS #AIFounder #LaunchStudio #Manifera
