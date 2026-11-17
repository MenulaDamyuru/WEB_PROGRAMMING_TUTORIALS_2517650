const billForm = document.getElementById("billForm");

billForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const billAmount = Number(document.getElementById("billAmount").value);
    const tipRate = Number(document.getElementById("tipRate").value);
    const people = Number(document.getElementById("people").value);
    const errors = [];

    // Check that the bill is a valid positive number.
    if (document.getElementById("billAmount").value.trim() === "" ||
        !Number.isFinite(billAmount) || billAmount <= 0) {
        errors.push("Enter a bill amount greater than 0.");
    }

    // Check that the number of people is a whole number greater than zero.
    if (document.getElementById("people").value.trim() === "" ||
        !Number.isInteger(people) || people <= 0) {
        errors.push("Enter a whole number of people (at least 1).");
    }

    const errorBox = document.getElementById("errors");
    const resultBox = document.getElementById("result");

    if (errors.length > 0) {
        errorBox.innerHTML = "<strong>Please correct these items:</strong><ul>" +
            errors.map(function (message) {
                return "<li>" + message + "</li>";
            }).join("") + "</ul>";
        resultBox.innerHTML = "";
        return;
    }

    errorBox.textContent = "";

    const tipAmount = billAmount * tipRate / 100;
    const totalAmount = billAmount + tipAmount;
    const amountPerPerson = totalAmount / people;

    resultBox.innerHTML =
        "<h3>Bill summary</h3>" +
        "<p>Bill amount: Rs. " + billAmount.toFixed(2) + "</p>" +
        "<p>Tip amount: Rs. " + tipAmount.toFixed(2) + "</p>" +
        "<p><strong>Total including tip: Rs. " + totalAmount.toFixed(2) + "</strong></p>" +
        "<p><strong>Each person pays: Rs. " + amountPerPerson.toFixed(2) + "</strong></p>";
});
