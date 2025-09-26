import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1), key="start_date", label_visibility="collapsed")
    with col2:
        end_date = st.date_input("End Date", datetime(2024,8,31), key="end_date", label_visibility="collapsed")

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/", json=payload)
        if response.status_code == 200:
            data = response.json()
            if not data:
                st.info("No expenses found for the selected date range.")
                return
            data_formatted = {
                "Category": list(data.keys()),
                "Total": [data[cat]['total'] for cat in data],
                "Percentage": [data[cat]['percentage'] for cat in data]
            }
            df = pd.DataFrame(data_formatted)
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            st.title("Expense Analytics")

            st.bar_chart(data=df_sorted.set_index("Category")["Percentage"], width=0, height=0, use_container_width=True)
            
            df_sorted["Total"] = df_sorted["Total"].map("${:,.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)

            st.table(df_sorted)
        else:
            st.error("Error fetching analytics")