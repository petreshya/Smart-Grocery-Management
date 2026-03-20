const API = "http://127.0.0.1:5000";

// Add Item
function addItem() {
    const userName = document.getElementById("user_name").value;
    if (!userName) {
        alert("Please enter your name");
        return;
    }
    
    const itemName = document.getElementById("name").value;
    if (!itemName) {
        alert("Please enter item name");
        return;
    }
    
    fetch(`${API}/add-item`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            user_name: userName,
            item_name: itemName,
            category: document.getElementById("category").value || "General",
            price: parseFloat(document.getElementById("price").value) || 0,
            priority: document.getElementById("priority").value || "essential",
            purchase_frequency: document.getElementById("purchase_frequency").value || "Monthly"
        })
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        alert(data.message || "Item Added Successfully");
        // Clear the form
        document.getElementById("name").value = "";
        document.getElementById("category").value = "";
        document.getElementById("price").value = "";
        document.getElementById("purchase_frequency").value = "";
    })
    .catch(err => {
        console.error('Error adding item:', err);
        alert('Error adding item: ' + err);
    });
}

// Load Items
function loadItems() {
    const userName = document.getElementById("user_name").value;
    if (!userName) {
        alert("Please enter your name");
        return;
    }
    
    fetch(`${API}/items?user_name=${encodeURIComponent(userName)}`)
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        let list = document.getElementById("itemList");
        list.innerHTML = "";
        if (data.length === 0) {
            list.innerHTML = "<li style='color: gray;'>No items added yet. Go to 'Add Item' to add groceries.</li>";
        } else {
            data.forEach(item => {
                const freq = item.purchase_frequency || item.purchase_frequency;
                const pri = item.priority || 'unknown';
                itemList.innerHTML += `
                    <div class="card">
                        <span><strong>${item.item_name}</strong> - ₹${item.price}</span>
                        <span><small>${item.category || 'General'} • ${pri} • ${freq}</small></span>
                        <button class="small-btn" onclick="deleteItem(${item.id})">Delete</button>
                    </div>`;
            });
        }
    })
    .catch(err => {
        console.error('Error loading items:', err);
        alert('Error loading items: ' + err);
    });
}

// Delete Item
function deleteItem(id) {
    const userName = document.getElementById("user_name").value;
    if (!userName) {
        alert("Please enter your name");
        return;
    }

    fetch(`${API}/delete-item/${id}?user_name=${encodeURIComponent(userName)}`, {
        method: "DELETE"
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        alert(data.message || "Item Deleted Successfully");
        loadItems();
    })
    .catch(err => {
        console.error('Error deleting item:', err);
        alert('Error deleting item: ' + err);
    });
}

// Set Budget
function setBudget() {
    const userName = document.getElementById("user_name").value;
    if (!userName) {
        alert("Please enter your name");
        return;
    }
    
    const budget = parseFloat(document.getElementById("budget").value);
    if (!budget || budget <= 0) {
        alert("Please enter a valid budget");
        return;
    }
    
    fetch(`${API}/set-budget`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            user_name: userName,
            monthly_budget: budget
        })
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }
        return res.json();
    })
    .then(data => alert(data.message || "Budget Updated Successfully"))
    .catch(err => {
        console.error('Error setting budget:', err);
        alert('Error setting budget: ' + err);
    });
}

// Recommendation
function getRecommendation() {
    const userName = document.getElementById("user_name").value;
    if (!userName) {
        alert("Please enter your name");
        return;
    }
    
    fetch(`${API}/recommend?user_name=${encodeURIComponent(userName)}`)
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        if (data.error) { 
            alert(data.error); 
            return; 
        }
        let list = document.getElementById("recommendList");
        list.innerHTML = "";

        if (data.recommended_items.length === 0) {
            list.innerHTML = "<li style='color: gray;'>No recommendations available.</li>";
        } else {
            data.recommended_items.forEach(item => {
                list.innerHTML += `<li>${item.item_name} - ₹${item.price}</li>`;
            });
        }

        document.getElementById("summary").innerHTML =
            `<strong>Total Cost:</strong> ₹${data.total_cost} | <strong>Remaining Budget:</strong> ₹${data.remaining_budget}`;
    })
    .catch(err => {
        console.error('Error getting recommendation:', err);
        alert('Error getting recommendation: ' + err);
    });
}
