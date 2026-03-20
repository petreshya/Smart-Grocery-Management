from database import get_connection, init_db

def seed():
    init_db()
    conn = get_connection()

    # Clear existing data
    conn.execute("DELETE FROM grocery")
    conn.execute("DELETE FROM budget")

    sample_items = [
        ("Milk", "Dairy", 60.0, "essential", 7),
        ("Eggs", "Dairy", 120.0, "essential", 4),
        ("Bread", "Bakery", 40.0, "essential", 5),
        ("Chocolate", "Snacks", 150.0, "non-essential", 1),
        ("Tomatoes", "Produce", 80.0, "essential", 3)
    ]

    conn.executemany(
        "INSERT INTO grocery (item_name, category, price, priority, purchase_frequency) VALUES (?, ?, ?, ?, ?)",
        sample_items
    )

    # Set an example monthly budget
    conn.execute("INSERT INTO budget (monthly_budget) VALUES (?)", (1500.0,))

    conn.commit()
    conn.close()

    print("Seeded database with sample items and budget.")

if __name__ == "__main__":
    seed()
