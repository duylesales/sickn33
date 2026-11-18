🧪 The two-account test. No code reading required.

1. Create two accounts in your app.
2. Log in as account A and open one of your own records.
3. Copy the URL.
4. Log in as account B and paste it.
5. If B can see A's data, you have a problem.

Anouk Smit, a primary-school teacher in Haarlem, ran this test herself. It failed immediately. 👶

She built Oppasklok in Bolt to solve a problem in her own friend group: sharing babysitters between five families. Word of mouth grew it to about 60 families, each with a profile listing children's names, ages, allergies and home addresses. Before opening it to a local parents' association of several hundred members, she read about AI app security and tried the test.

By changing a number in the URL, any logged-in parent could open any family's profile, children's allergies and address included. A second test, "view source," turned up a mapping API key in the page.

Anouk didn't know what either finding meant technically. She knew it wasn't something to launch with.

What LaunchStudio did (5 business days, €1,450):
✓ Database-level access rules: each family's data visible only to that family and the babysitters they explicitly invite
✓ The mapping key moved into a server-side function, with usage limits
✓ Backups in an EU region, with a tested restore
✓ Simple uptime alerts to Anouk's phone
✓ And then, on a call: the two-account test again, so she could watch it fail safely

Oppasklok opened to the parents' association two weeks later, and grew to 240 families by the end of the school year, with no data-access incidents. Anouk still runs the test herself after every major change.

"I couldn't read a line of the code, but I could run the test. Being able to see the fix myself mattered more than any explanation." - Anouk Smit

https://launchstudio.eu/en/blog/how-to-productionize-an-ai-app-when-you-cant-read-the-code

#Bolt #NoCode #AppSecurity #Startups #LaunchStudio #Manifera
