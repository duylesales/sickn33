🚨 Tim Verbeek runs a cargo bike rental shop in Delft and built Fietsdeel in Lovable. For two months it worked. Then every Friday afternoon, the staff dashboard went empty - while customers kept receiving booking confirmations. 😳

Tim prompted Lovable a dozen times. Each "fix" changed the dashboard query, and twice Lovable suggested making the reservations policy public. The bug wasn't in the dashboard at all. Here's what was really going on: 🧠

❌ A scheduled cleanup function archiving reservations using UTC instead of Dutch time
❌ Next morning's bookings archived on Friday afternoons, before staff saw them
❌ A reservations policy letting any customer list every booking, names and phone numbers included
❌ No staging, so every prompt went straight to live

✅ Cleanup function fixed to use Europe/Amsterdam time and archive only past pickups
✅ Archived reservations restored
✅ RLS rewritten: customers see their own bookings, staff see all of them
✅ A staging project for testing prompts safely - and the Lovable frontend left untouched

At **LaunchStudio**, backed by Manifera's 11+ years of production work, we diagnose before we change anything, then fix only what's broken underneath. 🛠️

💡 His result: €1,150, five business days. The Friday disappearances stopped that week, and Fietsdeel handled about 900 reservations over the spring season. 🚀

👉 Lovable says "fixed", but nothing changed? Here are the eight problems founders bring us most: https://launchstudio.eu/en/blog/fix-my-lovable-app-the-problems-founders-bring-us-most

#Lovable #Supabase #NoCode #AIFounder #LaunchStudio #Manifera
