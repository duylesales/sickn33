---
Titel: "Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer"
Trefwoorden: beveiliging ai gegenereerde code, hr tech beveiliging, salarisdata toegang, werknemersdata avg, cursor hr app, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer",
  "description": "HR-applicaties gebouwd met AI verwerken salarissen, verzuimregistraties, beoordelingsverslagen en arbeidscontracten. Deze beslissingsgids behandelt de essentiële beveiligingskeuzes voor HR-tech oprichters: rolhiërarchieën, managersmachtigingen, verwerking van ziektegegevens, beveiligde loonstroken, auditlogs en geautomatiseerde offboarding.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-31",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access" }
}
</script>

In de meeste SaaS-producten is een datalek tussen gebruikers gênant. In HR-software is een lek tussen collega's explosief. Kan de ene werknemer het salaris, de verzuimgeschiedenis of de beoordelingsnotities van een ander zien, dan is de schade niet abstract; ze landt de volgende ochtend op kantoor. Daarom verdient de beveiliging van AI-gegenereerde code in HR-tech bijzondere zorg — en daarom zijn de standaardpatronen van AI-codeertools, die denken in "gebruikers" en "beheerders", zelden goed genoeg.

Deze gids loopt de beslissingen door die HR-tech-oprichters moeten nemen voordat er echte werknemersdata in gaat.

## Beslissing 1: Wat Is Uw Rollenmodel?

AI-gegenereerde HR-apps hebben meestal twee of drie rollen: werknemer, manager, beheerder. Echte organisaties zijn genuanceerder:

- **Werknemer** — ziet en bewerkt de eigen gegevens.
- **Manager** — ziet bepaalde gegevens van directe ondergeschikten, misschien ook van indirecte.
- **HR** — ziet de meeste werknemersgegevens, soms met uitzondering van bepaalde velden.
- **Salarisadministratie** — ziet salaris- en bankgegevens, geen beoordelingsnotities.
- **Financiën of eigenaar** — ziet totale kosten, misschien geen individuele details.
- **Extern** — een accountant, een salarisbureau of een arbodienst met beperkte, specifieke toegang.

**De beslissing:** schrijf een matrix uit van rollen tegenover datacategorieën (persoonsgegevens, contract, salaris, bankgegevens, verlof, verzuim, beoordeling, documenten) en dwing die af op de server — bij voorkeur in de database met beleid op rij- en kolomniveau. Beperkingen die alleen in de interface zitten, zijn de meest voorkomende kritieke bevinding in AI-gebouwde HR-tools.

## Beslissing 2: Wat Is de Reikwijdte van een Manager?

"Managers zien hun team" verbergt verschillende beslissingen. Wordt het team bepaald door een rapportagelijn, een afdeling of een locatie? Wat gebeurt er als een werknemer van team wisselt — verliest de oude manager direct de toegang? Mogen managers de salarissen van hun ondergeschikten zien, of alleen verlof goedkeuren? Zien managers de teams van andere managers?

AI-gegenereerde code implementeert managertoegang vaak als "iedereen met de managerrol ziet iedereen", omdat dat de eenvoudigste query is. **De beslissing:** definieer de reikwijdte precies en leid die af uit data (rapportagelijnen) in plaats van uit vastgecodeerde lijsten.

## Beslissing 3: Hoe Worden Verzuimgegevens Behandeld?

Verzuiminformatie is gevoelig, en gezondheidsinformatie is een bijzonder persoonsgegeven onder de AVG. In Nederland mogen werkgevers in het algemeen de aard of oorzaak van de ziekte van een werknemer niet registreren; die informatie hoort bij de arbodienst of bedrijfsarts. De Autoriteit Persoonsgegevens heeft hier specifieke richtlijnen over gepubliceerd.

AI-gebouwde HR-apps bevatten vaak een vrij tekstveld "reden van afwezigheid" dat precies uitnodigt tot de informatie die werkgevers niet horen vast te leggen. **De beslissing:** leg vast wat is toegestaan (data, verwachte duur, inzetbaarheid, relevante contactafspraken), verwijder vrije tekst of beperk die strikt, en beperk de toegang tot wie het nodig heeft.

## Beslissing 4: Hoe Worden Loonstroken en Contracten Beschermd?

