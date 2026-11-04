---
Titel: "Mollie-Integratie voor AI-Gebouwde Apps: Een Stapsgewijze Gids"
Trefwoorden: mollie integratie ai-app, mollie lovable, mollie webhook, mollie supabase edge function, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Mollie-Integratie voor AI-Gebouwde Apps: Een Stapsgewijze Gids

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Mollie-Integratie voor AI-Gebouwde Apps: Een Stapsgewijze Gids",
  "description": "Een praktische gids voor Mollie-integratie in apps die met Lovable, Bolt of Cursor zijn gebouwd: API-sleutels, betalingen aanmaken in een Supabase edge function, de webhooks van Mollie met alleen een ID afhandelen, statussen, terugbetalingen en live gaan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-20",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/mollie-integration-for-ai-built-apps-step-by-step" },
  "citation": [
    { "@type": "CreativeWork", "name": "Mollie API documentation", "url": "https://docs.mollie.com/" },
    { "@type": "CreativeWork", "name": "Mollie", "url": "https://www.mollie.com/" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "iDEAL", "url": "https://www.ideal.nl/en/" }
  ]
}
</script>

Mollie is de betaalprovider waar veel Nederlandse en Belgische oprichters voor kiezen: gevestigd in Amsterdam, sterk in iDEAL en Bancontact, en met duidelijke tarieven. AI-appbuilders kiezen echter standaard voor Stripe. Vraag Lovable of Bolt om een Mollie-integratie en u krijgt meestal iets dat een betaling aanmaakt en de klant doorstuurt, maar niet de onderdelen die het betrouwbaar maken. Deze gids laat de volledige Mollie-integratie stap voor stap zien, voor een app met een Supabase-backend.

## Belangrijkste Punten

- **Mollie is een betaalprovider uit Amsterdam** die sterk is in iDEAL, Bancontact en SEPA, en past vanzelfsprekend bij Nederlandse en Belgische bedrijven.
- **AI-builders kiezen standaard voor Stripe,** dus Mollie-integraties die met prompts zijn gegenereerd, missen vaak de onderdelen die betalingen betrouwbaar maken.
- **De webhook van Mollie stuurt alleen een betalings-ID.** Uw server haalt de echte status op via de API van Mollie, waardoor vervalste webhooks onschadelijk zijn.
- **Bedragen zijn strings met twee decimalen, prijzen komen uit uw database,** en afhandelaars moeten idempotent zijn omdat Mollie uw webhook meerdere keren kan aanroepen.
- **Een volledige Mollie-integratie** met statussen, terugbetalingen en testen maakt meestal deel uit van een LaunchStudio-offerte van €1.200-€3.500.

## Wat U Nodig Heeft Voordat U Begint

- Een Mollie-account met een goedgekeurd websiteprofiel voor uw domein
- Test- en live API-sleutels (die beginnen met `test_` en `live_`)
- Een Supabase-project met edge functions ingeschakeld, of een andere serveromgeving
- Een tabel `orders` met minstens: id, user_id, amount, currency, status, mollie_payment_id

## Stap 1: Bewaar Sleutels Alleen op de Server

API-sleutels van Mollie zijn geheim. Voeg ze toe als secrets van edge functions, nooit in frontendcode of `.env`-bestanden die in de browserbundel terechtkomen.

```bash
supabase secrets set MOLLIE_API_KEY=test_xxxxxxxxxxxxxxxx
```

Schakel pas over op de `live_`-sleutel als u klaar bent om echte betalingen te accepteren, en leg geen van beide sleutels ooit vast in git.

## Stap 2: Maak de Betaling aan in een Edge Function

De browser vraagt uw functie om een bestelling te betalen. De functie zoekt de bestelling op, controleert of die bij de gebruiker hoort en maakt de betaling aan bij Mollie.

