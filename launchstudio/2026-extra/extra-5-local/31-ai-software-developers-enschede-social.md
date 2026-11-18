📝 REPORT CARD: Kenniswijzer, Enschede (pre-launch)

Student: Sanne Bruggeman, University of Twente graduate
Project: a peer-tutoring marketplace for students across Enschede's higher-ed institutions
Built with: Lovable, in a two-week sprint

UI design ................. A
Booking flow .............. A
Stripe checkout ........... A
Data access control ....... F

TEACHER'S COMMENTS (LaunchStudio pre-launch review)
The Supabase database had no row-level security policies at all. Any logged-in user could read every other user's booking history, phone number and payment metadata just by inspecting API calls in the browser console.

RESIT WORK (6 business days, €1,100)
✏️ Authorization rebuilt with RLS policies scoped to each user's own records
✏️ Server-side validation on every write
✏️ Rate limiting on the public API routes
✏️ Frontend untouched: the app looks and feels exactly the same

FINAL RESULT
Launch week: 400 University of Twente students, zero data exposure incidents. Next up: Saxion students across the city, on the same backend.

"I thought 'it works' meant it was ready. LaunchStudio showed me the difference between a demo and a product - and fixed it without touching a single line of my UI." - Sanne Bruggeman

Get your own report card before launch day: https://launchstudio.eu/en/blog/ai-software-developers-enschede

#AINativeFounder #LaunchStudio #Manifera #Enschede #ProductionReady
