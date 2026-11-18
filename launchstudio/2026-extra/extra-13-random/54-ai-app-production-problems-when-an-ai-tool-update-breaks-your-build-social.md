⛵ WHAT WAS ASKED vs. WHAT CHANGED

ASKED: "Update the text on the course overview page."

CHANGED:
✓ The text on the course overview page (looked perfect)
✗ The shared date-formatting helper, regenerated with a different library that read dates in UTC
✗ The Supabase client, updated along the way, changing how sessions refresh
✗ (Nothing to stop it: no committed lockfile)

Two days later, a student called. Her booking confirmation showed the wrong date.

Lars Nieuwenhuis runs a sailing school on the IJsselmeer near Hoorn and built Zeilschool in Lovable: students book courses, pay via iDEAL, choose boat types and get weather-dependent confirmations. A smooth season, about 1,100 bookings. Then that one copy change.

What it caused:
• Bookings made in the evening shifted to the next day, in confirmations and in the instructor schedule
• Some students logged out mid-booking
• Asking Lovable to revert produced a third variant, with problems of its own

What LaunchStudio did (5 business days, €1,450):
✓ The last known good versions restored from the history Lovable had synced to GitHub
✓ Date handling fixed, with the Europe/Amsterdam time zone set explicitly
✓ The lockfile and Node.js version committed and pinned
✓ Dependabot, with a test gate
✓ Tests for booking dates, login, payment and confirmation emails
✓ A staging environment
✓ Project rules telling Lovable not to change dependencies or shared helpers without explicit instruction
✓ Affected bookings corrected, and students notified

The summer season: around 1,500 bookings, no date or login regressions. Two later Lovable edits were caught by the tests before production, one of them another unintended helper change.

"I changed some words on a page and my app forgot what day it was. Now a change that touches more than I asked for can't reach my students." - Lars Nieuwenhuis

https://launchstudio.eu/en/blog/ai-app-production-problems-when-an-ai-tool-update-breaks-your-build

#Lovable #Regression #Testing #DevOps #LaunchStudio #Manifera
