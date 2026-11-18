⚖️ THE CASE OF KRAAMZORGPLANNER: rebuild or refactor?

THE DEFENDANT
Kraamzorgplanner, built by Ellen Wijnands in Lovable: scheduling for maternity care organisations, matching care assistants to new families. Four organisations as customers.

THE PROSECUTION
A newly hired developer: "Unmaintainable AI code. Rebuild in a different stack. Six months."

THE EVIDENCE, scored with Ellen
Exhibit A, the interface: highly valued by planners
Exhibit B, the data model: mostly sound, though care assistant availability was duplicated in three tables
Exhibit C, security: fixable, mainly RLS gaps
Exhibit D, the stack: React and Supabase could support the roadmap
Exhibit E, business timing: two more organisations waiting to sign

THE VERDICT
Refactor.

THE SENTENCE (LaunchStudio, 10 business days, €3,900)
✓ Availability consolidated into one table, with a migration
✓ The matching logic moved into a tested database function
✓ RLS fixed per organisation
✓ End-to-end tests for scheduling
✓ Staging and CI

AFTER THE TRIAL
Two weeks instead of six months. Both waiting organisations signed. And the developer stayed on, adding features to the refactored codebase through the new pipeline.

"The code wasn't how a developer would have written it. That didn't mean it had to be thrown away." - Ellen Wijnands

https://launchstudio.eu/en/blog/rebuild-vs-refactor-an-ai-built-app

#Refactoring #Lovable #Supabase #SaaS #LaunchStudio #Manifera
