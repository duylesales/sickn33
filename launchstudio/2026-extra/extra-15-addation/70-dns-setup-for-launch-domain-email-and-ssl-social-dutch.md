🚨 Anouk van Dijk bouwde Huurcontractcheck met Bolt en Supabase: het helpt huurders en kleine verhuurders huurcontracten te toetsen aan Nederlandse regels. Op de lanceringsdag volgde ze een tutorial om haar .nl-domein naar haar host te laten wijzen - en verwijderde ze wat op oude records leek om "op te ruimen". 😳

De site stond binnen een uur live. Haar zakelijke e-mail werkte niet meer, en niemand merkte het tot een journalist zei dat ze niet had gereageerd op een interviewverzoek. Zo regelt u DNS voor de lancering: domein, e-mail en SSL: 🧠

❌ Verwijderde MX- en SPF-records voor Microsoft 365
❌ Wachtwoordresets via een niet-geauthenticeerde provider die in spam belandden
❌ Supabase Auth die nog naar de Bolt-preview-URL stuurde, en een loshangend beta.-CNAME-record
❌ Het domein geregistreerd op het account van een voormalige freelancer

✅ MX en SPF hersteld, DKIM voor Microsoft 365 en een mail.-subdomein
✅ Eén gecombineerd SPF-record en DMARC in monitoringmodus
✅ Auth-redirect-URLs gerepareerd, het loshangende record verwijderd en DNSSEC ingeschakeld
✅ HTTPS-redirects, HSTS en het domein overgezet naar haar bedrijf met registrar lock en MFA

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat de lancering van uw app niet uw e-mail uitschakelt. 🛠️

💡 Het resultaat: €1.450, 4 werkdagen. De e-mail werkte dezelfde dag weer, mails van de app kwamen in de inbox aan en Internet.nl gaf de volle score voor HTTPS en e-mailauthenticatie. 🚀

👉 Lanceert u op uw eigen domein? Zo regelt u DNS zonder uw e-mail te breken: https://launchstudio.eu/nl/blog/dns-setup-for-launch-domain-email-and-ssl

#DNS #EmailAuthentication #SSL #ProductLaunch #AIFounder #LaunchStudio #Manifera
