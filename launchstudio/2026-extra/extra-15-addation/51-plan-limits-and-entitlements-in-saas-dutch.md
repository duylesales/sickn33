---
Titel: "Planlimieten en Entitlements Afdingen in SaaS"
Trefwoorden: saas plan limits, entitlements saas, feature gating stripe, enforce subscription limits supabase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Planlimieten en Entitlements Afdingen in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Planlimieten en Entitlements Afdingen in SaaS",
  "description": "Prijzenpagina's werken alleen als uw software de limieten daadwerkelijk afdwingt. Deze handleiding legt uit hoe u planlimieten en feature-entitlements implementeert in een met AI gebouwde SaaS: het modelleren van plannen en rechten, synchroniseren met Stripe of Mollie via webhooks, limieten afdwingen op server- en databaseniveau, omgaan met upgrades, downgrades en coulanceperiodes, en effectieve upgradeprompts ontwerpen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-07",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/plan-limits-and-entitlements-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Stripe: Entitlements", "url": "https://docs.stripe.com/billing/entitlements" },
    { "@type": "CreativeWork", "name": "Stripe: Subscription webhooks", "url": "https://docs.stripe.com/billing/subscriptions/webhooks" },
    { "@type": "CreativeWork", "name": "Supabase Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" }
  ]
}
</script>

Een prijzenpagina is een tweezijdige contractuele belofte. Klanten op het Starter-plan krijgen toegang tot bepaalde basisfuncties en quota. Klanten op het Pro-plan betalen aanzienlijk meer omdat zij profiteren van hogere limieten en geavanceerde mogelijkheden. Wanneer uw applicatie dit onderscheid echter niet strikt afdwingt, is uw prijzenpagina een wassen neus: gratis gebruikers overschrijden ongehinderd hun projectquota, Starter-klanten gebruiken zware Pro-functionaliteiten en niemand voelt de noodzaak om te upgraden.

In met AI gebouwde webapplicaties worden abonnementen en limieten schrikbarend vaak uitsluitend in de frontend (gebruikersinterface) gecontroleerd. De knop "Exporteer naar PDF" wordt verborgen voor Starter-gebruikers, maar het achterliggende API-endpoint voert de export vrolijk uit voor iedereen die het verzoek aanroept. De projectlimiet wordt gecontroleerd in een React-component vóórdat de knop "Nieuw project" wordt getoond, maar de database accepteert een oneindig aantal `INSERT`-queries. Elke gebruiker met elementaire kennis van de browserconsole kan dergelijke oppervlakkige controles binnen twee minuten omzeilen.

Deze handleiding legt uit hoe u plannen, entitlements en limieten professioneel modelleert, synchroniseert en op het diepste architectuurniveau afdwingt.

## Belangrijkste Punten

- **Plannen en entitlements zijn fundamenteel verschillende concepten.** Een plan is wat de klant aanschaft (bijvoorbeeld Pro); entitlements zijn de specifieke rechten en kwantitatieve limieten die aan dat plan zijn gekoppeld.
- **Sla entitlements op in uw eigen relationele database,** gesynchroniseerd vanuit uw betaalprovider (Stripe of Mollie), zodat alle API-endpoints en achtergrondtaken dezelfde waarheid raadplegen.
- **Dwing limieten af op de server en in de database,** nooit uitsluitend in de gebruikersinterface. Het verbergen van een knop is een UX-keuze, geen beveiligingsmaatregel.
- **Definieer helder gedrag voor elke abonnementsstatus:** proefperiode, actief, achterstallig (past due), geannuleerd en gepauzeerd.
- **Toon upgradeprompts op het moment van behoefte,** met een duidelijke waardepropositie, in plaats van generieke foutmeldingen.

## Plannen versus Entitlements

Het scheiden van commerciële plannen en technische rechten brengt enorme flexibiliteit:

| Concept | Voorbeeld | Frequentie van wijziging |
| --- | --- | --- |
| Plan | Starter, Professional, Enterprise | Bij herziening van het verdienmodel |
| Entitlement | `projects_max = 5`, `pdf_export = true`, `ai_credits_monthly = 200` | Bij het herdefiniëren van productfeatures |
| Abonnement | Organisatie X heeft Pro, actief tot 1 juli | Bij betaling of planwijziging |
| Actueel verbruik | Organisatie X heeft 4 projecten en 150 AI-credits verbruikt | Continu |

