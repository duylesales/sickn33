🚨 Elif Yilmaz heeft twee coworkingruimtes in Utrecht en bouwde Werkplek030 met Bolt en Supabase: werkplekken, vergaderruimtes, dagpassen en teamplekken voor ongeveer 180 leden. Toen zag ze iets vreemds in Stripe: leden op het "Team"-abonnement die er nooit voor hadden betaald. 😳

De oorzaak was binnen minuten gevonden. De policy leek redelijk: gebruikers mogen hun eigen profiel bewerken. Niemand vroeg wat er in het profiel stond.

❌ Een update-policy op profiles - en de rij bevatte plan en role
❌ Elk lid kon zichzelf met één API-aanroep op Team en admin zetten
❌ RLS uitgeschakeld op room_bookings, waardoor de boekingshistorie van elk lid zichtbaar was
❌ Factuur-pdf's in een openbare bucket, genoemd naar factuurnummer

✅ plan en role verplaatst naar een tabel memberships, alleen beschrijfbaar via een serverfunctie die de Stripe-webhook aanroept
✅ RLS op boekingen met een policy op basis van bedrijfslidmaatschap
✅ Facturen in een privébucket met ondertekende URL's
✅ Indexen voor de nieuwe policies, elke wijziging vastgelegd als migratie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar werk met PostgreSQL voor meerdere klanten, vergelijkt een RLS-audit wat elke policy toestaat met wat uw app bedoelt - en bewijst het met echte gebruikersaccounts. 🛠️

💡 Het resultaat: €2.100, zeven werkdagen. Onbetaalde upgrades stopten direct, de meeste gemiste omzet werd teruggehaald en boekingsqueries werden sneller dan voorheen. 🚀

👉 Gebruikt u Supabase? Controleer uw project op de zeven RLS-fouten die we het vaakst vinden: https://launchstudio.eu/nl/blog/supabase-rls-audit-the-policy-mistakes-we-find-most

#Supabase #PostgreSQL #RowLevelSecurity #Bolt #LaunchStudio #Manifera
