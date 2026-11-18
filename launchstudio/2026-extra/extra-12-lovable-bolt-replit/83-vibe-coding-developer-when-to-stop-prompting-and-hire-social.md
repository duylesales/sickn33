🕵️ THE CASE OF THE DOUBLE CHARGE

The crime: a few members charged twice for their annual fee. About eight a year, always during renewals, never reproducible.

The victim's business: Lidmaatschapbeheer, membership administration Wouter Klumpenaar built in Lovable for seven professional associations, around 9,000 members.

The investigation so far: forty AI sessions over five months. Each found a fix. Each fix seemed to work. Each renewal period brought the same complaints.

Enter an experienced reader. Time to solve: ninety minutes.

THE SUSPECTS
Suspect A: the scheduled renewal run.
Suspect B: a manual administrator action.
Both triggered the same renewal job. Neither job had idempotency.

THE SOLUTION
Both suspects did it. When both ran in the same window for the same member, two charges went out. No session had ever seen both, because they lived in different parts of the codebase and each conversation was only ever shown one. 🔍

CLOSING THE CASE (LaunchStudio, 3 business days, €3,400)
✓ The renewal job made idempotent on member and period, with a test proving a second call charges nothing
✓ Both paths now enqueue the same job, not duplicate logic
✓ A review for the same pattern elsewhere, which found two more, one sending duplicate welcome emails nobody had reported
✓ A reconciliation of charges against periods: 31 historical double charges across three years, all refunded
✓ Authorisation tested across 22 endpoints: four had no check, now fixed
✓ A handover so Wouter can maintain it

The double charges stopped. The 31 old ones came to €2,840 in refunds, and two associations said the proactive refund was why they renewed. Wouter's own note is about the five months, not the money.

"Forty sessions across five months on a bug that took someone ninety minutes, because it was in two files and no conversation ever saw both of them at once." - Wouter Klumpenaar

https://launchstudio.eu/en/blog/vibe-coding-developer-when-to-stop-prompting-and-hire

#VibeCoding #Lovable #NoCode #Startups #LaunchStudio #Manifera
