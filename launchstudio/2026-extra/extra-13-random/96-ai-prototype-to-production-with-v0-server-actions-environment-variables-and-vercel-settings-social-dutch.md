🚨 Olaf Terlouw, penningmeester van een voetbalclub in Maarssen met een achtergrond in webontwikkeling, bouwde Sportveldhuur met v0: clubs verhuren ongebruikte velden en trainingsslots aan andere teams en bedrijven, met online boeken en betalen. Negen clubs in de regio Utrecht gebruikten het. Toen merkte een huurder die zelf ontwikkelaar was dat hij boekingen van andere teams kon annuleren - de annuleeractie accepteerde elk boekings-ID. 😳

Vier Server Actions controleerden alleen op een ingelogde sessie. De geheime Stripe-sleutel had tijdens het debuggen het voorvoegsel NEXT_PUBLIC_ gekregen en stond in de browserbundle. Preview-deployments gebruikten productievariabelen en waren openbaar bereikbaar. En een gecachet clubdashboard met omzetcijfers werd na een deploy kort aan de penningmeester van een andere club getoond. Dit hebben v0-apps nodig voor Server Actions, omgevingsvariabelen en Vercel-instellingen:

❌ Server Actions behandeld als privéfuncties
❌ Een geheim blootgesteld via het voorvoegsel NEXT_PUBLIC_
❌ Openbare previews die op productievariabelen draaien
❌ Persoonlijke pagina's gecachet en aan de verkeerde gebruiker getoond

✅ Controles op eigendom en rol met Zod-validatie in elke Server Action
✅ De Stripe-sleutel geroteerd en verplaatst naar code die alleen op de server draait
✅ Omgevingsvariabelen in Vercel per omgeving gesplitst, previews op een stagingdatabase met deployment protection
✅ Persoonlijke dashboards als dynamisch gemarkeerd, gepoolde databaseverbindingen in de EU met row level security, headers en monitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat elk formulier in uw v0-app een deur is die controleert wie er klopt. ⚙️

💡 Het resultaat: € 2.300, acht werkdagen. Geen onbevoegde annuleringen of blootstelling tussen clubs meer, Sportveldhuur breidde uit naar 16 clubs, en Olaf bouwt nog steeds nieuwe schermen in v0 - vóór elke deploy getoetst aan de checklist. 🚀

👉 Van AI-prototype naar productie met v0: Server Actions, omgevingsvariabelen en Vercel-instellingen: https://launchstudio.eu/nl/blog/ai-prototype-to-production-with-v0-server-actions-environment-variables-and-vercel-settings

#v0 #Vercel #NextJS #ServerActions #LaunchStudio #Manifera
