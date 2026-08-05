---
Titel: "Soft Delete vs. Hard Delete: De beslissing over het datamodel van AI-gegenereerde apps die niemand uitlegt"
Trefwoorden: ai database, ai code tool, soft delete, hard delete, data recovery
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Soft Delete vs. Hard Delete: De beslissing over het datamodel van AI-gegenereerde apps die niemand uitlegt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Soft Delete vs. Hard Delete: De beslissing over het datamodel van AI-gegenereerde apps die niemand uitlegt",
  "description": "AI-coderingsassistenten kiezen standaard voor permanente hard deletes op databaserijen.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/soft-delete-data-recovery-ai-generated-app"
  }
}
</script>

Er is een specifiek soort stilte die volgt nadat een gebruiker op "verwijderen" klikt voor het verkeerde item – de seconde waarin hij zich realiseert wat er net is gebeurd, en de volgende seconde waarin hij zich realiseert dat er geen ongedaan maken is. Als de verwijderknop van uw app een `DELETE FROM`-instructie rechtstreeks tegen de database uitvoert, is die stilte permanent. En het is een beslissing die uw AI-coderingsassistent vrijwel zeker voor u heeft gemaakt zonder het ooit te vermelden.

## Het verschil van één woord dat niemand markeert tijdens de ontwikkeling

Wanneer u een AI-coderingsassistent vraagt om "een verwijderfunctie toe te voegen" voor een record, is de meest rechtstreekse en veel voorkomende implementatie een harde verwijdering (hard delete): een SQL `DELETE`-instructie (of gelijkwaardige ORM-oproep) die de rij volledig uit de database verwijdert, onmiddellijk, zonder enig spoor achter te laten. Het is de eenvoudigste mogelijke interpretatie van "verwijderen", het doorstaat elke test – het record is weg, exact zoals gevraagd – en het werkt vlekkeloos tot het moment dat iemand het verkeerde item verwijdert.

Het alternatief, zachte verwijdering (soft delete), verwijdert de rij daadwerkelijk überhaupt niet. In plaats daarvan stelt het een vlag in – doorgaans een `deleted_at`-tijdstempelkolom – en elk onderdeel van de applicatie dat uit die tabel leest wordt bijgewerkt om rijen te filteren waar die vlag is ingesteld. Functioneel verdwijnt een zacht verwijderd record uit het zicht van de gebruiker exact hetzelfde als een hard verwijderd record. Het verschil doet er pas toe op het moment dat iemand het terug nodig heeft: een zacht verwijderd record kan in seconden worden hersteld door de vlag te wissen, terwijl een hard verwijderd record het herstellen uit een database-back-up vereist – als er een bestaat, als deze recent genoeg is, en als het herstellen ervan niet ook elke andere wijziging terugdraait die sinds die tijd is gemaakt.

## Waarom AI-tools standaard kiezen voor de verkeerde keuze, en wanneer het er daadwerkelijk toe doet

Zachte verwijdering is niet de standaard waar een AI-tool naar grijpt omdat het oprecht meer werk is: het betekent het toevoegen van een kolom, het bijwerken van elke enkele query tegen die tabel om gemarkeerde rijen uit te sluiten, en doorgaans het bouwen van een soort beheerdersinterface om zacht verwijderde records later te bekijken en te herstellen. Een prompt zoals "laat gebruikers een project verwijderen" communiceert niets van die complexiteit – het vraagt simpelweg om verwijdering, en de AI geeft u de eenvoudigste versie. De beslissing over welke geschikt is hangt volledig af van wat er wordt verwijderd: een zachte verwijdering is bijna verplicht voor alles met opeenvolgende relaties (een project met taken, een gebruiker met bestellingen), alles wat een gebruiker per ongeluk via een UI zou kunnen verwijderen, of alles met nalevingsgestuurde bewaarvereisten. Een oprecht wegwerpbaar record met een laag risico heeft het mogelijk helemaal niet nodig.

