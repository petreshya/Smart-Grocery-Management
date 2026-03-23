# 🛒 BudgetMart — Smart Grocery Recommendation System

BudgetMart is a modern, AI-powered grocery recommendation system designed to help users manage their grocery lists and optimize their shopping within a fixed monthly budget. It uses a smart recommendation engine to suggest the best combination of essential and non-essential items.

## ✨ Features
- **Modern Premium UI:** A clean, responsive dashboard built with a professional purple/indigo theme.
- **Smart Budgeting:** Set your monthly budget and track your spending in real-time.
- **AI Recommendation:** Intelligent algorithm suggests the best items based on priority and budget.
- **Easy Management:** Add, view, and delete grocery items with ease.

## 🚀 Quick Start (Local Setup)

### 1. Backend Setup
```powershell
# Navigate to backend and setup virtual environment
cd backend
python -m venv .venv
.venv\Scripts\activate

# Install dependencies and start the Flask server
pip install -r requirements.txt
python app.py
```
*The backend will be running at `http://127.0.0.1:5000`*

### 2. Database Seeding (Optional)
```powershell
# Seed the database with sample items for testing
python backend/seed_data.py
```

### 3. Frontend Access
Simply open `frontend/index.html` in your browser. For the best experience, since the backend is running on port 5000, you can navigate directly to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** Vanilla JS, CSS (Modern Premium UI)
- **Deployment:** GitHub Pages / Local Hosting

## 📝 Notes
- Ensure Python 3.x is installed.
- The UI is optimized for modern browsers (Chrome, Edge, Firefox).
- Priority-driven recommendation engine ensures essential items are always prioritized.

---
Developed as a Capstone Project for Smart Grocery Management.
