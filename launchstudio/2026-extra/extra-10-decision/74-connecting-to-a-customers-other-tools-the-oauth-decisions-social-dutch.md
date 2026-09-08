🔗 *"Koppel met Google Calendar / Microsoft 365"*

Het lijkt een handig vinkje in uw SaaS.
Maar besef goed wat u in handen krijgt:

U beheert **OAuth-tokens die namens uw klant mogen handelen in andermans bedrijfssystemen**.

Wat er in de praktijk fout gaat:
❌ Te brede scopes (*"Deze app mag al uw e-mails lezen en bestanden wissen"*) ➔ potentiële klanten haken direct af
❌ Refresh tokens staan in **platte tekst** in Postgres (bij een lek heeft de hacker toegang tot alle klantdata!)
❌ Verbroken koppelingen blijven 'stil' ➔ het dashboard toont "Verbonden", terwijl er al 3 maanden niets meer synchroniseert
❌ Rood Google-waarschuwingsscherm bij lancering omdat de verificatie niet op tijd is aangevraagd

Hoe u OAuth-koppelingen wél veilig ontwerpt:
✅ **Minimale scopes:** Vraag alleen om de agenda's die uw app zelf heeft aangemaakt
✅ **Versleutel tokens at-rest:** AES-256 encryptie met KMS buiten de database
✅ **Voorkom race-conditions:** Eén centrale worker voor token-vernieuwing
✅ **Actieve storingsmeldingen:** Banner + directe e-mail bij verbroken autorisatie
✅ **Plan verificatie in:** Houd rekening met 2 tot 4 weken Google/Microsoft review

Bij **LaunchStudio**, ondersteund door Manifera (11+ jaar ervaring), bouwen we robuuste OAuth-integraties die veilig blijven en soepel door de Google-review heenkomen.

💡 Zo ontdekte Nienke Bakker van Afsprakenlijn dat 11 fysiotherapiepraktijken al sinds maart dubbele boekingen hadden doordat een Google-koppeling geruisloos was uitgevallen. Na onze automatische storingsmonitoring en tokenversleuteling liep de synchronisatie weer vlekkeloos.

👉 Hoe veilig bewaart uw software de OAuth-tokens van uw klanten? https://launchstudio.eu/nl/blog/connecting-to-a-customers-other-tools-the-oauth-decisions

#OAuth #GoogleWorkspace #SaaSIntegrations #CyberSecurity #LaunchStudio #Manifera
