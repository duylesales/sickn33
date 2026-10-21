🚨 Werkbonapp van Joost Verhagen regelt digitale werkbonnen voor 48 installatiebedrijven — zo'n 600 monteurs. Teamondersteuning was in Lovable toegevoegd met een uitnodigingsknop en één kolom organisation_id per profiel. Toen zag een installateur dat werkbonnen werden bekeken door een monteur die ze vier maanden eerder hadden verwijderd. 😳

"Verwijderen" haalde iemand alleen uit de teamlijst. De toegang via de API bleef intact — en de uitnodigingslinks verliepen nooit. Zo bouwt u teamuitnodigingen en lidmaatschappen die echt standhouden:

❌ Eén organisation_id per profiel, dus een onderaannemer kon niet bij twee installateurs horen
❌ Uitnodigingslinks met het organisatie-ID erin, zonder vervaldatum, bruikbaar voor iedereen
❌ Verwijderen dat een vlag zette in plaats van toegang in te trekken of sessies te beëindigen
❌ Geen auditlog van wie wie uitnodigde, wijzigde of verwijderde

✅ Aparte tabellen voor lidmaatschappen en uitnodigingen; alle 600 profielen overgezet
✅ Row level security herschreven over 17 tabellen rond één lidmaatschapsfunctie, gecontroleerd met tests tussen organisaties
✅ Willekeurige, gehashte uitnodigingstokens: 7 dagen geldig, eenmalig, gekoppeld aan het uitgenodigde e-mailadres
✅ Verwijderen dat het lidmaatschap wist, sessies uitlogt en tokens intrekt — plus een bewaking van de laatste eigenaar en een auditlog

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we dit wanneer een product voor één gebruiker zijn eerste teamklant krijgt. ⚙️

💡 Het resultaat: € 3.400, drie werkdagen. Bij het overzetten bleken 37 vertrokken monteurs bij 11 bedrijven nog toegang te hebben — vier hadden die gebruikt. Alles op dag één ingetrokken, en twee installateurs stapten over op een groter abonnement omdat onderaannemers toevoegen eindelijk werkte. 🚀

👉 Lovable Supabase: teamuitnodigingen en lidmaatschap van organisaties: https://launchstudio.eu/nl/blog/lovable-supabase-team-invitations-and-organisation-membership

#Supabase #Lovable #SaaS #AppSecurity #LaunchStudio #Manifera
