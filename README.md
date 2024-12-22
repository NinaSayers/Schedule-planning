# Schedule-planning
Final project of the subject Design and Analysis of Algorithms, 4th year of Computer Science, Faculty of Mathematics and Computing (MATCOM), University of Havana.

In this context, scheduling involves allocating limited resources (such as classrooms and teachers) to a set of activities (classes or exams) within a specific time frame. The goal is to create a schedule that minimizes conflicts (such as overlaps between classes) and maximizes efficient use of space and time. This problem presents multiple constraints, such as teacher availability and student preferences. Random conditions such as the possibility of missing classes due to events can also be considered.

## Computational Complexity of the Scheduling Problem
The scheduling problem belongs to the class of NP-hard problems. Broadly, this means that:
1. There is no known efficient (polynomial-time) algorithm that guarantees finding the optimal solution in all cases. "Efficient" here refers to the fact that the computation time does not grow explosively with the size of the problem.

2. Proposed solutions can be quickly verified. If a schedule is provided, it can be quickly checked if it satisfies all the constraints (for example, that there are no two classes in the same room at the same time, that a teacher is not assigned to two places at the same time, etc.).

## Why is it so necessary to solve it in practice?

The need to solve scheduling problems arises in a wide variety of everyday and business situations. Optimization in this area can lead to significant resource savings, improved efficiency, and increased satisfaction.

1. Education:
  •  School and university timetabling: Assigning classes to classrooms and teachers, minimizing conflicts and maximizing the use of resources.
  •  Exams: Ensuring that there are no schedule conflicts for students and optimizing the use of spaces.
  •  Tutoring and advising: Scheduling times so that students have access to help when they need it.

2. Transportation:
  •  Bus, train, and airplane schedules: Creating efficient routes that meet demand, minimizing delays and costs.
  •  Vehicle assignment to routes: Optimizing the use of the fleet.
  •  Delivery logistics: Planning delivery routes to maximize efficiency and reduce times.

3. Healthcare:
  •  Medical staff schedules: Ensuring adequate coverage in hospitals and clinics, considering specializations and staff preferences.
  •  Operating room bookings: Optimizing the use of expensive resources.
  •  Medical appointments: Scheduling appointments efficiently, avoiding queues, and maximizing the use of the doctor's time.

4. Production:
  •  Production planning in factories: Scheduling the manufacture of products on different machines, minimizing downtime and maximizing production.
  •  Project management: Assigning tasks to team members, considering task dependencies and deadlines.
  •  Equipment maintenance: Scheduling maintenance tasks efficiently, avoiding interruptions in production.

5. Events and conferences:
  •  Scheduling of lectures and workshops: Ensuring that there are no conflicts between sessions and maximizing attendance.
  •  Allocation of spaces for events: Optimizing the use of different venues.

### In short:

The beauty of the scheduling problem lies in its applicability. The same logic of resource allocation with constraints can be used for:

•  Staff scheduling: Assigning shifts to employees in different areas, considering the needs of each department and the preferences of the workers.
•  Project planning: Assigning resources (people, materials, equipment) to tasks in a project, considering deadlines and dependencies.
•  Supply chain optimization: Scheduling shipments, storage, and production in a logistics network.
•  Cloud resource management: Allocating computational resources to different users or applications based on demand and availability.