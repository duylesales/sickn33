6 days to build.
3 days before the trial.
1 developer friend doing a sanity check.
1 URL parameter.
0 row-level security.
2 racing teams about to share one database. 🏁

Bram Wolters built RaceGrid in Bolt in six intense days: a scheduling and telemetry-sharing platform for support crews at the TT Circuit Assen weekend. Team managers assign pit slots, share sensor data and message crew members in real time. It looked ready.

Three days before a trial rollout with two racing teams, Bram sent the link to a developer friend for a sanity check. The friend found that any logged-in user could open another team's telemetry feed just by editing the team ID in the URL. The Supabase tables had no row-level security at all.

The numbers on the other side:

4 business days to fix
€1,350 in total
1 full database schema audit
RLS policies scoped to team membership
1 Stripe secret key moved out of the frontend bundle into a server function
Backend permission checks on every API route that had only been checked in the UI

And the scoreboard:
0 data-isolation incidents during the TT weekend trial
1 extra team signed for next season

"I built RaceGrid to be fast, not to be a security project. I had no idea the way Bolt structured my database meant every team could see every other team's data. LaunchStudio found it and fixed it in less time than it took me to build the feature in the first place." - Bram Wolters

https://launchstudio.eu/en/blog/ai-security-vulnerabilities-assen

#AINativeFounder #LaunchStudio #Manifera #AISecurityVulnerabilities #Assen
