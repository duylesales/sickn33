---
Titel: "Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen"
Trefwoorden: ai applicatie beveiligingsaudit, freelancer offboarding, toegangsrechten intrekken, code eigenaarschap, account eigenaarschap, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen",
  "description": "Wanneer een freelancer of mede-oprichter vertrekt, blijven toegekende rechten vaak geruisloos actief. Dit artikel beschrijft de toegangs-audit die elke ondernemer moet uitvoeren — repositories, hosting, databases, API-sleutels, domeinen en betaalaccounts — inclusief de juridische kant van IE-overdracht.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-02",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-application-security-audit-after-a-freelancer-leaves-taking-back-access" }
}
</script>

De freelancer die je hielp om de laatste loodjes van je Lovable-app af te ronden was vriendelijk, werkte razendsnel en is inmiddels door naar een volgende opdrachtgever. De samenwerking verliep vlekkeloos. Maar ergens heeft een GitHub-account waar jij geen controle over hebt nog steeds schrijfrechten op jouw code, werkt de geheime Supabase-sleutel die tijdens het debuggen in een Slack-chat werd geplakt nog altijd, en wordt jouw domeinnaam volgend jaar maart automatisch verlengd op de creditcard van die freelancer. Een security-audit na het vertrek van een medewerker of externe specialist draait niet om wantrouwen. Het draait erom dat de enigen die wijzigingen kunnen aanbrengen in jouw bedrijf, de mensen zijn die daar vandaag de dag verantwoordelijk voor zijn.

## Waarom Toegangsrechten de Samenwerking Overleven

Snel bouwen met AI betekent in de praktijk: snel rechten uitdelen. Een freelancer heeft toegang nodig tot de Git-repository, de database, het hosting-dashboard en soms het account van de betalingsprovider om webhooks te testen. Een technisch mede-oprichter registreert het domein en de mailserver even snel op zijn eigen privéaccount omdat dat sneller gaat. Niemand legt dit formeel vast, en wanneer de samenwerking eindigt, denkt niemand eraan om die rechten weer in te trekken.

Dit vormt om drie redenen een reëel risico. Ten eerste kunnen accounts van voormalige medewerkers gecompromitteerd raken, zelfs als die personen zelf volkomen te goeder trouw zijn. Ten tweede kun je bij een storing of beveiligingsincident niet snel handelen als een cruciaal account beheerd wordt door iemand die op vakantie is of niet meer reageert. En ten derde stellen zakelijke klanten en investeerders tijdens een due-diligence steevast exact deze vraag: wie heeft er allemaal administratieve toegang tot jouw productiesystemen?

## De Toegangs-Audit: Onderdeel voor Onderdeel

**Broncode-repository.** Loop alle 'collaborators' en 'deploy keys' na op GitHub, GitLab of Bitbucket. Verwijder iedereen die geen actieve rol meer heeft. Controleer of de repository eigendom is van een zakelijke bedrijfsorganisatie of nog op iemands persoonlijke account staat; draag het eigenaarschap over indien nodig.

**AI-Builder projecten.** Lovable, Bolt, Replit en soortgelijke tools hebben hun eigen mechanismen om projecten te delen. Voormalige ontwikkelaars kunnen vaak nog steeds inloggen, prompts uitvoeren en live publiceren.

**Hosting en deployment.** Vercel, Netlify, Replit Deployments, AWS of DigitalOcean — controleer teamleden, persoonlijke API-tokens en gekoppelde Git-integraties.

**Database en backend.** Supabase- of Firebase-projectleden en API-sleutels. De 'service role keys' en database-wachtwoorden die een freelancer heeft ingezien, moeten altijd worden geroteerd (vervangen), niet enkel diens gebruikersaccount verwijderen.

**Geheime API-sleutels.** Payment providers (Mollie, Stripe), e-maildiensten, AI-model API's (OpenAI, Anthropic), kaartendiensten en analytics. Iedereen die een geheime sleutel onder ogen heeft gehad, heeft deze mogelijk nog ergens opgeslagen staan. Roteer elke sleutel die een vertrokken medewerker heeft kunnen zien.

**Domeinnaam en DNS.** Wie is de officiële registrant van het domein bij de registrar? Wiens creditcard betaalt de verlenging? Het verliezen van de controle over je domeinnaam is een van de weinige incidenten waarvan herstel vrijwel onmogelijk is.

**E-mail, analytics en supporttools.** Google Workspace, transactionele mailaccounts, helpdesk-software en error-trackers.

**App stores.** Beheerdersaccounts in Apple App Store Connect en de Google Play Console als je een mobiele app hebt.

## De Veilige Volgorde van Sleutelrotatie

Het ondoordacht roteren van API-sleutels kan je live productieomgeving per ongeluk platleggen. Hanteer daarom altijd deze veilige volgorde:
1. Breng elke locatie in kaart waar de sleutel wordt gebruikt (omgevingsvariabelen in Vercel, GitHub Actions secrets, achtergrondworkers).
2. Maak een nieuwe sleutel aan in het dashboard van de leverancier terwijl de oude sleutel nog actief blijft.
3. Update alle configuraties met de nieuwe sleutel en voer een nieuwe deployment uit.
4. Verifieer in de serverlogs of verzoeken succesvol binnenkomen met de nieuwe sleutel.
5. Trek pas daarna de oude sleutel definitief in.

