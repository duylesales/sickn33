📊 SCORECARD: Stoffenstudio

Before: 9 out of 20
After: 19 out of 20

Iris Jansen runs a curtain and upholstery studio in Den Bosch and built Stoffenstudio in Lovable: customers choose a fabric, enter window measurements, see a price, pay a 30% deposit and book a fitting. Friends and early customers loved it. Before announcing it to her 6,000 Instagram followers, she filled in a 20-question production readiness scorecard. She scored 9.

Her "no" answers sat exactly where the scorecard says to worry most:
✗ Question 1: changing an order number in the URL showed other customers' orders, home addresses included
✗ Question 2: the admin page for adjusting prices was reachable by anyone who knew the address
✗ Question 9: the deposit was marked paid when the browser came back from Mollie
✗ Plus: no alerts, no staging, no tested backups

A one-day LaunchStudio review confirmed them, and found two more:
✗ An unrestricted file upload for window photos
✗ The Mollie API key visible in the page source

The fixes (7 business days, €1,750):
✓ Row Level Security on orders and customers
✓ Deposits confirmed by verified webhooks
✓ The admin area behind server-side role checks
✓ Uploads restricted
✓ The key rotated and moved
✓ EU backups with a tested restore, staging and alerts

Iris retook the scorecard: 19. The last point was a privacy notice she wrote herself that weekend.

The Instagram launch brought 212 configured orders and 58 paid deposits in the first fortnight, with no payment mismatches and no data complaints.

"The scorecard didn't fix anything, but it told me I wasn't ready in a way I couldn't argue with. That was worth more than reassurance." - Iris Jansen

https://launchstudio.eu/en/blog/is-your-ai-application-production-ready-a-20-question-scorecard

#Lovable #AIApp #AppSecurity #Startups #LaunchStudio #Manifera
