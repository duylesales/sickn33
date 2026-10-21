🚨 Contractbeheer van Arnoud Steenbergen beheert contracten voor 22 facilitaire bedrijven, waaronder drie regionale ziekenhuisgroepen. De inkoop van een ziekenhuis vroeg om een pentestrapport, dus hij liet er direct een uitvoeren: € 7.500 bij het eerste bureau dat reageerde. 😳

31 bevindingen, 4 kritiek: een service role-sleutel in de frontend, een publieke bucket met getekende contracten, 17 endpoints zonder autorisatie, RLS uit op zes tabellen. Hij had een specialist betaald om te vinden wat een zelfreview van één dag had opgeleverd — en kon het rapport niet delen. Zo bereidt u zich voor op een pentest:

❌ Een test laten uitvoeren voordat de voor de hand liggende problemen zijn opgelost
❌ Het eerste bureau kiezen dat reageert, zonder voorbeeldrapport te zien
❌ Testen zonder documentatie, accounts of stagingomgeving
❌ Geen hertest inbegrepen, dus bevindingen blijven "open" in het rapport

✅ Drie dagen zelfreview over tien categorieën: sleutels, buckets, toegang tussen accounts, RLS, webhooks, sessies, uploads, enumeration, afhankelijkheden, rate limits
✅ Een stagingomgeving met geanonimiseerde productiedata, plus documentatie en vier accounts op verschillende rechtenniveaus
✅ Een tweede bureau gekozen op basis van een geanonimiseerd voorbeeldrapport, twee derde handwerk, met hertest inbegrepen
✅ Kritieke en hoge bevindingen opgelost en hertest, daarna een samenvatting van één pagina voor inkoop

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, doen we eerst de zelfreview — zodat uw pentestbudget vindt wat u zelf niet kon vinden. 🔍

💡 Het resultaat: de tweede test (€ 6.200) vond 0 kritiek en 2 hoog — een goedkeuringsstap voor contracten die kon worden overgeslagen en een gat in de rate limiting, die geen checklist zou vangen. Beide werden in vier dagen opgelost, de samenvatting ging naar het ziekenhuis, en het contract werd getekend. 🚀

👉 Voorbereiden op een penetratietest: https://launchstudio.eu/nl/blog/ai-app-security-preparing-for-a-penetration-test

#Pentest #Appbeveiliging #Inkoop #Lovable #LaunchStudio #Manifera
