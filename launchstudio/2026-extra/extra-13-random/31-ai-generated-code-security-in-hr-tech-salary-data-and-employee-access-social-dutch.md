🚨 Laura Timmermans, HR-adviseur in Ede, bouwde Verlofbord met Cursor: een portaal waarmee mkb-bedrijven verlof, verzuimmeldingen en loonstroken beheren, met goedkeuring door managers. Veertien bedrijven, 850 werknemers. Toen noemde een teamleider bij een klant — terloops — het salaris van een collega van een andere afdeling. 😳

Elke gebruiker met de managerrol kon elke werknemer in het bedrijf opvragen, inclusief salarissen en bankgegevens, omdat de API alleen op bedrijf filterde. Het verzuimformulier had een vrij tekstveld "reden" vol diagnoses. Loonstroken stonden in een openbare bucket met voorspelbare namen, er was geen toegangslog, en wie zes maanden eerder was vertrokken had nog een actief account. Dit betekent beveiliging van AI-gegenereerde code in HR-tech:

❌ "Manager" betekende "ziet iedereen"
❌ Salaris- en bankgegevens in dezelfde query als namen
❌ Diagnoses vastgelegd door de werkgever
❌ Raadbare loonstrookbestanden, geen logging van inzage, geen offboarding

✅ Een rollenmatrix afgedwongen met beleid op rijniveau, reikwijdte van managers afgeleid uit rapportagelijnen
✅ Salaris- en bankgegevens in een aparte tabel, alleen voor HR en salarisadministratie
✅ Het veld "reden" verwijderd — bestaande invoer gewist na het informeren van klanten
✅ Privéopslag van loonstroken met ondertekende links, toegangslogging, uitdiensttreding gekoppeld aan contracteinddata, en tests op verboden toegang bij elke deployment

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en een leiding met wortels in beveiliging, modelleren we toegang expliciet en testen we die doorlopend. ⚙️

💡 Het resultaat: € 3.100, tien werkdagen. Klanten werden transparant geïnformeerd en niemand vertrok — twee noemden de reactie juist als reden om te blijven. Verlofbord groeide naar 23 bedrijven, en de tests hielden al één regressie uit een latere Cursor-bewerking tegen. 🚀

👉 Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer: https://launchstudio.eu/nl/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access

#HRTech #Gegevensbescherming #Cursor #Toegangsbeheer #LaunchStudio #Manifera
