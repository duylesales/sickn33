📦 Picture a perfect conveyor belt. Smooth, fast, monitored, with a quality check at every station.

Now picture it delivering boxes with the lids off.

That's what Martijn Koster had two weeks before launch.

He runs Cateringklok from Den Bosch, built with Bolt and Supabase: event caterers manage menus, quotes and staff schedules. Ahead of a launch with a national catering association, he hired a DevOps contractor for a week, and the contractor did excellent work:
✓ A GitHub pipeline with tests and previews
✓ Separate Supabase projects for staging and production
✓ Uptime monitoring
✓ Structured logs

The belt was perfect. Then a pilot caterer filtered the quote list a certain way, and saw quotes from another company.

LaunchStudio's review looked inside the boxes:
✗ Quotes and menus tables with policies letting any logged-in user read every row
✗ Staff phone numbers exposed through a view without policies
✗ Mollie deposits marked as paid on the redirect page
✗ Quote PDFs in a public bucket

The infrastructure was solid. The application had simply never been reviewed.

Putting the lids on (LaunchStudio, 6 business days, €2,400):
✓ Policies rewritten per caterer and role, with tests running in the contractor's pipeline
✓ The view secured
✓ Deposits confirmed by verified webhooks, with reconciliation
✓ PDFs moved to private storage
✓ Email authentication, which the infrastructure scope hadn't covered

The association launched on schedule with around 60 caterers. And the contractor's pipeline now runs LaunchStudio's access tests on every change: both pieces of work, on one belt.

"I hired the right person for the wrong problem. The pipeline was perfect, it just delivered an app where everyone could see everyone's quotes." - Martijn Koster

https://launchstudio.eu/en/blog/production-launch-partner-vs-devops-contractor

#DevOps #Security #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
