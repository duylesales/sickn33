---
Titel: "Wat Kost het om SSO en Enterprisefuncties Toe te Voegen?"
Trefwoorden: kosten sso toevoegen, kosten saml sso implementatie, kosten enterprisefuncties saas, kosten auditlog ontwikkeling, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Wat Kost het om SSO en Enterprisefuncties Toe te Voegen?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat Kost het om SSO en Enterprisefuncties Toe te Voegen?",
  "description": "Een kostenoverzicht voor het toevoegen van enterprisefuncties aan SaaS-apps gebouwd met Lovable, Bolt, v0, Cursor of Claude Code: single sign-on met SAML of OpenID Connect, SCIM-provisioning, organisaties en rollen, auditlogs, locatie van gegevens, beveiligingsreviews en vragenlijsten, met gebruikelijke prijsranges, doorlopende kosten van providers, wat de kosten bepaalt en hoe u beslist wat u vóór de eerste enterprisedeal bouwt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-03",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cost-to-add-sso-and-enterprise-features" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Pricing", "url": "https://supabase.com/pricing" },
    { "@type": "CreativeWork", "name": "Supabase: Single Sign-On with SAML 2.0", "url": "https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml" },
    { "@type": "CreativeWork", "name": "RFC 7644: SCIM Protocol", "url": "https://datatracker.ietf.org/doc/html/rfc7644" },
    { "@type": "CreativeWork", "name": "Microsoft Entra ID: SAML-based single sign-on", "url": "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on" }
  ]
}
</script>

**Kort antwoord:** SAML single sign-on toevoegen aan een SaaS gebouwd met AI kost doorgaans €2.500 tot €4.000 als uw app al organisaties en rollen heeft, en meer als die eerst moeten worden gebouwd. Een volledig enterprise-gereedheidspakket met organisaties, rollen, SSO, auditlogs, een beveiligingsreview en documentatie voor het inkoopproces kost meestal €4.000 tot €7.500. SCIM-provisioning, eigen rollen en de locatie van gegevens komen daar nog bij. Doorlopende kosten omvatten mogelijke kosten van uw authenticatieprovider voor SSO-koppelingen en een klein beetje ondersteuning per nieuwe klantkoppeling.

Enterprisefuncties zijn vaak het verschil tussen een pilot en een getekend contract. Ze zijn ook makkelijk te overdimensioneren. Oprichters besteden soms maanden aan functies waar geen klant om heeft gevraagd, of onderschatten hoeveel werk SSO vraagt als de app geen organisatiemodel heeft. Deze pagina zet uiteen wat elke enterprisefunctie kost, wat de prijs bepaalt en hoe u alleen bouwt wat de eerste enterprisedeal vraagt.

## Belangrijkste Punten

- **Het model voor organisaties en rollen is het fundament;** zonder dat kost SSO meer.
- **Alleen SSO** kost doorgaans €2.500 tot €4.000 op een stevig fundament.
- **Auditlogs, SCIM en eigen rollen** zijn aparte kostenposten, elk met een gebruikelijke range.
- **Kosten van authenticatieproviders** kunnen per SSO-koppeling of per abonnement gelden.
- **Bouw voor de deal die voor u ligt,** en breid uit als volgende klanten daarom vragen.

## Kosten per Enterprisefunctie

| Functie | Wat het inhoudt | Gebruikelijke kosten | Gebruikelijke duur |
| --- | --- | --- | --- |
| Organisaties en rollen | Organisaties, leden, rollen voor beheerder en lid, afgedwongen in de database | €2.000-€4.000 | 1-2 weken |
| SAML SSO | SSO per organisatie, doorsturen op domein, just-in-time provisioning | €2.500-€4.000 | 1-2 weken |
| OpenID Connect SSO | Extra SSO-standaard voor sommige identity providers | €800-€1.500 bovenop SAML | 2-4 werkdagen |
| Verplichte SSO | Optie waarmee klanten SSO voor alle gebruikers verplichten | €500-€1.000 | 1-2 werkdagen |
| SCIM-provisioning | Automatisch aanmaken, bijwerken en verwijderen van gebruikers vanuit de identity provider | €2.000-€3.500 | 1-2 weken |
| Auditlogs | Vastgelegde events, beheerweergave, filters, export, bewaartermijn | €1.500-€3.000 | 1-2 weken |
| Eigen rollen | Klanten bepalen zelf rollen en rechten | €2.000-€4.000 | 1-2 weken |
| Opties voor locatie van gegevens | Hosting in een gekozen regio, of aparte projecten voor specifieke klanten | €1.500-€4.000 | 1-3 weken |
| Beveiligingsreview met fixes | Toegangscontrole, secrets, opslag, dependencies, headers | €1.500-€3.500 | 1-2 weken |
| Vragenlijst en bewijspakket | Beveiligingsoverzicht, subverwerkers, antwoorden op veelgestelde vragen | €800-€2.500 | 3-8 werkdagen |

