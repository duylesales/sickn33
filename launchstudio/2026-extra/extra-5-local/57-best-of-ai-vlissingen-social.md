⭐ REVIEW: Building PortWatch with Cursor

Reviewer: Joost Dekker, founder of PortWatch, a berth scheduling and vessel-tracking tool for smaller shipping agents in Vlissingen's port

Tool chosen after: a week of reading best-of-AI comparisons

Control over the code: ★★★★★
Code quality: ★★★★★
Extensible codebase: ★★★★★
Production readiness: not rated in any comparison he read

The comparisons were right about Cursor. It gave Joost a clean, extensible codebase. What they never covered was his own database configuration: vessel schedules and agent contact details were readable by any logged-in user, whichever shipping agency they belonged to.

LaunchStudio's review (5 business days, €1,450):
• Added the missing row-level security
• Added rate limiting, so one agent's system can't overwhelm the shared scheduling endpoints
• Moved validation of schedule updates to the server, instead of trusting the frontend

None of it was about Cursor being the wrong choice. It was the gap between picking a good tool and having a production-ready result.

Rating after the fix: PortWatch now serves multiple shipping agents with properly isolated data and stable performance under real port-scheduling load.

"I spent a week comparing tools before I even started building. I spent zero minutes thinking about what happened to the code after. Turns out that second part was the part that actually mattered." - Joost Dekker

Read the best-of-AI lists, then check what they leave out: https://launchstudio.eu/en/blog/best-of-ai-vlissingen

#AINativeFounder #LaunchStudio #Manifera #BestOfAI #Vlissingen
