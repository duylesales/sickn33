🔓 Sarah Kuipers runt vanuit Haarlem een boekhoudsaas voor freelancers, gebouwd met Bolt en Supabase. Op een dinsdagmiddag mailde een klant: door een getal in de adresbalk te veranderen, kon ze facturen van andere klanten openen, met namen, adressen en bedragen. Sarah nam binnen het uur contact op met LaunchStudio. De AVG-termijn van 72 uur was begonnen. ⏳

Wat er was misgegaan: 🧠

❌ Een door AI gegenereerde wijziging had elf dagen eerder de policy van de facturen versoepeld
❌ Factuur-pdf's stonden in een openbare bucket
❌ Een servicesleutel werd gebruikt in een functie aan de clientkant
❌ Geen tests of logging van toegang om het op te merken

Zo werd het incident afgehandeld: ✅

✅ Binnen anderhalf uur ingedamd: policy hersteld, pdf's naar privéopslag met signed links, sleutel geroteerd
✅ Logs en registraties van toegang tot de opslag geëxporteerd voordat er iets anders werd gewijzigd
✅ De impact vastgesteld met feiten: zo'n 1.300 facturen bereikbaar, met daadwerkelijke toegang door twee andere accounts tot 14 facturen
✅ Haar privacyadviseur beoordeelde de feiten, het datalek werd binnen 72 uur gemeld bij de Autoriteit Persoonsgegevens en betrokken klanten werden geïnformeerd, gevolgd door toegangstests, instructies voor Bolt en logging van toegang tot facturen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met systemen voor klanten met hoge eisen aan beveiliging en een CEO die medeoprichter was van een cybersecuritybedrijf, brengen we rust, feiten en een duidelijke volgorde van stappen. 🛠️

💡 Het resultaat: €2.400, beoordeling binnen 36 uur afgerond. Weinig opzeggingen, en drie maanden later blokkeerden de tests een vergelijkbare AI-wijziging vóór de productie. 🚀

👉 Service voor beveiligingsincidenten voor kleine SaaS-bedrijven: https://launchstudio.eu/nl/blog/security-incident-response-service-for-small-saas

#Datalek #AVG #Incidentrespons #Bolt #AIFounder #LaunchStudio #Manifera
