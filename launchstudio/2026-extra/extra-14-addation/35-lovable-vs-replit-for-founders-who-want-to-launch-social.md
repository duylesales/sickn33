⚽ Who does what? Splitting one product between two tools

Bas Groen coaches youth football in Alkmaar and wanted Scorebord: coaches enter match events on a phone during games, and parents see live scores, player minutes and season statistics. He built two prototypes, one in Lovable and one with Replit Agent.

A demo comparison would have picked Lovable for everything: its interface was clearly nicer. A workload comparison said something different. Replit's version ran a Python worker that calculated season stats and fair-play minutes overnight. The Lovable version did that by loading every match into the browser.

So Bas sorted the jobs:

LOVABLE'S JOB
📱 The coach and parent interface
📱 Live scores and match events

REPLIT'S JOB
🐍 A small Python service for nightly statistics

Both halves had production gaps. In Lovable, any parent could edit match events. In Replit, the worker used the development database and kept credentials in a config file.

How LaunchStudio connected the two (10 business days, €3,300):
✓ Supabase with Row Level Security: only a team's coaches write match events, parents can only read
✓ The Replit worker on a scheduled deployment, reading from Supabase through a restricted database role and writing to a statistics table
✓ Secrets moved to Replit Secrets and Supabase edge function secrets
✓ Monitoring on both parts

Scorebord launched for twelve teams at Bas's club, with about 400 parents following matches live. The nightly stats run takes under two minutes, and browsers no longer load full seasons.

"Comparing demos would have picked Lovable for everything. Comparing workloads showed me where each tool actually fits." - Bas Groen

https://launchstudio.eu/en/blog/lovable-vs-replit-for-founders-who-want-to-launch

#Lovable #Replit #SportsTech #AIFounder #LaunchStudio #Manifera
