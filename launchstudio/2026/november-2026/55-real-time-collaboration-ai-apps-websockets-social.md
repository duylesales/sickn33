# Social Media Post: Real-Time Collaboration in AI Apps with WebSockets

If your AI app is successful, it will be used by enterprise teams. And in the enterprise, no one works alone.

If User A edits a prompt while the AI is simultaneously streaming output, and you are using HTTP POST requests, you will corrupt the document.

You need Multiplayer Architecture:
1️⃣ Yjs (CRDTs): The math that prevents save conflicts.
2️⃣ WebSockets: The pipe that streams the keystrokes.
3️⃣ Hocuspocus (Fly.io): The long-running Node server (because Vercel Serverless doesn't do WebSockets).

Make your AI a "user" in the room. Let humans and agents type in the exact same document at the exact same time.

Read our technical guide on building Google-Docs style AI collaboration on the LaunchStudio blog.

#LaunchStudio #AISaaS #WebSockets #Yjs #CRDT #Nextjs #Tiptap
