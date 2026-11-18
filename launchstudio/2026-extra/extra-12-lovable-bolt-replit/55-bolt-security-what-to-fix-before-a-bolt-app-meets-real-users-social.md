🍽️ TODAY'S MENU, at a weekend demo about to go live "next week"

STARTER
Open the page, take the Supabase key. It's the service role key: unrestricted access to the whole database.

MAIN
Log in as any supplier, change one number in the address bar, and read a competitor's price list. None of the 23 endpoints checked who was asking.

SIDE DISH
Certificates in a public bucket, with predictable filenames.

SPECIAL OF THE DAY
A negative price, or a delivery date in 1970. Validation lived only in the browser, so both were accepted.

DESSERT
Call the "new submission" email endpoint as often as you like. No rate limits, on anything.

Quinten Aardema built Leveranciersportaal with Bolt in a weekend, to show a food wholesaler what was possible: a portal where its 90 suppliers submit price lists, certificates and delivery schedules. The wholesaler liked it and asked when it could go live. He said "next week," because it worked. 🥬

The kitchen, closed for a review (LaunchStudio, 2 business days, €2,900):
✓ The service role key rotated and removed, with database access moved to server-side functions using an anonymous key and policies
✓ Row-level security, with policies on all nine tables
✓ Authorisation on all 23 endpoints, scoped to the requesting supplier
✓ Server-side validation on every input, with a schema per endpoint
✓ The certificate bucket made private, with generated identifiers and signed URLs
✓ Rate limits on authentication, submission and notification; upload size limits; timeouts on external calls
✓ The original public preview retired, since it still held the old credentials
✓ A one-page record of what was checked

The portal launched a week late, with all 90 suppliers, and has run for two years. Quinten calls that week's delay the best decision of the project: a price list leaking between competing suppliers would have ended the wholesaler relationship on the spot.

"It worked perfectly. That was the whole problem - there was nothing to see, and any supplier could have read every competitor's prices by changing one number in the address bar." - Quinten Aardema

https://launchstudio.eu/en/blog/bolt-security-what-to-fix-before-a-bolt-app-meets-real-users

#Bolt #AppSecurity #Prototyping #Supabase #LaunchStudio #Manifera
