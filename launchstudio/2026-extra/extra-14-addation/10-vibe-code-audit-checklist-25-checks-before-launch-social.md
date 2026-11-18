✅✅✅✅✅ ❌✅✅✅❌ ✅✅❌✅✅ ✅✅✅✅✅ ✅✅❌✅✅

That was Koen Dijkhuizen's first run through a 25-point pre-launch checklist. Four red marks. One week to launch. 📋

Koen, a freelance bookkeeper in Tilburg, built Betaalseintje with Lovable: small businesses send polite, escalating payment reminders and track who has paid. 25 businesses were on the waiting list, and sign-ups would open on the first of the month. The app felt finished. He almost skipped the checklist.

The accounts section: passed easily. Then:

❌ CHECK 6: Change the invoice number in the URL. Other businesses' invoices opened, with their customers' names and amounts.
❌ CHECK 10: A Postmark server token in the page source.
❌ CHECK 13: Accounts only upgraded when the success page loaded.
❌ CHECK 23: A backup had never been restored.

Koen sent his results to LaunchStudio (6 business days, €1,600):
✓ RLS policies tied to business membership
✓ The Postmark token and reminder sending moved into an edge function
✓ Plan upgrades switched to a verified Stripe webhook
✓ A restore test, with Koen watching

SECOND RUN
Score: 24 out of 25. The only open item, check 3, was waiting for his business partner to set up access.

Betaalseintje opened on schedule. First quarter: 61 businesses, around 3,800 reminders sent. And check 6 is now part of Koen's routine after every new feature.

"I almost didn't do the checklist because the app felt finished. One URL change showed me it wasn't." - Koen Dijkhuizen

Run the 25 checks yourself: https://launchstudio.eu/en/blog/vibe-code-audit-checklist-25-checks-before-launch

#VibeCoding #Lovable #LaunchChecklist #AIFounder #LaunchStudio #Manifera
