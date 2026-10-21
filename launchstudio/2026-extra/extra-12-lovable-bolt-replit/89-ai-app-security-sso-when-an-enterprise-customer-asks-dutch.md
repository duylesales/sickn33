---
Titel: "AI-appbeveiliging: SSO Wanneer een Enterpriseklant Erom Vraagt"
Trefwoorden: ai-appbeveiliging, single sign-on, SAML, Microsoft Entra ID, SCIM, enterprise SaaS, Supabase SSO, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# AI-appbeveiliging: SSO Wanneer een Enterpriseklant Erom Vraagt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-appbeveiliging: SSO Wanneer een Enterpriseklant Erom Vraagt",
  "description": "De eerste enterpriseprospect vraagt om single sign-on, en bedoelt meer dan een inlogknop. SAML of OIDC, Entra ID in de praktijk, domeinverificatie, accounts koppelen, afdwingen, deprovisioning met SCIM, en de beveiligingsfouten die SSO tot een ingang maken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-sso-when-an-enterprise-customer-asks" }
}
</script>

De eerste grotere organisatie die uw product wil kopen, stuurt een beveiligingsvragenlijst, en ergens daarin staat een vraag die kleine producten nooit hebben hoeven beantwoorden: "Ondersteunt de applicatie single sign-on met onze identity provider?"

Voor een Nederlands bedrijf van een paar honderd mensen of meer is de identity provider bijna altijd Microsoft Entra ID — wat vroeger Azure Active Directory heette — en soms Google Workspace of Okta. Hun IT-afdeling wil dat medewerkers met hun bedrijfsaccount inloggen in uw product, wil dat de toegang eindigt wanneer iemand vertrekt, en wil niet nog een set wachtwoorden beheren.

Oprichters horen meestal "voeg een Microsoft-inlogknop toe". Het verzoek is groter dan dat, en onzorgvuldig geïmplementeerd wordt SSO de makkelijkste manier om in het account van iemand anders te komen. Dit artikel behandelt wat de klant werkelijk wil, de keuze van protocol en aanbieder, de implementatiedetails die ertoe doen, en de beveiligingsfouten die u moet vermijden.

## Waar de Klant Eigenlijk om Vraagt

"SSO" op een vragenlijst bundelt meestal vijf afzonderlijke eisen. Vraag welke van toepassing zijn voordat u offreert, omdat de moeite aanzienlijk verschilt.

**Inloggen via hun identity provider.** Medewerkers klikken op "Inloggen met uw bedrijfsaccount", authenticeren bij Microsoft, en komen in uw product terecht. Dit is de kern.

**Afgedwongen SSO.** Medewerkers van dat bedrijf kunnen op geen andere manier inloggen — geen wachtwoord, geen magic link. Zonder afdwingen is SSO een gemak; met afdwingen gelden de eigen controles van het bedrijf voor elke login.

**Hun meerfactorauthenticatie en conditional access.** Hun beleid — MFA, conforme apparaten, geblokkeerde landen — geldt, omdat de authenticatie bij hun provider plaatsvindt. Dit krijgt u gratis met afgedwongen SSO en is vaak de echte reden waarom ze erom vragen.

**Automatisch aanmaken en intrekken van accounts.** Nieuwe medewerkers krijgen toegang zonder uitnodiging; vertrekkers verliezen toegang op de dag dat ze vertrekken. Dit is SCIM, en het is een apart stuk werk.

**Rollen koppelen.** Lidmaatschap van een groep in hun directory bepaalt de rol in uw product — "Finance" wordt Accountant, "Inkoopleads" wordt Beheerder.

Een eerste enterpriseklant heeft doorgaans de eerste drie nodig en vraagt om de vierde. De vijfde kan meestal wachten.

## SAML of OIDC

Twee protocollen doen dit werk.

**SAML 2.0** is ouder, gebaseerd op XML en universeel in enterprise. Elke identity provider ondersteunt het, en inkoopchecklists noemen het expliciet. De configuratie is een uitwisseling van metadata — URL's, een entity ID en een ondertekeningscertificaat — tussen u en de IT-afdeling van de klant.

**OpenID Connect (OIDC)** is nieuwer, gebaseerd op JSON en eenvoudiger te implementeren. Entra ID, Google en Okta ondersteunen het allemaal goed. Het is wat knoppen als "Inloggen met Microsoft" meestal gebruiken.

