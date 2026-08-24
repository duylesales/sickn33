---
Titel: "5 Vragen die U Moet Stellen Voordat U Iemand Inhuurt om uw AI-App te Repareren"
Keywords: AI-app beveiliging, developer inhuren AI-app, Row Level Security audit, vaste prijs development, AI-gegenereerde codebase, LaunchStudio, Manifera, Lovable, Supabase beveiliging
Buyer Stage: Decision
---

# 5 Vragen die U Moet Stellen Voordat U Iemand Inhuurt om uw AI-App te Repareren

U heeft een werkend prototype gebouwd met Lovable, Bolt, Cursor of een vergelijkbare AI-builder, en nu heeft u iemand nodig om het productieklaar te maken — veilig, betrouwbaar, klaar voor echte gebruikers en echt geld. Het probleem is dat "iemand die een door AI gebouwde app kan repareren" bijna van de ene op de andere dag een overvolle, inconsistente markt is geworden, en de meeste oprichters hebben geen betrouwbare manier om een oprecht gekwalificeerde partner te onderscheiden van een freelancer die het maar wat probeert. Dit is geen algemeen "hoe huur ik een developer in"-artikel. Het is een specifieke interviewchecklist voor precies deze wervingsbeslissing, opgebouwd rond vijf vragen die het verschil blootleggen tussen een bureau dat door AI gegenereerde codebases echt begrijpt en een bureau dat maar wat gokt. Stel alle vijf de vragen aan elke kandidaat, voordat u iets ondertekent.

## Vraag 1: "Gaat u binnen mijn bestaande codebase werken, of wilt u deze opnieuw bouwen?"

Dit is de meest onthullende vraag die u kunt stellen, en die moet als eerste komen. Het eerlijke, deskundige antwoord is een variant van: "We werken binnen wat u al heeft. Een werkende frontend vanaf nul herschrijven verspilt de weken aan prompting en ontwerpbeslissingen die u al heeft gemaakt, en het introduceert nieuwe bugs in code die op dit moment werkt."

Een slecht antwoord klinkt als enthousiasme voor een frisse start — "eerlijk gezegd wordt het schoner als we de frontend gewoon goed opnieuw bouwen" — maar het is eigenlijk een rode vlag. Opnieuw bouwen is trager, duurder, en het gooit precies datgene weg wat een AI-builder de moeite waard maakte om te gebruiken: snelheid. Een team dat standaard kiest voor opnieuw bouwen, weet ofwel niet hoe het moet werken binnen andermans gegenereerde code, of heeft een financiële prikkel om u een groter project te verkopen dan u nodig heeft. De enige keer dat een gedeeltelijke rebuild legitiem is, is wanneer een specifiek onderdeel van de codebase daadwerkelijk onbruikbaar is — en een goed team benoemt dat onderdeel specifiek, in plaats van vaag naar "het geheel" te wijzen.

## Vraag 2: "Hoe precies gaat u om met Row Level Security, en wie kan de data van mijn gebruikers zien tijdens het proces?"

Row Level Security is het meest voorkomende gat in door AI gegenereerde Supabase- en Postgres-backends — schema's die op papier veilig lijken maar nooit daadwerkelijk zijn ingeschakeld of gekoppeld aan `auth.uid()`. Iedereen die beweert uw app te kunnen repareren, heeft hier een concreet, specifiek antwoord nodig, geen vage geruststelling.

Een goed antwoord noemt de daadwerkelijke mechanica: "We auditen elke tabel op bestaand RLS-beleid, bevestigen dat elk beleid is ingeschakeld en gekoppeld is aan de geauthenticeerde gebruiker in plaats van alleen aanwezig te zijn in het schema, en testen cross-account toegang rechtstreeks vóór en na de fix — niet alleen de code beoordelen, maar zelf daadwerkelijk proberen in te breken." Het moet ook het proces behandelen: wie in hun team heeft tijdens het traject toegang tot uw productiedatabase, gebruiken ze tijdgebonden inloggegevens, en wordt uw live gebruikersdata ooit geëxporteerd of ergens buiten uw eigen infrastructuur gekopieerd.

