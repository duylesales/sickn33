---
Titel: "Hoe Voeg Ik Inloggen met Google Toe aan een Lovable-App?"
Trefwoorden: inloggen met google lovable, lovable oauth, supabase google inloggen, social login ai-app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Voeg Ik Inloggen met Google Toe aan een Lovable-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Voeg Ik Inloggen met Google Toe aan een Lovable-App?",
  "description": "Inloggen met Google in een Lovable-app loopt via Supabase Auth en een OAuth-client in Google Cloud. Deze gids behandelt de inrichting, redirect-URL's voor preview en productie, het toestemmingsscherm, het koppelen van accounts en de redenen waarom inloggen met Google na de lancering kapotgaat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-19",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-add-google-login-to-a-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Login with Google", "url": "https://supabase.com/docs/guides/auth/social-login/auth-google" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A07 Identification and Authentication Failures", "url": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/" }
  ]
}
</script>

**Kort antwoord:** maak een OAuth-client aan in Google Cloud, schakel de Google-provider in Supabase Auth in met de ID en het geheim van die client, voeg de callback-URL van Supabase toe aan Google, voeg de domeinen van uw app toe aan de toegestane redirect-URL's in Supabase, en roep vanaf de inlogpagina van uw Lovable-app het inloggen met Google van Supabase aan. In de preview werkt het binnen een uur. Het betrouwbaar laten werken in productie vraagt nog een paar beslissingen.

## Belangrijkste Punten

- **Inloggen met Google in een Lovable-app loopt via Supabase Auth** en een OAuth-client die u in Google Cloud aanmaakt.
- **De meeste fouten in productie zijn configuratie:** een toestemmingsscherm dat nog in testmodus staat, redirect-URL's die naar het previewdomein wijzen, of een redirect-URI die niet overeenkomt.
- **Beslis vóór de lancering over het koppelen van accounts,** zodat gebruikers die zich met e-mail registreren en later Google gebruiken niet met twee accounts eindigen.
- **Vraag alleen basale scopes** (e-mail en profiel) om extra verificatie te vermijden en om de dataminimalisatie onder de AVG te respecteren.
- **Bied altijd een alternatief via e-mail aan;** niet elke gebruiker heeft een Google-account of wil dat gebruiken.

## Overzicht van de Inrichting

| Waar | Wat u instelt |
| --- | --- |
| Google Cloud Console | OAuth-toestemmingsscherm, OAuth-client (webapplicatie), toegestane redirect-URI |
| Supabase Auth | Google-provider inschakelen, client-ID en geheim invoeren, site-URL en redirect-URL's instellen |
| Lovable-app | Knop "Doorgaan met Google" die het inloggen van Supabase aanroept |

De toegestane redirect-URI in Google wijst naar het callback-endpoint van Supabase voor uw project, niet naar uw app. Supabase stuurt daarna terug naar uw app, en daarom moeten de URL's van uw app op de lijst met toegestane redirects in Supabase staan.

## Waarom Het na de Lancering Kapotgaat

**Redirects naar de preview.** De site-URL in Supabase wijst nog naar de preview van Lovable, waardoor gebruikers na het inloggen op het verkeerde domein terechtkomen. Zet de site-URL op productie en vermeld preview-URL's apart.

**"redirect_uri_mismatch".** De redirect-URI die in Google is ingesteld, komt niet exact overeen met wat Supabase stuurt, vaak door een ander project of een typefout.

**Toestemmingsscherm in testmodus.** Zolang het toestemmingsscherm van Google in testmodus staat, kunnen alleen vermelde testgebruikers inloggen. Publiceer het vóór de lancering. Afhankelijk van de scopes die u vraagt, kan Google verificatie eisen, dus vraag alleen om basaal profiel en e-mail.

**Eigen domein voor Supabase.** Als u Supabase later naar een eigen domein verhuist, verandert de callback-URL en moet Google worden bijgewerkt.

## Beslissingen Vóór de Lancering

