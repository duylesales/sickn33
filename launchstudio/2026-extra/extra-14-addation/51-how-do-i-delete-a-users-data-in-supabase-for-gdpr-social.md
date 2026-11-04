🚨 Sander Wijnberg organises speed dating events in Groningen and built Klikavond in Lovable. After an event, a participant sent a formal GDPR deletion request. Sander deleted her account in the Supabase dashboard and thought he was done. Two weeks later she emailed again: she was still getting newsletters, and another participant said her photo still appeared in his match history. 😳

He pressed delete. Her data was still in six places. Here's what the dashboard button didn't touch: 🧠

❌ Her photos, still sitting in Supabase Storage
❌ Match records that kept her name and photo URL
❌ Her email address, still in the newsletter tool
❌ No record of the request, the checks or the completion

✅ Personal data mapped across eleven tables and two processors
✅ One deletion function that removes profiles and photos, and anonymises match records for the other participant
✅ Contacts removed from the newsletter provider, with only the payment records bookkeeping requires kept
✅ Self-service account deletion and data export, plus a documented confirmation for the participant

At **LaunchStudio**, backed by Manifera's 11+ years of data protection work for Dutch clients from Herengracht 420 in Amsterdam, deletion, export and retention are designed in - not bolted on after a complaint. 🛠️

💡 His result: €1,650, five business days. Deletion requests now complete automatically within minutes, and the documentation answered a venue partner's privacy questions straight away. 🚀

👉 Does "delete user" in Supabase really delete everything? Here's how to handle a GDPR erasure request properly: https://launchstudio.eu/en/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr

#GDPR #AVG #Supabase #Privacy #LaunchStudio #Manifera
