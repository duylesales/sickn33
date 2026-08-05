---
Titel: "Het domein van uw AI-prototype migreren zonder een dag uitval"
Trefwoorden: ai deployment, ai native, DNS migration, custom domain setup, zero-downtime cutover
Koperfase: Overweging
Doelgroep: AI-Native oprichter
---

# Het domein van uw AI-prototype migreren zonder een dag uitval

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het domein van uw AI-prototype migreren zonder een dag uitval",
  "description": "Het overstappen van een tijdelijk subdomein naar een aangepast domein lijkt triviaal.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/dns-domain-migration-zero-downtime-ai-founders"
  }
}
</script>

Het is de dag van de lancering. U heeft het aangepaste domein gekocht, u bent enthousiast, en het voelt alsof het omzetten vijf minuten zou moeten duren: verander een paar DNS-records, klaar. De volgende acht uur bereiken sommige bezoekers uw app prima en anderen krijgen een foutmelding of een lege pagina, afhankelijk van welke DNS-cache hen op dat exacte moment toevallig bedient. En er is niets wat u kunt doen om het te versnellen als het eenmaal in beweging is.

## Waarom DNS-wijzigingen niet onmiddellijk gebeuren, hoewel het wel zo voelt

DNS-records worden geleverd met een Time To Live (TTL)-waarde – een getal, doorgaans in seconden, dat elke server en browser die dat record converteert vertelt hoe lang ze het oude antwoord mogen blijven gebruiken voordat ze opnieuw controleren. Als de DNS-records van uw domein zijn ingesteld met een standaard TTL van bijvoorbeeld 24 uur (86.400 seconden), dan geldt dat wanneer u verandert waar dat domein naartoe wijst, elke DNS-resolver ter wereld die het oude record al heeft gecached dit tot 24 uur blijft gebruiken na uw wijziging, ongeacht wanneer u het daadwerkelijk heeft gemaakt. Sommige bezoekers worden onmiddellijk naar uw nieuwe app geleid. Anderen blijven urenlang het oude subdomein of een dode eindpunt raken, puur gebaseerd op het moment dat hun lokale resolver voor het laatst zijn cache heeft ververst.

De meeste oprichters die overstappen van een tijdelijk Lovable- of Bolt-subdomein naar een echt aangepast domein weten niet dat TTL bestaat totdat ze de overstap al hebben gemaakt en zijn begonnen met het afhandelen van "uw site is down"-berichten van mensen die een uur later zeggen dat het prima werkt. De herstelling is niet iets wat u achteraf kunt toepassen als de migratie eenmaal onderweg is – het moet gebeuren *voordat* u het daadwerkelijke A- of CNAME-record aanraakt.

## De volgorde die u daadwerkelijk een schone omzetting oplevert

Een domeinmigratie zonder uitval volgt een specifieke volgorde: verlaag eerst de TTL op het bestaande DNS-record – vaak tot 300 seconden of minder – en wacht ten minste net zo lang als de *oude* TTL-waarde voordat u iets anders doet. Elk cachegeheugen wereldwijd heeft zo de kans gehad om de nieuwe, kortere TTL op te pikken. Pas nadat die wachttijd is verstreken verandert u het record daadwerkelijk om naar de nieuwe bestemming te wijzen. Omdat elke resolver nu de korte TTL respecteert, verspreidt de wijziging zich wereldwijd binnen minuten in plaats van uren. Nadat de omzetting als stabiel is bevestigd, kan de TTL worden teruggezet naar een normale waarde voor alledaagse prestaties.

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordt het zo: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. We hebben elf jaar ervaring in exact dat." Een domeinmigratie is een klein, eenmalig voorbeeld van exact dat soort kloof – het is geen coderingsprobleem dat een AI-tool kan oplossen, het is een infrastructuur-volgorde-probleem dat vereist dat u een dag van tevoren weet wat u moet doen.

