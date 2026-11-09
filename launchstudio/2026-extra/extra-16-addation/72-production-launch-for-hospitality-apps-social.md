🍔 Joost Verhagen owns three burger restaurants in Nijmegen and built Tafelbestel with Lovable and Supabase: guests scan a QR code, order and pay at the table through Mollie. Guests liked it. But on busy evenings the kitchen got some orders twice, some paid orders never arrived, and a guest with a sesame allergy got a bun from a new supplier the app still called sesame-free. 😟

The assessment found: 🧠

❌ Orders sent to the kitchen from the payment redirect page, so closed browsers lost orders and refreshes doubled them
❌ A menu loading every image at full size
❌ Allergens typed per menu item and not updated when the bun supplier changed
❌ Sequential table codes, one shared staff login per restaurant and receipt emails added to the newsletter

✅ Orders confirmed by verified, idempotent Mollie webhooks, with kitchen acknowledgement and a manager alert after a minute
✅ A cached menu with resized images
✅ An ingredient-based allergen model, so changing the bun updates every burger, with tested filters
✅ Unguessable table tokens, individual staff roles per restaurant, explicit newsletter opt-in and a load test of a full Friday

At **LaunchStudio**, backed by Manifera's 11+ years of building payment, integration and high-traffic systems for clients such as Vodafone and TNO, we get every order to the kitchen once and handle allergens with care. 🛠️

His result: €3,300, eight business days. About 600 orders the next Friday without one duplicate or missing order. 🚀

👉 Production launch for hospitality apps: https://launchstudio.eu/en/blog/production-launch-for-hospitality-apps

#Hospitality #Restaurants #QROrdering #Lovable #AIFounder #LaunchStudio #Manifera
