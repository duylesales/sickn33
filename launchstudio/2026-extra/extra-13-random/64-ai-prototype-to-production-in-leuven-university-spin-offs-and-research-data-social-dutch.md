🚨 Pieter-Jan Maes, postdoc in Leuven, bouwde LabAgenda met Cursor: reserveren en bijhouden van het gebruik van gedeelde labapparatuur zoals microscopen en sequencers, met automatische toerekening van kosten aan onderzoekssubsidies. Zijn departement gebruikte het twee jaar. Toen wilden drie instituten in België en Nederland het, en richtte hij een spin-off op. De eerste vragenlijst over gegevensbescherming was ongemakkelijke lectuur. 😳

Reserveringen, subsidienummers en gebruiksnotities van elke instelling stonden in één tabel die voor elke ingelogde gebruiker zichtbaar was. Inloggen ging met e-mail en wachtwoord, niet met institutionele gegevens. De database draaide in een Amerikaanse regio. Er was geen toegangslog, subsidiedata werd nooit verwijderd, en deployen betekende dat Pieter-Jan vanaf zijn laptop pushte. Dit houdt een labtool van AI-prototype naar productie brengen werkelijk in:

❌ Eén gedeelde tabel voor elke instelling
❌ Geen institutionele single sign-on
❌ Onderzoeksdata buiten de EU gehost en voor altijd bewaard
❌ Deployments vanaf een laptop

✅ Tenancy per instelling en faciliteit met row level security en rollen per faciliteit
✅ SSO via OpenID Connect voor institutionele logins, plus een alternatief voor externe gebruikers
✅ De database gemigreerd naar een EU-regio met back-ups en een geteste restore
✅ Toegangslogging, instelbare bewaartermijnen per instelling en releases met versies via CI met staging — terwijl het bureau voor technologietransfer de licentie afrondde

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en werk voor onderzoeksorganisaties als TNO, maken we van het vertrouwen dat in het lab vanzelfsprekend was regels die in code worden afgedwongen. ⚙️

💡 Het resultaat: € 3.200, elf werkdagen. Alle drie de instituten tekenden binnen twee maanden, LabAgenda beheert nu reserveringen voor 41 faciliteiten, en de beschrijving van de dataverwerking wordt bij elke inkoop hergebruikt. 🚀

👉 Van AI-Prototype naar Productie in Leuven: Universitaire Spin-Offs en Onderzoeksdata: https://launchstudio.eu/nl/blog/ai-prototype-to-production-in-leuven-university-spin-offs-and-research-data

#Leuven #SpinOff #Onderzoeksdata #SSO #LaunchStudio #Manifera
