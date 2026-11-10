🚨 Marloes Visser built Huiswerkhulp with Lovable and Supabase: secondary school students chat with volunteer tutors about homework, with a live indicator showing who's online. Two schools in Overijssel piloted it. Then a parent with a technical background noticed something worrying. 😳

Chats ran on public channels named after the student's first name and a number. Anyone with the app's public key could join any channel. Here's how to build realtime features in Supabase safely: 🧠

❌ Public Broadcast channels anyone could join
❌ Presence exposing tutor names and which student they were helping
❌ A message policy letting any logged-in user read all messages
❌ Subscriptions on every render, and messages lost when briefly offline

✅ Messages in a table with RLS for student, assigned tutor and coordinators
✅ Broadcasts to private channels by conversation ID with authorisation policies
✅ Private presence per school, without revealing who's helping whom
✅ Cleaned-up subscriptions, refetch after reconnect and cross-school access tests

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep the realtime magic for the people who are supposed to see it. 🛠️

Her result: €3,200, 9 business days. The new chat launched before the second term, grew to six schools and around 900 students - and the parent who reported the issue joined the volunteer team. 🚀

👉 Adding chat or live updates with Supabase? Here's how to do it securely: https://launchstudio.eu/en/blog/realtime-features-in-supabase-chat-presence-and-live-updates

#Supabase #Realtime #EdTech #AppSecurity #AIFounder #LaunchStudio #Manifera
