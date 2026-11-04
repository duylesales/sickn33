---
Titel: "Hoe Voeg Ik Stripe-Abonnementen Toe aan een Lovable-App?"
Trefwoorden: stripe abonnementen lovable, lovable stripe integratie, lovable terugkerende betalingen, stripe webhook supabase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Voeg Ik Stripe-Abonnementen Toe aan een Lovable-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Voeg Ik Stripe-Abonnementen Toe aan een Lovable-App?",
  "description": "Stripe-abonnementen toevoegen aan een Lovable-app vraagt om Stripe Checkout, een geverifieerde webhook, een tabel met abonnementen in Supabase en het klantportaal. Deze gids legt elk onderdeel uit en de fouten die leiden tot onbetaalde toegang of buitengesloten klanten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-18",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-add-stripe-subscriptions-to-a-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Stripe: Build subscriptions", "url": "https://docs.stripe.com/billing/subscriptions/build-subscriptions" },
    { "@type": "CreativeWork", "name": "Stripe Billing", "url": "https://docs.stripe.com/billing" },
    { "@type": "CreativeWork", "name": "Stripe: Receive events in your webhook endpoint", "url": "https://docs.stripe.com/webhooks" },
    { "@type": "CreativeWork", "name": "Stripe: Idempotent requests", "url": "https://docs.stripe.com/api/idempotent_requests" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

**Kort antwoord:** maak uw abonnementen aan als Products en Prices in Stripe, start abonnementen met Stripe Checkout vanuit een Supabase edge function, bewaar de abonnementsstatus van elke klant in een Supabase-tabel die alleen door een geverifieerde Stripe-webhook wordt bijgewerkt, en laat klanten hun facturering beheren via het Stripe Customer Portal. Uw Lovable-app geeft dan toegang op basis van die tabel, nooit op basis van de succespagina van de checkout.

Lovable kan veel hiervan genereren. De delen die het meestal fout doet, zijn precies de delen die bepalen of u wordt betaald.

## Belangrijkste Punten

- **Stripe-abonnementen in een Lovable-app hebben vier onderdelen nodig:** Products en Prices in Stripe, Checkout-sessies die op de server worden aangemaakt, een geverifieerde webhook en het Customer Portal.
- **Toegang hoort events van de webhook te volgen, nooit de succespagina.** De eigen richtlijnen van Stripe raden aan levering te laten volgen uit webhookevents, met verificatie van de handtekening.
- **Handel de volledige levenscyclus af:** proefperiodes, verlengingen, mislukte betalingen, opzeggingen en abonnementswijzigingen, niet alleen de eerste betaling.
- **Bescherm de abonnementsstatus met Row Level Security,** zodat gebruikers die kunnen lezen maar nooit schrijven.
- **Voor Nederlandse klanten** kan iDEAL een abonnement starten door SEPA-incasso in te richten voor verlengingen.

## De Vier Onderdelen

| Onderdeel | Waar het staat | Taak |
| --- | --- | --- |
| Products en Prices | Stripe-dashboard | Abonnementen, bedragen, intervallen en proefperiodes vastleggen |
| Checkout-sessie | Supabase edge function | Een abonnement starten voor de ingelogde gebruiker |
| Afhandeling van de webhook | Supabase edge function | Events van Stripe ontvangen en uw database bijwerken |
| Customer Portal | Stripe, geopend vanuit uw app | Klanten laten upgraden, downgraden, opzeggen en kaarten bijwerken |

## Stap 1: Leg Abonnementen Vast in Stripe, Niet in Code

Maak per abonnement een Product aan en per factuurinterval een Price. Uw app hoort naar Price-ID's te verwijzen, niet naar hardgecodeerde bedragen. Een prijs wijzigen wordt dan een taak in het Stripe-dashboard, geen codewijziging.

## Stap 2: Maak Checkout aan op de Server

De browser roept een edge function aan met het gekozen abonnement. De functie zoekt of maakt een Stripe Customer voor de gebruiker, maakt een Checkout Session aan in abonnementsmodus met de juiste Price-ID, en geeft de URL terug. De geheime sleutel van Stripe bestaat alleen in de secrets van de functie.

## Stap 3: Laat de Webhook over Toegang Beslissen

Maak een tabel `subscriptions` met de ID van de gebruiker of organisatie, de klant-ID van Stripe, de abonnements-ID, de status, het abonnement en het einde van de huidige periode. Uw webhook verifieert de handtekening van Stripe en handelt minstens af:

- `checkout.session.completed`: het nieuwe abonnement aan de gebruiker koppelen
- `customer.subscription.updated`: wijzigingen van abonnement, verlengingen, geplande opzeggingen
- `customer.subscription.deleted`: de toegang eindigt
- `invoice.payment_failed`: uw respijtperiode starten en de klant informeren

Maak de afhandeling idempotent, omdat Stripe hetzelfde event meer dan eens kan bezorgen, en bescherm de tabel met Row Level Security, zodat gebruikers hun eigen status kunnen lezen maar die nooit kunnen schrijven.

## Stap 4: Bepaal Functies met de Tabel

Uw Lovable-app leest de abonnementsrij van de gebruiker en toont of verbergt functies. Gevoelige functies horen ook op de server te worden gecontroleerd, in policies of edge functions, zodat een gebruiker ze niet vanuit de browser kan ontgrendelen.

## Stap 5: Voeg het Customer Portal Toe

In plaats van schermen te bouwen voor upgraden, downgraden en opzeggen, opent u het Customer Portal van Stripe vanuit een edge function. Dat handelt kaartwijzigingen, facturen en abonnementswijzigingen af, en elke wijziging komt via uw webhook terug.

## De Levenscyclus van een Abonnement Uitgelegd

Een abonnement is een toestandsmachine. Stripe documenteert de statussen die een abonnement kan hebben; in de praktijk moet uw app op een handvol daarvan reageren:

| Status | Betekenis | Wat uw app hoort te doen |
| --- | --- | --- |
| `trialing` | In een gratis proefperiode | Toegang geven, einddatum van de proef tonen |
| `active` | Betaald en actueel | Toegang geven |
| `past_due` | Een verlengingsbetaling mislukte, nieuwe pogingen lopen | Toegang behouden tijdens de respijtperiode, klant informeren |
| `canceled` | Beëindigd | Betaalde toegang intrekken, data bewaren volgens uw bewaarbeleid |
| `incomplete` | Eerste betaling niet afgerond | Nog geen toegang |
| `unpaid` | Pogingen uitgeput, afhankelijk van de instellingen | Toegang beperken, aanbieden om te betalen |

Door deze statussen in uw tabel `subscriptions` te spiegelen, bijgewerkt door webhooks, kan uw app overal consistente beslissingen nemen.

## Beveiliging en Betrouwbaarheid van Webhooks

Stripe ondertekent elke webhook met een geheim dat specifiek is voor uw endpoint. Uw afhandeling moet die handtekening verifiëren voordat het event wordt vertrouwd; anders kan iedereen een nep-event "betaling geslaagd" naar uw endpoint sturen. Stripe probeert mislukte events ook opnieuw en kan events meer dan eens of in een andere volgorde bezorgen. Praktische regels:

- Verifieer bij elk verzoek de handtekening
- Bewaar de ID's van verwerkte events en negeer duplicaten
- Haal het nieuwste abonnementsobject op bij Stripe als de volgorde ertoe doet, in plaats van op de volgorde van events te vertrouwen
- Reageer snel en doe traag werk daarna
- Monitor mislukte bezorgingen in het Stripe-dashboard

## Proefperiodes en Gratis Abonnementen

Proefperiodes verhogen het aantal aanmeldingen, maar maken de facturering ingewikkelder. Bepaal of een proefperiode vooraf een betaalmethode vereist: dat vereisen verlaagt het aantal aanmeldingen maar verhoogt de conversie; het niet vereisen doet het omgekeerde. Met Stripe is beide mogelijk. Leg gratis abonnementen vast als abonnement in uw app in plaats van als Stripe-abonnement, en maak pas een Stripe-abonnement aan wanneer een klant upgradet.

## Btw en Facturen

Stripe Billing maakt voor elke abonnementsperiode facturen aan, en Stripe Tax kan de btw berekenen voor klanten in de EU, inclusief verlegging voor bedrijven met een geldig btw-nummer. Zorg er voor een Nederlandse SaaS voor dat uw facturen uw bedrijfsgegevens en btw-nummer bevatten, en verzamel waar relevant de bedrijfsgegevens en btw-nummers van klanten. Uw accountant hoort de inrichting te bevestigen.

## Abonnementen Testen Zonder een Maand te Wachten

De testmodus van Stripe bevat test clocks, waarmee u het verstrijken van de tijd voor een klant simuleert en verlengingen, het einde van proefperiodes en mislukte betalingen in minuten activeert. Gebruik ze om elk pad in de levenscyclus vóór de lancering te testen. Dit is de effectiefste manier om te voorkomen dat u factureringsfouten pas op de eerste van de maand bij echte klanten ontdekt.

## Prijswijzigingen Later

U gaat prijzen wijzigen. Maak nieuwe Prices aan in Stripe in plaats van bestaande te bewerken, bepaal of bestaande klanten hun oude prijs houden, en communiceer wijzigingen vooraf. Omdat uw app naar Price-ID's verwijst en de informatie over het abonnement uit uw tabel met abonnementen leest, worden prijswijzigingen configuratie in plaats van codewijzigingen.

## Abonnementswijzigingen en Verrekening naar Rato

Wanneer klanten halverwege een periode upgraden of downgraden, kan Stripe de kosten automatisch naar rato verrekenen, met tegoeden of extra kosten voor het verschil. Bepaal uw beleid vóór de lancering: directe upgrades met verrekening naar rato, downgrades aan het einde van de periode, of eenvoudigere regels als uw doelgroep voorspelbaarheid verkiest. Het Customer Portal kan deze regels afdwingen, en elke wijziging komt via events `customer.subscription.updated` in uw app binnen, zodat uw logica voor toegang op één plek blijft.

## Dunning: Mislukte Betalingen Terughalen

Mislukte verlengingen horen er bij abonnementen gewoon bij: verlopen kaarten, onvoldoende saldo, weigeringen door de bank. Stripe biedt automatische nieuwe pogingen en e-mails aan klanten; combineer die met uw eigen melding in de app en een respijtperiode. Meet hoeveel mislukte verlengingen u terughaalt. Voor veel abonnementsbedrijven is het verbeteren van dit herstel een van de goedkoopste manieren om de omzet te verhogen, en het vraagt geen nieuwe klanten.

## Facturering op Organisatieniveau voor B2B

Koppel bij producten voor teams de Stripe-klant en het abonnement aan de organisatie in plaats van aan een individuele gebruiker. Prijzen per gebruiker kunnen worden ingericht met aantallen op het abonnementsitem, bijgewerkt wanneer leden worden toegevoegd of verwijderd. Zorg dat alleen eigenaren van een organisatie of beheerders van de facturering abonnementen kunnen wijzigen, afgedwongen op de server, en houd contactgegevens voor facturering gescheiden van persoonlijke gebruikersprofielen.

## Wat U na de Lancering Monitort

Houd het succes van de bezorging van webhooks in het Stripe-dashboard in de gaten, het aantal abonnementen per status, het herstelpercentage van mislukte betalingen en elk verschil tussen actieve Stripe-abonnementen en actieve betaalde accounts in uw app. Een klein wekelijks reconciliatierapport vangt problemen voordat klanten of uw accountant dat doen.

## Beveiligingschecklist voor Stripe in Lovable-Apps

- Geheime sleutel alleen in de secrets van edge functions, nooit in frontendvariabelen
- Handtekening van de webhook bij elk verzoek geverifieerd
- Prijzen op de server overgenomen uit Price-ID's van Stripe, nooit bedragen uit de browser
- Tabel met abonnementen leesbaar voor de eigenaar, alleen beschrijfbaar door servercode
- Sessies van het Customer Portal op de server aangemaakt, alleen voor de geauthenticeerde gebruiker
- Test- en live sleutels gescheiden per omgeving

## Waarom U Facturering Niet Zelf Bouwt

AI-builders kunnen een zelfgemaakt abonnementssysteem genereren met eigen logica voor verlengingen en opslag van kaarten. Vermijd dat. Stripe regelt kaartgegevens, sterke klantauthenticatie, nieuwe pogingen, facturen, btw en compliance; uw taak is de events correct aan uw app te koppelen. Zelf facturering bouwen betekent dat u verplichtingen uit de betaalkaartbranche en randgevallen op u neemt die Stripe al heeft opgelost.

## Een Opmerking over de Stripe-Integratie van Lovable

Lovable kan snel een koppeling met Stripe opzetten en checkoutcode genereren, wat een goed vertrekpunt is. Behandel het resultaat als een concept: controleer dat sessies op de server worden aangemaakt, dat webhooks worden geverifieerd, dat de tabel met abonnementen is beschermd en dat elk event in de levenscyclus wordt afgehandeld. Die vier controles maken van een werkende demo een betrouwbare facturering.

## Facturering Duidelijk Communiceren aan Klanten

Verrassingen in de facturering veroorzaken opzeggingen en supporttickets. Toon het abonnement, de prijs, het interval en de volgende factuurdatum in de accountinstellingen; stuur bij elke betaling een ontvangstbewijs; waarschuw klanten voordat een proefperiode overgaat in een betaald abonnement; en leg uit wat er gebeurt als een betaling mislukt. De e-mails van Stripe kunnen een deel hiervan afhandelen, maar duidelijkheid in de app is net zo belangrijk. Klanten die hun facturering begrijpen, betwisten die zelden.

## Houd Factureringslogica op Één Plek

Leg elke factureringsbeslissing - welk abonnement een gebruiker heeft, welke functies het ontgrendelt, wat er gebeurt bij een mislukte betaling - vast in code op de server en in policies die de tabel met abonnementen lezen. Verspreide controles in componenten lopen na verloop van tijd uit elkaar, zeker als prompts bestanden opnieuw genereren.

## De Fouten die We het Vaakst Zien

| Fout | Gevolg |
| --- | --- |
| Toegang gegeven op de succespagina | Gebruikers die de betaling afbreken krijgen toch toegang, of betalende gebruikers niet |
| Geen afhandeling van `invoice.payment_failed` | Mislukte verlengingen houden onbeperkt volledige toegang |
| Bedragen van prijzen in frontendcode | Klanten kunnen knoeien met wat ze betalen |
| Tabel met abonnementen beschrijfbaar voor gebruikers | Iedereen kan zichzelf upgraden |
| Test- en live sleutels door elkaar | Live klanten komen in de testmodus terecht, of andersom |

Voor Nederlandse klanten die iDEAL verkiezen, kan Stripe een eerste iDEAL-betaling gebruiken om SEPA-incasso in te richten voor verlengingen; onze gids over [iDEAL en Wero in Lovable-apps](https://launchstudio.eu/nl/blog/integrate-ideal-and-wero-into-a-lovable-app) legt die route uit.

## Het Laten Bouwen

LaunchStudio voegt Stripe-abonnementen toe aan Lovable-apps als onderdeel van een lancering met vaste prijs, meestal binnen het Launch & Grow-pakket (€2.500-€7.500 plus €49 per maand voor hosting). LaunchStudio wordt aangedreven door Manifera, dat al 11+ jaar betaalintegraties bouwt vanuit Amsterdam en Ho Chi Minh City; zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/). De eigen gids van Stripe over [het bouwen van abonnementen](https://docs.stripe.com/billing/subscriptions/build-subscriptions) is de gezaghebbende bron.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Leefstijlcoach Die Haar Eigen Gebruikers Betaalde

Femke Brouwers, leefstijlcoach in Zeist, bouwde Dagritme in Lovable: een app om gewoonten bij te houden, met coachingprogramma's op een maandabonnement. Lovable koppelde Stripe Checkout en markeerde gebruikers als "pro" zodra ze de succespagina bereikten.

Na twee maanden toonde Stripe 58 actieve abonnementen, terwijl de app 91 pro-gebruikers had. Sommigen hadden in Stripe opgezegd en hielden toegang; anderen hadden de checkout geopend, de succes-URL bereikt door een oud tabblad te verversen en nooit betaald. Mislukte verlengingen werden nooit opgemerkt, en de kolom `profiles.is_pro` was beschrijfbaar voor gebruikers.

LaunchStudio voegde een tabel met abonnementen toe die alleen door een geverifieerde webhook wordt bijgewerkt, handelde mislukte verlengingen af met een respijtperiode van zeven dagen en een e-mail, verplaatste de controle op abonnementen naar RLS voor premium-inhoud, koppelde het Customer Portal en bracht bestaande gebruikers in lijn met Stripe.

**Resultaat:** Vanaf de volgende factuurcyclus klopte de toegang in de app precies met Stripe, en het terughalen van mislukte verlengingen voegde ongeveer 9% toe aan de maandelijkse omzet.

> *"Ik dacht dat Stripe werkte omdat er geld binnenkwam. Ik wist alleen niet hoeveel meer er weglekte."*
> - **Femke Brouwers, Oprichter, Dagritme (Zeist)**

**Kosten & Doorlooptijd:** €2.700 (Launch & Grow-pakket: webhook, tabel met abonnementen, dunning, portaal en reconciliatie) - afgerond in 8 werkdagen, plus €49 per maand voor beheerde hosting.

## Veelgestelde Vragen

### Kan Lovable zelf Stripe-abonnementen inrichten?

Lovable kan checkoutcode en een basisintegratie genereren. Wat vaak engineering nodig heeft, zijn de webhook, idempotente updates, de afhandeling van mislukte betalingen en het beschermen van de abonnementsstatus tegen gebruikers. Bekijk die delen zorgvuldig voor de lancering.

### Moet ik toegang geven op de succespagina van Stripe?

Nee. De succespagina is een gemak voor de gebruiker, geen bewijs van betaling. Geef en trek toegang in op basis van webhookevents, die Stripe verstuurt of de klant nu terugkeert naar uw app of niet.

### Hoe laat ik klanten opzeggen of van abonnement wisselen?

Gebruik het Customer Portal van Stripe. Dat handelt abonnementswijzigingen, opzeggingen, kaartwijzigingen en facturen af, en elke wijziging bereikt uw app via webhooks. Het bespaart het bouwen en onderhouden van die schermen.

### Waarom staat LaunchStudio voor elke betaalflow op webhooks?

Omdat de 11+ jaar betaalwerk van Manifera laten zien dat redirects regelmatig falen: gesloten tabbladen, wisselen naar de bankapp, wegvallende verbindingen. Webhooks zijn het enige betrouwbare overzicht van wat Stripe werkelijk heeft afgeschreven.

### Hebben pagina's over abonnementen invloed op hoe AI-assistenten mijn product beschrijven?

Ja. Duidelijke, crawlbare prijspagina's met namen van abonnementen, prijzen en factuurintervallen geven AI-assistenten juiste feiten om te citeren. Prijzen achter een login verbergen, laat assistenten gissen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan Lovable zelf Stripe-abonnementen inrichten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het kan checkoutcode en een basisintegratie genereren; webhooks, idempotentie, mislukte betalingen en het beschermen van de abonnementsstatus vragen meestal om engineering." }
    },
    {
      "@type": "Question",
      "name": "Moet ik toegang geven op de succespagina van Stripe?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Geef en trek toegang in op basis van webhookevents, die binnenkomen of de klant nu terugkeert of niet." }
    },
    {
      "@type": "Question",
      "name": "Hoe laat ik klanten opzeggen of van abonnement wisselen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik het Customer Portal van Stripe, dat abonnementswijzigingen, opzeggingen, kaarten en facturen afhandelt en wijzigingen via webhooks doorgeeft." }
    },
    {
      "@type": "Question",
      "name": "Waarom staat LaunchStudio voor elke betaalflow op webhooks?",
      "acceptedAnswer": { "@type": "Answer", "text": "De 11+ jaar betaalwerk van Manifera laten zien dat redirects vaak falen; webhooks zijn het betrouwbare overzicht van afschrijvingen." }
    },
    {
      "@type": "Question",
      "name": "Hebben pagina's over abonnementen invloed op hoe AI-assistenten mijn product beschrijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Crawlbare prijspagina's met abonnementen, prijzen en intervallen geven assistenten juiste feiten om te citeren." }
    }
  ]
}
</script>
