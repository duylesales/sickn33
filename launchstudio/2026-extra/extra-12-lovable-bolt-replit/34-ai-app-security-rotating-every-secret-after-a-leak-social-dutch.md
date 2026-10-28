🚨 Inspectierapport van Suzanne Grotenhuis maakt zo'n 2.000 inspectierapporten per maand voor 39 inspectie- en keuringsbedrijven. Ze maakte haar repository vier dagen publiek om een codevoorbeeld te delen. Elf maanden eerder was er een omgevingsbestand gecommit - met de service role-sleutel van Supabase, e-mailgegevens, een kaartsleutel die op gebruik afrekent en haar webhook-secret. 😳

Binnen een dag hadden geautomatiseerde scanners het gevonden. Ze hoorde het van de kaartprovider: 140.000 verzoeken in elf uur vanaf onbekende adressen. Dit doet u in het eerste uur na een lek:

❌ Eerst het bestand of de commit verwijderen - de sleutel werkt nog, en klonen en scanners hebben hem al
❌ Alleen de sleutel vervangen die u opmerkte, niet alles in hetzelfde bestand
❌ Nooit de providerlogs controleren op gebruik
❌ De route open laten: geen scan op geheimen, zwakke ignore-regels, gedeelde logins

✅ De misbruikte kaartsleutel eerst vervangen, dan de databasesleutel, dan e-mail en het webhook-secret (met oud en nieuw allebei geldig tijdens de overgang)
✅ Elke sleutel in het bestand als gecompromitteerd behandeld, vervangen in volgorde van gevolg
✅ Database- en e-maillogs bekeken, een gedocumenteerde lekbeoordeling en een melding uit voorzorg bij de AP
✅ Scannen op geheimen tijdens de build, gecorrigeerde ignore-regels, toegang per persoon in een wachtwoordmanager, en een inventarisatie van negen geheimen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, helpen we u eerst te vervangen en daarna op te ruimen - de volgorde die het risico echt verlaagt. 🔑

💡 Het resultaat: na twee werkdagen en € 3.100 schold de kaartprovider € 2.840 aan gebruik kwijt, en werd er geen bewijs gevonden van toegang tot database of e-mail. Het echte incident, concludeerde ze, was de sleutel die elf maanden in dat bestand stond. 🚀

👉 Elk geheim vervangen na een lek: https://launchstudio.eu/nl/blog/ai-app-security-rotating-every-secret-after-a-leak

#Incidentrespons #Geheimen #Appbeveiliging #Lovable #LaunchStudio #Manifera
