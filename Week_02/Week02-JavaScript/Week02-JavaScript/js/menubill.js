/* =====================================================================
   MOD002619 Web Programming - Week 02, Task 2
   Menu bill: the user adds menu items and their cost, the total bill is
   derived from the list (there is no "total bill amount" input any more).
   ===================================================================== */

"use strict";

var items = []; // [{name: "Pizza", cost: 9.5}, ...]

function money(amount) {
    return "\u00A3" + amount.toFixed(2);
}

function totalBill() {
    // reduce is the concise way of summing a numeric property
    return items.reduce(function (sum, item) {
        return sum + item.cost;
    }, 0);
}

/** Re-draw the item table, the running total and the per-person figures. */
function render() {
    var body = document.getElementById("itemRows");
    body.innerHTML = "";

    if (items.length === 0) {
        var empty = document.createElement("tr");
        empty.innerHTML = '<td colspan="4" class="empty">No items yet &mdash; add your first menu item above.</td>';
        body.appendChild(empty);
    } else {
        items.forEach(function (item, index) {
            var row = document.createElement("tr");

            var nameCell = document.createElement("td");
            nameCell.textContent = item.name;

            var costCell = document.createElement("td");
            costCell.className = "numeric";
            costCell.textContent = money(item.cost);

            var indexCell = document.createElement("td");
            indexCell.textContent = String(index + 1);

            var actionCell = document.createElement("td");
            var remove = document.createElement("button");
            remove.type = "button";
            remove.className = "small remove";
            remove.textContent = "Remove";
            // closure keeps the right index for each button
            remove.addEventListener("click", function () {
                items.splice(index, 1);
                render();
            });
            actionCell.appendChild(remove);

            row.appendChild(indexCell);
            row.appendChild(nameCell);
            row.appendChild(costCell);
            row.appendChild(actionCell);
            body.appendChild(row);
        });
    }

    document.getElementById("outItemCount").textContent = String(items.length);
    document.getElementById("outItemsTotal").textContent = money(totalBill());
}

function setError(id, message) {
    var input = document.getElementById(id);
    var box = document.getElementById(id + "-error");
    if (!input || !box) {
        return;
    }
    if (message) {
        input.classList.add("invalid");
        box.classList.add("show");
        box.textContent = message;
    } else {
        input.classList.remove("invalid");
        box.classList.remove("show");
        box.textContent = "";
    }
}

/* ---- Task 2 trigger: add a menu item ---- */
function addItem() {
    var nameField = document.getElementById("itemName");
    var costField = document.getElementById("itemCost");
    var name = nameField.value.trim();
    var costRaw = costField.value.trim();
    var problems = [];

    if (name === "") {
        setError("itemName", "Please enter the item name.");
        problems.push("item name");
    } else {
        setError("itemName", "");
    }

    var cost = Number(costRaw);
    if (costRaw === "") {
        setError("itemCost", "Please enter the item cost.");
        problems.push("item cost");
    } else if (isNaN(cost)) {
        setError("itemCost", "The item cost must be a number.");
        problems.push("item cost");
    } else if (cost <= 0) {
        setError("itemCost", "The item cost must be greater than zero.");
        problems.push("item cost");
    } else if (cost > 1000) {
        setError("itemCost", "The item cost looks wrong (over \u00A31000).");
        problems.push("item cost");
    } else {
        setError("itemCost", "");
    }

    var summary = document.getElementById("formErrors");
    var list = document.getElementById("formErrorList");
    if (problems.length > 0) {
        list.innerHTML = "";
        problems.forEach(function (label) {
            var item = document.createElement("li");
            item.textContent = "Please correct the " + label + ".";
            list.appendChild(item);
        });
        summary.classList.add("show");
        return;
    }
    summary.classList.remove("show");

    items.push({ name: name, cost: cost });
    nameField.value = "";
    costField.value = "";
    nameField.focus();
    render();
}

/* ---- split the derived total between the people ---- */
function splitBill() {
    var people = Number(document.getElementById("numPeople").value);
    var tipRate = Number(document.getElementById("tipRate").value);

    if (isNaN(people) || people < 1 || people > 200) {
        setError("numPeople", "Enter a number of people between 1 and 200.");
        document.getElementById("result").classList.add("hidden");
        return;
    }
    setError("numPeople", "");

    if (items.length === 0) {
        var summary = document.getElementById("formErrors");
        var list = document.getElementById("formErrorList");
        list.innerHTML = "<li>Add at least one menu item first.</li>";
        summary.classList.add("show");
        document.getElementById("result").classList.add("hidden");
        return;
    }
    document.getElementById("formErrors").classList.remove("show");

    var bill = totalBill();
    var tipAmount = bill * (tipRate / 100);
    var total = bill + tipAmount;
    var perPerson = total / people;

    document.getElementById("outBill").textContent = money(bill);
    document.getElementById("outTipAmount").textContent = money(tipAmount);
    document.getElementById("outTotal").textContent = money(total);
    document.getElementById("outPeople").textContent = String(people);
    document.getElementById("outPerPerson").textContent = money(perPerson);

    var panel = document.getElementById("result");
    panel.classList.remove("hidden");
    panel.classList.add("show-ok");
}

window.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addItem").addEventListener("click", addItem);
    document.getElementById("splitBill").addEventListener("click", splitBill);
    // pressing Enter in the item name field also adds the item
    document.getElementById("itemName").addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            addItem();
        }
    });
    render();
});
