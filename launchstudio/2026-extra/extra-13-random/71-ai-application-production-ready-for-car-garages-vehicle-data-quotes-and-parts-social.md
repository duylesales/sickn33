🚨 Ferry Janssen, owner of an independent garage in Helmond, built Garagepost in Bolt: customers book services by licence plate, receive photo quotes for extra work, approve them in the app and pay before collecting their car. Three more garages in the Helmond–Eindhoven area joined. Then a customer who'd approved a €480 brake-disc quote received an invoice for €560. 😳

The parts catalogue price had risen between approval and invoice, and the quote was recalculated live. Approval links were guessable order numbers. Customers of one garage could see another garage's vehicles and invoices through the API. Monday mornings were routinely double-booked, payments were marked successful on browser redirect, and the plate lookup could be called without login thousands of times a day. Here's what makes a garage app production ready: 🧠

❌ Approved quotes that change price afterwards
❌ Guessable approval links
❌ Customers seeing other garages' data
❌ No capacity check and browser-confirmed payments

✅ Quotes frozen when sent, with parts prices stored per line and supplier references
✅ Random expiring approval tokens tied to the customer account, approvals logged with server timestamps
✅ Garage-level separation with row level security and capacity per lift and mechanic
✅ Verified Mollie webhooks linked to job release, the plate lookup rate-limited behind authentication, and private photo storage

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make sure "yes" to a quote means the same price on the invoice. ⚙️

His result: €2,200, eight business days. Disputed quotes stopped, Monday overbooking disappeared, and Garagepost signed four more independent garages in North Brabant. 🚀

👉 AI application production ready for car garages: vehicle data, quotes and parts: https://launchstudio.eu/en/blog/ai-application-production-ready-for-car-garages-vehicle-data-quotes-and-parts

#Automotive #Garage #Bolt #Payments #LaunchStudio #Manifera
