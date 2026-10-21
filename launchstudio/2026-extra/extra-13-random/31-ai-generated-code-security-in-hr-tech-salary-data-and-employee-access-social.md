🚨 Laura Timmermans, an HR consultant in Ede, built Verlofbord with Cursor: a portal for SMEs to manage leave, sick-leave reports and payslips, with manager approvals. Fourteen companies, 850 employees. Then a team lead at a client mentioned — in passing — the salary of a colleague in another department. 😳

Every user with the manager role could query every employee in the company, salaries and bank details included, because the API filtered only by company. The sick-leave form had a free-text "reason" field full of diagnoses. Payslips sat in a public bucket with predictable names, there was no access log, and people who'd left six months earlier still had active accounts. Here's what AI generated code security means in HR tech: 🧠

❌ "Manager" meaning "sees everyone"
❌ Salaries and bank details in the same query as names
❌ Diagnoses recorded by the employer
❌ Guessable payslip files, no read logging, no offboarding

✅ A role matrix enforced with row-level policies, manager scope derived from reporting lines
✅ Salary and bank data in a separate table for HR and payroll only
✅ The "reason" field removed — existing entries deleted after informing clients
✅ Private payslip storage with signed links, access logging, offboarding tied to contract end dates, and forbidden-access tests on every deploy

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and a security-rooted leadership, we model access explicitly and test it continuously. ⚙️

Her result: €3,100, ten business days. Clients were informed transparently and none left — two cited the response as a reason to stay. Verlofbord grew to 23 companies, and the tests have already blocked one regression from a later Cursor edit. 🚀

👉 AI generated code security in HR tech: salary data and employee access: https://launchstudio.eu/en/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access

#HRTech #DataProtection #Cursor #AccessControl #LaunchStudio #Manifera
