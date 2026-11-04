🚨 Lien Vermeulen coordinates a running club in Eindhoven and built Loopmaatje in Lovable: group runs, routes, check-ins and club challenges. Members kept asking for "the app", so she wrapped it with Capacitor herself and submitted it to Apple. It was rejected. Twice. 😳

She thought the hard part was wrapping the app. The hard part was making it something Apple considered an app. Here's what stood in the way: 🧠

❌ Guideline 4.2: the app was essentially the website in a wrapper
❌ Reviewers couldn't log in - sign-up needed a club invitation code
❌ The Supabase service key bundled inside the app, extractable by anyone
❌ No native features that made it worth installing

✅ Backend made production ready first: keys in edge functions, Row Level Security per club
✅ Native push notifications for run changes and weather cancellations
✅ Location-based check-in at the start point and offline route maps
✅ A reviewer demo account and submission notes explaining the native features

At **LaunchStudio**, backed by Manifera's 11+ years of building and publishing mobile apps, we take Lovable apps to phones - as a PWA or through Capacitor into the stores. 🛠️

💡 Her result: €6,400, eighteen business days. Approved on the next submission, installed by about 230 of the club's 310 members within three months - and she kept updating the interface in Lovable. 🚀

👉 Want your Lovable app in the App Store? Capacitor vs PWA, and what Apple really checks: https://launchstudio.eu/en/blog/can-i-publish-my-lovable-app-to-the-app-store

#Lovable #Capacitor #PWA #AppStore #LaunchStudio #Manifera
