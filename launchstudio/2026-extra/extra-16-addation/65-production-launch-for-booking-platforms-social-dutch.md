🏃‍♀️ Fleur Jansen geeft bootcamplessen in de buitenlucht in Haarlem en omliggende plaatsen, en bouwde Buitensport met Bolt en Supabase. Elke zondag om 20:00 gingen de lessen van de week erna open, en ochtendlessen met twintig plekken zaten binnen enkele minuten vol. Binnen een maand: lessen met meer dan twintig deelnemers, klanten die betaalden maar geen plek kregen en, na de overgang naar de wintertijd, herinneringen die een uur te laat kwamen. ⏰

De beoordeling verklaarde elk van die problemen: 🧠

❌ Beschikbaarheid berekend in de browser, boekingen toegevoegd zonder enige databasecontrole
❌ Plekken voor altijd vastgehouden als klanten de betaling afbraken, en bevestigingen die afhingen van de redirect van Mollie
❌ Tijden opgeslagen zonder tijdzone-informatie en herinneringen ingepland in UTC
❌ Een query voor beschikbaarheid die elke boeking ooit laadde, en precies om 20:00 op zondag traag werd

✅ Capaciteit gecontroleerd en gereserveerd binnen een databasetransactie, met een wachtlijst als een les vol is
✅ Reserveringen die na tien minuten verlopen, boekingen bevestigd door idempotente webhooks en late betalingen automatisch terugbetaald
✅ Tijden omgezet naar tijdstempels in Europe/Amsterdam, herinneringen in lokale tijd en de weken rond de klokwisseling getest
✅ Een geïndexeerde query voor beschikbaarheid met een korte cache, plus een loadtest met 400 mensen die tegelijk boeken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met systemen voor planning en betalingen voor klanten zoals Vodafone en TNO, maken we dubbele boekingen onmogelijk en houden we tijden correct bij elke klokwisseling. 🛠️

💡 Het resultaat: €2.600, zeven werkdagen. De zondag erna zo'n 350 boekingen in tien minuten, zonder één overboekte les. 🚀

👉 Productielancering voor boekingsplatforms: https://launchstudio.eu/nl/blog/production-launch-for-booking-platforms

#Boekingen #Bolt #Supabase #Mollie #AIFounder #LaunchStudio #Manifera
