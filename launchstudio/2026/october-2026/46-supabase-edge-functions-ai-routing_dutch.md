---
Titel: Hoe een App te Bouwen Met AI en te Beveiligen via Supabase
Trefwoorden: app bouwen met ai, Supabase Edge Functions, LLM routing, AI beveiliging, maatwerk backend, LaunchStudio, Manifera, API sleutel beveiliging, Next.js, Deno
Koperfase: Beslissing
Doelpersona: B (Technische Solo-Oprichter)
---

# Hoe een App te Bouwen Met AI en te Beveiligen via Supabase

Wanneer technische solo-oprichters hun eerste AI-app bouwen met Next.js, is de architectuur vaak gevaarlijk eenvoudig. Ze sturen tekst van de frontend direct naar de OpenAI API via een API-sleutel in hun `.env.local`-bestand.

Dit werkt prima op een lokale machine, maar in productie geeft u in feite uw creditcard aan de hele wereld.

Wanneer een API-sleutel zichtbaar is in de browser, kan iedereen deze kopiëren via de Chrome Developer Tools en op uw kosten scripts draaien. Audits tonen aan dat 45% van de AI-code beveiligingslekken bevat. Zonder server-side tussenpersoon kunt u geen verbruiksfacturering instellen, geen persoonsgegevens (PII) maskeren en misbruik niet beperken.

U heeft een veilige tussenpersoon nodig: **Supabase Edge Functions**.

## Waarom Frontend AI-Routing Faalt bij Schalen

1. **Geen Zicht op Facturering:** Als de frontend direct communiceert met OpenAI, weet uw database niet hoeveel tokens er zijn verbruikt.
2. **Vendor Lock-In:** Als OpenAI-calls in 20 frontend-componenten staan gehardcodeerd, vereist de overstap naar een goedkoper model een zware herschrijving.
3. **AVG-Aansprakelijkheid:** Als gebruikers gevoelige gegevens typen en de frontend deze direct naar de AI stuurt, pleegt u een AVG-overtreding.

## De Oplossing met Supabase Edge Functions

**Supabase Edge Functions** zijn server-side TypeScript-scripts op het Deno-netwerk. De frontend praat met de Edge Function, en de Edge Function communiceert met OpenAI.

Dit biedt de volgende voordelen:
- **Sleutelbeheer:** Sleutels staan in de kluis van Supabase en bereiken de browser nooit.
- **Controle Vóór Uitvoering:** De Edge Function controleert het `credit_balance` in Supabase en wijst het verzoek af bij nul saldo (402-status).
- **Dynamische LLM-Routing:** Stuur simpele verzoeken naar goedkope modellen (`gpt-4o-mini`) en ingewikkelde taken naar zwaardere modellen.
- **PII-Maskering:** Anonimiseer namen en e-mails server-side voordat het verzoek naar de AI-provider gaat.
- **Snelheidsbeperkingen (Rate Limiting):** Beperk het aantal verzoeken per gebruiker centraal op het serverniveau.

## De Tussenpersoon Bouwen met LaunchStudio

Het bouwen van een Edge Function die race-condities bij credits voorkomt, is uitdagend.

> "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën en producten om te zetten in software. Het gaat nu om de architectuur en de beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring met precies dat." — Herre Roelevink, Oprichter & Directeur, Manifera

