🚨 Lieke Ottenhof's Sportschoolbeheer manages memberships for 54 independent gyms and studios - about 8,000 members. Memberships were activated by a payment webhook that never checked the signature. The provider's dashboard showed every delivery succeeding, so it looked fine. 😳

The URL sat in a public repository for four days. Eleven weeks later, someone started posting fake "payment succeeded" messages to it - 23 memberships across nine gyms, worth €240–€580 a year each, some resold. Here's what an unverified webhook really is: 🧠

❌ A public URL that grants access when called - with no signature check
❌ No timestamp check, so captured messages could be replayed forever
❌ No record of processed events, so retries could double-grant
❌ Membership granted on the message's word, without asking the provider

✅ Signature verification on the raw body with a timing-safe comparison - failures rejected and alerted
✅ Messages older than five minutes refused, and every event ID recorded so replays and retries are harmless
✅ Verify, record, acknowledge - with activation in a background job, only after confirming the payment with the provider's API
✅ The 23 fake memberships found by cross-checking payments, plus a monthly reconciliation of memberships against real payments

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we check whether your webhook URL believes anyone who calls it. 🔏

Her result: two business days and €2,500 later, about €9,000 in annual membership value was recovered - and the reconciliation job has since caught two genuine failed-delivery gaps. Four lines of code now guard the entire revenue model. 🚀

👉 Webhooks you never verified: https://launchstudio.eu/en/blog/ai-app-security-webhooks-you-never-verified

#Webhooks #AppSecurity #Payments #Lovable #LaunchStudio #Manifera
