import pandas as pd

def recommend_items(data, budget):
    if len(data) == 0:
        return [], 0

    df = pd.DataFrame(data)

    # Priority scoring
    df["priority_score"] = df["priority"].apply(
        lambda x: 2 if x.lower() == "essential" else 1
    )

    # Sorting logic (AI decision style)
    df = df.sort_values(
        by=["priority_score", "purchase_frequency"],
        ascending=False
    )

    selected_items = []
    total_cost = 0

    for _, row in df.iterrows():
        if total_cost + row["price"] <= budget:
            selected_items.append({
                "item_name": row["item_name"],
                "price": row["price"],
                "category": row["category"],
                "priority": row["priority"]
            })
            total_cost += row["price"]

    return selected_items, total_cost