Een slecht antwoord is iets als "maakt u zich geen zorgen, wij zorgen voor de beveiliging" zonder specifieke details, of erger nog, een team dat RLS helemaal niet ongevraagd ter sprake brengt. Als een ontwikkelpartner Row Level Security niet binnen de eerste vijf minuten van een scopinggesprek kan uitleggen, hebben ze niet genoeg door AI gegenereerde apps gerepareerd om uw app aan toe te vertrouwen.

## Vraag 3: "Is dit een vaste prijs met vaste scope, of open-einde uurtarief?"

Het verharden van een bestaande app — beveiliging, betalingen, monitoring, infrastructuur — is afgebakend, begrensd werk. Een team dat dit al eerder heeft gedaan, kan u, na beoordeling van uw codebase, ruwweg vertellen wat er gerepareerd moet worden en wat het kost om het te repareren. Dat betekent dat prijzen met een vaste prijs en vaste scope haalbaar zijn en de standaardverwachting zouden moeten zijn.

Open-einde facturatie op uurbasis zonder afgebakende schatting is om twee redenen een waarschuwingssignaal. Ten eerste betekent het meestal dat het team uw codebase niet grondig genoeg heeft beoordeeld om te weten waar ze mee te maken hebben — ze prijzen hun eigen onzekerheid, niet uw project. Ten tweede ontneemt het u de mogelijkheid om het budget te beheersen: een eenvoudige RLS- en webhook-fix kan ongemerkt uitgroeien tot weken aan gefactureerde uren zonder natuurlijk eindpunt. Een goed antwoord klinkt als: "Zodra we uw repository hebben beoordeeld, geven we u een vaste prijs en een specifieke lijst van wat inbegrepen is — als we tijdens het traject iets buiten die scope tegenkomen, melden we dat en offreren we het apart voordat we het werk uitvoeren, in plaats van het achteraf te factureren."

## Vraag 4: "Wat gebeurt er met mijn code, hostingaccounts en inloggegevens als het traject eindigt?"

Deze vraag wordt gemakkelijk vergeten in de opwinding van het vinden van iemand die uw app kan repareren, maar het is enorm belangrijk. Wie is aan het einde ondubbelzinnig eigenaar van de code — u, of behoudt het bureau bepaalde rechten of toegang? Krijgen zij tijdelijke, afgebakende toegang tot uw Supabase-project, Stripe-account en hostingprovider, of dringen ze erop aan om alles te migreren naar hun eigen infrastructuur waar u geen volledige controle over heeft? Wat is het proces voor het intrekken van hun toegang en het roteren van eventuele inloggegevens waar ze bij konden, zodra het werk klaar is?

Een goed antwoord is eenduidig: u behoudt gedurende het hele traject volledig eigendom van uw codebase en alle accounts, toegang is afgebakend en tijdgebonden, en inloggegevens worden als standaard laatste stap geroteerd zodra het traject is afgerond — geen zaak waar u zelf om moet vragen. Een slecht antwoord is vaagheid over eigendom, aandringen op het migreren van uw infrastructuur naar accounts die zij beheren, of helemaal geen vermelding van een stap voor het roteren van inloggegevens. Als een partner niet duidelijk kan antwoorden op "wat gebeurt er als we stoppen met samenwerken", moet u niet met ze beginnen.

## Vraag 5: "Kunt u mij een specifiek eerder voorbeeld laten zien van het repareren van een door AI gegenereerde codebase — niet alleen een algemeen portfolio?"

