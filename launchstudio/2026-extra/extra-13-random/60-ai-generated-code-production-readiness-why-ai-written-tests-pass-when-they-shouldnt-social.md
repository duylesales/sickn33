📊 TEST SCOREBOARD: Energiemeter

                     Before    After
Test coverage        89%       81%
Mutation score       31%       84%
Regressions caught   -         4 in the next six months

Coverage went down. The tests got much better. 🔌

Wouter Jacobs, a data engineer in Kampen, built Energiemeter with Cursor: households connect smart-meter data, and the app compares their real usage against energy contracts on the market, including dynamic hourly tariffs, and alerts them when switching would save money. Around 2,600 households, plus a premium tier with automated switching advice. Wouter was proud of 89% coverage, all written with Cursor.

Then a customer complained the app had recommended a contract that would have cost her more. LaunchStudio found:
• The dynamic-tariff cost calculation was wrong around daylight-saving transitions
• Fixed charges were double-counted for some contract types
• The calculator tests asserted exactly those wrong results, because they'd been generated from the implementation
• The access tests mocked the Supabase client and only checked it was called with a user ID. They still passed when LaunchStudio deliberately removed the RLS policy.
• No test checked whether users could read other households' meter data, and through one reporting endpoint, they could

The tests were a mirror. They showed exactly what the code did, mistakes included.

What changed (7 business days, €1,900):
✓ The calculation and the reporting endpoint fixed
✓ Calculator tests rebuilt from hand-verified reference cases, including daylight-saving days and every contract type
✓ Access tests against a local Supabase instance, with negative cases for every table
✓ Payment tests in Stripe test mode
✓ A mutation-testing pass on the calculator and access layers
✓ All of it in CI

Recommendations were recalculated for every user, and affected customers informed. The new tests caught four regressions from Cursor edits in six months, two in the tariff calculator. And after Wouter published how calculations are verified, premium subscriptions grew 40%.

"My tests were a mirror. They showed me exactly what the code did - including the mistakes." - Wouter Jacobs

https://launchstudio.eu/en/blog/ai-generated-code-production-readiness-why-ai-written-tests-pass-when-they-shouldnt

#Testing #MutationTesting #Cursor #EnergyTech #LaunchStudio #Manifera
