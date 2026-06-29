# Social Media Post (Dutch): Deploying AI Agents to Production: Docker, Fly.io, and Railway

Vercel is fantastisch voor Next.js web-apps.
Vercel is verschrikkelijk voor Agentic AI.

Als u LangChain- of AutoGen-agenten bouwt die het web scrapen, code uitvoeren en 15 minuten nadenken om een complex probleem op te lossen, dan zal Vercel's Serverless time-out van 60 seconden uw app vernietigen.

U heeft een "Two-Tier" Architectuur nodig:
1️⃣ Control Plane: Next.js + Vercel voor de UI, Auth en Stripe.
2️⃣ Data Plane: Een stateful, langlopende Python/Node worker in een Docker-container, gehost op Fly.io of Railway.

De Control Plane plaatst de taak van de gebruiker in een Redis-wachtrij. De Data Plane (Docker-container) haalt de taak op, denkt 15 minuten na, en slaat het antwoord weer op in Supabase.

Stop met vechten tegen time-outs. Lees onze gids over het implementeren van AI-agenten in Docker op de LaunchStudio blog.

#LaunchStudio #Docker #Flyio #Railway #AIagents #AISaaS #Nextjs #DevOps
