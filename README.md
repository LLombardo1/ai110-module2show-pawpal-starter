# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule for Jordan:
07:30 - Mochi: Breakfast (10 min) [high]
08:00 - Mochi: Morning walk (30 min) [high]
08:00 - Luna: Play time (15 min) [medium]
Conflict: Mochi's Morning walk and Luna's Play time are both at 08:00.
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
tests/test_pawpal.py .....

5 passed
```

- Tests cover task completion, task addition, sorting by time, daily recurrence, and conflict detection.

## 📐 Smarter Scheduling

- Task sorting: `Scheduler.sort_by_time()` sorts tasks in HH:MM time order.
- Filtering: `Scheduler.get_tasks()` filters tasks by pet name or completion status.
- Conflict handling: `Scheduler.find_conflicts()` warns when incomplete tasks have the same date and time.
- Recurring tasks: `Task.next_occurrence()` creates the next daily or weekly task when a task is completed.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

- Open the PawPal+ app in Streamlit.
- Enter the owner name, pet name, and species.
- Enter a task title, time, duration, priority, and frequency.
- Select Add task to add the task to the pet.
- View the time-sorted task list.
- Enter available minutes and select Generate schedule.
- View the daily plan and any conflict warnings.

- **Screenshot or video** *(optional)*: Not included.
