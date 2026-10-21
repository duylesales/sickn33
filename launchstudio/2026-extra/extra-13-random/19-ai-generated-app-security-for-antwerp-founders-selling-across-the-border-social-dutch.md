🚨 Jana Peeters, keramiste in het Antwerpse Zurenborg, bouwde Atelierboek in Lovable: een boekingsplatform voor pottenbakworkshops. Zes Antwerpse studio's meldden zich aan, daarna vier in Amsterdam en Utrecht. Deelnemers boekten in het Nederlands, Frans en Engels. Toen ontdekten studio-eigenaren dat ze de deelnemers van andere studio's konden zien door een ID in de beheer-URL te veranderen. 😳

De checkout bood alleen kaarten, dus Nederlandse studio's misten boekingen van klanten die iDEAL verwachtten. Bancontact bevestigde via de redirect in de browser, waardoor wie de bankapp sloot als onbetaald op de wachtlijst belandde. Herinneringsmails voegden namen in zonder escaping, database en e-mail stonden in de VS, en de privacyverklaring was alleen Engelstalig. Dit moeten grensoverschrijdende AI-apps goed regelen:

❌ Alleen kaartbetaling voor Belgische en Nederlandse klanten
❌ Betalingen bevestigd door de browser, niet door de aanbieder
❌ Scheiding tussen studio's alleen in de interface
❌ Hosting in de VS en een privacyverklaring in één taal

✅ Mollie met Bancontact, iDEAL en kaarten, bevestigd via geverifieerde webhooks — eerdere afwijkingen verzoend
✅ Scheiding van data per studio afgedwongen in de database
✅ E-mailsjablonen met escaping en validatie die namen met accenten blijft accepteren
✅ Database en e-mail in de EU, plus een lijst met verwerkers voor privacyverklaringen in het Nederlands, Frans en Engels

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en zijn kantoor in Amsterdam, behandelen we beide kanten van de grens als volwaardige markten. ⚙️

💡 Het resultaat: € 1.850, acht werkdagen. Atelierboek groeide in zes maanden naar 23 studio's in België en Nederland, afwijkingen bij betalingen verdwenen, en twee Nederlandse studio's in een gemeentelijk cultuurprogramma tekenden na ontvangst van de lijst met verwerkers. 🚀

👉 Beveiliging van AI-apps voor Antwerpse oprichters die over de grens verkopen: https://launchstudio.eu/nl/blog/ai-generated-app-security-for-antwerp-founders-selling-across-the-border

#Antwerpen #Benelux #iDEAL #Bancontact #LaunchStudio #Manifera
