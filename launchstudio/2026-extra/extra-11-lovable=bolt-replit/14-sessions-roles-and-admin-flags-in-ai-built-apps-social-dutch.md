🔒 Marijn Kuipers bouwde DierZorg in Lovable voor 11 dierenklinieken rond Apeldoorn. Vlak voor een belangrijke samenwerking bleek uit een security audit dat medewerkers van Kliniek A patiëntendossiers en facturen van Kliniek B konden inzien door simpelweg een ID-parameter in de browser aan te passen. 😳

Inloggen is iets anders dan autorisatie. Waar het vaak misgaat bij gebruikersrollen en rechten in AI-apps:

❌ Vertrouwen op een simpele `is_admin` boolean in een door gebruikers aanpasbaar profiel
❌ Geen strikte scheiding tussen verschillende organisaties (multi-tenancy) op databaseniveau
❌ Rollen opslaan in de browser-storage waar ze handmatig bewerkt kunnen worden
❌ Geen actieve sessie-intrekking wanneer een medewerker uit dienst treedt of rechten verliest

Wat u wél moet inrichten vóór u meerdere organisaties op één platform toelaat:

✅ Strikte multi-tenant Row Level Security afdwingen op basis van geverifieerd organisatielidmaatschap
✅ Rollenstructuren en permissies vastleggen in beveiligde tabellen buiten het bereik van de frontend
✅ Gebruikmaken van cryptografisch ondertekende custom JWT claims via server-side Edge Functions
✅ Geautomatiseerde permissietests opnemen in uw deployment pipeline tegen datalekken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, richten we waterdichte multi-tenant autorisaties in zodat data tussen uw klanten 100% gescheiden blijft.

💡 Het resultaat: Marijn Kuipers liet DierZorg binnen 9 werkdagen beveiligen voor € 3.700 (Launch Ready Package: rollenmodel, multi-tenancy, permissietests). Zes weken later tekende een keten van 9 praktijken na een vlekkeloze audit en draaien de tests automatisch bij elke deploy. 🚀

👉 Leer hoe u multi-tenant rechten en sessies in Supabase correct beveiligt: https://launchstudio.eu/nl/blog/sessions-roles-and-admin-flags-in-ai-built-apps

#Supabase #Autorisatie #MultiTenancy #AVG #LaunchStudio #Manifera