Voor een B2B-product is het praktische antwoord: ondersteun SAML, omdat IT-afdelingen in enterprise dat verwachten te configureren, en voeg OIDC toe waar het voor bepaalde providers dingen eenvoudiger maakt. Een product dat alleen een algemene knop "Inloggen met Microsoft" biedt — multi-tenant OIDC voor elk Microsoft-account — heeft niet geleverd wat de vragenlijst vroeg, omdat het de login niet aan de tenant van de klant koppelt en geen afdwingen toestaat.

## Zelf Bouwen, Supabase Gebruiken, of Inkopen

Zelf een SAML-implementatie schrijven is de ene optie om uit te sluiten. Validatie van XML-handtekeningen is berucht makkelijk fout te doen, en verschillende van de ernstigste authenticatiekwetsbaarheden van het afgelopen decennium waren precies dat. Gebruik een onderhouden implementatie.

Dat laat twee realistische paden over voor een Lovable- of Supabase-product.

**SAML SSO van Supabase Auth**, beschikbaar op betaalde abonnementen. U registreert de identity provider van elke klant met de metadata en de e-maildomeinen waarvoor die verantwoordelijk is, en gebruikers van die domeinen loggen erdoor in. Het houdt authenticatie op één plek en kost niets extra naast het abonnement. Het regelt het inloggen; afdwingen, rollen koppelen en SCIM bouwt u zelf.

**Een gespecialiseerde identiteitslaag** — WorkOS, Auth0, Clerk of vergelijkbaar — die een beheerportaal biedt waar de IT-afdeling van de klant SSO zelf configureert, plus SCIM-directorysynchronisatie, tegen een vergoeding per koppeling. U ruilt geld voor de delen die supporttijd kosten: configuratie, vervangen van certificaten, directorysynchronisatie en eigenaardigheden van providers.

De beslissing volgt meestal het aantal enterpriseklanten dat u verwacht. Voor één of twee is Supabase SAML plus een beetje eigen code proportioneel. Is enterprise de richting van het bedrijf, dan betaalt een gespecialiseerde laag zich terug in supporturen, vooral omdat de IT-afdeling van de klant haar zonder u kan configureren en problemen kan oplossen.

## Domeinverificatie Komt Eerst

Dit is de beveiligingseigenschap die het meest uitmaakt, en de eigenschap die het vaakst wordt overgeslagen.

Een SSO-koppeling geeft identiteiten af voor e-mailadressen. Mag een koppeling die door Klant A is ingericht adressen op `@klant-b.nl` afgeven, dan kan iedereen die de identity provider van Klant A beheert, inloggen als iedereen bij Klant B. In een selfservice-opzet — waarin klanten tijdens een proefperiode hun eigen SSO inrichten — betekent dat dat elk proefaccount elke gebruiker kan overnemen wiens e-maildomein het claimt.

De regel: een koppeling mag alleen identiteiten afgeven voor domeinen waarvan de organisatie heeft bewezen dat ze eigenaar is. Het standaardbewijs is een DNS TXT-record:

```
_launchstudio-verify.klant.nl.  TXT  "ls-verify=8f3c1e9a2b7d4f60"
```

Genereer het token, vraag de klant het te publiceren, controleer het voordat u de koppeling activeert, en controleer het periodiek opnieuw. Sla de geverifieerde domeinen op bij de organisatie, en weiger elke bewering van een koppeling voor een e-mailadres daarbuiten.

```ts
const domain = assertion.email.split('@')[1].toLowerCase();
if (!connection.verifiedDomains.includes(domain)) {
  throw new AuthError('sso_domain_not_verified');
}
```

Verifieer nooit domeinen van gratis e-mailaanbieders — gmail.com, outlook.com, hotmail.com — hoe het verzoek ook is geformuleerd.

## Bestaande Accounts Koppelen

De meeste enterpriseklanten hebben al een paar gebruikers met wachtwoorden in uw product, aangemaakt tijdens de proefperiode. Wanneer SSO wordt aangezet, loggen die mensen in via hun identity provider en horen ze in hun bestaande account te belanden, niet in een nieuw leeg account.

Koppelen op e-mailadres is de voor de hand liggende aanpak en is alleen onder één voorwaarde veilig: het e-maildomein is geverifieerd voor die koppeling. Dan is de identity provider gezaghebbend voor dat adres, en is koppelen juist.

