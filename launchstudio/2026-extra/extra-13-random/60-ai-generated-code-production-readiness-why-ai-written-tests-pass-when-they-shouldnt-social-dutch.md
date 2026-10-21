🚨 Wouter Jacobs, data-engineer in Kampen, bouwde Energiemeter met Cursor: huishoudens koppelen hun slimme-meterdata en de app vergelijkt hun werkelijke verbruik met energiecontracten — inclusief dynamische uurtarieven — en adviseert wanneer overstappen loont. Zo'n 2.600 huishoudens. Hij was trots op 89% testdekking, allemaal door Cursor geschreven. Toen klaagde een klant dat de app een contract had aanbevolen dat haar meer zou hebben gekost. 😳

Dynamische tarieven werden rond de tijdwissel verkeerd berekend, en vaste kosten werden bij sommige contracten dubbel geteld. De tests van de calculator bevestigden precies die verkeerde uitkomsten — ze waren uit de implementatie gegenereerd. Toegangstests mockten Supabase en slaagden nog steeds toen row level security met opzet was verwijderd. En via één rapportage-endpoint konden gebruikers meterdata van andere huishoudens lezen. Daarom slagen door AI geschreven tests als ze zouden moeten falen:

❌ Tests die de code spiegelen — bugs inbegrepen
❌ Mocks die precies verbergen wat wordt getest
❌ Geen negatieve tests voor de verkeerde gebruiker of tenant
❌ Dekking verward met bescherming

✅ Berekening en rapportage-endpoint hersteld, aanbevelingen voor elke gebruiker opnieuw berekend
✅ Calculatortests opnieuw opgebouwd uit met de hand geverifieerde referentiegevallen, inclusief tijdwisseldagen en elk contracttype
✅ Toegangstests tegen een lokale Supabase-instance met negatieve gevallen voor elke tabel, plus betaaltests in Stripe-testmodus
✅ Mutatietesten op calculator en toegangslaag — score van 31% naar 84% — allemaal in CI

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, schrijft AI de testcode — en bepalen mensen wat de tests moeten bewijzen. ⚙️

💡 Het resultaat: € 1.900, zeven werkdagen. De dekking zakte naar 81%, maar de nieuwe tests vingen in zes maanden vier Cursor-regressies op — en premiumabonnementen groeiden 40% nadat Wouter publiceerde hoe berekeningen worden geverifieerd. 🚀

👉 Productierijpheid van AI-Gegenereerde Code: Waarom AI-Geschreven Tests Slagen Wanneer Ze Zouden Moeten Falen: https://launchstudio.eu/nl/blog/ai-generated-code-production-readiness-why-ai-written-tests-pass-when-they-shouldnt

#Testen #Mutatietesten #Cursor #EnergieTech #LaunchStudio #Manifera
