🔎 ERROR DECODER: what one parcel app's error messages told a stranger

What a malformed tracking code returned:
➜ the full SQL statement, with table and column names
➜ the internal hostname of the Postgres database
➜ stack traces showing library versions

What a failed carrier API call returned:
➜ the carrier's full error response, including Pakketpunt's account identifier

What the login form said:
➜ different messages for "unknown email" and "wrong password"

What the error tracker stored:
➜ full request bodies, including shop staff passwords submitted at login

Fleur Verhoef, a logistics analyst in Bussum, built Pakketpunt with Cursor: a network of local shops acting as parcel pickup points, with an app where recipients see which shop holds their parcel and shops scan parcels in and out. Sixty shops in the Gooi region took part. Then a shop owner's nephew, who studies cybersecurity, sent her a friendly report. Her app was so helpful when it failed that it told him how her database was built.

What LaunchStudio changed (4 business days, €980):
✓ A central error handler, with safe messages and a reference ID
✓ Detailed errors sent only to the error tracker, scrubbed of passwords, tokens and personal data
✓ Stored passwords removed from the tracker's history, and a password reset for affected staff
✓ Login and reset messages unified
✓ Production configuration confirmed
✓ And, since SQL showing up in errors is a warning sign: a review of the tracking-code lookup, which turned out to use parameterised queries safely

What an error says now: a friendly message, and a reference. Support got faster too: shop staff quote the reference, and Fleur finds the full error within seconds. And the nephew? He's now Pakketpunt's part-time security tester.

"My app was so helpful when it failed that it told a stranger how my database was built. Now it's helpful to me instead." - Fleur Verhoef

https://launchstudio.eu/en/blog/ai-generated-code-security-why-your-error-messages-leak-more-than-you-think

#AppSecurity #ErrorHandling #OWASP #Cursor #LaunchStudio #Manifera