Zonder verificatie is koppelen op e-mailadres een mechanisme om accounts over te nemen. Iedereen die een willekeurige identity provider `directeur@klant.nl` kan laten afgeven, krijgt het bestaande account van dat adres, met zijn data en zijn rol. AI-gegenereerde SSO-flows koppelen met enige regelmaat onvoorwaardelijk op e-mailadres, omdat de demonstratie dan werkt.

Beslis na het koppelen wat er met het wachtwoord gebeurt. Schakel voor een afgedwongen domein inloggen met wachtwoord uit voor die accounts, zodat het oude wachtwoord niet kan worden gebruikt om de controles van het bedrijf te omzeilen.

## Just-in-Time Aanmaken en Rollen Koppelen

Wanneer een medewerker voor het eerst via SSO inlogt en geen account heeft, kan het product er ter plekke een aanmaken en hem aan de organisatie toevoegen — just-in-time provisioning. Het neemt de noodzaak weg om mensen één voor één uit te nodigen, en dat is wat de IT-afdeling van de klant wil.

Drie regels houden het veilig:

- JIT geldt alleen voor geverifieerde domeinen van de organisatie die eigenaar is van de koppeling.
- Nieuwe gebruikers krijgen standaard de laagste rol — Lid of Alleen lezen — nooit Beheerder.
- Een hogere rol komt van een expliciete groepskoppeling of van een beheerder in uw product, niet van iets wat de gebruiker zelf beheert.

Rollen koppelen gebruikt de groepsclaims die de identity provider meestuurt. Koppel ze aan rollen in uw product, zoals gedefinieerd in het artikel over rollen en rechten in deze reeks:

```ts
const groupToRole = { 'LS-Admins': 'administrator', 'LS-Finance': 'accountant' };
const role = assertion.groups.map(g => groupToRole[g]).find(Boolean) ?? 'member';
```

Beoordeel gekoppelde rollen bij elke login opnieuw, zodat iemand uit een groep in Entra ID halen zijn rol in uw product verlaagt de volgende keer dat hij binnenkomt.

## Afdwingen en het Noodaccount

Afgedwongen SSO betekent dat de inlogpagina, bij een e-mailadres op een afgedwongen domein, de gebruiker naar zijn identity provider stuurt en verder niets aanbiedt. Inloggen met wachtwoord, magic links en wachtwoordherstel worden allemaal geweigerd voor dat domein — ook via de API, niet alleen in de interface.

Afdwingen schept één risico: als de SSO-configuratie van de klant breekt — een verlopen certificaat, een gewijzigde tenant, een verkeerd ingesteld beleid — kan niemand bij dat bedrijf inloggen. Houd één noodaccount aan: een benoemde eigenaar bij de klant, uitgezonderd van afdwingen, met sterke MFA, waarvan het gebruik wordt gelogd en gemeld. Leg schriftelijk vast wie het heeft.

## Deprovisioning: Het Deel Dat SSO Alleen Niet Oplost

Een veelvoorkomend misverstand, gedeeld door klanten en oprichters: wanneer een medewerker vertrekt en zijn Entra-account wordt uitgeschakeld, verliest hij de toegang tot uw product.

Hij verliest de mogelijkheid om opnieuw in te loggen. Hij verliest geen sessie die al openstaat. Duren uw sessies dertig dagen, dan houdt een vertrekker die op zijn laatste dag was ingelogd tot een maand toegang — op een laptop die hij misschien nog heeft.

Twee maatregelen dichten het gat.

**Kortere sessies voor SSO-gebruikers**, met opnieuw authenticeren bij de identity provider om de acht tot twaalf uur. Omdat inloggen voor iemand die nog in dienst is één klik is, zijn de kosten verwaarloosbaar; het sessie-artikel in deze reeks behandelt vernieuwen en intrekken.

**SCIM-provisioning.** De identity provider roept uw SCIM-endpoint aan wanneer een gebruiker wordt aangemaakt, gewijzigd of gedeactiveerd. Bij deactivering verwijdert u het lidmaatschap en trekt u sessies direct in, zoals het artikel over teamuitnodigingen beschrijft. SCIM is een gedefinieerd protocol met een handvol endpoints; het zelf implementeren is een paar dagen werk, en een gespecialiseerde identiteitslaag levert het als directorysynchronisatie.