```ts
// supabase/functions/create-payment/index.ts (simplified)
const order = await getOrderForUser(orderId, userId); // server-side lookup
const res = await fetch("https://api.mollie.com/v2/payments", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${Deno.env.get("MOLLIE_API_KEY")}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    amount: { currency: "EUR", value: order.amount.toFixed(2) },
    description: `Order ${order.id}`,
    redirectUrl: `https://yourapp.nl/orders/${order.id}`,
    webhookUrl: "https://<project>.functions.supabase.co/mollie-webhook",
    metadata: { order_id: order.id },
  }),
});
const payment = await res.json();
await savePaymentId(order.id, payment.id);
return Response.json({ checkoutUrl: payment._links.checkout.href });
```

Twee details die AI-tools vaak fout doen: Mollie verwacht het bedrag als **string met twee decimalen** (`"19.95"`), en de prijs moet uit uw database komen, niet uit het verzoek.

## Stap 3: Handel de Webhook van Mollie op de Juiste Manier Af

De webhook van Mollie verschilt van die van Stripe. Hij stuurt niet de details van de betaling, alleen de betalings-ID. Uw functie moet vervolgens **de betaling ophalen via de API van Mollie** om de status te lezen. Dat is een beveiligingsfunctie: een vervalste webhook kan niet beweren dat een betaling is betaald, omdat uw functie het rechtstreeks aan Mollie vraagt.

```ts
// supabase/functions/mollie-webhook/index.ts (simplified)
const form = await req.formData();
const id = form.get("id");
const payment = await fetchMolliePayment(id); // GET /v2/payments/{id}
await updateOrderFromPayment(payment.metadata.order_id, payment.status);
return new Response("OK", { status: 200 });
```

Maak `updateOrderFromPayment` **idempotent**: als de bestelling al betaald is, verandert een tweede webhook niets. Mollie kan uw webhook meerdere keren aanroepen naarmate de status van een betaling verandert.

## Stap 4: Koppel Elke Status

| Status bij Mollie | Wat uw app moet doen |
| --- | --- |
| `open` | Wachten, "betaling in behandeling" tonen |
| `pending` | Wachten, sommige methoden doen er langer over om te bevestigen |
| `authorized` | Voor methoden die capture ondersteunen, beslissen wanneer te capturen |
| `paid` | De bestelling leveren, toegang geven, ontvangstbewijs sturen |
| `canceled` | Gereserveerde voorraad of plaatsen vrijgeven, opnieuw proberen toestaan |
| `expired` | Hetzelfde als canceled |
| `failed` | Een duidelijke melding tonen, opnieuw proberen met een andere methode toestaan |

De terugkeerpagina hoort de status van de bestelling uit uw database te lezen, en niet aan te nemen dat het gelukt is omdat de klant terugkwam.

## Stap 5: Terugbetalingen en Chargebacks

Terugbetalingen horen te starten vanuit een beheeractie die een functie op de server aanroept. Chargebacks komen binnen als statuswijzigingen op de oorspronkelijke betaling, dus uw webhookafhandeling moet klaar zijn om toegang in te trekken wanneer een betaalde bestelling wordt teruggeboekt.

## Stap 6: Checklist om Live te Gaan

- Websiteprofiel in Mollie goedgekeurd voor het live domein
- `live_`-sleutel ingesteld in de productiesecrets, `test_`-sleutel alleen in staging
- Webhook-URL bereikbaar vanaf internet, die snel 200 teruggeeft
- Eén echte betaling van een klein bedrag van begin tot eind getest op mobiel
- Ontvangstbewijzen en facturen bevatten uw bedrijfsgegevens en btw-informatie

## De Architectuur in Één Oogopslag

Een betrouwbare Mollie-integratie in een app met Supabase-backend heeft vier bewegende delen:

| Onderdeel | Verantwoordelijkheid |
| --- | --- |
| Tabel `orders` | Bron van waarheid voor wat de klant verschuldigd is en de status van de bestelling |
| Edge function `create-payment` | Valideert de bestelling, maakt de Mollie-betaling aan, slaat de betalings-ID op |
| Edge function `mollie-webhook` | Haalt de betaling op bij Mollie en werkt de bestelling idempotent bij |
| Terugkeerpagina | Leest de status van de bestelling uit uw database en toont de juiste melding |

Niets in de browser beslist dat een bestelling betaald is. Die ene regel voorkomt de meeste betaalfouten in AI-gebouwde apps.

## Idempotentie in de Praktijk

Mollie roept uw webhook aan wanneer de status van een betaling verandert, en probeert het opnieuw als uw endpoint niet succesvol reageert. Uw afhandeling moet daarom hetzelfde resultaat opleveren, ongeacht hoe vaak die draait. In de praktijk:

- Werk de status van de bestelling alleen bij als de nieuwe status verschilt van de opgeslagen status
- Start bijwerkingen, zoals een ontvangstbewijs sturen of toegang geven, alleen bij de overgang naar `paid`, en leg vast dat u dat heeft gedaan
- Reageer snel met status 200 en doe traag werk daarna of in een wachtrij
- Log elke webhookaanroep met de betalings-ID en de resulterende status

Hetzelfde principe geldt voor het aanmaken van betalingen: als een klant dubbelklikt, hoort uw functie een bestaande openstaande betaling voor die bestelling te hergebruiken in plaats van een tweede aan te maken.

## Beveiligingsoverwegingen

- **Sleutels:** test- en live sleutels van Mollie zijn geheimen. Ze horen in de secrets van edge functions, gescheiden per omgeving, en moeten worden vervangen als ze zijn blootgesteld. Het Secrets Management Cheat Sheet van OWASP beschrijft de werkwijzen.
- **Webhook-endpoint:** omdat de webhook van Mollie alleen een ID bevat, hoeft u de inhoud niet te vertrouwen; u bevestigt altijd door Mollie aan te roepen. Beperk het endpoint toch met rate limiting en negeer onbekende ID's.
- **Metadata:** bewaar uw order-ID in de metadata van de betaling zodat de webhook de bestelling kan vinden, maar zet nooit persoonsgegevens die u niet nodig heeft in betalingsomschrijvingen.
- **Terugbetalingen:** beperk terugbetalingen tot geautoriseerde medewerkers via een functie op de server, en leg vast wie elke terugbetaling heeft gedaan.

## Meerdere Betaalmethoden

Mollie ondersteunt naast iDEAL veel methoden, waaronder kaarten, Bancontact, SEPA-overschrijving en andere, afhankelijk van uw account. U kunt de gehoste checkout van Mollie de beschikbare methoden laten tonen of er één vooraf selecteren op basis van het land van de klant. Voor Belgische klanten is Bancontact inschakelen meestal net zo belangrijk als iDEAL voor Nederlandse klanten.

## Live Gaan Zonder Verrassingen

Voer, voordat u overschakelt op de live sleutel, de volledige set testuitkomsten uit, bevestig dat de webhook-URL via HTTPS vanaf internet bereikbaar is, en controleer dat uw facturen of ontvangstbewijzen uw bedrijfsgegevens en btw-informatie bevatten. Reconcilieer na de lancering maandelijks de uitbetalingen van Mollie met bestellingen. Een klein verschil dat in de eerste maand wordt gevonden, kost een middag; hetzelfde verschil aan het einde van het jaar kost een week.

## Bestellingen Die Nooit Worden Betaald

Niet elke klant die een betaling start, rondt die af. Sommigen sluiten het tabblad, sommigen bedenken zich, sommigen raken afgeleid door hun bankapp. Zonder plan stapelen deze verlaten bestellingen zich op, blokkeren ze voorraad of plaatsen en vervuilen ze rapporten. Een nette aanpak:

- Geef elke openstaande bestelling een vervaltijd die past bij de betaalmethode, bijvoorbeeld 15-30 minuten voor iDEAL
- Geef gereserveerde voorraad of boekingsmomenten automatisch vrij wanneer Mollie `expired` of `canceled` meldt
- Bied voor bestellingen met een hoge waarde een link "rond uw betaling af" aan in een herinneringsmail, met een nieuwe betaling voor dezelfde bestelling
- Rapporteer verlaten bestellingen wekelijks; een plotselinge stijging wijst vaak op een probleem in de checkout in plaats van op klantgedrag

## Logging en Support

Wanneer een klant schrijft "ik heb betaald maar er gebeurde niets", hoort u binnen minuten te kunnen antwoorden. Log elke aangemaakte betaling en elke webhookaanroep met tijdstempels, de betalings-ID van Mollie, de order-ID en de resulterende status. Geef supportmedewerkers een eenvoudig scherm dat deze tijdlijn per bestelling toont. De meeste gevallen van "ontbrekende betaling" blijken verlopen betalingen, betalingen voor een andere bestelling, of een webhook die faalde door een deployment; een tijdlijn maakt elk daarvan meteen duidelijk.

## Uw Webhook Lokaal en in Staging Testen

Mollie moet uw webhook via internet kunnen bereiken, wat lokaal testen lastig maakt. Twee praktische opties: deploy de webhookfunctie naar een staging-project in Supabase en laat testbetalingen daarheen wijzen, of gebruik tijdens het ontwikkelen een tunnelingtool. Houd hoe dan ook per omgeving aparte test- en live sleutels aan, en laat live betalingen nooit naar een staging-endpoint wijzen.

## Mollie-Profielen en Meerdere Websites

Een Mollie-account kan meerdere websiteprofielen bevatten, elk met eigen betaalmethoden en instellingen. Als u een stagingsite en een productiesite heeft, of meerdere merken, houd ze dan als aparte profielen met aparte sleutels. Zo blijft testverkeer uit de productierapporten en kunt u methoden per merk inschakelen.

## Mollie of Stripe?

Als u nog kiest, de korte versie: Mollie past bij bedrijven die zich op Nederland en België richten en lokale methoden en een Nederlandse provider willen; Stripe past bij bedrijven die internationaal verkopen met complexe facturering. Beide ondersteunen iDEAL. Ons artikel over [iDEAL en Wero integreren in een Lovable-app](https://launchstudio.eu/nl/blog/integrate-ideal-and-wero-into-a-lovable-app) vergelijkt ze uitgebreider.

## Het Laten Bouwen

Een volledige Mollie-integratie met webhooks, statussen, terugbetalingen en testen is een gangbare klus voor LaunchStudio, meestal onderdeel van een vaste offerte tussen €1.200 en €3.500. LaunchStudio brengt de engineering van Manifera op enterpriseniveau naar de economie van oprichters: Manifera bouwt al 11+ jaar betaalintegraties met Stripe, Mollie en PayPal, vanuit het Amsterdamse kantoor aan de Herengracht 420 en het ontwikkelcentrum in Ho Chi Minh City. Zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/) voor de bredere stack, en [de API-documentatie van Mollie](https://docs.mollie.com/) voor de volledige referentie.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Sportclubapp Die Onbetaalde Contributie als Betaald Markeerde

Sjoerd Wiersma, penningmeester van een korfbalclub in Leeuwarden, bouwde Contributieman met Bolt, zodat leden hun jaarcontributie en bijdragen voor wedstrijddagen online konden betalen in plaats van via een overschrijving. Hij koos Mollie omdat de club al een account had. Bolt genereerde een betaalflow die leden naar Mollie en terug stuurde.

Aan het einde van de eerste maand waren het bankafschrift van de club en de app het oneens. De app toonde 212 betaalde contributies; Mollie toonde er 174. De oorzaak was de terugkeerpagina: elk lid dat die bereikte, werd als betaald gemarkeerd, ook leden die in hun bankapp annuleerden of de betaling lieten verlopen. Er was helemaal geen webhook. De live sleutel van Mollie stond bovendien in een omgevingsbestand van de frontend, en bedragen werden vanuit de browser verstuurd.

LaunchStudio verplaatste het aanmaken van betalingen naar een Supabase edge function met bedragen op de server, voegde een Mollie-webhook toe die de betaalstatus via de API ophaalde en lidmaatschappen idempotent bijwerkte, koppelde elke status aan een duidelijke melding voor leden en verving de blootgestelde sleutel. Met een reconciliatierapport kon Sjoerd elke maand de totalen van de app en Mollie vergelijken.

**Resultaat:** De reconciliatie van de maand daarop klopte tot op de cent. De club inde dat seizoen 96% van de jaarcontributies online, en de 38 leden die onterecht als betaald waren gemarkeerd, werden benaderd en betaalden binnen twee weken.

> *"De app zei dat iedereen had betaald. De bank zei iets anders. Ik wist niet dat een webhook het ding was dat tussen die twee getallen stond."*
> - **Sjoerd Wiersma, Oprichter, Contributieman (Leeuwarden)**

**Kosten & Doorlooptijd:** €1.700 (Launch Ready-pakket met betalingen: Mollie edge functions, webhook, statussen, vervanging van sleutels en reconciliatie) - afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Waarom stuurt de webhook van Mollie alleen een betalings-ID?

Het is een bewust beveiligingsontwerp. Omdat uw server de betaling via de API van Mollie moet ophalen om de status te weten, kan een vervalste webhook uw app er niet van overtuigen dat een betaling is geslaagd. Het betekent ook dat u altijd met de nieuwste status werkt, zelfs als webhooks in de verkeerde volgorde binnenkomen.

### Kan ik Mollie gebruiken met Lovable en Supabase?

Ja. De netste opzet gebruikt Supabase edge functions: één om betalingen aan te maken en één om webhooks te ontvangen. De Lovable-frontend roept de eerste functie aan en leest de status van de bestelling uit de database. Lovable heeft mogelijk expliciete instructies nodig, omdat het standaard voor Stripe kiest.

### Moet ik Mollie-bedragen opslaan als decimalen of in centen?

Sla bedragen in uw database op als gehele getallen in centen om afrondingsfouten te voorkomen, en zet ze pas bij het aanmaken van de betaling om naar het stringformaat met twee decimalen van Mollie. Veel AI-gegenereerde integraties gebruiken kommagetallen, wat bedragen als 19.949999 kan opleveren.

### Waarom is een moederbedrijf in Amsterdam belangrijk voor Mollie-integraties?

Mollie is een Amsterdams bedrijf, gebouwd voor Nederlandse en Europese betaalgewoonten. Door de vestiging van Manifera in Amsterdam en de lange lijst Nederlandse klanten kennen de engineers de manier waarop Nederlandse klanten betalen, hoe Mollie zich in de praktijk gedraagt en wat de Nederlandse boekhouding van betaalgegevens nodig heeft.

### Helpt een betrouwbare betaalintegratie bij de zichtbaarheid in zoekmachines en AI?

Indirect. Duidelijke prijspagina's, stabiele checkouts en juiste gestructureerde data over geaccepteerde betaalmethoden helpen zowel zoekmachines als AI-assistenten u aan te bevelen bij Nederlandse gebruikers. Kapotte checkouts leveren slechte betrokkenheidssignalen en negatieve reviews op die kunnen worden geciteerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom stuurt de webhook van Mollie alleen een betalings-ID?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het is een beveiligingsontwerp: de server haalt de betaling op via de API van Mollie, dus een vervalste webhook kan geen succes veinzen en de app ziet altijd de nieuwste status." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Mollie gebruiken met Lovable en Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gebruik één Supabase edge function om betalingen aan te maken en een andere voor webhooks, waarbij de Lovable-frontend de status van bestellingen uit de database leest." }
    },
    {
      "@type": "Question",
      "name": "Moet ik Mollie-bedragen opslaan als decimalen of in centen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Sla gehele getallen in centen op en zet ze pas bij het aanmaken van de betaling om naar de string met twee decimalen van Mollie, om afrondingsfouten te voorkomen." }
    },
    {
      "@type": "Question",
      "name": "Waarom is een moederbedrijf in Amsterdam belangrijk voor Mollie-integraties?",
      "acceptedAnswer": { "@type": "Answer", "text": "De vestiging van Manifera in Amsterdam en de ervaring met Nederlandse klanten betekenen bekendheid met Nederlandse betaalgewoonten, het gedrag van Mollie en wat de Nederlandse boekhouding nodig heeft." }
    },
    {
      "@type": "Question",
      "name": "Helpt een betrouwbare betaalintegratie bij de zichtbaarheid in zoekmachines en AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect, via duidelijke prijspagina's, stabiele checkouts en juiste gestructureerde data over betalingen, terwijl kapotte checkouts slechte signalen en negatieve reviews opleveren." }
    }
  ]
}
</script>
