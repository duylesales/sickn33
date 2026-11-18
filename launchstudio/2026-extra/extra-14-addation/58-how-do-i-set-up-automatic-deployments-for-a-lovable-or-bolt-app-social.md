✈️ THE OLD PRE-FLIGHT CHECKLIST, kept in one founder's head

☐ Build on the laptop
☐ Upload files to Netlify
☐ Change the database by hand in the Supabase dashboard
☐ Remember which column goes with which version (it's in my local notes)
☐ Make sure I'm on the right branch

Miss one step, and the flight goes down.

Wouter van Rossum runs an inspection company in Den Helder and built Keuringsapp with Bolt: inspectors fill in fire safety checklists on tablets, attach photos and generate reports for clients. Every release depended on Wouter remembering those five steps.

One evening, he deployed a new checklist version without its matching database column, which existed only in his local notes. The next morning, inspectors couldn't submit reports for three hours. Another time, he deployed from a branch with unfinished changes.

THE NEW CHECKLIST, run by the pipeline (LaunchStudio, 4 business days, €1,500)
☑ The repository connected to Netlify, with staging and production branches
☑ Every schema change in a migration
☑ A GitHub Actions workflow: lint, build, migrations and two end-to-end tests
☑ Edge functions deployed through the CLI
☑ Rollback steps documented

The next quarter: 22 updates, no failed deployments. One broken build from a Bolt change was blocked automatically before it reached any inspector.

"Every release depended on me remembering five manual steps. Now the pipeline remembers them for me." - Wouter van Rossum

https://launchstudio.eu/en/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app

#CICD #GitHubActions #Bolt #Supabase #LaunchStudio #Manifera