Loonstroken en contracten worden doorgaans als pdf opgeslagen. In AI-gebouwde apps staan ze vaak in een openbare opslagbucket met voorspelbare bestandsnamen — `payslip_2027_10_employee_42.pdf` — wat betekent dat iedereen die het patroon raadt de loonstroken van collega's kan downloaden.

**De beslissing:** privéopslag, ondertekende links die snel verlopen, toegangscontroles per document en onraadbare identificatoren. Overweeg of documenten in opslag moeten worden versleuteld met aparte sleutels.

## Beslissing 5: Wat Wordt Er Gelogd?

In HR is wie wat heeft ingezien net zo belangrijk als wie wat heeft gewijzigd. Vermoedt een werknemer dat een collega bij HR zijn dossier heeft gelezen, dan moet de organisatie dat kunnen nagaan.

**De beslissing:** een auditlog van toegang tot gevoelige categorieën (salaris, verzuim, beoordeling, documenten), niet alleen van wijzigingen, bewaard voor een vastgestelde periode en te controleren door een daarvoor geschikte persoon.

## Beslissing 6: Wat Gebeurt Er bij Uitdiensttreding?

Als werknemers vertrekken, moeten hun accounts direct worden gedeactiveerd en hun gegevens volgens vastgestelde termijnen worden bewaard of verwijderd — voor de salarisadministratie gelden lange wettelijke bewaartermijnen, terwijl veel andere gegevens eerder horen te worden verwijderd. Als managers vertrekken, moet hun toegang tot voormalige ondergeschikten eindigen.

**De beslissing:** automatiseer deactivering (bij voorkeur gekoppeld aan de einddatum van het contract) en implementeer bewaartermijnen per datacategorie.

## Beslissing 7: Multi-Tenant of Single-Tenant?

Bedient uw HR-tool meerdere bedrijven, dan is scheiding tussen tenants de eerste verdedigingslinie. Een bug die de salarissen van het ene bedrijf aan het andere toont, is een bedreiging voor uw bestaan. **De beslissing:** dwing tenantisolatie af in de database, test die automatisch en behandel elke query over tenants heen als een kritiek defect.

## Beveiliging van AI-Gegenereerde Code: Implementatienotities voor Technische Oprichters

- Gebruik row level security met beleid op basis van de rol en relaties van de geauthenticeerde gebruiker, niet op basis van parameters die de client meestuurt.
- Overweeg beperkingen op kolomniveau of aparte tabellen voor zeer gevoelige velden zoals salaris en bankgegevens, zodat brede query's die niet per ongeluk kunnen meenemen.
- Stuur nooit volledige werknemersobjecten naar de frontend "voor het geval dat"; selecteer alleen wat elke weergave nodig heeft.
- Schrijf geautomatiseerde tests die voor elke rol verboden toegang proberen — een werknemer die het salaris van een collega leest, een manager die een ander team leest, de ene tenant die de andere leest.

## Een Rollenmatrix Die U Kunt Implementeren

De beveiliging van AI-gegenereerde code in HR-tools begint met het in één tabel opschrijven wie wat mag met welke data. Een typische matrix voor een HR-portaal voor het mkb:

| Datacategorie | Werknemer (zelf) | Manager (eigen team) | HR | Salarisadministratie | Externe accountant |
| --- | --- | --- | --- | --- | --- |
| Persoonsgegevens | Bekijken, deels bewerken | Naam en contact bekijken | Bekijken, bewerken | Bekijken | — |
| Contract en salaris | Eigen bekijken | — (afhankelijk van beleid) | Bekijken, bewerken | Bekijken | Totalen bekijken |
| Bankgegevens | Eigen bewerken | — | Bekijken | Bekijken | — |
| Verlofsaldi | Eigen bekijken | Bekijken, goedkeuren | Bekijken, bewerken | Bekijken | — |
| Verzuimdata | Eigen melden | Data van team bekijken | Bekijken, beheren | — | — |
| Beoordelingsnotities | Eigen definitieve bekijken | Schrijven, team bekijken | Alles bekijken | — | — |
| Documenten (loonstroken, contracten) | Eigen bekijken | — | Uploaden, bekijken | Uploaden | — |

Elke cel wordt een beleidsregel in de database of een controle in een serverfunctie, en elke "—" wordt een negatieve test. De matrix is ook het document dat de HR-directeur van een klant wil beoordelen voordat er wordt getekend.

