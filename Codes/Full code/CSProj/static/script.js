console.log("JS IS RUNNING");

async function loadData() {
    let res = await fetch("/data");
    let data = await res.json();

    document.getElementById("balance").innerText = data.balance;

    let list = document.getElementById("list");
    list.innerHTML = "";

    data.transactions.forEach(t => {
        let li = document.createElement("li");

        li.innerHTML =
            t.name + " - PHP " + t.amount +
            " (" + t.category + ") [" + t.date + "] " +
            `<button onclick="deleteTransaction(${t.id})">Delete</button>
             <button onclick="editTransaction(${t.id})">Edit</button>`;

        list.appendChild(li);
    });
}

async function addTransaction() {
    let name = document.getElementById("name").value;
    let amount = document.getElementById("amount").value;

    await fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            amount: amount,
            type: document.getElementById("type").value,
            category: document.getElementById("category").value
        })
    });

    loadData();
    loadInsights();
}

async function deleteTransaction(id) {
    await fetch("/delete/" + id, { method: "DELETE" });
    loadData();
    loadInsights();
}

async function editTransaction(id) {
    let name = prompt("New name:");
    let amount = prompt("New amount:");
    let type = prompt("income or expense:");
    let category = prompt("Category:");

    await fetch("/edit/" + id, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name, amount, type, category })
    });

    loadData();
    loadInsights();
}

async function loadInsights() {
    let res = await fetch("/insights");
    let data = await res.json();

    document.getElementById("insights").innerHTML =
        "<p>Today: +" + data.today.income + " / -" + data.today.expense + "</p>" +
        "<p>Week: +" + data.week.income + " / -" + data.week.expense + "</p>" +
        "<p>Month: +" + data.month.income + " / -" + data.month.expense + "</p>" +
        "<p>Year: +" + data.year.income + " / -" + data.year.expense + "</p>";
}

loadData();
loadInsights();