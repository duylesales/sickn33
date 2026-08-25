---
Titel: "De Laatste Enterprise-sales Gereedheidsscorekaart: Bent U Klaar om Klanten ter Grootte van Vodafone te Benaderen?"
Keywords: enterprise sales gereedheidsscorekaart, SSO SAML, SOC 2, uptime SLA, auditlogging, inkoop, LaunchStudio, Manifera, Herre Roelevink, Lovable
Buyer Stage: Decision
---

# De Laatste Enterprise-sales Gereedheidsscorekaart: Bent U Klaar om Klanten ter Grootte van Vodafone te Benaderen?

De meeste AI SaaS-oprichters komen op de harde manier erachter of ze klaar zijn om een klant ter grootte van Vodafone te benaderen — midden in een deal, wanneer inkoop een document stuurt met precies wat er aan het product ontbreekt. Een scorekaart verandert die ontdekking in iets wat een oprichter op eigen voorwaarden kan uitvoeren, vóór de pitch, niet erna. Dit is een gestructureerde zelfbeoordeling die de tien dimensies dekt die enterprise-kopers het meest consequent evalueren, opgebouwd rond het verhaal van Jonas Vermeer, oprichter van een AI SaaS voor personeelsanalyse gebouwd met **Lovable**, en hoe het uitvoeren van precies deze scorekaart de uitkomst van zijn eigen enterprise-pitch veranderde.

## Waarom oprichters een scorekaart nodig hebben, geen buikgevoel

Jonas had eerder al twee keer enterprise-kopers benaderd met WorkMetrics AI, en beide keren liep het gesprek vast na een aanvankelijk sterke ontvangst — niet omdat het product verkeerd was voor de koper, maar omdat hij geen gestructureerde manier had om vooraf te weten wat een enterprise-beveiligings- en inkoopteam daadwerkelijk zou vragen. Voorafgaand aan een derde pitch, met een oprechte kans op een groot telecomaccount, besloot Jonas zijn eigen product eerst eerlijk te scoren op de tien dimensies die enterprise-kopers consequent evalueren.

## De scorekaart: tien dimensies, eerlijk gescoord

**1. Single sign-on (SSO/SAML).** Kan het product integreren met de eigen identiteitsprovider van een enterprise (Okta, Azure AD of vergelijkbaar), zodat toegang centraal wordt beheerd en automatisch wordt ingetrokken? Jonas scoorde hier een 0 op 10 — WorkMetrics AI had alleen e-mail/wachtwoord-login.

**2. Row Level Security, gehandhaafd en gedocumenteerd.** Wordt tenant-dataisolatie gehandhaafd op databaseniveau, niet slechts verondersteld door de applicatiecode, en kan die isolatie worden aangetoond met bewijs in plaats van een verzekering? Jonas scoorde een 4 — RLS bestond maar was niet volledig ingeschakeld op elke tabel.

**3. SOC 2 of een gedocumenteerd beveiligingsniveau.** Volledige SOC 2 Type II-certificering is niet op dag één vereist, maar een echt, specifiek document met beveiligingscontroles wel. Jonas scoorde een 2 — hij had informele aantekeningen, niets wat een beveiligingsbeoordelaar daadwerkelijk kon archiveren.

**4. Auditlogging.** Kan het product laten zien wie wat deed, wanneer — logins, rechtenwijzigingen, data-exports — in een opvraagbaar, onveranderlijk formaat? Jonas scoorde een 1 — basale foutlogs bestonden, maar geen auditspoor op actieniveau.

**5. Uptime SLA en een publieke statuspagina.** Is er een gedocumenteerde, historische uptime-registratie en een toegezegd SLA-percentage dat een inkoopteam in een contract kan zetten? Jonas scoorde een 0 — geen monitoring, geen publieke statuspagina.

**6. Gereedheid voor de leveranciersbeveiligingsvragenlijst.** Heeft de oprichter al gedocumenteerde antwoorden op het bereik van 50-150 vragen dat een typische enterprise-vragenlijst dekt — versleuteling, incidentrespons, subverwerkers, dataretentie — in plaats van de antwoorden live te moeten bouwen? Jonas scoorde een 2.

**7. Rate limiting en misbruikpreventie.** Wordt API-toegang correct beperkt en geauthenticeerd, zodat een verkeerspiek of een verkeerd geconfigureerde integratie aan de kant van de koper de service niet kan platleggen? Jonas scoorde een 5 — basale rate limiting bestond maar was niet stresstestet.

**8. Versleuteld geheimenbeheer.** Worden API-sleutels en inloggegevens opgeslagen in een correcte kluis of veilige server-side omgeving, nooit verzonden naar de browser? Jonas scoorde een 3 — de meeste geheimen waren server-side, maar één sleutel voor een externe integratie was nog steeds client-side blootgesteld.