## De Juridische Kant: Intellectueel Eigendom (IE)

Toegang is technisch; eigendom is juridisch. Controleer of je schriftelijke overeenkomsten hebt waarin vertrokken freelancers of bureaus alle intellectuele eigendomsrechten op de geschreven code en ontwerpen expliciet en onvoorwaardelijk overdragen aan jouw vennootschap. Zonder een getekende overdrachtsakte (*IP assignment*) rust het auteursrecht op maatwerkcode volgens het Nederlands recht vaak nog bij de maker. Het met terugwerkende kracht regelen van een IE-overdracht is eenvoudig zolang het contact goed is, maar wordt buitengewoon kostbaar en complex zodra er een investeerder aan tafel zit.

## Het Toegangsregister Template

Het belangrijkste resultaat van een toegangs-audit is een helder toegangsregister — een overzichtelijk document dat continu actueel wordt gehouden:

| Systeem | Doel | Eigenaarsaccount | Personen met toegang | Rol / Rechten | 2FA Actief? | Laatst gecontroleerd |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub repository | Broncode | Bedrijfsorganisatie | Oprichter, Lead Dev | Admin, Write | Ja | Datum |
| Supabase project | Database & Auth | Bedrijfs e-mail | Oprichter | Owner | Ja | Datum |
| Vercel | Hosting | Bedrijfsteam | Oprichter, Lead Dev | Owner, Member | Ja | Datum |
| Mollie | Betalingen | Bedrijf | Oprichter, Boekhouder | Beheerder, Alleen-lezen | Ja | Datum |
| Domeinregistrar | Domein & DNS | Bedrijf | Oprichter | Eigenaar | Ja | Datum |
| Resend | Transactionele e-mail | Bedrijf | Oprichter | Beheerder | Ja | Datum |
| Sentry | Error monitoring | Bedrijfsorganisatie | Oprichter, Developer | Admin, Member | Ja | Datum |

Houd daarnaast een lijst bij van geheime sleutels (met vermelding van de datum van de laatste rotatie, nooit de sleutelwaarde zelf). Evalueer dit overzicht maandelijks en direct na het vertrek van een medewerker.

## Verborgen Plekken Waar Toegang Achterblijft

