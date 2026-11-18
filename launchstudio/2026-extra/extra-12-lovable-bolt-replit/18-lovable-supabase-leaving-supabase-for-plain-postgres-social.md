🎭 DRESS REHEARSAL, then opening night

THE PRODUCTION
Gerlof Tichelaar built Zorgdossier in Lovable: care plan administration for small-scale residential care providers, 26 organisations, around 1,400 residents. A regional healthcare group offered a contract for nine locations, worth more than his entire existing revenue. Its procurement required personal data processed on infrastructure under a specific agreement, with a named certification, in a specific region.

THE CASTING CALL
He asked Supabase first, the step most founders skip. Part of the requirement could be met on different terms. The region and certification couldn't, on his timeline. So: a migration, not because Supabase wasn't good enough, but because a procurement department needed a specific answer.

THE DRESS REHEARSAL (on a copy)
• Found two extensions in use that the target didn't enable by default
• Measured the real cutover at 40 minutes, not the two hours assumed

THE PRODUCTION WORK (LaunchStudio, 16 business days across three weeks, €11,800)
✓ The database migrated to managed Postgres in the required region, with row counts and constraints verified against the source
✓ Authentication moved with password hashes imported, so no carer had to reset anything
✓ 31 Row Level Security policies rewritten against the new identity claim, and social login restored for the two organisations using it
✓ 94,000 documents copied, with two weeks of dual reads, and old links redirected instead of broken
✓ Realtime replaced with polling on the two screens using it, after confirming live updates weren't clinically necessary
✓ Backups configured, with a restore performed and timed
✓ The old project retired after a month, with a verified archive

OPENING NIGHT
Six o'clock on a Sunday morning. The 40-minute cutover. Nobody noticed.

THE REVIEWS
The contract was signed. Monthly infrastructure went from €85 to €310, which Gerlof calls the least interesting number in the project. The rehearsal is the part he recommends.

"I did not migrate because Supabase was not good enough. I migrated because a procurement department needed a specific answer, and that is the only reason I would do it again." - Gerlof Tichelaar

https://launchstudio.eu/en/blog/lovable-supabase-leaving-supabase-for-plain-postgres

#Supabase #PostgreSQL #Migration #HealthTech #LaunchStudio #Manifera
