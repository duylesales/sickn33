🚨 Wouter Klumpenaar's Lidmaatschapbeheer runs membership administration for seven professional associations — around 9,000 members. Every renewal period, a handful of members were charged twice. He spent five months and about forty AI sessions on it. Every fix seemed to work — until the next renewal. 😳

An experienced reader found the cause in ninety minutes: the renewal job could be triggered by two paths in different parts of the codebase, and no single conversation had ever seen both. Here's when to stop prompting and bring someone in: 🧠

❌ The same bug surviving forty sessions over five months
❌ Money moving through the product with no idempotency on charges
❌ Logic duplicated across two paths — and the same pattern elsewhere, sending duplicate welcome emails
❌ Four endpoints with no authorisation check that nobody had noticed

✅ The renewal job made idempotent on member and period, with a test proving a second run charges nothing
✅ Both invocation paths consolidated into one queued job
✅ A reconciliation query that found 31 historical double charges over three years — all refunded
✅ Authorisation tested across 22 endpoints, four gaps fixed, and a handover so Wouter can maintain it all

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we take on the work where mistakes are expensive — while the product stays yours to keep building. ⚙️

His result: €3,400, three business days. The double charges stopped, €2,840 was refunded proactively — and two associations said that refund is why they renewed. 🚀

👉 Vibe coding developer: when to stop prompting and hire: https://launchstudio.eu/en/blog/vibe-coding-developer-when-to-stop-prompting-and-hire

#VibeCoding #Lovable #NoCode #Startups #LaunchStudio #Manifera
