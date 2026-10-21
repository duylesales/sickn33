🚨 Evelien Hartman's Tandartsplanner handles scheduling and online booking for 58 dental practices. A new booking widget went live to every practice at once on a Monday morning. For practices sharing one chair between a dentist and a hygienist, availability was calculated wrong. By ten o'clock, eleven practices had double-booked chairs. 😳

Switching it off meant a rollback that also undid a migration and two fixes — so online booking was down everywhere for the morning. The same month, an AI recall feature spiked in cost and couldn't be stopped without a deploy. Here's how feature flags let you release to some customers first: 🧠

❌ Deploy and release as the same moment, for all 58 practices
❌ No way to switch off one feature without rolling back everything
❌ No kill switch for an AI feature that cost money per call
❌ The largest and most complex practices meeting new features at the same time as everyone else

✅ A flag table with owners and expiry dates, per-practice overrides and stable percentage rollouts
✅ Flags evaluated on the server, with only results sent to the browser — never used as a security boundary
✅ Kill switches for AI suggestions, SMS reminders and the booking widget, each with a clean "temporarily unavailable" state
✅ A beta group of six practices, errors tagged by active flag, a flag-change audit and tests with flags on and off

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make releases routine for products customers rely on every day. ⚙️

Her result: €2,800, three business days. The fixed widget went out via beta, then 25%, then everyone — zero double bookings. Nine features followed the same way; one bug was caught at three practices and switched off in under a minute. 🚀

👉 Lovable hosting: feature flags and releasing to some customers first: https://launchstudio.eu/en/blog/lovable-hosting-feature-flags-and-releasing-to-some-customers-first

#FeatureFlags #DevOps #SaaS #Lovable #LaunchStudio #Manifera