LaunchStudio's ingenieurs, ondersteund vanuit Manifera's kantoor in Singapore op 100 Tras Street, handelen domein- en infrastructuurmigraties af als een standaard onderdeel van het verplaatsen van een met AI gebouwd prototype naar een productie-gereed lancering. Als uw domeinoverstap nog voor u ligt, is het de moeite waard om [met een ingenieur te praten over uw migratieplan](https://launchstudio.eu/en/#contact) een paar dagen voordat u van plan bent om de knop om te zetten, en niet op de ochtend zelf.

## Een schone DNS-omzetting mislukt nog steeds zonder een certificaat dat erop wacht

Het goed krijgen van de TTL-volgorde lost het verspreidingsprobleem op, maar het lost een ander probleem op dan het probleem dat oprichters vervolgens opvangt: zelfs een perfect getimede DNS-omzetting leidt bezoekers naar een nieuw domein dat nog geen geldig HTTPS-certificaat heeft dat het dekt. De meeste hostingplatformen leveren een TLS-certificaat automatisch, maar pas *nadat* ze detecteren dat het domein daadwerkelijk naar hen wijst. Dit betekent dat het certificaatverzoek pas begint bij dezelfde DNS-wijziging die onmiddellijk zou moeten zijn, wat een tweede, afzonderlijke vertraging creëert bovenop het DNS-verspreidingsvenster.

```
1. DNS-omzetting voltooit — nieuw domein wijst nu naar uw host
2. Host detecteert het domein en vraagt een TLS-certificaat aan
3. Certificaatautoriteit valideert domeineigendom (minuten tot uren)
4. Totdat de validatie is voltooid mislukken HTTPS-verzoeken naar het nieuwe domein
```

De herstelling is het activeren van certificaatlevering vóór de daadwerkelijke omzetting overal waar het hostingplatform dit ondersteunt – veel providers laten u een domein toevoegen en vooraf valideren voordat het live is. Het certificaat is zo al uitgegeven en wacht op het moment dat DNS er daadwerkelijk naartoe wijst, in plaats van dat er een tweede aftelling begint exact wanneer bezoekers voor het eerst aankomen. Het expliciet bevestigen van deze stap, in plaats van aan te nemen dat "DNS is hersteld, dus de migratie is klaar", is wat een omzetting die van begin tot eind schoon is scheidt van een omzetting die een DNS-probleem van acht uur inruilt voor een korter maar nog steeds zichtbaar certificaatfout-venster.

## Echt voorbeeld

### Een AI-native oprichter in actie: De lanceringsdag die acht extra uur duurde

Milo Prins, een oprichter in Purmerend, bouwde ReisPlanner, een SaaS voor reisroutes, met behulp van Bolt. Klaar om publiekelijk te lanceren, had hij de app tijdens de ontwikkeling op een tijdelijk subdomein gedraaid en wilde hij op de lanceringsochtend overstappen naar zijn gekochte aangepaste domein. De wijziging zelf was op papier eenvoudig genoeg: werk de DNS-records bij om het nieuwe domein naar de app te laten wijzen.

Waar Milo geen rekening mee hield was de TTL van het bestaande DNS-record, die op de standaard, lange waarde was gelaten. Op het moment dat hij het record veranderde, bleven DNS-resolvers die de oude configuratie al hadden gecached deze urenlang gebruiken. Resolvers die toevallig sneller verversten pikten het nieuwe domein onmiddellijk op. Het resultaat was een onvoorspelbaar venster van acht uur waar ongeveer de helft van ReisPlanner's bezoekers op de lanceringsdag een gebroken ervaring kreeg, puur afhankelijk van hun locatie en de DNS-cache van hun ISP – precies op de dag dat Milo het zich het minst kon veroorloven.

LaunchStudio auditeerde de DNS-configuratie achteraf en herbouwde Milo's proces voor toekomstige wijzigingen: verlaag de TTL een volledige dag vóór een geplande DNS-wijziging, wacht het oude TTL-venster af voordat u omzet, voer de daadwerkelijke recordwijziging uit zodra de versreiding vrijwel onmiddellijk zal zijn, en herstel de normale TTL pas na het bevestigen van de stabiliteit. **Resultaat:** ReisPlanner's daaropvolgende infrastructuurwijzigingen voltooien nu zonder enige bezoekersgerichte uitval.

> *"Ik wist niet eens dat DNS-caching iets was wat me acht uur lang kon bijten. Het voelde als zo'n kleine technische stap, totdat het dat niet meer was."*
> — **Milo Prins, Oprichter, ReisPlanner (Purmerend)**

**Kosten en tijdlijn:** € 450 (DNS-audit, migratie-volgorde, gedocumenteerde omzettingsprocedure) — voltooid in 2 werkdagen.

---

## Veelgestelde vragen

### Wat is TTL en waarom veroorzaakt het uitval tijdens een domeinmigratie?

TTL (Time To Live) vertelt DNS-resolvers hoe lang ze een record moeten cachen voordat ze het opnieuw controleren. Als het tijdens een migratie hoog blijft gelaten, blijven sommige bezoekers uren na de wijziging de oude bestemming bereiken, wat een inconsistente uitval veroorzaakt.

### Hoe ver van tevoren moet ik mijn DNS-TTL verlagen voordat ik een domein migreer?

Minimaal moet u de bestaande (olde) TTL-waarde afwachten nadat u deze heeft verlaagd voordat u de daadwerkelijke bestemmingswijziging maakt. Als de oude TTL 24 uur was, plan de verlagingsstap dan ten minste een dag vóór de echte omzetting.

### Kan dit hetzelfde probleem veroorzaken bij hostingmigraties, en niet alleen bij domeinwijzigingen?

Ja – elke wijziging die inhoudt dat wordt bijgewerkt waar de DNS-records van een domein naartoe wijzen, inclusief het verhuizen tussen hostingproviders, is onderhevig aan dezelfde TTL-verspreidingsvertraging als het niet correct wordt geordend.

### Als DNS schoon verspreidt, is de migratie dan daadwerkelijk volbracht?

Niet noodzakelijkerwijs – de meeste hostingplatformen beginnen pas met het leveren van het TLS-certificaat van een nieuw domein zodra ze detecteren dat DNS naar hen wijst. Dit kan een afzonderlijk HTTPS-foutvenster creëren, zelfs nadat DNS zelf schoon is omgezet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom duurt een DNS domeinverwijzing soms 24 uur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vanwege de TTL (Time-to-Live) van het oude DNS record. DNS-resolvers wereldwijd onthouden het oude IP-adres totdat die TTL-tijd is afgelopen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom je downtime bij een domeinmigratie van een AI-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Verlaag de TTL 24-48 uur vóór de migratie naar 300 seconden (5 minuten). Voer daarna pas de IP/CNAME wijziging uit voor een vrijwel instant switch."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom krijgen bezoekers na een DNS-switch vaak een SSL/HTTPS-foutmelding?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat het nieuwe SSL/TLS certificaat pas wordt aangevraagd zodra de host de DNS-switch ziet. Vraag het SSL-certificaat vooraf aan via DNS-validation."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is dit een infrastructuurprobleem en geen code-bug?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zoals Herre Roelevink stelt: dit staat los van de app-code. Het is een plannings- en netwerkvolgorde die 1 dag van tevoren voorbereid moet worden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een begeleide zero-downtime domeinmigratie bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een DNS-audit en zero-downtime migratieprotocol kost gemiddeld €450 en duurt 2 werkdagen."
      }
    }
  ]
}
</script>