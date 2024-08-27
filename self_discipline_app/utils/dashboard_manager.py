import streamlit as st
from utils.skill_manager import SkillManager
from utils.task_manager import TaskManager
from utils.gamification_manager import GamificationManager

class DashboardManager:
    def __init__(self):
        self.skill_manager = SkillManager()
        self.task_manager = TaskManager()
        self.gamification_manager = GamificationManager()

    def display_dashboard(self):
        st.title("Dashboard")
        self.display_skills()
        self.display_tasks()
        self.display_gamification()

    def display_skills(self):
        st.header("Skills")
        skills = self.skill_manager.data_handler.read_data()
        for skill in skills.values():
            st.subheader(skill['name'])
            st.write(skill['description'])
            st.progress(skill['xp'] / 1000)
            st.write(f"Level: {skill['level']}")

    def display_tasks(self):
        st.header("Tasks")
        tasks = self.task_manager.data_handler.read_data()
        for task in tasks.values():
            st.subheader(task['name'])
            st.write(task['description'])
            st.write(f"Due Date: {task['due_date']}")
            st.checkbox("Completed", value=task['completed'])

    def display_gamification(self):
        st.header("Gamification")
        self.gamification_manager.display_achievements()
        self.gamification_manager.display_badges()