Vertrokken krachten behouden vaak toegang op plekken waar niemand aan denkt:
- Persoonlijke access tokens (PAT's) op GitHub of Vercel voor lokale deployments.
- Deploy keys en CI/CD secrets in oude forks of persoonlijke test-repositories.
- Geautoriseerde OAuth-apps die namens hen gekoppeld zijn aan bedrijfstools.
- No-code automations (Make, Zapier, n8n) die nog draaien onder hun privégegevens.
- Lokale `.env`-bestanden op hun eigen laptops — dé reden waarom sleutels altijd geroteerd moeten worden in plaats van enkel accounts te verwijderen.
- Lokale database-dumps of exports die tijdens het debuggen zijn gedownload.

Vraag vertrekkende freelancers altijd vriendelijk en schriftelijk om alle lokale kopieën van broncode, klantdata en configuratiebestanden te wissen en dit per mail te bevestigen.

## Waar LaunchStudio Past

LaunchStudio voert complete security-audits op toegangsrechten uit: elk account, elke integratie en elke API-sleutel wordt systematisch in kaart gebracht; het eigenaarschap wordt geconsolideerd onder jouw bedrijfsentiteit met tweefactorauthenticatie (2FA); gevoelige sleutels worden geroteerd zonder enige downtime; en we leveren een compleet, getoetst toegangsregister op. De code blijft altijd in jouw beheer, en niemand bij LaunchStudio behoudt toegang na afronding van het project, tenzij je kiest voor managed hosting.

LaunchStudio wordt ondersteund door Manifera, een softwarebedrijf met meer dan 11 jaar ervaring onder leiding van Herre Roelevink, die zijn loopbaan begon in cybersecurity. Manifera opereert vanuit Amsterdam (Herengracht 420), Singapore en Ho Chi Minhstad. Bekijk [Manifera's bedrijfspagina](https://www.manifera.com/about-us/); GitHub's [handleiding voor repository-toegangsbeheer](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository) biedt een praktisch startpunt.

[Plan een gratis adviesgesprek van 15 minuten](https://launchstudio.eu/nl/#contact) als je niet precies weet wie er momenteel bij jouw productiesystemen kan.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Verhuisplatform en Vier Vergeten Accounts

Nadia Bakkali, voormalig logistiek planner in Alphen aan den Rijn, bouwde Verhuisvriend in Lovable met hulp van twee freelancers: een marktplaats waar particulieren lokale sjouwers en bestelbussen per uur kunnen boeken, compleet met Mollie-betalingen en in-app chat. Na de livegang gingen beide freelancers huns weegs en runde Nadia het platform acht maanden lang zelfstandig, waarbij het volume groeide naar 1.700 voltooide verhuizingen.

Toen een groot landelijk verhuisbedrijf een exclusief strategisch partnerschap voorstelde, vroeg hun security officer wie er administratieve toegang had tot de productiesystemen van Verhuisvriend. Nadia moest het antwoord schuldig blijven. Een security-audit door LaunchStudio bracht al snel forse verrassingen aan het licht: een van de freelancers stond nog steeds geregistreerd als enige 'Owner' van zowel de GitHub-repository als het Supabase-project; de andere freelancer bezat nog een actieve Vercel-teamseat en een personal access token waarmee direct naar productie kon worden uitgerold; de live API-sleutel van Mollie was destijds in een WhatsApp-groep gedeeld en nooit vervangen; de domeinnaam stond op naam van de eerste freelancer geregistreerd; en geen van beiden had ooit een overdracht van intellectueel eigendom ondertekend.

De engineers van LaunchStudio trokken de situatie direct vlot: het eigenaarschap van de repository en het Supabase-project werd overgedragen aan Nadia's holding; beide freelancers werden van alle platformen ontkoppeld; het Vercel-token werd ingetrokken; de API-sleutels van Mollie, Supabase (service role), Resend en Google Maps werden in een gecontroleerde stappenreeks geroteerd zonder een minuut downtime; tweefactorauthenticatie werd overal verplicht gesteld; en er werd een formeel toegangsregister opgesteld. Nadia nam contact op met de freelancers, die het domein direct kosteloos overschreven en binnen een week een standaard IE-overdrachtsakte ondertekenden.

**Resultaat:** Nadia overhandigde het geauditeerde toegangsregister aan het verhuisbedrijf, waarna het partnerschap zonder belemmeringen werd ondertekend. Verhuisvriend hanteert voortaan een vaste offboarding-checklist bij elk extern project.

> *"Niemand had kwade bedoelingen. Maar als een van die jongens zijn laptop was kwijtgeraakt, was mijn hele onderneming in andermans handen gevallen."*
> — **Nadia Bakkali, Oprichter, Verhuisvriend (Alphen aan den Rijn)**

**Kosten & Tijdlijn:** € 1.300 (toegangs-audit, overdracht eigenaarschap, sleutelrotatie en inrichten toegangsregister) — afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Wat moet een beveiligingsaudit controleren nadat een freelancer vertrekt?

Elk account en elke sleutel waar de freelancer toegang toe had: Git-repositories, AI-builder platforms, hosting, databases, payment providers, e-maildiensten, analytics, domeinregistrars en app stores — plus de formele overdracht van het intellectueel eigendom (IE).

### Is het voldoende om enkel het gebruikersaccount van een freelancer te verwijderen?

Nee. Geheime API-sleutels, database-wachtwoorden en tokens die de freelancer heeft ingezien of lokaal heeft opgeslagen, blijven na verwijdering van het account gewoon werken. Deze secrets moeten altijd actief worden geroteerd.

### Kan het roteren van API-sleutels mijn live applicatie platleggen?

Ja, als je het in de verkeerde volgorde doet. Maak altijd eerst de nieuwe sleutel aan, update alle configuraties, deploy en verifieer de werking, en trek pas daarna de oude sleutel in.

### Waarom beschouwt Manifera toegangsbeheer als beveiliging en niet als administratie?

Omdat het merendeel van de daadwerkelijke datalekken en overnames ontstaat door vergeten achterdeuren en oude inloggegevens, en niet door ingewikkelde hackersaanvallen. Weten wie er in je systemen kan is het fundament van cybersecurity.

### Helpt een helder toegangsregister bij overnames en zakelijke partnerships?

Absoluut. Grote zakelijke partners en investeerders eisen tijdens een technische audit direct inzicht in wie controle heeft over de data en broncode. Een up-to-date register beantwoordt die vragen direct en toont professionele volwassenheid.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat moet een beveiligingsaudit controleren nadat een freelancer vertrekt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alle accounts, repositories, cloud-dashboards en API-sleutels waar de freelancer bij kon, plus de formele overdracht van het intellectueel eigendom." }
    },
    {
      "@type": "Question",
      "name": "Is het voldoende om enkel het gebruikersaccount van een freelancer te verwijderen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, tokens en secrets die lokaal zijn opgeslagen blijven werken; actieve rotatie van API-sleutels en wachtwoorden is noodzakelijk." }
    },
    {
      "@type": "Question",
      "name": "Kan het roteren van API-sleutels mijn live applicatie platleggen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen bij verkeerde volgorde; maak eerst een nieuwe sleutel aan, werk systemen bij en trek pas daarna de oude in." }
    },
    {
      "@type": "Question",
      "name": "Waarom beschouwt Manifera toegangsbeheer als beveiliging en niet als administratie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Veel security-incidenten ontstaan door vergeten toegangsrechten; weten wie toegang heeft is een absolute basisvereiste." }
    },
    {
      "@type": "Question",
      "name": "Helpt een helder toegangsregister bij overnames en zakelijke partnerships?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, investeerders en enterprise-partners verlangen formeel bewijs van systeem- en data-eigenaarschap tijdens due diligence." }
    }
  ]
}
</script>
