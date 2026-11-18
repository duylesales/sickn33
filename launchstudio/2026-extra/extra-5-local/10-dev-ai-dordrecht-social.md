4 shipping agents.
2 months.
1 server that couldn't scale.
0 monitoring.
4 hours offline.
2 phone calls at once.

That's the Dockflow story in six lines.

Eva Mulder built Dockflow in Lovable for berth scheduling and cargo-handoff coordination between small shipping agents on the rivers around Dordrecht. It launched cleanly. It ran on a single server instance that had been fine in testing.

Then came a week of unusually heavy shipping traffic. The server hit its resource limit and went down with zero warning. Eva found out when two agents called mid-operation asking where their berth schedules had gone. The emergency fix went live by hand and untested, because there was no deployment pipeline.

Now the other numbers:

6 business days to fix it
€1,850 in total
3 changes: auto-scaling infrastructure, uptime monitoring with real-time alerts, and a CI/CD pipeline with staging
0 unplanned downtime in the 4 months since

"Four hours doesn't sound like much until it's four hours during an actual shipment window, and two clients are calling you at once." - Eva Mulder

Dev AI tools make the first version cheap. Keeping it online belongs in the budget too.

👉 https://launchstudio.eu/en/blog/dev-ai-dordrecht

#AINativeFounder #LaunchStudio #Manifera #DevAI #Dordrecht
