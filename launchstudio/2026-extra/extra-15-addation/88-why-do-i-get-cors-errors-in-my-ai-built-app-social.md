🚨 Mila Verbeek built Plantwijzer with Bolt and Supabase: customers photograph a houseplant, get an AI health diagnosis and receive care reminders. On launch day, she connected plantwijzer.nl and announced it to her 9,000 newsletter subscribers. Every diagnosis failed: "blocked by CORS policy". 😳

An online tip to allow all origins fixed some requests but not others. Four separate problems were hiding behind one error message. Here's why AI-built apps get CORS errors: 🧠

❌ The allowed origin hard-coded to the preview domain
❌ No handling of OPTIONS preflight requests
❌ Large images crashing the function with a 500 and no headers - looking like CORS
❌ The care-reminder screen calling the AI API from the browser, key visible in the bundle

✅ A shared CORS helper allowing production, staging and local, including www
✅ Every function answering preflight and returning headers on errors
✅ Image size validated before upload, with a clear message
✅ The AI call moved into an edge function, the exposed key rotated, and errors sent to monitoring

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find the real problem behind confusing errors and fix it securely. 🛠️

The result: €1,400, 3 business days. Diagnoses worked again the same evening, and around 1,100 customers ran diagnoses in the first week with no CORS errors. 🚀

👉 Seeing "blocked by CORS policy"? Here are the causes and safe fixes: https://launchstudio.eu/en/blog/why-do-i-get-cors-errors-in-my-ai-built-app

#CORS #Bolt #Supabase #WebDevelopment #AIFounder #LaunchStudio #Manifera
