🇪🇺 Rivals under one roof: an NGO and a trade association, on the same platform

THE PLATFORM
Camille Lenaerts spent eight years at a Brussels-based environmental NGO, then built Dossierwatch with Cursor: organisations follow legislative files, get AI-generated summaries of new amendments in English and French, map stakeholder positions, and share internal notes. Twenty-two NGOs and three trade associations subscribed.

THE QUESTION
During onboarding, a trade association's IT lead asked: could other subscribers, including NGOs campaigning against us, see our stakeholder notes?

THE HONEST ANSWER
It depended on the page.

WHAT EACH SIDE COULD ACTUALLY SEE
🔓 The interface filtered by organisation, but a search endpoint returned matching notes from every organisation
🔓 Private notes were sent to an AI model to "improve summaries," without clients knowing

AND WHAT ELSE WAS WRONG
• Summaries weren't linked to the amendment versions they described, and one misattributed an amendment after a document was updated
• French accented terms didn't show up in search
• During the last plenary week, the site slowed to a crawl, because summaries were generated on page load

Clients who disagree for a living all needed to agree on one thing: the platform keeps their notes apart.

What LaunchStudio built (Launch & Grow, 12 business days, €3,700, plus €49/month):
✓ Organisation-level separation with Row Level Security and negative tests
✓ Private notes sent to the model only if an organisation opts in
✓ Every summary linked to its source document versions, regenerated when sources change, with AI labels and a review status
✓ Accent-insensitive, multilingual search
✓ Summary generation and ingestion moved to monitored background jobs, with public dossier pages cached
✓ A procurement-ready security and data description, with the AI provider listed as a processor

The trade association signed. The next plenary week passed with fast load times throughout. And Dossierwatch has added eleven organisations since, several of them citing the data description in procurement.

"My clients disagree with each other for a living. The one thing they all needed to agree on was that the platform kept their notes apart." - Camille Lenaerts

https://launchstudio.eu/en/blog/ai-prototype-to-production-in-brussels-eu-policy-startups-and-multilingual-data

#Brussels #PolicyTech #EUAffairs #Multilingual #LaunchStudio #Manifera
