🚨 Ellen Wijnands built Kraamzorgplanner in Lovable: scheduling for maternity care organisations, matching care assistants to new families. With four organisations as customers, she hired a developer - who recommended a six-month rebuild in a different stack because of "unmaintainable AI code". Two more organisations were waiting to sign. 😳

The code wasn't how a developer would have written it. That didn't mean it had to be thrown away. Here's what the decision matrix showed: 🧠

❌ Care assistant availability duplicated across three tables
❌ Gaps in Row Level Security between organisations
❌ Matching logic scattered across components
❌ No staging, CI or tests to change things safely

✅ Availability consolidated into one table with a migration
✅ Matching logic moved into a tested database function
✅ RLS fixed per organisation
✅ End-to-end tests for scheduling, plus staging and CI - with the interface planners loved kept intact

At **LaunchStudio**, backed by Manifera's 11+ years of taking over and modernising client codebases, we refactor by default and rebuild only by exception - keeping your frontend and fixing what's needed. 🛠️

💡 Her result: €3,900, ten business days. The refactor took two weeks instead of six months, both waiting organisations signed, and the developer kept building on the refactored codebase. 🚀

👉 Rebuild or refactor your AI-built app? Here's the decision matrix: https://launchstudio.eu/en/blog/rebuild-vs-refactor-an-ai-built-app

#Refactoring #Lovable #Supabase #SaaS #LaunchStudio #Manifera
