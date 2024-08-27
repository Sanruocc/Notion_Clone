import streamlit as st
from utils.skill_manager import SkillManager
from utils.task_manager import TaskManager
from utils.gamification_manager import GamificationManager
from utils.dashboard_manager import DashboardManager
from utils.database_manager import DatabaseManager

st.set_page_config(page_title="Skills Management", layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Skills", "Tasks", "Gamification", "Database", "Settings"])

    if page == "Dashboard":
        dashboard_manager = DashboardManager()
        dashboard_manager.display_dashboard()
    elif page == "Skills":
        skill_manager = SkillManager()
        skill_manager.manage_skills()
    elif page == "Tasks":
        task_manager = TaskManager()
        task_manager.manage_tasks()
    elif page == "Gamification":
        gamification_manager = GamificationManager()
        gamification_manager.display_gamification_dashboard()
    elif page == "Database":
        database_manager = DatabaseManager()
        database_manager.manage_database()
    elif page == "Settings":
        st.title("Settings")
        theme = st.selectbox("Select Theme", ["Light", "Dark", "Custom"])
        if theme == "Custom":
            primary_color = st.color_picker("Primary Color")
            secondary_color = st.color_picker("Secondary Color")
            background_color = st.color_picker("Background Color")
            text_color = st.color_picker("Text Color")
            if st.button("Apply Custom Theme"):
                custom_theme = f"""
                <style>
                :root {{
                    --primary-color: {primary_color};
                    --secondary-color: {secondary_color};
                    --background-color: {background_color};
                    --text-color: {text_color};
                }}
                </style>
                """
                st.markdown(custom_theme, unsafe_allow_html=True)
                st.success("Custom theme applied successfully!")
            else:
                st.warning("Custom theme application failed.")
        else:
            if st.button("Apply Theme"):
                if theme == "Light":
                    st.markdown(get_light_theme(), unsafe_allow_html=True)
                    st.success("Light theme applied successfully!")
                elif theme == "Dark":
                    st.markdown(get_dark_theme(), unsafe_allow_html=True)
                    st.success("Dark theme applied successfully!")
                else:
                    st.warning("Theme application failed.")

def get_light_theme():
    return """
    <style>
    :root {
        --primary-color: #ffffff;
        --secondary-color: #000000;
        --background-color: #f0f2f6;
        --text-color: #31333f;
    }
    </style>
    """

def get_dark_theme():
    return """
    <style>
    :root {
        --primary-color: #31333f;
        --secondary-color: #ffffff;
        --background-color: #262730;
        --text-color: #f0f2f6;
    }
    </style>
    """

if __name__ == "__main__":
    main()