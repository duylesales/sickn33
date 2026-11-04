🚨 Stefan Huisman bouwde Loonvoorbereider met Cursor en Supabase: een tool voor het voorbereiden van de salarisadministratie van kleine horecabedrijven. Een restaurantgroep met 14 vestigingen wilde tekenen. Toen vroeg hun beveiligingsvragenlijst: "Wordt multifactorauthenticatie afgedwongen voor alle gebruikers met toegang tot salarisgegevens?" Het antwoord was nee. 😳

Eén regel in een vragenlijst was die maand meer waard dan elke functie op zijn roadmap. Dit ontbrak in de app:

❌ Alleen inloggen met een wachtwoord, voor iedereen
❌ Interne beheeraccounts die de salarisgegevens van elke klant konden zien - ook zonder MFA
❌ Wachtwoordherstel dat iedereen met alleen een e-mailadres kon starten, zonder rate limit
❌ Geen mogelijkheid voor zakelijke klanten om MFA te verplichten voor hun eigen medewerkers

✅ Schermen voor TOTP-inschrijving en -controle met authenticator-apps
✅ aal2 afgedwongen in RLS-policies op salaristabellen - niet alleen verborgen pagina's
✅ MFA verplicht voor alle interne beheerders, met een verplichting per organisatie die klanten zelf kunnen aanzetten
✅ Rate limits op wachtwoordherstel en een gecontroleerde, vastgelegde herstelprocedure

Bij **LaunchStudio**, ondersteund door Manifera - waarvan oprichter Herre Roelevink zijn loopbaan in cybersecurity bij CFLW opbouwde - dwingen we MFA af waar het telt: op de server. 🛠️

💡 Het resultaat: €2.050, zes werkdagen. De restaurantgroep tekende nadat de securityofficer de wijziging had beoordeeld, 70% van de gebruikers schakelde MFA binnen drie maanden in, en nog drie klanten zetten de verplichting voor de hele organisatie aan. 🚀

👉 Vragen zakelijke klanten om tweestapsverificatie? Zo voegt u MFA goed toe aan een Supabase-app: https://launchstudio.eu/nl/blog/how-do-i-add-two-factor-authentication-to-my-app

#MFA #2FA #Supabase #AppSecurity #LaunchStudio #Manifera
