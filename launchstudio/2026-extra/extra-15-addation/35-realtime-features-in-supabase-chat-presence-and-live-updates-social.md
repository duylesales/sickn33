Imagine a school where every homework conversation happens over the loudspeaker. 📢

Every student's name is on the door. Anyone in the building can step in and listen. And a board in the hallway shows which tutor is helping which student.

That, in effect, was how Huiswerkhulp's chat worked before the fix.

Marloes Visser built Huiswerkhulp with Lovable and Supabase: secondary school students chat with volunteer tutors about homework, with a live indicator showing which tutors are online. Two schools in Overijssel piloted it, and the chat felt instant and friendly.

Then a parent with a technical background looked closer:
• Chat ran on public Broadcast channels named "chat-" plus the student's first name and a number
• A single public "tutors" presence channel exposed tutor names and which student each was helping
• Anyone with the app's public key could join any channel
• The messages table let any logged-in user read all messages, so Postgres Changes sent every message to every user
• Subscriptions piled up on every render, and messages sent while a student was briefly offline disappeared

How LaunchStudio closed the doors (9 business days, €3,200):
🚪 Messages stored with Row Level Security for the student, the assigned tutor and school coordinators only
🚪 New messages broadcast from the database to private channels named by conversation ID, with authorisation requiring participation
🚪 Presence on private channels per school, showing tutors as available without revealing who they help
🚪 Throttled typing indicators, proper cleanup, and a refetch after reconnecting
🚪 Automated tests proving students from one school can't join another school's channels

The new chat launched before the second term. Six schools and around 900 students later, no further access issues. The parent who raised it reviewed the fix and joined the volunteer team.

"The chat felt magical in the demo. I hadn't realised that the magic worked just as well for people who were never supposed to see the messages." - Marloes Visser

https://launchstudio.eu/en/blog/realtime-features-in-supabase-chat-presence-and-live-updates

#Supabase #Realtime #EdTech #AppSecurity #AIFounder #LaunchStudio #Manifera
