🧪 LAB NOTES: Can a homework app survive 20,000 students on a Monday?

SUBJECT
Huiswerkplanner, built by Karim Bouzid with Bolt and Supabase. Students see assignments, teachers post tasks, parents follow progress. A school board with 14 schools planned to roll it out to about 20,000 students at once, the Monday after the holidays.

KNOWN MAXIMUM SO FAR
About 300 people online at the same time.

EXPERIMENT 1
A load test simulating the morning peak: around 3,000 concurrent students opening their planner within ten minutes.
Observation: at about 600 concurrent users, the planner page went past five seconds and errors began.

DIAGNOSIS
• The planner loaded all assignments for the student's school and filtered in the browser
• Each assignment card made separate requests for subject and completion status
• The assignments policy checked class membership with a subquery per row, without indexes
• A realtime subscription on the whole assignments table pushed every change to every student

INTERVENTION (LaunchStudio, 11 business days, €4,600)
• Composite indexes for school, class and due date
• The policy rewritten with an indexed membership helper and (select auth.uid())
• A view returning a student's next two weeks of assignments, with subject and status, in one query
• Realtime narrowed to private channels per class, with broadcasts for new assignments
• Assignment images resized and cached
• One compute size up, after optimisation, because the test showed it was now the remaining limit

EXPERIMENT 2
5,000 concurrent users. 95th percentile under 700 milliseconds.

FIELD RESULT
On the Monday, around 11,000 students opened the app in the first hour, with peak concurrency near 2,800. Fast pages, no errors. The board extended the rollout to its primary schools' upper years the next term.

"The question wasn't whether Supabase could handle twenty thousand students. It was whether my queries could." - Karim Bouzid

https://launchstudio.eu/en/blog/how-many-users-can-a-supabase-app-handle

#Supabase #Bolt #Scalability #EdTech #AIFounder #LaunchStudio #Manifera
