🏥 Marloes ten Cate, a former hospital administrator in Hengelo, built Zorgrooster — a scheduling tool for home care nurses tracking patient visits, care notes, and medication schedules — using Lovable. It worked well for her pilot of four nurses. Then LaunchStudio's review found the Supabase backend had zero row-level security: any logged-in nurse could query the entire patient database, including medication records for patients that weren't theirs. 😳

That's not just a bug — with health data, that's a GDPR violation waiting to happen. 🧠

❌ Any nurse account could read every patient's care notes and medication history
❌ No encryption at rest on sensitive medication and care-note fields
❌ No audit log — no record of who accessed what, or when
❌ Roughly 45% of AI-generated code ships with at least one exploitable security gap like this

✅ Implemented granular RLS policies scoping each nurse to only her assigned patients
✅ Added encryption at rest for medication and care note fields
✅ Built an audit log tracking every record access for GDPR compliance

At **LaunchStudio**, Manifera's 120+ engineers run this exact data security audit — the same rigor applied to enterprise clients like Vodafone and TNO. 🛡️

Zorgrooster passed its regional care organization's data protection review on the first submission, and now schedules over sixty nurses across Hengelo and Twente. 🚀

👉 Handling patient data in Hengelo? Check your RLS policies before your next pilot: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #Hengelo #GDPR
