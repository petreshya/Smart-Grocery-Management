# BudgetMart — Smart Grocery Recommendation System

Quick steps to run the project for a demo (Windows):

1. Start backend

```powershell
cd "smart-grocery/backend"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
.venv\Scripts\python app.py
```

2. In a second terminal, seed the database with sample data (optional but recommended):

```powershell
cd "smart-grocery/backend"
.venv\Scripts\python seed_data.py
```

3. Serve the frontend files and open the app

```powershell
cd "smart-grocery/frontend"
# Use Python's simple HTTP server
python -m http.server 8000
# Open http://localhost:8000/index.html in your browser
```

Notes
- The backend runs on `http://127.0.0.1:5000` by default.
- Serve the frontend over HTTP (not file://) so fetch() calls work.
- `seed_data.py` inserts a few sample grocery items and a monthly budget to make the recommendation demo immediate.
