.

.

.

That's roughly what new clients saw after logging in. A white screen. ⬜

Thijs Hendriks built Dossierdesk with Lovable and Supabase: a portal where clients of a small immigration law firm upload documents, follow their application status and message their lawyer. Around 220 clients used it, and the firm promoted it on its website as a reason to choose them.

Then new clients started calling. Existing clients were fine. Thijs couldn't reproduce it with his own account. Until one new client shared a screenshot of the console:

Cannot read properties of null (reading 'case_number')

New clients had no case record until a lawyer created one. The dashboard assumed there was always a case.

Two more white screens turned up:
• Reloading any page except the homepage on the live host returned a 404
• After each deploy, clients with the portal open got a blank page when they navigated, because the old JavaScript chunks were gone

Filling in the white (LaunchStudio, 5 business days, €1,900):
✓ Empty states: new clients now see a welcome page explaining that their lawyer will open their case shortly
✓ Every data-driven component handles missing records
✓ A rewrite rule, so sub-pages reload properly
✓ One automatic reload when a chunk fails to load
✓ A top-level error boundary plus section boundaries, showing a friendly message instead of nothing
✓ Sentry reporting errors with page and browser, which caught two more crashes in the first week, on an older iPad and in an in-app browser

No blank-screen reports since. Support calls about the portal went from several a week to almost none, and new clients now finish their document uploads in their first session.

"For weeks I thought it was random. It was one missing check, and the console told us exactly where." - Thijs Hendriks

https://launchstudio.eu/en/blog/why-does-my-app-show-a-blank-white-screen

#React #Lovable #ErrorMonitoring #LegalTech #AIFounder #LaunchStudio #Manifera
