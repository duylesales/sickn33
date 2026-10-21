🚨 Huurbeheer van Annelies Vos verzorgt de huuradministratie voor 31 woonorganisaties — zo'n 9.500 huurwoningen. Een nieuwe vastgoedbeheerder importeerde zijn huurders uit een Nederlandse Excel-export. De import meldde dat het gelukt was. De volgende incassorun inde bij 214 huurders € 1,25 huur. 😳

De parser had "1.250,00" gelezen als 1,25. Dezelfde klant had het bestand ook twee keer opnieuw geïmporteerd, wat 380 dubbele huurders opleverde — en elk telefoonnummer was zijn voorloopnul kwijt. Zo bouwt u CSV-imports die uw data niet beschadigen:

❌ Rijen direct in productie geschreven, alleen getest met een zelfgemaakt kommagescheiden bestand
❌ Nederlandse bedragen en datums gelezen met Engelse aannames
❌ Geen voorbeeldweergave, dus niemand zag "huur: € 1,25" voordat het werd afgeschreven
❌ Geen ontdubbeling en geen manier om een import terug te draaien

✅ Inlezen van XLSX en CSV met herkenning van scheidingsteken en codering, plus expliciete Nederlandse notaties voor getallen en datums
✅ Een gefaseerde pijplijn: valideren in een tussentabel, geïnterpreteerde waarden tonen, foutenbestand downloaden, vastleggen in één transactie
✅ Upsert op het huurdernummer van het bronsysteem, batch-ID's op elke rij en zeven dagen terugdraaien
✅ Verwerking op de achtergrond, organisatie bepaald door de batch, bescherming tegen formule-injectie en 14 lastige testbestanden in CI

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, repareren we imports wanneer onboarding het product tegenhoudt. ⚙️

💡 Het resultaat: € 3.600, drie werkdagen. De 214 huurders werden de week erna correct geïncasseerd en de duplicaten samengevoegd. Het kwartaal daarna importeerden elf organisaties — en de voorbeeldweergave ving in vier bestanden problemen op voordat er iets werd weggeschreven. 🚀

👉 Lovable Supabase: CSV-imports die uw data niet beschadigen: https://launchstudio.eu/nl/blog/lovable-supabase-csv-imports-that-do-not-corrupt-your-data

#Supabase #Datakwaliteit #SaaS #Onboarding #LaunchStudio #Manifera
