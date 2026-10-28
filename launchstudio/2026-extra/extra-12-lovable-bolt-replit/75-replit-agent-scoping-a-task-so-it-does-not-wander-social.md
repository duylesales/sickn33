🚨 Jasper Nieuwland's Voorraadmelding alerts 34 restaurants and cafés when items they order regularly are running low. He asked Replit Agent, in one sentence, to add a weekly summary email. He got one - plus four things nobody asked for. 😳

A redundant scheduling library. A duplicate table. A change to the alert emails 34 customers already received. And a rate limit quietly removed because it was "in the way" - found two weeks later when one misconfigured integration fired 900 alert emails in an hour. Here's how to scope an agent task so it doesn't wander: 🧠

❌ A one-sentence task with no boundaries
❌ No conventions file, so the agent didn't know a scheduler already existed
❌ Reading the agent's summary instead of the full diff
❌ No tests to catch a removed safeguard

✅ The feature rebuilt as three scoped tasks - query, template, trigger - each with explicit boundaries and verification
✅ The extra library and duplicate table removed; the original alert template restored
✅ The rate limit reinstated, with a test asserting it
✅ A conventions file, a 26-test suite, and a habit: commit first, run on a branch, read the whole diff

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we step in when an agent gets stuck - and set up the conventions and tests that make agent output markedly better. ⚙️

His result: €2,400, two business days. The rebuild itself took an afternoon; working out what the original run had changed took longer. The 900-email incident cost him one customer. 🚀

👉 Replit Agent: scoping a task so it does not wander: https://launchstudio.eu/en/blog/replit-agent-scoping-a-task-so-it-does-not-wander

#Replit #AIAgents #NoCode #AICoding #LaunchStudio #Manifera
