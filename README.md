# 💰 AI Personal Finance Coach

An intelligent and interactive budgeting assistant built with **Streamlit** and powered by **OpenAI GPT-3.5**. This app helps users manage monthly income, visualize spending, and receive **personalized AI budgeting tips** — all through a beautiful and responsive interface.

---

## 🎯 Project Overview

Budgeting is essential — but often overwhelming. The **AI Personal Finance Coach** simplifies it by:

- Taking user input for monthly income & categorized expenses
- Generating real-time summaries & savings reports
- Visualizing spending through interactive charts
- Producing smart, friendly budgeting advice using GPT
- Letting users **export reports** and **track history**

Perfect for individuals seeking a simple, tech-enabled way to take control of their personal finances.

---

## 🧠 Key Features

| Feature | Description |
|--------|-------------|
| 📥 **User Input** | Accepts fixed and variable expense entries via intuitive UI |
| 📊 **Analytics Dashboard** | Shows income, expense total, savings, and savings rate |
| 📈 **Interactive Visualization** | Dynamic pie chart using Plotly to break down spending |
| 🤖 **AI Advice** | GPT-3.5 analyzes budget and returns friendly, actionable suggestions |
| 💾 **Data Export** | One-click download of your budget summary as CSV |
| 🗂️ **Local History Logging** | Automatically logs budgets to a local CSV for tracking |

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **AI Integration**: OpenAI GPT-3.5
- **Environment**: Python 3.10+, dotenv

---

## 🚀 Live App

🟢 [Launch the App on Streamlit Cloud](https://btc-signal-dashboard-mjzbtqux9dkpghrzrrwtru.streamlit.app/)  
*(Replace with actual app link if different)*

---

## 🖥️ Local Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/MoisesSanchez2020/AI-Personal-Finance-Coach.git
cd AI-Personal-Finance-Coach

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add your OpenAI key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# 5. Run the app
streamlit run app.py


📦 File Structure

AI-Personal-Finance-Coach/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env                    # (Ignored) Holds your OpenAI key
├── budget_history.csv      # App-generated history log
└── README.md               # You are here

📤 Example Prompt Sent to GPT
I earn $4000 per month. My expenses are:

Rent: $1200

Utilities: $150

Subscriptions: $50

Groceries: $400

Transportation: $200

Entertainment: $150

Others: $100
My total expenses are $2250 and I save around $1750 monthly.

Give me personalized budgeting advice in a friendly tone. Be concise and helpful.


🧑‍💻 Author
Moises Sanchez
🔗 LinkedIn Profile
🚀 Full-stack engineer with a passion for building tools that combine AI, finance, and great user experience.


📜 License
This project is licensed under the MIT License — feel free to fork, use, and contribute!

