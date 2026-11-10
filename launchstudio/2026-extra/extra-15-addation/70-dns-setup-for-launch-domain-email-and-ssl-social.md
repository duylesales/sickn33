🚨 Anouk van Dijk built Huurcontractcheck with Bolt and Supabase: it helps tenants and small landlords check rental contracts against Dutch rules. On launch day, she followed a tutorial to point her .nl domain to her host - deleting what looked like old records to "clean up". 😳

The site went live within an hour. Her company email stopped working, and nobody noticed until a journalist mentioned she hadn't replied to an interview request. Here's how to set up DNS for launch: domain, email and SSL: 🧠

❌ Deleted MX and SPF records for Microsoft 365
❌ Password resets from an unauthenticated provider landing in spam
❌ Supabase Auth still redirecting to the Bolt preview URL, and a dangling beta. CNAME
❌ The domain registered under a former freelancer's account

✅ MX and SPF restored, DKIM for Microsoft 365 and a mail. subdomain
✅ One combined SPF record and DMARC in monitoring mode
✅ Auth redirect URLs fixed, the dangling record removed and DNSSEC enabled
✅ HTTPS redirects, HSTS and the domain transferred to her company with lock and MFA

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure launching your app doesn't unplug your email. 🛠️

Her result: €1,450, 4 business days. Email was restored the same day, app emails reached inboxes, and Internet.nl showed full marks for HTTPS and email authentication. 🚀

👉 Launching on your own domain? Here's how to set up DNS without breaking email: https://launchstudio.eu/en/blog/dns-setup-for-launch-domain-email-and-ssl

#DNS #EmailAuthentication #SSL #ProductLaunch #AIFounder #LaunchStudio #Manifera
