🧾 ITEMISED: what one Supabase bill was really paying for

Gijs Kramer built Evenementenhub with Bolt and Supabase: event organisers sell tickets, publish programmes and share photos with attendees. Revenue grew steadily. The Supabase bill grew faster, until it was one of the company's biggest costs. Gijs had upgraded compute twice when pages got slow, and was thinking about switching providers.

The review read the bill line by line.

LINE 1: Two old prototypes, still on paid compute
LINE 2: A demo project for one large customer, still running
LINE 3: A staging project, one of four with paid compute, plus point-in-time recovery switched on in one of them
LINE 4: Egress, mostly event photos served at full size
LINE 5: A request log table, written on every page view, grown to tens of gigabytes
LINE 6: A realtime subscription on the programme page that reconnected on every navigation
LINE 7: Thousands of retried function calls a day, from a ticketing webhook that kept failing
LINE 8: Hundreds of fake accounts a week, created by bots through the open sign-up form
LINE 9: Two compute upgrades, bought to hide slow queries

The corrections (LaunchStudio, 6 business days, €2,400):
✂️ The two prototypes deleted, the demo paused, staging on smaller compute without add-ons
✂️ Photos resized into variants and served through a CDN
✂️ The request log replaced by the hosting platform's logs, with the old table archived and dropped
✂️ The realtime subscription cleaned up, and the webhook handler repaired
✂️ Turnstile on sign-up, with unconfirmed accounts removed after a week
✂️ Slow queries indexed and policies optimised, so production could move back to smaller compute

THE NEW TOTAL
Roughly 60% lower, while usage kept growing. Pages faster than before the downgrade. Gijs stayed with Supabase and now checks the usage page every month.

"I was paying for prototypes I'd forgotten, photos nobody needed at full size and a webhook that kept failing at night." - Gijs Kramer

https://launchstudio.eu/en/blog/why-does-my-supabase-bill-keep-growing

#Supabase #CloudCosts #EventTech #FinOps #AIFounder #LaunchStudio #Manifera
