🚨 A free-text "session_notes" column, added as a placeholder for a feature that never shipped. A few early users started typing real clinical notes into it anyway. 😳

Data you never stored can't leak, can't be subpoenaed, and doesn't need a deletion process built for it: 🧠

❌ A special-category health field with no encryption, visible to every debug query
❌ Password reset requests logging the full request body into a third-party tracker
❌ A phone number field nobody's used since a "maybe we'll add SMS" idea
❌ Raw card numbers or ID documents stored directly instead of tokenized at the processor

✅ Ask "does a real feature break without this field" for every schema column
✅ Tokenize payment data at the processor — never let raw card numbers touch your database
✅ Configure field-level redaction in your logging tool before sensitive data reaches it
✅ Strip personal identifiers before an AI API call, reinsert them after the response

At **LaunchStudio**, backed by Manifera's 11+ years of production security work, we audit exactly this kind of unnecessary exposure before it becomes a liability. 🔒

His result: the field either removed or properly encrypted, and a schema he could describe field by field in review. 🚀

👉 Send us your prototype link for free feedback on what your schema is storing: https://launchstudio.eu/en/blog/sensitive-data-deciding-what-not-to-store

#IndieHacker #DataMinimisation #LaunchStudio #Manifera #GDPR #AICoding
