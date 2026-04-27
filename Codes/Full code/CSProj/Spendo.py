from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

# -----------------------
# LOAD / SAVE FUNCTIONS
# -----------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"balance": 0, "transactions": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -----------------------
# HOME
# -----------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------
# GET DATA
# -----------------------
@app.route("/data")
def get_data():
    data = load_data()
    return jsonify(data)

# -----------------------
# ADD TRANSACTION
# -----------------------
@app.route("/add", methods=["POST"])
def add_transaction():
    data = load_data()
    req = request.json

    transaction = {
        "id": datetime.now().timestamp(),
        "name": req["name"],
        "amount": float(req["amount"]),
        "type": req["type"],  # income / expense
        "category": req["category"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if transaction["type"] == "income":
        data["balance"] += transaction["amount"]
    else:
        data["balance"] -= transaction["amount"]

    data["transactions"].append(transaction)
    save_data(data)

    return jsonify({"status": "success"})

# -----------------------
# DELETE TRANSACTION
# -----------------------
@app.route("/delete/<float:tid>", methods=["DELETE"])
def delete_transaction(tid):
    data = load_data()

    for t in data["transactions"]:
        if t["id"] == tid:
            if t["type"] == "income":
                data["balance"] -= t["amount"]
            else:
                data["balance"] += t["amount"]
            data["transactions"].remove(t)
            break

    save_data(data)
    return jsonify({"status": "deleted"})

# -----------------------
# EDIT TRANSACTION
# -----------------------
@app.route("/edit/<float:tid>", methods=["PUT"])
def edit_transaction(tid):
    data = load_data()
    req = request.json

    for t in data["transactions"]:
        if t["id"] == tid:
            # revert old balance
            if t["type"] == "income":
                data["balance"] -= t["amount"]
            else:
                data["balance"] += t["amount"]

            # update values
            t["name"] = req["name"]
            t["amount"] = float(req["amount"])
            t["type"] = req["type"]
            t["category"] = req["category"]

            # apply new balance
            if t["type"] == "income":
                data["balance"] += t["amount"]
            else:
                data["balance"] -= t["amount"]

            break

    save_data(data)
    return jsonify({"status": "updated"})

# -----------------------
# INSIGHTS
# -----------------------
@app.route("/insights")
def insights():
    data = load_data()
    now = datetime.now()

    today = now.strftime("%Y-%m-%d")
    week = now.isocalendar()[1]
    month = now.month
    year = now.year

    result = {
        "today": {"income": 0, "expense": 0},
        "week": {"income": 0, "expense": 0},
        "month": {"income": 0, "expense": 0},
        "year": {"income": 0, "expense": 0},
    }

    for t in data["transactions"]:
        t_date = datetime.strptime(t["date"], "%Y-%m-%d %H:%M:%S")

        def update(period):
            if t["type"] == "income":
                result[period]["income"] += t["amount"]
            else:
                result[period]["expense"] += t["amount"]

        if t_date.strftime("%Y-%m-%d") == today:
            update("today")
        if t_date.isocalendar()[1] == week:
            update("week")
        if t_date.month == month:
            update("month")
        if t_date.year == year:
            update("year")

    return jsonify(result)

# -----------------------
# RUN
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)