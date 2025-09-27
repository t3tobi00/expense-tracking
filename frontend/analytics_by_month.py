import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

def analytics_by_month():
    response = requests.post(f"{API_URL}/analytics/monthly/")
    if response.status_code == 200:
        data = response.json()
        if not data:
            st.info("No monthly expense data available.")
            return
        
        df = pd.DataFrame(data)
        
        st.title("Monthly Expense Analytics")

        # Convert total to numeric
        df["total"] = pd.to_numeric(df["total"])
        
        # Create a datetime column for proper sorting
        df['month_date'] = pd.to_datetime(df['month'], format='%B %Y')
        
        # Sort by month chronologically
        df_sorted = df.sort_values(by="month_date", ascending=True)

        # Create plotly bar chart with chronological order
        fig = px.bar(df_sorted, x="month", y="total", title="Monthly Expenses")
        fig.update_xaxes(categoryorder='array', categoryarray=df_sorted["month"].tolist())
        st.plotly_chart(fig, use_container_width=True)
        
        # Display formatted table (using original df for display)
        df_display = df_sorted.copy()
        df_display["Total"] = df_display["total"].map(lambda x: f"${x:,.2f}")
        df_display = df_display.drop(columns=["total", "month_date"])
        st.table(df_display)
    else:
        st.error("Error fetching monthly analytics")