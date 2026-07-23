🚨 Roos Dijkman didn't find out her maintenance app had a hole in it from a bug report. She found out from a tenant who'd waited three weeks for a leaking tap to get fixed — and finally called her directly, furious, after PandBeheer told them the request was "submitted." 😳

A silently unrouted request is worse than a crash, because it looks successful. The tenant sees a confirmation. The dashboard shows the request exists. Nobody has any signal it's stuck. 🧠

❌ Lovable built the obvious flow — tenant submits, request routes to the assigned contractor — which only works if every property actually has one
❌ Roos's property had recently lost its contractor after a falling-out, with a replacement planned "soon"
❌ When a request came in for that property, it saved to the database correctly — but with nobody to route the notification to, nothing fired
❌ No alert to the landlord, no escalation — just a fully valid record sitting invisible for three weeks

✅ Add a fallback routing rule: any request for a property without an assigned contractor routes directly to the landlord's inbox and dashboard as a flagged priority item
✅ Replace the generic "submitted" status with a visible "unassigned — needs contractor" state
✅ Add a daily digest that surfaces any request untouched for more than 48 hours, regardless of routing status

At **LaunchStudio**, this is precisely the kind of gap we look for before an app goes live with real tenants — not "does the happy path work," but what happens to every record that falls outside it. Backed by 160+ delivered projects. 🛡️

Her result: Roos caught two more unassigned-property requests the following month before they became complaints, both resolved within a day. 🚀

👉 Managing real tenants on an AI-built tool? See what a routing and notification audit involves: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #PropTech #AILandlordTools
