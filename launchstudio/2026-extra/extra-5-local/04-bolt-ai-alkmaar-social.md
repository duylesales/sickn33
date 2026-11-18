Eleven vendors. One month. One key nobody should ever have seen.

Joost van Dijk grew up watching the logistics behind Alkmaar's cheese market up close. So he built MarketWeigh in Bolt in about two weeks: inventory weights, pricing and invoicing for small food producers and market vendors.

Eleven paying vendors signed up in the first month.

Then a fellow founder opened developer tools on the public site, just out of curiosity. And there it was in the network requests: Joost's live Stripe secret key.

Not a test key. The live one. The one that can issue refunds and pull transaction data.

That founder was friendly. The next visitor might not have been.

"Someone could have drained transactions from eleven small businesses because of a mistake I didn't even know was possible to make." - Joost van Dijk

What our engineers did in 5 business days (€1,400):
→ Moved all payment logic to a server-side layer
→ Rotated every credential that had ever been exposed
→ Audited the rest of the codebase, and found two more leaks, including a mapping API key

Today MarketWeigh runs every payment through a secured backend. A follow-up scan found zero client-exposed credentials.

Bolt got Joost to his first eleven customers. Keeping their money safe took a different kind of work.

Built your SaaS with Bolt AI? Check your network tab before a stranger does: https://launchstudio.eu/en/blog/bolt-ai-alkmaar

#AINativeFounder #LaunchStudio #Manifera #BoltAI #Alkmaar