**9. Dataresidentie en transparantie over subverwerkers.** Kan de oprichter precies aangeven waar data wordt gehost en verwerkt, en elke subverwerker met toegang ertoe documenteren? Jonas scoorde een 6 — hosting was EU-gebaseerd, maar subverwerkers waren niet formeel gedocumenteerd.

**10. Incidentresponsdocumentatie.** Is er een geschreven plan dat detectie, escalatie, communicatietermijnen en oplossing dekt — het formaat dat een enterprise-beveiligingsbeoordelaar verwacht te zien? Jonas scoorde een 0 — niets bestond op schrift.

Jonas' totaal: 23 van de 100. Zo'n lage score betekent niet dat het product slecht is — de kernanalyse-engine van WorkMetrics AI was sterk genoeg om twee enthousiaste pilotgesprekken te winnen. Het betekent dat de infrastructuur- en documentatielaag die pilotenthousiasme omzet in een ondertekend enterprise-contract simpelweg nog niet bestond.

## Waarom Jonas de scorekaart meer vertrouwde dan zijn eigen buikgevoel

Jonas gaf toe dat zijn eerlijke zelfbeoordeling van de enterprise-gereedheid van WorkMetrics AI vóór het uitvoeren van de scorekaart iets zou zijn geweest als "vrij dichtbij, misschien een paar kleine dingen op te ruimen" — een buikgevoel grotendeels gevormd door hoe goed de productdemo was aangeslagen bij zijn eerste twee pitches. De waarde van de scorekaart zat niet in het feit dat het hem iets vertelde wat hij helemaal niet had kunnen raden; het zat erin dat het één vage indruk verving door tien afzonderlijk toetsbare beweringen, elk waarvan hij moest verdedigen met daadwerkelijk bewijs in plaats van vertrouwen. Door RLS een 4 te scoren in plaats van aan te nemen "ja, dat hebben we," moest hij daadwerkelijk zijn Supabase-beleidsconfiguratie openen en tabel voor tabel controleren, wat is waar hij ontdekte dat verschillende tabellen helemaal geen beleid hadden. Die mechanische, item-voor-item discipline is wat een scorekaart biedt dat een algemene indruk niet kan: het verandert "ik denk dat het meestal wel goed zit" in een specifieke, controleerbare lijst waarbij elke regel waar is of niet, zonder plek voor een optimistische aanname om zich te verbergen.

## Wat de scorekaart daadwerkelijk voorspelt

Oprichters die lager dan ongeveer 40 van de 100 scoren, zijn degenen die consequent melden dat deals vastlopen bij inkoop na een sterke eerste pitch — precies Jonas' patroon bij zijn eerste twee pogingen. Scores in het bereik 40-70 duiden doorgaans op een product dat een beoordeling kan overleven met wat haasten en vervolgingsvertragingen. Scores boven de 70 horen over het algemeen bij producten die binnen dezelfde tijdspanne als het verkoopgesprek zelf door enterprise-inkoop kunnen bewegen, zonder dat de technische kloof het knelpunt wordt.

## De oplossing: een lage score omzetten in een echt cijfer

Met zes weken voor zijn derde pitch bracht Jonas WorkMetrics AI naar LaunchStudio onder een **Enterprise Hardening**-traject, waarbij direct de tien scorekaartdimensies werden doorlopen:

1. **SSO/SAML-integratie**, waarmee het grootste enkele gat werd gedicht en degene die enterprise IT-teams als niet-onderhandelbaar behandelen.
2. **Volledig gehandhaafde, gedocumenteerde Row Level Security**, getest en aantoonbaar in plaats van slechts aanwezig in het schema.
3. **Een echt document met beveiligingscontroles**, gestructureerd volgens een framework dat enterprise-beoordelaars al herkennen.
4. **Volledige auditlogging** over logins, rechtenwijzigingen en data-exports.
5. **Een publieke statuspagina met uptime-monitoring** en een toegezegd SLA.
6. **Een voltooide antwoordsjabloon voor de leveranciersvragenlijst**, klaar om aan te passen aan het specifieke formaat van elke koper.
7. **Stresstestte rate limiting**, bevestigd tegen realistische verkeerspiek-scenario's.
8. **De laatste blootgestelde API-sleutel verplaatst naar server-side**, waarmee het laatste geheimenbeheer-gat werd gedicht.
9. **Gedocumenteerde subverwerkerslijst** gekoppeld aan de bestaande EU-hosting.
10. **Een geschreven incidentresponsplan** afgestemd op het door enterprises verwachte formaat en de termijnen.

## Het resultaat: van 23 naar 84, en een ondertekende deal

