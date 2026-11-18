🍜 FRIDAY NIGHT SERVICE REPORT: Pesanan, Rotterdam

Dewi Sutanto runs an Indonesian restaurant in Rotterdam. She built Pesanan with Lovable and Supabase to take pickup and delivery orders without paying platform commission. After three quiet weeks of testing, she promoted it on social media.

THE RUSH
63 orders in about forty minutes, almost all for pickup between 18:00 and 19:00.

WHAT WENT WRONG IN THE KITCHEN
🔥 No time slots, so every customer picked "as soon as possible"
🔥 Orders appeared on the kitchen tablet as soon as checkout started, including several whose payment later failed
🔥 Two customers got orders containing peanuts: allergens were free text, some dishes left it empty, and the satay sauce option added peanuts without updating the information
🔥 Duplicate orders printed when Mollie retried webhooks
🔥 Menu photos of several megabytes made the app slow on mobile

THE NEW SERVICE (LaunchStudio, 12 business days, €4,800)
✓ Pickup and delivery slots with capacity per fifteen minutes, enforced in a database function
✓ Preparation times per dish category, and a "pause orders" button for staff
✓ Orders reach the kitchen only after a verified Mollie webhook confirms payment, processed once
✓ Unpaid orders release their slot after ten minutes
✓ Allergens as structured data per dish and option, shown before adding to cart, with change history
✓ Compressed, cached menu images, VAT per product for food and alcoholic drinks, and kitchen updates scoped to open orders

THE NEXT FRIDAY
81 orders, spread across slots the kitchen could handle. No failed-payment orders in the kitchen. No duplicates. Dewi now keeps the commission on most of her takeaway revenue, and two neighbouring restaurants want Pesanan too.

"The app worked perfectly until it worked too well. Now it tells customers when we can actually cook their food." - Dewi Sutanto

https://launchstudio.eu/en/blog/restaurant-ordering-app-from-prototype-to-production

#FoodTech #Restaurants #Mollie #Supabase #AIFounder #LaunchStudio #Manifera
