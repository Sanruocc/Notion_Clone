import streamlit as st
from utils.data_handler import DataHandler

class TaskManager:
    def __init__(self):
        self.data_handler = DataHandler("data/tasks.json")

    def manage_tasks(self):
        st.title("Task Management")
        tasks = self.data_handler.read_data()
        selected_task = st.selectbox("Select a Task to Edit", list(tasks.keys()) + ["New Task"])

        if selected_task == "New Task":
            self.add_task()
        else:
            self.update_or_delete_task(selected_task, tasks[selected_task])

    def add_task(self):
        task_name = st.text_input("Task Name")
        task_description = st.text_area("Description")
        task_due_date = st.date_input("Due Date")
        associated_skill = st.selectbox("Associated Skill", ["Skill1", "Skill2"])

        if st.button("Add Task"):
            task = {
                "name": task_name,
                "description": task_description,
                "due_date": str(task_due_date),
                "associated_skill": associated_skill,
                "completed": False
            }
            self.data_handler.create(task_name, task)
            st.success(f"Task '{task_name}' added successfully!")

    def update_or_delete_task(self, task_name, task):
        new_name = st.text_input("Task Name", value=task_name)
        description = st.text_area("Description", value=task['description'])
        due_date = st.date_input("Due Date", value=task['due_date'])
        associated_skill = st.selectbox("Associated Skill", ["Skill1", "Skill2"], index=["Skill1", "Skill2"].index(task['associated_skill']))
        completed = st.checkbox("Completed", value=task['completed'])

        if st.button("Update Task"):
            updated_task = {
                "name": new_name,
                "description": description,
                "due_date": str(due_date),
                "associated_skill": associated_skill,
                "completed": completed
            }
            self.data_handler.update(task_name, updated_task)
            st.success(f"Task '{task_name}' updated successfully!")

        if st.button("Delete Task"):
            self.data_handler.delete(task_name)
            st.success(f"Task '{task_name}' deleted successfully!")