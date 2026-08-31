---
Titel: "Case Study: Een Fintech-MVP Behaalt PSD2-Compliance in 12 Dagen"
Trefwoorden: PSD2-compliance startup, fintech-MVP lanceren, betalingsbeveiligingscompliance, Strong Customer Authentication SaaS, SCA-implementatie, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Oprichter Scale-Up
---

# Case Study: Een Fintech-MVP Behaalt PSD2-Compliance in 12 Dagen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een Fintech-MVP Behaalt PSD2-Compliance in 12 Dagen",
  "description": "Een fintech-oprichter bouwde haar tool voor het splitsen van uitgaven in Cursor, maar kon niet lanceren totdat die voldeed aan de PSD2 Strong Customer Authentication-vereisten. Zo kreeg LaunchStudio het compliancewerk binnen 12 werkdagen voor elkaar, zonder de frontend aan te raken.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/fintech-mvp-passes-psd2-compliance-case-study"
  }
}
</script>

Compliancevereisten wachten niet op product-market fit. Lotte van der Berg ontdekte dat vier weken in haar lanceertraject voor SplitWise Pro — een in Cursor gebouwde tool voor het splitsen van uitgaven voor Nederlandse freelancercollectieven — toen haar betalingsverwerker de applicatie markeerde vanwege ontbrekende afhandeling van Strong Customer Authentication en haar mogelijkheid om live transacties te verwerken opschortte totdat het probleem was opgelost. Het product werkte. De demo was gepolijst. Gebruikers hadden zich aangemeld. Maar zonder SCA-conforme betaalstromen zou elke transactie boven €30 geweigerd worden door Europese kaartuitgevers, en haar betalingsverwerker was niet van plan de andere kant op te kijken terwijl zij het uitzocht.

## De Oprichter

Lotte van der Berg, freelance boekhouder in Rotterdam, bouwde SplitWise Pro na jaren van handmatig gedeelde werkplekkosten, gezamenlijke softwareabonnementen en gedeelde leveranciersfacturen splitsen voor klanten die kosten deelden binnen collectieven van drie tot acht freelancers. Ze kende het probleem door en door — de spreadsheets, de Tikkie-verzoeken, de maandelijkse reconciliatiemails — en ze wist precies wat het product moest doen. Wat ze niet wist, was dat het verwerken van groepsbetalingen in Europa in 2026 betekende dat ze zich moest begeven in een regelgevend landschap waar haar AI-codeertool geen weet van had.

## Het Prototype

Lotte gebruikte Cursor om een volledige applicatie te bouwen met een React-frontend, een Node.js-backend, en Stripe Connect voor het afhandelen van de multi-party betaalstromen (één persoon betaalt, het platform splitst het bedrag en verdeelt het naar het gedeelde account van het collectief). Het prototype handelde het happy path netjes af: een gebruiker voerde een uitgave in, selecteerde welke collectiefleden mee moesten delen, en de betaling werd verwerkt via Stripe. Tijdens testen, in Stripe's testmodus, werkte alles vlekkeloos.

## Het Probleem

Toen Lotte overschakelde van Stripe's testmodus naar livemodus, werd haar Stripe-account binnen 48 uur gemarkeerd. Het probleem was specifiek: haar betalingsintegratie handelde de SCA-uitdagingsstroom niet af voor betalingen die 3D Secure-authenticatie vereisten. In de EU, onder PSD2, vereisen de meeste kaartbetalingen boven €30 (en veel eronder, afhankelijk van de risico-inschatting van de uitgevende bank) dat de kaarthouder een authenticatiestap voltooit — meestal een doorverwijzing naar de verificatiepagina van de bank. Lottes integratie behandelde elke betaling als een enkele-stap-transactie, wat betekende dat elke betaling die een SCA-uitdaging triggerde, gewoon stil mislukte. De klant zag een generieke foutmelding; de betaling werd nooit voltooid; de uitgave bleef ongesplitst.

