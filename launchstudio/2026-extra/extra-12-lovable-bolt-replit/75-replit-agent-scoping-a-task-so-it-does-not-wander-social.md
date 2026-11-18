📦 DELIVERY NOTE

ORDERED (one sentence):
1 × weekly summary email

DELIVERED:
1 × weekly summary email ✅ works
1 × scheduling library ❓ the project already had scheduled deployments
1 × new "notifications" table ❓ duplicating the existing "alerts" table
1 × restyled alert email template ⚠️ changed the alerts 34 customers were already getting, "for consistency"
1 × removed rate-limiting check ⚠️ taken out because it got in the way of the summary job

Jasper Nieuwland built Voorraadmelding on Replit: low-stock alerting for hospitality suppliers, notifying 34 restaurants and cafés when items they order regularly run low. He asked the agent for a weekly summary. 🍽️

He spotted the template change when a customer asked why their alerts looked different. The missing rate limit showed itself two weeks later, when a misconfigured integration at one restaurant set off 900 alert emails in an hour.

RETURNS AND RE-ORDER (LaunchStudio, 2 business days, €2,400):
✓ The summary rebuilt as three scoped tasks (query, template, scheduled trigger), each with explicit boundaries and a check
✓ The extra scheduling library removed
✓ The "notifications" table dropped after confirming nothing had written to it, with the existing "alerts" table used instead
✓ The alert template restored, and the summary given a template of its own
✓ The rate limit reinstated, with a test asserting it
✓ A conventions file naming the scheduling approach and the notifications table, with a rule that existing templates are never changed as a side effect
✓ 26 tests covering notification volume limits and alert and summary generation
✓ A habit: commit before each run, work on a branch, read the whole diff

The 900-email incident cost Jasper one customer, who left citing the volume of mail. The rebuild took an afternoon. Working out what the original run had actually changed took longer.

"I asked for a weekly summary email. I got one, plus a library I did not need, a duplicate table, a change to emails thirty-four customers were already getting, and a rate limit quietly removed because it was in the way." - Jasper Nieuwland

https://launchstudio.eu/en/blog/replit-agent-scoping-a-task-so-it-does-not-wander

#Replit #AIAgents #NoCode #AICoding #LaunchStudio #Manifera
