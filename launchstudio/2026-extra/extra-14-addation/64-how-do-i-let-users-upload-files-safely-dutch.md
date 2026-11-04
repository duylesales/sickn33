---
Titel: "Hoe Laat Ik Gebruikers Veilig Bestanden Uploaden in Mijn AI-Gebouwde App?"
Trefwoorden: veilige bestandsuploads supabase, lovable bestand uploaden, privé storage-bucket, signed urls supabase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Laat Ik Gebruikers Veilig Bestanden Uploaden in Mijn AI-Gebouwde App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Laat Ik Gebruikers Veilig Bestanden Uploaden in Mijn AI-Gebouwde App?",
  "description": "Bestandsuploads zijn een van de riskantste functies in AI-gebouwde apps: openbare buckets, te raden paden, onbeperkte bestandsgroottes en gevaarlijke bestandstypen. Deze gids behandelt privébuckets, storagepolicies, signed URLs, validatie, beeldverwerking en bewaartermijnen in Supabase.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-12",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-let-users-upload-files-safely" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Storage access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" }
  ]
}
</script>

**Kort antwoord:** bewaar bestanden van gebruikers in een privé-bucket in Supabase Storage, orden de paden op organisatie- of gebruikers-ID, schrijf storagepolicies die uploaden en lezen alleen toestaan binnen de eigen map of organisatie van de gebruiker, lever bestanden via kortlevende signed URLs, en dwing limieten op bestandsgrootte en -type af op de bucket en op de server. Gebruik openbare buckets alleen voor bestanden die openbaar bedoeld zijn, zoals productfoto's in een openbare catalogus.

## Belangrijkste Punten

- **Bestandsuploads zijn een van de riskantste functies in AI-gebouwde apps:** openbare buckets, te raden paden, ontbrekende storagepolicies, onbeperkte groottes en gevaarlijke bestandstypen.
- **Supabase Storage heeft eigen toegangspolicies,** los van de policies op tabellen; beide moeten worden ingesteld.
- **Lever privébestanden via kortlevende signed URLs** die na een controle op eigendom worden gegenereerd.
- **Valideer type en grootte, wees voorzichtig met SVG en HTML, en verwijder metadata** zoals de gps-locatie uit foto's.
- **Bestanden zijn ook persoonsgegevens:** neem ze onder de AVG op in plannen voor verwijdering, bewaartermijnen en back-ups.

## De Risico's die AI-Builders Introduceren

| Standaard in veel AI-gebouwde apps | Risico |
| --- | --- |
| Openbare bucket voor alles | Iedereen met een link kan privédocumenten openen |
| Voorspelbare bestandsnamen (`invoice-1043.pdf`) | Links zijn te raden |
| Geen storagepolicies | Gebruikers kunnen bestanden van anderen overschrijven of verwijderen |
| Geen limieten op grootte | Opslagkosten en misbruik |
| Elk bestandstype geaccepteerd | Kwaadaardige bestanden, HTML of SVG met scripts die vanaf uw domein worden geserveerd |
| Originele foto's ongewijzigd opgeslagen | Locatiegegevens (EXIF) en enorme bestanden |

## Stap 1: Standaard Privébuckets

Maak privébuckets aan voor alles wat persoonlijk of zakelijk is: documenten, contracten, facturen, scans van identiteitsbewijzen, foto's van gebruikers. Gebruik openbare buckets alleen voor content die u ook op uw openbare website zou zetten.

## Stap 2: Gestructureerde Paden

Gebruik paden zoals `org/{organisation_id}/{record_id}/{random-name}.pdf`. Willekeurige bestandsnamen voorkomen raden; het voorvoegsel met de organisatie laat policies het eigendom controleren.

## Stap 3: Storagepolicies

Toegang tot storage wordt geregeld door policies op `storage.objects`, los van uw policies op tabellen. Sta toevoegen en lezen alleen toe waar de organisatie in het pad overeenkomt met een organisatie waar de gebruiker lid van is; beperk verwijderen tot eigenaren of beheerders.

