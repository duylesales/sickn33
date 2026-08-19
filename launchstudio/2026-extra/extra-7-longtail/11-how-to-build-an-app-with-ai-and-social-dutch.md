🚨 Wouter Hendriks bouwde "Werkbon," een offerte-tool voor aannemers, volledig in Bolt gedurende drie weken aan avonden — en stuurde het naar twee vrienden die het zonder problemen gebruikten. Wat geen van beide vrienden ooit triggerde: de database was een tijdelijke dev-instantie met nul back-ups, en elke aannemer kon de klantenlijst van een ander account opvragen door simpelweg een ID in de URL aan te passen. 😳

Een vriendelijke testronde met twee personen test niet wat een echte lancering daadwerkelijk vereist. 🧠

❌ De door Bolt ingerichte database was een tijdelijke ontwikkelinstantie zonder back-upschema — een herimplementatie had elke offerte in het systeem gewist
❌ Geen server-side controle bevestigde of een aannemer alleen zijn eigen offertes kon inzien; het ID in de URL was het enige dat in de weg stond
❌ Uitgaande e-mails voor offertemeldingen draaiden op een sandbox-e-mailconfiguratie die geruisloos zou stoppen met bezorgen na enkele tientallen berichten per dag
❌ Niets hiervan kwam naar voren tijdens het testen, omdat twee bevriende bètagebruikers geen reden hadden om halverwege opnieuw te deployen of naar andermans data te zoeken

✅ De database gemigreerd naar een persistente instantie met automatische back-ups
✅ Server-side eigendomscontroles toegevoegd over elk offerte- en klanteindpunt
✅ Een basisimplementatiepijplijn opgezet en de sandbox-e-mailconfiguratie gerepareerd

Bij **LaunchStudio** beschouwen we databaseduurzaamheid en toegangscontroles als een poort vóór de lancering, niet als een bijzaak — ondersteund door Manifera's 11+ jaar ervaring in productie-engineering vanuit Herengracht 420 in Amsterdam. 🛡️

Wouter's resultaat: twee weken na de fix groeide zijn pilotlijst van twee vrienden naar negen betalende gebruikers, en de app voelde niet langer als één ongelukkige klik verwijderd van een beschamende supportmail. 🚀

👉 Denkt u dat uw demo bewijst dat uw door AI gebouwde app klaar is voor lancering? Lees dit eerst: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #BuildWithAI #AppSecurity
