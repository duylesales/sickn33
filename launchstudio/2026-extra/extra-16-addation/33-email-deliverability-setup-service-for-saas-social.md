📄 THE DNS ZONE (illustrative, but the pattern was real)

TXT  v=spf1 include:provider-one ~all
TXT  v=spf1 include:provider-two ~all

Two SPF records. Which means SPF fails for every sender. ✉️

Daan Willems runs Bouwbord from Delft, a project management SaaS for architecture firms, built with v0, Cursor and Supabase. Firms signed up, invited their colleagues, and then emailed support: nobody got the invitations. Password resets sometimes took an hour. And one large firm's IT department quarantined every message the app sent.

Daan spent weeks debugging the invitation code. The code was fine. What the inventory found:
• Authentication emails went through Supabase's built-in development email service
• Invitations went through a second provider, from an unverified domain
• The monthly newsletter went out from the main domain through a marketing tool
• Two SPF records, no DKIM for the app's emails, and no DMARC

What LaunchStudio set up (4 business days, €1,450):
✓ Postmark for transactional email, on a dedicated subdomain
✓ Supabase Auth using it for sign-up, magic link and reset emails
✓ The newsletter on a separate marketing subdomain, with one-click unsubscribe
✓ SPF records merged into one, within the lookup limit
✓ DKIM for every sender
✓ DMARC published with monitoring and reporting, moved to quarantine after three weeks of reports
✓ Bounce and complaint webhooks feeding a suppression list
✓ Cleaned-up templates, with plain-text versions

📄 THE DNS ZONE, NOW
One SPF record. DKIM. DMARC.

Invitations and resets arrive within seconds. The large firm's IT released the app's messages after checking the authentication. And tickets about missing emails went from several a week to almost none.

"I spent weeks debugging the invitation code. The code was fine. The problem was two lines of DNS and an email service meant for testing." - Daan Willems

https://launchstudio.eu/en/blog/email-deliverability-setup-service-for-saas

#Email #Deliverability #DMARC #Supabase #AIFounder #LaunchStudio #Manifera
