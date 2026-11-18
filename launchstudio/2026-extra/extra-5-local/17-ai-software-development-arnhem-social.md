What the AI planned for vs. what customers actually did 💳

PLANNED: A customer signs up, takes the style quiz, and gets charged every month.
ACTUAL: Payments failed. Cards expired. Customers paused. All within the first billing cycle.

PLANNED: When a charge fails, the system retries.
ACTUAL: The retry loop had no idempotency check. Several customers were charged twice.

PLANNED: The founder knows who's subscribed.
ACTUAL: There was no way to see which subscriptions were in good standing.

This was StyleCrate, a curated fashion subscription box from Arnhem founder Iris Bakker, part of the city's ArtEZ-adjacent creative scene. She built it in Cursor. Sign-ups, preference quizzes and box customization all worked beautifully, and her first 60 waitlist signups became paying subscribers within two weeks.

The happy path was perfect. Billing doesn't live on the happy path.

What LaunchStudio rebuilt (8 business days, €1,400):
→ Billing logic driven by Stripe's subscription lifecycle events
→ Idempotency keys, so a retry can never charge twice
→ A simple internal dashboard showing subscription status at a glance

The next three billing cycles: zero duplicate charges. Today: 180+ active subscribers.

"Cursor built me a subscription flow that looked complete. It had never seen what happens when a real customer's card expires mid-cycle." - Iris Bakker

Running subscriptions on AI-generated code? Test the unhappy path: https://launchstudio.eu/en/blog/ai-software-development-arnhem

#AINativeFounder #LaunchStudio #Manifera #StripeBilling #Arnhem
