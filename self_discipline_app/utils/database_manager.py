import streamlit as st
from utils.data_handler import DataHandler
import os

class DatabaseManager:
    def __init__(self):
        self.personal_data_handler = DataHandler("data/personal_data.json")
        self.social_data_handler = DataHandler("data/social_data.json")
        self.study_materials_handler = DataHandler("data/study_materials.json")

    def manage_database(self):
        st.title("Database Management")
        category = st.selectbox("Select a Category", ["Personal Data", "Social Data", "Study Materials"])

        if category == "Personal Data":
            self.manage_personal_data()
        elif category == "Social Data":
            self.manage_social_data()
        elif category == "Study Materials":
            self.manage_study_materials()

    def manage_personal_data(self):
        st.header("Personal Data Management")
        data = self.personal_data_handler.read_data()
        selected_entry = st.selectbox("Select an Entry to Edit", list(data.keys()) + ["New Entry"])

        if selected_entry == "New Entry":
            self.add_personal_data_entry()
        else:
            self.update_or_delete_personal_data_entry(selected_entry, data[selected_entry])

    def add_personal_data_entry(self):
        entry_key = st.text_input("Entry Key")
        entry_value = st.text_area("Entry Value")
        tags = st.text_input("Tags (comma-separated)")

        if st.button("Add Entry"):
            entry = {
                "value": entry_value,
                "tags": tags.split(",")
            }
            self.personal_data_handler.create(entry_key, entry)
            st.success(f"Entry '{entry_key}' added successfully!")

    def update_or_delete_personal_data_entry(self, entry_key, entry):
        new_key = st.text_input("Entry Key", value=entry_key)
        new_value = st.text_area("Entry Value", value=entry['value'])
        new_tags = st.text_input("Tags (comma-separated)", value=",".join(entry['tags']))

        if st.button("Update Entry"):
            updated_entry = {
                "value": new_value,
                "tags": new_tags.split(",")
            }
            self.personal_data_handler.update(entry_key, updated_entry)
            st.success(f"Entry '{entry_key}' updated successfully!")

        if st.button("Delete Entry"):
            self.personal_data_handler.delete(entry_key)
            st.success(f"Entry '{entry_key}' deleted successfully!")

    def manage_social_data(self):
        st.header("Social Data Management")
        data = self.social_data_handler.read_data()
        selected_entry = st.selectbox("Select an Entry to Edit", list(data.keys()) + ["New Entry"])

        if selected_entry == "New Entry":
            self.add_social_data_entry()
        else:
            self.update_or_delete_social_data_entry(selected_entry, data[selected_entry])

    def add_social_data_entry(self):
        entry_key = st.text_input("Entry Key")
        entry_value = st.text_area("Entry Value")
        interaction_log = st.text_area("Interaction Log")

        if st.button("Add Entry"):
            entry = {
                "value": entry_value,
                "interaction_log": interaction_log
            }
            self.social_data_handler.create(entry_key, entry)
            st.success(f"Entry '{entry_key}' added successfully!")

    def update_or_delete_social_data_entry(self, entry_key, entry):
        new_key = st.text_input("Entry Key", value=entry_key)
        new_value = st.text_area("Entry Value", value=entry['value'])
        new_interaction_log = st.text_area("Interaction Log", value=entry['interaction_log'])

        if st.button("Update Entry"):
            updated_entry = {
                "value": new_value,
                "interaction_log": new_interaction_log
            }
            self.social_data_handler.update(entry_key, updated_entry)
            st.success(f"Entry '{entry_key}' updated successfully!")

        if st.button("Delete Entry"):
            self.social_data_handler.delete(entry_key)
            st.success(f"Entry '{entry_key}' deleted successfully!")

    def manage_study_materials(self):
        st.header("Study Materials Management")
        data = self.study_materials_handler.read_data()
        selected_entry = st.selectbox("Select an Entry to Edit", list(data.keys()) + ["New Entry"])

        if selected_entry == "New Entry":
            self.add_study_materials_entry()
        else:
            self.update_or_delete_study_materials_entry(selected_entry, data[selected_entry])

    def add_study_materials_entry(self):
        entry_key = st.text_input("Entry Key")
        entry_value = st.text_area("Entry Value")
        tags = st.text_input("Tags (comma-separated)")
        file = st.file_uploader("Upload File", type=["pdf", "png", "jpg", "jpeg"])

        if st.button("Add Entry"):
            entry = {
                "value": entry_value,
                "tags": tags.split(","),
                "file": file.name if file else None
            }
            if file:
                file_path = os.path.join("data/uploads", file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                entry["file_path"] = file_path
            self.study_materials_handler.create(entry_key, entry)
            st.success(f"Entry '{entry_key}' added successfully!")

    def update_or_delete_study_materials_entry(self, entry_key, entry):
        new_key = st.text_input("Entry Key", value=entry_key)
        new_value = st.text_area("Entry Value", value=entry['value'])
        new_tags = st.text_input("Tags (comma-separated)", value=",".join(entry['tags']))
        new_file = st.file_uploader("Upload File", type=["pdf", "png", "jpg", "jpeg"])

        if st.button("Update Entry"):
            updated_entry = {
                "value": new_value,
                "tags": new_tags.split(","),
                "file": new_file.name if new_file else entry['file']
            }
            if new_file:
                file_path = os.path.join("data/uploads", new_file.name)
                with open(file_path, "wb") as f:
                    f.write(new_file.getbuffer())
                updated_entry["file_path"] = file_path
            self.study_materials_handler.update(entry_key, updated_entry)
            st.success(f"Entry '{entry_key}' updated successfully!")

        if st.button("Delete Entry"):
            self.study_materials_handler.delete(entry_key)
            st.success(f"Entry '{entry_key}' deleted successfully!")