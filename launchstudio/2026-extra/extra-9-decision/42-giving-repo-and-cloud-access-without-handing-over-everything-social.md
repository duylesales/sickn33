🚨 A Firebase service account key was still live eight months after the code using it was deleted. Nobody had told it to stop working. 😳

Trust is not an access model. Clicking Invite and picking the highest role is how founders get here: 🧠

❌ A `service_role` key pasted into a Cursor chat and a Discord thread
❌ A former designer still holding Write access, plus an unexplained deploy key
❌ A personal repo with no audit log and no clean way to offboard anyone
❌ A registrar login shared over chat — the credential that can take your identity

✅ Grant capability, not ownership: Write on GitHub, Developer on Supabase, never Admin
✅ Move contracted work into its own GitHub org and Supabase organisation first
✅ Use restricted Stripe keys and a scoped Cloudflare zone role, not the registrar login
✅ Write the revocation checklist the day you grant access, while you remember every click

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we set up scoped access service by service so you keep control while your engineer gets real capability. 🔐

His result: all three exposures resolved before the engagement began, run on scoped roles, offboarding done in eleven. 🚀

👉 Talk to an engineer who reads AI-generated code daily — bring your repo and permissions: [Link to article]

#IndieHacker #SupabaseSecurity #LaunchStudio #Manifera #AICoding #DevSecOps