- **Accounts koppelen.** Als iemand zich met e-mail registreert en later Google gebruikt met hetzelfde adres, moet dat dan hetzelfde account zijn? Supabase kan identiteiten met hetzelfde geverifieerde e-mailadres koppelen; beslis en test het gedrag.
- **Profielen aanmaken.** Zorg dat er ook voor Google-gebruikers een profielrij wordt aangemaakt, meestal met een databasetrigger op nieuwe authenticatiegebruikers, niet alleen in de flow voor registratie met e-mail.
- **Zakelijke accounts.** Voor B2B kunt u het inloggen beperken tot bepaalde bedrijfsdomeinen of gebruikers op basis van het domein van hun e-mailadres aan organisaties koppelen, afgedwongen op de server.
- **Privacyverklaring.** Vermeld Google als inlogprovider en welke data u ontvangt.

## Testchecklist

1. Een nieuwe gebruiker logt in productie in met Google: profiel aangemaakt, komt op de juiste pagina terecht
2. Een bestaande gebruiker met e-mail logt in met Google: het gedrag komt overeen met uw beslissing over koppelen
3. Inloggen werkt in mobiele browsers en in browsers binnen apps
4. Uitloggen en opnieuw inloggen werkt zonder lussen
5. Een gebruiker buiten uw toegestane domeinen (als u beperkt) wordt geweigerd

## Hoe Inloggen via OAuth Stap voor Stap Werkt

Wie de flow begrijpt, kan problemen eenvoudig oplossen. Wanneer een gebruiker op "Doorgaan met Google" klikt:

1. Uw app vraagt Supabase het inloggen met Google te starten, inclusief waar hij daarna naartoe moet terugkeren.
2. Supabase stuurt de browser door naar het toestemmingsscherm van Google met de ID van uw OAuth-client.
3. De gebruiker kiest een account en keurt de gevraagde scopes goed.
4. Google stuurt door naar de callback-URL van Supabase met een autorisatiecode.
5. Supabase wisselt de code in voor de identiteit van de gebruiker, maakt de gebruiker aan of vindt hem, en geeft een sessie uit.
6. Supabase stuurt de browser terug naar uw app op een toegestane URL, waar de sessie wordt opgepakt.

Problemen bij stap 3 komen meestal door instellingen van het toestemmingsscherm. Problemen bij stap 4 meestal door de toegestane redirect-URI in Google Cloud. Problemen bij stap 6 meestal door de site-URL en de lijst met toegestane redirects in Supabase. De gids van Supabase over inloggen met Google en de documentatie over redirect-URL's beschrijven elke instelling.

## De Kant van Google Cloud Inrichten

In de Google Cloud Console richt u een OAuth-toestemmingsscherm in met de naam van uw app, een supportadres, een logo en links naar uw privacybeleid en voorwaarden. Daarna maakt u een OAuth-client van het type "webapplicatie" aan en voegt u de callback-URL van Supabase toe als toegestane redirect-URI. Een paar praktische opmerkingen:

- Gebruik een Google Cloud-project dat eigendom is van het account van uw bedrijf, geen persoonlijk project
- Houd de branding van het toestemmingsscherm gelijk aan die van uw app, zodat gebruikers het vertrouwen
- Publiceer het toestemmingsscherm vóór de lancering; in testmodus kunnen alleen vermelde testgebruikers inloggen
- Vraag de minimale scopes; extra gevoelige scopes starten het verificatieproces van Google

## De Kant van Supabase Inrichten

Schakel in de instellingen van Supabase Auth de Google-provider in en voer de client-ID en het geheim in. Zet de site-URL op uw productiedomein, en vermeld elke legitieme redirectbestemming: productie, staging en preview-URL's als u die gebruikt. Als uw app op meerdere subdomeinen draait, neem ze dan allemaal op. Bewaar het clientgeheim van Google alleen in Supabase; het mag nooit in frontendcode verschijnen.

## Profielen, Rollen en Organisaties voor Google-Gebruikers