## Stap 4: Signed URLs

Om een privébestand te tonen of te downloaden, maakt u na een controle van de toegang van de gebruiker een signed URL met een korte geldigheid, zoals een paar minuten. Sla signed URLs niet blijvend op in de database; genereer ze wanneer ze nodig zijn.

## Stap 5: Valideer Uploads

- Stel op de bucket een maximale bestandsgrootte en toegestane MIME-typen in
- Controleer type en grootte voor gevoelige flows nogmaals op de server
- Wees voorzichtig met SVG- en HTML-bestanden; lever ze als download of sta ze niet toe
- Verklein afbeeldingen en verwijder metadata, vooral locatiegegevens uit foto's van telefoons

## Stap 6: Bewaartermijnen en Verwijdering

Bestanden zijn ook persoonsgegevens. Verwijder ze wanneer het bijbehorende record of account wordt verwijderd, en leg bewaartermijnen vast. Onze [gids over AVG-verwijdering](https://launchstudio.eu/nl/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr) behandelt hoe storage past in verzoeken om gegevenswissing.

## Stap 7: Maak Er Back-ups Van

Databaseback-ups bevatten geen storage. Maak apart back-ups van bestanden die ertoe doen, zoals contracten en facturen.

## Hoe Toegangscontrole in Supabase Storage Werkt

Supabase Storage bewaart bestanden in buckets en houdt de metadata van bestanden bij in een tabel, `storage.objects`, die wordt beschermd door Row Level Security-policies. Een bucket kan openbaar zijn, wat betekent dat iedereen met de URL bestanden kan downloaden, of privé, wat betekent dat de toegang wordt geregeld door policies en signed URLs. De documentatie van Supabase over toegangscontrole in storage beschrijft hoe policies de bucket, het bestandspad en de gebruiker controleren. Omdat policies het pad kunnen inspecteren, kunt u met een mapstructuur zoals `org/{organisation_id}/...` regels schrijven als "leden van deze organisatie mogen bestanden in de map van de organisatie lezen".

## De Meest Voorkomende Kwetsbaarheden bij Uploads

| Kwetsbaarheid | Voorbeeld | Gevolg |
| --- | --- | --- |
| Openbare bucket voor privébestanden | Facturen opgeslagen in een openbare bucket | Iedereen met of die een link raadt, kan ze lezen |
| Voorspelbare paden | `/documents/1043/payslip.pdf` | Het systematisch afgaan van bestanden van andere gebruikers |
| Geen uploadpolicies | Elke gebruiker kan naar elke map schrijven | Bestanden van anderen overschrijven of in hun mappen plaatsen |
| Geen controle op type | HTML of SVG met scripts uploaden | Scripts die op uw domein worden uitgevoerd wanneer bestanden worden bekeken |
| Geen limieten op grootte | Uploads van meerdere gigabytes | Opslagkosten en denial of service |
| Langlevende links opgeslagen in de database | Signed URLs die maanden geldig zijn | Gedeelde of gelekte links blijven bruikbaar |

OWASP rekent verschillende hiervan tot gebrekkige toegangscontrole, het grootste risico in de Top 10 voor webapplicaties.

## Een Uploadflow Ontwerpen

Een veilige uploadflow werkt meestal zo: de gebruiker kiest een bestand; de app controleert voor het gemak grootte en type in de browser; de upload gaat naar een privébucket onder een pad met het ID van de gebruiker of organisatie en een willekeurige bestandsnaam; een storagepolicy staat het toevoegen alleen in dat pad toe; een databaserecord koppelt het bestand aan de eigenaar en het bedrijfsobject; en verwerking zoals het verkleinen van afbeeldingen of het verwijderen van metadata gebeurt in een serverfunctie voordat het bestand wordt gebruikt. Downloads vragen een signed URL aan bij een functie die eerst het eigendom controleert.

## Afbeeldingen: Verkleinen en Metadata

Foto's van telefoons zijn vaak groot en bevatten EXIF-metadata, waaronder gps-coördinaten, het apparaatmodel en tijdstempels. Originelen opslaan verspilt ruimte en kan laten zien waar foto's zijn gemaakt, wat woonadressen kan onthullen. Verklein afbeeldingen tot de formaten die uw app toont, zet ze om naar efficiënte formaten en verwijder metadata bij het uploaden. Dat verbetert prestaties en privacy tegelijk.

## Gevaarlijke Bestandstypen

Sommige bestanden kunnen code uitvoeren of content in browsers weergeven. HTML- en SVG-bestanden die vanaf uw domein worden geserveerd, kunnen scripts uitvoeren in de sessies van uw gebruikers. Blokkeer deze typen, tenzij uw app ze nodig heeft. Moet u ze toch accepteren, lever ze dan met headers die een download afdwingen in plaats van weergave, of vanaf een apart domein. Accepteer voor documenten de formaten die uw gebruikers echt nodig hebben, zoals PDF en gangbare afbeeldingstypen, en weiger de rest.

## Scannen op Virussen en Malware

Als gebruikers bestanden met elkaar delen, kunt u overwegen uploads op malware te scannen, vooral bij B2B-producten waarbij bestanden tussen bedrijven worden uitgewisseld. Scandiensten en open-source scanners kunnen na het uploaden in een achtergrondfunctie draaien en bestanden als schoon markeren voordat ze voor anderen beschikbaar worden. Voor veel oprichtersapps is dit optioneel; voor platforms waarop documenten worden gedeeld, is het een redelijke verwachting.

## Bestanden en de AVG

Geüploade bestanden bevatten vaak de gevoeligste persoonsgegevens in een app: scans van identiteitsbewijzen, loonstroken, medische brieven, contracten. Behandel ze daarnaar. Houd ze in EU-regio's, beperk de toegang tot wie die nodig heeft, neem ze op in functies voor het verwijderen en exporteren van gegevens, leg bewaartermijnen vast en maak er apart back-ups van, omdat databaseback-ups geen storage bevatten. Artikel 32 van de AVG vereist beveiliging die past bij het risico, en weinig dingen verhogen het risico meer dan identiteitsbewijzen in een openbare bucket.

## Een Praktische Indeling van Buckets

Een eenvoudige indeling dekt de meeste apps:

| Bucket | Zichtbaarheid | Inhoud | Patroon van het pad |
| --- | --- | --- | --- |
| `public-assets` | Openbaar | Logo's, marketingafbeeldingen, openbare productfoto's | `/{category}/{file}` |
| `user-files` | Privé | Avatars, persoonlijke uploads | `/{user_id}/{random}.{ext}` |
| `org-documents` | Privé | Contracten, facturen, gedeelde documenten | `/{org_id}/{object_id}/{random}.{ext}` |
| `archive` | Privé, beperkt | Kopieën van wettelijk verplichte documenten | `/{year}/{org_id}/{file}` |

Scheid buckets op gevoeligheid, zodat policies eenvoudig blijven en fouten in de ene bucket geen invloed hebben op een andere.

## Bestanden Migreren uit een Openbare Bucket

Als privébestanden al in een openbare bucket staan, migreer ze dan: maak een privébucket aan, kopieer bestanden met nieuwe willekeurige namen naar paden op basis van de eigenaar, werk de verwijzingen in de database bij, test downloads via signed URLs en verwijder daarna de openbare kopieën. Controleer of de openbare URL's zijn gedeeld of geïndexeerd; als gevoelige documenten zijn blootgesteld, beoordeelt u uw verplichtingen onder de AVG, waaronder mogelijk een melding bij de Autoriteit Persoonsgegevens binnen 72 uur.

## De Beveiliging van Uploads Testen

Test als twee gebruikers in verschillende organisaties: upload, toon, download en verwijder elkaars bestanden via de interface en de API; probeer niet-toegestane typen en te grote bestanden te uploaden; controleer dat foto's geen gps-metadata meer bevatten; bevestig dat signed URLs verlopen. Automatiseer de test op downloads tussen organisaties.

## Samenvatting

Privébuckets, paden op basis van eigenaar, storagepolicies, signed URLs, validatie, het verwijderen van metadata en opname in verwijdering en back-ups: zeven gewoonten die bestandsuploads veranderen van een veelvoorkomende bron van datalekken in een veilige functie.

## Prestaties en Kosten van Bestandsopslag

Bestanden bepalen de kosten van opslag en bandbreedte. Verklein afbeeldingen tot de formaten die uw app toont, comprimeer documenten waar mogelijk, gebruik een CDN voor openbare bestanden en stel cache-headers in voor bestanden die zelden veranderen. Voor privébestanden profiteren kortlevende signed URLs binnen hun geldigheid nog steeds van caching. Bekijk het opslaggebruik maandelijks; één functie die originele foto's van 12 megapixel opslaat, kan ongemerkt uw hele rekening domineren.

## Veelgemaakte Fouten

- Eén openbare bucket voor alles gebruiken omdat de preview werkte
- Signed URLs in de database opslaan alsof ze blijvend zijn
- Elk bestandstype toestaan "voor de flexibiliteit"
- Storage vergeten bij het verwijderen van gebruikersaccounts
- Aannemen dat databaseback-ups ook bestanden bevatten

## Verder Lezen

Zie onze gidsen over AVG-verwijdering in Supabase en over het maken van back-ups van de database van een Lovable-app voor de kant van verwijdering en back-ups bij het omgaan met bestanden.

## Vragen Voordat U Uploads Bouwt

Welke bestandstypen hebben gebruikers echt nodig? Hoe groot mogen bestanden zijn? Wie mag elk bestand zien, en hoe lang? Moeten bestanden buiten de app worden gedeeld? Moeten bestanden om wettelijke redenen worden bewaard? Worden bestanden gescand voordat anderen ze kunnen openen? Met duidelijke antwoorden zijn policies, limieten en bewaartermijnen eenvoudig te implementeren en makkelijk aan klanten uit te leggen.

## De Opbrengst

Veilige uploads beschermen de gevoeligste documenten van uw gebruikers en uw reputatie. Ze laten u ook met vertrouwen vragen van klanten over opslag beantwoorden: standaard privé, toegang alleen voor de eigenaar, kortlevende links en gedocumenteerde bewaartermijnen.

## Waar U Vandaag Begint

Maak een lijst van uw buckets en markeer elke bucket als openbaar of privé. Elke openbare bucket met persoonlijke of zakelijke documenten is uw eerste oplossing.

## Het Laten Oplossen

Het beveiligen van bestandsuploads is een van de meest voorkomende oplossingen van LaunchStudio, meestal een tot drie dagen binnen een Launch Ready-pakket. LaunchStudio wordt ondersteund door Manifera, vertrouwd door Vodafone, TNO en CFLW, waarvan de engineers veilige documentverwerking bouwen voor enterpriseklanten vanuit Amsterdam en Ho Chi Minh-stad; zie [het portfolio van Manifera](https://www.manifera.com/portfolio/). Supabase legt [toegangscontrole in storage](https://supabase.com/docs/guides/storage/security/access-control) uit in de documentatie.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Huurapp met Openbare Loonstroken

Bart Smulders bouwde Huurdossier in Bolt: huurders die reageren op huurwoningen uploaden één keer hun identiteitsbewijs, loonstroken en werkgeversverklaring, en delen daarna een dossierlink met verhuurders. Binnen twee maanden gebruikten zo'n 900 huurders in Eindhoven de app.

Een verhuurder merkte dat de links naar dossierbestanden eruitzagen als `/storage/v1/object/public/documents/1234/payslip.pdf`. Door het getal te wijzigen, opende hij de loonstroken van andere huurders. De bucket was openbaar, de paden waren opeenvolgende ID's, en er waren geen storagepolicies. Foto's van identiteitskaarten die met een telefoon waren gemaakt, bevatten bovendien locatiegegevens die lieten zien waar ze waren genomen.

LaunchStudio verplaatste alle documenten naar een privébucket met willekeurige bestandsnamen, migreerde de bestaande bestanden en werkte de verwijzingen bij, schreef storagepolicies zodat huurders alleen bij hun eigen map konden, implementeerde het delen van dossiers via tijdelijk geldige signed links die verhuurders via een deelpagina ontvingen, verwijderde metadata uit afbeeldingen, stelde limieten op grootte en type in en voegde het verwijderen van alle bestanden toe wanneer een huurder het account opheft. Bart documenteerde het incident en informeerde de betrokken gebruikers.

**Resultaat:** Na de oplossing was geen enkel bestand meer bereikbaar zonder toestemming. Bart voegde een openbare pagina toe die uitlegt hoe dossiers worden beschermd, en meerdere verhuurders noemden die als reden om links van Huurdossier te accepteren.

> *"Het hele punt van mijn app was gevoelige documenten op één veilige plek bewaren. Ze stonden op één plek. Die was alleen niet veilig."*
> - **Bart Smulders, Oprichter, Huurdossier (Eindhoven)**

**Kosten & Doorlooptijd:** €1.950 (Launch Ready-pakket: privéopslag, migratie van bestanden, storagepolicies, delen via signed links, verwijderen van metadata, limieten en verwijdering) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Zijn buckets in Supabase Storage standaard privé?

Dat kiest u bij het aanmaken van een bucket. Veel AI-gegenereerde opzetten maken openbare buckets aan, omdat previews daarmee makkelijk werken. Controleer elke bucket en maak alles wat persoonlijk of zakelijk is privé.

### Beschermen mijn RLS-policies op de database ook geüploade bestanden?

Nee. Storage heeft eigen policies op `storage.objects`. U heeft naast policies op tabellen ook storagepolicies nodig, bij voorkeur gebaseerd op hetzelfde eigendom van organisatie of gebruiker.

### Hoe lang moeten signed URLs geldig zijn?

Zo kort als praktisch mogelijk, vaak een paar minuten voor bekijken of downloaden. Genereer ze op verzoek na een controle van de toegang, in plaats van langlevende links op te slaan.

### Waarom verwijdert Manifera metadata uit geüploade afbeeldingen?

Omdat foto's van telefoons vaak gps-coördinaten en apparaatgegevens bevatten. De op beveiliging gerichte werkwijze van Manifera, gevormd door de cybersecurity-achtergrond van Herre Roelevink, behandelt metadata als persoonsgegevens die niet onnodig mogen worden opgeslagen of gedeeld.

### Kunnen blootgestelde bestanden in zoekmachines verschijnen?

Ja. Openbare bestanden waarnaar ergens wordt gelinkt, kunnen worden gecrawld en geïndexeerd, en sommige kunnen later in AI-gegenereerde antwoorden opduiken. Privébuckets en signed URLs voorkomen dat.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zijn buckets in Supabase Storage standaard privé?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat kiest u bij het aanmaken; AI-gegenereerde opzetten maken ze vaak openbaar, dus controleer en maak gevoelige buckets privé." }
    },
    {
      "@type": "Question",
      "name": "Beschermen mijn RLS-policies op de database ook geüploade bestanden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Storage heeft eigen policies op storage.objects nodig." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moeten signed URLs geldig zijn?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zo kort als praktisch mogelijk, vaak minuten, op verzoek gegenereerd na een controle van de toegang." }
    },
    {
      "@type": "Question",
      "name": "Waarom verwijdert Manifera metadata uit geüploade afbeeldingen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Foto's van telefoons bevatten gps- en apparaatgegevens; dat zijn persoonsgegevens die niet onnodig bewaard mogen worden." }
    },
    {
      "@type": "Question",
      "name": "Kunnen blootgestelde bestanden in zoekmachines verschijnen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Gelinkte openbare bestanden kunnen worden geïndexeerd; privébuckets en signed URLs voorkomen dat." }
    }
  ]
}
</script>
