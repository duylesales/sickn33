---
Title: "IT Web Development Company Procurement: The 'Security by Obscurity' Trap"
Keywords: it web development company, offshore software security, custom software development, Zero Trust architecture, data encryption, GDPR compliance, Manifera
Buyer Stage: Consideration / Risk Assessment
Target Persona: B (CISO / IT Director)
Content Format: Security Audit Framework
---

# IT Web Development Company Procurement: The "Security by Obscurity" Trap

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "IT Web Development Company Procurement: The 'Security by Obscurity' Trap",
  "description": "A CISO's guide to auditing an IT web development company. Explains the dangers of 'Security by Obscurity', how cheap agencies fail at RBAC and Data-at-Rest encryption, and how to mandate a Zero Trust architecture.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-25"
}
</script>

When evaluating an **IT web development company**, the procurement process usually focuses on two metrics: hourly rate and technical stack. Security is often relegated to a single checkbox on an RFP: *"Is your code secure?"*

The vendor checks the box. The contract is signed.

Two years later, a junior employee accidentally accesses the CEO’s unencrypted payroll data by simply changing a number in the URL (e.g., from `id=402` to `id=1`). The company faces a massive GDPR fine and severe reputational damage. 

When the CISO audits the codebase, they discover that the offshore agency didn't build an actual security architecture. They built "Security by Obscurity."

> *"Security by Obscurity means hiding the keys under the doormat and hoping the burglar doesn't look there. In enterprise software, it is the signature of an amateur engineering team."* — Standard CISO Axiom

