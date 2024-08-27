from utils.data_handler import DataHandler

class GoalManager:
    def __init__(self):
        self.data_handler = DataHandler("data/goals.json")

    def add_goal(self, name, description, deadline):
        goal = {
            "name": name,
            "description": description,
            "deadline": deadline,
            "sub_tasks": [],
            "completed": False
        }
        self.data_handler.create(name, goal)

    def get_goals(self):
        goals = self.data_handler.read_data()
        return list(goals.values()) if goals else []

    def calculate_progress(self, name):
        goal = self.data_handler.read(name)
        if goal:
            total_tasks = len(goal["sub_tasks"])
            completed_tasks = sum(1 for task in goal["sub_tasks"] if task["completed"])
            return completed_tasks / total_tasks if total_tasks else 0
        return 0

    def complete_goal(self, name):
        goal = self.data_handler.read(name)
        if goal:
            goal["completed"] = True
            self.data_handler.update(name, goal)