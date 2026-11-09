🔓 Sanne Bakker runs a bookkeeping firm in Apeldoorn and built Boekdeel with Lovable and Supabase: a portal where clients upload receipts, sign engagement letters and download annual reports. A month before inviting her 60 clients, a friend in IT logged in with a test account and changed one number in the address bar. He saw another client's annual report. 😱

The security review found more than one open door: 🧠

❌ Policies letting any logged-in user read every row
❌ A public storage bucket, so report links worked without logging in
❌ The service role key used in a client-side function
❌ Admin checks in the browser only and password reset links that could redirect anywhere

✅ Database policies per client and assigned staff, with automated tests for every table
✅ Reports in a private bucket with short-lived signed links
✅ The key rotated, email sending moved to the server and admin roles checked server-side
✅ Rate limits, security headers, restricted redirects and a tested backup restore

At **LaunchStudio**, backed by Manifera's 11+ years of delivering software for clients such as Vodafone and TNO, we harden AI-built apps before launch at a fixed price, without changing your interface. 🛠️

Her result: €2,650, seven business days. Sanne launched to all 60 clients on schedule, and two larger clients got their security questions answered with one report. 🚀

👉 Security hardening for your AI app before launch: https://launchstudio.eu/en/blog/ai-app-security-hardening-service-before-launch

#Security #Lovable #Supabase #Launch #AIFounder #LaunchStudio #Manifera
