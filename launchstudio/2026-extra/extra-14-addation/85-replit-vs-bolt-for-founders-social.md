🌙 03:00. Who's checking competitor prices?

In Prijswacht's first version: nobody.

Sven Dijkman built Prijswacht in Bolt, so small webshop owners could track competitors' prices and get alerts when they change. The dashboard looked great in Bolt's preview. But the core feature, checking hundreds of competitor pages every few hours, ran as code in the browser while the dashboard was open. Close the tab, and the checking stopped.

So Sven rebuilt the checker with Replit Agent, as a Python worker on a scheduled deployment, and kept the Bolt dashboard. A night shift, finally. But it was connected loosely: the worker wrote to the same Supabase database using an over-privileged key.

What LaunchStudio set up, keeping both halves (11 business days, €3,600):

THE DAY SHIFT (Bolt)
✓ The dashboard deployed on Netlify
✓ Row Level Security per shop

THE NIGHT SHIFT (Replit)
✓ A scheduled deployment with a restricted database role
✓ Rate limiting towards competitor sites
✓ Retry logic
✓ Monitoring

THE HANDOVER
✓ Alerts sent by an edge function whenever a price change is detected

03:00 now: the checks run, every four hours, whether anyone is online or not. Within a quarter, Prijswacht reached 75 paying webshops.

"Bolt built the dashboard I wanted. The feature that mattered needed a server that never sleeps, and that's where Replit fitted." - Sven Dijkman

https://launchstudio.eu/en/blog/replit-vs-bolt-for-founders

#Replit #Bolt #SaaS #Supabase #LaunchStudio #Manifera
