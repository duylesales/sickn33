---
title: "Industrial IoT Platform Vendors: The Edge Computing vs Cloud Decision"
keywords: "industrial IoT platform vendor, edge computing vs cloud IoT, IIoT vendor selection, industrial IoT architecture decision, edge computing vendor due diligence"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Industrial IoT Platform Vendors: The Edge Computing vs Cloud Decision

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Industrial IoT Platform Vendors: The Edge Computing vs Cloud Decision",
  "description": "A CTO's technical guide to deciding between edge and cloud architecture when selecting an industrial IoT platform vendor, covering latency requirements, bandwidth constraints, hybrid deployment patterns, and gateway hardware lock-in.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-12",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/industrial-iot-platform-vendors-edge-computing-vs-cloud-decision"}
}
</script>

A vibration sensor on a stamping press can generate a decision that needs to happen in under 10 milliseconds — stop the press before a tooling failure damages a die worth six figures — or it can generate a trend line that a reliability engineer reviews once a week to plan next quarter's maintenance schedule. Both are legitimate industrial IoT use cases, and they belong on architecturally different sides of the same decision: the first has to happen at the edge, physically close to the equipment, because round-tripping to a cloud region and back introduces latency the safety-critical control loop cannot tolerate; the second can run entirely in the cloud, where storage is cheap and compute for training a machine learning model across a fleet of assets is far more powerful than anything practical to run on factory-floor hardware.

Most industrial IoT platform vendors pitch either an edge-first or cloud-first architecture as though it's a universal answer, when in reality almost every real deployment needs both, in different proportions depending on the specific use case. For a CTO selecting an IIoT vendor, understanding where the edge/cloud boundary should sit for your specific workloads — and whether the vendor's architecture actually supports that split cleanly — is a more consequential decision than almost any feature on the platform's marketing page. This article works through how to make that call.

## Start With Latency Requirements, Not Architecture Preference

The single clearest determinant of edge versus cloud placement is latency tolerance for the specific decision being made. A safety interlock, a real-time process control adjustment, or any use case where a delayed response has a direct physical consequence (equipment damage, product defect, safety incident) needs processing at the edge — typically defined as compute running on-premises, often on a ruggedized industrial PC or a purpose-built edge gateway physically close to or directly connected to the equipment generating the data, with response times in the single-digit to low-double-digit milliseconds.

Analytics, trend detection, cross-asset pattern recognition, and any workload where a delay of seconds to minutes is operationally acceptable can run in the cloud, where the platform benefits from centralized compute, easier model retraining across a full fleet of assets rather than a single site, and simpler long-term data retention. Before evaluating any vendor, categorize your actual planned use cases by latency requirement — this categorization, done honestly against real operational needs rather than architectural preference, should drive the vendor conversation, not the reverse.

## Bandwidth Reality: Why "Send Everything to the Cloud" Rarely Works

A single high-frequency vibration sensor sampling at even a modest rate can generate a nontrivial data volume, and a facility with hundreds of sensors across dozens of assets, each streaming continuously, quickly produces a bandwidth requirement that most industrial network connections were never provisioned for. Sending 100% of raw sensor data to the cloud continuously is rarely practical or necessary — the edge computing value proposition, beyond latency, includes local preprocessing: filtering, aggregation, and feature extraction happening on-site so that only meaningful, reduced-volume data (an anomaly flag, a computed feature set, a periodic summary rather than a continuous raw stream) traverses the network to the cloud.

Ask the vendor specifically how their edge layer handles this preprocessing — is it configurable per sensor type and use case, or a fixed pipeline that may not match your specific bandwidth constraints? Also ask what happens during a network outage: does the edge layer buffer data locally and backfill once connectivity restores, or is data lost during any gap in cloud connectivity? For a facility with unreliable or metered connectivity (common in remote industrial sites, mining operations, or older facilities not built with high-bandwidth networking in mind), this buffering behavior directly determines whether the platform is usable at all.

## Hybrid Architecture: What a Genuinely Capable Vendor Should Offer

The realistic architecture for most industrial deployments is hybrid: edge compute handling latency-critical control loops and local data reduction, with a cloud layer handling fleet-wide analytics, long-term storage, and cross-site pattern detection that no single edge node can see on its own. Ask the vendor to describe their specific hybrid architecture, not in marketing terms but in concrete component terms: what runs on the edge gateway, what protocol carries data from edge to cloud (MQTT is common for this specific hop, given its lightweight publish-subscribe design suited to constrained and intermittent connections), and how model updates or configuration changes get pushed back down from the cloud to edge devices across potentially hundreds of physically distributed locations.

This last point — over-the-air update and configuration management for a distributed edge fleet — is an operationally significant capability that's easy to overlook during evaluation but expensive to discover missing after deployment. Ask specifically how the vendor handles fleet-wide edge software updates: a manual, one-site-at-a-time process is a very different operational commitment than a managed, staged rollout capability built into the platform.

## Gateway Hardware Lock-In and the Standards Question

Edge computing introduces a physical-layer vendor dependency that pure cloud platforms don't carry: the edge gateway hardware itself. Some IIoT vendors sell or mandate proprietary gateway hardware that only runs their software stack; others support deployment on standard, off-the-shelf industrial PCs or containerized workloads (increasingly via Kubernetes-based edge orchestration frameworks like K3s, suited to resource-constrained edge environments) that could, in principle, run a different vendor's software if you ever switched.

