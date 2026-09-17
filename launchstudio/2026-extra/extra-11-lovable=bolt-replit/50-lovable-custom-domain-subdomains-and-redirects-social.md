🚨 Wouter Claassen launched Zaalplanner on `app.zaalplanner.nl` for community halls and sports centres around Tilburg. A month later, search engines indexed an unprotected staging domain (`staging.zaalplanner.nl`), and auth cookies configured on the root domain bled across environments — causing live user sessions to corrupt and staging test accounts to overwrite production data. 😳

Managing multi-domain SaaS architecture requires precise subdomain routing, cookie scoping, and canonical redirects: 🧠

❌ Allowing search engines to crawl and index private staging environments due to missing headers
❌ Scoping authentication cookies to the root domain (`.domain.com`), allowing session leakage across staging and production
❌ Missing canonical 301 redirects between `www` and root apex domains, splitting SEO authority
❌ Misconfigured CORS policies rejecting valid API requests from brand subdomains

✅ Protect all staging and development subdomains behind HTTP Basic Auth or VPN IP whitelisting
✅ Scope authentication cookies strictly to fully qualified hostnames (`app.domain.com`)
✅ Implement strict 301 canonical redirects and HSTS preloading at the DNS and edge layer
✅ Configure dedicated email sending subdomains (`mail.domain.com`) isolated from web routing

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we configure pristine DNS, subdomain, and routing architectures that eliminate cross-environment security risks. 🌐

His result: Wouter Claassen completed the domain structure overhaul in 3 business days for €1,600 (domain structure, staging protection, session scoping, certificates, redirects, sending subdomain). Staging pages disappeared from search within three weeks, session corruption ended, and Zaalplanner has a rock-solid domain foundation. 🚀

👉 Master subdomain routing, cookie scoping, and redirects for your web application: https://launchstudio.eu/en/blog/lovable-custom-domain-subdomains-and-redirects

#DNS #CustomDomain #DevOps #WebSecurity #LaunchStudio #Manifera