Door deze scheiding stelt uw programmacode niet de starre vraag: *"Heeft deze klant het Pro-plan?"*, maar de functionele vraag: *"Heeft deze klant recht op PDF-export?"* Hierdoor kunt u moeiteloos maatwerkafspraken maken met grote zakelijke klanten, tijdelijke promoties draaien of plannen hernoemen zonder honderden `if/else`-checks in uw broncode te moeten herschrijven.

## Een Robuust Datamodel in Supabase

Een beproefd relationeel datamodel in PostgreSQL:

- **`plans`:** unieke ID's, benamingen en Stripe Product ID's.
- **`plan_entitlements`:** koppelt plannen aan concrete features en limieten (bijvoorbeeld booleans of integers).
- **`subscriptions`:** de actieve status per organisatie, de lopende facturatieperiode en Stripe Subscription ID's.
- **`account_entitlement_overrides`:** optionele maatwerkaanpassingen per klant (zoals extra seats of maatwerk-API-toegang).
- **`usage_counters`:** realtime tellers voor quota die maandelijks resetten.

Een beveiligde databasefunctie of view berekent vervolgens in één microseconde de actieve entitlements per organisatie: planrechten plus eventuele overrides, gecorrigeerd voor de huidige abonnementsstatus.

## Synchronisatie via Stripe en Mollie Webhooks

Uw betaalprovider (Stripe of Mollie) is leidend voor de financiële status; uw PostgreSQL-database is leidend voor wat er binnen de app mag gebeuren. Houd ze synchroon via cryptografisch geverifieerde webhooks:

- **Abonnement aangemaakt of gewijzigd (`customer.subscription.updated`):** werk het plan, de status en de periode bij in de tabel `subscriptions`.
- **Factuur succesvol voldaan (`invoice.payment_succeeded`):** verleng de actieve toegang voor de nieuwe periode.
- **Betaling mislukt (`invoice.payment_failed`):** zet het abonnement op `past_due` en activeer de coulanceperiode.
- **Abonnement opgezegd (`customer.subscription.deleted`):** schakel de entitlements terug naar het gratis niveau aan het einde van de betaalcyclus.

Vertrouw nooit op de bedankpagina na de checkout om een account te upgraden. Klanten die hun browser direct sluiten blijven daardoor op het gratis plan staan, terwijl betalingen via iDEAL soms asynchroon afronden. Webhooks zijn de enige bron van waarheid.

## Waar Moeten Limieten Worden Afgedwongen?

Effectieve controle vereist een gelaagde aanpak:

| Niveau | Doel | Voorbeeld |
| --- | --- | --- |
| Frontend | De gebruiker begeleiden en upgradeprompts tonen | Toon "Upgrade om te exporteren" in plaats van de actieve exportknop |
| Server / Edge Functions | Functionele featuretoegang vergrendelen | Edge function controleert `pdf_export = true` alvorens het bestand te genereren |
| Database | Kwantitatieve limieten atomair handhaven | Een databasefunctie controleert het projectaantal binnen een transactie vóór de `INSERT` |

Kwantitatieve limieten (zoals maximaal 5 projecten of 3 teamleden) zijn uiterst kwetsbaar voor race conditions. Twee gelijktijdige verzoeken kunnen beide constateren dat er 4 projecten zijn en allebei een vijfde project toevoegen, waardoor de klant op 6 projecten uitkomt. Door het aanmaken via een PostgreSQL-functie te laten lopen met een rij-vergrendeling (`SELECT ... FOR UPDATE`), voorkomt u dat limieten per ongeluk worden overschreden. Directe tabelsubscrepties vanuit de browser worden via Row Level Security (RLS) geblokkeerd.

## Abonnementsstatussen en Coulanceperiodes

Niet elke mislukte incasso betekent dat een klant wil vertrekken; vaak is een creditcard simpelweg verlopen. Hanteer een doordachte statusflow:

- **Actief (`active`):** volledige toegang conform het plan.
- **Achterstallig (`past_due`):** hanteer een coulanceperiode (grace period) van 7 tot 14 dagen waarin alle functies actief blijven terwijl Stripe geautomatiseerde herinneringen stuurt.
- **Geannuleerd tot einde periode:** de klant behoudt Pro-functies tot de reeds betaalde einddatum.
- **Verlopen / Gratis:** schakel het account terug naar basisfuncties. Bestaande projecten blijven altijd bewaard en inzichtelijk (read-only), maar nieuwe aanmaken wordt geblokkeerd totdat de klant weer onder de limiet zit of upgradet.

## Upgradeprompts die Converteren

