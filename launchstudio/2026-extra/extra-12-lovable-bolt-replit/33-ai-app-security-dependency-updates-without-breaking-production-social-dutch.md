🚨 Werkbonnen van Menno Zwartjes regelt digitale werkbonnen en handtekeningen voor 47 installatiebedrijven - zo'n 400 monteurs. In veertien maanden had hij nooit een afhankelijkheid bijgewerkt. Toen draaide hij een audit: 63 meldingen, 11 in pakketten die binnenkomende verzoeken afhandelen. 😳

Eén was een fout in het verwerken van verzoeken waarmee een gemanipuleerde payload onbeperkt geheugen kon opslokken - op precies de publieke endpoints die de telefoons van zijn monteurs gebruikten. Ze was negen maanden eerder gepubliceerd. Zo werkt u afhankelijkheden bij zonder productie te breken:

❌ Geen lockfile in de repository - elke build haalde versies opnieuw op
❌ Nooit een audit gedraaid, dus niemand wist wat kwetsbaar was
❌ Elke melding hetzelfde behandelen, of de lijst negeren omdat ze lang is
❌ Pakketten geïnstalleerd voor één datumformaat en één knop

✅ Lockfile gecommit, en de 63 meldingen beoordeeld op bereikbaarheid: 11 dringend, 34 alleen voor ontwikkeling
✅ De 11 direct toegepast met een geschreven testlijst, en major-versies één voor één geüpgraded
✅ Geautomatiseerde scans bij elke build, meldingen naar zijn telefoon, en pull requests voor nieuwe meldingen
✅ 9 ongebruikte directe afhankelijkheden verwijderd (190 pakketten weg), installatiescripts uitgeschakeld, en een updateroutine met drie snelheden op papier

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, houden we uw afhankelijkheden actueel, zodat niets zich opstapelt tot een upgrade van een week. 📦

💡 Het resultaat: na drie werkdagen en € 2.600 was de geheugenfout gedicht, zonder aanwijzing van misbruik. Het aantal pakketten ging van 1.340 naar 1.150 - en Menno besteedt nu zo'n 40 minuten per maand aan updates. 🚀

👉 Afhankelijkheden bijwerken zonder productie te breken: https://launchstudio.eu/nl/blog/ai-app-security-dependency-updates-without-breaking-production

#SupplyChain #Appbeveiliging #npm #Lovable #LaunchStudio #Manifera
