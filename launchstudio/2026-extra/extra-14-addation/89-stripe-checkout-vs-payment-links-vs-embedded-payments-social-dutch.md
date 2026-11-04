🚨 Sophie Mertens geeft pottenbakworkshops in Mechelen en bouwde Kleiatelier in Lovable: mensen boeken een workshop, betalen en krijgen e-mails ter voorbereiding. Lovable koppelde per workshop een Payment Link van Stripe. De betalingen kwamen binnen - maar de app had geen idee wie had betaald. Sophie koppelde elke avond met de hand betalingen aan boekingen, en twee keer was een workshop overboekt. 😳

Met Payment Links werd ze betaald. Ze vertelden haar app alleen niet wie waarvoor had betaald. Dit ontbrak er:

❌ Betalingen niet gekoppeld aan boekingen of gebruikersaccounts
❌ Onbetaalde reserveringen die onbeperkt plekken bezet hielden
❌ Geen webhook die boekingen na betaling bevestigt
❌ Avonden kwijt aan het met de hand afstemmen van Stripe en de boekingslijst

✅ Checkout-sessies van Stripe per boeking op de server aangemaakt, met het boekings-ID in de metadata
✅ Bancontact en iDEAL ingeschakeld
✅ Een webhook die de boeking pas na betaling bevestigt
✅ Onbetaalde reserveringen na 30 minuten automatisch vrijgegeven, plus voorbereidingsmails bij bevestiging

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar integraties met Stripe, Mollie en PayPal, kiezen we de eenvoudigste optie van Stripe die bij uw fase past - met webhooks die uw app in lijn houden. 🛠️

💡 Het resultaat: €1.450, vijf werkdagen. Het handmatige koppelen stopte volledig, overboekingen verdwenen, en een wachtlijst biedt vrijgekomen plekken nu automatisch aan de volgende persoon aan. 🚀

👉 Stripe Checkout, Payment Links of ingebedde betalingen? Dit past in elke fase bij uw AI-gebouwde app: https://launchstudio.eu/nl/blog/stripe-checkout-vs-payment-links-vs-embedded-payments

#Stripe #Betalingen #Bancontact #iDEAL #LaunchStudio #Manifera
