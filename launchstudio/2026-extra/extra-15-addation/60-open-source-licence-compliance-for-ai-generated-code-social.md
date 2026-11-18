⏳ Two weeks before closing

THE DEAL
Nina Postma built Roosterwijzer with Cursor and Supabase: scheduling and workforce planning for childcare organisations, with a Next.js frontend and a separate reporting service. Two years in, with steady revenue, she agreed terms with a sector-focused fund. Subject to technical due diligence.

THE REQUEST
The fund's reviewer asked for a licence inventory. Nina didn't have one.

THE SCAN
Over 900 packages. Most permissively licensed. But:
• The reporting service, partly agent-generated, embedded a modified AGPL-licensed charting and reporting server that customers used through the app
• Two smaller packages had no licence at all
• The frontend shipped without third-party notices
• A commercial font was embedded in PDF reports without a matching licence

THE RATING
AGPL issue: high priority. The fund wanted a remediation plan before closing.

THE NEXT TWO WEEKS (LaunchStudio, 12 business days, €4,700)
→ The modified AGPL component replaced with a permissively licensed charting library, with the affected reports rebuilt in the same layout
→ The two unlicensed packages replaced with maintained alternatives
→ The commercial font swapped for an openly licensed equivalent
→ A third-party notices page generated automatically at build time
→ Licence scanning and SBOM generation in CI, plus a written dependency policy
→ Cursor's project instructions listing approved libraries and asking for licence checks on new dependencies
→ The changes and AI tool settings documented for the reviewer

CLOSING DAY
The reviewer closed the AGPL finding within two weeks, and the investment completed on the original terms.

AFTERWARDS
Roosterwijzer now includes its SBOM in public-sector tenders, which childcare organisations' procurement teams increasingly ask for.

"I had never opened a licence file in my life. One embedded component nearly changed the terms of our funding round." - Nina Postma

https://launchstudio.eu/en/blog/open-source-licence-compliance-for-ai-generated-code

#OpenSource #Licensing #DueDiligence #Cursor #AIFounder #LaunchStudio #Manifera
