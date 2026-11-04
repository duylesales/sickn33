🚨 Stefan Huisman built Loonvoorbereider with Cursor and Supabase: a payroll preparation tool for small hospitality businesses. A restaurant group with 14 locations wanted to sign. Then their security questionnaire asked: "Is multi-factor authentication enforced for all users with access to salary data?" The answer was no. 😳

One line in a questionnaire was worth more than any feature on his roadmap that month. Here's what the app was missing: 🧠

❌ Password login only, for everyone
❌ Internal admin accounts that could see every customer's salary data - also without MFA
❌ Password resets anyone could trigger with just an email address, with no rate limit
❌ No way for business customers to require MFA for their own staff

✅ TOTP enrolment and challenge screens with authenticator apps
✅ aal2 enforced in RLS policies on salary tables - not just hidden pages
✅ MFA required for all internal admins, with an organisation-wide requirement customers can switch on
✅ Rate limits on password resets and a verified, logged recovery procedure

At **LaunchStudio**, backed by Manifera - whose founder Herre Roelevink built his career in cybersecurity at CFLW - we enforce MFA where it counts: on the server. 🛠️

💡 His result: €2,050, six business days. The restaurant group signed after its security officer reviewed the change, 70% of users enabled MFA within three months, and three more customers turned on the organisation-wide requirement. 🚀

👉 Business customers asking for two-factor authentication? Here's how to add MFA to a Supabase app properly: https://launchstudio.eu/en/blog/how-do-i-add-two-factor-authentication-to-my-app

#MFA #2FA #Supabase #AppSecurity #LaunchStudio #Manifera
