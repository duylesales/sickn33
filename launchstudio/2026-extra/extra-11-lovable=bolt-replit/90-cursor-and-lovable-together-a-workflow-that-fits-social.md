🚨 Ivo Schaminée built Servicecontract with Lovable - maintenance contract administration for eleven installation firms around Oss and Uden - and used Cursor for the parts the builder handled badly. One Thursday he consolidated the renewal calculation locally. On Friday a customer asked for a two-word label change. 😳

He made it in the builder, which regenerated the file holding the renewal logic - and his whole Thursday was gone. Here's how two tools collide on one codebase: 🧠

❌ Business logic living inside a screen the builder feels free to rewrite
❌ Local work not yet pushed while the builder pushes its own version
❌ No tests to catch a broken date rule
❌ Two tools editing the same area with no agreement on who owns what

✅ The renewal calculation extracted into its own module, with the mid-month rule confirmed by three firms
✅ Tests around the boundary cases
✅ The repository as source of truth, one shared formatter, committed lockfile and rules files for both tools
✅ A simple working agreement: pull before starting, push when finishing, one tool per area at a time

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set up Lovable and Cursor to work together instead of against each other. 🔀

His result: 34 reminders had gone out with wrong dates before anyone noticed. Seven business days and €3,300 later they were corrected - and there have been no collisions in the nine months since. 🚀

👉 Cursor and Lovable together - a workflow that fits: https://launchstudio.eu/en/blog/cursor-and-lovable-together-a-workflow-that-fits

#Cursor #Lovable #Workflow #GitHub #LaunchStudio #Manifera
