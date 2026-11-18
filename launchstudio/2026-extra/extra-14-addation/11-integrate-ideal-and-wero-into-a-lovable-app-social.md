📊 POLL: How would you like to pay for your monthly plant cutting?

iDEAL ████████████████ most of you
Card  ████ a few of you

That's roughly what Sanne Mulder heard when she asked her followers why more than half the people reaching checkout left without paying. 🌱

Sanne runs a small plant nursery in Haarlem and built Stekje in Lovable: a monthly subscription that sends a cutting, care instructions and a pot. Lovable had generated a Stripe card checkout. An Instagram feature brought good traffic, but the card-only checkout lost most of it.

So she asked Lovable to add iDEAL. The result created a one-off iDEAL payment every month, so customers had to pay each renewal by hand. Some did. Most forgot. And because the success page upgraded subscriptions, a few customers who cancelled in their banking app still got plants.

What LaunchStudio rebuilt under the existing Lovable screens (8 business days, €2,300):
✓ A first payment with iDEAL through Stripe that also creates a SEPA Direct Debit mandate, so renewals collect automatically
✓ Subscriptions activated only by a verified webhook
✓ Cancelled and expired payments handled properly
✓ The Stripe secret key moved into an edge function
✓ A simple admin view of failed renewals for Sanne

THE NEW POLL RESULTS
Checkout completion: from about 45% to roughly 80% in the first month after launch
Renewals that depend on customers remembering: 0
Active subscribers by the end of the season: around 340

"I thought adding iDEAL was a checkbox. It turned out to be the difference between a webshop and a subscription business." - Sanne Mulder

https://launchstudio.eu/en/blog/integrate-ideal-and-wero-into-a-lovable-app

#iDEAL #Wero #Lovable #Stripe #LaunchStudio #Manifera