Gecombineerd in één project delen deze onderdelen werk en kosten ze minder dan de som der delen. Een gebruikelijk volledig pakket komt uit tussen €4.000 en €7.500 binnen Launch & Grow.

## Gebruikelijke Pakketten

| Pakket | Inhoud | Gebruikelijke prijs |
| --- | --- | --- |
| SSO op een bestaand organisatiemodel | SAML SSO, doorsturen op domein, just-in-time provisioning, kleine fixes aan rollen | €2.500-€4.000 |
| Eerste enterpriseklant | Organisaties en rollen, SAML SSO, auditlogs, beveiligingsreview, bewijspakket | €4.000-€7.500 |
| Volwassen enterpriseniveau | Voegt SCIM, eigen rollen, locatie van gegevens en OpenID Connect toe | €7.500 en meer, vaak in fasen |

## Wat de Kosten Bepaalt

1. **Of er een organisatiemodel is.** Apps met alleen individuele accounts hebben eerst een tenantmodel nodig, en dat is vaak de grootste post.
2. **De authenticatieopzet.** Supabase Auth, Clerk, Auth0 of een eigen opzet ondersteunen SSO elk op een andere manier.
3. **Aantal identity providers.** Alleen Microsoft Entra ID ondersteunen is eenvoudiger dan elke provider ondersteunen.
4. **Eisen aan provisioning.** Just-in-time provisioning is eenvoudig; SCIM voegt een volledige API voor gebruikerssynchronisatie toe.
5. **Omvang van de audit.** Logins en wijzigingen in rollen loggen gaat snel; elke wijziging in gegevens over veel tabellen loggen is meer werk.
6. **Locatie van gegevens.** Aparte projecten per klant verhogen de inrichtings- en beheerinspanning.
7. **De staat van de code.** Rollen die alleen in de browser worden gecontroleerd, moeten eerst naar de server en database.

## Doorlopende Kosten

Enterprisefuncties hebben lopende kosten naast de ontwikkeling:

- **Kosten van authenticatieproviders.** Sommige providers nemen SSO op in hogere abonnementen of rekenen per SSO-koppeling; controleer de actuele prijzen van uw provider.
- **Inrichting per klant.** Elke nieuwe SSO-koppeling vraagt om een uitwisseling van configuratie met het IT-team van de klant, doorgaans minder dan een uur zodra de functie bestaat.
- **Opslag van logs.** Auditlogs groeien in de loop van de tijd; instellingen voor de bewaartermijn houden de opslagkosten redelijk.
- **Onderhoud.** Identity providers wijzigen periodiek certificaten en instellingen; monitoring signaleert verlopende certificaten.
- **Updates van vragenlijsten.** Antwoorden en documenten moeten worden bijgewerkt als de app of de providers veranderen.

Met Launch & Grow valt routineonderhoud onder de doorlopende dienst van €49 per maand.

## Moet U Laten Betalen voor Enterprisefuncties?

Veel SaaS-bedrijven bieden SSO, auditlogs en geavanceerde rollen alleen aan in een enterpriseniveau, of rekenen eenmalige kosten per SSO-koppeling. De redenering is eenvoudig: deze functies zijn vooral nuttig voor grotere klanten, voegen supportwerk toe en hebben soms kosten bij providers. Door ze apart te prijzen, verdient u de ontwikkelkosten vaak al binnen de eerste één of twee enterprisecontracten terug. Welk model u ook kiest, door de functies zo te bouwen dat ze per organisatie kunnen worden ingeschakeld, blijft uw prijsstelling flexibel.

## Bouw Alleen Wat de Deal Vraagt

De meest gemaakte fout is een complete set enterprisefuncties bouwen voordat een enterpriseklant erom vraagt. Een betere aanpak:

