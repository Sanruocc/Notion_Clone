import streamlit as st
from utils.data_handler import DataHandler

class DatabaseManager:
    def __init__(self):
        self.data_handler = DataHandler("data/database.json")

    def manage_database(self):
        st.title("Database Management")
        data = self.data_handler.read_data()
        categories = list(data.keys())
        selected_category = st.selectbox("Select a Category to Edit", categories + ["New Category"])

        if selected_category == "New Category":
            self.add_category()
        else:
            self.update_or_delete_category(selected_category, data[selected_category])

    def add_category(self):
        category_name = st.text_input("Category Name")
        category_data = st.text_area("Category Data")

        if st.button("Add Category"):
            self.data_handler.create(category_name, category_data)
            st.success(f"Category '{category_name}' added successfully!")

    def update_or_delete_category(self, category_name, category_data):
        new_name = st.text_input("Category Name", value=category_name)
        new_data = st.text_area("Category Data", value=category_data)

        if st.button("Update Category"):
            self.data_handler.update(category_name, new_data)
            st.success(f"Category '{category_name}' updated successfully!")

        if st.button("Delete Category"):
            self.data_handler.delete(category_name)
            st.success(f"Category '{category_name}' deleted successfully!")