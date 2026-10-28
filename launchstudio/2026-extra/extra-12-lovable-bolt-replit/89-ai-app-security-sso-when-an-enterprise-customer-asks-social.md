🚨 Bart Engelen's Leveranciersportaal handles supplier qualification for 14 procurement teams. A regional utility with 2,000 employees wanted to buy - if sign-in went through their Entra ID, enforced, with leavers losing access automatically. He enabled Supabase SAML, let organisations paste their own IdP metadata, and linked users to existing accounts by email. 😳

A review a week before go-live found that any trial account could register its own test identity provider, assert any customer's email address - and be linked straight into that person's account. Here's what SSO for an enterprise customer actually requires: 🧠

❌ No domain verification, so any connection could assert any email domain
❌ Account linking by email, unconditionally
❌ 30-day sessions, so a disabled Entra user kept access for up to a month
❌ No monitoring of SAML certificate expiry

✅ DNS TXT domain verification; every connection limited to verified domains, free email providers refused
✅ Linking only for verified domains, with password sign-in disabled on enforced domains
✅ Just-in-time provisioning at the Member role, Entra groups mapped to roles, enforcement in the API with one logged break-glass owner
✅ 10-hour SSO sessions, SCIM deprovisioning, certificate expiry alerts and a configuration guide for the customer's IT team

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we implement SSO when a product's first enterprise deal depends on it. ⚙️

His result: €5,600, five business days. Logs confirmed nobody had exploited the gap. The utility signed at €38,000 a year - and eleven months later the expiry alert fired, so the certificate rotated without a single locked-out user. 🚀

👉 AI app security: SSO when an enterprise customer asks: https://launchstudio.eu/en/blog/ai-app-security-sso-when-an-enterprise-customer-asks

#SSO #EnterpriseSaaS #AppSecurity #Supabase #LaunchStudio #Manifera
