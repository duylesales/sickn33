6 months.
~40 changes shipped by the founder herself, in Lovable.
2 times the access tests failed.
2 fixes, made by asking Lovable to fix the failing test.
5 changes sent for review.
5 answers, each within a working day.
0 security or payment regressions in production. 🐩

Jolien Verbeek runs Trimplanner from Hoorn, a SaaS for dog grooming salons built with Lovable and Supabase, used by around 90 salons for appointments, client records and payments. After a Launch & Grow project, she had one fear: that her habit of improving the app every week in Lovable would undo the security work. It had happened before, when a prompt disabled a database policy to fix an error, and nobody noticed for a month.

What the project left in place:
• Lovable connected to GitHub
• Project knowledge in Lovable, plus rules in the repository describing the data model, salon separation, payment handling and migration patterns
• Access and webhook tests in the pipeline
• An agreement: any change involving new tables, roles or payments goes for review

What the two failed tests caught:
1. A prompt that created a new table for pet notes, without a policy
2. A change to the appointment query that dropped the salon filter

What went for review included a new subscription plan.

All of it fit within ongoing care at €49 a month, after the original €3,600 Launch & Grow project.

Jolien kept her weekly rhythm. And the salons noticed the app getting better, not more fragile.

"I was afraid that after the project I would have to stop building. Instead, the tests tell me when Lovable makes a mistake, and I fix it before anyone notices." - Jolien Verbeek

https://launchstudio.eu/en/blog/how-launchstudio-works-with-your-ai-tool-after-launch

#Lovable #AICoding #VibeCoding #SaaS #AIFounder #LaunchStudio #Manifera
