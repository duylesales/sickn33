---
Title: Real-Time Samenwerking in AI Apps met WebSockets
Keywords: Real-Time, Samenwerking, AI, Apps, WebSockets, Yjs, CRDT
Buyer Stage: Bewustzijn
---

# Real-Time Samenwerking in AI Apps met WebSockets

Als uw AI-toepassing succesvol is, zal deze op de werkvloer van een onderneming terechtkomen. En in een onderneming werkt niemand alleen. Twee marketingmanagers willen de door de AI gegenereerde campagnekop tegelijkertijd in hetzelfde document bewerken. Als uw app afhankelijk is van standaard HTTP `POST` verzoeken om de database bij te werken, zullen ze elkaars werk overschrijven en de gevreesde "Save Conflict" fout veroorzaken. Om een echt multiplayer, AI-native product te bouwen, moet u afscheid nemen van de HTTP request/response-cyclus en de wereld van **WebSockets en CRDT's** betreden.

## De Beperkingen van HTTP voor Multiplayer AI

Traditionele web-apps worden gebouwd op een stateless protocol: HTTP. U haalt de pagina op, bewerkt de tekst en verzendt deze terug. 

Voor multiplayer-samenwerking (zoals Google Docs) is dit fataal. Als Gebruiker A en Gebruiker B tegelijkertijd bewerken, wie "wint" er dan wanneer ze op opslaan klikken? Wat gebeurt er als de AI tegelijkertijd tekst rechtstreeks in het document streamt (bijv. GitHub Copilot)? U krijgt racecondities die leiden tot corruptie van documenten.

Bovendien is poling (elke seconde controleren of er wijzigingen zijn) een ramp voor de prestaties, vooral wanneer u betaalt voor serverloze rekenkracht.

## De WebSockets Oplossing

WebSockets bieden een persistente, bidirectionele verbinding tussen de client en de server. In plaats van bestanden over te sturen, streamen u en de server voortdurend delta's (kleine wijzigingen).

"Gebruiker A typte een 'h' op index 4."
"De AI voegde een alinea in op index 100."

Wanneer deze delta's onmiddellijk over de socket worden uitgezonden, ziet elke verbonden client dat de cursors over het scherm vliegen in realtime.

## CRDT's: De Magie Achter Multiplayer

WebSockets verplaatsen de data, maar ze lossen de conflicten niet op. Wat als Gebruiker A een alinea verwijdert, terwijl de AI precies in diezelfde alinea nieuwe tekst streamt? De server ontvangt conflicterende commando's met een milliseconde verschil.

De oplossing is **Conflict-Free Replicated Data Types (CRDTs)**. Dit zijn complexe datastructuren die wiskundig garanderen dat alle clients uiteindelijk in exact dezelfde staat zullen convergeren, ongeacht de volgorde waarin ze updates ontvangen, of de tijdelijke netwerkuitval.

Het industriestandaard open-source CRDT-raamwerk voor JavaScript is **Yjs**.

## Architectuur met Next.js, Yjs en Supabase

Het implementeren van Yjs in een moderne AI-stack vereist specifieke infrastructuur, omdat Vercel Serverless Functions niet goed overweg kunnen met langlopende WebSocket-verbindingen.

Hier is de correcte multiplayer architectuur:

### 1. De Backend (Hocuspocus + Fly.io)
U kunt geen WebSockets hosten op Vercel. U moet een langlopende Node.js-server (met behulp van een framework als Hocuspocus of een aangepaste Y-Websocket-server) implementeren op een platform als Fly.io of Railway.

Deze server houdt het hoofddocument in het geheugen, synchroniseert met alle verbonden clients en slaat periodiek de binaire Yjs-status op in uw Supabase Postgres-database.

### 2. De Frontend (Next.js + Tiptap)
Aan de kant van de client gebruikt u een framework voor een teksteditor dat Yjs standaard ondersteunt. **Tiptap** is hier de gouden standaard voor React-applicaties. U bindt Tiptap aan de Yjs-provider:

```javascript
import * as Y from 'yjs'
import { HocuspocusProvider } from '@hocuspocus/provider'
import { useEditor } from '@tiptap/react'

const ydoc = new Y.Doc()
const provider = new HocuspocusProvider({
  url: 'wss://your-fly-io-server.com',
  name: 'document-123',
  document: ydoc,
})

// Tiptap synchroniseert nu out-of-the-box met alle andere gebruikers
```

### 3. De AI-deelnemer (Server-Side Client)
Dit is waar AI-applicaties echt krachtig worden. De AI is niet zomaar een API-call; het is **een gebruiker in de kamer**.

Wanneer een mens om een LLM-samenvatting vraagt, maakt uw Node.js worker verbinding met de WebSocket-server, instantieert een Yjs-client en begint tokens (terwijl ze uit OpenAI stromen) rechtstreeks in het document te schrijven alsof het een mens met een eigen cursor is. Hierdoor kunnen mensen zien hoe de AI aan het schrijven is, en de AI corrigeren en bewerken voordat deze klaar is!

## Prestaties & Schaling

CRDT's (met name de geschiedenis van elke toetsaanslag) verbruiken RAM. Na verloop van tijd kan de Yjs binaire blob megabytes groot worden voor één enkel document. U moet de WebSocket-server configureren om periodiek de Yjs-geschiedenis te "prunen" en deze in een platte string in de database weg te schrijven, anders zullen uw servers zonder geheugen komen te zitten.

## De LaunchStudio-aanpak

Bij LaunchStudio verheffen we AI SaaS van tools voor één speler naar professionele platforms voor bedrijven. We integreren Tiptap en Yjs in uw Next.js frontend en implementeren speciale, sterk schaalbare Hocuspocus WebSocket-servers op Fly.io om de multiplayer state te beheren. We zorgen ervoor dat uw AI-agenten en menselijke gebruikers in perfecte harmonie kunnen samenwerken, de cursors tegelijkertijd over het scherm dansen, zonder enige save-conflicten.

---

*Wilt u Google Docs-stijl multiplayer samenwerking toevoegen aan uw AI-product? LaunchStudio bouwt schaalbare WebSocket en CRDT-infrastructuren. [Neem contact op](https://launchstudio.eu/en/).*
