🛠️ THE BUILD-OR-BUY LEDGER of one very fast founder

Lucas Timmermans built Projectkas with Cursor: budgeting and invoicing for event production companies. Proud of his speed, he built everything himself.

BUILT: Authentication, with custom password hashing
WHAT BROKE: A reset flaw let password reset links be reused
NOW BOUGHT: Supabase Auth, with a password reset campaign

BUILT: Billing that stored card tokens and ran its own renewal logic
WHAT BROKE: After a server restart, several customers were charged twice
NOW BOUGHT: Stripe Billing, with Checkout and the Customer Portal, and the double charges refunded

BUILT: An SMTP sender on a cheap server
WHAT BROKE: Emails stopped reaching Outlook users
NOW BOUGHT: A transactional email provider, with an authenticated domain

BUILT: A homemade analytics dashboard
NOW BOUGHT: A privacy-friendly analytics service

STILL BUILT, AND KEPT: the budgeting and invoicing logic. The actual product.

All three breakages happened within two months. Lucas was spending more time keeping infrastructure alive than building the budgeting features customers wanted.

The migration took LaunchStudio 16 business days, for €6,300, including testing.

Since then, infrastructure incidents have stopped. And within the next month, Lucas shipped the multi-currency budgeting feature his customers had been asking for.

"I could build all of it. That was exactly the problem: I was maintaining all of it, too." - Lucas Timmermans

https://launchstudio.eu/en/blog/build-vs-buy-for-saas-features-auth-billing-email

#SaaS #BuildVsBuy #Stripe #Supabase #LaunchStudio #Manifera
