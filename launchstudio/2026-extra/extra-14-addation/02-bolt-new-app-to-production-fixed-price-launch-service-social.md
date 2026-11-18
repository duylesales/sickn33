Bolt preview: ██████████████████░░ 90%
Production:   ░░░░░░░░░░░░░░░░░░░░ 0%

The last 10% is where the app actually has to work. 🔧

Maarten Oosterhuis runs a small heat pump installation business in Zwolle. He built Offertewerk in Bolt.new so his installers could quote at the customer's kitchen table on a tablet: pick a model, measure the rooms, add labour, generate a PDF. In the Bolt preview, it was perfect.

Then he exported to GitHub and deployed to Netlify. Three things broke at once:
1. The build failed, because two component imports differed only in letter case
2. After he fixed that by hand, every page except the homepage returned 404 on refresh, which installers hit constantly on patchy mobile connections
3. PDF generation failed silently, because the PDF service's API key had only ever existed in his Bolt session

The last 10% (LaunchStudio, 8 business days, €1,850):
▓ Import paths fixed, plus a lint rule that catches case mismatches
▓ SPA rewrites configured on Netlify
▓ The PDF call moved into a serverless function, with the key as an environment variable
▓ Row Level Security, so each installer sees only their own quotes
▓ A staging site for testing Bolt changes, and uptime alerts to Maarten's phone

Production: ████████████████████ 100%

Offertewerk went live eight business days later. That heating season, four installers created around 620 quotes from the field. The share of quotes sent the same day rose from roughly a third to nearly all of them.

"Bolt got me ninety percent of the way. The last ten percent was stuff I didn't even know existed until it broke." - Maarten Oosterhuis

https://launchstudio.eu/en/blog/bolt-new-app-to-production-fixed-price-launch-service

#BoltNew #Netlify #AIApp #Deployment #LaunchStudio #Manifera
