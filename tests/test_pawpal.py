from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def test_mark_complete_changes_task_status():
    task = Task("Breakfast", "08:00", 10)

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "dog")

    pet.add_task(Task("Walk", "08:00", 20))

    assert len(pet.tasks) == 1


def test_sort_by_time_returns_tasks_in_order():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)
    pet.add_task(Task("Walk", "09:00", 20))
    pet.add_task(Task("Breakfast", "07:30", 10))

    tasks = Scheduler(owner).sort_by_time(Scheduler(owner).get_tasks())

    assert [task.title for _, task in tasks] == ["Breakfast", "Walk"]


def test_daily_task_creates_next_occurrence_when_completed():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)
    pet.add_task(Task("Medicine", "08:00", 5, frequency="daily"))

    next_task = Scheduler(owner).mark_task_complete("Mochi", "Medicine")

    assert pet.tasks[0].completed is True
    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(days=1)


def test_find_conflicts_flags_matching_times():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)
    pet.add_task(Task("Walk", "08:00", 20))
    pet.add_task(Task("Breakfast", "08:00", 10))

    conflicts = Scheduler(owner).find_conflicts()

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]