1. **Vraag de prospect om de eisen op schrift,** vaak een beveiligingsvragenlijst of een IT-checklist.
2. **Scheid must-haves van nice-to-haves.** SSO met hun identity provider en een auditlog zijn vaak must-haves; SCIM en eigen rollen in het begin vaak niet.
3. **Bouw het fundament goed,** vooral organisaties en rollen, omdat al het andere daarvan afhangt.
4. **Lever wat nodig is voor de evaluatie,** met gedateerde plannen voor de rest.
5. **Breid uit als volgende klanten erom vragen,** op hetzelfde fundament.

Met deze aanpak blijft het eerste enterpriseproject meestal tussen €4.000 en €6.000 in plaats van €10.000 of meer.

## Wat het Kost om Geen Enterprisefuncties te Hebben

Enterprisedeals zonder de vereiste functies lopen meestal vast bij de goedkeuring door IT. De kosten staan niet als regel op een factuur, maar zitten in een vertraagd of verloren contract, vaak per jaar meerdere keren de ontwikkelkosten waard. Sommige oprichters proberen eisen te omzeilen met handmatige processen, zoals gebruikers met de hand verwijderen als een klant een lijst met vertrekkers mailt. Dat werkt voor één klant, maar levert risico en supportwerk op dat met elk nieuw account groeit.

## Voorbeeld van een Kostenverdeling

Voor een B2B-SaaS met individuele accounts, Supabase Auth en een prospect die SSO met Entra ID, een auditlog en een ingevulde vragenlijst eist, is een gebruikelijk project van rond €6.000 ongeveer als volgt verdeeld:

| Onderdeel | Geschat aandeel |
| --- | --- |
| Model voor organisaties en rollen, met migratie | 30% |
| SAML SSO met doorsturen op domein en provisioning | 25% |
| Auditlogs met beheerweergave en export | 15% |
| Beveiligingsreview en fixes | 15% |
| Bewijspakket en ondersteuning bij de vragenlijst | 10% |
| Onboarding van de klant voor de eerste SSO-koppeling | 5% |

## Wat We van U Nodig Hebben

- De eisen of vragenlijst van de prospect, als die er zijn
- Toegang tot uw repository, database, authenticatieprovider en hosting
- Beslissingen over rollen, te loggen events en de prijs van enterprisefuncties
- Een introductie bij de IT-contactpersoon van de klant voor de eerste koppeling
- Tijd om de documentatie te bekijken voordat die wordt verstuurd

## Overzicht van Prijzen

| Pakket | Enterprisewerk dat doorgaans is inbegrepen |
| --- | --- |
| Launch Ready (€800-€3.500) | Beveiligingsreview, ondersteuning bij vragenlijsten, kleine fixes aan rollen |
| Launch & Grow (€2.500-€7.500 plus €49 per maand) | Organisaties, SSO, auditlogs, enterprise-gereedheidspakketten |

De offerte staat vast na de beoordeling. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Niet Inbegrepen

De bovenstaande kosten omvatten geen kosten van authenticatieproviders, certificeringen zoals ISO 27001 of SOC 2, geaccrediteerde penetratietests en juridische review van contracten. We bereiden het technische fundament en de documentatie voor die daarvoor nodig zijn en kunnen afstemmen met auditors, testers en juristen.

## Hoe Lang Duurt het Tot de Eerste Enterpriseklant Live Is?

Van getekende offerte tot de eerste SSO-login van de klant duren de meeste projecten twee tot vier weken, afhankelijk van of er een organisatiemodel is en hoe snel het IT-team van de klant reageert. Het inkoopproces van de klant kan parallel lopen; het bewijspakket vroeg voorbereiden verkort dat vaak. We plannen het werk zo dat de functies die de klant als eerste test, meestal SSO en rollen, het eerst klaar zijn.

## Zelf Bouwen Versus Inkopen

Sommige authenticatieproviders en gespecialiseerde diensten bieden SSO, SCIM en auditlogs aan als beheerde functies, geprijsd per koppeling of per gebruiker. Die kunnen de ontwikkelkosten verlagen, maar voegen een terugkerende vergoeding en een extra subverwerker toe. Bouwen op uw bestaande provider, zoals Supabase Auth met SAML, heeft op kleine schaal vaak lagere lopende kosten. We vergelijken beide opties voor uw situatie, inclusief het verwachte aantal enterpriseklanten in de komende twee jaar, zodat de beslissing is gebaseerd op de totale kosten en niet op de eerste factuur.

