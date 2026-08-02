---
Title: "A Software Company is Not an IT Department: Conway's Law"
Keywords: a software company, custom software development, Conway's Law, IT department, software architecture, organizational design, offshore software engineering, Manifera
Buyer Stage: Consideration / Organizational Design
Target Persona: B (CEO / CIO)
Content Format: Organizational Strategy & Architecture
---

# A Software Company is Not an IT Department: Conway's Law

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A Software Company is Not an IT Department: Conway's Law",
  "description": "An executive guide to organizational design in tech. Explains Conway's Law, the fundamental difference between an IT Department and a Software Company, and how to restructure teams for elite product velocity.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-30"
}
</script>

The CEO of a massive logistics enterprise realizes that the future of their industry is digital. They declare that they are no longer just a trucking business; they are now **a software company**. 

To execute this vision, the CEO tells their existing IT Department to build a revolutionary new customer-facing SaaS platform. 

The IT Department is historically organized into functional silos. There is a "Database Team," a "Security Team," a "Frontend Team," and an "Operations Team." 

Eighteen months later, the SaaS platform launches. It is a disaster. The user interface requires the customer to log into three different portals just to track one shipment. The billing data is entirely disconnected from the routing data. The software feels like it was built by five different companies who never spoke to each other. 

The CEO is furious. *"Why is this software so disjointed and broken?"*

The CEO has just collided with the most powerful sociological force in software engineering: **Conway's Law**. 

You cannot become **a software company** by simply ordering an IT Department to write code. You must fundamentally restructure how your humans are organized, because the software will always perfectly mirror the organizational chart.

## The Iron Trap of Conway's Law

Coined by computer programmer Melvin Conway in 1967, Conway's Law states: 
*"Any organization that designs a system will produce a design whose structure is a copy of the organization's communication structure."*

If your company has four separate departments that require managers to send formal emails to each other to get anything done, your software will have four separate databases that require slow, rigid APIs to communicate with each other. 

### The IT Department (Cost Center)
An IT Department is designed to minimize risk. It is organized by function (Database, Security, Operations) because its historical job was to keep the email servers running and protect the company from hackers. If the Frontend Team needs a new database column, they must submit a formal ticket to the Database Team and wait three weeks. This structure is safe, but it destroys product velocity. 

### The Software Company (Profit Center)
A true Software Company is designed to maximize value. It is not organized by technical function; it is organized by *Business Domain*. 

Elite software companies do not have a "Database Team." They have a "Customer Checkout Team." 
This team is a cross-functional "Pod." It contains a Product Manager, a Frontend Developer, a Backend Developer, and a QA Tester, all sitting at the same table (or in the same Slack channel). 

If the Frontend Developer needs a new database column for the checkout page, they don't submit a ticket to a separate department. They turn around and ask the Backend Developer in their pod to build it. The communication loop drops from three weeks to three minutes. Because the team is unified around a business domain, the software they produce is unified and seamless for the customer.

> *"If you want a seamless, tightly integrated software product, you must design a seamless, tightly integrated human organization. You cannot ship a great product from a broken org chart."* — Organizational Architecture Axiom

## The Inverse Conway Maneuver: Designing the Org Chart Before the Architecture

Most executives discover Conway's Law by accident, after their software has already turned into a tangled mess. But there is a proactive version of the same principle, known in engineering circles as the "Inverse Conway Maneuver." Instead of letting your existing org chart dictate a bad architecture, you deliberately design the org chart you want first, and let the software architecture naturally follow.

Here is how this plays out in practice. A mid-market fintech company wants to move from a single monolithic application to a microservices architecture, with independent services for Payments, Onboarding, and Fraud Detection. If they simply tell their existing, siloed "Backend Team" to "build microservices," the team will produce three services that are technically separate but still tightly coupled, because the humans writing them still sit in one WhatsApp group and make decisions in one weekly meeting. The org chart hasn't changed, so Conway's Law guarantees the software won't either.

The Inverse Conway Maneuver flips the sequence:

1.  **Draw the target architecture diagram first.** Decide on paper that Payments, Onboarding, and Fraud Detection will be three independently deployable services, each with its own database.
2.  **Split the team to match, before a single service is coded.** Create three separate pods, each with its own Backend Developer, and give each pod ownership of exactly one service and one database.
3.  **Cut the informal communication channels between pods.** This sounds counterintuitive, but it is the crucial step. If the Payments pod and Onboarding pod can still casually message each other to "just quickly sync the database directly," they will, and the services will re-couple within weeks. Communication between pods must go through the same formal API contract that any external customer would use.
4.  **Measure deployment independence, not just code separation.** The real test of whether the maneuver worked is whether the Payments pod can deploy ten times a day without ever needing to coordinate with the Fraud Detection pod. If a deployment still requires a cross-pod meeting, the org chart hasn't actually changed yet.

Companies that skip step 1 and jump straight to hiring "microservices developers" almost always end up with what industry engineers call a "distributed monolith": technically separate services that are so behaviorally entangled they must all be deployed together anyway, giving you all the operational overhead of microservices with none of the independence benefits.

## The Manifera Pod Methodology

