📢 CONGRATULATIONS ON YOUR PROMOTION!

You are now a manager in ShiftHub. You can view your coworkers' shift and pay data.

How did you earn it? You edited one value in a request your browser sends.

(Nobody ever received this announcement. But before LaunchStudio's security review, anyone could have promoted themselves.)

Sietse Postma built ShiftHub in v0: a shift-scheduling app for manufacturing employers around Drachten, piloted at the request of his own former employer. Managers use it to view payroll-adjacent shift data for their teams.

The security review found that a user's role, employee or manager, was read straight from a value sent by the browser. It was never verified against the database. So any regular employee could modify a request and grant themselves manager-level access.

How the self-promotion path was closed (4 business days, €740):
✔ Every role check now happens server-side, against verified account data
✔ Nothing the client sends is trusted for permissions
✔ Logging flags any future attempt at privilege escalation

The result: role-based access enforced entirely on the server, closed before it reached any live manufacturing client.

"I had no idea someone could just edit a request and become a manager in my own app. LaunchStudio found it before I signed my first real employer client." - Sietse Postma

In your app, who decides roles: the server or the browser? https://launchstudio.eu/en/blog/ai-security-issues-drachten

#AINativeFounder #LaunchStudio #Manifera #AISecurityIssues #Drachten
