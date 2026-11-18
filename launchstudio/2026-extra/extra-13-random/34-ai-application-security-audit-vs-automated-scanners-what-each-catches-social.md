🚦 FOUR SCANNERS AND ONE REVIEW

🟢 Dependabot: all clear
🟢 Semgrep: all clear
🟢 gitleaks: all clear
🟢 Weekly OWASP ZAP scan: all clear
🔴 Independent review: four access-control issues

Niels Brandsma, a backend developer in Hoofddorp, built SlotPark with Cursor: companies near Schiphol share unused parking spaces with each other's employees through a booking app, with monthly invoicing. Being security-conscious, he ran all four scanners. Twelve companies and about 400 employees used it. Then a prospective customer, an airline services company, required an independent review before signing.

The review found nothing the scanners had missed in their own categories. They were right about everything they could see. It found four things they couldn't:
🔴 Any employee could view and cancel other companies' bookings by changing a booking ID
🔴 The company-admin API checked that a user was an admin, but not of which company, so any company admin could edit another company's spaces and pricing
🔴 Row Level Security was on for bookings, with a policy allowing reads by any authenticated user
🔴 Invoice amounts were calculated from prices the client sent during booking

Turning red to green (LaunchStudio, 5 business days, €1,250):
✓ Ownership and tenant checks fixed
✓ RLS policies rewritten to scope by company and user
✓ Price calculation moved to the server
✓ 27 automated authorisation tests for every role and tenant boundary, added to the same CI pipeline as the scanners

The airline services company signed after receiving the review and re-test report. And in the year that followed, the authorisation tests caught two regressions while the scanners, as before, stayed green.

"I had four tools telling me I was fine. They were right about everything they could see. The problems were all in what they couldn't." - Niels Brandsma

https://launchstudio.eu/en/blog/ai-application-security-audit-vs-automated-scanners-what-each-catches

#AppSecurity #SAST #DevSecOps #Cursor #LaunchStudio #Manifera
