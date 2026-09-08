🚨 Fatima's Dubai customer said monthly invoices never matched their own records. Fourteen months of invoices had been quietly wrong — and the product never once showed an error. 😳

Founders assume a timestamp is a timestamp everywhere. Here's why that's the bug that never announces itself: 🧠

❌ Time entries were stored as browser timestamps with no conversion, so their meaning depended on where the person happened to be sitting
❌ Monthly totals were computed against UTC boundaries, so anything logged after 20:00 on the 31st in Dubai fell into the next month
❌ Recurring weekly reminders stored as fixed UTC times had shifted an hour after the last clock change — customers adjusted their calendars manually rather than reporting it
❌ Adding 24 hours to get "tomorrow at the same time" breaks on the two nights a year a day is 23 or 25 hours long

✅ Store every moment in UTC and convert only for display — never store a browser time without converting it
✅ Compute report boundaries in each customer's own timezone, not the server's
✅ Use a date type without a time component for calendar dates like birthdays and invoice dates
✅ Store the timezone alongside recurring events so they stay correct across daylight saving changes

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit date handling before a customer discovers it's been wrong for over a year. 🕐

Her result: all timestamps converted to UTC with originating timezone retained, reporting fixed per account, and 14 months of entries corrected through a verified backfill. 🚀

👉 Find out where your product's dates are quietly lying: https://launchstudio.eu/en/blog/time-zones-and-dates-the-quiet-source-of-wrong-answers

#SaaS #Engineering #IndieHacker #FounderLife #LaunchStudio #Manifera
