💡 "Expected savings: €X per year.*"

* Based on last year's gas price, an optimistic efficiency, and a subsidy scheme that changed months ago. Assumptions not shown.

That asterisk didn't exist in the original report. It should have. 🌡️

Rutger Visscher runs a heat pump installation company in Assen and built Warmtewijzer with Bolt and Supabase: homeowners enter details about their home and get an advice report with a recommended heat pump, expected savings, a subsidy amount and a quote. Leads came in fast. Then several customers complained after installation that their savings were far below the report. And one report showed a subsidy amount from a scheme that had changed months before.

The fine print the assessment found:
• Savings calculated in the browser with a fixed gas price from a year earlier and an optimistic efficiency, with no assumptions shown
• A hard-coded subsidy amount
• Reports with homeowners' addresses and floor plans in a public bucket
• Minute-level smart meter data, for customers who had connected a device, kept forever and visible to every installer in the company

Putting the fine print in plain view (LaunchStudio, Launch & Grow, 12 business days, €4,500, plus €49/month):
✓ Calculations moved to the server, with documented, versioned assumptions
✓ A range of expected savings in each report, with the key inputs shown
✓ Energy price and efficiency assumptions configurable, and each report recording which version it used
✓ Subsidy rules stored as data, with effective dates and the source, plus a note that customers must meet the conditions and apply themselves
✓ Reports in private storage with signed links
✓ Meter data limited to hourly values, with consent recorded and withdrawable, older data aggregated to daily, and access only for the installer handling that customer

Complaints about savings dropped once reports showed ranges and assumptions, and conversion stayed strong, because customers trusted the explanation. When subsidy amounts changed again, Rutger updated them in the admin panel within minutes.

"Our old report sold heat pumps with a number nobody could explain. Now it shows what we assume and why, and customers buy because they understand." - Rutger Visscher

https://launchstudio.eu/en/blog/production-launch-for-energy-transition-software

#EnergyTransition #HeatPump #Solar #Bolt #AIFounder #LaunchStudio #Manifera