Een algemeen portfolio van eerder klantwerk vertelt u dat een team software kan bouwen. Het vertelt u niet dat ze de specifieke faalpatronen van door AI gegenereerde code begrijpen: RLS aanwezig in het schema maar nooit ingeschakeld, Stripe-integraties die uitsluitend client-side zijn zonder server-side webhook die de betaling bevestigt, API-sleutels die blootgesteld in frontend-JavaScript staan, ontbrekende connection pooling die pas zichtbaar wordt onder echte gelijktijdige belasting.

Vraag specifiek: "Neem me mee door een echt voorbeeld waarin u een bestaande Lovable-, Bolt- of Cursor-app heeft verhard — wat vond u, wat heeft u gerepareerd, en wat was het resultaat?" Een team dat dit werk daadwerkelijk heeft gedaan, antwoordt specifiek: de tool die de oprichter gebruikte, de exacte kwetsbaarheidsklasse die ze vonden, de fix die ze doorvoerden, en een meetbaar resultaat van voor en na. Een team dat antwoordt met algemeenheden — "we hebben al eerder met startups gewerkt" — zonder de AI-builder, het specifieke gat of een concreet resultaat te noemen, heeft dit specifieke soort werk waarschijnlijk niet vaak genoeg gedaan om uw eerste keuze te zijn.

## Hoe LaunchStudio Scoort op Deze Vijf Vragen

Leg LaunchStudio langs precies deze checklist. Bij vraag één: het hele model is opgebouwd rond werken binnen uw bestaande AI-builder-frontend — Lovable, Bolt, Cursor of vergelijkbaar — zonder rebuild, waarbij de backend eronder in 1 tot 3 weken wordt verhard. Bij vraag twee: RLS-audit en handhaving gekoppeld aan `auth.uid()` is een standaard, met naam genoemd onderdeel van elk traject, geen bijzaak. Bij vraag drie: de pakketten van LaunchStudio zijn vaste prijs en vaste scope, van Launch Ready tot Enterprise Hardening, zodat u de kosten kent voordat het werk begint. Bij vraag vier: u behoudt volledig eigendom van uw code en accounts, met afgebakende, tijdgebonden toegang tijdens het traject. Bij vraag vijf: dit artikel zelf, en de casestudy hieronder, zijn precies het soort specifieke, met naam genoemde voorbeeld dat deze vraag beoogt naar boven te halen — geen algemene portfolioclaim.

## Belangrijkste inzichten

- Vraag of een kandidaat binnen uw bestaande codebase gaat werken of deze opnieuw wil bouwen — standaard kiezen voor rebuild wijst vaak op onbekendheid met door AI gegenereerde code, niet op echte technische noodzaak.

- Eis specifieke details over Row Level Security: wie krijgt toegang tot uw productiedata tijdens de fix, en hoe verifiëren ze dat RLS daadwerkelijk is ingeschakeld en gekoppeld, niet alleen aanwezig in het schema.

- Vaste prijs met vaste scope zou de standaard moeten zijn voor dit soort afgebakend verhardingswerk; open-einde uurtarieven zonder afgebakende schatting betekenen meestal dat het team uw codebase niet grondig genoeg heeft beoordeeld.

- Verduidelijk vooraf eigendom en de omgang met inloggegevens — u zou gedurende het hele traject volledige controle over uw code en accounts moeten behouden, met toegang die wordt ingetrokken en inloggegevens die als standaard laatste stap worden geroteerd.

- Vraag om een specifiek eerder voorbeeld van het repareren van een door AI gegenereerde codebase, geen algemeen portfolio — de details van het antwoord (welke tool, welke kwetsbaarheid, welke fix, welk resultaat) vertellen u meer dan welke referentielijst dan ook.

## Klaar om LaunchStudio Deze Vijf Vragen Zelf te Stellen?

De beste manier om een partner te beoordelen, is deze vijf vragen rechtstreeks aan hen te stellen en te zien hoe specifiek de antwoorden zijn.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), ondersteund door meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio nemen senior engineeringteams uw bestaande, door AI gebouwde frontend en implementeren ze productieklare beveiliging, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige MVP, zonder rebuild, tegen een vaste prijs waar u vooraf mee instemt. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Platform voor Reisitinerarie-planning

