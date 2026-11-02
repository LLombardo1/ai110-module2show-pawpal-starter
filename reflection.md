# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial design uses Owner, Pet, Task, and Scheduler classes. A user can add a pet, add a care task, and view today's schedule. Owner stores pets, Pet stores tasks, Task stores care details, and Scheduler creates the daily plan.

**b. Design changes**

The design changed when I added task frequency, due date, and completion status. These details were needed for recurring tasks and filtering completed tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time, duration, priority, due date, and completion status. Priority and available time matter most because important tasks should fit into the day.

**b. Tradeoffs**

The scheduler will check for tasks at the exact same time instead of checking every possible overlap. This is simple and useful for a basic pet care planner.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to create the class design, build the scheduling methods, connect the Streamlit app, and write tests. Questions about sorting tasks, recurring tasks, and test cases were helpful.

**b. Judgment and verification**

I did not use a more complex conflict system that checks every overlapping duration. I used exact matching times because it was easier to read and matched the project requirement. I verified the result with a test and the CLI demo.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, adding a task to a pet, sorting by time, daily recurrence, and conflict detection. These tests are important because they check the main scheduler behaviors.

**b. Confidence**

I am confident that the main scheduler features work because five tests pass. Next, I would test an empty task list, a weekly recurring task, and tasks that overlap but do not start at the same time.

---

## 5. Reflection

**a. What went well**

I am most satisfied with building a working scheduler and showing the plan in both the CLI demo and Streamlit app.

**b. What you would improve**

In another iteration, I would let users edit and remove tasks and improve conflict detection for overlapping durations.

**c. Key takeaway**

I learned that planning classes before writing code makes the system easier to build. AI can help with ideas and code, but I need to test and review the results.
