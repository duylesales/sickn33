Would you put the fire alarm in the kitchen? 🔥

Every time someone cooks, it goes off. Soon nobody trusts it. And when there's a real fire, nobody hears it.

That's roughly what happened to Sporthal Online's email.

Jeroen Bos built Sporthal Online with Lovable and Supabase: a booking platform for sports halls and courts run by municipalities and sports foundations. Password resets and confirmations went through Supabase's default email service. A monthly newsletter to all users went out from the same domain through a marketing tool. Neither was domain-authenticated.

Then one large newsletter went out, and support tickets poured in:
• Users couldn't reset their passwords
• New sign-ups never got confirmation emails
• Booking confirmations went missing

Some emails hit the default service's rate limits. Others landed in spam, because the domain had no SPF, DKIM or DMARC and had just been linked to a newsletter several recipients marked as spam. And bounced addresses from old imports kept getting mail.

Moving the alarm out of the kitchen (LaunchStudio, 6 business days, €1,900):
🚨 Transactional email on Postmark, from its own subdomain, with SPF, DKIM and a DMARC policy starting in monitoring mode
🚨 Supabase Auth connected through custom SMTP, with branded Dutch and English templates
🚨 Booking confirmations and reminders on the same transactional stream, through an edge function
🍳 The newsletter moved to Brevo, on a separate authenticated subdomain, with consent records and unsubscribe links
🧹 Bounce and complaint webhooks feeding a suppression table, and users with invalid addresses asked to fix them at next login

Within days, password resets and confirmations reached inboxes reliably. Tickets about missing emails dropped by more than 90%. The next newsletter went out without touching transactional delivery.

"One newsletter took down my login process. Separating the two kinds of email was like moving the fire alarm out of the kitchen." - Jeroen Bos

https://launchstudio.eu/en/blog/transactional-email-providers-resend-vs-postmark-vs-brevo

#EmailDeliverability #Postmark #Brevo #Resend #AIFounder #LaunchStudio #Manifera
