💬 Four copies of the same login code, arguing (dramatized)

CLIENT 1: I'll refresh the token now.
CLIENT 2: No, I'll refresh it now.
CLIENT 3: I just refreshed it. Yours is old.
CLIENT 4: The phone was locked and the signal's weak. Refresh failed. Signing the user out.
SALES REP: ...I was halfway through my visit notes.

Ruud Koopman built Klantbezoek in Lovable: a CRM-lite for the field sales reps of a building supplies wholesaler, used on phones between customer visits. Reps complained they were logged out constantly, often while typing visit notes, which were then lost.

LaunchStudio found three causes at once:
1. The code created a Supabase client in four different components, each refreshing tokens on its own schedule
2. The app ran on both klantbezoek.nl and www.klantbezoek.nl, and notification emails linked to the www version
3. When phones locked between visits, token refresh failed on weak connections, and the app signed users out instead of retrying

What changed (4 business days, €1,200):
✓ One single client module
✓ www redirected to the canonical domain, with redirect settings updated
✓ Refresh retried when the connection comes back, instead of signing out
✓ Draft visit notes saved locally, so nothing is lost even if a session does expire

The same conversation now:
CLIENT: Connection's back. Refreshing. All good.
SALES REP: (keeps typing)

Unexpected logouts went from a daily complaint to essentially none. And once reps trusted the app, visit notes logged per rep per week rose noticeably.

"Every logout cost a rep their notes and their patience. The cause turned out to be four copies of the same login code arguing with each other." - Ruud Koopman

https://launchstudio.eu/en/blog/why-does-my-lovable-app-log-users-out

#Lovable #Supabase #Authentication #UX #LaunchStudio #Manifera