If you are outsourcing [custom software development](https://www.manifera.com/services/custom-software-development/), you must stop accepting verbal promises of security. You must audit the agency’s architectural approach to authorization and encryption.

## The 3 Pillars of the "Security by Obscurity" Trap

Cheap agencies rely on obscuring data rather than mathematically securing it. Here is how they fail.

### 1. Insecure Direct Object References (IDOR)
In a poorly built application, the URL to view an invoice might look like this: `/invoices/view/8042`. 
An agency practicing Security by Obscurity assumes that because User A doesn't *know* the ID for User B's invoice (8043), User A cannot view it. But if User A simply changes the URL to `8043` in their browser, the server returns the invoice because the backend never checked if User A was actually *authorized* to view it. 

### 2. Frontend-Only Authorization
Amateur developers often implement Role-Based Access Control (RBAC) by hiding buttons on the frontend. If a user is not an Admin, the "Delete Database" button is simply set to `display: none;` in the CSS. 
However, the actual API endpoint (`DELETE /api/database`) remains completely open. A malicious user with basic technical knowledge can bypass the frontend entirely, send a direct request to the API, and delete the database.

### 3. Ignoring Data-at-Rest Encryption
Many agencies will proudly state they use HTTPS (Data in Transit encryption). This is the bare minimum required by modern web browsers; it is not an achievement. The real test is Data-at-Rest. 
If an attacker breaches the database server and downloads the SQL file, what do they see? In an amateur build, they see plaintext passwords, plain text credit card numbers, and plain text PII (Personally Identifiable Information).

## How to Audit an IT Web Development Company

To prevent these catastrophic failures, your technical due diligence must mandate a **Zero Trust Architecture**. 

Zero Trust assumes that the frontend is compromised, the network is compromised, and the user is malicious. Every single request must be mathematically verified.

### The CISO's Vendor Audit Checklist

Before signing a contract with an **IT web development company**, demand written answers to these architectural questions:

| The CISO's Question | The "Security by Obscurity" Answer | The Zero Trust Answer |
|---|---|---|
| **"How do you prevent IDOR attacks?"** | "We use UUIDs (long random strings) instead of integers so users can't guess the URLs." | "UUIDs are good, but insufficient. Every single API endpoint enforces strict, server-side RBAC checks to verify the user's JWT token matches the resource owner." |
| **"How is the API secured?"** | "We hide the admin buttons for regular users on the frontend." | "The backend API is completely decoupled from the frontend. The backend verifies authorization on every incoming request, regardless of what the frontend UI displays." |
| **"How do you handle sensitive PII?"** | "Our database is hosted on AWS, which is very secure." | "We encrypt specific PII columns (like social security numbers) at the application level before they are written to the database (Data-at-Rest encryption)." |

## The Manifera Security Standard

At Manifera, we know that [offshore software development](https://www.manifera.com/services/offshore-software-development/) is often viewed as a security risk by enterprise CISOs. We built our Hybrid Offshore model to eliminate that risk entirely.

Our Vietnamese engineering pods are governed by Dutch Architects who enforce strict European security standards (including GDPR compliance and ISO 27001 best practices). 

We do not allow "Security by Obscurity." Our CI/CD pipelines include automated Static Application Security Testing (SAST) to detect IDOR vulnerabilities and hardcoded secrets *before* they are merged into the main branch. We mandate server-side RBAC on every endpoint. We treat your data as if it is already under attack.

Stop outsourcing your security architecture to cheap agencies. Contact our Amsterdam team for a technical audit of your software platform.

---

## Frequently Asked Questions

### (Scenario: IT Director reviewing a vulnerability report) What is an IDOR vulnerability and why is it so common?
Insecure Direct Object Reference (IDOR) happens when an application provides direct access to an object (like a database record) based on user-supplied input (like a URL parameter `id=5`), without verifying if the user is authorized to view it. It is common in cheap offshore development because it requires extra backend code and careful RBAC planning to prevent, which order-taker agencies usually skip.

### (Scenario: CISO establishing vendor guidelines) Why isn't hiding a button on the frontend sufficient for security?
Because the frontend (the browser) is entirely controlled by the user. Any user with basic knowledge can open the browser's Developer Tools, unhide the button, or simply bypass the frontend entirely and send a malicious request directly to your backend API using a tool like Postman. All authorization logic must exist on the backend server, which the user cannot manipulate.

### (Scenario: CTO planning a GDPR compliance audit) What is the difference between Data in Transit and Data at Rest encryption?
Data in Transit (HTTPS) encrypts data as it travels between the user's browser and your server, stopping hackers from intercepting it on public Wi-Fi. Data at Rest encrypts the data as it is stored on your actual hard drives or databases. If a hacker breaches your server, Data at Rest encryption ensures they only steal unreadable ciphertext, not plain-text user emails and passwords.

### (Scenario: VP Engineering setting up CI/CD pipelines) How can we automatically catch security flaws in offshore code?
By integrating SAST (Static Application Security Testing) tools like SonarQube or Snyk into your CI/CD pipeline. These tools automatically scan the offshore team's code on every Pull Request. If they detect hardcoded passwords, SQL injection vulnerabilities, or obvious IDOR flaws, the pipeline automatically blocks the code from being merged into production.

### (Scenario: Procurement Officer evaluating risk) How does Manifera ensure GDPR compliance with an offshore team?
Through our Hybrid Offshore model. Our Dutch Architects act as the compliance firewall. Furthermore, we employ a Zero Trust development environment: our Vietnamese engineers never have access to production databases containing real PII. They build and test the software using strictly anonymized, synthetic data, ensuring GDPR compliance is maintained at all times.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is an IDOR vulnerability and why is it so common?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IDOR (Insecure Direct Object Reference) occurs when an app grants access to a record just because a user changed a URL ID, without verifying authorization. It's common because preventing it requires extra backend RBAC code that cheap agencies skip."
      }
    },
    {
      "@type": "Question",
      "name": "Why isn't hiding a button on the frontend sufficient for security?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the user controls the browser. They can unhide the button or bypass the frontend entirely to send direct requests to the API. All authorization checks must happen on the backend server."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between Data in Transit and Data at Rest encryption?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Data in Transit (HTTPS) encrypts data moving over the network. Data at Rest encrypts data stored on your database. Without Data at Rest encryption, a breached server exposes plain-text PII to hackers."
      }
    },
    {
      "@type": "Question",
      "name": "How can we automatically catch security flaws in offshore code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By integrating SAST (Static Application Security Testing) tools into your CI/CD pipeline. These scan code on every Pull Request and automatically block merges if they detect vulnerabilities like SQL injections or hardcoded secrets."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera ensure GDPR compliance with an offshore team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our Dutch Architects act as a compliance firewall. Our offshore engineers operate in a Zero Trust environment and never access production PII. They build and test using only anonymized, synthetic data."
      }
    }
  ]
}
</script>
