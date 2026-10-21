🚨 Jeroen Wijnstra's Contributiebeheer collects around €2 million a year in membership fees for 63 associations and clubs. He had Cursor write his test suite: 412 tests, 91% coverage, all green. Then a direct debit run charged 140 members twice. 😳

The function behind it had eleven tests. All eleven passed — because they'd been generated from the code, and updated when the code changed, encoding the bug as the expected result. Here's how to build a test suite you can actually trust: 🧠

❌ Tests that assert nothing that could fail: "renders", "returns a value", "mock was called"
❌ Assertions derived from the implementation rather than the business rule
❌ Coverage treated as the goal instead of verified behaviour
❌ A four-minute suite that gave enough confidence to deploy a fee change on a Friday

✅ 280 decorative tests deleted; 40 rewritten against the associations' actual rules
✅ An authorisation test per endpoint — which found three of 31 with no check at all
✅ Money tests for mid-year joining, leaving, rounding, zero and the maximum, with awkward amounts
✅ A failing regression test written before the fix; 94 tests in 50 seconds, wired into deployment

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the proportionate suite that makes deploying stop being nerve-racking. ⚙️

His result: €3,300, three business days. The 140 duplicate charges were refunded, and the suite now catches what the 412 tests let through. 🚀

👉 Cursor and tests: generating a suite you can trust: https://launchstudio.eu/en/blog/cursor-and-tests-generating-a-suite-you-can-trust

#Testing #Cursor #AICoding #SoftwareQuality #LaunchStudio #Manifera
