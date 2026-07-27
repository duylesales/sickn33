🔐 Thijs Kooiman bouwde Handelspunt, een B2B-marktplaats die groothandelaren uit de Zwolse regio verbindt met zelfstandige retailers, met Bolt in drie weken. Alles werkte tijdens het testen — totdat de lanceringscontrole van LaunchStudio ontdekte dat de Stripe-webhook niet werd geverifieerd tegen het ondertekeningsgeheim van Stripe. Iedereen had een "betaling geslaagd"-gebeurtenis kunnen vervalsen en een bestelling als betaald kunnen markeren zonder ooit te betalen. 😳

AI schrijft snelle code, niet automatisch veilige code — en bij betaalflows wordt die kloof kostbaar. 🧠

❌ Checkout-sessies werden correct server-side aangemaakt, maar webhookgebeurtenissen bleven ongeverifieerd
❌ Iedereen kon een nepbetalingsbevestiging vervalsen en gratis voorraad bemachtigen
❌ Admin-voorraadroutes hadden geen rolgebaseerde toegangscontrole om ze af te schermen
❌ Niets hiervan kwam naar voren bij normaal testen — alleen een adversariële beoordeling vangt dit op

✅ De webhookverificatielaag herbouwd tegen het ondertekeningsgeheim van Stripe
✅ Idempotentiebeheer toegevoegd om dubbele orderverwerking te blokkeren
✅ Admin-voorraadroutes vergrendeld achter correcte rolgebaseerde toegangscontrole

Bij **LaunchStudio** voeren de 120+ technici van Manifera — hetzelfde team achter projecten voor Vodafone en cyberbeveiligingsbedrijf CFLW — dit exacte dreigingsmodelleringsproces uit op elke door AI gebouwde checkout-flow. 🛡️

Handelspunt verwerkte zijn eerste 200 echte transacties zonder één frauduleuze bestelling, en Thijs nam in zijn eerste maand twaalf groothandelaren aan boord. 🚀

👉 Verwerkt u betalingen in Zwolle? Laat uw webhooks controleren vóór u echt geld verwerkt: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #Zwolle #PaymentSecurity