Gebruikers die met Google inloggen, slaan uw registratieformulier over, dus alles wat dat formulier deed - een profielrij aanmaken, een standaardrol toekennen, aan een organisatie koppelen - moet ook voor hen gebeuren. De robuuste aanpak is een databasetrigger op nieuwe gebruikers die het profiel aanmaakt, plus logica op de server die het lidmaatschap van organisaties regelt, bijvoorbeeld via uitnodigingen. Test de ervaring van de eerste login voor een gloednieuwe Google-gebruiker; dat is het pad dat het vaakst kapot is.

## Inloggen Beperken voor Zakelijke Apps

Voor B2B-producten wilt u misschien dat alleen gebruikers van bepaalde bedrijven kunnen inloggen, of dat gebruikers op basis van het domein van hun e-mailadres in een organisatie worden geplaatst. Implementeer deze regels op de server: controleer het domein van het e-mailadres in een trigger of edge function, en weiger of verwijs door. Vertrouw er niet op dat u de Google-knop in de interface verbergt.

## Ook Microsoft en Apple Toevoegen

Zakelijke gebruikers hebben vaak een Microsoft-account; iPhone-gebruikers geven misschien de voorkeur aan Inloggen met Apple, wat Apple in sommige situaties in de App Store verplicht stelt als andere social logins worden aangeboden. Supabase ondersteunt beide met een vergelijkbare configuratie. Voeg ze toe op basis van uw doelgroep, niet standaard, en houd het koppelen van identiteiten consistent over providers.

## Privacy en Transparantie

Social login betekent dat Google, Microsoft of Apple gegevens over het inloggen verwerken. Vermeld elke provider in uw privacyverklaring, leg uit welke data u ontvangt (meestal naam, e-mailadres en profielfoto) en bewaar alleen wat u nodig heeft. Onder het AVG-beginsel van dataminimalisatie is er geen reden om voor authenticatie toegang tot agenda, contacten of Drive te vragen.

## Testen voor de Lancering

Test op desktop en in mobiele browsers, ook in browsers binnen apps zoals Instagram of LinkedIn, die OAuth-flows soms blokkeren of aanpassen. Test een nieuwe gebruiker, een terugkerende gebruiker, een gebruiker die zich eerder met e-mail registreerde, een gebruiker uit een geblokkeerd domein als u toegang beperkt, en uitloggen gevolgd door opnieuw inloggen. Deze tests kosten een half uur en vangen bijna elk probleem op de lanceringsdag.

## Veelvoorkomende Foutmeldingen en Wat Ze Betekenen

| Melding of symptoom | Waarschijnlijke oorzaak |
| --- | --- |
| "Access blocked: app has not completed verification" | Toestemmingsscherm in testmodus of gevoelige scopes gevraagd |
| "redirect_uri_mismatch" | Toegestane redirect-URI in Google komt niet overeen met de callback van Supabase |
| Terug op het previewdomein | Site-URL of redirectlijst in Supabase niet bijgewerkt |
| Ingelogd maar de app geeft fouten | Ontbrekende profielrij of rol voor nieuwe Google-gebruikers |
| Inloglus op mobiel | Problemen met redirect-URL of sessieopslag in browsers binnen apps |

## Beveiligingsoverwegingen bij Social Login

Social login verschuift de beveiliging van wachtwoorden naar Google, en dat is een sterkte: Google-accounts hebben vaak tweestapsverificatie en een sterke detectie van lekken. Het schept ook afhankelijkheden die u moet beheren. Als een gebruiker de toegang tot zijn Google-account verliest, verliest hij de toegang tot uw app, tenzij er een alternatief is; bied herstel via e-mail aan. Als iemands Google-account wordt gecompromitteerd, is uw app ook blootgesteld; overweeg voor gevoelige apps uw eigen tweede factor te vereisen voor beheerders. De richtlijnen van OWASP over fouten in identificatie en authenticatie gelden ongeacht de provider: bescherm sessies, handel uitloggen goed af en voorkom dat tokens in URL's of logs lekken.

