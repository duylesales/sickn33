⛵ Lisa Postma bouwde SailSync — een boekings- en onderhouds-SaaS-tool voor jachthavens rond Sneek — in Cursor, met een nachtelijke betalingsreconciliatietaak bedoeld om beschikbaarheid en kosten synchroon te houden. De code zag er correct uit en doorstond elke handmatige test. Wat ze niet opmerkte: de taak was nooit daadwerkelijk bij een scheduler in productie geregistreerd. Hij draaide gewoon nooit, en de beschikbaarheid bij drie jachthavens raakte uit sync — wat leidde tot dubbele boekingen tijdens een druk zeilweekend. 😳

Bevestigen dat de code bestaat en bevestigen dat hij daadwerkelijk in productie draait, zijn twee verschillende dingen. 🧠

❌ Een reconciliatietaak die in de codebase bestond maar nooit bij een taakscheduler was geregistreerd
❌ Geen monitoring of alarmering om te signaleren dat hij stilletjes nooit uitvoerde
❌ Beschikbaarheid raakte uit sync bij drie jachthavens zonder dat iemand het merkte
❌ Het probleem kwam alleen naar boven via dubbele boekingen tijdens het drukke zeilseizoen

✅ De ontbrekende schedulerconfiguratie gevonden en gerepareerd
✅ De reconciliatietaak correct geïmplementeerd, met monitoring en alarmering
✅ Een handmatige override toegevoegd zodat personeel reconciliatie op aanvraag kan activeren

Bij **LaunchStudio** is het testen van de onzichtbare delen van een SaaS-product — taken, webhooks, achtergrondprocessen — een standaardonderdeel van elke productiebeoordeling die ons engineeringteam met 160+ projecten uitvoert. 🛡️

Haar resultaat: SailSyncs reconciliatietaak draait nu elke nacht betrouwbaar bij alle aangesloten jachthavens, met onmiddellijke alarmering als hij ooit faalt. 🚀

👉 Heeft u een geplande taak of webhook die u alleen ooit in de code heeft gezien, niet bevestigd in productie? Laat het controleren: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #SaaSReliability #Sneek
