---
Title: "Security-First Development: Building Software That Hackers Cannot Break"
Keywords: application security, secure software development, OWASP, penetration testing, DevSecOps, Manifera
Buyer Stage: Consideration
Target Persona: A (CTO / VP Engineering)
Content Format: Strategic Guide
---

# Security-First Development: Building Software That Hackers Cannot Break

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Security-First Development: Building Software That Hackers Cannot Break",
  "description": "A comprehensive guide for CTOs on embedding security into every phase of software development — from threat modelling to OWASP Top 10 prevention, penetration testing, and building a security-conscious engineering culture.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-08-04"
}
</script>

The average cost of a data breach in 2025 reached €4.5 million globally, according to IBM's annual Cost of a Data Breach report. For startups, the number is irrelevant — because a single breach often means death. When a startup loses customer data, it does not pay a fine and move on. It loses every enterprise deal in its pipeline, its reputation is permanently damaged, and customer churn spikes to unsurvivable levels. Security is not a feature to add after launch. It is the foundation everything else stands on.

## Threat Modelling: Think Like an Attacker Before Writing Code

Most development teams build features and then ask "is this secure?" after deployment. Security-first teams ask "how could this be attacked?" before writing the first line of code. This is threat modelling — the practice of systematically identifying what could go wrong.

**The STRIDE framework for developers:**

For every new feature, walk through these six threat categories:

- **Spoofing.** Can an attacker pretend to be another user? Does your authentication system verify identity at every request, or only at login?
- **Tampering.** Can an attacker modify data in transit or at rest? Are API requests signed? Are database records integrity-checked?
- **Repudiation.** Can a user deny performing an action? Do you have audit logs that prove what happened and when?
- **Information disclosure.** Can an attacker access data they should not see? Are error messages leaking database schemas or stack traces?
- **Denial of service.** Can an attacker overwhelm your system? Do you have rate limiting on all public endpoints?
- **Elevation of privilege.** Can a regular user gain admin access? Is your authorisation checked at every endpoint, not just the UI?

Spend 30 minutes on STRIDE analysis before building any feature that handles user data, authentication, or payments. This €50 investment in developer time can prevent a €4.5 million breach.

## The OWASP Top 10: Practical Prevention

The OWASP Top 10 remains the definitive list of the most critical web application security risks. In 2026, these are the attacks your code must resist:

**1. Broken Access Control** (most critical). The number one vulnerability. Occurs when users can access data or functions they should not. Prevention: check authorisation on the server side for every request. Never rely on the frontend to hide buttons — an attacker does not use your UI.

**2. Injection** (SQL, NoSQL, command). Occurs when user input is embedded directly into queries. Prevention: use parameterised queries exclusively. Never construct queries by concatenating user input strings. This is a solved problem — there is no excuse for injection vulnerabilities in 2026.

**3. Cryptographic Failures.** Storing passwords in plaintext, using MD5 for hashing, transmitting sensitive data over HTTP. Prevention: use bcrypt or Argon2 for password hashing, TLS 1.3 for all connections, AES-256 for data at rest.

**4. Security Misconfiguration.** Default credentials, unnecessary open ports, verbose error messages in production, S3 buckets set to public. Prevention: automated security scanning in CI/CD, infrastructure-as-code with security baselines, environment-specific configuration management.

**5. Server-Side Request Forgery (SSRF).** An attacker tricks your server into making requests to internal services. Prevention: whitelist allowed outbound URLs, validate and sanitise all user-supplied URLs, restrict server-side HTTP clients to specific domains.

## Authentication and Authorisation: Getting the Basics Right

Authentication (who are you?) and authorisation (what can you do?) are the two most critical security layers. Getting them wrong renders every other security measure meaningless.

**Authentication best practices in 2026:**

