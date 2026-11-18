Tested as the admin, for a month: ✅ everything works.
Tested as a student, for one hour: ❌ ❌ ❌ ❌ 📸

Marloes Vink, a photography teacher in Haarlem, built Lichtlessen in Lovable: an online course platform with video lessons, assignments and teacher feedback. She tested it for weeks, always logged in as herself. Two days before launch, a friend tried it as a student.

What the friend found in that one hour:
❌ Changing a number in the URL opened other students' assignment submissions
❌ "Mark as complete" worked on lessons the student hadn't bought
❌ Cancelled iDEAL payments still unlocked the course
❌ The video player failed in Safari on iPhone

None of it was visible from the admin account.

Marloes postponed by a week. What LaunchStudio did (6 business days, €2,400):
✓ RLS fixed on submissions and lesson progress
✓ Course access checks moved to the server
✓ Access tied to verified payment webhooks
✓ Video playback fixed with a compatible streaming setup
✓ Three Playwright tests on every deployment: sign-up and purchase, student permissions, teacher feedback

The launch went ahead a week later, with 120 students in the first cohort. In the following months, the automated tests caught two regressions before any student saw them.

Your one-hour test: log in as your newest, least-privileged user. Then try everything you shouldn't be able to do.

"I tested my app for a month. I just never tested it as anyone other than the person who built it." - Marloes Vink

https://launchstudio.eu/en/blog/how-do-i-test-my-ai-built-app-before-launch

#Testing #Lovable #Playwright #QA #LaunchStudio #Manifera