Kunt u nog geen SCIM bieden, zeg dat dan eerlijk op de vragenlijst en beschrijf de compenserende maatregel: korte sessies, een beheerder in de organisatie van de klant die gebruikers direct kan verwijderen, en een auditlog van logins.

## Beveiligingsfouten Die SSO tot een Ingang Maken

Naast domeinverificatie en het koppelen van accounts keren vijf fouten steeds terug.

**De bewering niet goed valideren.** Handtekening, audience, recipient, vervaltijd en de verwachte uitgever moeten allemaal worden gecontroleerd. Een onderhouden bibliotheek doet dat; een zelfgeschreven parser vaak niet.

**Inloggen vanuit de IdP zonder zorg accepteren.** Logins die bij de identity provider beginnen in plaats van op uw site, zijn handig en missen de koppeling aan het verzoek die beschermt tegen vervalste antwoorden. Ondersteun ze alleen als een klant het eist, met korte geldigheid van beweringen en bescherming tegen hergebruik.

**De e-mailclaim van een multi-tenant OIDC-app vertrouwen.** "Inloggen met Microsoft" voor elke tenant levert e-mailclaims op die niet altijd zijn geverifieerd. Koppel elke verbinding aan het specifieke tenant-ID van de klant.

**De koppeling van de ene organisatie een andere laten raken.** Elke koppeling hoort bij precies één organisatie; een gebruiker die erdoor inlogt, belandt in die organisatie en nergens anders.

**Het verlopen van certificaten negeren.** SAML-ondertekeningscertificaten worden doorgaans jaarlijks vervangen. Wanneer het certificaat van de klant verloopt en niemand de configuratie bijwerkte, is elke gebruiker bij dat bedrijf op een maandagochtend buitengesloten. Sla de vervaldatum op en waarschuw zestig dagen van tevoren.

## Inloglogs Waar de Klant om Zal Vragen

Zodra SSO live is, wordt het beveiligingsteam van de klant een vaste lezer van uw product, en het eerste waar ze om vragen, is bewijs.

Leg elke SSO-login vast met de organisatie, de koppeling, de gebruiker, het resultaat en de reden van een eventuele mislukking — handtekening ongeldig, domein niet geverifieerd, gebruiker niet aangemaakt, certificaat verlopen. Mislukte pogingen doen er meer toe dan geslaagde: een golf mislukkingen voor één koppeling is ofwel een verkeerde configuratie die u kunt oplossen voordat de klant belt, ofwel iets ergers.

Toon de eigen inloggeschiedenis van een organisatie aan haar beheerders, filterbaar op gebruiker en datum. Het beantwoordt "logde deze persoon nog in nadat hij vertrok" zonder supportticket, en het is het soort mogelijkheid dat een antwoord op een vragenlijst verplaatst van "op verzoek" naar "beschikbaar in het product".

Twee beslissingen over bewaring horen in het bewaarregister dat elders in deze reeks wordt beschreven: hoe lang inloglogs worden bewaard — twaalf maanden is gebruikelijk voor beveiligingsdoeleinden — en of IP-adressen worden opgeslagen, omdat die onder de AVG persoonsgegevens zijn. Beslis bewust en schrijf de reden op; de privacyfunctionaris van de klant zal ernaar vragen.

Maak SSO-fouten tot slot zichtbaar voor uzelf. Een waarschuwing wanneer één koppeling binnen een uur meer dan een handvol mislukkingen oplevert, vangt het verlopen certificaat, de tenantmigratie en het verkeerd ingestelde beleid op voordat een heel bedrijf op een maandagochtend buitengesloten blijkt.

## De Commerciële Kant

SSO wordt vaak verkocht in een hoger abonnement, en enterprisekopers verwachten dat. Twee punten maken het gesprek makkelijker.

Prijs het zo dat het de werkelijke kosten weerspiegelt — vergoedingen per koppeling als u een aanbieder gebruikt, supporttijd voor configuratie, en het werk aan afdwingen en SCIM — in plaats van als een boete. Klanten nemen een "SSO-belasting" die willekeurig oogt kwalijk, en accepteren een prijs die duidelijk hoort bij een enterpriseabonnement met andere enterprisefuncties.

