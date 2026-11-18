A team lead at a client company mentioned, in passing, a colleague's salary. The colleague worked in a different department. 💼

Laura Timmermans, an HR consultant in Ede, built Verlofbord with Cursor: a portal where small and medium-sized companies manage leave requests, sick-leave reports and payslip distribution, with manager approvals. Fourteen companies, 850 employees in total. That one remark started a review.

Three lessons from what it found.

LESSON 1: "Same company" is not the same as "should see it."
Every user with the manager role could query every employee in their company, salaries and bank details included, because the API only filtered by company.
➜ A role matrix enforced with row-level policies, manager scope derived from reporting lines, and salary and bank data in a separate table visible only to HR and payroll roles.

LESSON 2: A free-text field collects whatever people type into it.
The sick-leave form had a "reason" field, and employees had entered diagnoses.
➜ The field removed, existing entries deleted after the client companies were informed. The form now records only dates and availability.

LESSON 3: People leave, and access should leave with them.
Payslips sat in a public bucket with predictable names. There was no access log. Employees who'd left six months earlier still had active accounts, and managers kept access to former reports.
➜ Payslips in private storage with signed links and random identifiers, an access log for sensitive categories, offboarding tied to contract end dates, and automated tests that try forbidden access for every role and tenant on every deployment.

The work took 10 business days, for €3,100. Laura informed her clients transparently. None left, and two named the response as a reason to stay. Verlofbord has since grown to 23 companies, and the forbidden-access tests have blocked one regression from a later Cursor edit.

"I built the tool to make HR easier for small companies. I nearly made it the reason one of them had the worst week in its history." - Laura Timmermans

https://launchstudio.eu/en/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access

#HRTech #DataProtection #Cursor #AccessControl #LaunchStudio #Manifera
