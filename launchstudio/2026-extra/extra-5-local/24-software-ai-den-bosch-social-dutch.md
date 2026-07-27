🚨 Thijs Verhoeven, een technische solo-oprichter, bouwde CivicDesk — een tool voor het bijhouden van burgerverzoeken voor kleine gemeenten — met v0 over drie weken. Tijdens een pilot met een Noord-Brabantse gemeente werkten twee medewerkers tegelijkertijd hetzelfde verzoek bij, en de ene statuswijziging overschreef stilletjes de andere, zonder enige waarschuwing en zonder auditspoor. 😳

Voor overheidsgerelateerde software is een onverklaard gegevensverlies zoals dat diskwalificerend. 🧠

❌ Geen optimistic locking bij gelijktijdig schrijven naar hetzelfde record
❌ Geen auditlogboek dat bijhoudt wie welk veld wijzigde, en wanneer
❌ Het door v0 gegenereerde schema had geen database-niveau-constraints die dit voorkwamen
❌ Hij kon elke regel code lezen — maar kon niet zien waar geen rekening mee was gehouden

✅ Optimistic locking implementeren op de verzoekrecords
✅ Een correct auditlogboek toevoegen met tijdstempel en gebruikers-ID bij elke veldwijziging
✅ De database-niveau-constraints toevoegen die het gegenereerde schema had weggelaten

Bij **LaunchStudio** brengen de technici van Manifera 160+ opgeleverde projecten en klanten zoals Vodafone en TNO naar precies dit soort architectuurbeoordeling — de stilzwijgende beslissingen die een AI-tool neemt maar nooit signaleert. 🛡️

Het resultaat voor CivicDesk: de tool doorstond de volgende gemeentelijke aanbestedingsbeoordeling, waarbij het auditspoor specifiek werd genoemd als voldoend aan hun vastleggingsvereiste. 🚀

👉 Technische oprichter die vertrouwt op code die u kunt lezen maar nog niet heeft stresstest? Laat een tweede ronde uitvoeren: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #SoftwareArchitecture #DenBosch
