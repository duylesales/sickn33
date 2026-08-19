🚨 Thijs Overkamp bouwde "Uurlijst," een urenregistratietool voor freelancers, in Lovable gedurende één regenachtig weekend in Nijmegen — en het werkte precies zoals hij had gevraagd. Wat hij nooit had bedacht om te vragen: wat gebeurt er als een freelancer een geregistreerd uur bewerkt nadat de factuur van die week al is verzonden. 😳

Een AI-tool bouwt wat u beschrijft. Niet het randgeval waarvan u niet wist dat u het moest beschrijven. 🧠

❌ Een uur bewerken na facturatie liet het factuurtotaal geruisloos ongewijzigd, wat leidde tot een discrepantie tussen wat de app toonde en wat er daadwerkelijk gefactureerd was
❌ Het was geen crash — gewoon een stille, escalerende nauwkeurigheidsbug die geen enkele demo ooit zou hebben opgemerkt
❌ Freelancers konden ook uren registreren met een datum in de toekomst, waardoor het weekoverzicht tijd bevatte die nog niet had plaatsgevonden

✅ De facturatielogica herbouwd zodat bewerkingen na het genereren een herberekeningsvlag activeren in plaats van geruisloos te verouderen
✅ Een vergrendelingsmechanisme toegevoegd zodat een definitieve factuur niet kan worden bewerkt zonder een expliciete override
✅ Een server-side controle toegevoegd die uren in de toekomst weigert, plus geautomatiseerde tests voor de exacte bewerkingsvolgorde na facturatie

Bij **LaunchStudio** is het vangen van de bedrijfslogica die een AI-tool nooit expliciet is opgedragen af te dwingen vaste praktijk — dezelfde strengheid die Manifera's technici, inclusief het team aan Pho Quang Street in Ho Chi Minh City, meenemen naar elke review. 🛡️

Thijs' resultaat: een facturatiestroom die nu het exacte scenario opvangt dat hij "helemaal niet had bedacht" om te testen — want waarom zou hij het op zichzelf hebben getest? 🚀

👉 Benieuwd welk deel van "software engineering" uw AI-tool eigenlijk heeft overgeslagen? Lees het 5-stappen overzicht: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #LovableAI #SoftwareEngineering
