🔐 Joyce Vermeulen runs a bookkeeping office in Hoorn and built Klantmap with Lovable and Supabase: about 180 clients upload receipts and bank statements, and her team prepares their VAT returns. During onboarding, a new client who worked in IT asked: "How do you make sure other clients can't see my documents?" Joyce realised she didn't know. 😶

An exposure test through the API answered the question within minutes. Every client was one query away from every other client's files: 🧠

❌ A policy letting any logged-in user list all documents
❌ A public storage bucket with file paths based on client names
❌ Users who could edit their own role column and promote themselves
❌ A security definer function that never checked who was calling

✅ An agreed access model: clients, assigned staff, owner
✅ Policies rewritten for all eleven tables, separately per operation
✅ A private bucket with per-client folders and signed URLs
✅ Negative authorisation tests per role and project instructions for Lovable

At **LaunchStudio**, backed by Manifera's 11+ years of securing enterprise systems, we test Row Level Security the way an attacker would and fix it at a fixed price, without touching your interface. 🛠️

Her result: €1,850, five business days. The portal looks the same, and Joyce now answers security questionnaires with a one-page document and tests to back it up. 🚀

👉 Supabase RLS fix service, at a fixed price: https://launchstudio.eu/en/blog/supabase-rls-fix-service-fixed-price

#Supabase #RLS #Lovable #Security #AIFounder #LaunchStudio #Manifera
