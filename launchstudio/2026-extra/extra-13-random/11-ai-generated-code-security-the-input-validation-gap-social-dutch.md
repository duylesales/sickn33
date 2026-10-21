🚨 Mehmet Kaya, voormalig marktonderzoeksanalist in Tilburg, bouwde Formlab met Cursor: een enquêtetool voor kleine onderzoeksbureaus. Acht bureaus betaalden ervoor toen het IT-team van een klant vóór interne goedkeuring een routinematige beveiligingscontrole deed. Binnen een uur waren er twee problemen gevonden. 😳

Een respondent kon een antwoord met een scripttag insturen — en omdat het dashboard antwoorden als ruwe HTML toonde, draaide het in de browser van elke bureaumedewerker. En elk lid van een werkruimte kon zich tot eigenaar maken door "role": "owner" aan een verzoek toe te voegen. Dit is de kloof in invoervalidatie bij AI-gegenereerde code:

❌ Verzorgde validatie in de browser, geen enkele op de server
❌ API-handlers die opsloegen wat er ook maar in het verzoek stond (mass assignment)
❌ dangerouslySetInnerHTML gebruikt om de opmaak van antwoorden te behouden (opgeslagen XSS)
❌ Niets dat een toekomstige bewerking door Cursor tegenhield een fix te verwijderen

✅ Strikte Zod-schema's op alle 34 API-routes, gedeeld met de frontend
✅ Ruwe HTML vervangen door een opgeschoonde Markdown-renderer met alleen basisopmaak
✅ Een Content Security Policy die inline scripts blokkeert als vangnet
✅ Een weigeringstest per route in CI — en opgeslagen antwoorden gescand en opgeschoond

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, behandelen we validatie als systeem op elke servergrens, niet als losse pleister per formulier. ⚙️

💡 Het resultaat: € 1.350, vijf werkdagen. Formlab doorstond twee weken later de vervolgcontrole van de klant — en drie zusterbedrijven namen een abonnement. De CI-tests hebben sindsdien twee terugvallen door AI-bewerkingen opgevangen. 🚀

👉 Beveiliging van AI-gegenereerde code: de kloof in invoervalidatie uitgelegd: https://launchstudio.eu/nl/blog/ai-generated-code-security-the-input-validation-gap

#AppSecurity #Cursor #TypeScript #OWASP #LaunchStudio #Manifera
