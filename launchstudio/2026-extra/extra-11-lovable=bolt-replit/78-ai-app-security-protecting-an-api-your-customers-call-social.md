🚨 Tim Roozendaal's Bezorgtijd shows delivery slots at checkout for 34 Dutch webshops around Tilburg and Breda. Endpoints checked the key, then trusted the IDs in the request. A developer typed an order number from a paper note into a test call — and received another retailer's order, with a competitor's name in the address. 😳

Here's what protecting an API your customers call actually means: 🧠

❌ Checking the key but not whether that key may see this specific object
❌ Internal endpoints that became public the day the API was published
❌ Update endpoints that let a caller change which customer owns an order
❌ No rate limits, no pagination, and error messages quoting column names

✅ Authorisation per object on every endpoint, not just per key
✅ Accept only a defined list of fields on updates
✅ Rate limits per key, enforced pagination, and generic outward errors
✅ Versioning, documentation with key-safety guidance, and testing from a second account

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we test your API like someone trying to get in. 🧪

His result: eight business days and €4,400 later, all 23 endpoints check per-object access — including seven internal ones, one of which listed every slot for every retailer. Two webshops calling the API from browser JavaScript had their keys rotated. The reporting developer's employer expanded to three sister companies. 🚀

👉 Protecting an API your customers call: https://launchstudio.eu/en/blog/ai-app-security-protecting-an-api-your-customers-call

#APISecurity #Ecommerce #Lovable #B2B #LaunchStudio #Manifera