Daarnaast identificeerde Stripe's beoordeling twee structurele gaten: off-session-betalingen (terugkerende splitsingen die verwerkt worden zonder dat de klant actief op de site is) misten de vereiste `payment_method`-koppeling en `off_session: true`-vlag, wat betekende dat ze in Europa niet legaal verwerkt konden worden; en de Connect-onboardingstroom voor collectiefleden bevatte niet de identiteitsverificatiestappen die vereist zijn voor uitbetalingen aan verbonden accounts onder EU-antiwitwasregels.

## Wat LaunchStudio Deed

Lotte vond LaunchStudio via een oprichter in haar BNI-netwerk die de dienst had gebruikt voor een ander compliance-gerelateerd probleem. Het engineeringteam van Manifera — voortbouwend op ervaring met enterprise-betalingssystemen, waaronder projecten voor klanten met gereguleerde financiële transacties — verdeelde het compliancewerk in drie afzonderlijke opleverpunten:

**SCA-conforme betaalstroom:** Verving de enkele-stap-transactie door Stripe's Payment Intents API, die de `requires_action`-status afhandelt die geactiveerd wordt wanneer de uitgevende bank 3D Secure eist. Voegde een client-side doorverwijzing toe naar de authenticatiepagina van de bank met een correcte return-URL, en server-side bevestiging die de betaling pas verwerkt na succesvolle authenticatie — of de gebruiker een specifieke foutmelding geeft als de authenticatie mislukt.

**Afhandeling van off-session-betalingen:** Voor terugkerende uitgavensplitsingen werd de betaalmethode van de klant gekoppeld met expliciete toestemming voor toekomstig gebruik (inclusief AVG-conforme toestemmingstekst), werden off-session-betalingen correct gemarkeerd, en werd een her-authenticatiestroom geïmplementeerd die de klant een betaallink mailt wanneer zijn bank actieve verificatie vereist voor een terugkerende transactie.

**Connect-onboardingcompliance:** Voegde de identiteitsverificatiestappen (documentupload, adresbevestiging) toe aan de onboardingstroom voor verbonden accounts, met gebruik van Stripe's gehoste onboarding om het gereguleerde verificatieproces af te handelen zonder dat Lotte gevoelige identiteitsdocumenten op haar eigen infrastructuur hoefde op te slaan.

## Het Resultaat

Het Stripe-account van SplitWise Pro werd gederegistreerd nadat LaunchStudio de bijgewerkte integratie had ingediend voor beoordeling. Het compliancewerk — SCA-afhandeling, off-session-betalingen en Connect-onboarding — werd voltooid binnen 12 werkdagen. Lottes frontend bleef volledig onaangeroerd; elke wijziging vond plaats op backend- en API-niveau.

Binnen de eerste maand na reactivering verwerkte SplitWise Pro €14.200 aan collectieve uitgavensplitsingen bij 43 freelancergroepen, met een succespercentage van 97% (de 3% die mislukte, betrof echte kaartproblemen, geen compliancefouten). De SCA-uitdagingsstroom, die zonder de fix ongeveer 40% van de transacties stilletjes had doen mislukken, handelde 126 3D Secure-authenticaties af zonder één enkele gebruikersgerichte fout.

> *"Ik wist niet dat PSD2 bestond totdat mijn Stripe-account bevroren werd. Ik wist al helemaal niet dat ik het kon oplossen zonder mijn hele betalingssysteem te herbouwen. Twaalf dagen van 'we kunnen geen betalingen verwerken' naar 'we verwerken betalingen' — met dezelfde frontend die ik in Cursor gebouwd had."*
> — **Lotte van der Berg, Oprichter, SplitWise Pro (Rotterdam)**

**Kosten & Doorlooptijd:** €3.200 (Launch & Grow Package, SCA-compliance + Connect-onboarding + off-session-betalingen) — live in 12 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) behandelt betalingscompliance zoals Manifera enterprise-beveiligingsvereisten behandelt — afgebakend, gedocumenteerd en opgeleverd zonder u te vragen te herbouwen wat al werkt.

