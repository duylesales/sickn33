🚨 Arjen Wolters, ontwikkelaar en paardeneigenaar in Assen, bouwde Stallenlog in één lang weekend met Windsurf: pensionstallen beheren paarden, voerschema's, afspraken met hoefsmid en dierenarts en maandfacturen. Binnen twee maanden gebruikten 26 stallen en zo'n 700 eigenaren het. Toen kregen echte eigenaren facturen voor paarden met de naam "Test Horse 3". 😳

Het seedscript van de agent was tegen productie gedraaid — twee keer — omdat er één Supabase-project voor alles was. De Postmark-sleutel stond in een gecommit configuratiebestand. Routes controleerden op een sessie maar niet op lidmaatschap van een stal, dus eigenaren zagen paarden en dierenartsnotities van andere stallen. Het schema was afgeweken van de migraties, er waren 214 directe afhankelijkheden (vier kwetsbaar), en geen foutregistratie. Dit laat de agent achterwege als Windsurf-code naar productie gaat:

❌ Eén omgeving voor ontwikkeling, test en echte klanten
❌ Een geheim gecommit in de repository
❌ "Ingelogd" behandeld als "geautoriseerd"
❌ Schemadrift, wildgroei aan afhankelijkheden en stille fouten

✅ Aparte projecten voor ontwikkeling, staging en productie met eigen sleutels — Postmark-sleutel geroteerd
✅ Row level security per stal en eigenaar, met negatieve tests
✅ Een schone migratiebasis en 61 ongebruikte of dubbele afhankelijkheden verwijderd
✅ Sentry, uptimecontroles, en CI die merges blokkeert op tests, scannen op geheimen en meldingen over afhankelijkheden — plus een regelbestand voor Windsurf

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, voegen we de vangrails toe waarvan een agent niet weet dat hij ze nodig heeft. ⚙️

💡 Het resultaat: € 2.500, negen werkdagen. Arjen bouwt nog bijna alles met Windsurf, nu via pull requests die door CI worden bewaakt — en Stallenlog groeide naar 58 stallen zonder nieuwe lekken van testdata. 🚀

👉 AI-Code naar Productie met Windsurf: Wat de Agent Achterwege Laat: https://launchstudio.eu/nl/blog/ai-code-to-production-with-windsurf-what-the-agent-leaves-out

#Windsurf #AgenticCoding #Supabase #DevOps #LaunchStudio #Manifera
