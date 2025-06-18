import streamlit as st
import pandas as pd
import plotly.express as px
import os
from io import BytesIO

# Page config
st.set_page_config(page_title="AI Personal Finance Coach", layout="centered")
st.title("💰 AI Personal Finance Coach")
st.subheader("Track your budget and get AI-powered financial advice")

# User input
st.header("Step 1: Enter Your Monthly Income & Expenses")

income = st.number_input("Monthly Income ($)", min_value=0.0, value=4000.0)

st.markdown("### Fixed Expenses")
rent = st.number_input("🏠 Rent / Mortgage", min_value=0.0, value=1200.0)
utilities = st.number_input("💡 Utilities", min_value=0.0, value=150.0)
subscriptions = st.number_input("💼 Subscriptions", min_value=0.0, value=50.0)

st.markdown("### Variable Expenses")
groceries = st.number_input("🛍️ Groceries", min_value=0.0, value=400.0)
transport = st.number_input("🚗 Transportation", min_value=0.0, value=200.0)
entertainment = st.number_input("🎉 Entertainment", min_value=0.0, value=150.0)
others = st.number_input("📟 Other Expenses", min_value=0.0, value=100.0)

# Calculations
total_expenses = rent + utilities + subscriptions + groceries + transport + entertainment + others
savings = income - total_expenses
savings_rate = (savings / income * 100) if income > 0 else 0

# Summary
st.header("📊 Monthly Summary")
st.metric("Total Income", f"${income:,.2f}")
st.metric("Total Expenses", f"${total_expenses:,.2f}")
st.metric("Estimated Savings", f"${savings:,.2f}")
st.metric("Savings Rate", f"{savings_rate:.1f}%")

# Chart
data = {
    "Category": ["Rent", "Utilities", "Subscriptions", "Groceries", "Transport", "Entertainment", "Others", "Savings"],
    "Amount": [rent, utilities, subscriptions, groceries, transport, entertainment, others, savings]
}
df = pd.DataFrame(data)
fig = px.pie(df, values="Amount", names="Category", title="💸 Expense Breakdown")
st.plotly_chart(fig, use_container_width=True)

# Export to CSV
csv_buffer = BytesIO()
df.to_csv(csv_buffer, index=False)
st.download_button("📁 Download Budget CSV", csv_buffer.getvalue(), "budget_summary.csv", "text/csv")

# Generate prompt for ChatGPT Free
prompt = f"""
I earn ${income} per month. My expenses are:
- Rent: ${rent}
- Utilities: ${utilities}
- Subscriptions: ${subscriptions}
- Groceries: ${groceries}
- Transportation: ${transport}
- Entertainment: ${entertainment}
- Others: ${others}

My total expenses are ${total_expenses} and I save around ${savings} monthly.

Give me personalized budgeting advice in a friendly tone. Be concise and helpful.
"""

st.markdown("### 🧠 Copy This Prompt for ChatGPT")
st.text_area("Prompt", prompt, height=200)
st.markdown("➡️ Go to [chat.openai.com](https://chat.openai.com), paste the prompt, and get your advice.")