Dit is exact het soort datamodelleringsoordeel dat met AI gegenereerde code scheidt van productie-architectuur – niet een bug precies, maar een standaard die nooit daadwerkelijk is geëvalueerd tegen de echte kosten van het verkeerd krijgen ervan. LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering. Het beoordelen van verwijder-semantiek tegen de daadwerkelijke impact van elke tabel is een standaard onderdeel van hoe onze ingenieurs, werkend vanuit Manifera's kantoor in Amsterdam, het datamodel van een met AI gebouwde app voorbereiden op echte gebruikers.

Als u niet zeker weet welke van de verwijderfuncties van uw app harde verwijderingen zijn die wachten om een slechte dag te veroorzaken, is het de moeite waard om [uw datamodel te beoordelen met ons team](https://launchstudio.eu/en/#contact) voordat uw eerste echte gebruiker er op de harde manier achter komt.

## Zachte verwijdering breekt stilletjes unieke beperkingen (Unique Constraints)

Het omzetten van een tabel naar zachte verwijdering introduceert een probleem dat pas verschijnt zodra iemand iets probeert te hergebruiken waarvan hij denkt dat het weg is: een normale unieke beperking (unique constraint) op een kolom zoals `email` weet het verschil niet tussen een actieve rij en een zacht verwijderde rij. Een gebruiker die zijn account verwijdert en zich vervolgens opnieuw probeert aan te melden met hetzelfde e-mailadres stuit dus op een beperkingsschending op een record dat, vanuit het perspectief van het product, niet meer bestaat. Het account ziet er overal in de app verwijderd uit, maar de database bevat nog steeds de oude rij, en de unieke index ziet deze nog steeds.

Met AI gegenereerde migraties houden hier vrijwel nooit rekening mee, omdat de beperking werd geschreven voordat zachte verwijdering in het schema bestond. En niets dwingt een hernieuwde controle af zodra `deleted_at` wordt toegevoegd. De herstelling is een partiële unieke index die alleen uniekheid afdwingt onder actieve rijen, en niet alle rijen:

```
CREATE UNIQUE INDEX users_email_active_unique
ON users (email)
WHERE deleted_at IS NULL;
```

Hiermee aanwezig is het e-mailadres van een verwijderd account oprecht vrij om te hergebruiken, terwijl twee actieve accounts nog steeds niet kunnen botsen. Het is een kleine toevoeging, maar het is het soort ding dat alleen wordt opgevangen door iemand die bewust test op "verwijder een account, meld u dan opnieuw aan met hetzelfde e-mailadres" – een test die vrijwel niemand uitvoert totdat een echte gebruiker er op stuit en een verwarrende aanmeldingsfout krijgt in plaats van een vers account.

Het zelfde patroon verschijnt op elke kolom die uniek was voordat zachte verwijdering bestond – een werkruimte-slug, een uitnodigingscode, een subdomein – overal waar de app uniekheid belooft aan een gebruiker, maar de onderliggende beperking nooit is bijgewerkt om te begrijpen dat een zacht verwijderde rij niet zou moeten meetellen. Het auditeren van elke unieke beperking op een nieuw zacht te verwijderen tabel is wat voorkomt dat dit naar boven komt als een ondersteuningsverzoek maanden nadat de migratie is verzonden.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het project dat in één klik verdween

Daniël Wesseling, een oprichter in Emmeloord, bouwde ProjectVolg, een SaaS voor projectbeheer, met behulp van Lovable. De verwijderfunctie voor een project werkte betrouwbaar in elke test die Daniël uitvoerde tijdens de ontwikkeling: klik op verwijderen, bevestig, het project is weg. Schoon, eenvoudig, exact zoals bedoeld – omdat het in elke test Daniël was die een testproject verwijderde dat hij niet meer nodig had.

Het echte incident gebeurde toen een gebruiker, die een oud gearchiveerd project wilde verwijderen, per ongeluk op verwijderen klikte bij een actief project dat nog vol zat met openstaande taken. Het bevestigingsvenster bood niet genoeg pauze, en binnen seconden waren het project en elk van de geassocieerde taken permanent verdwenen uit de database – omdat de met AI gegenereerde verwijderfunctie een oprechte harde verwijdering had uitgevoerd, doordringend naar elke gerelateerde tabel zonder zachte-verwijderingsvlag om het op te vangen. Er was geen manier om het via de app zelf terug te brengen.

LaunchStudio herbouwde ProjectVolg's verwijderlogica rond een zachte-verwijderingspatroon: een `deleted_at`-tijdstempel op projecten en hun gerelateerde taken, elke bestaande query bijgewerkt om gemarkeerde records te filteren, en een eenvoudige beheerweergave voor "recent verwijderd" waar een project kon worden hersteld binnen een venster van 30 dagen voordat het permanent werd gewist op een schema. **Resultaat:** de allereerstvolgende per ongeluk uitgevoerde verwijdering, weken later, werd door de gebruiker zelf binnen een minuut hersteld, zonder enige betrokkenheid van engineering.

> *"Het verliezen van dat project leerde me op de harde manier dat 'verwijderen' en 'voor altijd weg' niet dezelfde knop zouden moeten zijn. Nu is het oprecht onmogelijk om per ongeluk gegevens te verliezen."*
> — **Daniël Wesseling, Oprichter, ProjectVolg (Emmeloord)**

**Kosten en tijdlijn:** € 750 (schema-migratie voor zachte verwijdering, query-updates, beheerweergave voor herstel) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Waarom kiezen AI-coderingsassistenten standaard voor harde verwijderingen in plaats van zachte verwijderingen?

Omdat een harde verwijdering de eenvoudigste, meest letterlijke interpretatie is van een verzoek om "verwijdering". Het correct bouwen van een zachte verwijdering vereist aanvullende schema-wijzigingen en query-updates die niet besloten liggen in een eenvoudige prompt.

### Welke tabellen in mijn app hebben daadwerkelijk zachte verwijdering nodig?

Alles met opeenvolgende relaties (cascading relationships), alles wat een gebruiker per ongeluk via de UI zou kunnen verwijderen, en alles met bewaar- of auditvereisten.

### Kan zachte verwijdering achteraf worden toegevoegd aan een app die al harde verwijderingen gebruikt?

Ja, hoewel het het toevoegen van de vlagkolom vereist en het auditeren van elke bestaande query tegen die tabel om ervoor te zorgen dat verwijderde rijen overal consistent worden gefilterd waar ze worden gelezen.

### Vertraagt het toevoegen van zachte verwijdering mijn databasequery's?

Over het algemeen niet betekenisvol – het filteren op een geïndexeerde `deleted_at`-kolom voegt verwaarloosbare overhead toe vergeleken met de kosten van een niet-herstelbare accidentele verwijdering.

### Als ik zachte verwijdering toevoeg, kan een verwijderde gebruiker zich dan opnieuw aanmelden met hetzelfde e-mailadres?

Niet automatisch – een standaard unieke beperking behandelt de oude, zacht verwijderde rij nog steeds als bezet. Deze moet dus worden vervangen door een partiële unieke index gericht op alleen actieve rijen, anders stuit het hergebruikte e-mailadres op een beperkingsfout.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen Hard Delete en Soft Delete in een database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hard Delete voert `DELETE FROM table` uit en wist data permanent. Soft Delete zet een `deleted_at` timestamp, waardoor data bewaard blijft maar verborgen wordt."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom kiezen Lovable en Cursor standaard voor Hard Delete?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat Hard Delete de meest eenvoudige SQL-code is om te genereren. Soft Delete vereist extra velden, query-filters en unieke index aanpassingen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met unieke velden (zoals e-mail) bij Soft Delete?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een standaard UNIQUE constraint blokkeert een nieuw account met hetzelfde e-mailadres. Je hebt een partiële index nodig (`WHERE deleted_at IS NULL`)."
      }
    },
    {
      "@type": "Question",
      "name": "Welke tabellen moeten verplicht Soft Delete gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tabellen met gekoppelde relaties (zoals Projecten -> Taken, Gebruikers -> Bestellingen) en alle data die een gebruiker per ongeluk via de UI kan wissen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost het migreren naar Soft Delete bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het migreren van je database-schema naar Soft Delete inclusief herstel-adminpaneel kost gemiddeld €750 en duurt 4 werkdagen."
      }
    }
  ]
}
</script>