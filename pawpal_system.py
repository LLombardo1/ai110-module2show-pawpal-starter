from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    time: str
    duration_minutes: int
    priority: str = "medium"
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.completed = True

    def next_occurrence(self) -> "Task | None":
        """Create the next daily or weekly occurrence."""
        days = {"daily": 1, "weekly": 7}
        if self.frequency not in days:
            return None
        return Task(
            self.title,
            self.time,
            self.duration_minutes,
            self.priority,
            self.frequency,
            False,
            self.due_date + timedelta(days=days[self.frequency]),
        )


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task for this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_tasks(self, pet_name: str | None = None, completed: bool | None = None) -> list[tuple[Pet, Task]]:
        """Return tasks filtered by pet name or completion status."""
        tasks = []
        for pet in self.owner.pets:
            if pet_name is not None and pet.name != pet_name:
                continue
            for task in pet.tasks:
                if completed is None or task.completed == completed:
                    tasks.append((pet, task))
        return tasks

    def sort_by_time(self, tasks: list[tuple[Pet, Task]]) -> list[tuple[Pet, Task]]:
        """Return tasks in chronological order."""
        return sorted(tasks, key=lambda item: item[1].time)

    def build_daily_plan(self, available_minutes: int) -> list[tuple[Pet, Task]]:
        """Choose incomplete tasks that fit within the available time."""
        priorities = {"high": 0, "medium": 1, "low": 2}
        tasks = [
            item
            for item in self.get_tasks(completed=False)
            if item[1].due_date <= date.today()
        ]
        tasks.sort(key=lambda item: (priorities.get(item[1].priority, 1), item[1].time))

        plan = []
        minutes_used = 0
        for pet, task in tasks:
            if minutes_used + task.duration_minutes <= available_minutes:
                plan.append((pet, task))
                minutes_used += task.duration_minutes
        return self.sort_by_time(plan)

    def find_conflicts(self) -> list[str]:
        """Return warnings for incomplete tasks at the same time and date."""
        conflicts = []
        scheduled = {}
        for pet, task in self.get_tasks(completed=False):
            key = (task.due_date, task.time)
            if key in scheduled:
                other_pet, other_task = scheduled[key]
                conflicts.append(
                    f"Conflict: {other_pet.name}'s {other_task.title} and "
                    f"{pet.name}'s {task.title} are both at {task.time}."
                )
            else:
                scheduled[key] = (pet, task)
        return conflicts

    def mark_task_complete(self, pet_name: str, task_title: str) -> Task | None:
        """Complete a task and add its next recurring occurrence when needed."""
        for pet, task in self.get_tasks(pet_name=pet_name, completed=False):
            if task.title == task_title:
                task.mark_complete()
                next_task = task.next_occurrence()
                if next_task is not None:
                    pet.add_task(next_task)
                return next_task
        return None