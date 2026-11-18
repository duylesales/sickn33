📋 SECURITY QUESTIONNAIRE, question 17 (illustrative number)

"Is multi-factor authentication enforced for all users with access to salary data?"
☐ Yes
☑ No

One line. One deal on hold. 🔐

Stefan Huisman built Loonvoorbereider with Cursor and Supabase: payroll preparation for small hospitality businesses, where owners enter hours and the tool prepares data for their payroll provider. A restaurant group with 14 locations wanted to sign. Then its security questionnaire got to that line.

Behind the "No":
• Password login only
• Stefan's own admin accounts could see every customer's salary data, also without MFA
• Password resets could be triggered by anyone who knew an email address, with no rate limit

Turning it into a "Yes" (LaunchStudio, 6 business days, €2,050):
✓ TOTP enrolment and challenge screens
✓ aal2 enforced in RLS policies on salary tables
✓ MFA required for all of Stefan's internal admin accounts
✓ An option for customers to require MFA for all their members
✓ Rate limits on password resets
✓ MFA resets logged, with a verified support procedure

"Is multi-factor authentication enforced for all users with access to salary data?"
☑ Yes

The restaurant group signed after its security officer reviewed the change. Within three months, 70% of all users had MFA on, and three other customers switched on the organisation-wide requirement.

"One line in a questionnaire was worth more than any feature on my roadmap that month." - Stefan Huisman

https://launchstudio.eu/en/blog/how-do-i-add-two-factor-authentication-to-my-app

#MFA #2FA #Supabase #AppSecurity #LaunchStudio #Manifera