En documenteer het. Een korte pagina voor de IT-afdeling van de klant — welke identity providers worden ondersteund, welke metadata ze nodig hebben, hoe domeinverificatie werkt, wat afdwingen doet, hoe SCIM zich gedraagt — maakt van een week e-mailen een middag configureren, en is de pagina die hun beveiligingsbeoordelaar leest.

## Testen Voordat de Klant Het Doet

Test tegen een echte identity provider, niet tegen een nabootsing. Een gratis Entra ID-ontwikkeltenant of een test-Okta-organisatie laat u de echte flows doorlopen: eerste login met JIT, koppelen van een bestaand wachtwoordaccount, rolwijzigingen op basis van groepen, afdwingen dat wachtwoorden weigert, een uitgeschakelde gebruiker die toegang verliest, een certificaatwissel.

Voeg de twee negatieve tests toe die het meest uitmaken: een koppeling die een e-mailadres op een niet-geverifieerd domein probeert af te geven, moet falen, en een gebruiker van de koppeling van de ene organisatie mag nooit in een andere organisatie verschijnen.

## Dit Inrichten

Voor een Lovable- of Supabase-product dat zich voorbereidt op zijn eerste enterpriseklant, is dit doorgaans vier tot zes dagen: de werkelijke eisen van de klant vastgesteld — inloggen, afdwingen, provisioning, rollen koppelen — SAML via Supabase Auth of een gespecialiseerde identiteitslaag in plaats van een zelfgeschreven implementatie, domeinverificatie via DNS met beweringen beperkt tot geverifieerde domeinen, accounts koppelen alleen voor geverifieerde domeinen met inloggen via wachtwoord daarna uitgeschakeld, just-in-time aanmaken met de laagste rol, koppeling van groepen aan rollen opnieuw beoordeeld bij elke login, afdwingen in de API en de interface, een gelogd noodaccount, kortere sessies voor SSO-gebruikers, SCIM-deprovisioning of een gedocumenteerde compenserende maatregel, bewaking van het verlopen van certificaten, inloglogs voor de beheerders van de klant, een configuratiegids voor de IT-afdeling van de klant, en tests tegen een echte identity provider.

LaunchStudio implementeert dit wanneer de eerste enterprisedeal van een product ervan afhangt. Daarachter staat Manifera — elf jaar, 120+ engineers, 160+ projecten, met opleveringen voor enterpriseklanten waaronder Vodafone, TNO en CFLW.

