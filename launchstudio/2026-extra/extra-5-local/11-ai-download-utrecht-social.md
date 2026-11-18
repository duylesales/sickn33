Dear Utrecht student founder who just hit "Download" on your AI-built app,

Congratulations. Really. You built something that works, and the code is yours.

Before you share the link with your study group, try one small test: log in, open one of your own records, and change the number at the end of the URL.

Merel Kramer didn't know to try that. She built StudyLoop, a note-sharing platform for study groups, with Lovable. She downloaded the code, put it on a free hosting tier and shared it with three groups. Within a week, a fellow student changed a number in the URL and read someone else's private notes.

Nobody hacked anything. The database had no row-level security. The AI had written queries that fetched notes by ID without checking who owned them. Every note was technically public to anyone who knew where to look.

Here's what fixed it, in 5 business days for €900:
- Row-level security policies tied to account ownership
- Session-based authorization checks at the database layer
- A staging environment, so changes get tested before real users see them

StudyLoop now serves 200+ active students across three Utrecht study programs, with no unauthorized access since the fix.

Merel put it best: "I thought downloading the code meant I was done."

You're not done yet. But you're closer than you think.

Warmly,
The LaunchStudio team, backed by Manifera's 11+ years of production engineering

P.S. The full download-to-launch checklist is here: https://launchstudio.eu/en/blog/ai-download-utrecht

#AINativeFounder #LaunchStudio #Manifera #AIDownload #Utrecht
