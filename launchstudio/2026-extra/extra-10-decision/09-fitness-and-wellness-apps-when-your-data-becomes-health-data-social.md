🚨 Marijke's running app had a "how did you feel" field. Months later it was full of entries like "back to running after my ACL surgery" — visible in full to any running-club captain in the group. 😳

Wellness apps accumulate health data one honest note at a time, without anyone deciding to build a health product: 🧠

❌ The feeling-log field was stored in the same table as route distances and pace times, no distinction at all
❌ Every entry was visible by default to the whole running-club group's shared training log
❌ No consent screen ever explained what the field was actually used for
❌ Wearable-sourced heart rate and sleep data sat in a less protected table just because it arrived via API instead of a form

✅ Reclassify the feeling-log field as special category data in its own access-controlled table
✅ Exclude it from the group social feed by default, with an explicit per-entry opt-in to share
✅ Add a specific consent screen the first time a user types into a health-adjacent field
✅ Treat wearable API data with the same Article 9 rigor as anything typed directly into the app

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we secure the "why" behind the behavior data, not just the steps and the pace times. 🏃

Her result: Looproute kept the feature that made it useful for training feedback, removed the accidental broadcast of injury notes to entire groups, and saw feeling-log usage increase once it was private by default. 🚀

👉 Audit which of your fields are quietly health data: https://launchstudio.eu/en/blog/fitness-and-wellness-apps-when-your-data-becomes-health-data

#WellnessApp #GDPR #FitnessTech #StartupFounders #LaunchStudio #Manifera
