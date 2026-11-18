🏥 From first day to last day: what a hospital means by "SSO"

Tessa Groen built Inwerkplan with Lovable and Supabase: new employees follow personalised checklists, complete training modules and meet their buddies. After pilots with smaller companies, a hospital group in Zuid-Holland wanted it for all new staff, around 3,000 employees across several locations. One condition: login through Microsoft Entra ID, and automatic removal of leavers.

Inwerkplan only had magic links. Tessa's first try, a "Sign in with Microsoft" button, missed the point. It let in any Microsoft account, didn't link users to the hospital, ignored the hospital's groups and did nothing when people left. Some hospital staff also already had magic-link accounts from the pilot.

Here's the employee lifecycle LaunchStudio built (16 business days, €6,500):

BEFORE DAY ONE
The hospital's two email domains verified through DNS records. SAML SSO configured through Supabase Auth with the hospital's Entra ID.

DAY ONE
First login provisions the employee into the hospital's organisation. Their role, HR, manager or new employee, comes from their Entra ID group.

PILOT USERS
Existing accounts linked by verified email, with progress kept.

EVERY DAY
Magic links and passwords blocked for the hospital's domains. Sessions limited to working-day durations. SSO and provisioning events written to an audit log.

LAST DAY
SCIM provisioning through a dedicated service deactivates the user automatically when they're disabled in Entra ID.

FOR THE IT TEAM
A setup guide with screenshots.

The hospital's IT approved after one test session. In the first year, around 1,100 new employees onboarded through Inwerkplan, and leavers lost access within minutes of being disabled. Two more healthcare organisations signed after hearing about the integration.

"I thought SSO meant a 'Sign in with Microsoft' button. For the hospital, it meant their IT department staying in control of every account, from the first day to the last." - Tessa Groen

https://launchstudio.eu/en/blog/saml-sso-implementation-for-b2b-saas

#SSO #SAML #EntraID #HealthTech #B2BSaaS #LaunchStudio #Manifera
