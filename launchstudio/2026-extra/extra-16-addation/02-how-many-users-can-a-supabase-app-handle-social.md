📈 Karim Bouzid built Huiswerkplanner with Bolt and Supabase: a homework planner where students see assignments, teachers post tasks and parents follow progress. Then a school board with 14 schools decided to roll it out to 20,000 students on one Monday morning. Karim had never had more than 300 people online at once. 😬

A load test told the truth: at about 600 concurrent students, the planner took more than five seconds and errors started. The question wasn't "can Supabase handle 20,000 users?" Here's what actually limited capacity: 🧠

❌ The planner loaded every assignment in the school and filtered in the browser
❌ Each assignment card made its own extra requests
❌ A policy with a subquery per row and no indexes
❌ Realtime on the whole table pushing every change to every student

✅ Composite indexes and a faster, indexed policy
✅ One view returning a student's next two weeks in a single query
✅ Realtime narrowed to private channels per class
✅ One compute size up, only after optimisation proved it was the last limit

At **LaunchStudio**, backed by Manifera's 11+ years of running PostgreSQL systems with large user bases, we optimise first and scale second. 🛠️

His result: €4,600, eleven business days. On Monday, 11,000 students opened the app in the first hour, peak concurrency near 2,800, zero errors. 🚀

👉 How many users can your Supabase app really handle? https://launchstudio.eu/en/blog/how-many-users-can-a-supabase-app-handle

#Supabase #Bolt #Scalability #EdTech #AIFounder #LaunchStudio #Manifera
