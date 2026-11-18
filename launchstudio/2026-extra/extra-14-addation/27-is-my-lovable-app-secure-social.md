🧪 The 30-minute security test, run on an accountant's client portal

TEST 1: Log in as two different clients. Can they see each other's data on screen?
✅ PASS. The interface filtered by client.

TEST 2: Change the document ID in the URL.
❌ FAIL. Another client's bank statement opened.

TEST 4: Search the JavaScript bundle for secrets.
❌ FAIL. An email provider's secret key was right there.

Nadia El Amrani runs a small accounting practice in Rotterdam and built Boekhoudportaal in Lovable: clients upload receipts and bank statements, see their quarterly VAT overview and message the practice. Forty clients were invited to a soft launch. A friend who works in IT ran the test with her.

Why test 2 failed: the Supabase policy on documents let any logged-in user read any row, and storage links never expired. The interface only made it look private.

What LaunchStudio fixed (7 business days, €2,400):
✓ RLS rewritten: clients see only their own documents, accountants only their assigned clients
✓ Files in a private bucket with short-lived signed URLs
✓ Email sending moved into an edge function, and the key rotated
✓ An audit log of document access, for the practice's own records

THE RETEST
Tests 1 to 6: ✅ ✅ ✅ ✅ ✅ ✅

The full launch went ahead three weeks later than planned. The practice now serves around 120 clients through the portal.

"The app looked careful. Each client only saw their own files on screen. Underneath, everyone could see everything if they knew where to look." - Nadia El Amrani

Run the six tests on your own app: https://launchstudio.eu/en/blog/is-my-lovable-app-secure

#Lovable #AppSecurity #Supabase #FinTech #LaunchStudio #Manifera