Ask directly whether the vendor's edge software is portable to standard hardware and containerized deployment, or tied to their own proprietary appliance. This is directly analogous to the sensor protocol lock-in risk relevant to [predictive maintenance vendor contracts](https://www.manifera.com/blog/iot-sensor-platform-vendors-for-predictive-maintenance-data-ownership-clauses) — a proprietary gateway compounds switching cost well beyond the software layer, since replacing the platform means replacing physical hardware across every deployed site simultaneously, rather than migrating software incrementally.

## Security Implications of the Edge/Cloud Boundary

The edge/cloud boundary is also a security boundary, and it carries the same OT/IT convergence risk relevant to any system that bridges factory-floor equipment with wider network connectivity. An edge gateway that has both a direct connection to PLCs or SCADA systems and an outbound connection to the public internet (to reach the vendor's cloud platform) is, structurally, a bridge between the OT and IT/internet-facing worlds — the same architectural pattern worth scrutinizing closely when evaluating [manufacturing execution system vendors](https://www.manifera.com/blog/manufacturing-execution-system-vendors-ot-it-integration-risk).

Ask the vendor specifically how the edge gateway is secured: is outbound-only connectivity enforced (the gateway initiates connections to the cloud, rather than accepting inbound connections, which meaningfully reduces attack surface), is data encrypted both in transit and at rest on the gateway itself, and what is the gateway's own patch and vulnerability management process, given that it is effectively an internet-connected device sitting inside your OT network perimeter.

## Making the Final Call

The edge-versus-cloud decision is not a single architectural choice made once — it's a per-use-case determination that a genuinely capable industrial IoT vendor should be able to discuss fluently, backed by a real hybrid architecture rather than a single deployment model stretched to cover every scenario. Categorize your actual use cases by latency tolerance and bandwidth reality before evaluating vendors, push for specifics on edge fleet management and gateway hardware portability, and treat the edge gateway's security posture as seriously as any other internet-connected device on your OT network. The vendor worth choosing is the one whose architecture reflects genuine engineering judgment about where each workload belongs, not a one-size-fits-all pitch.

Manifera helps manufacturing and industrial organizations architect edge and cloud IoT deployments matched to real latency and security requirements — see our [custom software development](https://www.manifera.com/services/custom-software-development/) and [migration to EU cloud infrastructure](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/) services for how we approach this kind of architecture decision.

## Frequently Asked Questions

### How do I know if an industrial IoT use case needs edge or cloud processing?
Categorize by latency tolerance for the decision being made. Safety interlocks, real-time process control, and any scenario where a delayed response has a direct physical consequence need edge processing with single-digit to low-double-digit millisecond response times. Trend analysis and fleet-wide pattern detection tolerating seconds-to-minutes delay can run in the cloud.

### Why can't I just send all sensor data to the cloud?
Bandwidth constraints make this impractical for most facilities with dozens of assets streaming continuously. Edge preprocessing — filtering, aggregation, and feature extraction on-site — reduces what actually needs to traverse the network to meaningful, reduced-volume data rather than a continuous raw stream.

### What does a genuinely hybrid IIoT architecture look like?
Edge compute handles latency-critical control loops and local data reduction, typically communicating to the cloud via a lightweight protocol like MQTT, while the cloud layer handles fleet-wide analytics, long-term storage, and cross-site pattern detection. Ask vendors to describe this in concrete component terms, not marketing language.

### Why does edge gateway hardware create vendor lock-in risk?
Some vendors mandate proprietary gateway hardware that only runs their own software stack, while others support standard industrial PCs or containerized deployment. Proprietary hardware compounds switching cost, since replacing the platform means replacing physical hardware across every site simultaneously rather than migrating software incrementally.

### What security questions should I ask about an edge gateway connected to OT systems?
Ask whether the gateway enforces outbound-only connectivity to reduce attack surface, whether data is encrypted in transit and at rest, and what the gateway's patch and vulnerability management process looks like, since it functions as an internet-connected device sitting inside your OT network perimeter.
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I know if an industrial IoT use case needs edge or cloud processing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Categorize by latency tolerance for the decision being made. Safety interlocks, real-time process control, and any scenario where a delayed response has a direct physical consequence need edge processing with single-digit to low-double-digit millisecond response times. Trend analysis and fleet-wide pattern detection tolerating seconds-to-minutes delay can run in the cloud."
      }
    },
    {
      "@type": "Question",
      "name": "Why can't I just send all sensor data to the cloud?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bandwidth constraints make this impractical for most facilities with dozens of assets streaming continuously. Edge preprocessing — filtering, aggregation, and feature extraction on-site — reduces what actually needs to traverse the network to meaningful, reduced-volume data rather than a continuous raw stream."
      }
    },
    {
      "@type": "Question",
      "name": "What does a genuinely hybrid IIoT architecture look like?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Edge compute handles latency-critical control loops and local data reduction, typically communicating to the cloud via a lightweight protocol like MQTT, while the cloud layer handles fleet-wide analytics, long-term storage, and cross-site pattern detection. Ask vendors to describe this in concrete component terms, not marketing language."
      }
    },
    {
      "@type": "Question",
      "name": "Why does edge gateway hardware create vendor lock-in risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some vendors mandate proprietary gateway hardware that only runs their own software stack, while others support standard industrial PCs or containerized deployment. Proprietary hardware compounds switching cost, since replacing the platform means replacing physical hardware across every site simultaneously rather than migrating software incrementally."
      }
    },
    {
      "@type": "Question",
      "name": "What security questions should I ask about an edge gateway connected to OT systems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask whether the gateway enforces outbound-only connectivity to reduce attack surface, whether data is encrypted in transit and at rest, and what the gateway's patch and vulnerability management process looks like, since it functions as an internet-connected device sitting inside your OT network perimeter."
      }
    }
  ]
}
</script>