When legacy enterprises try to build software by hiring standard [offshore software development](https://www.manifera.com/services/offshore-software-development/) agencies, they usually replicate their own broken IT structure. They hire 10 random offshore developers and treat them like a siloed IT department, throwing Jira tickets over the wall and wondering why the resulting software is fragmented and buggy.

At Manifera, we use Conway's Law as a weapon to guarantee software quality. 

We do not provide fragmented freelancers. We provide pre-assembled, cross-functional Engineering Pods. 

When you partner with our Hybrid Offshore model, we assign a dedicated Pod to your specific Business Domain (e.g., the "Logistics Tracking Pod"). 
This pod contains our Vietnamese Backend Specialists, Frontend Specialists, and QA Engineers, all communicating instantly. Crucially, the Pod is led by a European Product Manager and a Dutch Architect based in our Amsterdam headquarters. 

We act as a seamless extension of your business, not a siloed IT vendor. The Dutch Tech Lead translates your business vision directly to the cross-functional pod, ensuring extreme velocity and architectural unity. 

Stop fighting Conway's Law. Contact our Amsterdam team to deploy an integrated, cross-functional software pod.

---

## Frequently Asked Questions

### (Scenario: CEO reorganizing the company) What is 'Conway's Law' and why does it affect software quality?
Conway's Law states that a company's software architecture will perfectly mirror its human communication structure. If your company is organized into rigid, isolated departments that don't talk to each other, your software will be a disjointed mess of isolated systems that don't integrate properly.

### (Scenario: CIO transitioning to product) What is the fundamental difference between an IT Department and a Software Engineering organization?
An IT department is organized by technical function (Database, Security, Network) and optimized for risk reduction and maintaining existing systems. A Software Engineering organization is organized into cross-functional 'Pods' built around specific business goals (e.g., the 'Checkout Team'), optimized for rapid product creation and deployment velocity.

### (Scenario: VP Engineering auditing slow delivery) Why does organizing teams by 'technical function' destroy software velocity?
If you have a separate 'Frontend Team' and 'Database Team', every new feature requires cross-departmental coordination. The Frontend developer must submit a ticket to the Database manager, wait for approval, and wait for scheduling. This turns a 2-hour coding task into a 3-week bureaucratic nightmare.

### (Scenario: Founder structuring a new project) What is a cross-functional 'Pod'?
A Pod is a small, autonomous team (usually 4-8 people) that contains all the skills necessary to build a feature from start to finish. It includes a Product Manager, Frontend Developer, Backend Developer, and QA. Because they are on the same team, they don't have to ask other departments for permission, resulting in massive velocity.

### (Scenario: Procurement evaluating Manifera) How does Manifera's team structure use Conway's Law to benefit the client?
We do not operate as a disconnected IT vendor. We deploy cross-functional Pods dedicated entirely to your specific product domain. With a Dutch Architect and Product Manager leading our Vietnamese developers, the communication structure is perfectly unified. According to Conway's Law, this unified team mathematically guarantees a unified, seamless software product.

### (Scenario: CTO planning a microservices migration) What is the 'Inverse Conway Maneuver' and how does it differ from just reacting to Conway's Law?
Most companies discover Conway's Law only after their software is already a mess. The Inverse Conway Maneuver is the proactive version: you design the org chart you want first, split teams to match before writing a service, and cut informal cross-team communication channels so the architecture is forced to follow the new structure. Skipping this and simply telling an existing siloed team to 'build microservices' usually produces a 'distributed monolith,' where services are technically separate but still have to be deployed together.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is 'Conway's Law' and why does it affect software quality?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Conway's law dictates that software architecture mirrors the organization's human communication structure. If your company operates in rigid, siloed departments, you will inevitably build rigid, disjointed software that frustrates users."
      }
    },
    {
      "@type": "Question",
      "name": "What is the fundamental difference between an IT Department and a Software Engineering organization?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IT Departments are organized by function (Security, Database) to minimize risk. True Software organizations are organized into cross-functional Pods built around business value (e.g., the 'Checkout Team') to maximize product velocity."
      }
    },
    {
      "@type": "Question",
      "name": "Why does organizing teams by 'technical function' destroy software velocity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because it forces developers to constantly wait on other departments. If a frontend engineer needs a database change, they have to file a ticket and wait weeks for the Database Team to process it. Cross-functional pods eliminate these communication bottlenecks."
      }
    },
    {
      "@type": "Question",
      "name": "What is a cross-functional 'Pod'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A Pod is a small, autonomous team containing all the necessary skills to build a feature (Backend, Frontend, QA, PM). Because they work together daily on a shared goal, they communicate instantly and ship code with blistering speed."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's team structure use Conway's Law to benefit the client?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We provide pre-assembled, cross-functional Hybrid Pods. Our Dutch Architects and Vietnamese developers operate as a single, highly integrated unit dedicated to your business domain, which mathematically guarantees the production of seamless, highly integrated software."
      }
    },
    {
      "@type": "Question",
      "name": "What is the 'Inverse Conway Maneuver' and how does it differ from just reacting to Conway's Law?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Inverse Conway Maneuver is the proactive application of Conway's Law: you design the target org chart first, split teams to match before writing any code, and cut informal cross-team communication channels so the software architecture is forced to follow. Skipping this step and telling an existing siloed team to 'build microservices' usually produces a 'distributed monolith' that must still be deployed as one unit."
      }
    }
  ]
}
</script>
