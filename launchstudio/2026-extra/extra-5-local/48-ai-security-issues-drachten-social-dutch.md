🏭 Sietse Postma bouwde ShiftHub — een dienstroosterapp voor productiewerkgevers rond Drachten — in v0, en pilotte hem bij zijn eigen voormalige werkgever. Wat hij niet wist: de rol van een gebruiker werd rechtstreeks gelezen uit een waarde die door de browser werd verstuurd, in plaats van geverifieerd tegen de database. Elke gewone werknemer kon een verzoek bewerken en zichzelf managerniveau-toegang toekennen tot de dienstrooster- en loongegevens van collega's. 😳

Als uw door AI gebouwde app bepaalt wie "admin" is op basis van wat de browser zegt, is dat geen rolcontrole — dat is een erecode. 🧠

❌ Gebruikersrol gelezen uit door de client verstuurde gegevens in plaats van server-side geverifieerd
❌ Elke werknemer kon een verzoek aanpassen om te escaleren naar managerniveau-toegang
❌ Loonadjacente dienstroostergegevens blootgesteld aan iedereen die wist hoe hij een formulierveld moest bewerken
❌ Het gat was onzichtbaar vanuit het perspectief van de oprichter zelf — de app "werkte" prima

✅ Autorisatie herbouwd zodat elke rolcontrole server-side plaatsvindt tegen geverifieerde accountgegevens
✅ Elke afhankelijkheid van wat de client stuurt, verwijderd
✅ Logging toegevoegd om elke toekomstige poging tot privilege-escalatie te signaleren

Bij **LaunchStudio** is precies dit patroon — het vertrouwen van door de client verstuurde gegevens — het meest voorkomende probleem dat ons engineeringteam met 160+ projecten vindt in prototypes van oprichters. 🛡️

Zijn resultaat: ShiftHub handhaaft nu rolgebaseerde toegang volledig server-side, waarmee het escalatiepad werd gedicht voordat het een levende productieklant bereikte. 🚀

👉 Voer een tien-minutencontrole uit op uw eigen app, en laat ons de rest verifiëren: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #AISecurityIssues #Drachten
