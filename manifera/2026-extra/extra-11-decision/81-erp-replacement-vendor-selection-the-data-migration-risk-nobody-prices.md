---
title: "ERP Replacement Vendor Selection: The Data Migration Risk Nobody Prices"
keywords: "ERP replacement vendor selection, ERP data migration risk, ERP implementation vendor due diligence, legacy ERP migration vendor, ERP vendor comparison"
buyer_stage: "Decision"
target_persona: "CTO"
---

# ERP Replacement Vendor Selection: The Data Migration Risk Nobody Prices

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ERP Replacement Vendor Selection: The Data Migration Risk Nobody Prices",
  "description": "A CTO's guide to evaluating ERP replacement vendors through the lens of data migration risk — mock cycles, reconciliation, and the cutover mechanics that determine whether go-live actually holds.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-01",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/erp-replacement-vendor-selection-the-data-migration-risk-nobody-prices"}
}
</script>

Ask an ERP implementation vendor for a fixed quote and the number will almost always undercount one line item: data migration. Gartner has pegged data migration at 15-30% of total ERP implementation cost when done properly, yet most SOWs bury it as a single "data conversion" bullet with a vague hourly estimate. The vendors who low-ball this line aren't being deceptive — they genuinely don't know your data's condition until they profile it, and profiling rarely happens before contract signature. That gap between "estimated at signing" and "discovered in mock 1" is where ERP projects go from 20% over budget to 80% over budget, and it's the single best predictor of whether a go-live date survives contact with reality.

If you're replacing SAP ECC, an aging Dynamics GP instance, or a heavily customized NetSuite tenant, the vendor conversation needs to start with data, not modules. The functional fit matters, but functional fit doesn't blow up timelines. Nineteen years of accumulated general ledger entries with inconsistent chart-of-accounts mappings do.

## Why Data Migration Is Structurally Under-Priced

