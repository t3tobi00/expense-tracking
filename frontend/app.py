import streamlit as st
from form_tab import form_tab
from analytics_tab import analytics_tab

API_URL = "http://localhost:8000"

st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    form_tab()
    
with tab2:
    analytics_tab()