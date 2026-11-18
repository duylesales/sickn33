🪣 Five holes in the margin bucket

Sjoerd Brinkman, a former carpenter, runs a renovation company in Apeldoorn with 18 employees. He built Begrotingsmaker with Lovable and Supabase: estimators pick a job template, adjust quantities and generate a branded PDF quote. Quote prep time halved, and two other renovation companies wanted the tool. Then his accountant noticed that recent projects earned less than quoted.

HOLE 1: Only sales prices per line were stored. When material prices rose, nobody saw margins shrink.
HOLE 2: Material prices were typed in by hand and rarely updated.
HOLE 3: Extra work agreed on site went on paper or into WhatsApp, and often never got invoiced.
HOLE 4: Clients accepted quotes by email reply, so nobody knew which version they had accepted.
HOLE 5: The browser-generated PDF sometimes rounded totals differently from the invoice.

The repairs (LaunchStudio, 17 business days, €6,800):
🔧 A calculation model with components, costs, labour norms and markups per section, calculated on the server with exact decimals, showing cost and margin per line
🔧 Price lists from two wholesalers imported with price dates, and alerts on open quotes when material prices change
🔧 On-site extra work registered by project managers with photos and quantities, sent to clients for approval, and flowing into progress and final invoices
🔧 Quote versions tracked, with clients accepting a specific version through an authenticated link that records name, time and document
🔧 One server-side calculation, VAT per work type as advised by the accountant, and internal costs hidden from clients and subcontractors with Row Level Security

Six months later: invoiced extra work up substantially compared with the previous period, and margin gaps between quote and result narrowing. Both other companies onboarded, and Sjoerd now uses real project data to refine labour norms.

"We were good at building and bad at writing down what we built. The tool now remembers every extra hour so I don't have to." - Sjoerd Brinkman

https://launchstudio.eu/en/blog/quoting-tool-for-construction-companies-built-with-ai

#ConstructionTech #Quoting #Renovation #Margins #AIFounder #LaunchStudio #Manifera
