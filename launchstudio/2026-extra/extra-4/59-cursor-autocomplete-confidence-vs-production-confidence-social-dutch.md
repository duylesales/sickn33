🚨 Een toestemmingscontrole in de IT-ticketingtool van Twan Buitenhuis zag er precies zo betrouwbaar uit als elke andere suggestie die Cursor die week deed — schoon, coherent, passend bij de omringende code. De controle was fout voor precies één rolcombinatie, en die combinatie dook op zodra echte gebruikers gingen inloggen. 🎯

🧠 Cursor twijfelt nooit. Elke autocomplete ziet er even zelfverzekerd uit, of het nu om een triviale functie gaat of om een toestemmingscontrole die gevoelige data afschermt — en dat uniforme vertrouwen is het echte gevaar.

❌ De controle verwerkte elke rol die Twan afzonderlijk testte correct — gewone gebruikers, beheerders, supportmedewerkers — maar niet een gebruiker met twee rollen tegelijk
❌ Die combinatie bestond niet in Twans testaccounts, alleen bij zijn echte vroege gebruikers zodra TicketVolg live ging
❌ Toestemmingslogica is precies de categorie waar "plausibel maar fout" echte schade veroorzaakt — syntactisch schoon, logisch coherent, subtiel kapot
❌ Zowel een snelle doorlezing als normaal handmatig testen missen dit door hun aard — niemand testte toevallig die exacte combinatie

✅ Pas bewust strengere controle toe op authenticatie, autorisatie en betaallogica — niet hetzelfde niveau als de rest
✅ Bouw een expliciete testmatrix die elke realistische rolcombinatie dekt, niet alleen elke rol afzonderlijk
✅ Draai die matrix opnieuw bij elke toekomstige wijziging aan het toegangscontrolesysteem

Bij **LaunchStudio** passen we precies dit soort gerichte beoordeling toe op door Cursor gebouwde codebases vóór productie, ondersteund door het in Singapore gevestigde engineeringteam van Manifera. 🛡️

Zijn resultaat: het toestemmingssysteem van TicketVolg verwerkt nu elke realistische rolcombinatie correct, en Twan heeft een echte testmatrix in plaats van een snelle handmatige controle. 🚀

👉 Bouwt u toegangscontrole met Cursor? Laat de rolcombinaties testen: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #IndieHacker #CursorAI