## Effecten op Conversie

Social login verlaagt meestal de drempel bij het registreren, vooral op mobiel, waar wachtwoorden typen omslachtig is. Meet het in plaats van het aan te nemen: vergelijk enkele weken lang de afrondingspercentages voor de Google-knop en het e-mailformulier. Sommige B2B-doelgroepen verkiezen Microsoft; sommige privacybewuste doelgroepen vermijden social login helemaal. Uw eigen data laat zien welke opties een prominente plek verdienen.

## Het na de Lancering Werkend Houden

OAuth-configuraties gaan stil kapot wanneer domeinen veranderen. Werk, telkens wanneer u een domein toevoegt, naar een eigen domein voor Supabase verhuist, van hosting verandert of een nieuwe omgeving lanceert, zowel de toegestane redirect-URI's in Google als de redirectlijst in Supabase bij, en test daarna het inloggen op de nieuwe URL. Eén regel in uw checklist voor deployment voorkomt een verrassend vaak voorkomende storing.

## Wanneer Inloggen met Google Niet Genoeg Is

Sommige klanten zullen vragen om single sign-on via hun eigen identiteitsprovider, zoals Microsoft Entra ID of Okta, zodat hun IT-afdeling de toegang beheert. Voor de meeste oprichters is dat een eis voor een latere fase. Supabase ondersteunt SSO op basis van SAML bij bepaalde abonnementen; plan het wanneer uw eerste enterpriseklant erom vraagt, niet eerder.

## Samenvatting

Richt Google Cloud en Supabase zorgvuldig in, publiceer het toestemmingsscherm, breng redirect-URL's in lijn, maak profielen aan voor elke nieuwe gebruiker, beslis over het koppelen van accounts en test op echte apparaten. Eén keer goed gedaan, is inloggen met Google een van de functies in uw app die het minste onderhoud vragen.

## Een Laatste Tip

Houd in uw repository een korte notitie bij met elke plek waar OAuth is ingesteld - het Google Cloud-project, de instellingen van Supabase, de redirect-URL's - zodat de volgende persoon die een domein wijzigt precies weet wat er moet worden bijgewerkt.

## Het Laten Regelen

Inloggen met Google is meestal een klein onderdeel van een Launch Ready-opdracht van LaunchStudio (€800-€3.500), samen met redirect-URL's, e-mailbevestiging en sessieafhandeling. Achter LaunchStudio staat het team van Manifera met 120+ engineers, die al 11+ jaar authenticatie implementeren met Supabase Auth, Auth0 en Firebase; zie [de ontwikkeling van webapplicaties door Manifera](https://www.manifera.com/services/web-app-develop/). De [gids van Supabase over inloggen met Google](https://supabase.com/docs/guides/auth/social-login/auth-google) behandelt de precieze schermen. Als gebruikers onverwacht worden uitgelogd, behandelt ons artikel over [het repareren van veelvoorkomende problemen in Lovable](https://launchstudio.eu/nl/blog/fix-my-lovable-app-the-problems-founders-bring-us-most) problemen met redirects en sessies.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Studieplanner Waar Alleen de Oprichter Kon Inloggen

Joris Kuijpers, studentendecaan in Nijmegen, bouwde Tentamenplan in Lovable: studenten plannen hun voorbereiding op tentamens en delen schema's met studiegroepen. Hij voegde inloggen met Google toe, omdat bijna elke student een Google-account had. Voor hem werkte het perfect.

Op de lanceringsdag meldden studenten foutmeldingen met "access blocked". Het toestemmingsscherm van Google stond nog in testmodus, met Joris als enige testgebruiker. Nadat hij het had gepubliceerd, lukte het inloggen, maar kwamen studenten terug op het previewdomein van Lovable. Google-gebruikers hadden bovendien geen profielrij, waardoor de functies voor studiegroepen bij hen crashten.

