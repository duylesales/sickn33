📸 Sophie van Rijn, a photography teacher in Middelburg, built Fotoschool Zeeland Online with Lovable and Supabase to sell video courses on landscape and portrait photography. Her first big launch went to about 6,000 subscribers at 20:00. Within minutes the sales page slowed, checkout failed for many visitors and buyers who did pay got no access. Meanwhile, links to her videos were circulating on a photography forum. 😱

The assessment found: 🧠

❌ A sales page loading all course data and full-size images for every visitor
❌ A custom checkout calling the payment API from the client, with access granted on the success page
❌ Course videos stored as public files
❌ Dutch VAT for every EU buyer, no consent step for immediate access and refunds that never removed access

✅ A static, cached sales page with optimised images
✅ Stripe's hosted checkout with access granted by verified, idempotent webhooks
✅ Signed video playback and expiring, watermarked workbook downloads
✅ VAT per customer country, approved by her accountant, a recorded consent step, automatic access removal on refunds and a load test of 2,000 visitors in five minutes

At **LaunchStudio**, backed by Manifera's 11+ years of building platforms with payments, content and traffic peaks, we make sure launch day sells instead of crashes. 🛠️

Her result: €3,000, seven business days. The next launch sold more than twice as many courses, without a single checkout failure. 🚀

👉 Production launch for creator and course platforms: https://launchstudio.eu/en/blog/production-launch-for-creator-and-course-platforms

#OnlineCourses #CreatorEconomy #Lovable #Stripe #AIFounder #LaunchStudio #Manifera
