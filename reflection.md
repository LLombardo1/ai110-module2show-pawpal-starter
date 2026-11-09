# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- I used four classes: Owner, Pet, Task, and Scheduler.
- Owner keeps track of pets.
- Pet keeps track of its tasks.
- Task stores the task details, like the time and priority.
- Scheduler puts the tasks in order and makes the daily plan.
- The user can add a pet, add a task, and see the schedule.

**b. Design changes**

- I added frequency, due date, and completed status to tasks.
- I needed these so daily and weekly tasks could repeat.
- Completed tasks do not show in the daily plan.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler looks at time, duration, priority, due date, and completion status.
- High-priority tasks are picked first.
- The plan only includes tasks that fit in the available time.

**b. Tradeoffs**

- The scheduler checks when two tasks have the exact same time.
- It does not check all task time overlaps.
- I kept it simple because it still gives the user a helpful warning.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI to help plan the classes and understand the project.
- AI was helpful for sorting tasks, recurring tasks, and tests.
- I used the suggestions, but I chose what made sense for my project.
- I used separate chats for design, coding, and testing so I could stay organized.

**b. Judgment and verification**

- I did not use a harder conflict system that checks every overlap.
- I kept matching times because it was easier to understand.
- I ran the CLI demo and checked the tests.

---

## 4. Testing and Verification

**a. What you tested**

- I tested completing a task, adding a task, sorting, daily tasks, and conflicts.
- These tests check the main parts of the scheduler.

**b. Confidence**

- I feel confident because the main tests pass.
- Next, I would test an empty task list.
- I would also test weekly tasks and more time overlaps.

---

## 5. Reflection

**a. What went well**

- I am happy that I made a working scheduler.
- I like that it works in the CLI and Streamlit app.

**b. What you would improve**

- I would add edit and remove task buttons.
- I would improve conflict checking for overlapping tasks.

**c. Key takeaway**

- I learned that planning classes first makes coding easier.
- AI can help, but I still need to test and check my work.
- I learned that I am the lead architect because I decide what to keep, change, and test.
