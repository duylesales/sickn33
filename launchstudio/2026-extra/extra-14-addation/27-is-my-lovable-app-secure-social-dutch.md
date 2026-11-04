🚨 Nadia El Amrani heeft een kleine boekhoudpraktijk in Rotterdam en bouwde Boekhoudportaal in Lovable: klanten uploaden bonnetjes en bankafschriften, zien hun btw-overzicht per kwartaal en sturen berichten aan de praktijk. Veertig klanten werden uitgenodigd voor een zachte lancering. Een bevriende IT'er deed eerst samen met haar een beveiligingstest van 30 minuten. 😳

Test één slaagde: twee klantaccounts zagen op het scherm elkaars data niet. Test twee faalde - flink. Dit brachten die 30 minuten aan het licht:

❌ Een document-ID in de URL veranderen opende het bankafschrift van een andere klant
❌ Een Supabase-policy op documents waarmee elke ingelogde gebruiker elke rij kon lezen
❌ Links naar bestanden die nooit verliepen
❌ Een geheime sleutel van een e-mailprovider in de JavaScript-bundel

✅ RLS herschreven: klanten zien alleen hun eigen documenten, boekhouders alleen hun toegewezen klanten
✅ Bestanden verplaatst naar een privébucket met kortlevende ondertekende URL's
✅ Het versturen van e-mail verplaatst naar een edge function, sleutel vervangen
✅ Een auditlog van de toegang tot documenten voor de eigen administratie van de praktijk

Bij **LaunchStudio**, ondersteund door Manifera en de cybersecurity-achtergrond van de oprichter bij CFLW, is beveiliging het eerste waar we in elk Lovable-project naar kijken. 🛠️

💡 Het resultaat: €2.400, zeven werkdagen. Ze deed alle zes tests opnieuw en slaagde, de volledige lancering ging drie weken later door, en het portaal bedient nu ongeveer 120 klanten. 🚀

👉 Is uw Lovable-app veilig? Doe de zelftest van 30 minuten voordat uw klanten het doen: https://launchstudio.eu/nl/blog/is-my-lovable-app-secure

#Lovable #AppSecurity #Supabase #FinTech #LaunchStudio #Manifera
