⚖️ Vraagt een gebruiker om verwijdering volgens de AVG en zet u simpelweg `is_deleted = true` in de database? Pas op: een soft-delete is géén wettelijke gegevenswissing.

Als verwijderde gebruikersnamen blijven opduiken in zoekresultaten, e-maillijsten of back-ups, overtreedt u direct Artikel 17 van de AVG.

Waar het vaak misgaat bij AVG-gegevenswissing in Supabase:

❌ Soft-deletes gebruiken waardoor persoonsgegevens vindbaar blijven voor achtergrondtaken en exports
❌ Persoonsgegevens blijven achter in gekoppelde tabellen (zoals reacties, logs en notificaties)
❌ Geüploade pasfoto's en documenten blijven oneindig opvraagbaar in cloudopslag-buckets
❌ Geen onderscheid tussen data die gewist móet worden en facturen die 7 jaar bewaard moeten blijven

Wat u wél moet inrichten vóór een privacy-klacht escaleert naar de toezichthouder:

✅ Inrichten van geautomatiseerde cascading deletes of onomkeerbare pseudonimisering van historische data
✅ Directe verwijdering van gekoppelde mediabestanden en documenten uit opslagbuckets
✅ Juridisch sluitend retentiebeleid dat fiscale bewaarplichten verenigt met het recht op vergetelheid
✅ Geautomatiseerde bevestigingsrapporten die exact aantonen welke data conform de wet is gewist

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, richten we data-lifecycle- en verwijderstromen in die 100% voldoen aan de AVG.

💡 Zo handelde buurtplatform Buurtkracht in Zwolle privacyverzoeken juridisch sluitend af en doorstond glansrijk een gemeentelijke audit.

👉 Ontdek hoe u gegevenswissing en AVG-erasure technisch correct inricht: https://launchstudio.eu/nl/blog/data-deletion-and-erasure-in-practice

#AVG #GDPR #Privacy #Supabase #LaunchStudio #Manifera