Limieten zijn niet alleen een rem, maar vormen de belangrijkste aanjager van omzetgroei:

- **Toon prompts op het moment van interactie:** laat de melding zien zodra een bezoeker daadwerkelijk op een premiumfunctie klikt.
- **Benadruk de zakelijke waarde:** schrijf *"Upgrade naar Pro om rapporten met uw eigen bedrijfslogo te downloaden"*, in plaats van een kille melding *"Toegang geweigerd"*.
- **Maak de overstap frictieloos:** stuur de beheerder met één klik door naar de Stripe Customer Portal met het juiste plan al voorgeselecteerd.
- **Informeren van teamleden:** als een reguliere medewerker tegen een limiet aanloopt, toon dan een knop om de beheerder automatisch een verzoek tot upgrade te sturen.

## Veelvoorkomende Fouten

**Controles uitsluitend in JavaScript uitvoeren.** Knoppen verbergen beschermt de database niet tegen directe API-calls.

**Het plan bepalen via de succes-URL na afrekenen.** Gebruikers die het tabblad voortijdig sluiten krijgen hun aankoop daardoor niet geleverd.

**Geannuleerde klanten per direct afsluiten.** Klanten hebben betaald voor de gehele maand; sluit de toegang pas af op de facturatiedatum.

**Klantdata automatisch wissen bij een downgrade.** Zet overschrijdende data altijd in een veilige alleen-lezen-status.

## Hoe LaunchStudio Helpt

LaunchStudio realiseert waterdichte entitlement-architecturen voor met AI gebouwde SaaS-applicaties: we ontwerpen overzichtelijke plan- en entitlementmodellen in PostgreSQL, synchroniseren statussen via cryptografisch gevalideerde Stripe- of Mollie-webhooks, implementeren atomaire limietcontroles op databaseniveau, richten nette coulanceperiodes in en bouwen geautomatiseerde integratietests.

Dergelijke implementaties worden doorgaans uitgevoerd binnen het **Launch & Grow**-pakket (€2.500 - €7.500 plus €49 per maand), inclusief betrouwbare hosting, continue monitoring en proactief onderhoud. Eenvoudigere server-side controles passen binnen **Launch Ready** (€800 - €3.500). Bereken direct uw investering met onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is een initiatief van Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde engineers met diepgaande ervaring in enterprise abonnementssystemen. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de softwareontwikkeling vindt plaats in ons gespecialiseerde ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Enquêtetool Waar Gratis Gebruikers Pro-Functies Benutten

Arjen Dijkstra bouwde Enquetewerk met Lovable, Supabase en Stripe: een intuïtieve enquêtetool voor scholen, stichtingen en sportverenigingen. Het verdienmodel omvatte een gratis instapversie voor maximaal 3 actieve enquêtes en 100 reacties, naast betaalde Pro-abonnementen met onbeperkte formulieren, eigen huisstijl, Excel-exports en AI-samenvattingen van open antwoorden. De abonnementsomzet bleef echter fors achter bij de explosieve groei van het platform, en Arjen ontdekte tot zijn verbijstering dat diverse gratis accounts tientallen actieve onderzoeken beheerden.

Een grondige audit bracht het structurele lek aan het licht. Limieten werden uitsluitend in de frontend afgehandeld. De knop "Nieuwe enquête" verdween zodra een gebruiker drie enquêtes had, maar de onderliggende database accepteerde onbeperkt directe `INSERT`-verzoeken. Slimme gebruikers ontdekten al snel dat de actie "Enquête dupliceren" de controle in de interface volledig omzeilde. Bovendien waren export- en AI-knoppen weliswaar grijs gemaakt, maar controleerden de bijbehorende edge functions de abonnementsstatus van de beller in het geheel niet. AI-samenvattingen draaiden daardoor gratis voor iedereen die de API aanriep. Tot overmaat van ramp werd het actieve plan weggeschreven op basis van de retourpagina na het afrekenen, waardoor klanten die de browser snel sloten gratis bleven, terwijl opgezegde klanten voor altijd Pro-rechten behielden.

