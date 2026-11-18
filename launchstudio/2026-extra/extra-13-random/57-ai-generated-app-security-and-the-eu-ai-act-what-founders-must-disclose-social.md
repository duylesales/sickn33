⚖️ Same app, one extra button. Two very different products.

                         THE CV COACH (existing)           THE CV SCREENER (planned)
Who uses it              Job seekers                       Recruitment agencies
What it does             Feedback on improving your CV     Upload fifty CVs, get them ranked
                         for a vacancy
Under the EU AI Act      A candidate-facing coaching tool  Likely high-risk recruitment AI,
                                                           with substantial obligations

Emre Yilmaz, a career coach in Nieuwegein, built CVcoach in Lovable with OpenAI's API. About 3,000 job seekers used the coach. Emre planned the screener next. Before building it, he asked LaunchStudio to review the app and the plan.

The review also found gaps in the coach itself:
• The chat didn't clearly say it was an AI
• The privacy notice didn't mention OpenAI as a processor, or explain data retention
• Full CVs, photos and dates of birth included, were sent to the model, when only experience and skills were needed
• Uploaded vacancy texts could carry prompt injections that altered the feedback
• Chat logs with full CVs were kept forever

What LaunchStudio changed (7 business days, €2,000):
✓ A clear AI disclosure in the chat
✓ Photos, birth dates and contact details stripped from CVs before anything reaches the model
✓ Vacancy and CV content delimited as untrusted data in prompts, and outputs sanitised
✓ 30-day retention on chat logs
✓ An accurate processor list for Emre's updated privacy notice

And the screener? With legal advice, Emre postponed it. Instead, he built an employer-facing tool that helps recruiters write inclusive vacancy texts.

CVcoach grew to 7,500 users in six months. Two university career services adopted it after reviewing its privacy and AI disclosures. And Emre avoided building a high-risk system his small company wasn't ready to run.

"The coaching tool and the ranking tool looked like the same app with one extra button. Legally and ethically, they were completely different products." - Emre Yilmaz

https://launchstudio.eu/en/blog/ai-generated-app-security-and-the-eu-ai-act-what-founders-must-disclose

#EUAIAct #AITransparency #GDPR #HRTech #LaunchStudio #Manifera
