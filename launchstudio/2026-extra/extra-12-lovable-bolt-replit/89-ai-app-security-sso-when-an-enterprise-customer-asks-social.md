🧭 The path a pre-launch review found, in plain words

START: any organisation, a free trial included, could register its own identity provider.
GAP 1: nothing limited which email domains that provider could claim.
GAP 2: incoming users were linked to existing accounts by email address alone.
END: a trial account could claim the address of any user at any customer, and be linked straight into their account.

And a second path, slower but real: sessions lasted thirty days, so an employee disabled in the customer's directory could keep access for up to a month.

Bart Engelen built Leveranciersportaal in Lovable: supplier qualification and certificate management for 14 procurement teams. A regional utility with around 2,000 employees wanted to buy, on one condition: sign-in through their Entra ID, enforced, with leavers losing access automatically. Bart enabled Supabase SAML, added a screen for pasting identity provider metadata, and linked by email so trial users kept their data. The review came a week before go-live. ⚡

Closing both paths (LaunchStudio, 5 business days, €5,600):
✓ Domain verification through DNS TXT records, with each connection limited to the organisation's verified domains, and free email providers refused
✓ Account linking only on verified domains, with password sign-in turned off for linked accounts on enforced domains
✓ The metadata screen restricted to verified organisations on the enterprise plan
✓ Just-in-time provisioning at Member, with three Entra groups mapped to roles and re-checked at every sign-in
✓ Enforcement in the API as well as the sign-in page, plus one logged break-glass owner at the utility
✓ SSO sessions cut to ten hours
✓ SCIM directory sync through a dedicated identity layer, so deactivated employees lose access within minutes
✓ Certificate expiry stored, with an alert at sixty days
✓ A configuration guide for the utility's IT department

Logs confirmed no other organisation had registered an SSO connection before the fix. The utility signed for €38,000 a year, and its IT team configured the connection in an afternoon. Eleven months later the expiry alert fired, and the certificate was rotated without a single locked-out user.

"I had built SSO that let any trial account sign in as anyone at any customer, as long as it typed their email address into its own test identity provider. The review found it a week before the utility went live." - Bart Engelen

https://launchstudio.eu/en/blog/ai-app-security-sso-when-an-enterprise-customer-asks

#SSO #EnterpriseSaaS #AppSecurity #Supabase #LaunchStudio #Manifera