Nadia Kowalski bouwde een SaaS-prototype voor reisitinerarie-planning met **Lovable**, ontworpen om onafhankelijke reizigers te helpen bij het opstellen van meerstedenreizen met door AI voorgestelde routes en activiteiten. Voordat ze zich vastlegde op een lancering, wilde ze de backend laten verharden — maar na het horrorverhaal van een bureau van een vriendin besloot ze drie kandidaten grondig te interviewen in plaats van de eerste de beste die op haar mail reageerde in te huren.

Nadia gebruikte precies de vijf bovenstaande vragen bij alle drie de kandidaten. Twee bureaus vielen snel af: beide wilden open-einde uurtarieven zonder vaste scope, en beide gaven vage, niet-specifieke antwoorden toen ze vroeg hoe ze met Row Level Security zouden omgaan — één zei simpelweg "we zorgen dat het veilig is" zonder `auth.uid()`, beleidskoppeling of enige verificatiestap te noemen. De derde kandidaat, LaunchStudio, gaf haar na beoordeling van haar repository een prijs met vaste scope en nam haar mee door een specifiek RLS-implementatieplan voor haar Supabase-database, nog voordat ze iets had ondertekend.

Engineers beveiligden haar Supabase-database met correct gekoppeld RLS-beleid, herstelden een blootgestelde Google Maps API-sleutel die in haar frontend-JavaScript stond, en voegden Stripe-webhookafhandeling toe voor haar premium itinerarie-niveau, zodat upgrades server-side werden bevestigd in plaats van te vertrouwen op een client-side redirect.

**Resultaat:** Nadia lanceerde haar premium tier naar haar eerste 300 wachtlijstgebruikers zonder beveiligingsincidenten en zonder facturatiegeschillen.

**Kosten & Doorlooptijd:** € 2.200 (Launch & Grow) — 8 werkdagen.

---

---

---
## Veelgestelde Vragen

### Waarom is vragen naar Row Level Security zo belangrijk bij het inhuren van iemand om mijn app te repareren?

Row Level Security is het meest voorkomende gat in door AI gegenereerde Supabase- en Postgres-backends — het is vaak aanwezig in het schema, maar nooit daadwerkelijk ingeschakeld of gekoppeld aan de geauthenticeerde gebruiker, wat betekent dat elk account technisch de data van een ander account zou kunnen lezen. Een partner die niet specifiek kan uitleggen hoe ze RLS-beleid gaan auditen, inschakelen en testen, heeft waarschijnlijk niet genoeg door AI gegenereerde apps gerepareerd om uw app aan toe te vertrouwen.

### Waarom moet ik voorzichtig zijn met een team dat mijn app opnieuw wil bouwen in plaats van repareren?

Opnieuw bouwen gooit de weken aan prompting en ontwerpbeslissingen weg die al in uw werkende frontend zijn verwerkt, introduceert nieuwe bugs in code die op dit moment functioneert, en is bijna altijd trager en duurder dan het verharden van de backend onder wat u al heeft. Standaard kiezen voor een rebuild wijst er meestal op dat een team niet zeker is van zichzelf bij het werken binnen andermans door AI gegenereerde code.

### Is een vaste prijs realistisch voor dit soort werk, of moet ik uurtarieven verwachten?

Prijzen met een vaste prijs en vaste scope zijn realistisch en zouden de standaardverwachting moeten zijn. Het verharden van een bestaande app voor beveiliging, betalingen en monitoring is afgebakend werk dat een ervaren team nauwkeurig kan inschatten na beoordeling van uw codebase. Open-einde uurtarieven zonder afgebakende schatting betekenen meestal dat het team uw project niet grondig genoeg heeft beoordeeld om het correct te kunnen prijzen.

