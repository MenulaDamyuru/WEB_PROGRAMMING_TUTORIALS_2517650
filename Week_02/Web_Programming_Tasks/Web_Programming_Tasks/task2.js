const itemForm = document.getElementById("itemForm");
const itemList = document.getElementById("itemList");
const errorBox = document.getElementById("errors");
const resultBox = document.getElementById("result");
const items = [];

itemForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const nameInput = document.getElementById("itemName");
    const costInput = document.getElementById("itemCost");
    const name = nameInput.value.trim();
    const cost = Number(costInput.value);
    const errors = [];

    if (name === "") {
        errors.push("Enter a menu item name.");
    }

    if (costInput.value.trim() === "" || !Number.isFinite(cost) || cost <= 0) {
        errors.push("Enter an item cost greater than 0.");
    }

    if (errors.length > 0) {
        showErrors(errors);
        return;
    }

    items.push({ name: name, cost: cost });
    nameInput.value = "";
    costInput.value = "";
    showErrors([]);
    displayItems();
});

function displayItems() {
    itemList.innerHTML = "";

    if (items.length === 0) {
        itemList.innerHTML = '<li class="empty">No items added yet.</li>';
        return;
    }

    items.forEach(function (item, index) {
        const listItem = document.createElement("li");
        const itemText = document.createElement("span");
        itemText.textContent = item.name + " - Rs. " + item.cost.toFixed(2);

        const removeButton = document.createElement("button");
        removeButton.type = "button";
        removeButton.className = "remove-button";
        removeButton.textContent = "Remove";
        removeButton.addEventListener("click", function () {
            items.splice(index, 1);
            displayItems();
        });

        listItem.appendChild(itemText);
        listItem.appendChild(removeButton);
        itemList.appendChild(listItem);
    });
}

function showErrors(messages) {
    if (messages.length === 0) {
        errorBox.textContent = "";
        return;
    }

    errorBox.innerHTML = "<strong>Please correct these items:</strong><ul>" +
        messages.map(function (message) {
            return "<li>" + message + "</li>";
        }).join("") + "</ul>";
}

document.getElementById("calculateButton").addEventListener("click", function () {
    const peopleInput = document.getElementById("people");
    const people = Number(peopleInput.value);
    const tipRate = Number(document.getElementById("tipRate").value);
    const errors = [];

    if (items.length === 0) {
        errors.push("Add at least one menu item.");
    }

    if (peopleInput.value.trim() === "" || !Number.isInteger(people) || people <= 0) {
        errors.push("Enter a whole number of people (at least 1).");
    }

    if (errors.length > 0) {
        showErrors(errors);
        resultBox.innerHTML = "";
        return;
    }

    showErrors([]);

    // Add the cost of every menu item to get the bill amount.
    let billAmount = 0;
    items.forEach(function (item) {
        billAmount += item.cost;
    });

    const tipAmount = billAmount * tipRate / 100;
    const totalAmount = billAmount + tipAmount;
    const amountPerPerson = totalAmount / people;

    resultBox.innerHTML =
        "<h3>Bill summary</h3>" +
        "<p>Items total: Rs. " + billAmount.toFixed(2) + "</p>" +
        "<p>Tip amount: Rs. " + tipAmount.toFixed(2) + "</p>" +
        "<p><strong>Total including tip: Rs. " + totalAmount.toFixed(2) + "</strong></p>" +
        "<p><strong>Each person pays: Rs. " + amountPerPerson.toFixed(2) + "</strong></p>";
});
