import streamlit as st

st.title("🔐 Login to CompeteBot")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        st.success(f"Welcome, {username}!")
        st.page_link("pages/2_Comparison_Dashboard.py", label="➡ Go to Dashboard", icon="📊")
    else:
        st.error("Please enter both username and password.")