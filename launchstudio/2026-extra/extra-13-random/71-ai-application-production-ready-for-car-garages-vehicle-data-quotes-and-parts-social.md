🔧 Two versions of the same brake job

VERSION A: the quote the customer approved
Brake discs: €480
Status: approved

VERSION B: the invoice the customer received
Brake discs: €560
Why: the parts catalogue price rose between approval and invoicing, and the quote was recalculated live

Ferry Janssen, owner of an independent garage in Helmond, built Garagepost in Bolt: customers book services by licence plate, get photo quotes for extra work, approve them in the app, and pay before collecting their car. Three other independent garages around Helmond and Eindhoven started using it. Then one customer complained.

Customers trust a garage that shows them the photo and the price. They stop trusting it the moment the price moves after they've said yes.

The review found more:
• Approval links were order numbers anyone could guess
• Customers of one garage could see vehicles and invoices from another, through the API
• Monday mornings were routinely double-booked, because capacity wasn't checked
• Payments were marked successful on the browser redirect
• The licence plate lookup could be called without logging in, thousands of times a day

Making version A the only version (LaunchStudio, 8 business days, €2,200):
✓ Quotes frozen the moment they're sent, with parts prices stored per line and supplier references
✓ Approval links as random, expiring tokens tied to the customer account, with approvals logged using server timestamps
✓ Garage-level separation with Row Level Security
✓ Capacity per lift and per mechanic built into bookings
✓ Payments confirmed by verified Mollie webhooks, linked to releasing the car
✓ The plate lookup behind authentication, and rate-limited
✓ Photos moved to private storage

Disputed quotes stopped, because every approval now has a fixed price and a record. Monday overbooking disappeared. And Garagepost signed four more independent garages in North Brabant.

"Customers trust a garage that shows them the photo and the price. They stop trusting it the moment the price moves after they said yes." - Ferry Janssen

https://launchstudio.eu/en/blog/ai-application-production-ready-for-car-garages-vehicle-data-quotes-and-parts

#Automotive #Garage #Bolt #Payments #LaunchStudio #Manifera
