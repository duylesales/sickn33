---
title: "Manufacturing Execution System Vendors: OT/IT Integration Risk"
keywords: "manufacturing execution system vendor, MES vendor selection, OT IT integration risk, MES software due diligence, factory floor software vendor"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Manufacturing Execution System Vendors: OT/IT Integration Risk

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Manufacturing Execution System Vendors: OT/IT Integration Risk",
  "description": "A CTO's guide to evaluating MES vendors on the OT/IT convergence risk they introduce, covering ISA-95 hierarchy, PLC and SCADA protocol support, network segmentation, and patch cadence for shop-floor-connected software.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-04",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/manufacturing-execution-system-vendors-ot-it-integration-risk"}
}
</script>

A manufacturing execution system sits in the single most sensitive position in an industrial technology stack: it bridges operational technology — the PLCs, SCADA systems, and control networks that actually run production equipment — with information technology — the ERP, analytics, and cloud systems the rest of the business depends on. That bridge is exactly where the MES delivers its value, and exactly where it introduces the highest-consequence integration risk in the entire manufacturing IT estate. A CTO evaluating MES vendors is not just buying production scheduling and quality tracking software; they are deciding how much OT/IT convergence risk to accept, and how well the vendor understands that risk versus treating it as somebody else's problem.

This is not abstract risk. A poorly architected MES integration has been the entry vector in real industrial security incidents, and even absent a security event, a badly segmented OT/IT boundary can turn a routine ERP patch into unplanned downtime on a production line. This article covers what to verify technically before selecting an MES vendor, framed around where OT/IT integration risk actually concentrates.

## Anchor the Evaluation in ISA-95, Not the Vendor's Own Terminology

The ISA-95 standard defines a five-level hierarchy for manufacturing operations: Level 0 (the physical process itself), Level 1 (sensors and actuators), Level 2 (supervisory control — PLCs and SCADA), Level 3 (manufacturing operations management — this is where MES lives), and Level 4 (business planning — ERP). The MES's job is to sit at Level 3 and mediate cleanly between Level 2's real-time control data and Level 4's business transaction data, without becoming a direct conduit that lets Level 4 systems (or worse, external actors who've compromised Level 4) reach down into Level 2 control systems.

Every MES vendor should be able to describe, in ISA-95 terms, exactly where their product sits and what data crosses each boundary in which direction. A vendor who cannot speak fluently in this framework — who describes their architecture only in generic "cloud-connected" marketing terms — is a signal that OT/IT boundary discipline may not have been a first-class design concern for the product. Ask directly: what data flows from Level 2 to Level 3, what flows from Level 3 to Level 4, and is any flow bidirectional in a way that could let a Level 4 compromise propagate downward?

## Protocol Support: OPC UA, Modbus, and the Legacy Tail

At the shop-floor integration layer, ask specifically which industrial protocols the MES natively supports for pulling data off PLCs and SCADA systems. OPC UA (Open Platform Communications Unified Architecture) is the modern standard, built with security (encryption and authentication) as a core design feature rather than an afterthought, and is the protocol you want as the primary integration path wherever your equipment supports it. Modbus, still extremely common on older equipment, was designed in the 1970s with no built-in security whatsoever — authentication, encryption, and access control all have to be layered on externally, typically at the network level.

The realistic situation on most factory floors is a mix: newer equipment speaking OPC UA, older equipment speaking Modbus or a proprietary protocol requiring a vendor-specific gateway or driver. Ask the MES vendor for their protocol coverage list against your actual equipment inventory, not a generic capability claim, and specifically ask how they secure Modbus-based connections, since the protocol itself provides no protection and the burden falls entirely on the integration architecture around it.

## Network Segmentation and the Purdue Model

Industrial security practice, formalized in the Purdue Enterprise Reference Architecture (which maps closely to ISA-95), calls for network segmentation between IT and OT zones, typically implemented through a demilitarized zone (DMZ) that mediates traffic rather than allowing direct connections between the corporate network and the control network. An MES, by its nature, needs to talk to both zones, which makes its own network placement one of the most consequential architecture decisions in the whole deployment.

Ask the vendor explicitly: does their reference architecture place MES components within a DMZ, with brokered, one-directional-where-possible data exchange to Level 2 systems? Or does their default deployment pattern require the MES server to have direct network reachability to both the corporate network and the PLC/SCADA network simultaneously — a pattern that, if that server is ever compromised, gives an attacker a direct bridge into production control systems? This is a question that a genuinely OT-experienced vendor will answer readily and in detail; a vendor whose customer base is mostly IT-side software deployments will often not have a clear answer.

## Patch Cadence: The Conflict Between IT Hygiene and OT Stability

IT security practice pushes for rapid patching. OT environments prioritize stability and validated change control, because an unplanned reboot or behavioral change on a system connected to live production equipment can halt a line or, in worse cases, create a physical safety incident. These two philosophies are in direct tension, and an MES vendor sits squarely in the middle of that tension.

Ask the vendor about their patch release cadence, whether patches are cumulative or granular (so you can apply a security fix without also absorbing an unrelated feature change mid-production-run), and what validation process they recommend before applying a patch to a production-connected instance. Also ask about extended support timelines for the specific version you'd be deploying — manufacturing environments often run software for 7-10+ years without a major version upgrade, considerably longer than typical enterprise IT software lifecycles, and a vendor whose support model assumes annual major-version churn is a poor fit for that reality.

