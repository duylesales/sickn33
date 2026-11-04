🚨 Bart Smulders bouwde Huurdossier in Bolt: huurders die reageren op huurwoningen uploaden één keer hun identiteitsbewijs, loonstroken en werkgeversverklaring, en delen daarna een dossierlink met verhuurders. Binnen twee maanden gebruikten zo'n 900 huurders in Eindhoven de app. Toen merkte een verhuurder dat de links naar bestanden eindigden op /public/documents/1234/payslip.pdf - en door het getal te wijzigen, opende hij de loonstroken van andere huurders. 😳

Het hele punt van zijn app was gevoelige documenten op één veilige plek bewaren. Ze stonden op één plek. Die was alleen niet veilig. Dit is waarom:

❌ Alle documenten in een openbare bucket
❌ Opeenvolgende ID's in de bestandspaden, waardoor links te raden waren
❌ Helemaal geen storagepolicies
❌ Telefoonfoto's van identiteitskaarten met nog de locatiegegevens van waar ze waren gemaakt

✅ Alle documenten verplaatst naar een privébucket met willekeurige bestandsnamen, en bestaande bestanden gemigreerd
✅ Storagepolicies zodat huurders alleen bij hun eigen map kunnen
✅ Dossiers delen via tijdelijk geldige signed links op een deelpagina voor verhuurders
✅ Metadata verwijderd uit afbeeldingen, limieten op grootte en type, en elk bestand verwijderd wanneer een huurder het account opheft

Bij **LaunchStudio**, ondersteund door Manifera - vertrouwd door Vodafone, TNO en CFLW voor veilige documentverwerking - maken we uploads standaard privé, alleen toegankelijk voor de eigenaar en kortlevend. 🛠️

💡 Het resultaat: €1.950, vijf werkdagen. Na de oplossing was geen enkel bestand meer bereikbaar zonder toestemming, en een openbare pagina over de bescherming van dossiers werd een reden voor verhuurders om links van Huurdossier te accepteren. 🚀

👉 Laat u gebruikers bestanden uploaden in uw AI-gebouwde app? Dit zijn de zeven stappen om dat veilig te doen: https://launchstudio.eu/nl/blog/how-do-i-let-users-upload-files-safely

#Supabase #Bestandsuploads #AppSecurity #AVG #LaunchStudio #Manifera
