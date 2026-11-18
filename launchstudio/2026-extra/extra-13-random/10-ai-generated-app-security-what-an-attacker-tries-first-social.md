🕵️ A guest's first five minutes with a cheese farm tour app (minute marks dramatized)

MINUTE 1: She opens her ticket. The URL ends in a booking number.
MINUTE 2: She changes the number. Another family's booking appears: names, phone number, hotel.
MINUTE 3: She types /admin after the domain. A page loads listing every booking of the season.
MINUTE 5: She emails the founder. Politely.

Ruben Dekker organises tours of traditional cheese farms around Alkmaar and built Kaasroute in Bolt: tourists book a tour, pay online and get a digital ticket with a QR code, and partner farms see upcoming visitors. In its second summer, Kaasroute handled a few thousand bookings, many from international visitors. The admin link wasn't shown anywhere in the app. Ruben assumed nobody would look.

The guest, who worked in IT, looked in her first five minutes. And Ruben was lucky it was her.

What LaunchStudio did, starting the same day (4 business days, €1,100):
✓ Day one: the admin area and its API locked behind server-side role checks
✓ Day one: ownership checks, so a ticket is visible only to its booker, with unguessable ticket codes instead of sequential numbers
✓ A payment API key found in the page source, rotated and moved server-side
✓ Rate limiting and uniform error messages on login
✓ The farm partners' portal limited to each farm's own visitors
✓ Logs checked for signs of earlier access, and help assessing whether a data breach notification was needed

No evidence of wider access turned up in the logs. Kaasroute finished the season with the fixes in place. Ruben sent the guest a free tour for two, and added a "report a security issue" address to the site's footer.

"I assumed nobody would look. Somebody looked in her first five minutes, and I'm lucky it was her." - Ruben Dekker

https://launchstudio.eu/en/blog/ai-generated-app-security-what-an-attacker-tries-first

#AppSecurity #Bolt #OWASP #Startups #LaunchStudio #Manifera
