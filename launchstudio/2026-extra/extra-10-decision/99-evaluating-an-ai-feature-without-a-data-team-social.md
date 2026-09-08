📉 Daria fixed a billing-category bug, tested it on 4 cases, shipped it — and quietly dropped her biggest category's accuracy from 91% to 63%. 😅

Testing a prompt change only on the cases it's meant to fix is exactly how this happens. Here's the damage: 🧠

❌ She tested the fix on the 4 billing complaints it was meant to solve — and only those 4
❌ The added emphasis on billing made the model tag anything mentioning an amount as billing, including meter disputes and connection requests
❌ Accuracy on the largest category fell from ~91% to 63% while billing improved by just a few points
❌ Nobody caught it for 2 weeks — the only signal was complaint volume from teams receiving misrouted work

✅ Build a 30–50 example test set from real, anonymised inputs across every category, not just the one you're fixing
✅ Run the set before and after every change, and look specifically at what got worse
✅ Roll out behind a flag to a small share of volume first, watching accuracy before going wide
✅ Track the correction and retry rate in production as the signal your offline set can't capture

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn prompt iteration from guesswork into a measured, repeatable process. 📊

Her result: a 45-complaint test set across all 8 categories, staged rollout at 10% of volume, and the evaluation workflow delivered in 2 business days. 🚀

👉 Find out if your last prompt change actually helped: https://launchstudio.eu/en/blog/evaluating-an-ai-feature-without-a-data-team

#AIEval #PromptEngineering #SaaS #IndieHacker #LaunchStudio #Manifera
