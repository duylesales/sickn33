🔑 Doing support with the keys to the whole building

Imagine giving your part-time colleague a master key to the entire office, just so she can open the post room. She'll open the post room. She might also, by accident, open the server room.

That's roughly how support worked at Weekmenu.

Lotte Hendriks runs a meal-planning subscription from Deventer and built Weekmenu with Bolt and Supabase: about 1,400 subscribers get weekly recipes and shopping lists, paid through Mollie. Most mornings, Lotte and her colleague handled support requests: pausing subscriptions, changing delivery days, issuing credits for missing recipes, fixing accounts stuck after failed payments. All of it in the Supabase and Mollie dashboards, with Lotte's own login.

Twice, the wrong row got edited. Once, a whole week of recipes vanished for a group of subscribers after a mistaken update. Nobody could tell who did what. And refunds in Mollie often never showed up in the app.

What LaunchStudio built: a building where each person has the doors they need (8 business days, €2,900):
🚪 A subscriber search, and a subscriber page with plan, payment history, delivery preferences and recent emails
🚪 Eight support actions covering most requests: pause, resume, change delivery day, issue credit, retry payment and more
🚪 Credits and refunds through the Mollie API, so the app and the provider stay in sync
🚪 Recipe and weekly menu management in the panel
🚪 Separate staff roles for support and admin, with MFA
🚪 An audit log of every action

A support request now takes under a minute instead of several minutes of database work. Lotte's colleague handles support alone, with her own account. And since the panel launched, no data has been changed by mistake.

"I used to do support with the keys to the whole building. Now my colleague has exactly the doors she needs, and I can see who opened which one." - Lotte Hendriks

https://launchstudio.eu/en/blog/admin-panel-development-service-for-ai-built-apps

#AdminPanel #SaaS #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
