import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def form_tab():
    selected_date = st.date_input("Enter Date", datetime(2024,8,1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        data = response.json()
        # st.write(data)
    else:
        st.error("Error fetching data")
        data = []

    categories = data and list(set(item["category"] for item in data)) or ["Food", "Transport", "Utilities", "Entertainment", "Other", "Rent", "Health"]

    with st.form("expense_form"):
        col1, col2, col3 = st.columns(3)
        # text label for each column
        with col1:
                st.text("Amount")
        with col2:
                st.text("Category")
        with col3:
                st.text("Notes")

        expenses = []

        for i in range(5):

            if i < len(data):
                amount = data[i]["amount"]
                category = data[i]["category"]
                notes = data[i]["notes"]
            else:
                amount = 0.0
                category = categories[0]
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(f"Amount {i+1}", min_value=0.0, value=amount, step=1.0, key=f"amount_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category), key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submitted = st.form_submit_button("Submit")
        if submitted:
            filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]
            requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses added/updated successfully")
            else:
                st.error("Error adding/updating expenses")