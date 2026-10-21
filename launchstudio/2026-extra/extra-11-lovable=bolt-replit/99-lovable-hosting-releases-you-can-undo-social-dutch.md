🚨 Kassakoppeling van Mark Oudshoorn synchroniseert de verkopen van 34 winkels rond Gorinchem en Leerdam met hun voorraad- en boekhoudsystemen. Hij zette wijzigingen direct live, zonder staging. Op een donderdag liet hij een agent-sessie de verkooptabel "opruimen" — en de migratie verwijderde de kolom die vastlegde van welke kassa elke verkoop kwam. 😳

De code terugdraaien kostte dertig seconden en veranderde niets, want de data was weg. De back-up van die ochtend terugzetten zou een dag aan verkopen van alle 34 winkels wissen. Daarom zijn ongedaan maken en terugdraaien niet hetzelfde:

❌ Direct vanuit de werkomgeving live zetten, zonder staging
❌ Een rollback die nooit getest was
❌ Door een agent gegenereerde migraties die data raken, ongelezen uitgevoerd
❌ Een database-account van de applicatie dat kolommen mocht verwijderen

✅ Staging met geanonimiseerde data, reproduceerbare builds en elke deploy gekoppeld aan een commit
✅ Rollback getest en getimed op 40 seconden
✅ Schemawijzigingen volgens expand-and-contract: elke migratie die data raakt wordt eerst gelezen, met vooraf een snapshot
✅ Feature flags, gescheiden databasegegevens en een releaseroutine van vijf regels

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we van elke release iets wat u kunt terugdraaien. ↩️

💡 Het resultaat: na zes werkdagen en € 3.400 — de verloren kolom gereconstrueerd uit kassabonnen (de gaten bij twee winkels in overleg afgeschreven) en elf maanden zonder incident. De regel "eerst lezen, dan uitvoeren" heeft sindsdien nog twee destructieve voorstellen tegengehouden. 🚀

👉 Releases die u kunt terugdraaien: https://launchstudio.eu/nl/blog/lovable-hosting-releases-you-can-undo

#DevOps #Lovable #Migraties #Retail #LaunchStudio #Manifera
