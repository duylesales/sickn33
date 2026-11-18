🍲 RECIPE: An 11-second recipe page

Lisanne de Groot built Kookschrift with Lovable and Supabase, where home cooks share recipes, save favourites and plan weekly menus. Instagram brought around 15,000 users. Then reviews mentioned slowness, and most mobile visitors left before the recipe page loaded: up to eleven seconds on 4G.

Here's how that dish was made.

INGREDIENTS
• Phone photos served at full size, around 6 MB each, even in thumbnail grids
• Three chart libraries and a rich text editor in the bundle of every page, though only two pages used them
• A recipe list that fetched every recipe with every column, long instructions included, then filtered in the browser
• Separate requests per recipe card for the author, the like count and the saved status
• No index on user_id for favourites

METHOD
Combine everything. Serve on a 4G connection. Wait.

THE NEW RECIPE (LaunchStudio, 7 business days, €2,600)
1. Resize photos on upload into thumbnail, medium and large variants, convert existing photos, and serve them through a CDN with lazy loading
2. Load heavy libraries only on the pages that use them, and replace two chart libraries with one
3. Serve the list from a database view with only card fields, author names, like counts and saved status in one query, with pagination
4. Add indexes for favourites, likes and recipe filters
5. Move search to a full-text index

READY IN
Recipe page: around 1.5 seconds on 4G. List page: under a second.

SERVES
More people, for longer. Mobile bounce rate dropped noticeably, sessions grew longer, and app store ratings recovered within two months.

"I thought my users needed better recipes. They actually needed pages that loaded before they lost interest." - Lisanne de Groot

Why is your AI-built app slow? https://launchstudio.eu/en/blog/why-is-my-ai-built-app-slow

#Performance #WebVitals #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