- **Multi-factor authentication** should be mandatory for all admin accounts and strongly encouraged for all users. SMS-based MFA is deprecated — use TOTP (authenticator apps) or WebAuthn (passkeys/hardware keys).
- **Session management.** Use short-lived access tokens (15-60 minutes) with long-lived refresh tokens. Store tokens in HTTP-only, secure, SameSite cookies — never in localStorage.
- **Password policies.** Minimum 12 characters, no maximum length, check against known breached password databases (HaveIBeenPwned API). Do not enforce arbitrary complexity rules (uppercase + number + symbol) — they encourage users to write passwords on sticky notes.

**Authorisation architecture:**

Implement role-based access control (RBAC) at minimum. For complex applications, consider attribute-based access control (ABAC) where permissions depend on context (user role + resource ownership + time of day + IP address).

The critical rule: **authorisation must be checked on the server side, on every request, for every resource.** The frontend controls what the user sees; the backend controls what the user can do. These are independent systems.

## Security in the CI/CD Pipeline

Security scanning that happens once a quarter is security theatre. Real security requires automated checks on every code change:

**Static Application Security Testing (SAST).** Analyse source code for vulnerabilities before it runs. Tools: SonarQube, Semgrep, CodeQL. Run on every pull request. Block merges when critical vulnerabilities are detected.

**Dependency scanning.** Your application's dependencies have their own vulnerabilities. Tools: Dependabot, Snyk, Socket. Automatically create pull requests when vulnerable dependencies are detected. Block deployments when critical CVEs are unpatched.

**Secret scanning.** Developers accidentally commit API keys, passwords, and tokens to version control. Tools: GitGuardian, TruffleHog, GitHub secret scanning. Scan every commit in real-time. Alert immediately when secrets are detected. Rotate compromised credentials within hours, not weeks.

**Dynamic Application Security Testing (DAST).** Test the running application for vulnerabilities from the outside. Tools: OWASP ZAP, Burp Suite. Run against staging environments after deployment.

## Incident Response: When Prevention Fails

No system is impenetrable. Your incident response plan determines whether a breach is a survivable event or a company-ending catastrophe.

**The incident response checklist:**

1. **Detection** (minutes). Automated alerts from your monitoring system flag anomalous behaviour — unusual login patterns, data exfiltration volumes, or privilege escalation attempts.
2. **Containment** (minutes-hours). Isolate the compromised system. Revoke the compromised credentials. Block the attacker's access without taking down the entire application.
3. **Investigation** (hours-days). Analyse logs to determine the scope of the breach. What data was accessed? How did the attacker get in? Is the attack still active?
4. **Notification** (within 72 hours for GDPR). Notify affected users and regulatory authorities. Be transparent about what happened and what you are doing about it.
5. **Recovery** (days-weeks). Patch the vulnerability, restore from clean backups, implement additional monitoring.
6. **Post-mortem** (1 week after). Blameless analysis of what went wrong, what went right, and what changes prevent recurrence.

## Security Across Distributed Development Teams

When your code is written across multiple countries and time zones, security practices must be explicitly codified — not assumed.

