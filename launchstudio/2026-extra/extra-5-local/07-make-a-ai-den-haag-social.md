⏱️ 10 minutes.

That's how long it took a legal consultancy's IT team to find out PolicyPilot wasn't ready.

Nina de Groot, a former policy analyst, built PolicyPilot in Cursor. It's a document review tool that helps NGOs and legal consultancies track regulatory changes and flag compliance risks in contracts. Two consultancies near the city center piloted it.

Then one of them ran its standard vendor check. If you sell to Den Haag's institutions, this is roughly the exam:

☐ Do API endpoints require authentication?
→ ❌ Several didn't. The right URL pattern returned data without a login.
☐ Is there rate limiting?
→ ❌ None.
☐ Are client documents encrypted at rest?
→ ❌ No, in a tool built for confidential legal material.
☐ Does the API reject malformed input?
☐ Is there a written data retention and deletion policy?

Those last two are the questions an institutional buyer usually asks next. Have your answers ready.

The fix: authentication middleware on every API route, rate limiting, and document storage encrypted at rest.

The outcome: the same IT team that flagged the gaps signed off on PolicyPilot for full deployment.

"I'd built something that looked ready for legal clients. It took their IT team about ten minutes to find out it wasn't." - Nina de Groot

In a city this networked, your first reference client opens the door to the next one. Worth passing the exam first.

👉 Making an AI product for institutional clients? Get your backend reviewed first: https://launchstudio.eu/en/blog/make-a-ai-den-haag

#AINativeFounder #LaunchStudio #Manifera #MakeAnAIProduct #DenHaag
