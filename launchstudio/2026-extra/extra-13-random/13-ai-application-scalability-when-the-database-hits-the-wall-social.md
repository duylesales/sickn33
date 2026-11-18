MYTH: "The app is slow, so I need a bigger server."
FACT: Two server upgrades changed nothing. Four indexes changed everything. 📚

Koen Hendriks, a librarian in Enschede, built Leesclub on Replit: book clubs schedule meetings, track reading progress chapter by chapter, and discuss books in threaded comments. It started with his own two clubs and grew through library networks to about 1,900 clubs and 14,000 readers across the eastern Netherlands.

The trouble came on Sunday evenings, when lots of clubs met and readers updated their progress at the same time. First slow, then errors. Koen upgraded his Replit deployment to a bigger machine. Twice. No difference.

MYTH: "Each request is independent."
FACT: Each one opened a new Postgres connection, and the limit ran out minutes into the Sunday peak.

MYTH: "A discussion page is one query."
FACT: It ran one query per comment, just to fetch the author.

MYTH: "The database will find the rows."
FACT: The reading-progress table had 3.2 million rows, and no index on club_id or user_id.

MYTH: "A counter is harmless."
FACT: Every progress update also incremented a counter on the club row, so members of large clubs queued behind each other.

What LaunchStudio changed (Launch & Grow, 9 business days, €2,800, plus €49/month):
✓ Connection pooling and a shared client
✓ Comments and authors fetched in a single query
✓ Four indexes, chosen from the slowest real queries
✓ The club counter replaced by a computed value, cached for five minutes
✓ Notification records older than 90 days archived
✓ Koen's app servers scaled back down to their original size

Sunday-evening errors stopped completely. The discussion page for the largest clubs went from about 3.5 seconds to 180 milliseconds. And hosting costs fell by around 35% once the unnecessary upgrades were reversed.

"I kept buying bigger servers for a problem that lived somewhere else. Four indexes did more than two upgrades." - Koen Hendriks

https://launchstudio.eu/en/blog/ai-application-scalability-when-the-database-hits-the-wall

#Postgres #Scalability #Replit #Supabase #LaunchStudio #Manifera
