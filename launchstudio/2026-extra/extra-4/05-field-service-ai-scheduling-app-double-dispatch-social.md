🚨 Two vans pulled up to the same address within twenty minutes of each other — both technicians convinced they'd been assigned the job. Jorrit Hagen's MonteurPlanner, built with Cursor, had let an office admin reschedule a job over the phone without ever writing that change back to the technician's availability calendar. The slot still showed open. 😳

Every field service scheduling tool eventually gets tested by this exact scenario — and most fail it, because the calendar was built as a display, not a single source of truth. 🧠

❌ Cursor generated conflict detection for the obvious case — two jobs booked through the same flow — but not for a manual reschedule made outside it
❌ Most AI-generated scheduling apps write assignments to the jobs table and availability to a separate, loosely connected process
❌ A reschedule via a side channel — an admin edit, a phone override — often updates the job but never fires the availability write-back
❌ The next automated dispatch fills that same "open" slot with a second technician, and nobody knows until both vans show up

✅ Route every path that touches a technician's schedule — automated booking, admin drag-and-drop, phone overrides — through one single availability function
✅ Add a locking check that blocks any second assignment to an already-committed slot, regardless of which interface triggered it
✅ Fire an immediate admin-facing conflict alert instead of silently allowing the double-booking

At **LaunchStudio**, this is a textbook example of what our CEO Herre Roelevink calls the real challenge today — not the idea, but the concurrency architecture underneath it. Backed by Manifera's 120+ engineers. 🛡️

His result: MonteurPlanner has run without a single double-dispatch incident since, across a technician team that's grown from four to nine. 🚀

👉 Got a manual-override path in your scheduling tool? Get a scoped review before it finds your busiest technician: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #FieldService #AIScheduling
