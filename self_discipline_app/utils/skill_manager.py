import streamlit as st
from utils.data_handler import DataHandler

class SkillManager:
    def __init__(self):
        self.data_handler = DataHandler("data/skills.json")

    def manage_skills(self):
        st.title("Skill Management")
        skills = self.data_handler.read_data()
        selected_skill = st.selectbox("Select a Skill to Edit", list(skills.keys()) + ["New Skill"])

        if selected_skill == "New Skill":
            self.add_skill()
        else:
            self.update_or_delete_skill(selected_skill, skills[selected_skill])

    def add_skill(self):
        skill_name = st.text_input("Skill Name")
        skill_description = st.text_area("Description")
        skill_level = st.slider("Level", 1, 100, 1)
        skill_xp = st.number_input("XP", 0, 1000, 0)

        if st.button("Add Skill"):
            skill = {
                "name": skill_name,
                "description": skill_description,
                "level": skill_level,
                "xp": skill_xp
            }
            self.data_handler.create(skill_name, skill)
            st.success(f"Skill '{skill_name}' added successfully!")

    def update_or_delete_skill(self, skill_name, skill):
        new_name = st.text_input("Skill Name", value=skill_name)
        description = st.text_area("Description", value=skill['description'])
        level = st.slider("Level", 1, 100, value=skill['level'])
        xp = st.number_input("XP", 0, 1000, value=skill['xp'])

        if st.button("Update Skill"):
            updated_skill = {
                "name": new_name,
                "description": description,
                "level": level,
                "xp": xp
            }
            self.data_handler.update(skill_name, updated_skill)
            st.success(f"Skill '{skill_name}' updated successfully!")

        if st.button("Delete Skill"):
            self.data_handler.delete(skill_name)
            st.success(f"Skill '{skill_name}' deleted successfully!")