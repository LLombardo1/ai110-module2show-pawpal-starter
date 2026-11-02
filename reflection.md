# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- I used four classes: Owner, Pet, Task, and Scheduler.
- The Owner stores the pets, and each Pet stores its own tasks.
- The Task class stores the task name, time, duration, priority, and frequency.
- The Scheduler is the main part of the system because it sorts tasks and creates the daily plan.
- A user can add a pet, add a care task, and view the daily schedule.

**b. Design changes**

- I added task frequency, due date, and completion status.
- These changes were needed because a recurring task has to know when it happens again.
- Completion status also lets the scheduler avoid showing finished tasks in the daily plan.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler looks at the task time, duration, priority, due date, and completion status.
- Priority matters most because important pet care tasks should be handled first.
- Available time also matters because the plan should only include tasks that fit into the day.

**b. Tradeoffs**

- The scheduler checks for tasks that start at the exact same time.
- It does not check every possible overlap between task durations.
- This was a reasonable choice because it keeps the system simple and still gives the user a warning.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI to brainstorm the class design and understand the scheduling requirements.
- The most helpful questions were about sorting tasks by time, handling recurring tasks, and understanding test cases.
- I used the suggestions as a starting point and chose the parts that matched the project requirements.

**b. Judgment and verification**

- I decided not to use a more complex conflict system that checks every overlapping duration.
- I kept exact matching times because the code was easier to read and matched the project requirement.
- I reviewed the code, ran the CLI demo, and checked the conflict detection test before keeping the final version.

---

## 4. Testing and Verification

**a. What you tested**

- I tested task completion, task addition, sorting by time, daily recurrence, and conflict detection.
- These tests were important because they check the main parts of the scheduler.

**b. Confidence**

- I am confident that the main scheduler features work because all five tests pass.
- I would test an empty task list next.
- I would also test a weekly recurring task and tasks that overlap without starting at the same time.

---

## 5. Reflection

**a. What went well**

- I am most satisfied with building a working scheduler.
- I also like that the plan can be seen in both the CLI demo and the Streamlit app.

**b. What you would improve**

- I would add a way for users to edit and remove tasks.
- I would also improve conflict detection so it checks overlapping task durations.

**c. Key takeaway**

- I learned that planning the classes first makes the system easier to build.
- AI can help with ideas and code, but I still need to test and review the results.
