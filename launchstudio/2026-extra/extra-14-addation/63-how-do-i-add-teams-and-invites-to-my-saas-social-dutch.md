🚨 Rianne Mulders bouwde Uurwerk in Lovable: urenregistratie en facturatie voor freelance ontwerpers. Het groeide naar 600 gebruikers - toen begonnen kleine ontwerpbureaus te vragen om teamaccounts met gedeelde klanten, gedeelde projecten en één factuur. Ze promptte "voeg teams toe". Dat leverde een tabel voor teams op, teamleden zagen gedeelde projecten nog steeds niet, en één poging maakte elk project zichtbaar voor iedereen. 😳

Teams klonk als één functie. Het bleek een nieuw fundament onder elke functie die ze al had. Dit is waarom prompten niet werkte:

❌ Een tabel voor teams toegevoegd, maar elke policy nog op basis van user_id
❌ Geen lidmaatschappen of rollen, dus geen manier om te bepalen wie wat mocht zien
❌ Geen veilige uitnodigingsflow
❌ Facturering in Stripe nog gekoppeld aan individuele gebruikers

✅ Organisaties, lidmaatschappen en uitnodigingen ontworpen als één wijziging
✅ organisation_id toegevoegd aan klanten, projecten, urenregels en facturen, met elke policy herschreven rond lidmaatschap
✅ Een uitnodigingsflow met verlopende tokens en limieten op plaatsen, en klanten in Stripe verplaatst naar organisaties met prijzen per plaats
✅ Alle 600 bestaande gebruikers in één weekend gemigreerd naar persoonlijke organisaties

Bij **LaunchStudio**, ondersteund door Manifera's 120+ engineers en 11+ jaar multi-tenant B2B-systemen, bouwen we teams als het fundament dat ze zijn - geen lappendeken van prompts. 🛠️

💡 Het resultaat: €4.700, dertien werkdagen. Bestaande freelancers merkten alleen een nieuwe knop "Team uitnodigen", 34 bureaus namen binnen drie maanden een teamabonnement, en de gemiddelde omzet per account verdubbelde ongeveer. 🚀

👉 Maakt u van uw AI-gebouwde tool een B2B-SaaS? Zo voegt u teams en uitnodigingen goed toe: https://launchstudio.eu/nl/blog/how-do-i-add-teams-and-invites-to-my-saas

#SaaS #B2B #Supabase #Lovable #LaunchStudio #Manifera
