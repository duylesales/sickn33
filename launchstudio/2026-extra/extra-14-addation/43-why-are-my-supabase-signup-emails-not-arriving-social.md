Volunteer #1 ✉️
Volunteer #2 ✉️
Volunteer #3 ✉️
...
Volunteer #30 ✉️
Volunteer #31 ·
Volunteer #32 ·
Volunteer #33 ·

Then silence. 🔇

Mirjam Dekkers coordinates a food bank in Helmond and built Voedselhulp in Lovable: volunteers sign up for distribution shifts and get reminders. On launch evening, the first 30 or so volunteers received confirmation emails. After that, nothing. People tried again, created duplicate accounts, and gave up.

Nobody saw an error. Not the volunteers, not Mirjam.

What had happened:
• Supabase's built-in email had hit its sending limit
• The emails that did go out came from a generic address, and several landed in spam
• Password reset links pointed to the Lovable preview domain

What LaunchStudio fixed (3 business days, €850):
✓ Custom SMTP through an EU-region transactional provider
✓ SPF, DKIM and DMARC records on the food bank's domain
✓ Production redirect URLs
✓ Dutch email templates with the food bank's name
✓ One-time codes instead of magic links, for volunteers using work email
✓ Duplicate accounts merged

The next morning, every waiting volunteer was confirmed. Within a month, 210 volunteers had registered, and reminders landed in inboxes, not spam.

"Thirty people got in and then the door quietly closed. Nobody saw an error, including me." - Mirjam Dekkers

https://launchstudio.eu/en/blog/why-are-my-supabase-signup-emails-not-arriving

#Supabase #Lovable #EmailDeliverability #NonProfit #LaunchStudio #Manifera
