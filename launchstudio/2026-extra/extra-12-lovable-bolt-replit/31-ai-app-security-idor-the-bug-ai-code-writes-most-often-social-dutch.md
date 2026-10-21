🚨 Factuurstroom van Coen Bleeker verzorgt de facturatie voor 380 freelancers en kleine bureaus. Facturen stonden op een URL die eindigde op een oplopend nummer. Een gebruiker typte zijn eigen factuurnummer verkeerd — en kwam uit bij die van iemand anders: naam en adres van de klant, bedragen, en de bankgegevens van de freelancer. 😳

Hij probeerde er nog drie voordat hij Coen schreef. Elk endpoint vereiste een login. Geen enkel controleerde eigenaarschap. Dit is de fout die door AI gegenereerde code het vaakst schrijft:

❌ 31 van de 47 endpoints met een identificatie en zonder eigenaarschapscontrole
❌ Geneste records op ID opgehaald zonder de bovenliggende factuur te controleren
❌ Row-level security op slechts vier van de veertien tabellen
❌ Oplopende factuur-ID's in URL's, een uitnodiging tot enumeration

✅ Elke query beperkt tot het account van de sessie, via een gedeelde hulpfunctie die de veilige manier de standaard maakt
✅ Geneste identificaties gecontroleerd tegen het bovenliggende record
✅ RLS-policies op alle 14 tabellen, en willekeurige ID's in URL's — met het leesbare factuurnummer behouden voor weergave
✅ Een geautomatiseerde test die inlogt als tweede organisatie, elke ID opvraagt, en de build laat falen bij elke data

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, openen we uw records vanuit een ander account — tien minuten, en de test die er het meest toe doet. 🔍

💡 Het resultaat: na twee werkdagen en € 3.800 vond de logcontrole 61 verzoeken tussen accounts in veertien maanden; de betrokken bedrijven en de Autoriteit Persoonsgegevens werden geïnformeerd. De geautomatiseerde test heeft sindsdien twee nieuwe foute endpoints opgevangen vóór de deploy. 🚀

👉 IDOR, de fout die AI-code het vaakst schrijft: https://launchstudio.eu/nl/blog/ai-app-security-idor-the-bug-ai-code-writes-most-often

#Appbeveiliging #IDOR #Toegangsbeheer #Lovable #LaunchStudio #Manifera