### Wat moet er gebeuren met mijn code en inloggegevens nadat het traject is afgerond?

U zou gedurende het hele traject volledig eigenaar moeten blijven van uw codebase en alle accounts, elke toegang die aan de ontwikkelpartner wordt verleend, zou afgebakend en tijdgebonden moeten zijn, en inloggegevens zouden als standaard laatste stap geroteerd moeten worden zodra het werk is afgerond — geen zaak waar u zelf om moet vragen.

### Hoe scoort LaunchStudio op deze vijf vragen?

LaunchStudio werkt binnen uw bestaande AI-builder-frontend zonder rebuild, behandelt RLS-audit en -handhaving als een standaard, met naam genoemd onderdeel, biedt pakketten met vaste prijs en vaste scope, zorgt ervoor dat u volledig eigenaar blijft van code en accounts met tijdgebonden toegang tijdens het traject, en kan wijzen op specifieke, met naam genoemde casestudy's van het verharden van door AI gegenereerde codebases in plaats van een algemene portfolioclaim.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom is vragen naar Row Level Security zo belangrijk bij het inhuren van iemand om mijn app te repareren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Row Level Security is het meest voorkomende gat in door AI gegenereerde Supabase- en Postgres-backends — het is vaak aanwezig in het schema, maar nooit daadwerkelijk ingeschakeld of gekoppeld aan de geauthenticeerde gebruiker, wat betekent dat elk account technisch de data van een ander account zou kunnen lezen. Een partner die niet specifiek kan uitleggen hoe ze RLS-beleid gaan auditen, inschakelen en testen, heeft waarschijnlijk niet genoeg door AI gegenereerde apps gerepareerd om uw app aan toe te vertrouwen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom moet ik voorzichtig zijn met een team dat mijn app opnieuw wil bouwen in plaats van repareren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Opnieuw bouwen gooit de weken aan prompting en ontwerpbeslissingen weg die al in uw werkende frontend zijn verwerkt, introduceert nieuwe bugs in code die op dit moment functioneert, en is bijna altijd trager en duurder dan het verharden van de backend onder wat u al heeft. Standaard kiezen voor een rebuild wijst er meestal op dat een team niet zeker is van zichzelf bij het werken binnen andermans door AI gegenereerde code."
      }
    },
    {
      "@type": "Question",
      "name": "Is een vaste prijs realistisch voor dit soort werk, of moet ik uurtarieven verwachten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Prijzen met een vaste prijs en vaste scope zijn realistisch en zouden de standaardverwachting moeten zijn. Het verharden van een bestaande app voor beveiliging, betalingen en monitoring is afgebakend werk dat een ervaren team nauwkeurig kan inschatten na beoordeling van uw codebase. Open-einde uurtarieven zonder afgebakende schatting betekenen meestal dat het team uw project niet grondig genoeg heeft beoordeeld om het correct te kunnen prijzen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er gebeuren met mijn code en inloggegevens nadat het traject is afgerond?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U zou gedurende het hele traject volledig eigenaar moeten blijven van uw codebase en alle accounts, elke toegang die aan de ontwikkelpartner wordt verleend, zou afgebakend en tijdgebonden moeten zijn, en inloggegevens zouden als standaard laatste stap geroteerd moeten worden zodra het werk is afgerond — geen zaak waar u zelf om moet vragen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe scoort LaunchStudio op deze vijf vragen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio werkt binnen uw bestaande AI-builder-frontend zonder rebuild, behandelt RLS-audit en -handhaving als een standaard, met naam genoemd onderdeel, biedt pakketten met vaste prijs en vaste scope, zorgt ervoor dat u volledig eigenaar blijft van code en accounts met tijdgebonden toegang tijdens het traject, en kan wijzen op specifieke, met naam genoemde casestudy's van het verharden van door AI gegenereerde codebases in plaats van een algemene portfolioclaim."
      }
    }
  ]
}
</script>
