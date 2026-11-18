💬 A conversation with GrensFlow's API, before the fix (dramatized)

CUSTOMER: Show me shipment 1042.
API: Are you logged in?
CUSTOMER: Yes.
API: Here you go.
CUSTOMER: Now show me shipment 1043.
API: Are you logged in?
CUSTOMER: Still yes.
API: Here you go.
CUSTOMER: ...That one isn't mine.
API: I never asked.

Ruben Alting built GrensFlow in Cursor: a SaaS tool for small businesses in Winschoten and the border region to manage customs paperwork and shipment tracking for trade with Germany. He iterated fast, adding every feature his first customers requested.

By his fourth signed customer, a support ticket revealed the problem: one customer could see another customer's shipment records just by changing a number in the URL. The AI-generated route checked one thing, whether you were logged in. It never checked the second: whether the shipment was yours.

The same conversation, after LaunchStudio (7 business days, €1,450):

CUSTOMER: Show me shipment 1043.
API: Logged in? Yes. Belongs to your account? No. Request denied.

What changed under the hood:
• Authorization rebuilt across every API endpoint
• Tenant-scoped database queries
• Automated tests that catch this class of bug on every future deployment

"I was adding features every week and never once thought to check if customers could see each other's data. LaunchStudio found it before it became a real problem." - Ruben Alting

Does your API ask the second question? https://launchstudio.eu/en/blog/ai-in-saas-winschoten

#AINativeFounder #LaunchStudio #Manifera #SaaSFoundation #Winschoten