## Waarom Apps Gebouwd met AI Vaak Eerst Grondwerk Nodig Hebben

De meeste SaaS-producten gebouwd met AI beginnen met individuele accounts, omdat een prompt als "voeg login toe" dat oplevert. Rollen, als die er al zijn, worden vaak als veld bij de gebruiker opgeslagen en alleen in de interface gecontroleerd. Gegevens zijn gekoppeld aan een gebruiker in plaats van aan een organisatie. Niets daarvan is een probleem totdat er een enterpriseklant komt, maar het betekent dat SSO niet zomaar kan worden ingeschakeld. De identity provider heeft een organisatie nodig om zijn gebruikers aan te koppelen, en rollen moeten worden afgedwongen waar ze niet kunnen worden omzeild.

Dat grondwerk verklaart waarom offertes voor dezelfde functie zo kunnen verschillen tussen apps. Twee oprichters vragen misschien allebei om "SSO met Entra ID". Voor de één, wiens app al organisaties en in de database afgedwongen rollen heeft, is het een project van twee weken van rond €3.000. Voor de ander, wiens app alleen individuele accounts en rolcontroles in de browser heeft, is het een project van vier weken van rond €6.000, waarvan het grootste deel het fundament is. De beoordeling vóór de offerte maakt dat verschil zichtbaar, zodat u weet waar het geld naartoe gaat.

## Tip voor de Begroting

Behandel het eerste enterpriseproject bij uw begroting als een investering in verkoop in plaats van als een technische kostenpost. Vergelijk het met de jaarwaarde van de deal die het mogelijk maakt en met de pijplijn van vergelijkbare klanten erachter. Een project van een paar duizend euro dat een contract van tienduizenden euro's per jaar mogelijk maakt en de volgende klanten goedkoper maakt om aan te sluiten, is meestal een makkelijke beslissing zodra de cijfers op één pagina staan.

## Het Fundament Hergebruiken voor Latere Klanten

Het goede nieuws is dat u het grondwerk maar één keer betaalt. Na het eerste enterpriseproject is het toevoegen van een nieuwe SSO-klant vooral configuratie samen met hun IT-team. SCIM, eigen rollen of extra auditevents toevoegen bouwt voort op hetzelfde model. Oprichters merken meestal dat de tweede en derde enterpriseklant veel goedkoper zijn om aan te sluiten dan de eerste, wat het rendement van de eerste investering flink verbetert.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat software bouwt voor grote organisaties zoals Vodafone en TNO, waar SSO en audittrails standaard zijn. De CEO van Manifera, Herre Roelevink, was medeoprichter van het cybersecuritybedrijf CyberDevOps, nu CFLW Cyber Strategies. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We helpen u precies te bouwen wat de deal nodig heeft, tegen een vaste prijs.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Contract van €40.000 Achter een Vraag van €5.000

Naomi Vos heeft vanuit Zwolle een SaaS voor compliancetraining voor zorgorganisaties, gebouwd met Bolt en Supabase. Een ziekenhuisgroep met zo'n 1.500 medewerkers wilde een contract van ongeveer €40.000 per jaar, op voorwaarde dat het platform inloggen met Microsoft Entra ID ondersteunde, vertrekkers automatisch verwijderde, een auditlog van afgeronde cursussen bijhield en een beantwoorde vragenlijst had. Een andere leverancier had €18.000 geoffreerd voor een "volledige enterprisesuite" met SCIM, eigen rollen en een aparte database per klant.

LaunchStudio nam de eisen van het ziekenhuis samen met Naomi door. Het automatisch verwijderen van vertrekkers kon worden opgelost met just-in-time provisioning plus een dagelijkse controle bij de identity provider, zonder volledige SCIM voor het eerste contract. Eigen rollen en een aparte database waren niet vereist. De vaste offerte omvatte een organisatiemodel met drie rollen, SAML SSO met doorsturen op domein en verplichte SSO, een auditlog voor logins, wijzigingen in rollen en afgeronde cursussen met export, een beveiligingsreview en een bewijspakket, voor €5.400.

