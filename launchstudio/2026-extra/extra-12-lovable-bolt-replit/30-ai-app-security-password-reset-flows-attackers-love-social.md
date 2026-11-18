🤔 QUIZ: What really owns an account?

A) The password
B) The email address the password reset goes to

Answer: B. Here's how one client of a Zwolle customer portal found out.

Gerben Stuiver built Klantportaal in Lovable: a customer portal where 62 accountancy and administration offices share documents and messages with around 4,000 business clients. The password reset was reasonable: a random token, valid for 24 hours. The email change wasn't protected at all. A signed-in user could change the account's address with no password confirmation, no check of the new address, and no message to the old one. 🔐

The attack, step by step:
1. A client's laptop was compromised through unrelated malware, and the session cookie stolen
2. The attacker used that session to change the account's email to one they controlled
3. They waited for the session to expire
4. They used the ordinary password reset, which now went to their address
5. They had the account permanently. The real owner was locked out, and told nothing.

The business found out when their accountant mentioned a document request they'd never made.

What LaunchStudio changed (2 business days, €2,300):
✓ Email changes need the current password, a confirmation link to the new address, and only apply once confirmed
✓ The old address gets notified, with a 48-hour reversal link
✓ Reset tokens: 30 minutes instead of 24 hours, single use, hashed at rest, and any earlier token invalidated
✓ Identical responses and timing for known and unknown addresses across reset, registration and login (which used to say plainly whether an email existed)
✓ Rate limits per account and per IP on reset, which had none and had been used to send 900 reset emails in one afternoon the month before
✓ Every session ended on a password change, with a notification
✓ No more automatic sign-in from the reset link
✓ A support recovery procedure requiring confirmation from a second contact at the same office, with every use recorded

The account was recovered manually, and the incident reported to the business and their accountant. In the next year, the old-address notification fired for four email changes. One was reversed by a client who hadn't made it: a takeover attempt caught in eleven minutes, by a message that cost nothing to send.

"Everyone protects the password. Nobody protects the address the password reset goes to, and that is the one that actually owns the account." - Gerben Stuiver

https://launchstudio.eu/en/blog/ai-app-security-password-reset-flows-attackers-love

#AppSecurity #AccountTakeover #Authentication #Lovable #LaunchStudio #Manifera
