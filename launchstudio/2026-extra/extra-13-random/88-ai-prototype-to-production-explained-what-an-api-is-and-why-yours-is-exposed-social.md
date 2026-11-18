🏡 A tour of the doors in an egg farm's app

Liesbeth Hoek runs a free-range egg farm near Barneveld and built Eierbestel in Bolt: households subscribe to weekly egg deliveries, pick delivery days, and pause during holidays. About 700 households around the Veluwe. Liesbeth didn't know what an API was, and didn't think she had one.

Think of the app as a house. The screens are the front door: they only show you what's yours. The API is the kitchen door round the back, and it's where the app actually fetches things. A customer who works in IT tried the doors.

THE FRONT DOOR: the customer's delivery page
✓ Shows your own delivery.

THE KITCHEN DOOR: the same page, with a different number in the address
✗ Other customers' names, addresses and delivery notes, like "key under the mat."

THE STAFF DOOR: a "driver route" page, hidden from customers
✗ The full day's delivery list, for anyone who opened its address.

THE PANTRY DOOR (found by LaunchStudio): subscription updates
✗ Accepted a price sent by the browser.

THE SIDE DOOR (found by LaunchStudio): delivery notes
✗ No limit on how often it could be called.

Fitting locks (LaunchStudio, 5 business days, €1,250):
✓ Ownership checks on every customer endpoint, with Row Level Security
✓ The driver route restricted to a driver role
✓ Prices calculated only on the server
✓ Rate limits and input validation
✓ Notes like "key under the mat" shown to drivers only on the delivery day
✓ And the two-account test, run with Liesbeth on a call, so she could watch every door close

Liesbeth informed affected customers, and most thanked her for being open about it. Eierbestel grew to 950 households, and Liesbeth now runs the two-account test herself after every change.

"I didn't know I had a kitchen door. Now I know every door in my app, and I know each one checks who's knocking." - Liesbeth Hoek

https://launchstudio.eu/en/blog/ai-prototype-to-production-explained-what-an-api-is-and-why-yours-is-exposed

#APISecurity #NoCode #Bolt #SmallBusiness #LaunchStudio #Manifera
