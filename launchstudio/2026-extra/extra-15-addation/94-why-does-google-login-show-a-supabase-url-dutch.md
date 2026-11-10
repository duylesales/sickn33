---
Titel: "Waarom Toont Google Login Een Supabase-URL? Uw Inlogscherm Branden"
Trefwoorden: google login toont supabase url, supabase oauth custom domein, continue to supabase.co, google consent screen app naam, LaunchStudio, Manifera
Koperfase: Probleembewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Waarom Toont Google Login Een Supabase-URL? Uw Inlogscherm Branden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Toont Google Login Een Supabase-URL? Uw Inlogscherm Branden",
  "description": "Wanneer gebruikers inloggen met Google op een Supabase-applicatie, toont het scherm vaak 'Doorgaan naar xyz.supabase.co' in plaats van uw eigen bedrijfsnaam. Deze gids legt uit hoe dit ontstaat, welke schade dit toebrengt aan vertrouwen en conversie, en hoe u dit professioneel oplost met een geverifieerd Google OAuth-toestemmingsscherm, een custom domein voor Supabase Auth en waterdichte redirect-instellingen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-20",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-does-google-login-show-a-supabase-url" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Login with Google", "url": "https://supabase.com/docs/guides/auth/social-login/auth-google" },
    { "@type": "CreativeWork", "name": "Supabase: Custom domains", "url": "https://supabase.com/docs/guides/platform/custom-domains" },
    { "@type": "CreativeWork", "name": "Google: OAuth consent screen and app verification", "url": "https://support.google.com/cloud/answer/13463073" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" }
  ]
}
</script>

**Kort antwoord:** Google toont een vreemd Supabase-adres zoals "Doorgaan naar abcdefgh.supabase.co" omdat Google bij een standaard OAuth-koppeling de gebruiker terugstuurt naar de authenticatieserver van uw Supabase-project. Google toont standaard de domeinnaam van die redirect-URL. Gebruikers zien hierdoor op het meest privacygevoelige moment van hun registratie een willekeurige, cryptische link, wat bij voorzichtige zakelijke klanten direct argwaan wekt en leidt tot afhakers. De oplossing bestaat uit twee stappen: configureer het Google OAuth-toestemmingsscherm met uw eigen bedrijfsnaam, logo en privacybeleid en laat dit verifiëren door Google; stel vervolgens een custom domein in voor Supabase Auth (zoals `auth.uwdomein.nl`), zodat alle communicatie via uw eigen herkenbare merk verloopt.

## Belangrijkste Inzichten

- **Google toont standaard het domein van de redirect-URL,** en dat verwijst standaard rechtstreeks naar uw technische Supabase-projectcode.
- **Een ongebrand inlogscherm schaadt de conversie:** kritische en zakelijke gebruikers zien het aan voor een geavanceerde phishing-aanval.
- **De professionele oplossing vereist twee ingrepen:** een officieel goedgekeurd Google-toestemmingsscherm én een Supabase custom domein.
- **De Google-merkverificatie** vereist een geverifieerd domein via Google Search Console, een publiek privacybeleid en een actieve homepage.
- **Redirect-URL's moeten exact matchen** tussen Google Cloud Console en Supabase; één typefout resulteert in een fatale `redirect_uri_mismatch`-fout.

## Waarom het Supabase-Adres Verschijnt

Inloggen met Google verloopt via het industriestandaard OAuth 2.0-protocol. Uw webapplicatie stuurt de bezoeker door naar de inlogservers van Google. Nadat de gebruiker zijn Google-account selecteert en akkoord geeft, stuurt Google de gebruiker terug naar een vooraf goedgekeurde "redirect URL" met een eenmalige autorisatiecode. In de standaardconfiguratie van Supabase is die redirect-URL: `https://uwprojectref.supabase.co/auth/v1/callback`. De Supabase-backend wisselt deze code vervolgens veilig om voor een sessietoken voordat de bezoeker wordt doorgestuurd naar uw eigen app.