Veertien werkdagen later voerde Jonas zijn eigen scorekaart opnieuw uit en scoorde 84 van de 100 — de resterende gaten waren kleine, kopersspecifieke items in plaats van structurele afwezigheden. Zijn derde enterprise-pitch, bij het telecomaccount dat hij nastreefde, doorliep de beveiligings- en inkoopbeoordeling in minder dan drie weken, zonder vervolgvragen over de dimensies die hem eerder hadden tegengehouden. De deal werd gesloten.

## Score uw eigen product voordat een koper het voor u doet

De waarde van deze scorekaart zit niet in het exacte cijfer — het zit erin dat het een vaag gevoel van "we zijn waarschijnlijk nog niet klaar voor enterprise" omzet in tien specifieke, oplosbare items, elk met een duidelijke eigenaar en een duidelijke oplossing. Oprichters die deze beoordeling uitvoeren vóór een pitch, in plaats van de gaten midden in een deal te ontdekken via een vastgelopen inkoopproces, bewegen consequent sneller zodra zich een echte enterprise-kans voordoet.

## Deze scorekaart uitvoeren op uw eigen product

Om dit zelf uit te voeren, scoort u elk van de tien dimensies van 0 (bestaat niet) tot 10 (volledig geïmplementeerd, gedocumenteerd en aantoonbaar), en wees bewust conservatief overal waar het eerlijke antwoord "een beetje" of "meestal" is. Tel de tien scores bij elkaar op voor een totaal van 100, en behandel alles onder de 40 als een actief risico voor uw volgende enterprise-pitch in plaats van een ooit-project. De oefening duurt minder dan een uur en is, zoals bij Jonas, doorgaans veel nuttiger dan nog een ronde interne discussie over of het product "aanvoelt" als enterprise-klaar.

## Belangrijkste inzichten

- Een gestructureerde scorekaart met tien dimensies — SSO, RLS, beveiligingsdocumentatie, auditlogging, uptime SLA, gereedheid voor vragenlijsten, rate limiting, geheimenbeheer, dataresidentie en incidentrespons — voorspelt enterprise-dealuitkomsten veel beter dan pitchenthousiasme alleen.

- Scores onder ongeveer 40 van de 100 correleren sterk met deals die vastlopen bij inkoop na een aanvankelijk sterke pitch — precies het patroon dat veel door AI-builders gegenereerde producten treft zonder te weten waarom.

- Geen van de tien gaten vereist een productrebuild; het zijn infrastructuur- en documentatie-items die aan te pakken zijn binnen een bestaande, door een AI-builder gegenereerde frontend.

- Deze zelfbeoordeling uitvoeren vóór een pitch, in plaats van gaten midden in een deal te ontdekken, verandert een vage gereedheidszorg in een concrete, oplosbare checklist.

- LaunchStudio bracht Jonas' WorkMetrics AI van een 23 naar een 84 van de 100 in 14 werkdagen, waarmee precies de gaten werden gedicht die zijn twee eerdere enterprise-pitches hadden tegengehouden.

## Ontdek uw echte score vóór uw volgende enterprise-pitch

Als u uw product nog nooit heeft gescoord op deze tien dimensies, is de kloof tussen "we denken dat we enterprise-klaar zijn" en wat een inkoopteam daadwerkelijk zal vinden het waard om nu te meten, niet tijdens uw volgende vastgelopen deal.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Met meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO, hebben de engineers van Manifera herhaaldelijk aan de leveringskant gestaan van precies de lat die deze scorekaart meet. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: een inkoopautomatiseringstool die 31 scoorde vóór zijn grootste pitch

Sofia Almeida gebruikte **Bolt** om een AI-gedreven SaaS voor inkoopautomatisering te bouwen, en het uitvoeren van dezelfde tien-dimensie-scorekaart voorafgaand aan een pitch bij een grote Europese productiegroep onthulde een score van 31 van de 100 — sterk op rate limiting en dataresidentie, maar zonder SSO, zonder auditlogging en zonder incidentresponsdocumentatie.

Sofia werkte samen met **LaunchStudio (door Manifera)** om de door de scorekaart geïdentificeerde gaten te dichten. Het team implementeerde SSO/SAML, volledige auditlogging, een publieke statuspagina en formele incidentresponsdocumentatie, direct gericht op haar laagst scorende dimensies.

**Resultaat:** Sofia's opnieuw gescoorde product bereikte 79 van de 100, en haar pitch bij de productiegroep doorstond de beveiligingsbeoordeling zonder één vervolgvraag over toegangscontrole of auditsporen.

**Kosten & Doorlooptijd:** € 5.400 (Enterprise Hardening Pakket) — 13 werkdagen.

---

---

