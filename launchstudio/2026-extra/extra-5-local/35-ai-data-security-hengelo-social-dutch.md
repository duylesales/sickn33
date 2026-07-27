🏥 Marloes ten Cate, een voormalig ziekenhuisadministrateur in Hengelo, bouwde Zorgrooster — een planningstool voor thuiszorgverpleegkundigen die bezoeken, zorgnotities en medicatieschema's bijhoudt — met Lovable. Het werkte goed voor haar pilot van vier verpleegkundigen. Toen ontdekte de beoordeling van LaunchStudio dat de Supabase-backend geen enkele row-level security had: elk ingelogd verpleegkundigenaccount kon de volledige patiëntendatabase opvragen, inclusief medicatiegegevens van patiënten die niet aan hen waren toegewezen. 😳

Dat is niet zomaar een bug — bij gezondheidsgegevens is dat een AVG-schending die op het punt staat te gebeuren. 🧠

❌ Elk verpleegkundigenaccount kon de zorgnotities en medicatiegeschiedenis van elke patiënt lezen
❌ Geen versleuteling in rust voor gevoelige medicatie- en zorgnotitievelden
❌ Geen auditlogboek — geen registratie van wie wat wanneer heeft geopend
❌ Ongeveer 45% van de door AI gegenereerde code wordt uitgeleverd met minstens zo'n uitbuitbaar beveiligingslek

✅ Granulair RLS-beleid geïmplementeerd dat elke verpleegkundige beperkt tot alleen haar toegewezen patiënten
✅ Versleuteling in rust toegevoegd voor medicatie- en zorgnotitievelden
✅ Een auditlogboek gebouwd dat elke recordtoegang bijhoudt voor AVG-naleving

Bij **LaunchStudio** voeren de 120+ technici van Manifera precies deze databeveiligingsaudit uit — dezelfde nauwkeurigheid die wordt toegepast bij zakelijke klanten zoals Vodafone en TNO. 🛡️

Zorgrooster doorstond de gegevensbeschermingsbeoordeling van de regionale zorgorganisatie bij de eerste indiening, en verzorgt nu de planning voor meer dan zestig verpleegkundigen in Hengelo en Twente. 🚀

👉 Verwerkt u patiëntgegevens in Hengelo? Controleer uw RLS-beleid vóór uw volgende pilot: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #Hengelo #GDPR
