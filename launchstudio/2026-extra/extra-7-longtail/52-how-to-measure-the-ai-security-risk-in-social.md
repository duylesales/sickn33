🚨 Niamh O'Sullivan, a former junior developer, built CoachTrail — a coaching platform — with Cursor. She read every line of the generated code herself: clean structure, sensible naming, nothing alarming. Then she found a live Stripe secret key sitting in plain text in a public JavaScript file, by accident, while debugging something else entirely. 😬

Being able to read the code and having measured its security risk are two very different claims. 🧠

❌ The Stripe secret key had been placed directly into a frontend config file instead of a server-side environment variable
❌ It looked completely ordinary in the code — just a constant being imported like any other
❌ A manual read-through by a technical founder caught the "wrong code" patterns and missed the "missing protection" pattern entirely
❌ Anyone opening the browser's network tab or page source could have found a live payment-processing credential

✅ Rotate the exposed key immediately once found
✅ Move all payment-related secrets to a server-side proxy layer, out of anything shipped to the browser
✅ Run a full pass across the rest of the codebase checking every other integration for the same exposure pattern

At **LaunchStudio**, we treat "I can read the code" and "the code has been audited" as two separate questions — because AI-generated code reads like something a competent developer wrote, and that familiarity is exactly what makes real risk easy to miss. 🛡️

Niamh's result: exposed key rotated, secrets moved server-side, and a clean pass across every other integration — completed in 6 business days. 🚀

👉 Technical enough to read your AI-generated code? That's not the same as having measured its risk: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AISecurity #SecretsManagement