Vendors price migration off a demo environment or a sample extract, not your production data. Three things routinely surface only after the contract is signed and the real extract lands: duplicate customer and vendor master records accumulated over a decade of manual entry, orphaned transactional records referencing deleted master data, and undocumented custom fields that hold business-critical logic (a "notes" field that's actually being parsed by a downstream report, for instance).

A vendor who quotes migration before running a data profiling pass against your actual production tables is quoting blind. The profiling pass — typically a week of read-only access plus automated scripts checking null rates, referential integrity, and duplicate-key clustering — should happen during due diligence, before the SOW is finalized, not as sprint one of the build phase. If a vendor resists profiling before contracting, that's the first red flag: they're either understaffed for it or planning to treat the discovery as a change order goldmine later.

## The Mock Cycle Discipline That Separates Real Migration Teams

Every credible ERP migration runs multiple mock cycles — commonly called Mock 1, Mock 2, Mock 3 — where the full extract-transform-load sequence executes against a copy of production data, loads into a test instance, and gets reconciled line by line against source. Mock 1 usually surfaces 60-70% of data quality issues: broken foreign keys, encoding mismatches, unit-of-measure conversion errors. Mock 2 should show a dramatic drop in exceptions if the team is actually fixing root causes rather than patching symptoms. Mock 3 is the rehearsal for cutover timing — how long does the full load actually take, and does it fit inside your production freeze window?

Ask any shortlisted vendor exactly how many mock cycles are in their plan and what the exit criteria are for each one. "We'll do testing" is not an answer. A specific answer sounds like: "Mock 1 validates transform logic against a 10% sample, Mock 2 runs the full volume with reconciliation reports comparing record counts and control totals by object type, Mock 3 is a dress rehearsal timed against the actual cutover window with the real infrastructure." Vendors who can't describe this in that level of detail haven't run enough migrations to know where they fail.

## Reconciliation Is the Only Proof That Matters

The migration isn't "done" because records loaded without error — it's done when reconciliation confirms nothing was silently dropped, duplicated, or mistranslated. That means control totals: sum of open AR balances in source must equal sum of open AR balances in target, general ledger trial balance must tie out to the cent, inventory quantity-on-hand by SKU must match a physical or cycle count snapshot taken at extraction time. Record-count matching alone is insufficient — you can lose a $2M invoice and gain a $2M duplicate and still have matching row counts.

Insist that reconciliation reports are a contractual deliverable, not an internal QA artifact the vendor keeps to themselves. You want to see the actual variance reports at each mock cycle, with sign-off from your finance and operations leads before cutover is scheduled. A vendor unwilling to share raw reconciliation output — as opposed to a summary slide saying "99.8% reconciled" — is asking you to trust a number you can't audit.

## Cutover Mechanics: Freeze Windows, Delta Loads, and Rollback

Full data migrations rarely load in one shot at cutover; the initial bulk load happens weeks earlier against a frozen extract, and a "delta load" captures everything that changed in source between extraction and go-live. The delta load window is where timing risk concentrates — if your business can't tolerate more than a 48-hour transaction freeze but the vendor's delta process needs 72 hours to extract, transform, validate, and load, you have a scheduling conflict that needs solving before cutover weekend, not during it.

Equally important: what's the rollback plan if cutover fails validation? A vendor with real migration experience will have a defined go/no-go checklist with objective pass criteria (reconciliation within tolerance, critical interfaces confirmed live, a defined number of open P1 defects) and a documented path back to the legacy system if criteria aren't met. Vendors who present cutover as "we go live and fix issues in hypercare" without a rollback contingency are betting your business operations on a single unrehearsed event.

## Tooling and Integration Debt Discovery

Beyond the core migration, legacy ERPs typically feed and are fed by a web of point-to-point integrations — EDI to distribution partners, a custom eCommerce connector, a homegrown reporting extract that finance has depended on for years without IT's knowledge. A migration vendor scoped only for the ERP conversion itself will treat these as "not in scope" until they break in week two of hypercare. During due diligence, ask the vendor to help you inventory every system with a live data feed to or from the legacy ERP, and confirm explicitly which of those integrations are in their migration scope versus which fall to your team or a separate [systems integration](https://www.manifera.com/services/custom-software-development/) engagement.

This is also where tooling choice matters. Purpose-built migration platforms (SAP Migration Cockpit, Syniti, or custom ETL pipelines built on standard tooling) each carry different tradeoffs in auditability, reusability for future migrations, and vendor lock-in. A vendor using a proprietary in-house tool that only they can operate leaves you dependent on them for every future data load — ask what happens to the migration pipeline and its documentation after go-live.

## Making the Vendor Call

The vendors worth shortlisting for an ERP replacement are the ones who ask to profile your real data before they'll commit to a migration number, who can describe their mock cycle methodology in specific, falsifiable detail, and who treat reconciliation reporting as something you see raw, not summarized. Cheap migration quotes are cheap because they're priced against clean demo data that doesn't resemble what's actually sitting in your production tables after a decade of manual entry and undocumented workarounds.

Manifera runs ERP replacement and legacy data migration projects with data profiling built into the due diligence phase, not billed as a change order after signature — see our approach to [custom software development](https://www.manifera.com/services/custom-software-development/) and how we structure [offshore delivery teams](https://www.manifera.com/services/offshore-software-development/) around this kind of high-stakes migration work. If you're evaluating vendors for an ERP replacement and want a second opinion on a migration plan before you sign, [get in touch](https://www.manifera.com/contact-us/).

## By The Numbers: What a Real Mock Cycle Report Should Show

A credible vendor's mock cycle reporting should follow a predictable trajectory, and you should ask to see it in numbers, not adjectives. Mock 1 against a full production-volume extract typically surfaces exceptions on 8-15% of records for a moderately messy legacy system (duplicate master records, broken foreign keys, encoding mismatches) — if a vendor reports under 2% on Mock 1, either your data is unusually clean or they ran it against a sanitized sample rather than the true extract, and you should ask which. Mock 2 should show exceptions dropping by 70-85% from Mock 1 if the team fixed root causes in the transform logic rather than manually patching individual bad records — a Mock 2 that only improves 20-30% signals symptom-patching that will resurface at cutover. Reconciliation tolerance for financial control totals (AR, AP, GL trial balance) should be zero variance, not "within 1%" — a 1% variance on a $50M AR ledger is $500,000 unaccounted for, which is not an acceptable migration outcome regardless of how it's framed in a summary slide. Load timing should be measured and reported in Mock 3 against the actual production freeze window, with a documented buffer of at least 20% — a delta load timed to exactly fit the freeze window with zero margin is a plan that fails the first time source data volume runs higher than the rehearsal.

## Frequently Asked Questions

### How much should ERP data migration realistically cost as a percentage of the total project budget?
Expect 15-30% of total implementation cost for a proper migration, depending on data quality and the number of legacy systems being consolidated. If a vendor's quote puts migration under 10% of the total, ask what's excluded — it's usually reconciliation depth or the number of mock cycles.

### How many mock migration cycles are actually necessary?
Three is the practical minimum for a mid-to-large ERP replacement: one to surface data quality issues, one to validate fixes at full volume, and one as a timed cutover rehearsal. Smaller, cleaner datasets can sometimes get away with two, but fewer than that means cutover weekend becomes your first real test.

### What's the difference between a bulk load and a delta load during cutover?
The bulk load moves the full historical dataset from a frozen extract taken weeks before go-live. The delta load captures every transaction that occurred in the source system between that extraction and the actual cutover moment, so the target system reflects a truly current state at go-live.

### Should we hire a separate data migration specialist instead of relying on the ERP implementation vendor?
For complex, multi-system consolidations or highly customized legacy environments, a specialist migration partner working alongside the ERP integrator often produces better reconciliation outcomes than expecting one vendor to be excellent at both configuration and migration. Ask your ERP vendor directly how much dedicated migration expertise is on the team versus generalist consultants.

### What should be in the rollback plan if cutover validation fails?
A documented go/no-go checklist with objective, pre-agreed pass criteria, a defined maximum number of open P1 defects, and a tested procedure for reverting to the legacy system without data loss for transactions that occurred during the cutover window. If the vendor can't produce this document before cutover weekend, that's a sign the plan doesn't exist yet.

### (Scenario: Mock 1 reconciliation report shows less than 2% exceptions on a system known to have years of manual data entry) What should a CTO suspect?
Suspect the vendor ran Mock 1 against a cleaned or sampled subset rather than the true full-volume production extract, since a genuinely messy legacy dataset rarely reconciles that cleanly on the first pass. Ask directly for the extraction methodology and row counts used, and compare them against your actual production table counts before accepting the result.

### (Scenario: finance lead refuses to sign off on cutover because a reconciliation variance report shows a small AP discrepancy) How should a CTO handle this disagreement with the migration vendor?
Back the finance lead — a documented, non-zero variance on control totals is exactly the kind of unresolved discrepancy a go/no-go checklist should block on, regardless of how small it looks in percentage terms. Require the vendor to trace the specific discrepancy to its source records before rescheduling cutover, rather than accepting a vendor's assurance that it's immaterial.

### (Scenario: legacy ERP has an undocumented custom field that a downstream finance report has silently depended on for years) How do we catch this before it breaks in migration?
This is precisely what the pre-contract data profiling pass is designed to surface — insist the vendor's profiling scope explicitly includes cross-referencing custom fields against known downstream reports and integrations, not just the core object tables. Interview finance, ops, and any team with a legacy reporting dependency directly during discovery, since institutional knowledge about undocumented field usage rarely lives in the ERP's own schema documentation.

### (Scenario: two vendors quote migration at similar total cost but very differently structured line items) How should a CTO compare the quotes meaningfully?
Compare the number of mock cycles, the depth of reconciliation reporting promised (raw variance reports versus summary percentages), and whether data profiling happens before or after contract signature — these structural differences predict overrun risk far better than the headline total. A lower quote with only two mock cycles and summary-only reconciliation is a higher-risk bet than a similarly priced quote with three mock cycles and contractual raw reporting access.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much should ERP data migration realistically cost as a percentage of the total project budget?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Expect 15-30% of total implementation cost for a proper migration, depending on data quality and the number of legacy systems being consolidated. If a vendor's quote puts migration under 10% of the total, ask what's excluded — it's usually reconciliation depth or the number of mock cycles."
      }
    },
    {
      "@type": "Question",
      "name": "How many mock migration cycles are actually necessary?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three is the practical minimum for a mid-to-large ERP replacement: one to surface data quality issues, one to validate fixes at full volume, and one as a timed cutover rehearsal. Smaller, cleaner datasets can sometimes get away with two, but fewer than that means cutover weekend becomes your first real test."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between a bulk load and a delta load during cutover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The bulk load moves the full historical dataset from a frozen extract taken weeks before go-live. The delta load captures every transaction that occurred in the source system between that extraction and the actual cutover moment, so the target system reflects a truly current state at go-live."
      }
    },
    {
      "@type": "Question",
      "name": "Should we hire a separate data migration specialist instead of relying on the ERP implementation vendor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For complex, multi-system consolidations or highly customized legacy environments, a specialist migration partner working alongside the ERP integrator often produces better reconciliation outcomes than expecting one vendor to be excellent at both configuration and migration. Ask your ERP vendor directly how much dedicated migration expertise is on the team versus generalist consultants."
      }
    },
    {
      "@type": "Question",
      "name": "What should be in the rollback plan if cutover validation fails?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A documented go/no-go checklist with objective, pre-agreed pass criteria, a defined maximum number of open P1 defects, and a tested procedure for reverting to the legacy system without data loss for transactions that occurred during the cutover window. If the vendor can't produce this document before cutover weekend, that's a sign the plan doesn't exist yet."
      }
    },
    {
      "@type": "Question",
      "name": "(Scenario: Mock 1 reconciliation report shows less than 2% exceptions on a system known to have years of manual data entry) What should a CTO suspect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Suspect the vendor ran Mock 1 against a cleaned or sampled subset rather than the true full-volume production extract. Ask directly for the extraction methodology and row counts used, and compare them against your actual production table counts before accepting the result."
      }
    },
    {
      "@type": "Question",
      "name": "(Scenario: finance lead refuses to sign off on cutover because a reconciliation variance report shows a small AP discrepancy) How should a CTO handle this disagreement with the migration vendor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Back the finance lead — a documented, non-zero variance on control totals should block cutover regardless of how small it looks in percentage terms. Require the vendor to trace the discrepancy to its source records rather than accepting an assurance that it's immaterial."
      }
    },
    {
      "@type": "Question",
      "name": "(Scenario: legacy ERP has an undocumented custom field that a downstream finance report has silently depended on for years) How do we catch this before it breaks in migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "This is what the pre-contract data profiling pass is designed to surface — insist the scope explicitly includes cross-referencing custom fields against known downstream reports and integrations. Interview finance, ops, and any team with a legacy reporting dependency directly during discovery."
      }
    },
    {
      "@type": "Question",
      "name": "(Scenario: two vendors quote migration at similar total cost but very differently structured line items) How should a CTO compare the quotes meaningfully?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Compare the number of mock cycles, the depth of reconciliation reporting promised, and whether data profiling happens before or after contract signature — these structural differences predict overrun risk better than the headline total."
      }
    }
  ]
}
</script>
