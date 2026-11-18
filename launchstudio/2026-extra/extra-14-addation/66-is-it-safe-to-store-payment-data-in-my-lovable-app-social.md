🚫 Three things your app should never store:

1. Card numbers
2. Expiry dates
3. CVC codes

One ticket shop had a table with all three. 312 cards in it. 🃏

Dennis Groot organises regional board game conventions and built Spelbeurs in Bolt: visitors buy tickets and book tables for tournaments. He asked Bolt for "faster checkout for returning visitors." Bolt generated a form that saved card numbers, expiry dates and CVC codes in a saved_cards table, then sent them to the payment provider's API on every purchase.

A developer friend spotted the table while helping with an unrelated bug. Row Level Security was enabled. But the service key was in the frontend, so anyone could have read the table anyway.

What LaunchStudio did (4 business days, €1,700):
✓ The custom form and the table removed
✓ The stored data securely deleted
✓ Every key rotated
✓ A switch to the provider's hosted checkout, with saved payment methods handled by the provider itself
✓ Verified webhooks connected
✓ Payment fields scrubbed from logs

Dennis informed his payment provider and sought advice on notifying customers.

Returning visitors still get one-click checkout, through the provider's saved payment methods. And Dennis's app now stores no card data at all.

"I asked for faster checkout. I got a database full of card numbers that should never have existed." - Dennis Groot

https://launchstudio.eu/en/blog/is-it-safe-to-store-payment-data-in-my-lovable-app

#PCIDSS #Payments #Stripe #AppSecurity #LaunchStudio #Manifera
