🚨 Marloes Vink, a photography teacher in Haarlem, built Lichtlessen in Lovable: an online course platform with video lessons, assignments and teacher feedback. She tested it for weeks - always logged in as herself, the admin. Two days before launch, a friend tried it as a student. In one hour, the friend found four launch blockers. 😳

She had tested her app for a month - just never as anyone other than the person who built it. Here's what one hour as a student revealed: 🧠

❌ Students could open other students' assignment submissions by changing a number in the URL
❌ "Mark as complete" worked on lessons the student hadn't bought
❌ Cancelled iDEAL payments still unlocked the course
❌ The video player failed in Safari on iPhone

✅ RLS fixed on submissions and lesson progress
✅ Course access checks moved to the server and tied to verified payment webhooks
✅ Video playback fixed with a compatible streaming setup
✅ Three Playwright tests (sign-up and purchase, student permissions, teacher feedback) running on every deployment

At **LaunchStudio**, backed by Manifera's QA practice from 11+ years and 160+ projects, every app is tested before launch with multiple roles, real payment scenarios and real devices. 🛠️

💡 Her result: €2,400, six business days. The launch went ahead a week later with 120 students in the first cohort, and the automated tests caught two regressions before students ever saw them. 🚀

👉 About to launch an AI-built app? Here's the practical pre-launch testing plan: https://launchstudio.eu/en/blog/how-do-i-test-my-ai-built-app-before-launch

#Testing #Lovable #Playwright #QA #LaunchStudio #Manifera
