🚨 Ruben Aerts installed Hotjar on Bloomcart to figure out why 30% of customers abandoned the delivery-address form. It was live within an hour, defaults untouched. 😳

Session replay feels harmless until you check what it's actually recording. Here's the gap that took six weeks to notice: 🧠

❌ The "gift message" field was recorded in full, unmasked, capturing personal notes to recipients
❌ A "special delivery instructions" field had customers typing building access codes, also unmasked
❌ Masking isn't the default in most session-replay tools — the tool has no idea which of your fields are sensitive
❌ A generic "we use cookies" banner isn't specific enough consent for full session replay under GDPR

✅ Mask by exception: block everything, then deliberately unmask only what you're actively investigating
✅ Name session recording explicitly in your consent banner, not folded into a general analytics toggle
✅ Set retention to 30-90 days — long enough to be useful, short enough to limit exposure
✅ Limit dashboard access to whoever is actually doing support or UX work, not the whole team

At **LaunchStudio**, backed by Manifera's 11+ years of engineering experience, we review exactly this kind of masking and consent configuration before a tool like Hotjar goes live on a real product. 🔒

His result: the six weeks of unmasked recordings were deleted, the original postcode-lookup bug was found within two weeks of the fix, and the whole privacy review was completed in 1 business day. 🚀

👉 Check what your session replay tool is actually capturing: [Link to article]

#SessionReplay #GDPRCompliance #DataPrivacy #SaaSPrivacy #LaunchStudio #Manifera
