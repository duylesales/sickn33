On launch day, Anouk van Dijk tidied up her DNS. 🌐

She'd built Huurcontractcheck with Bolt and Supabase, a tool that helps tenants and small landlords check rental contracts against Dutch rules. Following a tutorial, she pointed her .nl domain at her hosting platform and deleted what looked like old records, just to keep things clean.

Within an hour, the website was live. It felt like a good day.

It wasn't until a journalist mentioned she'd never replied to an interview request that Anouk found out her company email had stopped working.

The "old records" she'd deleted included the MX records for her Microsoft 365 mailbox, and her SPF record. And once someone looked properly, there was more:
• Password reset emails from the app, sent through an unauthenticated provider, landing in spam
• Supabase Auth still sending users to the Bolt preview URL after they confirmed their email
• A leftover beta. CNAME pointing at a hosting project deleted months earlier
• The domain registered under the account of a freelancer who'd helped with an earlier website

LaunchStudio put it back together (4 business days, €1,450):
→ MX and SPF restored from the email provider's documentation, the same day
→ DKIM for Microsoft 365 and for a transactional provider on a mail. subdomain, one combined SPF record, and DMARC in monitoring mode
→ Supabase Auth's site URL and redirect URLs set to the production domain
→ The dangling beta. record removed, and DNSSEC enabled at the registrar
→ HTTPS redirects and HSTS configured
→ The domain transferred to Anouk's company account, with registrar lock and MFA

Company email came back that same day, app emails began reaching inboxes, and the Internet.nl test showed full marks for HTTPS and email authentication. Anouk now keeps a document listing every DNS record and why it exists.

"I thought I was tidying up old records. I was actually unplugging my own email." - Anouk van Dijk

https://launchstudio.eu/en/blog/dns-setup-for-launch-domain-email-and-ssl

#DNS #EmailAuthentication #SSL #ProductLaunch #AIFounder #LaunchStudio #Manifera
