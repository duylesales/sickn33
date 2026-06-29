---
Title: Foutopsporing en Waarschuwingen voor AI Apps met Sentry
Keywords: Foutopsporing, Waarschuwingen, AI, Apps, Sentry, Monitoring
Buyer Stage: Bewustzijn
---

# Foutopsporing en Waarschuwingen voor AI Apps met Sentry

Uw AI SaaS-product staat live. Gebruikers uploaden PDF's en uw RAG-pijplijn extraheert netjes inzichten. Dan ontvangt u een boze e-mail van een zakelijke klant: *"De AI weigert ons financiële rapport van het derde kwartaal te analyseren. Er staat alleen maar 'Genereren...' en dan loopt het vast."* U controleert de Supabase database logs—niets. U controleert de Vercel logs—niets. Zonder het specifieke PDF-bestand te hebben (wat de klant u vanwege vertrouwelijkheid niet mag opsturen), heeft u geen idee waarom de applicatie faalde. Was het een parserfout? Was de payload te groot voor OpenAI? In AI-ontwikkeling komen stille storingen vaker voor dan harde crashes. Om dit te overleven, moet u enterprise-grade **Foutopsporing en Waarschuwingen implementeren met Sentry**.

## De 3 Soorten AI-fouten

Een standaard CRUD-applicatie crasht meestal vanwege een null-pointer of een ontbrekende databasekolom. AI-applicaties falen op veel uniekere en stillere manieren:

**1. Parserfouten in de verwerkingspijplijn:** De gebruiker uploadt een PDF, maar deze is gecodeerd in een vreemd formaat. De bibliotheek `pdf2json` verwerkt het document in stilte als een lege string. De AI krijgt nul context en "hallucineert" een antwoord omdat het de bron niet kan "zien". Dit resulteert in geen 500 serverfout, maar wel in een 0% nauwkeurigheidsgraad voor de klant.

**2. LLM Time-outs en Rate Limits:** U overschrijdt uw Tokens-Per-Minuut (TPM) limiet op OpenAI, of Anthropic beleeft een degradatie-incident en het antwoord duurt 45 seconden, waardoor uw Vercel Edge Function een time-out krijgt.

**3. Ongeldige JSON-uitvoer:** U instrueerde het model om een stricte JSON te retourneren, maar het model hallucineerde en voegde `'''json` markdown-tags toe, waardoor uw `JSON.parse()` logica in de backend brak.

## Sentry integreren in de Next.js AI Stack

Sentry is de industriestandaard voor foutopsporing (error tracking). Het vangt ongehandelde uitzonderingen op (exceptions), legt de volledige stacktrace vast en stuurt deze naar een centraal dashboard.

Maar u kunt Sentry niet zomaar installeren en het erbij laten. U moet **context verrijken**.

```typescript
import * as Sentry from "@sentry/nextjs";

export async function processPDF(fileBuffer, userId, orgId) {
  try {
    const text = await parsePDF(fileBuffer);
    
    // Vang stille parserfouten op
    if (text.length === 0) {
      Sentry.captureMessage("PDF Parsing yielded empty text", {
        level: "warning",
        extra: { userId, orgId, fileSize: fileBuffer.length }
      });
      throw new Error("Empty document");
    }

    const aiResponse = await generateSummary(text);
    return aiResponse;

  } catch (error) {
    // Koppel de fout aan de specifieke gebruiker voor klantenondersteuning
    Sentry.setUser({ id: userId });
    Sentry.setTag("organization_id", orgId);
    Sentry.captureException(error);
    
    throw error;
  }
}
```

Wanneer de zakelijke klant nu klaagt over zijn financiële rapport van het derde kwartaal, opent u Sentry, filtert u op hun `organization_id` en ziet u onmiddellijk dat de parser een leeg document retourneerde vanwege wachtwoordbeveiliging op de PDF. U lost de bug op in plaats van in het duister te tasten.

## Alarmen Instellen: Wanneer wordt u wakker gebeld?

U moet niet de hele dag naar het Sentry-dashboard staren, en u mag ook niet overspoeld worden met meldingen telkens wanneer één gebruiker een kapotte PDF uploadt.

U moet slimme waarschuwingsregels instellen:

1. **Slack-melding:** Als de bug *Nieuw* is (Sentry heeft deze specifieke fout nog nooit eerder gezien), stuur dan een melding naar het `#engineering-fouten` kanaal.
2. **Kritiek Alarm (PagerDuty/Telefoon):** Als het percentage `429 Too Many Requests` fouten van de OpenAI API de 5% in 5 minuten overschrijdt, bel dan onmiddellijk de hoofdontwikkelaar. Uw rate limits worden maximaal benut en de app is in wezen down.

## Prestatiebewaking (Tracing)

Naast foutopsporing kan Sentry ook API-latenties volgen (hoe lang het duurt om een functie uit te voeren). Door uw LLM-aanroepen met Sentry spans te instrumenteren, kunt u de "P95 TTFT" (Time To First Token) visueel bewaken. Als u de backend-prompt wijzigt en plotseling de P95-latentie toeneemt van 1,2 seconden naar 3,5 seconden, zal de prestatiebewaking van Sentry dit onmiddellijk aantonen.

## De LaunchStudio-aanpak

Bij LaunchStudio implementeren we geen code in productie tenzij het volledig observeerbaar is. Als integraal onderdeel van ons ontwikkelingsproces integreren we Sentry diep in uw Next.js en Supabase stack. We configureren de waarschuwingsregels, instrumenteren de RAG-pijplijnen om stille parsingsfouten op te vangen en koppelen het direct aan uw Slack-werkruimte. We zorgen ervoor dat wanneer er iets misgaat in uw AI-product, u niet alleen weet *dat* het kapot is, maar ook *waarom* en *hoe* u het binnen enkele minuten kunt repareren.

---

*Is uw engineeringteam blind voor productie AI-fouten? LaunchStudio installeert uitgebreide foutopsporings- en waarschuwingsinfrastructuur in Next.js AI-applicaties. [Laten we de kwaliteit van uw product beveiligen](https://launchstudio.eu/en/).*