Het accountkeuzescherm van Google toont aan de gebruiker met welk platform hij verbinding maakt. Zonder een geverifieerd OAuth-toestemmingsscherm toont Google simpelweg de domeinnaam van het ontvangende callback-adres: uw Supabase-projectreferentie. Voor een potentiële klant die verwacht in te loggen bij "Verlofzaken", oogt een melding als *"Doorgaan naar qwkxjrtplmzv.supabase.co"* op zijn minst slordig en in het slechtste geval uiterst verdacht.

## Waarom Dit Uw Conversie en Reputatie Schaadt

- **Gebruikersvertrouwen:** Internetgebruikers zijn getraind om alert te zijn op verdachte internetadressen. Een onbekende domeinnaam tijdens de authenticatiestap doet direct denken aan een phishingpoging.
- **Conversieverlies:** Elke twijfel tijdens de registratieflow leidt tot afhakers, terwijl u juist fors heeft geïnvesteerd om bezoekers naar deze stap te leiden.
- **B2B-verkoop:** IT-managers en security officers bij zakelijke klanten voeren vaak een veiligheidscheck uit op de inlogprocedure; een cryptische URL leidt direct tot blokkades.
- **Merkuitstraling:** Het geeft het signaal af dat uw softwareproduct nog een onvolwassen hobbyproject is in plaats van een volwaardige zakelijke SaaS-oplossing.

## Stap 1: Configureer het Google OAuth-Toestemmingsscherm

Open de Google Cloud Console en navigeer naar **APIs & Services > OAuth consent screen** (in recentere interfaces aangeduid als Google Auth Platform branding):

- **Applicatienaam (App name):** De officiële handelsnaam van uw product zoals klanten die kennen.
- **App-logo:** Een vierkant, herkenbaar logo met hoge resolutie.
- **E-mailadres voor gebruikersondersteuning:** Een professioneel adres (zoals `support@uwdomein.nl`).
- **Geautoriseerde domeinen (Authorised domains):** Voeg uw eigen hoofddomein toe (bijvoorbeeld `uwdomein.nl`).
- **Links naar documentatie:** Vul werkende links in naar uw homepage, uw privacyverklaring en uw algemene voorwaarden op uw eigen domein.

Zet de publicatiestatus van de app op **"In production"** (In productie) in plaats van "Testing". In de testmodus kunnen uitsluitend handmatig toegevoegde testgebruikers inloggen en krijgen anderen een waarschuwingsscherm te zien.

## Stap 2: Laat Uw Merk Verifiëren door Google

Google toont uw bedrijfsnaam en logo pas officieel nadat uw aanvraag door het Google Trust & Safety-team is geverifieerd. Voor applicaties die uitsluitend standaardgegevens opvragen (*basic scopes* zoals e-mailadres, basisprofiel en OpenID), is dit een relatief gestroomlijnde controle. Google toetst hierbij:

- Of u de eigenaar bent van het gekoppelde domein (geverifieerd via Google Search Console).
- Of uw homepage een duidelijke beschrijving van de software bevat en rechtstreeks linkt naar het privacybeleid.
- Of uw privacyverklaring helder uitlegt welke Google-gebruikersgegevens worden verzameld en hoe deze worden beschermd.
- Of uw merknaam en logo geen inbreuk maken op bestaande handelsmerken.

Deze verificatie duurt doorgaans enkele werkdagen. Vraagt uw app echter om gevoelige permissies (zoals leesrechten op Gmail of Google Drive), dan volgt een zware security-audit. Vermijd dergelijke rechten tenzij ze strikt noodzakelijk zijn voor uw kernproduct.

## Stap 3: Een Custom Domein voor Supabase Auth

Zelfs met een goedgekeurd Google-toestemmingsscherm loopt de tussenstap nog altijd over `supabase.co`. Gebruikers met een scherp oog zien dit adres kortstondig in de adresbalk flitsen. Supabase biedt op zijn Pro-abonnement de mogelijkheid om een custom domein in te richten (bijvoorbeeld `auth.uwdomein.nl` of `api.uwdomein.nl`).

Het stappenplan:

1. **Maak een CNAME-record aan in uw DNS:** Wijs uw subdomein (zoals `auth.uwdomein.nl`) aan naar uw projectcode bij Supabase, inclusief het door Supabase verstrekte verificatierecord.
2. **Activeer het custom domein in het Supabase-dashboard** zodra de DNS-propagatie is voltooid.
3. **Voeg de nieuwe callback-URL toe in Google Cloud:** Voeg `https://auth.uwdomein.nl/auth/v1/callback` toe aan de lijst met geautoriseerde omleidings-URI's.
4. **Werk de omgevingsvariabelen in uw frontend bij:** Laat de Supabase-client communiceren met uw nieuwe auth-subdomein in plaats van de generieke project-URL.
5. **Behoud het oude callback-adres tijdelijk in Google:** Laat het oude adres minimaal twee weken actief staan zodat gebruikers die midden in een sessie zitten geen foutmelding krijgen.

Een bijkomend groot voordeel: met een custom domein blijven authenticatiecookies en API-verzoeken binnen uw eigen hoofddomein (first-party context), wat problemen met Safari's Intelligent Tracking Prevention voorkomt. Lees ook [waarom apps crashen op iPhone en Safari](https://launchstudio.eu/nl/blog/why-does-my-app-break-on-iphone-and-safari).

## Stap 4: Redirect-URL's Nauwkeurig Instellen in Supabase

Nadat Google de gebruiker heeft teruggeleid naar Supabase, stuurt Supabase de bezoeker door naar de uiteindelijke landingspagina van uw applicatie. Supabase weigert redirects naar URL's die niet expliciet op de witte lijst staan.

**Controleer in het Supabase-dashboard:**
- **Site URL:** Moet verwijzen naar de officiële homepage van uw productie-applicatie (`https://app.uwdomein.nl`).
- **Redirect URLs:** Moet alle specifieke routes bevatten voor productie, staging en lokale ontwikkeling (`http://localhost:5173/**`). Vermijd te brede wildcards op productie om open-redirect kwetsbaarheden te voorkomen.

## Veelgemaakte Fouten bij OAuth-Inrichting

| Fout | Gevolg |
| --- | --- |
| Toestemmingsscherm staat nog op "Testing" | Alleen handmatig geregistreerde testers kunnen inloggen; klanten krijgen een fout |
| Redirect URI in Google wijkt één letterteken af | Harde `redirect_uri_mismatch` foutmelding tijdens inloggen |
| Privacybeleid staat op een ander domein dan de app | Google keurt de merkverificatie af |
| Custom domein actief, maar frontend gebruikt oude URL | Het lelijke Supabase-adres blijft zichtbaar op het inlogscherm |
| Oude callback te snel gewist uit Google Console | Klanten met actieve browsertabbladen kunnen niet meer inloggen |
| Onnodig zware Google-permissies opgevraagd | Verificatieproces duurt weken en toont angstaanjagende beveiligingswaarschuwingen |

