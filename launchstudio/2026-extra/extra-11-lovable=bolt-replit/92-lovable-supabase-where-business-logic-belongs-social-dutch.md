🚨 Declaratie van Carola Mudde verwerkt zo'n 1.400 declaraties per maand voor twee gemeenten, een woningstichting en vier culturele organisaties rond Sittard en Geleen. Alle drie de bedrijfsregels — goedkeuring boven € 500, bonnetje boven € 50, één keer indienen — zaten in de browser. 😳

Toen werden elf declaraties door een dubbelklik twee keer ingediend, en acht daarvan twee keer uitbetaald. Daarom horen bedrijfsregels niet in een scherm:

❌ Een spreadsheet-import die het scherm omzeilde — 60 declaraties zonder bonnetje ingevoerd
❌ Geen uniciteit, dus een dubbelklik op een trage verbinding betekende een dubbele betaling
❌ Goedkeuring alleen in de interface gecontroleerd — twee declaraties na goedkeuring gewijzigd
❌ Een database zonder constraints: geen foreign keys, elke kolom mocht leeg zijn

✅ Regels in gewone taal opgeschreven en door alle zeven organisaties bevestigd
✅ 214 rijen met overtredingen gevonden en per organisatie gecorrigeerd
✅ Not-null-, foreign key- en uniciteitsconstraints, plus triggers voor bonnetjes en onwijzigbare goedkeuringen
✅ Een audittabel waarin alleen kan worden toegevoegd, een import via hetzelfde gevalideerde pad, en het schema als migraties

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zetten we bedrijfsregels in de database, waar elke weg naar de data ze moet respecteren. 🗄️

💡 Het resultaat: na negen werkdagen en € 4.900 — geen dubbele of ononderbouwde declaraties in veertien maanden, de acht dubbele betalingen teruggehaald, en de audittrail is nu wat de accountant van één gemeente elk jaareinde opvraagt. 🚀

👉 Lovable + Supabase — waar bedrijfslogica hoort: https://launchstudio.eu/nl/blog/lovable-supabase-where-business-logic-belongs

#Supabase #Lovable #Database #Overheid #LaunchStudio #Manifera
