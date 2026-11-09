📧 Daan Willems runs a project management SaaS for architecture firms from Delft, built with v0, Cursor and Supabase. Firms signed up, invited colleagues and then emailed support: nobody received the invitations. Password resets sometimes took an hour, and a large firm's IT department quarantined every message from the app. 📭

He spent weeks debugging the invitation code. The code was fine. The setup wasn't: 🧠

❌ Auth emails sent through Supabase's built-in development email service
❌ Invitations from a second provider on an unverified domain
❌ Two SPF records, so SPF failed for every sender, and no DKIM or DMARC
❌ The newsletter sent from the main domain, mixing marketing with transactional mail

✅ Postmark for transactional email on a dedicated subdomain, connected to Supabase Auth
✅ The newsletter moved to a separate marketing subdomain with one-click unsubscribe
✅ SPF merged within limits, DKIM for every sender and DMARC with reporting, then quarantine
✅ Bounce and complaint webhooks, a suppression list and clean templates with plain text

At **LaunchStudio**, backed by Manifera's 11+ years of running production systems that send email for clients such as Vodafone and TNO, we make sure your app's emails reach the inbox. 🛠️

His result: €1,450, four business days. Invitations and resets arrive within seconds, and missing-email tickets dropped to almost none. 🚀

👉 Email deliverability setup service for SaaS: https://launchstudio.eu/en/blog/email-deliverability-setup-service-for-saas

#Email #Deliverability #DMARC #Supabase #AIFounder #LaunchStudio #Manifera
