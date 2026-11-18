🗂️ An auditor asks for a register of processing. You don't have one. You sit down to write it. Here's what turns up in one morning.

EXHIBIT A: a "notes" field
Meant for parking instructions. In a substantial share of records, practitioners had written clinical information, because it was convenient. That makes it health data, a special category, with stricter rules than anything else in the product.

EXHIBIT B: error tracking
It captured full request bodies: patient names, appointment reasons, and those same notes. Sent to a service outside the EU, with no data processing agreement and no scrubbing.

EXHIBIT C: a forgotten trial
An analytics service, tried for two weeks, eleven months earlier. Still receiving page events every day, with patient identifiers in the URLs. Nothing in the product referenced it, and nobody had thought about it since.

Jorinde Talsma built Kliniekplanner in Lovable: appointment scheduling and patient communication for physiotherapy and podiatry clinics, 37 clinics, around 22,000 patients. One clinic's auditor asked for the register. 🩺

Case closed (LaunchStudio, 4 business days, €2,900):
✓ A register built from the schema, covering nine processing activities
✓ The notes field treated as potentially clinical: access restricted, a warning shown to practitioners, special category handling applied
✓ Error tracking moved to an EU-hosted provider, scrubbing request bodies entirely
✓ The abandoned analytics service removed and its retained data deleted on request
✓ Patient identifiers taken out of URLs
✓ Retention per activity (appointments per clinic instruction, communication logs 24 months, technical logs 30 days), enforced by a scheduled job, not just written down
✓ Two unused fields removed from the patient record
✓ The register committed to the repository, then reused as the processing annex and to rewrite the privacy policy

The auditor's questions were answered from the register. Jorinde names Exhibit C as the finding that justified the whole exercise.

"I expected to spend a morning writing a document. I spent a morning finding out that a tool I stopped using last year had been collecting patient data every day since." - Jorinde Talsma

https://launchstudio.eu/en/blog/records-of-processing-the-register-nobody-builds-until-asked

#GDPR #Privacy #HealthTech #Lovable #LaunchStudio #Manifera
