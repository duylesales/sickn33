🚨 Fleur Verhoef, a logistics analyst in Bussum, built Pakketpunt with Cursor: sixty local shops in the Gooi region act as parcel pickup points, and recipients see which shop holds their parcel. Then a shop owner's nephew - a cybersecurity student - sent her a friendly report. 😳

By submitting malformed tracking codes, he'd received full SQL statements with table and column names, the internal Postgres hostname and stack traces with library versions. A failed carrier call returned the carrier's full error, including Pakketpunt's account ID. Login told unknown emails apart from wrong passwords - and the error tracker stored full request bodies, including staff passwords. Here's why AI-generated error messages leak more than you think: 🧠

❌ SQL, hostnames and stack traces returned to the browser
❌ Third-party error responses passed straight through
❌ Login messages that reveal which accounts exist
❌ Passwords sitting in the error tracker

✅ A central error handler with safe messages and reference IDs
✅ Detailed errors in the tracker only - with passwords, tokens and personal data scrubbed
✅ Stored passwords removed from tracker history and a forced reset for affected staff
✅ Unified login and reset messages, production config confirmed, and the tracking lookup verified as safely parameterised

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make your errors helpful to you and useless to attackers. ⚙️

Her result: €980, four business days. Errors now reveal nothing but a friendly message and a reference, support is faster because staff quote the ref - and the nephew became Pakketpunt's part-time security tester. 🚀

👉 AI generated code security: why your error messages leak more than you think: https://launchstudio.eu/en/blog/ai-generated-code-security-why-your-error-messages-leak-more-than-you-think

#AppSecurity #ErrorHandling #OWASP #Cursor #LaunchStudio #Manifera
