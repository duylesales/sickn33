🚨 A user with a flagged nut allergy tapped MaaltijdPlan's "swap this recipe" button one evening. The app suggested a dish containing almonds — the exact allergen on her profile. She caught it before cooking. She never trusted the app again, and told Iris Bosch exactly why she was cancelling. 😳

An allergen filter that works on the main screen and nothing else isn't a safety feature — it's a false sense of one. 🧠

❌ The main weekly meal plan correctly filtered allergens — but the "swap" feature queried the recipe database directly, with the allergen filter never wired in
❌ Each AI-assisted extra (swap, regenerate, grocery export) was built as its own feature request, without the original filtering logic carried over
❌ Everything "worked" in testing because Iris tested the feature she'd just built, not its interaction with every other constraint already on file
❌ Industry research puts the share of AI-generated code with security or correctness gaps at around 45% — constraint-handling gaps like this are a real chunk of that number

✅ Centralize allergen filtering into a single shared function every recipe-serving feature must call before returning results
✅ Deliberately test every AI-suggestion, regenerate, and export flow against a fake allergen — not just the main screen
✅ Add an automated test that fails the build if any new recipe-serving path skips the allergen check

At **LaunchStudio**, our audits for consumer food and health apps specifically test cross-feature constraint enforcement, not just the feature it was originally built for. Backed by Manifera's 11+ years of production engineering. 🛡️

Iris's result: MaaltijdPlan now enforces allergen rules at one shared layer instead of per-feature, closing the gap for good. 🚀

👉 Building a food, health, or safety-critical app with AI? Get a free cross-feature check: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #FoodTech #AISecure
