🚨 Nadia el Amrani's Verwijzing handles referral letters for a GP practice and two allied-health clinics in Roosendaal. A practice manager, checking a link, changed the number at the end of the address out of curiosity - and saw a different patient's referral letter. 😳

Nothing had gone wrong technically. That was exactly how it was built. Here's where user files go wrong: 🧠

❌ Uploads written beside the code, lost on the next redeploy
❌ Files served from a public path anyone can reach
❌ Filenames built from a patient's surname and a sequence number
❌ No size limits, no type validation, no record of who downloaded what

✅ Private storage under random identifiers, with ownership recorded per customer
✅ Downloads through signed links valid for minutes, after an authorisation check
✅ Server-side size limits and content-based type validation
✅ Access logging - and deletion that actually reaches storage and backups

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we move uploads out of the guessable-address danger zone. 📁

Her result: the feature was taken offline the same afternoon and the breach handled with the practice's data protection officer. Six business days and €3,400 later, every file lives in private storage behind signed links. The log review showed only the reporting manager had accessed the pattern - and the clinics stayed customers. 🚀

👉 Where user files should live in a Replit app: https://launchstudio.eu/en/blog/replit-file-uploads-where-user-files-should-live

#Replit #DataProtection #AVG #HealthTech #LaunchStudio #Manifera
