🔎 ERROR DECODER

What the browser said:
"blocked by CORS policy"

What it actually meant, in Plantwijzer's case:
1. The function only allowed the preview domain
2. The function didn't answer preflight requests
3. The function crashed on large images and returned a 500 with no headers
4. (Not CORS at all, but found along the way) an AI provider key, visible in the frontend bundle

Mila Verbeek built Plantwijzer with Bolt and Supabase: customers photograph a houseplant, get an AI diagnosis of its health and receive care reminders. It worked perfectly on the Bolt preview domain. On launch day, she connected plantwijzer.nl, announced it to 9,000 newsletter subscribers, and every diagnosis failed.

She tried an online tip to allow all origins. Some requests started working. Others didn't. Four hours of fighting one message, because one message was hiding several problems.

The decoded fixes (LaunchStudio, 3 business days, €1,400):
✓ A shared CORS helper with an allowed-origins list for production, staging and local development, including both plantwijzer.nl and www.plantwijzer.nl
✓ Every function answers preflight requests and returns headers on errors too
✓ Image size checked before upload, with a clear message for oversized photos
✓ The AI call moved into an edge function, and the exposed key rotated
✓ Function errors sent to error monitoring

Diagnoses worked again the same evening. In the first week, around 1,100 customers ran diagnoses with no CORS errors. And the rotated key closed a gap that could have run up AI costs on Mila's account.

Next time you see "blocked by CORS policy": check whether the function crashed first.

"I spent four hours fighting a CORS message. The real problems were a hard-coded domain, a crash and a key I didn't know was public." - Mila Verbeek

https://launchstudio.eu/en/blog/why-do-i-get-cors-errors-in-my-ai-built-app

#CORS #Bolt #Supabase #WebDevelopment #AIFounder #LaunchStudio #Manifera