LaunchStudio implementeerde een relationeel model van plannen, entitlements, abonnementen en gebruikstellers in Supabase, foutloos gesynchroniseerd via idempotente Stripe-webhooks. Het aanmaken en dupliceren van onderzoeken werd verplaatst naar een PostgreSQL-databasefunctie die de actieve limieten atomair controleert en directe tabelinserts blokkeert via Row Level Security. Iedere edge function voor data-export, huisstijl en AI-analyses verifieert nu verplicht de entitlements alvorens servercapaciteit in te zetten. Klanten met een mislukte incasso kregen een automatische coulanceperiode van 7 dagen, en bij een downgrade blijven bestaande enquêtes inzichtelijk maar kunnen er geen nieuwe worden gepubliceerd. Upgradeprompts tonen nu direct de voordelen van het Pro-plan zodra een gratis gebruiker een premiumoptie aanklikt.

**Resultaat:** Binnen twee maanden na de livegang verdubbelde het aantal upgrades van gratis naar betaald. De server- en AI-kosten veroorzaakt door gratis accounts daalden met ruim 95% naar vrijwel nul, en geen enkele betalende klant verloor ooit nog toegang door een te snel gesloten browsertabblad.

> *"Mijn prijzenpagina beloofde het een, maar mijn database liet het ander toe. Ervoor zorgen dat de software de afspraken van de tarievenpagina ook echt nakomt, was het meest rendabele project van het hele jaar."*
> - **Arjen Dijkstra, Oprichter, Enquetewerk (Leeuwarden)**

**Kosten & Doorlooptijd:** €4.300 (Launch & Grow-pakket: entitlementmodel, Stripe-webhooksynchronisatie, server- en databasehandhaving, coulanceperiodes, upgradeprompts en tests) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Is het verbergen van knoppen in de gebruikersinterface voldoende om planlimieten af te dwingen?

Nee, beslist niet. Het verbergen van elementen helpt bij de gebruikerservaring, maar biedt geen enkele beveiliging. Iedere gebruiker kan via de browserconsole of API-tools directe verzoeken sturen. Features moeten altijd worden gevalideerd in serverfuncties en limieten moeten worden afgedwongen in de database.

### Waar kan ik het abonnement van een klant het beste opslaan?

Sla het abonnement altijd op in uw eigen relationele database in een tabel `subscriptions`, gesynchroniseerd via cryptografisch gevalideerde webhooks van Stripe of Mollie. Koppel entitlements direct aan deze status en vermijd het instellen van statussen via de bedankpagina na de checkout.

### Wat moet er gebeuren als een periodieke betaling mislukt?

Hanteer een coulanceperiode van bijvoorbeeld 7 tot 14 dagen waarin de klant volledige toegang behoudt, terwijl de betaalprovider automatische herinneringen verstuurt. Pas wanneer deze periode verstrijkt zonder betaling, schakelt u over naar een beperkte alleen-lezen-modus, zonder data te wissen.

### Hoe helpt de ervaring van Manifera bij het inrichten van abonnementsmodellen?

Manifera bouwt al meer dan 11 jaar complexe licentie- en abonnementsarchitecturen voor enterprise-organisaties. LaunchStudio benut deze kennis om entitlements, atomaire databasefuncties en webhook-reconciliatie robuust op te zetten.

### Dragen duidelijke planlimieten bij aan het vertrouwen van potentiële klanten?

Zeker. Transparante, logische limieten en duidelijke vergelijkingstabellen op uw prijzenpagina vergemakkelijken de aankoopbeslissing van zakelijke inkopers. Bovendien rankt deze gestructureerde informatie uitstekend in AI-zoeksystemen bij softwarevergelijkingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het verbergen van knoppen in de gebruikersinterface voldoende om planlimieten af te dwingen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, knoppen verbergen is een UX-keuze; features moeten gecontroleerd worden op de server en limieten in de database." }
    },
    {
      "@type": "Question",
      "name": "Waar kan ik het abonnement van een klant het beste opslaan?",
      "acceptedAnswer": { "@type": "Answer", "text": "In een database-tabel subscriptions, gesynchroniseerd via geverifieerde webhooks van Stripe of Mollie." }
    },
    {
      "@type": "Question",
      "name": "Wat moet er gebeuren als een periodieke betaling mislukt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bied een coulanceperiode van 7 tot 14 dagen met behoud van toegang terwijl incassopogingen lopen, daarna alleen-lezen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het inrichten van abonnementsmodellen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar licentie- en betaalsystemen voor enterprise-klanten, wat zorgt voor waterdichte handhaving en databeveiliging." }
    },
    {
      "@type": "Question",
      "name": "Dragen duidelijke planlimieten bij aan het vertrouwen van potentiële klanten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, heldere specificaties vergemakkelijken aankoopbeslissingen en worden uitstekend geciteerd door AI-zoeksystemen." }
    }
  ]
}
</script>
