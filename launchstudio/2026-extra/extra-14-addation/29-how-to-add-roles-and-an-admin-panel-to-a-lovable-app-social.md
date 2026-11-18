The admin page was hidden.
Not locked.
Hidden.

The role was a column on your own profile.
The profile page saved the whole row.
So you could edit the row.
And become a coordinator.

And a coordinator could see
residents' addresses
and the medical notes
on sensitive requests. 🏘️

Roos van Dam coordinates a neighbourhood help network in Zaandam. She built Buurthulp in Lovable: residents post requests, like groceries or a lift to the doctor, volunteers accept them, and coordinators manage volunteers and check sensitive requests. About 140 volunteers and 300 residents joined.

One volunteer discovered it without meaning to, through the browser's developer tools. The admin page only checked the role inside the React component.

LaunchStudio. 6 business days. €1,750.
A user_roles table with no write policies.
Existing coordinators migrated into it.
The role column removed from profiles.
A has_role helper.
RLS rewritten, so medical notes and addresses are visible only to coordinators and the assigned volunteer.
Approving volunteers and assigning coordinators moved into edge functions.
An audit log.

Closed within four business days.
The network's board informed.
The incident documented.
The audit log reviewed every month.
Around 2,000 requests handled since.

"The admin page was hidden. That's all it was: hidden. Anyone who knew how to look could promote themselves." - Roos van Dam

https://launchstudio.eu/en/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app

#Lovable #Supabase #AccessControl #Community #LaunchStudio #Manifera
