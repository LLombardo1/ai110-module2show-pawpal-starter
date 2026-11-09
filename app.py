import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

st.subheader("Owner and Pet")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_time = st.text_input("Time", value="08:00")
with col3:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col4:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add task"):
    pet = next((pet for pet in st.session_state.owner.pets if pet.name == pet_name), None)
    if pet is None:
        pet = Pet(pet_name, species)
        st.session_state.owner.add_pet(pet)
    pet.add_task(Task(task_title, task_time, int(duration), priority, frequency))
    st.success("Task added.")

schedule = Scheduler(st.session_state.owner)
tasks = schedule.sort_by_time(schedule.get_tasks())
if tasks:
    st.write("Current tasks:")
    st.table(
        [
            {
                "Pet": pet.name,
                "Task": task.title,
                "Time": task.time,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
                "Frequency": task.frequency,
                "Completed": task.completed,
            }
            for pet, task in tasks
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

if tasks:
    st.subheader("Edit Task")
    selected_task = st.selectbox(
        "Choose a task",
        tasks,
        format_func=lambda item: f"{item[0].name} - {item[1].title} at {item[1].time}",
    )
    pet, task = selected_task
    with st.form("edit_task"):
        edited_title = st.text_input("Task title", value=task.title, key="edit_title")
        edited_time = st.text_input("Time", value=task.time, key="edit_time")
        edited_duration = st.number_input(
            "Duration (minutes)", min_value=1, max_value=240,
            value=task.duration_minutes, key="edit_duration"
        )
        edited_priority = st.selectbox(
            "Priority", ["low", "medium", "high"],
            index=["low", "medium", "high"].index(task.priority), key="edit_priority"
        )
        edited_frequency = st.selectbox(
            "Frequency", ["once", "daily", "weekly"],
            index=["once", "daily", "weekly"].index(task.frequency), key="edit_frequency"
        )
        if st.form_submit_button("Save changes"):
            task.title = edited_title
            task.time = edited_time
            task.duration_minutes = int(edited_duration)
            task.priority = edited_priority
            task.frequency = edited_frequency
            st.success("Task updated.")

st.divider()

st.subheader("Today's Schedule")
available_minutes = st.number_input("Available minutes", min_value=1, max_value=1440, value=60)

if st.button("Generate schedule"):
    plan = schedule.build_daily_plan(int(available_minutes))
    if plan:
        st.table(
            [
                {
                    "Time": task.time,
                    "Pet": pet.name,
                    "Task": task.title,
                    "Duration": task.duration_minutes,
                    "Priority": task.priority,
                }
                for pet, task in plan
            ]
        )
    else:
        st.info("No incomplete tasks fit in the available time.")
    for warning in schedule.find_conflicts():
        st.warning(warning)
