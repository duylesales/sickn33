👁️ What the tools saw, and what they never saw

WHAT THE TOOLS SAW
✓ Every pull request, with thoughtful comments from an AI reviewer
✓ Dependencies, through Dependabot
✓ Secrets, through secret scanning
✓ Monthly Supabase advisor checks: no critical warnings

WHAT THE TOOLS NEVER SAW
✗ An invoices table policy letting any logged-in user read every row, created months earlier in the dashboard and never part of a pull request
✗ Quote PDFs in a public bucket
✗ Password reset redirects that accepted any URL
✗ Backups that had never been restored

Kim Hoogendoorn runs Moodportaal from Amsterdam, a client portal for interior designers built with Claude Code and Supabase: designers share mood boards, quotes and invoices with clients. With all those tools in place, Kim felt confident. Then a larger design studio asked for a security review before onboarding 40 clients.

LaunchStudio's role-based testing found the second list (5 business days, €2,000). Then:
✓ Policies rewritten per designer and client
✓ Access tests that run in the pipeline
✓ Files moved to private storage
✓ Redirects restricted
✓ A tested restore
✓ The setup documented

Kim's existing tools all stayed. They just got company: tests that encode the access rules themselves.

The design studio onboarded its 40 clients after reading the summary report. Two months later, an AI-generated change that would have widened the invoice policy failed the access test before it could be merged.

"My tools reviewed every line I changed. Nobody had reviewed the lines I never changed, or the settings that were not in the code at all." - Kim Hoogendoorn

https://launchstudio.eu/en/blog/launchstudio-vs-ai-code-review-tools

#CodeReview #Security #ClaudeCode #Supabase #AIFounder #LaunchStudio #Manifera