**Resultaat:** De IT-afdeling van het ziekenhuis keurde het platform na één gesprek goed, en het contract werd vijf weken na de start van het project getekend. Toen een tweede ziekenhuisgroep later SCIM eiste, werd dat voor €2.600 op hetzelfde fundament toegevoegd.

> *"Ik stond op het punt €18.000 uit te geven aan functies waar niemand om had gevraagd. Precies bouwen wat de eerste klant nodig had, kostte een derde daarvan en sloot de deal."*
> - **Naomi Vos, Oprichter, Zorgleerlijn (Zwolle)**

**Kosten & Doorlooptijd:** €5.400 (Launch & Grow-pakket: organisaties en rollen, SAML SSO, auditlog, beveiligingsreview en bewijspakket, plus €49 per maand) - afgerond in 15 werkdagen.

## Veelgestelde Vragen

### Wat kost het om SSO aan mijn SaaS toe te voegen?

SAML SSO kost doorgaans €2.500 tot €4.000 als uw app al organisaties en rollen heeft. Als die eerst moeten worden gebouwd, kost een gecombineerd project meestal €4.000 tot €6.000. Kosten van de authenticatieprovider voor SSO kunnen apart gelden.

### Wat kost een volledig enterprise-gereedheidspakket?

Doorgaans €4.000 tot €7.500 binnen Launch & Grow, voor organisaties en rollen, SSO, auditlogs, een beveiligingsreview en documentatie voor het inkoopproces. SCIM, eigen rollen en de locatie van gegevens worden toegevoegd als dat nodig is.

### Heb ik SCIM-provisioning nodig?

In het begin niet altijd. Veel enterpriseklanten accepteren just-in-time provisioning met een periodieke controle op verwijderde gebruikers. SCIM wordt belangrijk voor grotere klanten met strikt identiteitsbeheer. We bekijken de werkelijke eisen voordat we het aanraden.

### Hoe helpt de ervaring van Manifera bij enterprisefuncties?

Manifera bouwt al 11+ jaar software voor grote organisaties zoals Vodafone en TNO, over 160+ projecten, en de CEO was medeoprichter van een cybersecuritybedrijf. LaunchStudio gebruikt die ervaring om enterprisefuncties af te bakenen tot wat klanten werkelijk eisen.

### Helpen enterprisefuncties bij mijn SEO en zichtbaarheid in AI?

Ja. Pagina's over SSO-ondersteuning, beveiliging en integraties sluiten aan bij waar IT-kopers op zoeken en wat ze aan AI-antwoordmachines vragen. Juiste openbare informatie maakt het waarschijnlijker dat uw product wordt meegenomen als die kopers tools vergelijken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost het om SSO aan mijn SaaS toe te voegen?",
      "acceptedAnswer": { "@type": "Answer", "text": "SAML SSO kost doorgaans €2.500 tot €4.000 als uw app al organisaties en rollen heeft. Als die eerst moeten worden gebouwd, kost een gecombineerd project meestal €4.000 tot €6.000." }
    },
    {
      "@type": "Question",
      "name": "Wat kost een volledig enterprise-gereedheidspakket?",
      "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans €4.000 tot €7.500 binnen Launch & Grow, voor organisaties en rollen, SSO, auditlogs, een beveiligingsreview en documentatie voor het inkoopproces. SCIM, eigen rollen en de locatie van gegevens worden toegevoegd als dat nodig is." }
    },
    {
      "@type": "Question",
      "name": "Heb ik SCIM-provisioning nodig?",
      "acceptedAnswer": { "@type": "Answer", "text": "In het begin niet altijd. Veel enterpriseklanten accepteren just-in-time provisioning met een periodieke controle op verwijderde gebruikers." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij enterprisefuncties?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar software voor grote organisaties zoals Vodafone en TNO, over 160+ projecten, en de CEO was medeoprichter van een cybersecuritybedrijf. LaunchStudio gebruikt die ervaring om enterprisefuncties af te bakenen tot wat klanten werkelijk eisen." }
    },
    {
      "@type": "Question",
      "name": "Helpen enterprisefuncties bij mijn SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Pagina's over SSO-ondersteuning, beveiliging en integraties sluiten aan bij waar IT-kopers op zoeken en wat ze aan AI-antwoordmachines vragen." }
    }
  ]
}
</script>
