📜 HOUSE RULES for a codebase with two AI tools

Marieke Verbeek, a former logistics planner in Venlo, built Laadplanner in Lovable: a tool for small transport companies to plan loading slots at warehouses. When it outgrew Lovable, she exported it to GitHub and switched to Cursor. Her part-time freelance developer preferred Claude Code. Within two months, the codebase showed it:
• Cursor sessions put data access straight into components with the Supabase client
• Claude Code sessions added server actions with Drizzle on a privileged connection, some queries scoped to the transport company, some not
• Three different error handling patterns
• Translations partly hard-coded
• Each tool had added its own date library
• No instructions for either tool, and changes pushed straight to main, which deployed automatically

The house rules LaunchStudio agreed with Marieke and the freelancer (10 business days, €3,700):

RULE 1: Browser reads go through the Supabase client, protected by Row Level Security.
RULE 2: Writes go through server actions using one scoped data access module.
RULE 3: One way to handle errors. One way to translate. One date library.
RULE 4: Both tools read the same instruction document, referenced from Cursor rules and from CLAUDE.md, covering architecture, security rules, conventions and protected paths.
RULE 5: Nobody pushes to main. Branch protection and pull request reviews.
RULE 6: Tests run on every change, including negative authorisation tests.
RULE 7: Everything passes through staging first.

Before the rules took effect, the unscoped queries were fixed, and duplicate dependencies removed.

The result: Marieke and her freelancer still use their favourite tools, but every change follows the same patterns. Over the next quarter, the tests caught several AI-generated changes that would have bypassed tenant scoping. Laadplanner signed its first warehouse operator, with over 200 transport company users.

"The argument about which tool was better turned out to be the wrong argument. What we needed was one set of rules both tools had to follow." - Marieke Verbeek

https://launchstudio.eu/en/blog/claude-code-vs-cursor-for-founders

#ClaudeCode #Cursor #AICoding #Logistics #AIFounder #LaunchStudio #Manifera
