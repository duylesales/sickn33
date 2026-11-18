🍔 KITCHEN TICKET (illustrative)
Table 7
1× Classic burger
1× Classic burger
Status: duplicate

KITCHEN TICKET
Table 12
Paid: yes
Order received: no

KITCHEN TICKET
Table 3
Allergen note: sesame-free
Actually: the bun supplier changed, and the new bun contains sesame

Joost Verhagen owns three burger restaurants in Nijmegen and built Tafelbestel with Lovable and Supabase: guests scan a QR code, order and pay at the table through Mollie. Guests liked it. But on busy evenings, tickets like these appeared. And one guest with a sesame allergy received a burger the app still said was sesame-free.

Why:
• Orders were sent to the kitchen from the payment redirect page. Close the browser too early, and you'd paid without an order. Refresh, and it went twice.
• Allergens were typed per menu item, and nobody updated them when the bun changed
• The menu loaded every item with full-size images
• Table codes were sequential numbers
• All staff at each restaurant shared one login
• Receipt email addresses went straight onto the newsletter list

What LaunchStudio changed (8 business days, €3,300):
✓ Orders confirmed by verified, idempotent Mollie webhooks
✓ The kitchen display acknowledges each order, with an alert to the manager if it doesn't within a minute
✓ A cached menu with resized images
✓ Allergens on an ingredient model: change the bun once, and every burger using it updates, with allergen filters tested
✓ Unguessable table tokens, reset by staff between guests
✓ An account and a role per employee, per restaurant
✓ Newsletter sign-up as an explicit opt-in, separate from receipts
✓ A load test of a full Friday evening at all three restaurants

The next Friday: around 600 orders through the app, not a single duplicate or missing ticket. The menu loads in under a second. And Joost now reviews allergen changes per ingredient, not per dish.

"A wrong burger is a complaint. A wrong allergen is a guest in danger. Now the app gets both right, even on our busiest night." - Joost Verhagen

https://launchstudio.eu/en/blog/production-launch-for-hospitality-apps

#Hospitality #Restaurants #QROrdering #Lovable #AIFounder #LaunchStudio #Manifera