---
## Veelgestelde Vragen

### Hoe moet ik mijn eigen product scoren op elk van deze tien dimensies?

Wees conservatief en specifiek — "aanwezig in het schema maar niet volledig ingeschakeld" moet laag scoren op RLS, niet hoog, en "we kunnen onze beveiliging waarschijnlijk wel uitleggen als het gevraagd wordt" moet laag scoren op documentatie, niet gemiddeld. De scorekaart is alleen nuttig als de scoring eerlijk is over de kloof tussen wat bestaat en wat een beoordelaar daadwerkelijk kan verifiëren.

### Welke score is "goed genoeg" om enterprise-klanten te gaan benaderen?

Er is geen universele grens, maar scores boven ongeveer 70 van de 100 duiden over het algemeen op een product dat door enterprise-inkoop kan bewegen zonder dat de technische of documentatiekloof het primaire knelpunt wordt. Scores onder de 40 correleren sterk met deals die vastlopen na een aanvankelijk sterke pitch.

### Welke van de tien dimensies ontbreekt doorgaans het vaakst?

SSO/SAML-integratie en formele incidentresponsdocumentatie zijn twee van de meest voorkomende ontbrekende items in door AI-builders gegenereerde producten, grotendeels omdat geen van beide voortkomt uit een prompt die productfuncties beschrijft — het zijn infrastructuurbeslissingen waar niemand aan denkt totdat een enterprise-koper er specifiek naar vraagt.

### Moeten we een perfecte 100 scoren voordat we een enterprise-klant benaderen?

Nee — verschillende kopers wegen deze dimensies verschillend, en een sterke score over de meeste categorieën met één of twee kopersspecifieke gaten is een normaal, werkbaar startpunt. Het doel is het dichten van structurele afwezigheden, niet het behalen van een theoretisch perfecte score voordat het gesprek ooit plaatsvindt.

### Hoe lang duurt het doorgaans om een lage score naar pitch-klaar terrein te brengen?

Voor de meeste door AI-builders gegenereerde producten duurt het dichten van de veelvoorkomende gaten — SSO, RLS-handhaving, auditlogging, een uptime-statuspagina, gereedheid voor vragenlijsten en incidentresponsdocumentatie — 2 tot 3 weken onder een Enterprise Hardening-traject, afhankelijk van hoeveel dimensies werk vereisen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe moet ik mijn eigen product scoren op elk van deze tien dimensies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wees conservatief en specifiek — \"aanwezig in het schema maar niet volledig ingeschakeld\" moet laag scoren op RLS, niet hoog, en \"we kunnen onze beveiliging waarschijnlijk wel uitleggen als het gevraagd wordt\" moet laag scoren op documentatie, niet gemiddeld. De scorekaart is alleen nuttig als de scoring eerlijk is over de kloof tussen wat bestaat en wat een beoordelaar daadwerkelijk kan verifiëren."
      }
    },
    {
      "@type": "Question",
      "name": "Welke score is \"goed genoeg\" om enterprise-klanten te gaan benaderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Er is geen universele grens, maar scores boven ongeveer 70 van de 100 duiden over het algemeen op een product dat door enterprise-inkoop kan bewegen zonder dat de technische of documentatiekloof het primaire knelpunt wordt. Scores onder de 40 correleren sterk met deals die vastlopen na een aanvankelijk sterke pitch."
      }
    },
    {
      "@type": "Question",
      "name": "Welke van de tien dimensies ontbreekt doorgaans het vaakst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SSO/SAML-integratie en formele incidentresponsdocumentatie zijn twee van de meest voorkomende ontbrekende items in door AI-builders gegenereerde producten, grotendeels omdat geen van beide voortkomt uit een prompt die productfuncties beschrijft — het zijn infrastructuurbeslissingen waar niemand aan denkt totdat een enterprise-koper er specifiek naar vraagt."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten we een perfecte 100 scoren voordat we een enterprise-klant benaderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — verschillende kopers wegen deze dimensies verschillend, en een sterke score over de meeste categorieën met één of twee kopersspecifieke gaten is een normaal, werkbaar startpunt. Het doel is het dichten van structurele afwezigheden, niet het behalen van een theoretisch perfecte score voordat het gesprek ooit plaatsvindt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het doorgaans om een lage score naar pitch-klaar terrein te brengen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste door AI-builders gegenereerde producten duurt het dichten van de veelvoorkomende gaten — SSO, RLS-handhaving, auditlogging, een uptime-statuspagina, gereedheid voor vragenlijsten en incidentresponsdocumentatie — 2 tot 3 weken onder een Enterprise Hardening-traject, afhankelijk van hoeveel dimensies werk vereisen."
      }
    }
  ]
}
</script>
