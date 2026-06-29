---
Title: Optimalisatie van Vercel Edge-functies voor LLM-reacties met lage latentie
Keywords: Vercel, Edge-functies, LLM, Latentie, Streaming
Buyer Stage: Overweging
---

# Optimalisatie van Vercel Edge-functies voor LLM-reacties met lage latentie

De gebruikerservaring in AI-producten is afhankelijk van de waargenomen snelheid. Als een gebruiker meer dan 2 seconden wacht, gaat hij ervan uit dat uw app kapot is.

## Waarom Edge-functies?
Traditionele Serverless-functies hebben last van koude starts. Edge-functies worden wereldwijd uitgevoerd, dicht bij de gebruiker, met vrijwel geen opstarttijd.

## Implementatie
Forceer de runtime naar de Edge bij het implementeren van de Vercel AI SDK. Dit garandeert wereldwijd een Time-to-First-Byte (TTFB) van minder dan 500 ms.
