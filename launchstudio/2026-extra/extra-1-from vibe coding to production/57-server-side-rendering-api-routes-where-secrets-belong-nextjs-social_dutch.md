🚨 Een bouwfout blokkeerde zijn lancering. De fix van een AI-codeerassistent liet hem direct verdwijnen. Wat daadwerkelijk gebeurde: zijn geheime API-sleutel werd rechtstreeks gebundeld in publiek toegankelijke JavaScript, zichtbaar voor iedereen die de broncode van zijn site bekeek — maandenlang. 🔓

Next.js vermengt frontend en backend in één project. Precies dat gemak maakt de grens makkelijk vervaagd. 🧠

❌ `NEXT_PUBLIC_` betekent expliciet "gebundeld in clientcode, zichtbaar voor iedereen" — geen generieke fix voor een bouwfout
❌ Een niet-geprefixt geheim gerefereerd in client-side code faalt tijdens het bouwen — verleidelijk om te "fixen" door gewoon het voorvoegsel toe te voegen
❌ Een API-aanroep die een geheime sleutel nodig heeft, client-side geschreven in plaats van via een server-side API-route, dwingt de blootstelling af
❌ Een breed gemarkeerd clientcomponent kan server-only logica, inclusief geheimreferenties, de clientbundel intrekken

✅ Doorzoek elke omgevingsvariabelereferentie: oprecht publiek en correct geprefixt, of alleen server-side — nooit beide
✅ Bouw jouw app en inspecteer de daadwerkelijk gecompileerde clientbundel op iets gevoelig ogends
✅ Dit is structureel anders dan hardgecodeerde geheimen in broncode — een correct opgeslagen geheim, blootgesteld door waar het gerefereerd wordt
✅ Indien blootgesteld, roteer de credential — hetzelfde principe als elk ander blootgesteld geheim

Bij **LaunchStudio** reviewen we Next.js-apps specifiek op dit server-client-grensprobleem, en controleren zowel broncode als de gecompileerde bundel. Gesteund door Manifera's productie-Next.js-ervaring. 🛡️

Zijn resultaat: de blootgestelde sleutel direct geroteerd, de aanroep geherstructureerd via een correcte server-side route. 🚀

👉 Laat jouw Next.js-app controleren op geheimen die de server-client-grens overschrijden: [Link naar artikel]

#IndieHacker #LaunchStudio #Manifera #NextJS #AISecure
