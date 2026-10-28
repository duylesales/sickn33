🚨 Koen Vermeulen's Ledenadmin runs membership administration for five sports clubs around Helmond - about 4,000 members with addresses, dates of birth, bank details and sometimes medical notes. Row level security was enabled. The policy let any logged-in user read the whole table. 😳

Every member could read every other member's bank details, across all five clubs. Here's why "RLS enabled" is not the same as protected: 🧠

❌ A policy written during development to make an empty list go away - returning everything
❌ The role column stored in a profile users can edit themselves
❌ Sensitive data like bank details in the same table as everything else
❌ Forgotten tables, such as an old import copy, still readable with the public key

✅ An organisation and membership model: each club a tenant, with real roles
✅ Policies per table and per operation, with identity taken from the session
✅ Bank details in a separate table readable only by club administrators
✅ Test by attacking: several accounts, an unauthenticated client, and a direct enumeration of every table

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we write Supabase policies that hold when someone actually tries. 🛡️

His result: nine business days and €4,600 later, the attack test also found two forgotten readable tables, both removed. The five clubs signed a joint data processing agreement that had been stalled - and Koen now has a document for every board that asks who can see what. 🚀

👉 Row level security policies that actually hold: https://launchstudio.eu/en/blog/supabase-security-row-level-security-policies-that-hold

#Supabase #RowLevelSecurity #Lovable #AVG #LaunchStudio #Manifera
