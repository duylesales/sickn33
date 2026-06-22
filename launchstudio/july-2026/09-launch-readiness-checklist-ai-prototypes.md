---
Title: The 20-Point Launch Readiness Checklist for AI Prototypes
Keywords: Point, Launch, Readiness, Checklist, Prototypes
Buyer Stage: Decision
---

# The 20-Point Launch Readiness Checklist for AI Prototypes

Before launching your AI-built prototype to real users, verify these 20 critical items across security, payments, deployment, performance, and legal compliance. Approximately 95% of AI-generated applications fail at least 10 of these checks. Each failed item represents a risk to your users, your revenue, or your reputation. This checklist helps you identify and fix the gaps before they become problems.

This checklist is based on our experience reviewing hundreds of AI-built prototypes at LaunchStudio. We have identified the 20 items that most frequently cause problems after launch — ranked by severity and grouped by category. Use it as your pre-launch audit before accepting your first real user.

## Security (Items 1–5) — Mandatory

All five security items must pass before launch. Skipping any of these creates immediate risk to your users and potential legal liability for you.

### 1. Authentication Uses a Proven Provider

**Check**: Your app uses Supabase Auth, Firebase Authentication, Auth0, or another established authentication provider — not a custom-built login system.

**Why it matters**: Custom authentication is the most common source of security vulnerabilities in web applications. Proven providers handle password hashing, session management, token rotation, and brute force protection correctly.

**How to verify**: Check your codebase for the authentication library or service being used. If you see password comparison logic in your own code, you are likely using custom authentication and should switch to a provider.

### 2. API Keys and Secrets Are in Environment Variables

**Check**: No API keys, database URLs, secret keys, or credentials are hardcoded in your frontend JavaScript files.

**Why it matters**: Any value in your frontend code is visible to users via browser developer tools. Exposed secret keys can lead to unauthorized database access, fraudulent API usage, and data breaches.

**How to verify**: Search your codebase for strings starting with "sk_", "secret", "password", or your Supabase/Stripe secret keys. Check your deployed application's JavaScript bundle by viewing the page source.

### 3. Database Has Row Level Security Enabled

**Check**: Every table in your Supabase database has RLS enabled with appropriate policies that restrict users to their own data.

**Why it matters**: Without RLS, any authenticated user can query, modify, or delete any row in any table — including other users' data. This is the most critical and most commonly missed security measure in AI-built applications.

**How to verify**: Open your Supabase dashboard, go to each table, and check that RLS is enabled (the lock icon should be active). Review the policies to ensure they restrict access by user ID.

### 4. HTTPS Is Enforced on All Pages

**Check**: Your application redirects all HTTP traffic to HTTPS and has a valid SSL certificate.

**Why it matters**: Without HTTPS, user data (including login credentials) is transmitted in plain text and can be intercepted by anyone on the same network.

**How to verify**: Visit your application URL with http:// — it should automatically redirect to https://. Check that the browser shows a lock icon in the address bar.

### 5. Input Validation on All User-Submitted Data

**Check**: Every form and API endpoint validates and sanitizes user input before processing or storing it.

**Why it matters**: Without validation, attackers can inject malicious scripts (XSS), SQL commands (SQL injection), or corrupt your database with invalid data.

**How to verify**: Try submitting forms with empty fields, extremely long text, HTML tags, and special characters. The application should reject invalid input with clear error messages.

## Payments (Items 6–9) — Required If You Accept Payments

### 6. Stripe Is in Live Mode

**Check**: Your Stripe integration uses live API keys (starting with pk_live and sk_live), not test keys.

**How to verify**: Check your environment variables for the Stripe publishable key prefix. Process a small real transaction (€0.50) and verify it appears in your Stripe dashboard under live mode.

### 7. Webhooks Are Configured and Verified

**Check**: Stripe webhooks are configured to send events to your production endpoint, and your code verifies the webhook signature before processing.

**Why it matters**: Without webhook verification, attackers could send fake payment confirmation events to grant themselves free access. Without webhooks at all, your application cannot respond to payment events like successful payments, cancellations, and failed charges.

### 8. Failed Payments Are Handled Gracefully

**Check**: When a payment fails (declined card, insufficient funds, expired card), your application shows a clear error message and does not grant access to paid features.

**How to verify**: Use Stripe's test card numbers for declined payments and verify your application handles each scenario correctly.

### 9. Users Get Access Only After Confirmed Payment

**Check**: Premium features are gated behind verified payment status, not just the completion of a checkout form.

**Why it matters**: Without proper verification, users might access paid features by navigating directly to URLs or manipulating client-side state.

## Deployment (Items 10–14) — Essential

### 10. App Runs on Your Own Domain

**Check**: Your application is accessible at yourdomain.com, not a preview URL like project-abc123.vercel.app.

### 11. Environment Variables Are Set for Production

**Check**: All configuration values (API keys, database URLs, feature flags) are stored as environment variables in your hosting platform, not in code files.

### 12. Build Process Works Without Manual Steps

**Check**: Pushing code to your repository automatically triggers a build and deployment without any manual intervention.

### 13. Error Tracking Is Set Up

