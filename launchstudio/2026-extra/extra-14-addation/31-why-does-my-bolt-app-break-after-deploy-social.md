🎧 AUDIO TOUR: three stops where a museum app broke on its first day

Emma Lambrecht, a museum educator in Bruges, built Zaalgids with Bolt: visitors scan a QR code next to an artwork and get text, audio and a small quiz for children. In Bolt's preview, it was flawless. On Netlify, on the first test day, it broke at every stop.

STOP 1: The QR code
Each code linked straight to a room page, like /room/flemish-primitives. Every one returned 404, because there was no rewrite rule.

STOP 2: The audio
Emma added a rewrite by hand. Then the audio files didn't load. Their storage URL came from an environment variable that only existed in her Bolt session.

STOP 3: The quiz
Quiz scores, saved through Supabase, failed. The production domain was missing from Supabase's allowed URLs, which also broke the staff login.

THE RESTORATION (LaunchStudio, 6 business days, €1,600)
✓ Netlify rewrites
✓ Environment variables configured per environment
✓ Production and preview domains added to Supabase Auth settings
✓ Audio moved to a CDN-backed bucket, with caching for the museum's weak wifi
✓ Offline caching for the tour text
✓ A pre-deployment check that runs the production build and tests the QR routes automatically

END OF TOUR
Zaalgids went live for the museum's summer exhibition. Over twelve weeks, visitors started around 9,600 tours, and audio loaded reliably, even in the basement galleries.

"Every QR code pointed to a page that didn't exist, according to the server. In the preview, it had always existed." - Emma Lambrecht

https://launchstudio.eu/en/blog/why-does-my-bolt-app-break-after-deploy

#Bolt #Netlify #Vite #Deployment #LaunchStudio #Manifera