[Stuur ons de beveiligingsvragenlijst](https://launchstudio.eu/nl/#contact) en wij vertellen u wat de regel over SSO werkelijk vereist.

## Echt voorbeeld

### Een Proefaccount Dat als Iedereen Kon Inloggen

Bart Engelen bouwde Leveranciersportaal in Lovable: leverancierskwalificatie en certificaatbeheer voor inkoopteams, gebruikt door 14 bedrijven.

Een regionaal nutsbedrijf met zo'n 2.000 medewerkers wilde het kopen op één voorwaarde: inloggen via hun Entra ID, afgedwongen, met automatisch verlies van toegang voor vertrekkers. Bart zette Supabase SAML aan, voegde een instellingenscherm toe waar de beheerder van een organisatie de metadata van zijn identity provider kon plakken, en koppelde binnenkomende gebruikers op e-mailadres aan bestaande accounts, zodat proefgebruikers hun data zouden houden.

Een review vóór de livegang vond het probleem. Elke organisatie — ook een gratis proefaccount — kon een identity provider registreren, en niets beperkte welke e-maildomeinen die provider mocht afgeven. Een proefaccount met een eigen test-identity provider kon het adres van elke gebruiker bij elke klant afgeven en direct aan diens account worden gekoppeld. Daarnaast duurden sessies dertig dagen, zodat een medewerker van het nutsbedrijf die in Entra ID was uitgeschakeld tot een maand toegang zou houden.

Vijf werkdagen: domeinverificatie via DNS TXT-records, met elke koppeling beperkt tot de geverifieerde domeinen van de organisatie en gratis e-mailaanbieders geweigerd; accounts koppelen beperkt tot geverifieerde domeinen, met inloggen via wachtwoord uitgeschakeld voor gekoppelde accounts op afgedwongen domeinen; het selfservicescherm voor metadata beperkt tot organisaties op het enterpriseabonnement na verificatie; just-in-time aanmaken met de rol Lid, met drie Entra-groepen gekoppeld aan rollen en opnieuw beoordeeld bij elke login; afdwingen in de API en op de inlogpagina, met één gelogde noodeigenaar bij het nutsbedrijf; SSO-sessies ingekort tot tien uur; SCIM-directorysynchronisatie via een gespecialiseerde identiteitslaag, zodat gedeactiveerde medewerkers binnen minuten toegang verloren; de vervaldatum van het certificaat opgeslagen met een waarschuwing na zestig dagen vooraf; en een configuratiegids voor de IT-afdeling van het nutsbedrijf.

**Resultaat:** vóór de fix waren er geen SSO-koppelingen door andere organisaties geregistreerd, bevestigd uit de logs. Het nutsbedrijf tekende een contract van €38.000 per jaar, en hun IT-afdeling configureerde de koppeling in een middag aan de hand van de gids. Elf maanden later ging de waarschuwing voor het verlopende certificaat af; het certificaat werd vervangen zonder één buitengesloten gebruiker.

> *"Ik had SSO gebouwd waarmee elk proefaccount als iedereen bij elke klant kon inloggen, zolang het hun e-mailadres in zijn eigen test-identity provider typte. De review vond het een week voordat het nutsbedrijf live ging."*
> — **Bart Engelen, Oprichter, Leveranciersportaal (Arnhem)**

**Kosten & Doorlooptijd:** €5.600 (domeinverificatie, accounts koppelen op geverifieerde domeinen, SSO-configuratie beperkt tot abonnement, JIT-aanmaken met koppeling van groepen aan rollen, afdwingen op API-niveau met noodaccount, kortere SSO-sessies, SCIM-deprovisioning, bewaking van verlopende certificaten, configuratiegids voor IT) — afgerond in 5 werkdagen.

## Veelgestelde vragen

### Wat bedoelt een enterpriseklant met SSO?

Meestal inloggen via hun identity provider, afdwingen zodat geen andere login mogelijk is, hun MFA en conditional access die van toepassing zijn, automatische deprovisioning via SCIM, en soms rollen op basis van groepen. Vraag welke van toepassing zijn voordat u offreert.

### Moet ik SAML of OIDC ondersteunen?

SAML, omdat IT-afdelingen in enterprise verwachten dat te configureren, met OIDC waar het voor bepaalde providers dingen eenvoudiger maakt. Een algemene knop "Inloggen met Microsoft" voor elke tenant is geen enterprise-SSO.

### Waarom is domeinverificatie zo belangrijk?

Omdat een SSO-koppeling identiteiten afgeeft voor e-mailadressen. Zonder bewijs dat de organisatie eigenaar is van het domein, kan elke koppeling elk adres afgeven en bestaande accounts overnemen.

### Verwijdert het uitschakelen van iemand in Entra ID zijn toegang?

Het stopt nieuwe logins, niet bestaande sessies. Gebruik korte sessies voor SSO-gebruikers en SCIM-deprovisioning om toegang direct in te trekken.

### Moet ik SAML zelf bouwen?

Nee. Gebruik de SAML-ondersteuning van Supabase Auth of een gespecialiseerde identiteitsaanbieder. Zelfgeschreven validatie van XML-handtekeningen is een klassieke bron van ernstige authenticatiekwetsbaarheden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat bedoelt een enterpriseklant wanneer hij om SSO vraagt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Inloggen via hun identity provider, afdwingen, hun MFA en conditional access, SCIM-deprovisioning, en soms rollen op basis van groepen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een B2B-SaaS SAML of OIDC ondersteunen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eerst SAML, omdat enterprise-IT dat verwacht, met OIDC waar nuttig — een algemene multi-tenant Microsoft-inlogknop is geen enterprise-SSO."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom heeft SSO domeinverificatie nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zonder bewijs van domeineigendom kan elke SSO-koppeling elk e-mailadres afgeven en bestaande accounts overnemen."
      }
    },
    {
      "@type": "Question",
      "name": "Beëindigt het uitschakelen van een gebruiker in Entra ID zijn toegang?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het blokkeert nieuwe logins maar geen open sessies — gebruik korte SSO-sessies en SCIM-deprovisioning voor directe intrekking."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik SAML zelf implementeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — gebruik Supabase Auth SAML of een gespecialiseerde identiteitslaag; zelfgeschreven validatie van handtekeningen is een klassieke bron van kwetsbaarheden."
      }
    }
  ]
}
</script>