## Vendor Lock-In Through Proprietary Protocols

A subtler but longer-term risk: some MES vendors use proprietary data historians or proprietary protocols for their own PLC/SCADA connectivity layer, rather than standards-based OPC UA. This can create meaningful lock-in — your production data, and the integration work connecting it, becomes tied to that vendor's specific technology in a way that is expensive to unwind later, similar in spirit to application-level vendor lock-in but with the added complexity of physical equipment dependencies.

Ask directly whether the vendor's shop-floor connectivity layer is built on open, standards-based protocols that a different MES could theoretically reuse, or a proprietary layer unique to their platform. This matters most for organizations planning a multi-decade manufacturing technology roadmap, where the cost of re-architecting shop-floor connectivity during a future MES replacement should be a known, weighed factor rather than a surprise discovered years in.

## Making the Final Call

MES selection is, underneath the production-scheduling and quality-tracking feature comparison, fundamentally a decision about how much OT/IT integration risk you are willing to accept and how competently the vendor manages it. Push every finalist vendor to speak fluently in ISA-95 and Purdue-model terms, get specific answers on protocol coverage against your actual equipment, and pressure-test their patch cadence against the realities of a production environment that cannot tolerate IT-style rapid iteration. The vendors who treat this as a first-class design concern, not an afterthought bolted onto a generic software platform, are the ones capable of bridging OT and IT without becoming the weakest link between them.

Manifera works with manufacturing organizations to architect MES integrations that respect OT/IT boundary discipline from the design phase — see our [custom software development](https://www.manifera.com/services/custom-software-development/) services or read about [our way of working](https://www.manifera.com/about-us/our-way-of-working/) for how we structure this kind of technical due diligence.

## Frequently Asked Questions

### What is ISA-95 and why does it matter when evaluating MES vendors?
ISA-95 is the standard hierarchy for manufacturing operations, running from the physical process (Level 0) through sensors and control (Levels 1-2), manufacturing operations management where MES lives (Level 3), and business planning (Level 4, typically ERP). A vendor who can describe their architecture fluently in these terms has treated OT/IT boundary discipline as a core design concern rather than an afterthought.

### What's the difference between OPC UA and Modbus for MES integration?
OPC UA is the modern industrial protocol built with encryption and authentication as core features. Modbus, still common on older equipment, was designed with no built-in security, so any Modbus-based MES connection needs security layered on externally at the network level — ask vendors specifically how they handle this.

### How does network segmentation affect MES security risk?
Best practice, following the Purdue model, places MES components in a demilitarized zone that mediates traffic between the corporate IT network and the OT control network, rather than giving the MES server direct simultaneous reachability to both. Direct reachability creates a bridge that, if compromised, could let an attacker reach production control systems.

### Why does patch cadence matter more for MES than typical enterprise software?
OT environments prioritize stability and validated change control because unplanned changes on production-connected systems can halt a line or create safety risks, which conflicts with typical IT practice of rapid patching. Ask vendors about granular versus cumulative patches and extended support timelines, since manufacturing software often runs 7-10+ years without a major version change.

### Can proprietary MES protocols create long-term vendor lock-in?
Yes. Some vendors use proprietary data historians or shop-floor connectivity protocols instead of open standards like OPC UA, which ties your production data and integration work to that vendor specifically. This matters most for organizations planning a multi-decade manufacturing technology roadmap where a future MES replacement is a realistic possibility.
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is ISA-95 and why does it matter when evaluating MES vendors?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ISA-95 is the standard hierarchy for manufacturing operations, running from the physical process (Level 0) through sensors and control (Levels 1-2), manufacturing operations management where MES lives (Level 3), and business planning (Level 4, typically ERP). A vendor who can describe their architecture fluently in these terms has treated OT/IT boundary discipline as a core design concern rather than an afterthought."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between OPC UA and Modbus for MES integration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "OPC UA is the modern industrial protocol built with encryption and authentication as core features. Modbus, still common on older equipment, was designed with no built-in security, so any Modbus-based MES connection needs security layered on externally at the network level — ask vendors specifically how they handle this."
      }
    },
    {
      "@type": "Question",
      "name": "How does network segmentation affect MES security risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Best practice, following the Purdue model, places MES components in a demilitarized zone that mediates traffic between the corporate IT network and the OT control network, rather than giving the MES server direct simultaneous reachability to both. Direct reachability creates a bridge that, if compromised, could let an attacker reach production control systems."
      }
    },
    {
      "@type": "Question",
      "name": "Why does patch cadence matter more for MES than typical enterprise software?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "OT environments prioritize stability and validated change control because unplanned changes on production-connected systems can halt a line or create safety risks, which conflicts with typical IT practice of rapid patching. Ask vendors about granular versus cumulative patches and extended support timelines, since manufacturing software often runs 7-10+ years without a major version change."
      }
    },
    {
      "@type": "Question",
      "name": "Can proprietary MES protocols create long-term vendor lock-in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Some vendors use proprietary data historians or shop-floor connectivity protocols instead of open standards like OPC UA, which ties your production data and integration work to that vendor specifically. This matters most for organizations planning a multi-decade manufacturing technology roadmap where a future MES replacement is a realistic possibility."
      }
    }
  ]
}
</script>
