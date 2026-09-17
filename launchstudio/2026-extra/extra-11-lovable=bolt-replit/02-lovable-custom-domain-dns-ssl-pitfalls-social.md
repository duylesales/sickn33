🚨 Sanne connected her custom domain to Shiftly in one afternoon. Signups came in, but one third of new users never logged in — password resets went straight to spam, and OAuth redirected back to the old preview URL. 😳

Pointing an A-record is only ten percent of going live on a custom domain. Here's what founders forget: 🧠

❌ Transactional emails sent without SPF, DKIM, and DMARC DNS records — dumped into spam folders
❌ OAuth callbacks and magic links still configured with the temporary platform preview address
❌ Apex and www versions fighting for traffic without a canonical 301 redirect
❌ SSL certificate issued for the web root but failing silently on API subdomains

✅ Configure verified DNS authentication (SPF, DKIM, DMARC) for reliable email deliverability
✅ Update all Supabase Auth redirect URLs and site URLs to the canonical production domain
✅ Implement strict apex-to-www canonical redirects and HSTS preloading
✅ Automate SSL provisioning across all production and staging subdomains

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit your complete domain plumbing so your launch day isn't sabotaged by invisible DNS traps. 🌐

Her result: completed registrations for Shiftly in Amsterdam jumped from 66% to over 90% in three weeks with zero changes to product code. 🚀

👉 Make sure your custom domain setup doesn't lose your first customers: https://launchstudio.eu/en/blog/lovable-custom-domain-dns-ssl-pitfalls

#Lovable #CustomDomain #DNS #EmailDeliverability #LaunchStudio #Manifera
