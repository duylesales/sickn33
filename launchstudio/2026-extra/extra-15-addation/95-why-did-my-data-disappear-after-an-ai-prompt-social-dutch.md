🚨 Eva Kuipers bouwde Behandelbord met Lovable en Supabase: eenendertig diëtisten gebruiken het dagelijks voor cliëntdossiers, sessienotities en voedingsplannen van zo'n 2.600 cliënten. Op een avond vroeg Eva Lovable om "het notitieveld op te splitsen in aparte velden". 😳

De migratie droppte de tabel session_notes en maakte hem opnieuw aan - op productie. De volgende ochtend was elke eerdere sessienotitie weg. Er waren dagelijkse back-ups, maar geen point-in-time recovery, en sinds de laatste back-up was zo'n veertien uur aan nieuwe notities geschreven. Wat te doen als data verdwijnt na een AI-prompt: 🧠

❌ De builder rechtstreeks gekoppeld aan de productiedatabase
❌ Een drop-en-opnieuw-aanmaken-migratie die niemand had gereviewd
❌ Geen point-in-time recovery
❌ Gezondheidsgegevens kwijt, met AVG-verplichtingen om te beoordelen

✅ Wijzigingen gestopt, het incident vastgelegd en diëtisten geïnformeerd
✅ De back-up teruggezet in een apart project en notities in de nieuwe structuur gezet, met behoud van nieuwere notities
✅ Notities uit de tussenliggende uren hersteld uit API-logs
✅ Staging voor Lovable, PITR, migratiereview, beperkte toegang en soft deletes

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, herstellen we zorgvuldig - en zorgen we dat één prompt nooit meer het werk van uw klanten kan wissen. 🛠️

💡 Het resultaat: €3.400, 8 werkdagen, met de data op dag twee terug. 99,6% van de eerdere notities kwam terug, elke diëtist bleef, en de review ving het jaar daarna twee riskante migraties. 🚀

👉 Data kwijt na een AI-prompt? Zo herstelt en voorkomt u het: https://launchstudio.eu/nl/blog/why-did-my-data-disappear-after-an-ai-prompt

#DataRecovery #Backups #Lovable #HealthTech #AIFounder #LaunchStudio #Manifera
