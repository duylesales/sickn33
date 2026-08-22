---
title: "Just Add Real-Time: Why 'A Few Websockets' Turns Into a Six-Month Distributed Systems Problem"
keywords: "custom software development company, offshore software development company, software architecture, dedicated development team"
buyer_stage: "Consideration"
target_persona: "CTO"
---

# Just Add Real-Time: Why "A Few Websockets" Turns Into a Six-Month Distributed Systems Problem

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Just Add Real-Time: Why 'A Few Websockets' Turns Into a Six-Month Distributed Systems Problem",
  "description": "A CTO's guide to why real-time collaboration features — the kind that look simple in a competitor's product — are quietly one of the hardest distributed-systems problems in modern software, and why the estimate was wrong from day one.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/real-time-collaboration-feature-complexity-underestimate" }
}
</script>

The original estimate was three weeks: "add websockets, broadcast changes to connected clients." Six months later, the team is still fighting conflicting edits, out-of-order updates, and a reconnection flow that occasionally duplicates a user's own changes back at them.

**The Pain:** A CTO greenlit a real-time collaborative editing feature — multiple users editing the same document, board, or record simultaneously — based on an estimate that treated it as "adding websockets" to an existing CRUD application. The feature demoed fine with two people in the same room on the same network. In production, with real network variability, concurrent edits from multiple users routinely produce conflicting states, dropped updates, and a reconnection flow after a network blip that either loses changes or duplicates them.

**The Agitation:** Real-time collaboration is a genuine distributed-systems problem wearing a simple UI — conflict resolution, operational transformation or CRDTs, presence management, and reconnection state reconciliation are all research-grade problems that companies like Google and Figma have dedicated entire engineering teams to solving, not a feature that bolts onto an existing request-response architecture in a few weeks. A CTO who greenlit the feature on the original estimate now has a team that's spent months fighting symptoms — patching one conflict scenario only to discover another — without addressing the actual architectural gap: the system was never designed to reconcile concurrent, out-of-order state changes from multiple simultaneous sources.

## The Real-Time Architecture Mandate

The first mandate is recognizing explicitly, before estimating, that real-time collaborative editing requires a fundamentally different data model than a request-response CRUD application — specifically, either an operational transformation system or a CRDT (conflict-free replicated data type) approach designed from the ground up to reconcile concurrent edits deterministically, not a broadcast-and-hope layer added on top of existing state management.

The second mandate is explicit presence and connection-state management as a first-class system component, not an afterthought — tracking who's connected, what they're editing, and reconciling state correctly when a client reconnects after a network interruption, which is where most naive real-time implementations actually fail in production, not in the happy-path broadcast case that demos well.

The third mandate is choosing, deliberately, between building custom conflict-resolution logic and adopting a proven, battle-tested library or protocol for this exact problem — Yjs, Automerge, and similar CRDT libraries exist precisely because this problem has already been solved well by specialists, and building a custom operational-transformation system from scratch is rarely justified against the risk of getting the edge cases wrong.

The fourth mandate is re-scoping the estimate honestly once the real architecture is understood — a genuine real-time collaborative feature, done properly, is typically a multi-month investment with dedicated testing for concurrent-edit and reconnection scenarios, and communicating that reality to the business early is far less costly than months of production firefighting against an estimate that was wrong from the start.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects assess the real-time feature's actual distributed-systems requirements upfront and set an honest, re-scoped estimate before development starts, preventing the months of symptom-patching a wrong initial estimate produces.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam implement the collaboration layer using proven CRDT libraries or operational-transformation approaches, with dedicated testing for concurrent-edit and reconnection scenarios that a demo never surfaces.

This is Dutch Management × Vietnamese Mastery: European architectural judgment that recognizes real-time collaboration as the distributed-systems problem it actually is, paired with execution capacity experienced in the specific libraries and patterns that solve it correctly. Learn more about [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) and how a properly scoped real-time architecture avoids months of production firefighting.

## Case Study & Testimonial

### A Vienna Design-Tool Startup's Conflict Resolution Spiral

Kreativraum GmbH, a Vienna-based collaborative design-tool startup, had spent five months trying to ship a multi-user canvas-editing feature built on a broadcast-based websocket layer added to their existing REST architecture. Concurrent edits from two designers on the same canvas routinely produced visually broken states, and a network reconnection after even a brief interruption sometimes duplicated a user's own recent changes back onto the canvas.

Manifera re-architected the collaboration layer around Yjs, a proven CRDT library, replacing the custom broadcast-and-merge logic entirely, and built explicit presence tracking and reconnection state reconciliation as first-class components with dedicated test coverage for concurrent-edit scenarios. The rebuilt feature shipped in nine weeks and has run in production for the following eight months without a single reported conflict-resolution defect.

