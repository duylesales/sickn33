Imagine you're a welder in Friesland, applying for a job through a recruitment platform. 🔧

You upload your CV. A checkbox says you'd like to join the talent pool. It was already ticked, and nobody stored that you ever saw it. An AI model scores your CV against the vacancy. Below 40%, you're moved to "rejected," and no human ever looks. Your CV sits in a public storage bucket, with a predictable file name. Every recruiter on the platform can search for you through the API. If parsing your CV fails, its full text gets written into an error log. And nothing is ever deleted.

That was Vakkracht, before a candidate complained.

Sophie Lambrecht, who had run a staffing agency for technical trades in Leeuwarden, built Vakkracht in Lovable: installation, welding and construction companies post vacancies, and an AI model matches CVs to requirements like certifications and driving licences. Twelve employers and two staffing agencies joined in the first quarter, and about 1,400 candidates applied.

What changed for the welder (LaunchStudio, 11 business days, €3,300):
✓ Only recruiters at the organisation you applied to can see you, enforced with Row Level Security
✓ Your CV in private storage, with signed links and malware scanning
✓ Your data deleted four weeks after the vacancy closes, or after twelve months if you explicitly join the talent pool
✓ An explicit, versioned consent record instead of a pre-ticked box, with one-click withdrawal
✓ No automatic rejection: low scores go to a recruiter review queue, with the match explanation shown
✓ CV text scrubbed from logs
✓ A tool to export or delete your data, embeddings included

Vakkracht notified affected candidates and the regulator, on advice, and received no further complaints. It then signed a regional staffing agency that had declined earlier over privacy concerns, and grew to 31 employers within six months.

"The matching was the clever part, and it was the part nobody worried about. Everyone worried about who could see the CVs - and they were right to." - Sophie Lambrecht

https://launchstudio.eu/en/blog/building-an-ai-recruitment-tool-ai-app-production-problems-with-cvs-and-consent

#Recruitment #HRTech #GDPR #EUAIAct #LaunchStudio #Manifera
