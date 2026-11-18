🔴 INCIDENT REPORT: SensorForge
Severity: High | Downtime: 6 hours | Status: Resolved

SUMMARY
A routine update took SensorForge offline. SensorForge is an IoT fleet-monitoring dashboard that Delft founder Daan Smit built entirely in Cursor for engineering teams running distributed sensor networks.

TIMELINE
1. Daan pushes a change straight to production. No staging test.
2. A database migration runs incorrectly.
3. The dashboard goes dark during a pilot customer's active monitoring window.
4. There is no rollback. Daan rebuilds the previous database state by hand from partial logs.

ROOT CAUSE
Not the code. The process. Every deploy went from a laptop straight to production, with nothing in between.

CONTRIBUTING FACTOR
Writing good code and running production infrastructure are different skills. Daan had the first one.

REMEDIATION (LaunchStudio, 8 business days, €2,100)
✔ CI/CD pipeline with automated tests
✔ Staging environment that mirrors production
✔ One-command rollback

OUTCOME
Manual production deploys eliminated entirely.

FOUNDER STATEMENT
"I could write the code. I had no idea how exposed I was every single time I hit deploy, until it actually cost a customer six hours of downtime." - Daan Smit

Building AI products solo? Set up the pipeline before you have to write your own incident report: https://launchstudio.eu/en/blog/build-ai-delft

#AINativeFounder #LaunchStudio #Manifera #BuildAI #Delft
