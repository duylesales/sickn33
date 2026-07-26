🎙️ Milan Verhagen, een oprichter in Zwolle, bouwde KlantStroom — een CRM-tool voor kleine verkoopteams — met Cursor. Pull request na pull request zag er op het eerste gezicht netjes uit. Elke handmatige test die hij uitvoerde, slaagde probleemloos. 😳

Een netjes ogende app en een veilige app zijn niet hetzelfde. 🧠

❌ Een webhook kon twee keer afgaan voor dezelfde gebeurtenis en een duplicaatklantrecord aanmaken
❌ Geen unieke constraint hield dit tegen, en er bestond geen idempotentiecontrole op de binnenkomende gebeurtenis
❌ Het kwam nooit naar voren in tests, omdat niemand precies de timing testte die het triggert
❌ Onopgemerkt was het een kwestie van tijd voordat duplicaatrecords rapportages en facturering zouden corrumperen

✅ Een idempotentiesleutelcontrole toegevoegd aan de webhook-handler
✅ Een unieke constraint toegevoegd aan de klanttabel om duplicaten volledig te voorkomen
✅ Het handjevol duplicaatrecords opgeruimd dat zich al stilletjes had opgehoopt

Bij **LaunchStudio** brengt Manifera meer dan 11 jaar productie-engineeringervaring naar precies dit soort beoordeling, dagelijks uitgevoerd door onze Amsterdamse engineers bij Lovable-, Bolt-, Cursor- en v0-projecten. 🛡️

Zijn resultaat: KlantStroom verwerkt nu opnieuw geleverde webhooks veilig, waarbij het aanmaken van duplicaten structureel onmogelijk is in plaats van slechts onwaarschijnlijk. 🚀

👉 Zeker dat uw vibe-coded app productieklaar is omdat het elke test doorstond die u bedacht: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #VibeCoding #ProductionReady
