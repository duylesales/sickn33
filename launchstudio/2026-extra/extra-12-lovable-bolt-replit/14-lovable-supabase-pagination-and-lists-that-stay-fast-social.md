📊 Two customers of one timesheet app

                          A typical firm     The largest firm (90 consultants)
Hour entries              about 3,000        about 240,000
Hours overview            instant            11 seconds
Monthly export            works              times out, every month
Workaround                none needed        exporting week by week

Rutger Doedens built Urenstaat with Lovable: timesheet and project-hours tracking for engineering consultancies, 34 firms. Two complaints arrived in the same fortnight, both from the same customer, and both with the same cause.

The overview fetched every hour entry for the firm and paginated in the browser. The export did the same, then built a CSV in memory. Fine for 3,000 rows. Not for 240,000.

His worst performance problems all lived in his best customer's account. They were the only ones with enough data to find them, and the last people he wanted finding them.

What LaunchStudio changed (1 business day, €1,900):
✓ Cursor pagination on timestamp and ID, with a matching composite index and a total sort order
✓ The row count replaced by a "next" control, using the fetch-one-extra technique
✓ Filters reduced from nine arbitrary fields to four with indexes, and the consultant-name filter moved to full-text search
✓ The export rewritten to walk the data with a cursor and stream rows straight to the response
✓ A background job, with an email link, for exports above a threshold
✓ Everything tested against a seeded database of 400,000 entries, not the 900 in development

📊 The largest firm, after
Hours overview: from 11 seconds to 240 milliseconds
Monthly export: 9 seconds, instead of failing
Workaround: no longer needed, and mentioned at renewal

"My worst performance problems were all in my best customer's account. They were the only ones with enough data to find them, and the last people I wanted finding them." - Rutger Doedens

https://launchstudio.eu/en/blog/lovable-supabase-pagination-and-lists-that-stay-fast

#Supabase #Performance #Pagination #Lovable #LaunchStudio #Manifera
