🚨 Wouter van Rossum runs an inspection company in Den Helder and built Keuringsapp with Bolt: inspectors fill in fire safety checklists on tablets and generate client reports. One evening he deployed a new checklist version from his laptop - without the matching database column, which existed only in his local notes. The next morning, inspectors couldn't submit reports for three hours. 😳

Every release depended on him remembering five manual steps. Here's how deployment worked before: 🧠

❌ Builds made on his laptop and uploaded to Netlify by hand
❌ Database changes made by hand in the Supabase dashboard, not in git
❌ No checks before a release reached inspectors
❌ Once, a deploy from a branch with unfinished changes

✅ The repository connected to Netlify with staging and production branches
✅ Every schema change moved into migrations
✅ A GitHub Actions workflow with lint, build, migrations and two end-to-end tests
✅ Edge functions deployed through the CLI, and rollback steps documented

At **LaunchStudio**, backed by Manifera's 160+ enterprise projects with GitHub Actions and cloud pipelines as standard, we make AI's speed safe: checks, staging, deliberate promotion and one-click rollback. 🛠️

💡 His result: €1,500, four business days. Over the next quarter, Wouter released 22 updates without a failed deployment - and one broken build from a Bolt change was blocked automatically before it reached inspectors. 🚀

👉 Still deploying your Lovable or Bolt app by hand? Here's a practical CI/CD setup: https://launchstudio.eu/en/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app

#CICD #GitHubActions #Bolt #Supabase #LaunchStudio #Manifera
