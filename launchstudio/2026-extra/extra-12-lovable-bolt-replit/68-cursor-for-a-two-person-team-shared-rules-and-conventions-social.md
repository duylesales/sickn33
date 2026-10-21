🚨 Steven Doornekamp and his co-founder built Zorgdeclaratie in Cursor — declaration handling between 52 allied health practices and insurers. They split the work by feature and built in parallel for four months. No rules file, no review. Then, at the end of December, 60 declarations went out with the wrong period and two insurers rejected them. 😳

The cause: each half calculated week numbers with a different date library — and they disagreed. One repository, two products inside it. Here's how a two-person team keeps AI editors building one codebase: 🧠

❌ Two date libraries, two form approaches, two validation libraries in one repo
❌ Errors thrown in one half and returned as values in the other
❌ Plural table names on one side, singular on the other
❌ Neither founder able to work in the other's half — a week of illness stopped half the product

✅ A rules file written together in an afternoon, from the actual code: one library per job, five never-broken rules
✅ The losing libraries removed; date handling unified with a test from the insurer specification
✅ Every change through a pull request with a five-minute diff review by the other person
✅ One shared vocabulary — declaration, practice, insurer, period — replacing three sets of synonyms

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we write this rules file when we hand a project to a client team — it's what keeps the work consistent after we leave. ⚙️

Their result: €3,100, three business days. The 60 declarations were resubmitted — and when his co-founder was away for two weeks, the product kept moving. 🚀

👉 Cursor for a two-person team: shared rules and conventions: https://launchstudio.eu/en/blog/cursor-for-a-two-person-team-shared-rules-and-conventions

#Cursor #SmallTeams #CodeReview #AICoding #LaunchStudio #Manifera