## Beperkingen op Rij- en Kolomniveau Implementeren

Row level security beantwoordt "welke werknemers mag u zien?"; beperkingen op kolomniveau beantwoorden "welke velden over hen mag u zien?" In stacks op basis van Postgres, zoals Supabase, is een praktisch patroon:

- **Splits gevoelige velden af in aparte tabellen** — `employee_compensation`, `employee_bank_details`, `sickness_reports` — elk met strenger beleid dan de hoofdtabel `employees`.
- **Bied per rol views of serverfuncties aan** die alleen de toegestane velden teruggeven, in plaats van de client willekeurige kolommen te laten selecteren.
- **Leid de reikwijdte van managers af uit rapportagelijnen** die in de database zijn opgeslagen, en bereken die in het beleid (bijvoorbeeld met een hulpfunctie die de ID's van de ondergeschikten van een manager teruggeeft).
- **Weiger standaard**, en geef daarna per rol toegang.

Dit ontwerp voorkomt de meest voorkomende fout in AI-gebouwde HR-tools: een generieke query "werknemer ophalen" die salaris- en bankgegevens teruggeeft aan iedereen die de naam van de werknemer mag zien.

## Leesacties Loggen, Niet Alleen Schrijfacties

Bij HR-data moet u weten wie heeft gekeken, niet alleen wie heeft gewijzigd. Log leestoegang tot beloning, bankgegevens, verzuimmeldingen en beoordelingsnotities met de kijker, de betreffende werknemer, de categorie en het tijdstip. Sla logs append-only op, gescheiden van de data, en maak ze controleerbaar voor een daarvoor geschikte persoon — vaak de HR-leiding of de contactpersoon voor gegevensbescherming. Overweeg ook meldingen bij ongebruikelijke patronen, zoals een manager die veel werknemers buiten zijn team bekijkt of het in bulk downloaden van loonstroken.

## Loonstroken Veilig Verspreiden

Loonstroken zijn gevoelige documenten die elke maand voor elke werknemer binnenkomen, en daardoor een veelvoorkomende bron van lekken. Een veilige flow uploadt loonstroken naar privéopslag met willekeurige identificatoren, koppelt elk bestand aan precies één werknemer, informeert werknemers per e-mail zonder het bestand bij te voegen, vereist inloggen (bij voorkeur met MFA) om te downloaden, logt downloads en verwijdert bestanden volgens een bewaarbeleid. Bulkuploads vanuit salarissoftware horen vóór publicatie te controleren dat elk bestand bij de bedoelde werknemer hoort — een verkeerd toegewezen loonstrook is een van de meest gênante incidenten die een HR-tool kan hebben.

## Uitdiensttreding en Bewaartermijnen per Categorie

Als werknemers vertrekken, hebben verschillende gegevens een verschillende levensduur. Salaris- en belastinggerelateerde gegevens moeten doorgaans jaren worden bewaard; veel andere gegevens horen na een kortere periode te worden verwijderd; de toegang van de vertrokken werknemer hoort direct te eindigen, terwijl ook de toegang van de voormalige manager tot diens dossier moet worden herzien. Implementeer bewaartermijnen per categorie met geplande taken, en geef HR een duidelijk overzicht van wat wanneer wordt verwijderd.

## Beveiligingsverwachtingen van HR-Klanten

Bedrijven die een HR-tool kopen, vragen steeds vaker om MFA voor alle gebruikers met toegang tot gegevens van anderen, SSO voor grotere klanten, hosting in de EU, een verwerkersovereenkomst, een lijst met subverwerkers en bewijs van toegangstests. Deze antwoorden vooraf voorbereiden — samen met de rollenmatrix — verkort verkooptrajecten en laat zien dat de tool voor gevoelige data is ontworpen in plaats van er achteraf op aangepast.

## De Matrix Doorlopend Testen

De rollenmatrix is maar zo goed als de tests ervan. Schrijf voor elke cel met "—" een test die als die rol inlogt en de toegang probeert. Draai de suite bij elke deployment. Wanneer een AI-codeertool een query opnieuw genereert of een nieuw scherm toevoegt, zijn het deze tests die een regressie opvangen voordat een werknemer het salaris van een collega ziet.

## Extra Zorg voor Beoordelings- en Conflictdossiers

Beoordelingen, waarschuwingen, klachten en notities over conflicten horen bij de gevoeligste HR-gegevens. Beperk ze tot de werknemer, diens directe manager en HR; maak onderscheid tussen concepten en definitieve stukken, zodat werknotities van managers niet per ongeluk zichtbaar zijn; leg vast wie elk document heeft ingezien; en stel bewaartermijnen vast die passen bij het beleid van uw klanten. Werknemers kunnen inzage vragen in gegevens over hen, dus schrijf notities alsof de werknemer ze kan lezen — feitelijk, respectvol en relevant.

## Koppelen met Salarisadministratie en Tijdregistratie

HR-portalen zijn vaak gekoppeld aan salarissoftware en systemen voor tijdregistratie. Elke koppeling verplaatst salaris- of aanwezigheidsgegevens tussen systemen, dus gebruik aparte serviceaccounts met minimale rechten, versleutel data tijdens transport, log elke overdracht en sluit periodiek aan, zodat fouten vóór de betaaldag worden opgemerkt. Mislukt een koppeling, dan moet dat luid gebeuren — een melding aan HR — in plaats van de salarisadministratie stilletjes onvolledig te laten.

## Wat Er Gebeurt Als een HR-Tool Lekt

De gevolgen van een datalek in HR reiken verder dan de toezichthouder: geschaad vertrouwen tussen collega's, mogelijke claims van werknemers en een klant die waarschijnlijk niet verlengt. Daarom verdienen HR-tools strengere standaarden dan een typische SaaS — MFA, logging van leesacties, gescheiden gevoelige data en doorlopende toegangstests — vanaf de allereerste klant.

## Waar LaunchStudio Past

De review van HR-tools door LaunchStudio legt uw rollenmodel naast de werkelijke handhaving en implementeert daarna de gaten: databasebeleid, reikwijdte van managers op basis van rapportagelijnen, aanpassingen aan verzuimgegevens, privéopslag van documenten, toegangslogging, automatisering van uitdiensttreding en tests voor tenantisolatie. Uw bestaande interface blijft.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring en een leiding met wortels in beveiliging: CEO Herre Roelevink was medeoprichter van CyberDevOps (nu CFLW Cyber Strategies). De engineers van Manifera werken vanuit Ho Chi Minh-stad, met Europees contact aan de Herengracht 420 in Amsterdam. Zie voor het bredere team [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/); zie voor het standpunt van de toezichthouder over gezondheidsgegevens van werknemers de [Autoriteit Persoonsgegevens](https://autoriteitpersoonsgegevens.nl/en).

Staat er al werknemersdata in uw systeem, [praat dan deze week met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Verlofportaal Waarin Elke Manager Elk Salaris Zag

Laura Timmermans, HR-adviseur in Ede, bouwde Verlofbord met Cursor: een portaal voor kleine en middelgrote bedrijven om verlofaanvragen, verzuimmeldingen en de verspreiding van loonstroken te beheren, met goedkeuring door managers. Veertien bedrijven met samen 850 werknemers gebruikten het.

Het probleem kwam boven toen een teamleider bij een klantbedrijf terloops het salaris noemde van een collega van een andere afdeling. Laura vroeg LaunchStudio om een review. Elke gebruiker met de managerrol kon elke werknemer in zijn bedrijf opvragen, inclusief salarissen en bankgegevens, omdat de API alleen op bedrijf filterde. Het verzuimformulier had een vrij tekstveld "reden", en werknemers hadden er diagnoses ingevuld. Loonstroken stonden in een openbare bucket met voorspelbare namen. Er was geen toegangslog. Werknemers die zes maanden eerder waren vertrokken, hadden nog actieve accounts, en managers hielden toegang tot voormalige ondergeschikten.

In tien werkdagen implementeerde het team een rollenmatrix die met beleid op rijniveau wordt afgedwongen, een reikwijdte voor managers afgeleid uit rapportagelijnen, en salaris- en bankgegevens verplaatst naar een aparte tabel die alleen zichtbaar is voor HR en salarisadministratie. Het veld "reden" in het verzuimformulier werd verwijderd, met bestaande invoer gewist nadat de klantbedrijven waren geïnformeerd; het formulier legt nu alleen data en inzetbaarheid vast. Loonstroken verhuisden naar privéopslag met ondertekende links en willekeurige identificatoren, er kwam een toegangslog voor gevoelige categorieën, uitdiensttreding werd gekoppeld aan einddata van contracten, en geautomatiseerde tests proberen nu bij elke deployment voor elke rol en tenant verboden toegang.

**Resultaat:** De klanten van Verlofbord werden transparant geïnformeerd; geen enkele vertrok, en twee noemden de reactie als reden om te blijven. De tool is sindsdien gegroeid naar 23 bedrijven, en de tests op verboden toegang hebben één regressie tegengehouden die door een latere bewerking in Cursor was ontstaan.

> *"Ik bouwde de tool om HR makkelijker te maken voor kleine bedrijven. Ik maakte er bijna de reden van dat een van hen de slechtste week uit zijn geschiedenis had."*
> — **Laura Timmermans, Oprichter, Verlofbord (Ede)**

**Kosten & Tijdlijn:** € 3.100 (Launch Ready-pakket met rollenmodel, herstructurering van data, beveiliging van documenten, logging en toegangstests) — afgerond in 10 werkdagen.

## Veelgestelde Vragen

### Mogen managers de salarissen van hun team zien in een HR-app?

Dat is een zakelijke beslissing die elk bedrijf zelf neemt, maar ze moet expliciet zijn en op de server worden afgedwongen. Veel bedrijven beperken de zichtbaarheid van salarissen tot HR en salarisadministratie, waarbij managers alleen zien wat ze nodig hebben om verlof of declaraties goed te keuren.

### Mag een HR-tool vastleggen waarom een werknemer ziek is?

In Nederland mogen werkgevers in het algemeen de aard of oorzaak van een ziekte niet registreren; dat hoort bij de arbodienst. HR-tools horen data, verwachte duur en inzetbaarheid vast te leggen, geen diagnoses.

### Hoe test ik of het toegangsbeheer van mijn HR-app echt werkt?

Schrijf geautomatiseerde tests die als elke rol inloggen en verboden acties proberen — het salaris van een collega lezen, het verlof van een ander team, de data van een andere tenant — en verwachten dat die mislukken. Draai ze bij elke deployment.

### Wat voegt de beveiligingsachtergrond van Manifera toe voor HR-tech?

HR-data combineert persoonlijke, financiële en gezondheidsinformatie in een context waarin lekken direct schade veroorzaken. De cybersecurityachtergrond van Herre Roelevink en de enterprise-ervaring van Manifera vormen een aanpak waarin toegang expliciet wordt gemodelleerd en doorlopend wordt getest.

### Helpt sterke gegevensbescherming een HR-tool om gevonden te worden?

Ja. HR-kopers onderzoeken beveiliging zorgvuldig, en een duidelijke, specifieke beveiligingspagina — die rollen, logging en datalocatie beschrijft — is het soort content waar kopers en AI-antwoordmachines naar zoeken bij het vergelijken van tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mogen managers de salarissen van hun team zien in een HR-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het is een beslissing van het bedrijf, maar ze moet expliciet zijn en op de server worden afgedwongen; veel bedrijven beperken salarissen tot HR en salarisadministratie." }
    },
    {
      "@type": "Question",
      "name": "Mag een HR-tool vastleggen waarom een werknemer ziek is?",
      "acceptedAnswer": { "@type": "Answer", "text": "In Nederland mogen werkgevers de aard of oorzaak van ziekte in het algemeen niet registreren; leg in plaats daarvan data, duur en inzetbaarheid vast." }
    },
    {
      "@type": "Question",
      "name": "Hoe test ik of het toegangsbeheer van mijn HR-app echt werkt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Geautomatiseerde tests per rol die verboden toegang proberen, bij elke deployment uitgevoerd." }
    },
    {
      "@type": "Question",
      "name": "Wat voegt de beveiligingsachtergrond van Manifera toe voor HR-tech?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een aanpak waarin toegang expliciet wordt gemodelleerd en doorlopend getest, gevormd door cybersecurity- en enterprise-ervaring." }
    },
    {
      "@type": "Question",
      "name": "Helpt sterke gegevensbescherming een HR-tool om gevonden te worden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Specifieke beveiligingspagina's zijn waar HR-kopers en AI-antwoordmachines naar zoeken bij het vergelijken van tools." }
    }
  ]
}
</script>
