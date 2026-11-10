🚨 Thomas Verhoeven bouwde Coachclip met v0, Next.js en Supabase: sportcoaches uploaden trainingsvideo's, tekenen aantekeningen en delen feedback met spelers. Volledig gehost op Vercel werkte het prachtig - tot clubs meer video uploadden en de maandrekening snel opliep. 😳

Bandbreedte en lange videoverwerking in serverless functies zorgden voor kosten en timeouts. Thomas overwoog alles naar Hetzner te verhuizen - maar had nog nooit een server beheerd. Zo kiezen EU-oprichters tussen Hetzner en Vercel: 🧠

❌ Videobestanden die via de applicatie werden geserveerd
❌ Transcoding binnen request handlers, met timeouts
❌ Een snel stijgende rekening voor bandbreedte
❌ Een volledige verhuizing naar servers die niemand in het team kon beheren

✅ De Next.js-frontend op Vercel gehouden, met Europese functies
✅ Video's in EU-objectopslag met een CDN en signed URLs
✅ Transcoding op een geharde Hetzner-worker in Duitsland, gedeployd vanuit GitHub met monitoring
✅ Supabase in Frankfurt met een jobwachtrij die app en worker afstemt

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, geven we u de besparing zonder de meldingen om drie uur 's nachts. 🛠️

💡 Het resultaat: €5.300, 13 werkdagen. De maandelijkse infrastructuurkosten daalden met zo'n 65%, videoverwerking werd betrouwbaar zonder timeouts, en de worker draait onder de managed hosting van LaunchStudio. 🚀

👉 Hetzner of Vercel voor uw EU-SaaS? Zo beslist u: https://launchstudio.eu/nl/blog/hetzner-vs-vercel-for-eu-founders

#Hetzner #Vercel #CloudCosts #SportsTech #AIFounder #LaunchStudio #Manifera
