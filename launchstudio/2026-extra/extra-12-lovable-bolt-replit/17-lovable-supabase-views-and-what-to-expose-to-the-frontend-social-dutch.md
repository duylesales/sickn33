🚨 Vakantieverhuur van Iris Molenaar regelt boekingen en omzet voor 210 eigenaren van vakantiewoningen aan de Zeeuwse en Zuid-Hollandse kust. Het eigenaarsdashboard was traag, dus een AI-sessie maakte een view om het te aggregeren. De pagina werd direct snel. 😳

Hij schakelde ook de beveiliging op de tabel eronder uit. Elke eigenaar die de view direct opvroeg, kreeg de bezetting en omzet van alle 500 woningen — inclusief die van de concurrenten tegen wie ze hun prijzen bepaalden. Dit stelt u in Supabase aan de frontend bloot:

❌ Een view aangemaakt zonder security invoker — die volledig langs row-level security liep
❌ Drie van de vier views voor clients met hetzelfde gebrek
❌ Onderliggende tabellen nog steeds direct bereikbaar via de API
❌ Tabellen van een verlaten experiment die blootgesteld bleven

✅ Elke view voor clients opnieuw gedefinieerd met security invoker en getest als drie verschillende eigenaren
✅ Clienttoegang ingetrokken op zes tabellen die nu alleen via views bereikbaar zijn
✅ De dure jaarvergelijking verplaatst naar een materialized view, elke 15 minuten ververst met een regel "bijgewerkt om"
✅ Een geautomatiseerde test die elke view opvraagt als tweede organisatie en faalt als er een rij terugkomt

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vragen we uw API op als een andere klant — een test van tien minuten met soms een ongemakkelijke uitkomst. 🔍

💡 Het resultaat: na twee werkdagen en € 2.200 was het lek binnen een dag na de melding gedicht. De test tussen tenants heeft sindsdien twee foute views uit latere AI-sessies opgevangen vóór productie — en het dashboard laadt nog steeds binnen 200 ms. 🚀

👉 Views en wat u aan de frontend blootstelt: https://launchstudio.eu/nl/blog/lovable-supabase-views-and-what-to-expose-to-the-frontend

#Supabase #RowLevelSecurity #Databeveiliging #Lovable #LaunchStudio #Manifera
