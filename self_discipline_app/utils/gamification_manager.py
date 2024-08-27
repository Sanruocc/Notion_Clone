import streamlit as st
from utils.data_handler import DataHandler

class GamificationManager:
    def __init__(self):
        self.achievement_handler = DataHandler("data/achievements.json")
        self.badge_handler = DataHandler("data/badges.json")

    def display_gamification_dashboard(self):
        st.title("Gamification Dashboard")
        self.display_achievements()
        self.display_badges()

    def display_achievements(self):
        st.header("Achievements")
        achievements = self.achievement_handler.read_data()
        for achievement in achievements.values():
            st.subheader(achievement['name'])
            st.write(achievement['description'])
            st.progress(achievement['progress'])
            if achievement['unlocked']:
                st.success("Unlocked!")

    def display_badges(self):
        st.header("Badges")
        badges = self.badge_handler.read_data()
        for badge in badges.values():
            st.subheader(badge['name'])
            st.write(badge['description'])
            if badge['earned']:
                st.success("Earned!")