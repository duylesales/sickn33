"How many outside services touch your users' data?"

Manon Duyvesteyn wrote down four. The real answer was eleven. 🔢

Roll call for Tolkplanner, her Lovable app for interpreter booking: 24 agencies, around 1,100 interpreters.

1. Hosting ✓ (on her list)
2. Database ✓ (on her list)
3. Email ✓ (on her list)
4. Payments ✓ (on her list)
5. Error tracking, receiving full request bodies with interpreter names and assignment details
6. A support chat widget on the logged-in app, with access to the page ⚠️ no processing agreement
7. Analytics, capturing URLs that held assignment identifiers ⚠️ no processing agreement
8. A model API, added six months earlier, summarising full assignment briefs ⚠️ no processing agreement on that tier
9. A font service, contacted on every page load, receiving visitors' IP addresses ⚠️ no processing agreement
10. An SMS provider for interpreter notifications, set up once and genuinely forgotten
11. A document signing service, holding signed contracts with interpreters' personal details

A customer's privacy officer had asked for the list before renewing.

The cleanup (LaunchStudio, 4 business days, €2,800):
✓ The inventory built from code, environment variables and network traffic, recording what each service receives
✓ #9 removed, with fonts self-hosted
✓ #7 replaced by a cookie-free tool that receives no identifiers, and identifiers taken out of URLs
✓ #5 set to scrub request bodies
✓ #8 moved to a tier with processing terms and an EU region, receiving only the brief text, not the whole assignment record
✓ #6 removed from logged-in pages and replaced with a support link
✓ Agreements located and filed for the rest
✓ A published subprocessor page with locations and a last-updated date
✓ A rule before any new service: agreement, location check, list update, 30 days' notice to customers

The renewal went ahead, and the privacy officer specifically mentioned the published page. Manon now sends the link with every proposal. Two of the eleven no longer exist in her product at all.

"I would have sworn there were four. The one that bothered me most was the font - every visitor's IP address going to a company I had never thought about, because a generated stylesheet imported it." - Manon Duyvesteyn

https://launchstudio.eu/en/blog/subprocessors-listing-every-service-your-app-touches

#GDPR #Subprocessors #Privacy #Lovable #LaunchStudio #Manifera
