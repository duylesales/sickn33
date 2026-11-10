🚨 Tessa Groen built Inwerkplan with Lovable and Supabase: new employees follow personalised onboarding checklists and training. A hospital group in Zuid-Holland wanted it for around 3,000 staff - on one condition: login through Microsoft Entra ID, with automatic removal of leavers. 😳

Inwerkplan only supported magic links. A "Sign in with Microsoft" button didn't meet the requirement. Here's what SAML SSO really means for B2B SaaS: 🧠

❌ Only magic link login
❌ A Microsoft social button allowing any Microsoft account
❌ No mapping to the hospital's organisation or groups
❌ No deprovisioning when staff left, and existing pilot accounts to merge

✅ SAML SSO through Supabase Auth with Entra ID, after verifying two email domains
✅ Users provisioned on first login, with roles mapped from Entra ID groups
✅ Pilot accounts linked by verified email, preserving progress
✅ Other logins blocked for hospital domains, SCIM deprovisioning, audit logs and an IT guide

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your customer's IT department in control of every account, from first day to last. 🛠️

Her result: €6,500, 16 business days. Approved after one test session, around 1,100 new employees onboarded in year one, leavers lose access within minutes - and two more healthcare organisations signed. 🚀

👉 Asked for SAML SSO by a big customer? Here's how to implement it: https://launchstudio.eu/en/blog/saml-sso-implementation-for-b2b-saas

#SSO #SAML #EntraID #HealthTech #B2BSaaS #LaunchStudio #Manifera
