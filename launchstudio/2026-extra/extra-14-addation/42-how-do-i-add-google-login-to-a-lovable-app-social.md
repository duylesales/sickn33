🚨 Joris Kuijpers, a student counsellor in Nijmegen, built Tentamenplan in Lovable: students plan exam revision and share schedules with study groups. He added Google login because nearly every student has a Google account. It worked perfectly - for him. On launch day, students saw "access blocked". 😳

It worked every time he tested it. He was the only person in the world it was configured to work for. Here's what was wrong: 🧠

❌ The Google consent screen still in testing mode, with Joris as the only test user
❌ Once published, logins sent students back to the Lovable preview domain
❌ No profile row for Google users, so study group features crashed
❌ No plan for students who had already registered with email

✅ Consent screen published with simplified, basic scopes
✅ Production site URL and redirect list set in Supabase
✅ A trigger that creates a profile for every new auth user
✅ Identity linking for students who signed up with email first, tested on iOS and Android browsers

At **LaunchStudio**, backed by Manifera's 11+ years of authentication work, we make social login work for every user - not just the founder. 🛠️

💡 His result: €950, three business days. Login problems disappeared within a day, and about 1,300 students signed up during the exam period - three-quarters of them through Google. 🚀

👉 Adding Google login to a Lovable app? Here's the setup and why it breaks after launch: https://launchstudio.eu/en/blog/how-do-i-add-google-login-to-a-lovable-app

#Lovable #Supabase #GoogleLogin #EdTech #LaunchStudio #Manifera
