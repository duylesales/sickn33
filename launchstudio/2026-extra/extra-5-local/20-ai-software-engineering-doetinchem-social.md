Q&A: The one question that nearly stalled a manufacturing deal 🏭

Q: Who's the founder?
A: Niels Terhorst from Doetinchem. He built WerkVloer in Bolt: shift scheduling and equipment-maintenance logging for small industrial workshops.

Q: How far along was it?
A: Two workshops in the Achterhoek were already using it. A third, larger manufacturer was close to signing, pending what its operations manager called "a basic technical review."

Q: What was the question?
A: Whether WerkVloer kept an audit trail. Niels realized he had no idea.

Q: Did it?
A: No. Edits to maintenance logs silently overwrote earlier entries, with no history. For a client that needs maintenance records for compliance, that's a serious gap.

Q: Anything else?
A: Two more things. The equipment API credentials were exposed in the frontend, and shift schedules had no row-level security between workshop accounts.

Q: What changed?
A: LaunchStudio added an append-only audit log for maintenance entries, moved the credentials to a secured backend, and isolated each workshop's data. 7 business days, €1,450.

Q: And the deal?
A: WerkVloer passed the technical review. It now runs at four workshops, with a full, compliant maintenance audit trail.

Q: In Niels's words?
A: "Their operations manager asked one specific question about audit trails, and I realized I had no idea if we even had one. The LaunchStudio review found that and two other issues I'd never have caught myself."

Selling to manufacturers? Get audited before their operations manager asks: https://launchstudio.eu/en/blog/ai-software-engineering-doetinchem

#AINativeFounder #LaunchStudio #Manifera #AIAudit #Doetinchem