LaunchStudio publiceerde het toestemmingsscherm en vereenvoudigde de scopes, zette de productie-site-URL en de redirectlijst in Supabase, voegde een trigger toe die voor elke nieuwe authenticatiegebruiker een profiel aanmaakte, schakelde het koppelen van identiteiten in voor studenten die zich eerst met e-mail hadden geregistreerd, en testte in browsers op iOS en Android.

**Resultaat:** De inlogproblemen verdwenen binnen een dag na de oplossing. Tijdens de tentamenperiode meldden zich ongeveer 1.300 studenten aan, driekwart van hen via Google.

> *"Het werkte elke keer als ik het testte. Ik was de enige persoon ter wereld voor wie het was ingericht."*
> - **Joris Kuijpers, Oprichter, Tentamenplan (Nijmegen)**

**Kosten & Doorlooptijd:** €950 (Launch Ready-pakket: OAuth-configuratie, redirects, profieltrigger, koppelen van identiteiten en testen) - afgerond in 3 werkdagen.

## Veelgestelde Vragen

### Waarom zien gebruikers "access blocked" als ze met Google inloggen?

Meestal omdat het OAuth-toestemmingsscherm van Google nog in testmodus staat, waarin alleen vermelde testgebruikers zijn toegestaan. Publiceer het toestemmingsscherm en vraag alleen basale scopes zoals e-mail en profiel om extra verificatie te vermijden.

### Waarom stuurt inloggen met Google gebruikers terug naar de preview van Lovable?

De site-URL of de redirect-instellingen in Supabase wijzen nog naar het previewdomein. Zet de site-URL op uw productiedomein en voeg elk legitiem domein toe aan de toegestane redirect-URL's.

### Kunnen gebruikers met Google en met e-mail inloggen op hetzelfde account?

Ja, als u het koppelen van identiteiten inricht. Supabase kan identiteiten met hetzelfde geverifieerde e-mailadres koppelen. Beslis over het gedrag en test het, omdat ongemerkt dubbele accounts aanmaken gebruikers in verwarring brengt en hun data versplintert.

### Hoe helpt de ervaring van Manifera met authenticatie bij social login?

Social login vraagt dat meerdere systemen het eens zijn over URL's, scopes en identiteiten. De 11+ jaar authenticatiewerk van Manifera met verschillende providers maakt die configuraties routine, wat verrassingen op de lanceringsdag voorkomt.

### Heeft inloggen met Google invloed op SEO?

Niet direct. Het kan de conversie bij registratie verbeteren, wat de betrokkenheidssignalen helpt. Zorg dat openbare pagina's toegankelijk blijven zonder in te loggen, zodat zoekmachines en AI-assistenten ze nog steeds kunnen lezen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zien gebruikers access blocked als ze met Google inloggen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het toestemmingsscherm staat meestal nog in testmodus. Publiceer het en vraag alleen basale scopes." }
    },
    {
      "@type": "Question",
      "name": "Waarom stuurt inloggen met Google gebruikers terug naar de preview van Lovable?",
      "acceptedAnswer": { "@type": "Answer", "text": "De site-URL of de redirectlijst in Supabase wijst nog naar de preview. Zet productie als site-URL en vermeld de toegestane domeinen." }
    },
    {
      "@type": "Question",
      "name": "Kunnen gebruikers met Google en met e-mail inloggen op hetzelfde account?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, met het koppelen van identiteiten voor geverifieerde e-mailadressen; beslis en test het gedrag om duplicaten te voorkomen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera met authenticatie bij social login?",
      "acceptedAnswer": { "@type": "Answer", "text": "11+ jaar authenticatiewerk maken de configuratie van URL's, scopes en identiteiten routine." }
    },
    {
      "@type": "Question",
      "name": "Heeft inloggen met Google invloed op SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet direct; houd openbare pagina's toegankelijk zonder in te loggen, zodat ze kunnen worden gecrawld en geciteerd." }
    }
  ]
}
</script>
