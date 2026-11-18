🎫 BOARDING PASS
Harlingen ➜ Wadden Islands
Ticket no. 10001

Ticket no. 10002
Ticket no. 10003
Ticket no. 10004...

See the problem?

Wouter Zijlstra built EilandGo in Bolt, ahead of the summer tourist season: ferry ticket booking and island travel planning for tourists heading from Harlingen to the Wadden Islands. Every confirmation included a QR code tied to a simple, sequentially generated ticket number.

During a pre-launch risk assessment, LaunchStudio's engineers spotted it. Take one real ticket number, count up, and you land on a valid, unused ticket. Someone could plausibly generate a fraudulent boarding pass without ever paying. That hurts EilandGo's revenue and undermines the ferry operator's boarding controls at the same time.

(The ticket numbers above are illustrative. The pattern was real.)

What changed before the first full season (4 business days, €830):
⚓ Sequential numbers replaced with cryptographically random, unpredictable identifiers
⚓ Server-side verification against the actual payment record at boarding
⚓ Boarding validation that checks the payment, not just the QR code

The result: EilandGo now issues tickets that can't be predicted or forged, verified against real payment records at the point of boarding.

"I never thought about ticket numbers as a security risk. LaunchStudio explained exactly how someone could have exploited it, and fixed it before our busiest season started." - Wouter Zijlstra

Are your IDs guessable? https://launchstudio.eu/en/blog/ai-security-risk-harlingen

#AINativeFounder #LaunchStudio #Manifera #AISecurityRisk #Harlingen