Ondersteund door de senior backend-engineers van [Manifera](https://www.manifera.com/) (gevestigd in Amsterdam en Ho Chi Minh City) bouwt [LaunchStudio](https://launchstudio.eu/en/) veilige LLM-routinginfrastructuur. Wij stellen CORS-headers in, schrijven PII-maskeringsmiddleware en implementeren atomaire database-transacties.

## Belangrijkste Inzichten

- Roep een LLM API nooit rechtstreeks aan vanuit de frontend om sleuteldiefstal te voorkomen.
- Supabase Edge Functions fungeren als een veilige server-side tussenpersoon op het Deno-netwerk.
- Edge Functions maken Pre-Flight facturatiecontroles, PII-maskering en dynamische routing mogelijk.
- LaunchStudio biedt de enterprise-engineering om Edge Function-architecturen veilig uit te rollen.

## Echt Voorbeeld

### Een AI-Native Oprichter in Actie: De Medische Vertaal-App

Jonas, een ontwikkelaar in Berlijn, bouwde een AI-vertaal-app voor artsen. Artsen typte Duitse medische notities in om overzichten te genereren via de Anthropic API.

Jonas riep Anthropic direct aan vanuit de React-frontend. Binnen een maand ontdekte een student de API-sleutel in de netwerk-tab en gebruikte deze om 40 boeken te vertalen, wat Jonas een rekening van €2.200 opleverde. Bovendien stuurde hij patiëntennamen onversleuteld door (een ernstige AVG-overtreding).

Jonas schakelde **LaunchStudio (door Manifera)** in.

We herbouwden zijn routing-laag via Supabase Edge Functions. We beveiligden de sleutels in de kluis van Supabase en bouwden een Edge Function die het abonnement verifieerde en patiëntennamen en geboortedata anonimiseerde *voordat* de tekst naar Anthropic ging.

**Resultaat:** Sleutels waren onzichtbaar voor de frontend. Door het verwijderen van PII slaagde Jonas voor een data-audit van een Berlijns ziekenhuis en sloot een enterprise-contract van €40.000. *"LaunchStudio's Edge Function-architectuur heeft mijn bedrijf gered."*

**Kosten & Doorlooptijd:** €3.500 (Edge Function Routing & PII-Sanering) — afgerond in 8 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### 1. Wat is een "Edge Function" precies?
Een klein, snel backend-script op het Deno-netwerk dat op servers dicht bij de gebruiker draait. Het onderschept verzoeken van de frontend en verwerkt logica veilig voordat het met externe API's communiceert.

### 2. Waarom Supabase Edge Functions gebruiken in plaats van AWS Lambda?
Als uw database in Supabase staat, integreren Edge Functions automatisch met de authenticatie van uw gebruikers, zonder dat u complexe AWS IAM-rollen hoeft in te stellen.

### 3. Hoe streamt een Edge Function AI-antwoorden?
Edge Functions ondersteunen Server-Sent Events (SSE). Onze engineers schrijven code die de "typ-animatie" veilig van een LLM doorstuurt naar de frontend.

### 4. Vertraagt een tussenpersoon de applicatie?
Nauwelijks. Edge Functions voegen een verwaarloosbare vertraging toe (vaak <50ms), wat opweegt tegen de beveiliging en nauwkeurige facturering.

### 5. Schrijft LaunchStudio mijn Supabase Edge Functions voor mij?
Ja. Onze backend-engineers schrijven de TypeScript-code, verwerken de LLM-routing en PII-maskering, en rollen deze direct uit op uw Supabase-project.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een 'Edge Function' precies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een snel backend-script op Deno-servers dicht bij de gebruiker. Het verwerkt verzoeken van de frontend veilig voordat het met externe API's communiceert."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom Supabase Edge Functions gebruiken in plaats van AWS Lambda?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Supabase Edge Functions integreren direct met uw Supabase-database en authenticatie, wat complexe AWS-configuraties overbodig maakt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe streamt een Edge Function AI-antwoorden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via Server-Sent Events (SSE) wordt de typ-stream van een LLM in real-time en veilig doorgegeven aan de frontend van de gebruiker."
      }
    },
    {
      "@type": "Question",
      "name": "Vertraagt een tussenpersoon de applicatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nauwelijks. De vertraging is vaak onder 50ms, wat een minimale prijs is voor het beveiligen van API-sleutels en facturering."
      }
    },
    {
      "@type": "Question",
      "name": "Schrijft LaunchStudio mijn Supabase Edge Functions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Wij schrijven de TypeScript-code, regelen de LLM-routing en PII-maskering en richten het uit op uw Supabase-project."
      }
    }
  ]
}
</script>
