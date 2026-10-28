🚨 Wouter Jacobs, a data engineer in Kampen, built Energiemeter with Cursor: households connect smart-meter data and the app compares their real usage with energy contracts - including dynamic hourly tariffs - and advises when to switch. About 2,600 households. He was proud of 89% test coverage, all written by Cursor. Then a customer complained the app had recommended a contract that would have cost her more. 😳

Dynamic tariffs were miscalculated around daylight-saving changes, and fixed charges were double-counted for some contracts. The calculator tests asserted exactly those wrong results - they'd been generated from the implementation. Access tests mocked Supabase and still passed with row level security deliberately removed. And one reporting endpoint let users read other households' meter data. Here's why AI-written tests pass when they shouldn't: 🧠

❌ Tests that mirror the code - bugs included
❌ Mocks that hide the very thing being tested
❌ No negative tests for the wrong user or tenant
❌ Coverage mistaken for protection

✅ Calculation and reporting endpoint fixed, recommendations recalculated for every user
✅ Calculator tests rebuilt from hand-verified reference cases, including clock-change days and every contract type
✅ Access tests against a local Supabase instance with negative cases for every table, plus Stripe test-mode payment tests
✅ Mutation testing on calculator and access layers - score from 31% to 84% - all wired into CI

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, AI writes the test code - humans decide what the tests must prove. ⚙️

His result: €1,900, seven business days. Coverage dipped to 81%, but the new tests caught four Cursor regressions in six months - and premium subscriptions grew 40% after Wouter published how calculations are verified. 🚀

👉 AI generated code production readiness: why AI-written tests pass when they shouldn't: https://launchstudio.eu/en/blog/ai-generated-code-production-readiness-why-ai-written-tests-pass-when-they-shouldnt

#Testing #MutationTesting #Cursor #EnergyTech #LaunchStudio #Manifera