> *"We spent five months patching a broadcast layer that was never going to work, because we never actually named what kind of problem we were solving. Once we called it a CRDT problem and used the library built for exactly that, it took nine weeks."*
> — **CTO, Kreativraum GmbH, Austria**

## Broadcast-Layer Approach vs. Manifera's CRDT-Based Architecture

| Criteria | Broadcast-Layer Approach | Manifera's CRDT-Based Architecture |
|---|---|---|
| Conflict resolution | Ad hoc, breaks under concurrent edits | Deterministic, built into the data structure |
| Reconnection handling | Frequently loses or duplicates changes | Explicit state reconciliation on reconnect |
| Development approach | Custom logic built from scratch | Proven, battle-tested library |
| Time to production-stable | Months of symptom-patching | Weeks, with dedicated concurrent-edit testing |
| Long-term maintenance risk | High, edge cases keep surfacing | Low, built on maintained, widely-used foundations |

## The Economics

A real-time collaboration feature built on the wrong architectural foundation typically costs a team months of engineering time fighting symptoms — each patched conflict scenario revealing another — before the underlying gap is even correctly diagnosed, easily consuming €80,000-€150,000 in engineering cost before shipping something genuinely production-stable. Properly scoping the feature from the start using proven CRDT or operational-transformation approaches typically costs €50,000-€90,000 and reaches production-stable in a fraction of the time, because the hardest problems were already solved by the library rather than being re-discovered the hard way. [Talk to Manifera](https://www.manifera.com/contact-us/) about scoping your real-time feature against the architecture it actually requires, before the estimate goes six months over.

## Frequently Asked Questions

### (Scenario: CTO whose real-time feature estimate was based on "just adding websockets") Why did our real-time collaboration feature estimate turn out to be so wrong?

Because websockets solve the transport problem — getting messages between client and server — but not the harder problem of reconciling concurrent, conflicting edits from multiple users, which requires a fundamentally different data architecture like CRDTs or operational transformation.

### (Scenario: CTO deciding whether to build custom conflict resolution or use a library) Should we build our own conflict-resolution logic or use an existing library?

Use an existing, proven library like Yjs or Automerge wherever possible — this exact problem has already been solved well by specialists, and custom operational-transformation logic is difficult to get right across all the edge cases a production system will encounter.

### (Scenario: CTO trying to understand why the feature demoed fine but breaks in production) Why did the real-time feature work fine in our demo but break with real users?

Demos typically involve one or two users on the same stable network, which never exercises the concurrent-edit conflicts and network-interruption reconnection scenarios that are the actual hard problems real-time collaboration needs to solve.

### (Scenario: CTO trying to re-scope a stalled real-time feature project) We're already months into a struggling real-time feature — is it better to keep patching or re-architect?

If the underlying architecture is a broadcast-and-merge approach without a proper conflict-resolution foundation, re-architecting around a proven CRDT library is typically faster than continuing to patch individual conflict scenarios indefinitely.

### (Scenario: CTO trying to estimate a real-time feature honestly before starting) How should a CTO estimate a real-time collaborative feature honestly from the start?

Treat it explicitly as a distributed-systems problem requiring a CRDT or operational-transformation data model, presence management, and dedicated concurrent-edit and reconnection testing, typically a multi-month investment even using proven libraries, not a multi-week addition to existing architecture.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO whose real-time feature estimate was based on \"just adding websockets\") Why did our real-time collaboration feature estimate turn out to be so wrong?", "acceptedAnswer": { "@type": "Answer", "text": "Websockets solve the transport problem, not the harder problem of reconciling concurrent, conflicting edits, which requires a fundamentally different data architecture like CRDTs." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding whether to build custom conflict resolution or use a library) Should we build our own conflict-resolution logic or use an existing library?", "acceptedAnswer": { "@type": "Answer", "text": "Use an existing, proven library like Yjs or Automerge wherever possible, since custom operational-transformation logic is difficult to get right across all edge cases." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to understand why the feature demoed fine but breaks in production) Why did the real-time feature work fine in our demo but break with real users?", "acceptedAnswer": { "@type": "Answer", "text": "Demos typically involve one or two users on a stable network, which never exercises the concurrent-edit conflicts and reconnection scenarios that are the actual hard problems." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to re-scope a stalled real-time feature project) We're already months into a struggling real-time feature — is it better to keep patching or re-architect?", "acceptedAnswer": { "@type": "Answer", "text": "If the underlying architecture lacks a proper conflict-resolution foundation, re-architecting around a proven CRDT library is typically faster than continuing to patch indefinitely." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to estimate a real-time feature honestly before starting) How should a CTO estimate a real-time collaborative feature honestly from the start?", "acceptedAnswer": { "@type": "Answer", "text": "Treat it explicitly as a distributed-systems problem requiring a CRDT or operational-transformation data model, typically a multi-month investment even with proven libraries." } }
  ]
}
</script>
