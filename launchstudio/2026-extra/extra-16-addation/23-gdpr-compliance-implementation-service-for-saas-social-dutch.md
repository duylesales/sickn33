🗂️ Eline Mertens heeft een HR-adviesbureau in Den Bosch en bouwde Verlofwijs met Claude Code en Supabase: kleine werkgevers beheren er verlof, ziektedagen en personeelsdocumenten mee. Haar eerste zakelijke klant, met 80 medewerkers, vroeg om een verwerkersovereenkomst, een lijst met subverwerkers en bewijs dat gegevens van medewerkers konden worden verwijderd. Ze kon het niet met zekerheid beantwoorden. 😟

De gegevensinventaris vond persoonsgegevens op zeven plekken: 🧠

❌ Contracten en ziekmeldingen in een openbare storagebucket
❌ Medische notities in request bodies bij foutregistratie, en namen van medewerkers in URL's van analytics
❌ De database gehost buiten de EU, en verwijderen haalde alleen de login weg
❌ Elke beheerder kon elke medewerker bij alle bedrijven zien

✅ Database en opslag naar een EU-regio, opslag privé gemaakt met signed links
✅ Toegang op basis van bedrijf en rol afgedwongen in Row Level Security
✅ Gegevens geminimaliseerd: geen request bodies in logs, ID's in URL's, alleen verlofdata naar de AI-provider
✅ Functies voor verwijderen en bewaartermijnen plus documentatie voor de verwerkersovereenkomst

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software voor Europese klanten zoals Vodafone en TNO, implementeren we de technische kant van de AVG, zodat uw app doet wat uw privacydocumenten beloven. 🛠️

💡 Het resultaat: €3.200, negen werkdagen. De klant tekende binnen twee weken, en twee andere werkgevers gebruikten dezelfde documenten zonder verdere vragen. 🚀

👉 AVG-implementatieservice voor SaaS: https://launchstudio.eu/nl/blog/gdpr-compliance-implementation-service-for-saas

#AVG #Privacy #SaaS #ClaudeCode #AIFounder #LaunchStudio #Manifera