**Check**: An error tracking service (Sentry, LogRocket, Bugsnag) is configured to capture and alert you about production errors.

### 14. Backup Strategy Exists for Your Database

**Check**: Your database has automated daily backups enabled and you have tested restoring from a backup at least once.

## Performance (Items 15–18) — Strongly Recommended

### 15. Page Loads in Under 3 Seconds

**Check**: Test your application on Google PageSpeed Insights — aim for a performance score above 70 on mobile.

### 16. Works on Mobile

**Check**: All pages and features work correctly on mobile devices with touch-friendly buttons, readable text, and proper layouts.

### 17. Handles Errors Without Crashing

**Check**: Network failures, API errors, and missing data show user-friendly error messages instead of white screens or technical error dumps.

### 18. No Console Errors in Production

**Check**: Open browser developer tools on your production site — there should be no JavaScript errors in the console during normal usage.

## Legal and Launch (Items 19–20) — Required for EU

### 19. Terms of Service and Privacy Policy in Place

**Check**: Your application has accessible pages for Terms of Service and Privacy Policy, and users agree to these during registration.

### 20. Tested with at Least 3 Real People

**Check**: At least 3 people from your target audience have used the application without guidance and you have addressed the issues they found.

## Scoring Your Application

| Score | Assessment | Recommendation |
| --- | --- | --- |
| 18–20 passed | Launch ready | You are ready to accept real users. Launch with confidence. |
| 14–17 passed | Almost ready | Fix the remaining items before launch. Most gaps can be addressed in a few days. |
| 8–13 passed | Needs work | Your prototype is a strong starting point but needs professional production readiness work. |
| 0–7 passed | Not ready | Do not launch yet. Get professional help to address the critical gaps. |

Most AI-built prototypes score between 4 and 8 on this checklist. That is completely normal — it reflects the gap between prototype and production that all AI-generated applications share. The important thing is knowing the score and addressing the gaps before your first real user.

## Key Takeaways

- Use this 20-point checklist to assess your AI-built prototype's production readiness

- All 5 security items are mandatory — never launch without them

- Most AI-built prototypes pass only 4–8 of the 20 items

- Row Level Security is the most commonly failed and most critical item

- Professional launch services can address all failed items in 1–3 weeks

## Scored Below 16? We Can Help

If your application failed multiple checks on our 20-point checklist, do not panic. LaunchStudio specializes in closing these critical backend gaps, transforming your AI prototype into a launch-ready, enterprise-grade product.

LaunchStudio is Operated by **Manifera**, an international custom software development firm founded and directed by **Herre Roelevink**. To provide cost-effective yet high-quality software solutions, Herre established offices in **Singapore** and **Ho Chi Minh City, Vietnam**, alongside its European HQ in **Amsterdam, the Netherlands** (Herengracht 420). This global delivery network enables us to bridge the gap between AI speed and professional engineering stability. Through LaunchStudio, our senior developers will review your checklist score and address all security, payment, and deployment gaps in just 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: Resolving Launch Checklist Gaps for a Support Analytics Tool

Lucas, a former support manager, used **Cursor** to build a chatbot logs analytics dashboard for client support teams. Although the dashboard visually populated data nicely, a launch readiness audit revealed his app failed 12 of the 20 checklist checks: he was on a free Supabase plan with zero database backups, had no error tracking software (Sentry), lacked database access controls (RLS), and API credentials were hardcoded directly in client-side script tags.

Lucas partnered with **LaunchStudio (by Manifera)**. The engineering team secured the client-side code by moving all secrets to environment variables, configured comprehensive Supabase RLS policies, migrated his database to secure automated daily backups, and integrated Sentry for real-time error logging.

**Result:** Lucas's tool became fully production-ready, allowing him to pass client security audits and sign up his first three corporate customers within 10 days of launch.

**Cost & Timeline:** €3,200 (Grow Package) — production-ready and deployed in 10 business days.

---

## Frequently Asked Questions

### How many checklist items must pass before I can launch?

All 5 security items are mandatory — launching without them exposes your users' data and creates legal liability. Payment items are required if you accept payments. We recommend passing at least 16 out of 20 items before going live.

### What is the most commonly failed checklist item?

Row Level Security (item 3) is the most commonly failed item. Approximately 80% of AI-built Supabase applications we review have RLS either disabled or incorrectly configured, meaning any authenticated user can access any other user's data.

### Can I use this checklist for apps not built with AI?

Yes, this checklist applies to any web application preparing for launch. The items are universal production readiness requirements. However, AI-built applications fail these checks more frequently because AI generators prioritize functionality and UI over security and operational readiness.

### How long does it take to fix failed checklist items?

For an experienced developer, most individual items take 1–4 hours to implement. The full set of fixes for a typical AI-built application takes 1–3 weeks when done professionally. LaunchStudio handles all checklist items as part of our launch packages, priced at €800–€7,500.

### What happens if I launch without completing the security checklist?

Launching without security measures exposes you to data breaches, unauthorized access to user accounts, potential GDPR violations (with fines up to 4% of annual revenue or €20 million), loss of user trust, and potential legal action from affected users.
