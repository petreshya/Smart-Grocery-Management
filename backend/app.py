from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_connection, init_db
from model import recommend_items

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

init_db()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/add.html')
def add():
    return app.send_static_file('add.html')

@app.route('/recommendation.html')
def recommendation():
    return app.send_static_file('recommendation.html')

# ---------------- ADD ITEM ----------------
@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.json
    conn = get_connection()
    conn.execute("""
        INSERT INTO grocery 
        (user_name, item_name, category, price, priority, purchase_frequency)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["user_name"],
        data["item_name"],
        data["category"],
        data["price"],
        data["priority"],
        data["purchase_frequency"]
    ))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item Added Successfully"})


# ---------------- GET ITEMS ----------------
@app.route("/items", methods=["GET"])
def get_items():
    user_name = request.args.get("user_name")
    if not user_name:
        return jsonify({"error": "user_name parameter required"}), 400
    
    conn = get_connection()
    items = conn.execute("SELECT * FROM grocery WHERE user_name=?", (user_name,)).fetchall()
    conn.close()

    return jsonify([dict(item) for item in items])


# ---------------- DELETE ITEM ----------------
@app.route("/delete-item/<int:id>", methods=["DELETE"])
def delete_item(id):
    user_name = request.args.get("user_name")
    if not user_name:
        return jsonify({"error": "user_name parameter required"}), 400
    
    conn = get_connection()
    conn.execute("DELETE FROM grocery WHERE id=? AND user_name=?", (id, user_name))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item Deleted Successfully"})


# ---------------- SET BUDGET ----------------
@app.route("/set-budget", methods=["POST"])
def set_budget():
    data = request.json
    user_name = data.get("user_name")
    
    if not user_name:
        return jsonify({"error": "user_name required"}), 400
    
    conn = get_connection()

    conn.execute("DELETE FROM budget WHERE user_name=?", (user_name,))
    conn.execute(
        "INSERT INTO budget (user_name, monthly_budget) VALUES (?, ?)",
        (user_name, data["monthly_budget"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Budget Updated Successfully"})


# ---------------- RECOMMENDATION ----------------
@app.route("/recommend", methods=["GET"])
def recommend():
    user_name = request.args.get("user_name")
    if not user_name:
        return jsonify({"error": "user_name parameter required"}), 400
    
    conn = get_connection()

    items = conn.execute("SELECT * FROM grocery WHERE user_name=?", (user_name,)).fetchall()
    budget_data = conn.execute(
        "SELECT monthly_budget FROM budget WHERE user_name=? ORDER BY id DESC LIMIT 1",
        (user_name,)
    ).fetchone()

    conn.close()

    if not budget_data:
        return jsonify({"error": "Please Set Budget First"}), 400

    items_list = [dict(item) for item in items]

    recommended, total_cost = recommend_items(
        items_list,
        budget_data["monthly_budget"]
    )

    return jsonify({
        "recommended_items": recommended,
        "total_cost": total_cost,
        "remaining_budget":
            budget_data["monthly_budget"] - total_cost
    })


if __name__ == "__main__":
    app.run(debug=True)
