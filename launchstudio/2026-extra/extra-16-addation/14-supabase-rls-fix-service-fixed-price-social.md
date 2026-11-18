Q: "How do you make sure other clients cannot see my documents?" 📂

That's what a new client, who works in IT, asked Joyce Vermeulen during onboarding. Joyce runs a small bookkeeping office in Hoorn and built Klantmap with Lovable and Supabase: around 180 clients upload receipts and bank statements, and her team prepares their quarterly VAT returns.

Joyce realised she didn't know.

A, BEFORE (from an exposure test):
• The documents table let any logged-in user read every row, so a client could list every other client's document names and metadata through the API
• The upload bucket was public, with file paths based on client names
• Users could update their own role column in profiles
• A function that generated quarterly overviews ran as security definer, without checking who called it

Q: So what's the access model?
A: Agreed with Joyce first: clients see only their own documents and messages, staff see the clients assigned to them, and Joyce as owner sees everything.

Q: And how is it enforced?
A, AFTER (LaunchStudio, 5 business days, €1,850):
✓ Policies rewritten for all eleven tables, with separate rules per operation
✓ Roles moved into a protected table
✓ An explicit permission check in the overview function
✓ A private bucket, with policies per client folder and signed URLs
✓ Negative authorisation tests for every role
✓ Frontend queries that relied on broad access adjusted
✓ Project instructions documenting the patterns for future Lovable sessions

The portal's interface didn't change at all. Joyce sent her IT-minded client a one-page description of the access rules, and later used the same document to answer a larger client's security questionnaire.

"I could finally answer the question every client should be asking. And I could prove the answer with tests." - Joyce Vermeulen

https://launchstudio.eu/en/blog/supabase-rls-fix-service-fixed-price

#Supabase #RLS #Lovable #Security #AIFounder #LaunchStudio #Manifera