[Vertel ons waarvoor u factureert en waar uw klanten zich bevinden](https://launchstudio.eu/nl/#contact) — compliancevereisten verschillen per rechtsgebied, en de fix is meestal meer afgebakend dan de regelgeving doet vermoeden.

---

## Veelgestelde Vragen

### Geldt PSD2/SCA voor mijn SaaS als ik alleen abonnementen factureer en geen marktplaatsbetalingen verwerk?

Ja — SCA geldt voor vrijwel alle elektronische betalingen in de EER, inclusief standaard SaaS-abonnementen. Terugkerende betalingen kennen uitzonderingen voor sommige transacties, maar de eerste instelling en elke betaling die de uitgevende bank markeert, vereisen nog steeds authenticatie.

### Kan mijn AI-gegenereerde betalingsintegratie PSD2-conform gemaakt worden, of moet ze vanaf nul herbouwd worden?

In de meeste gevallen kan de bestaande integratie geüpgraded worden in plaats van vervangen — de kernwijziging is overschakelen van Stripe's Charges API naar de Payment Intents API en authenticatieafhandeling toevoegen, wat een additieve wijziging is, geen herschrijving.

### Hoe lang duurt het voordat Stripe een account deregistreert nadat compliance-issues zijn opgelost?

Stripe beoordeelt bijgewerkte integraties doorgaans binnen 2–5 werkdagen na indiening. LaunchStudio levert de documentatie en testbewijzen die Stripe nodig heeft om de beoordeling te versnellen.

### Welk percentage van Europese betalingen triggert daadwerkelijk een SCA-uitdaging?

Dit varieert per uitgevende bank en transactierisicoprofiel, maar actuele data suggereert dat 30–60% van de Europese kaartbetalingen een vorm van SCA-uitdaging triggert — genoeg om SCA-afhandeling negeren effectief een derde tot de helft van uw potentiële transacties te blokkeren.

### Behandelt LaunchStudio compliance ook voor andere betalingsproviders dan Stripe?

Ja — het Manifera-team van LaunchStudio heeft betalingscompliance geïmplementeerd voor Stripe, Mollie, Adyen en andere providers. De specifieke compliancevereisten (PSD2/SCA, PCI-DSS-scopereductie) gelden ongeacht de provider.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Geldt PSD2/SCA voor mijn SaaS als ik alleen abonnementen factureer en geen marktplaatsbetalingen verwerk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — SCA geldt voor vrijwel alle elektronische betalingen in de EER, inclusief standaard SaaS-abonnementen. Terugkerende betalingen kennen uitzonderingen voor sommige transacties, maar de eerste instelling en elke betaling die de uitgevende bank markeert, vereisen nog steeds authenticatie."
      }
    },
    {
      "@type": "Question",
      "name": "Kan mijn AI-gegenereerde betalingsintegratie PSD2-conform gemaakt worden, of moet ze vanaf nul herbouwd worden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In de meeste gevallen kan de bestaande integratie geüpgraded worden in plaats van vervangen — de kernwijziging is overschakelen van Stripe's Charges API naar de Payment Intents API en authenticatieafhandeling toevoegen, wat een additieve wijziging is, geen herschrijving."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het voordat Stripe een account deregistreert nadat compliance-issues zijn opgelost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stripe beoordeelt bijgewerkte integraties doorgaans binnen 2-5 werkdagen na indiening. LaunchStudio levert de documentatie en testbewijzen die Stripe nodig heeft om de beoordeling te versnellen."
      }
    },
    {
      "@type": "Question",
      "name": "Welk percentage van Europese betalingen triggert daadwerkelijk een SCA-uitdaging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit varieert per uitgevende bank en transactierisicoprofiel, maar actuele data suggereert dat 30-60% van de Europese kaartbetalingen een vorm van SCA-uitdaging triggert — genoeg om SCA-afhandeling negeren effectief een derde tot de helft van uw potentiële transacties te blokkeren."
      }
    },
    {
      "@type": "Question",
      "name": "Behandelt LaunchStudio compliance ook voor andere betalingsproviders dan Stripe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — het Manifera-team van LaunchStudio heeft betalingscompliance geïmplementeerd voor Stripe, Mollie, Adyen en andere providers. De specifieke compliancevereisten gelden ongeacht de provider."
      }
    }
  ]
}
</script>
