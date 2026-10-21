🚨 Gerben Stuiver's Klantportaal connects 62 accountancy offices with about 4,000 business clients. A client's laptop was hit by malware and their session cookie stolen. The attacker changed the account's email address — no password needed, no confirmation, no notice to the old address — then used the normal password reset. 😳

They owned the account permanently. The real owner was locked out without a single notification. Here's why password recovery is the back door attackers prefer: 🧠

❌ Email changes with no password check, no verification and no warning to the old address
❌ Reset tokens valid for 24 hours
❌ Forms that confirmed whether an email was registered
❌ No rate limit — the reset endpoint had sent 900 emails in one afternoon

✅ Email changes now need the current password, confirmation at the new address, and a 48-hour reversal link to the old one
✅ Reset tokens: 30 minutes, single use, hashed, and cancelling any previous token
✅ Identical responses and timing for known and unknown addresses across reset, registration and login, plus rate limits per account and IP
✅ All sessions ended on password change, no auto sign-in from the link, and a written support recovery procedure

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we test the back door, not just the front. 🔑

His result: two business days and €2,300 later, the old-address notification has fired four times in a year — and one client reversed a change they hadn't made, catching an attempted takeover in eleven minutes. 🚀

👉 Password reset flows attackers love: https://launchstudio.eu/en/blog/ai-app-security-password-reset-flows-attackers-love

#AppSecurity #AccountTakeover #Authentication #Lovable #LaunchStudio #Manifera
