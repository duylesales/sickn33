```
$ npm test
  412 passing (4m)
  Coverage: 91%
  ✓ All tests passed
```

Meanwhile, in production: a direct debit run charged 140 members twice. 💸

Jeroen Wijnstra built Contributiebeheer in Cursor: membership fee administration for 63 associations and clubs, collecting around €2 million a year in direct debits. He'd asked the assistant to write a test suite and accepted what it gave him.

Then a change to fix an unrelated rounding issue touched the pro-rata discount for mid-year joiners. The discount began applying to the full annual amount, not the remaining months, and recent joiners got a second charge.

Eleven tests covered that function. All eleven passed. They had been generated from the implementation, asserted whatever the code produced at the time, and were updated automatically when the code changed. The bug became the expected result.

```
$ npm test   # after the review
  94 passing (50s)
```

How 412 became 94 (LaunchStudio, 3 business days, €3,300):
✓ 280 tests deleted for asserting nothing that could fail: renders without crashing, returns a value, mock was called
✓ The other 132 checked for assertions derived from the code, not the intent, with 40 rewritten against business rules taken from the association agreements
✓ An authorisation test per endpoint across all 31, which found three endpoints with no check at all
✓ Money tests written from the rules, using awkward amounts: mid-year joining, leaving, rounding, zero, and the maximum contribution
✓ An end-to-end test of the collection run
✓ A test for the double charge, written before the fix and confirmed failing first
✓ The suite wired into deployment

The 140 duplicate charges were refunded and the associations informed. Jeroen's verdict on the old suite: it was actively harmful, because it gave him enough confidence to deploy a contribution calculation change on a Friday without checking it by hand.

"Four hundred and twelve tests, ninety-one percent coverage, all green, and they were green because they had been written from the code rather than from what the code was supposed to do." - Jeroen Wijnstra

https://launchstudio.eu/en/blog/cursor-and-tests-generating-a-suite-you-can-trust

#Testing #Cursor #AICoding #SoftwareQuality #LaunchStudio #Manifera
