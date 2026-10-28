🚨 Hugo Verbeek was elf jaar beleidsadviseur voordat hij in Den Haag BuurtSignaal oprichtte: bewoners melden kapotte straatverlichting, illegale dumpingen en onveilige oversteekplaatsen, en gemeentelijke teams beoordelen en reageren. Gebouwd in Windsurf, als pilot in één stadsdeel - bewoners waren enthousiast, medewerkers nog meer. Toen stuurde inkoop een vragenlijst over beveiliging en privacy met 90 vragen. Hugo kon er ongeveer een derde beantwoorden. 😳

Medewerkers hadden alleen de rollen "gebruiker" en "beheerder", met beperkingen alleen in de interface. Geen auditlog. Inloggen met wachtwoorden in plaats van via de identiteitsprovider van de gemeente. Foto's van bewoners met locatiegegevens voor altijd bewaard, hosting in de VS en toetsenbordvallen in het meldformulier. Dit houdt AI-code naar productie brengen voor publieke inkopers werkelijk in:

❌ Twee rollen, deels afgedwongen in de interface
❌ Geen registratie van wie data van bewoners inzag of wijzigde
❌ Wachtwoorden in plaats van SSO van de gemeente
❌ Onbeperkte bewaring, hosting in de VS en ontoegankelijke formulieren

✅ Vier medewerkersrollen afgedwongen in de database, plus een append-only auditlog
✅ SSO via de OpenID Connect-provider van de gemeente, met MFA voor beheerders
✅ Locatiemetadata uit foto's verwijderd, afgesproken bewaartermijnen, EU-hosting met geteste back-ups
✅ Toegankelijkheidsverbeteringen en een aan de BIO gekoppeld beveiligingsoverzicht, lijst met verwerkers, herstelbeschrijving, incidentprocedure en exitplan

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering - inclusief werk voor TNO - versterken we eerst, zodat de penetratietest het werk bevestigt in plaats van de basis te catalogiseren. ⚙️

💡 Het resultaat: € 6.900, eenentwintig werkdagen. De onafhankelijke pentest vond twee bevindingen met een laag risico, nog dezelfde week opgelost. BuurtSignaal tekende een driejarig contract, en twee buurgemeenten draaiden sindsdien een pilot met dezelfde documentatie. 🚀

👉 Van AI-code naar productie in Den Haag: GovTech-startups en publieke inkopers: https://launchstudio.eu/nl/blog/ai-code-to-production-in-the-hague-govtech-and-public-sector-buyers

#GovTech #DenHaag #BIO #Toegankelijkheid #LaunchStudio #Manifera
