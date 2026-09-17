🚨 Sanne Bakker launched Shiftly, a shift-matching tool for hospitality staff in Amsterdam, on her custom domain in a single afternoon. Over the next fortnight, one-third (33%) of new users never completed registration — confirmation emails landed straight in spam without SPF/DKIM, and the payment callback still pointed to the old preview URL, causing users to abandon checkout. 😳

Pointing an A-record is only ten percent of going live on a custom domain. Here's what founders forget: 🧠

❌ Transactional emails sent without verified SPF, DKIM, and DMARC DNS records — dumped into spam folders
❌ OAuth callbacks and magic links still configured with temporary platform preview addresses
❌ Apex and www versions competing for traffic without canonical 301 redirects
❌ SSL certificate working on the root domain but failing silently on API and auth subdomains

✅ Configure verified DNS authentication (SPF, DKIM, DMARC) for reliable transactional email delivery
✅ Update all Supabase Auth redirect URLs and site URLs to the canonical production domain
✅ Implement strict apex-to-www canonical redirects and HSTS preloading
✅ Automate SSL provisioning across all production and staging subdomains

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit your complete domain plumbing so your launch day isn't sabotaged by invisible DNS traps. 🌐

Her result: Sanne Bakker completed the domain, email authentication, and callback sweep in 3 business days for €1,150. Completed registrations for Shiftly rose from roughly 66% to over 90% in the following three weeks with zero changes to product code. 🚀

👉 Make sure your custom domain setup doesn't lose your first customers: https://launchstudio.eu/en/blog/lovable-custom-domain-dns-ssl-pitfalls

#Lovable #CustomDomain #DNS #EmailDeliverability #LaunchStudio #Manifera
