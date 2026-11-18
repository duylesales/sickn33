⚖️ THE CASE OF THE €14,000 ROOF

THE CLAIM
A customer disputed a €14,000 roofing contract, saying the signed version had a lower price.

THE DEFENCE
Tekenklaar, the app it was signed in, couldn't prove otherwise.

THE EVIDENCE, as it stood
• The "signed PDF" was regenerated from the database every time it was opened
• The contractor had edited the price after signing, to correct a line item
• Signing links were sequential IDs that never expired
• The only identity check was having the link
• The timestamp came from the customer's own browser
• Signed PDFs sat in a public storage bucket

Loes Vermaat, who ran the office of her family's roofing company in Gorinchem, built Tekenklaar with Cursor: small contractors send quotes and agreements, and customers sign on their phones. Forty-five contractors used it, and about 900 documents were signed in its first year. The signature looked real. What was missing was everything that proves a signature is real.

THE NEW RULES OF EVIDENCE (LaunchStudio, 8 business days, €2,400)
✓ Every document frozen as a PDF at the moment it's sent, with its SHA-256 hash stored
✓ Signing links as random, single-use tokens that expire after 14 days
✓ Email verification, plus optional SMS codes above a threshold each contractor sets
✓ An evidence trail recorded on the server, with timestamps from a trusted timestamping service
✓ Signed documents locked: any change means a new version to be signed
✓ Documents in private storage
✓ A signing certificate page appended to each signed PDF
✓ An EU signing provider, integrated as an option for contractors needing advanced signatures

VERDICT
The disputed case was settled, and Loes rebuilt trust with a transparent explanation to every contractor. Two later disputes were resolved quickly using the evidence certificate. Tekenklaar grew to 70 contractors.

"The signature looked real. What was missing was everything that proves a signature is real." - Loes Vermaat

https://launchstudio.eu/en/blog/building-an-ai-contract-signing-app-ai-generated-code-security-for-e-signatures

#ESignature #eIDAS #AppSecurity #Cursor #LaunchStudio #Manifera
