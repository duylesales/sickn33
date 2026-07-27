🔓 Sanne Bruggeman bouwde Kenniswijzer, een marktplaats voor peer-tutoring voor studenten in Enschede, in een sprint van twee weken met Lovable. Strakke UI, werkende boekingsflow, Stripe-checkout — een oprecht indrukwekkende demo. Toen ontdekte de lanceringscontrole van LaunchStudio dat de Supabase-database geen enkele row-level security had: elke ingelogde gebruiker kon de boekingsgeschiedenis, het telefoonnummer en de betalingsmetadata van elke andere gebruiker lezen, simpelweg door de browserconsole te bekijken.

Een gepolijste demo en een productieklare backend zijn niet hetzelfde. 🧠

❌ AI-tools zijn geoptimaliseerd voor "het werkt als ik het test", niet voor "het overleeft iemand die niet de oprichter is"
❌ Supabase-tabellen werden geleverd met open lees-/schrijfrechten die niemand had gecontroleerd
❌ Elke geauthenticeerde gebruiker kon de privégegevens van een andere student opvragen
❌ De kloof was onzichtbaar totdat iemand het netwerktabblad van de browser opende

✅ De autorisatielaag herbouwd met RLS-beleid beperkt tot de eigen gegevens van elke gebruiker
✅ Serverzijdige validatie toegevoegd aan elke schrijfbewerking
✅ Rate limiting ingesteld op publieke API-routes vóór de campusbrede lancering

Bij **LaunchStudio** passen de 120+ technici van Manifera dezelfde beoordelingschecklist toe op een prototype uit Enschede als op een zakelijke codebase voor klanten zoals Vodafone en TNO. 🛡️

Kenniswijzer werd in de eerste week gelanceerd voor 400 studenten van de Universiteit Twente zonder enig incident van gegevensblootstelling — en Sanne hoefde geen enkele regel van haar UI aan te passen. 🚀

👉 Bouwt u in Enschede? Laat uw lanceringsgereedheid controleren vóór dag één: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #Enschede #ProductionReady
