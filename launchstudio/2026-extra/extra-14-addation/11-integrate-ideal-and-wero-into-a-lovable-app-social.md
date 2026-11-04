🚨 Sanne Mulder runs a small plant nursery in Haarlem and built Stekje in Lovable: a monthly subscription with a cutting, care instructions and a pot. An Instagram feature brought great traffic - and more than half of the people who reached checkout left without paying. 😳

A quick poll of her followers gave the answer: they wanted iDEAL. Lovable's card-only Stripe checkout didn't offer it, and the first iDEAL attempt made things worse. Here's what broke: 🧠

❌ A card-only checkout for Dutch shoppers
❌ iDEAL added as a one-off payment every month, so renewals depended on customers remembering
❌ Subscriptions activated on the success page - even for customers who cancelled in their banking app
❌ The Stripe secret key sitting in frontend code

✅ First payment via iDEAL, creating a SEPA Direct Debit mandate for automatic renewals
✅ Subscriptions activated only by a verified webhook
✅ Cancelled and expired payments handled properly
✅ Secret key moved into an edge function, plus an admin view of failed renewals

At **LaunchStudio**, backed by Manifera's 11+ years of Dutch payment integrations from Amsterdam, we add iDEAL underneath your Lovable screens - ready for the move to Wero. 🛠️

💡 Her result: €2,300, eight business days. Checkout completion rose from about 45% to roughly 80%, and Stekje grew to around 340 active subscribers by the end of the season. 🚀

👉 Selling to Dutch customers from a Lovable app? Here's how to add iDEAL and prepare for Wero: https://launchstudio.eu/en/blog/integrate-ideal-and-wero-into-a-lovable-app

#iDEAL #Wero #Lovable #Stripe #LaunchStudio #Manifera
