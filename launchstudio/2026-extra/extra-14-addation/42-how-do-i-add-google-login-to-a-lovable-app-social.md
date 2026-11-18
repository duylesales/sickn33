🧩 RIDDLE: A login button works perfectly every single time its builder tests it. On launch day, it works for no one else. Why?

ANSWER: Because the builder was the only person in the world it was configured for.

Joris Kuijpers, a student counsellor in Nijmegen, built Tentamenplan in Lovable: students plan exam revision and share schedules with study groups. He added Google login, since nearly every student has a Google account. For him, it worked flawlessly.

On launch day, students saw "access blocked." The Google consent screen was still in testing mode, with Joris as the only test user.

BONUS RIDDLE: What happens when you publish the consent screen?
ANSWER: Logins succeed, and send everyone back to the Lovable preview domain.

FINAL RIDDLE: Why does the study group feature crash for Google users?
ANSWER: They never got a profile row.

The solutions (LaunchStudio, 3 business days, €950):
✓ The consent screen published, with simpler scopes
✓ The production site URL and redirect list set in Supabase
✓ A trigger that creates a profile for every new auth user
✓ Identity linking for students who had first registered with email
✓ Tested on iOS and Android browsers

Login problems disappeared within a day of the fix. Over the exam period, around 1,300 students signed up, three-quarters of them with Google.

"It worked every time I tested it. I was the only person in the world it was configured to work for." - Joris Kuijpers

https://launchstudio.eu/en/blog/how-do-i-add-google-login-to-a-lovable-app

#Lovable #Supabase #GoogleLogin #EdTech #LaunchStudio #Manifera
