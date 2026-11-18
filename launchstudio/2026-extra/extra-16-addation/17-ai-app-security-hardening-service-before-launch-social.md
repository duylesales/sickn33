A month before launch, a friend logged in with a test account and changed one number in the address bar. 🔢

Sanne Bakker runs a small bookkeeping firm in Apeldoorn. She had built Boekdeel with Lovable and Supabase, a portal where clients upload receipts, sign engagement letters and download their annual reports. Sixty clients were about to be invited. Her friend works in IT, and he was only curious.

He saw another test client's annual report.

Sanne thought she was weeks away from launch. She was actually one curious visitor away from a data breach.

The review confirmed what her friend had found, and found more:
• Several tables had Row Level Security enabled, with a policy that let any logged-in user read all rows
• The reports bucket was public, so anyone with a link could download a file without logging in
• The service role key was used in a client-side function to send notification emails
• The admin page checked the user's role in the browser only
• Password reset links could redirect to any website

The weeks before launch looked different after that (LaunchStudio, 7 business days, €2,650):
✓ Policies rewritten so each client sees only their own records and staff see their assigned clients, with automated tests for every table
✓ Reports in a private bucket, with short-lived signed links
✓ Email sending moved to a server function, and the exposed key rotated
✓ The admin role checked on the server
✓ Redirect URLs restricted to Boekdeel's own domain
✓ Rate limits on login and upload, security headers, and a tested restore from backup

Sanne launched to all 60 clients on schedule. When two of her larger clients asked how their financial documents were protected, she sent them the summary report. No follow-up meeting needed.

"I thought I was weeks away from launch. I was actually one curious visitor away from a data breach. Now I can explain exactly how client data is protected." - Sanne Bakker

https://launchstudio.eu/en/blog/ai-app-security-hardening-service-before-launch

#Security #Lovable #Supabase #Launch #AIFounder #LaunchStudio #Manifera