At Manifera, security is embedded into our [way of working](https://www.manifera.com/about-us/our-way-of-working/) across Amsterdam and Ho Chi Minh City:

- **Security-focused code review checklist** — every PR is reviewed for OWASP Top 10 vulnerabilities in addition to functional correctness.
- **Automated security gates in CI/CD** — no deployment proceeds without passing SAST, dependency scanning, and secret detection.
- **Quarterly security training** — both Amsterdam and Ho Chi Minh City teams participate in capture-the-flag exercises and vulnerability awareness sessions.
- **Production access controls** — role-based access with MFA, audit logging, and geographic restrictions.

Security is not a phase — it is a discipline. Discuss your application's security posture with our team — [manifera.com/contact-us](https://www.manifera.com/contact-us/).

---

## Frequently Asked Questions

### How much should a startup budget for application security? (Scenario: CEO planning the annual budget for a Series A SaaS company)

Allocate 8-12% of your total engineering budget to security. For a team costing €1 million/year, that is €80,000-€120,000 — covering tool licenses (€15,000-€30,000/year for SonarQube, Snyk, and monitoring), annual penetration testing (€10,000-€25,000), and developer time for security-focused work (the largest cost). This investment prevents breaches that would cost 40-100x more to recover from.

### When should we get a penetration test? (Scenario: CTO preparing for an enterprise sales cycle that requires a security assessment)

Get your first professional penetration test before signing your first enterprise customer — they will ask for the report. Thereafter, conduct penetration tests annually and after any major architectural change (new authentication system, new API surface, infrastructure migration). Budget €10,000-€25,000 per engagement for a thorough test by a reputable firm. Automated scanners are not a substitute — human testers find business logic vulnerabilities that tools miss.

### Is SOC 2 certification necessary for B2B SaaS? (Scenario: VP Sales losing enterprise deals because prospects require SOC 2)

If you sell to companies with more than 200 employees, yes — SOC 2 Type II is increasingly a hard requirement. The certification process takes 6-12 months and costs €30,000-€80,000 (including auditor fees and tooling). Start with SOC 2 Type I (point-in-time assessment) which takes 3-4 months, then progress to Type II (ongoing assessment over 6+ months). The investment pays for itself by unlocking enterprise deals that would otherwise be blocked.

### How do we handle security when using offshore development teams? (Scenario: CISO evaluating risk of having production code written by teams in Southeast Asia)

Four controls: (1) All production environment access goes through VPN with MFA — geographic location of the developer does not change the access controls. (2) Code undergoes the same automated security scanning regardless of who writes it — SAST, dependency scanning, and secret detection. (3) Security-sensitive code (authentication, payment processing, data encryption) is reviewed by senior engineers with security expertise, regardless of team location. (4) Regular security training ensures all team members understand OWASP Top 10 and secure coding practices.

### What is the biggest security mistake startups make? (Scenario: First-time CTO building a SaaS application)

Storing secrets (API keys, database passwords) in source code or environment variables that are committed to version control. This single mistake has caused more startup breaches than any other vulnerability. The fix: use a dedicated secrets management service (AWS Secrets Manager, HashiCorp Vault, Doppler) from day one. It takes 2 hours to set up and eliminates an entire category of catastrophic risk.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much should a startup budget for application security?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Allocate 8-12% of your total engineering budget to security. For a team costing €1 million/year, that is €80,000-€120,000 covering tool licenses, annual penetration testing, and developer time for security work. This prevents breaches costing 40-100x more to recover from."
      }
    },
    {
      "@type": "Question",
      "name": "When should we get a penetration test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before signing your first enterprise customer. Thereafter, annually and after major architectural changes. Budget €10,000-€25,000 per engagement. Automated scanners are not a substitute — human testers find business logic vulnerabilities that tools miss."
      }
    },
    {
      "@type": "Question",
      "name": "Is SOC 2 certification necessary for B2B SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you sell to companies with more than 200 employees, yes. SOC 2 Type II takes 6-12 months and costs €30,000-€80,000. Start with Type I (3-4 months) then progress to Type II. The investment unlocks enterprise deals that would otherwise be blocked."
      }
    },
    {
      "@type": "Question",
      "name": "How do we handle security when using offshore development teams?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Four controls: (1) VPN with MFA for all production access. (2) Same automated security scanning regardless of who writes the code. (3) Security-sensitive code reviewed by senior engineers with security expertise. (4) Regular security training on OWASP Top 10 for all team members."
      }
    },
    {
      "@type": "Question",
      "name": "What is the biggest security mistake startups make?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Storing secrets in source code or committed environment variables. Use a dedicated secrets management service (AWS Secrets Manager, HashiCorp Vault, Doppler) from day one. It takes 2 hours to set up and eliminates an entire category of catastrophic risk."
      }
    }
  ]
}
</script>