Onze handleiding over [Google login toevoegen aan Lovable](https://launchstudio.eu/nl/blog/how-do-i-add-google-login-to-a-lovable-app) behandelt de initiële implementatie; dit artikel perfectioneert de zakelijke merkervaring.

## Breid de Merkbeleving Uit naar Alle Inlogkanalen

Hetzelfde principe geldt voor inloggen met Apple, Microsoft Azure AD of LinkedIn: overal waar OAuth wordt ingezet, moet het omleidingsdomein naadloos aansluiten bij uw merk. Zorg daarnaast dat transactionele e-mails (zoals magische inloglinks en wachtwoord-resets) niet verstuurd worden vanaf een standaard Supabase-afzender, maar vanaf uw eigen domein met geconfigureerde DKIM- en SPF-records. Zie onze gids over [DNS-configuratie voor livegang](https://launchstudio.eu/nl/blog/dns-setup-for-launch-domain-email-and-ssl).

## Het Testprotocol Vóór Livegang

Doorloop de volgende controles op een staging-omgeving voordat u de wijziging activeert voor al uw betalende gebruikers:

- Test registratie en inloggen met een kersvers Google-account dat nog nooit eerder met de app gekoppeld was.
- Test met een zakelijk Google Workspace-account om te verifiëren dat enterprise-instellingen geen roet in het eten gooien.
- Test op iPhone Safari, Android Chrome en desktopbrowsers.
- Test vanuit een in-app browser (zoals Instagram of LinkedIn) en zorg dat er een duidelijke alternatieve inlogoptie via e-mail beschikbaar is.
- Controleer of bestaande gebruikerssessies netjes intact blijven na het activeren van het custom auth-domein.

## Hoe LaunchStudio Helpt

LaunchStudio richt professionele, betrouwbare authenticatie in voor met AI gebouwde SaaS-applicaties: we configureren Google- en Microsoft-toestemmingsschermen, begeleiden het officiële verificatietraject, richten Supabase custom domeinen in inclusief DNS-records, configureren redirect-omgevingen voor dev, staging en productie, personaliseren e-mailtemplates en garanderen een geruisloze overgang voor uw bestaande gebruikers.

Het **Launch Ready**-pakket (€800 - €3.500) omvat complete authenticatie-inrichting, beveiliging en livegang; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt continue hostingbegeleiding, monitoring en prioritaire ondersteuning. Bereken een prijsindicatie met onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is een initiatief van Manifera, een software-ontwikkelingsbedrijf met ruim 11 jaar ervaring, meer dan 160 opgeleverde projecten en 120+ senior engineers gespecialiseerd in enterprise identiteitsbeheer en IT-security. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de technische engineering vindt plaats in het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City en onze vestiging aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in de Praktijk: De HR-Tool die Leek op een Phishing-Aanval

Jasper Mulder bouwde Verlofzaken met Lovable en Supabase: een gestroomlijnde verlof- en verzuimapplicatie voor het MKB, waarmee medewerkers vakantiedagen aanvragen en teamleiders met één klik goedkeuring geven. Jasper richtte zich specifiek op HR-managers van bedrijven met 20 tot 150 medewerkers, waarbij registratie en inloggen standaard verliepen via zakelijke Google Workspace-accounts.

Tijdens een belangrijke verkoopperiode zetten twee veelbelovende prospects hun proefperiode plotseling stil nadat hun interne IT-beveiligers aan de bel hadden getrokken over het inlogscherm. Google toonde bij het inloggen prominent: *"Doorgaan naar xptlqmvhrzke.supabase.co"*. Een van de IT-managers meldde Jasper letterlijk dat het scherm *"exact leek op een interne phishingtest om personeel te testen"*. Uit Jaspers eigen analytics bleek bovendien dat zo'n 25% van de websitebezoekers die op "Inloggen met Google" klikte, het registratieproces voortijdig afbrak. Het toestemmingsscherm stond nog in de testmodus met een generieke projectnaam, het privacybeleid linkte provisorisch naar een openbaar Google Docs-bestand en de Supabase-redirects bevatten alleen het testdomein waardoor staging-sessies op productie belandden.

LaunchStudio bracht het privacybeleid en de gebruiksvoorwaarden onder op Jaspers eigen domein, verifieerde het eigendom via Google Search Console en richtte het OAuth-toestemmingsscherm in met de officiële naam, het logo en de juiste domeinen van Verlofzaken. De aanvraag voor officiële merkverificatie werd ingediend en binnen vier werkdagen goedgekeurd door Google. Daarnaast werd een custom domein (`auth.verlofzaken.nl`) via DNS aan Supabase gekoppeld, het nieuwe callback-adres werd in Google geregistreerd en de frontendcode werd omgezet, terwijl het oude callback-adres nog twee weken als vangnet actief bleef. Alle redirect-URL's werden per omgeving strak getrokken en de transactionele e-mails kregen een professionele opmaak vanaf het bedrijfsdomein.

**Resultaat:** Het Google-inlogscherm toont nu trots *"Doorgaan naar Verlofzaken"* met het officiële bedrijfslogo. Het percentage voltooide aanmeldingen via Google schoot omhoog van circa 75% naar 93% van de pogingen, en beide voorheen stilgezette zakelijke prospects ondertekenden alsnog een jaarcontract nadat hun IT-afdelingen de nieuwe infrastructuur hadden goedgekeurd.

> *"Ik verloor zakelijke deals door één enkel scherm waar ik zelf nooit echt naar had gekeken. Nu is het eerste wat klanten zien mijn eigen merk, in plaats van een verdacht willekeurig internetadres."*
> - **Jasper Mulder, Oprichter, Verlofzaken (Arnhem)**

**Kosten & Doorlooptijd:** €1.600 (Launch Ready-pakket: toestemmingsscherm en verificatie, Supabase custom domein, redirect-configuratie, gebrande auth-e-mails en tests) - afgerond in 7 werkdagen inclusief de review van Google.

## Veelgestelde Vragen

### Waarom toont inloggen met Google de tekst "Doorgaan naar supabase.co"?

Omdat Google gebruikers na autorisatie terugstuurt naar de authenticatieserver van uw Supabase-project. Zonder een geverifieerd OAuth-toestemmingsscherm en zonder een custom auth-domein toont Google standaard de technische domeinnaam van die redirect-bestemming.

### Heb ik een betaald Supabase-plan nodig voor een custom domein?

Ja, een custom domein is beschikbaar als betaalde add-on binnen de betaalde Supabase-abonnementen. Voor een commerciële applicatie met betalende klanten wegen deze geringe kosten ruimschoots op tegen de enorme toename in betrouwbaarheid en conversie. Lees ook [heb ik een betaald Supabase-plan nodig](https://launchstudio.eu/nl/blog/do-i-need-a-paid-supabase-plan-for-production).

### Hoe lang duurt de merkverificatie bij Google gemiddeld?

Voor applicaties die uitsluitend standaard inloggegevens opvragen (zoals e-mailadres en openbaar profiel), duurt de goedkeuring doorgaans enkele werkdagen, mits uw domeinverificatie in Search Console, homepage en privacyverklaring volledig op orde zijn.

### Hoe helpt de ervaring van Manifera bij het inrichten van zakelijke authenticatie?

Manifera implementeert al meer dan 11 jaar enterprise single sign-on (SSO), OAuth-integraties en identity management voor internationale zakelijke platforms. LaunchStudio past die beveiligingsnormen toe op AI-applicaties zodat ze direct voldoen aan de strenge eisen van zakelijke IT-afdelingen.

### Heeft een gebrand inlogscherm invloed op SEO of vindbaarheid in AI-zoekmachines?

Indirect zeer zeker. Domeinvalidatie in Google Search Console, een transparante homepage en een officieel privacybeleid vormen de basis voor sterke domeinautoriteit. Bovendien zorgt een professionele, vertrouwde inlogervaring voor een aanzienlijk hogere conversie uit het organische zoekverkeer dat u aantrekt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom toont inloggen met Google de tekst \"Doorgaan naar supabase.co\"?",
      "acceptedAnswer": { "@type": "Answer", "text": "Google toont de domeinnaam van uw Supabase-project tenzij uw merk geverifieerd is en Supabase Auth via een custom domein loopt." }
    },
    {
      "@type": "Question",
      "name": "Heb ik een betaald Supabase-plan nodig voor een custom domein?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, een custom domein is een betaalde toevoeging op Supabase-plannen, essentieel voor professioneel gebruikersvertrouwen." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt de merkverificatie bij Google gemiddeld?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal enkele werkdagen voor basisrechten, mits het domein geverifieerd is en het privacybeleid op orde is." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het inrichten van zakelijke authenticatie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera implementeert al 11+ jaar veilige SSO en identiteitsbeheer conform strenge zakelijke IT- en privacyrichtlijnen." }
    },
    {
      "@type": "Question",
      "name": "Heeft een gebrand inlogscherm invloed op SEO of vindbaarheid in AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect wel; domeinverificatie en professioneel beleid versterken de E-E-A-T en verhogen de conversie van organisch verkeer." }
    }
  ]
}
</script>
