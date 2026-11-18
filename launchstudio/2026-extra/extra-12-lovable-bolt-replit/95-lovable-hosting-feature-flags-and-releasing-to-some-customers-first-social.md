🪜 Two ways to release an online booking widget to 58 dental practices

THE CLIFF
Monday morning ➜ all 58 at once.
Practices using split chairs (one chair shared by a dentist and a hygienist in the same hour) got the wrong availability.
Within three hours, eleven practices had double-booked chairs, and receptionists were phoning patients to move appointments.
Turning it off meant a rollback. The release also carried a migration and two unrelated fixes, so the rollback took all morning, with online booking down everywhere.

THE STAIRS
Step 1 ➜ a beta group of six practices, including the two largest and two that use split chairs
Step 2 ➜ 25%
Step 3 ➜ everyone
Over two weeks, without a double booking.

Evelien Hartman built Tandartsplanner in Lovable: appointment scheduling, recall reminders and online booking for 58 dental practices. That same month, an AI recall suggestion feature had a cost spike when a loop called the model over and over, and the only way to stop it was a deploy. 🦷

Building the stairs (LaunchStudio, 3 business days, €2,800):
✓ A feature flag table with kinds, owners and expiry dates, per-practice overrides and stable percentage rollout
✓ Flags evaluated on the server in the booking and recall functions, with only the results sent to the browser
✓ Kill switches for AI recall suggestions, SMS reminders and the booking widget, each with a clean "unavailable" state
✓ The six-practice beta group, who agreed to get features first
✓ Errors and slow requests tagged with active flags in the logs
✓ An audit of flag changes on the admin page, and a weekly report of release flags past their expiry
✓ Booking calculation tests with the widget's flag on and off

In six months, nine features went out the same way. A problem in a new invoicing screen was caught at three practices and switched off in under a minute. When the model provider went down for two hours, the AI kill switch went on and practices saw a clear message instead of errors.

"Releasing to all fifty-eight practices at once meant eleven of them found the bug for us before ten o'clock. Now six practices find it, and I switch it off before the others even see it." - Evelien Hartman

https://launchstudio.eu/en/blog/lovable-hosting-feature-flags-and-releasing-to-some-customers-first

#FeatureFlags #DevOps #SaaS #Lovable #LaunchStudio #Manifera
