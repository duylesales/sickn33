🚪 One house, three front doors

Door 1: Supabase Auth, for workers.
Door 2: a custom session system for businesses, written during one debugging session.
Door 3: an old magic-link route nobody used anymore, still unlocked.

Floor Bakker had built a product she was scared of. 🏨

She runs Shiftwerk, a recruitment SaaS for hospitality from Utrecht, built over eight months with Cursor and later Claude Code, using Next.js, Supabase and Stripe. Restaurants post shifts, workers apply. Around 300 businesses and 4,000 workers. But bugs were increasing, and there were files Floor didn't dare to touch.

Behind the doors, the review found more:
• API routes that checked whether you were logged in, but not whether the shift belonged to your business
• Two Stripe keys in a committed script
• 140 dependencies, around 30 of them unused
• No tests
• Deployments from Floor's laptop

What LaunchStudio did (9 business days, €3,400):
✓ One front door: everything on Supabase Auth, with business accounts migrated and the old route removed
✓ Ownership checks on every API route, through one shared helper
✓ Keys rotated, moved to environment variables, and the repository history cleaned
✓ Unused dependencies removed, the rest updated
✓ Tests for login, access between businesses, applications and Stripe webhooks
✓ A GitHub pipeline deploying previews and production on Vercel, with database migrations
✓ Project rules for both Cursor and Claude Code

In the next two months, bug reports dropped noticeably and build times fell by around a third. Floor went back to building every week, and the tests blocked two changes that would have broken access between businesses.

"I had built a product I was scared of. Now I have a codebase with rules, and my AI assistant follows them better than I did." - Floor Bakker

https://launchstudio.eu/en/blog/cost-to-make-a-cursor-or-claude-code-app-production-ready

#Cursor #ClaudeCode #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
