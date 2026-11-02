from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner("Jordan")
    mochi = Pet("Mochi", "dog")
    luna = Pet("Luna", "cat")
    owner.add_pet(mochi)
    owner.add_pet(luna)

    mochi.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    mochi.add_task(Task("Breakfast", "07:30", 10, "high", "daily"))
    luna.add_task(Task("Play time", "08:00", 15, "medium"))

    scheduler = Scheduler(owner)
    print(f"Today's Schedule for {owner.name}:")
    for pet, task in scheduler.build_daily_plan(60):
        print(f"{task.time} - {pet.name}: {task.title} ({task.duration_minutes} min) [{task.priority}]")

    for warning in scheduler.find_conflicts():
        print(warning)


if __name__ == "__main__":
    main()