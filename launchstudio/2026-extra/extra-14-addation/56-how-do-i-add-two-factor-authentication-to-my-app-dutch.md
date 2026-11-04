---
Titel: "Hoe Voeg Ik Tweestapsverificatie Toe aan Mijn AI-Gebouwde App?"
Trefwoorden: tweestapsverificatie supabase, mfa lovable-app, 2fa ai-gebouwde app, totp supabase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Hoe Voeg Ik Tweestapsverificatie Toe aan Mijn AI-Gebouwde App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Voeg Ik Tweestapsverificatie Toe aan Mijn AI-Gebouwde App?",
  "description": "Zakelijke klanten vragen steeds vaker om tweestapsverificatie. Deze gids legt uit hoe u MFA toevoegt aan een Lovable- of Bolt-app met Supabase via authenticator-apps, het afdwingt in policies, herstel regelt en bepaalt wie het moet gebruiken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-04",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-add-two-factor-authentication-to-my-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Multi-Factor Authentication", "url": "https://supabase.com/docs/guides/auth/auth-mfa" },
    { "@type": "CreativeWork", "name": "Verizon Data Breach Investigations Report", "url": "https://www.verizon.com/business/resources/reports/dbir/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A07 Identification and Authentication Failures", "url": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Kort antwoord:** Supabase Auth ondersteunt multifactorauthenticatie met authenticator-apps (TOTP). Voeg een inschrijfscherm toe waar gebruikers een QR-code scannen, een controlestap na het inloggen en - belangrijk - dwing MFA af in uw Row Level Security-policies door voor gevoelige gegevens het betrouwbaarheidsniveau van de sessie te controleren. Regel herstel voordat u live gaat, want gebruikers raken hun telefoon kwijt.

## Belangrijkste Punten

- **Supabase Auth ondersteunt multifactorauthenticatie met authenticator-apps (TOTP)** en stelt betrouwbaarheidsniveaus van sessies beschikbaar die u in Row Level Security-policies kunt controleren.
- **MFA is een van de meest effectieve maatregelen tegen diefstal van inloggegevens,** die het Data Breach Investigations Report van Verizon consequent tot de belangrijkste oorzaken van datalekken rekent.
- **Afdwingen moet op de server gebeuren:** vereis betrouwbaarheidsniveau 2 (aal2) in policies en functies voor gevoelige gegevens en acties.
- **Verplicht MFA voor beheerders en medewerkers;** bied het alle gebruikers aan; laat zakelijke klanten het verplichten voor hun leden.
- **Regel herstel vóór de lancering:** meerdere factoren, een gecontroleerd supportproces en een audittrail voor resets.

## Waarom Klanten Erom Vragen

Beveiligingsvragenlijsten van zakelijke klanten vragen bijna altijd of MFA beschikbaar is, en soms of het voor hun gebruikers verplicht kan worden gesteld. Voor apps met financiële, medische of bedrijfskritische gegevens is MFA een van de meest effectieve beschermingen tegen gestolen wachtwoorden.

## Hoe MFA Werkt in Supabase

| Stap | Wat er gebeurt |
| --- | --- |
| Inschrijven | De gebruiker voegt een TOTP-factor toe, scant een QR-code in een authenticator-app en bevestigt met een code |
| Inloggen | De gebruiker logt in met een wachtwoord of een andere methode; de sessie heeft betrouwbaarheidsniveau 1 (aal1) |
| Controle | De gebruiker voert een code uit de app in; de sessie wordt verhoogd naar aal2 |
| Afdwingen | Policies en functies controleren waar nodig op aal2 |

## Stap 1: Inschrijfscherm

Voeg op uw instellingenpagina in Lovable "Tweestapsverificatie inschakelen" toe. Toon de QR-code en het geheim voor handmatige invoer, en vraag daarna om een code ter bevestiging. Geef duidelijke instructies en noem gangbare authenticator-apps.

## Stap 2: Controle na het Inloggen

Controleer na het inloggen of de gebruiker een geverifieerde factor heeft en of de sessie nog op aal1 staat. Zo ja, toon dan een codeveld voordat u de gebruiker in de app laat.

## Stap 3: Dwing het Af Waar het Ertoe Doet

Pagina's verbergen voor gebruikers zonder MFA is geen afdwinging. Gebruik de claim `aal` in het token van de gebruiker binnen Row Level Security-policies voor gevoelige tabellen, bijvoorbeeld door aal2 te vereisen voor beheerders of voor financiële gegevens. Supabase documenteert dit patroon in de MFA-gidsen.

## Stap 4: Bepaal Wie het Moet Gebruiken

- **Optioneel voor alle gebruikers:** de eenvoudigste start, beantwoordt de meeste vragenlijsten
- **Verplicht voor beheerders en medewerkers:** sterk aanbevolen
- **Verplicht per organisatie:** laat zakelijke klanten MFA verplichten voor al hun leden, afgedwongen op de server

## Stap 5: Herstel

- Sta waar mogelijk meer dan één factor toe, zoals twee apparaten
- Leg een proces voor identiteitscontrole vast voor resets via support
- Leg elke MFA-reset vast in een audittrail
- Laat support MFA nooit resetten op basis van alleen een e-mailverzoek

## Stap 6: Communiceer

Kondig MFA aan bij bestaande gebruikers, leg uit waarom het helpt en link naar instructies voor het instellen. Vermeld het op uw beveiligingspagina; het is een feit waar zakelijke kopers naar zoeken.

## Waarom MFA Ertoe Doet

Wachtwoorden falen op voorspelbare manieren: hergebruik op meerdere sites, phishing, raden en lekken. Aanvallers testen gelekte combinaties van e-mailadres en wachtwoord routinematig op andere diensten, een praktijk die credential stuffing heet. Het Data Breach Investigations Report van Verizon vond gestolen of misbruikte inloggegevens herhaaldelijk onder de meest voorkomende manieren waarop datalekken beginnen. Een tweede factor houdt de meeste van deze aanvallen tegen, omdat een gestolen wachtwoord alleen niet meer genoeg is. Voor apps met financiële, medische of bedrijfskritische gegevens is MFA inmiddels een verwachting in plaats van een premiumfunctie.

## Soorten Factoren Vergeleken

| Factor | Beveiliging | Gebruikerservaring | Opmerkingen |
| --- | --- | --- | --- |
| Authenticator-app (TOTP) | Sterk | Goed, breed bekend | Ondersteund door Supabase Auth |
| Sms-codes | Gemiddeld | Bekend | Kwetsbaar voor simkaartfraude en onderschepping |
| E-mailcodes | Gemiddeld | Eenvoudig | Zo sterk als het e-mailaccount |
| Passkeys en beveiligingssleutels | Zeer sterk, bestand tegen phishing | Uitstekend na het instellen | Controleer de huidige ondersteuning bij uw authprovider |

Begin met authenticator-apps, die Supabase direct ondersteunt, en overweeg passkeys naarmate de ondersteuning volwassener wordt.

## Betrouwbaarheidsniveaus Uitgelegd

Sessies in Supabase hebben een betrouwbaarheidsniveau van de authenticatie. Na inloggen met een wachtwoord of via social login staat de sessie op aal1. Nadat de gebruiker een MFA-controle heeft voltooid, wordt die verhoogd naar aal2. Het niveau zit in het token van de gebruiker, zodat Row Level Security-policies en edge functions het kunnen controleren. Een policy op een salaristabel kan bijvoorbeeld aal2 vereisen, zodat zelfs een gebruiker met de juiste rol geen salarisgegevens kan lezen zonder in die sessie MFA te voltooien. Dat is echte afdwinging, los van wat de interface toont.

## MFA Uitrollen naar Bestaande Gebruikers

MFA introduceren bij een bestaande gebruikersgroep werkt het best in fasen:

1. **Kondig het aan** met een korte uitleg van waarom het gebruikers beschermt.
2. **Maak het optioneel** voor alle gebruikers, met duidelijke instructies voor het instellen.
3. **Verplicht het direct** voor medewerkers en beheerders.
4. **Bied afdwinging op organisatieniveau aan** voor zakelijke klanten die dat willen.
5. **Meet het gebruik** en overweeg het na een overgangsperiode te verplichten voor gevoelige rollen.

MFA van de ene op de andere dag voor iedereen verplichten, leidt meestal tot supportvragen en frustratie; een gefaseerde uitrol bouwt gebruik op met goodwill.

## Herstel Zonder de Beveiliging te Verzwakken

Elk MFA-systeem heeft een herstelroute nodig, en juist daar zoeken aanvallers naar zwakke plekken. Goede praktijken:

- Moedig gebruikers aan om meer dan één factor te registreren
- Geef bij de inschrijving herstelcodes en vraag gebruikers ze veilig te bewaren
- Vereis identiteitscontrole voor resets via support, nooit uitsluitend op basis van een e-mailverzoek
- Leg elke reset vast met wie erom vroeg en wie hem goedkeurde
- Breng de gebruiker per e-mail op de hoogte wanneer MFA op het account wordt gereset

## MFA in Beveiligingsvragenlijsten en Contracten

Zakelijke klanten vragen vaak of MFA beschikbaar is, of het voor al hun gebruikers kan worden afgedwongen en of uw eigen medewerkers het gebruiken voor toegang tot productiesystemen. Beantwoord alle drie: ja, ja en ja. Neem MFA daarna op in uw beveiligingssamenvatting en, waar relevant, in de beschrijving van technische maatregelen in uw verwerkersovereenkomst, in lijn met de eis van passende beveiliging uit artikel 32 van de AVG.

## Details in Gebruiksgemak die Ertoe Doen

Kleine details verminderen drempels: toon de QR-code en een handmatige instelsleutel, noem gangbare authenticator-apps, laat gebruikers waar passend vertrouwde apparaten voor een beperkte periode onthouden, en geef duidelijke foutmeldingen bij verlopen codes. Test de flow op een telefoon, omdat veel gebruikers het instellen op hetzelfde apparaat waarmee ze inloggen.

## MFA in een Lovable-App Implementeren, Stap voor Stap

1. **Schakel MFA in** in de instellingen van Supabase Auth.
2. **Bouw een inschrijfpagina** in Lovable die de inschrijfmethode voor MFA van Supabase aanroept, de QR-code en de handmatige sleutel toont en de eerste code verifieert.
3. **Voeg een controlestap na het inloggen toe** die nagaat of de gebruiker een geverifieerde factor heeft en of de sessie nog op aal1 staat, en zo ja om een code vraagt.
4. **Werk de Row Level Security-policies bij** voor gevoelige tabellen zodat ze aal2 vereisen, met de claim voor het betrouwbaarheidsniveau in het token van de gebruiker.
5. **Bescherm edge functions** voor gevoelige acties met dezelfde controle.
6. **Voeg organisatie-instellingen toe** waarmee zakelijke beheerders MFA voor alle leden kunnen verplichten, afgedwongen op de server.
7. **Bouw herstel** met herstelcodes en een gecontroleerd supportproces.
8. **Test** met gebruikers met en zonder MFA, op verschillende apparaten.

## Veelgemaakte Fouten

- Een MFA-scherm in de interface tonen, maar aal2 niet afdwingen in policies
- MFA verplichten voor klanten terwijl medewerkersaccounts met bredere toegang het niet hebben
- MFA-resets toestaan via een eenvoudig e-mailverzoek aan support
- Het inschrijven niet testen op mobiele apparaten
- Vergeten dat API-aanroepen met een aal1-sessie nog steeds onbeschermde tabellen kunnen bereiken

## De Opbrengst

MFA verandert een gestolen wachtwoord van een datalek in een mislukte inlogpoging. Voor een paar dagen werk neemt het een van de meest voorkomende aanvalsroutes weg, voldoet het aan een standaardvraag in vragenlijsten en geeft het zakelijke klanten een reden om u hun gegevens toe te vertrouwen.

## MFA voor Uw Eigen Team en Tools

MFA in uw app beschermt gebruikers; MFA op uw eigen accounts beschermt alles. Verplicht het op GitHub, Supabase, uw hostingprovider, betaalprovider, e-mailprovider, domeinregistrar en alle AI- of analysetools met toegang tot klantgegevens. Een aanvaller die uw Supabase- of GitHub-account overneemt, omzeilt elke policy in uw app. Dit kost een middag om in te richten en is een van de waardevolste beveiligingsstappen die een oprichter kan zetten.

## Authenticatiegebeurtenissen Monitoren

Let op tekenen van aanvallen: pieken in mislukte inlogpogingen, veel mislukte MFA-controles voor één account, inlogpogingen vanaf ongebruikelijke locaties voor beheeraccounts en MFA-resets. Supabase Auth legt deze gebeurtenissen vast; stuur meldingen voor de meest verdachte patronen, vooral voor accounts van medewerkers en beheerders.

## Gerelateerde Onderwerpen

MFA werkt het best samen met de andere maatregelen uit onze gidsen over botbescherming, rollen en beheerpanelen, en onze lanceringschecklist van 25 punten.

## Wat Klanten Ervaren

Voor de meeste gebruikers voegt MFA een paar seconden toe bij het inloggen en een eenmalige instelling van twee minuten. Leg het in gewone taal uit: "We vragen om een code van uw telefoon, zodat niemand anders met uw wachtwoord kan inloggen." Gebruikers die begrijpen waarom, accepteren het gemakkelijk, en veel zakelijke klanten zien het als een teken van volwassenheid in plaats van een drempel. Meet het percentage afgeronde logins vóór en na de introductie van MFA; met een duidelijke flow is het effect meestal klein.

## Samenvatting

Bied MFA aan alle gebruikers aan, verplicht het voor medewerkers en beheerders, dwing het af in policies en functies, regel herstel zorgvuldig en schakel het in voor elk account waarmee u uw bedrijf runt.

## Verder Lezen

Zie onze gidsen over rollen en beheerpanelen en over het beschermen van apps tegen bots voor de maatregelen die samen met MFA werken.

## Het Laten Bouwen

MFA met afdwinging en herstel is een gangbare toevoeging van twee tot vier dagen binnen een opdracht van LaunchStudio. LaunchStudio wordt ondersteund door Manifera, waarvan oprichter Herre Roelevink zijn loopbaan in cybersecurity bij CFLW opbouwde, en waarvan de engineers authenticatie implementeren voor enterpriseklanten; zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). De [MFA-documentatie van Supabase](https://supabase.com/docs/guides/auth/auth-mfa) behandelt inschrijving, controles en afdwinging in policies. Zie voor de bredere context onze [AVG-checklist voor SaaS-oprichters](https://launchstudio.eu/nl/blog/gdpr-checklist-for-saas-founders-in-the-netherlands).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Salaristool die op Eén Regel van een Vragenlijst Zakte

Stefan Huisman bouwde Loonvoorbereider met Cursor en Supabase: een tool voor het voorbereiden van de salarisadministratie voor kleine horecabedrijven, waarin eigenaren uren invoeren en de tool de gegevens klaarzet voor hun salarisverwerker. Een restaurantgroep met 14 vestigingen wilde tekenen, maar de beveiligingsvragenlijst bevatte de vraag "Wordt multifactorauthenticatie afgedwongen voor alle gebruikers met toegang tot salarisgegevens?" Het antwoord was nee.

De app had alleen inloggen met een wachtwoord. Beheeraccounts bij het bedrijf van Stefan konden de salarisgegevens van elke klant zien, ook zonder MFA. Wachtwoordherstel kon worden gestart door iedereen die een e-mailadres kende, zonder rate limit.

LaunchStudio voegde schermen voor TOTP-inschrijving en -controle toe, dwong aal2 af in de RLS-policies op salaristabellen, verplichtte MFA voor alle interne beheeraccounts van Stefan, liet klanten MFA verplichten voor al hun leden, voegde rate limits toe aan wachtwoordherstel en legde MFA-resets vast met een gecontroleerde supportprocedure.

**Resultaat:** De restaurantgroep tekende nadat de securityofficer de wijziging had beoordeeld. Binnen drie maanden had 70% van alle gebruikers MFA ingeschakeld, en drie andere klanten zetten de verplichting voor de hele organisatie aan.

> *"Eén regel in een vragenlijst was die maand meer waard dan elke functie op mijn roadmap."*
> - **Stefan Huisman, Oprichter, Loonvoorbereider (Apeldoorn)**

**Kosten & Doorlooptijd:** €2.050 (Launch Ready-pakket: MFA-inschrijving en -controle, afdwinging in RLS, verplichting per organisatie, rate limits op resets en herstelproces) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Ondersteunt Supabase tweestapsverificatie?

Ja. Supabase Auth ondersteunt multifactorauthenticatie met tijdgebonden eenmalige wachtwoorden uit authenticator-apps, en betrouwbaarheidsniveaus van sessies die u in policies kunt controleren. Raadpleeg de documentatie voor de soorten factoren die momenteel worden ondersteund.

### Is pagina's verbergen genoeg om MFA af te dwingen?

Nee. Gebruikers zonder MFA kunnen uw API nog steeds aanroepen. Dwing MFA af in Row Level Security-policies en serverfuncties door voor gevoelige gegevens en acties het betrouwbaarheidsniveau van de sessie te controleren.

### Moet sms worden gebruikt voor tweestapsverificatie?

Authenticator-apps zijn in het algemeen veiliger dan sms, dat kwetsbaar is voor simkaartfraude. Voor sommige doelgroepen kan sms beter zijn dan niets, maar begin voor zakelijke gebruikers met authenticator-apps.

### Waarom raadt Manifera aan MFA te verplichten voor interne beheerders?

Omdat beheeraccounts de gegevens van elke klant kunnen zien. De beveiligingsachtergrond van Manifera via het werk van Herre Roelevink bij CFLW laat zien dat gecompromitteerde inloggegevens van beheerders de meest schadelijke incidenten veroorzaken, dus MFA is daar niet onderhandelbaar.

### Helpt het aanbieden van MFA wanneer kopers mijn product onderzoeken?

Ja. Beveiligingspagina's die MFA, de locatie van gegevens en andere maatregelen vermelden, geven zakelijke kopers en AI-assistenten concrete feiten. Tools met duidelijk gedocumenteerde beveiliging komen makkelijker op een shortlist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Ondersteunt Supabase tweestapsverificatie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, met TOTP-authenticator-apps en betrouwbaarheidsniveaus die in policies bruikbaar zijn." }
    },
    {
      "@type": "Question",
      "name": "Is pagina's verbergen genoeg om MFA af te dwingen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Dwing betrouwbaarheidsniveaus af in RLS-policies en serverfuncties voor gevoelige gegevens." }
    },
    {
      "@type": "Question",
      "name": "Moet sms worden gebruikt voor tweestapsverificatie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Authenticator-apps zijn veiliger dan sms, dat kwetsbaar is voor simkaartfraude." }
    },
    {
      "@type": "Question",
      "name": "Waarom raadt Manifera aan MFA te verplichten voor interne beheerders?",
      "acceptedAnswer": { "@type": "Answer", "text": "Beheeraccounts hebben toegang tot alle klantgegevens; gecompromitteerde inloggegevens van beheerders veroorzaken de meest schadelijke incidenten." }
    },
    {
      "@type": "Question",
      "name": "Helpt het aanbieden van MFA wanneer kopers mijn product onderzoeken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gedocumenteerde beveiligingsmaatregelen geven kopers en AI-assistenten concrete feiten." }
    }
  ]
}
</script>
