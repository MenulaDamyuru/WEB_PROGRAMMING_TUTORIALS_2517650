/* =====================================================================
   MOD002619 Web Programming - Week 02, Task 1
   Bill splitter: total bill + tip rate + number of people.

   All functions are defined in this external file; the HTML only holds
   element ids, so the implementation is hidden from the page source.
   ===================================================================== */

"use strict";

/**
 * Read a value from the DOM, convert it to a number and validate it.
 * Returns an object so the caller knows both the number and the reason
 * it was rejected - used to build the on-page error messages.
 *
 * @param {string} id        element id to read
 * @param {string} label     human readable name used in messages
 * @param {number} min       smallest accepted value
 * @param {number} max       largest accepted value (Infinity if no limit)
 * @param {boolean} allowZero whether 0 is acceptable
 */
function readNumber(id, label, min, max, allowZero) {
    var element = document.getElementById(id);
    var raw = element.value.trim();
    var errors = [];

    if (raw === "") {
        errors.push("Please enter the " + label.toLowerCase() + ".");
        return { id: id, value: NaN, errors: errors };
    }

    var value = Number(raw);

    if (isNaN(value)) {
        errors.push("The " + label.toLowerCase() + " must be a number.");
    } else if (!isFinite(value)) {
        errors.push("The " + label.toLowerCase() + " is too large.");
    } else if (value < min) {
        errors.push("The " + label.toLowerCase() + " cannot be less than " + min + ".");
    } else if (value > max) {
        errors.push("The " + label.toLowerCase() + " cannot be more than " + max + ".");
    } else if (!allowZero && value === 0) {
        errors.push("The " + label.toLowerCase() + " cannot be zero.");
    }

    return { id: id, value: value, errors: errors };
}

/** Show or hide the styled error block underneath one input. */
function setFieldError(id, messages) {
    var input = document.getElementById(id);
    var box = document.getElementById(id + "-error");

    if (!input || !box) {
        return;
    }

    if (messages.length === 0) {
        input.classList.remove("invalid");
        box.classList.remove("show");
        box.textContent = "";
    } else {
        input.classList.add("invalid");
        box.classList.add("show");
        box.textContent = messages.join(" ");
    }
}

/** Format a number as British pounds. */
function money(amount) {
    return "\u00A3" + amount.toFixed(2);
}

/**
 * Calculate the bill: validates every input, shows the error summary and,
 * when everything is valid, writes the totals into the results panel.
 */
function calculateBill() {
    var bill = readNumber("billAmount", "Bill amount", 0.01, 100000, false);
    var people = readNumber("numPeople", "Number of people", 1, 200, false);
    var tipSelect = document.getElementById("tipRate");
    var tipRate = Number(tipSelect.value);

    // per-field messages
    setFieldError("billAmount", bill.errors);
    setFieldError("numPeople", people.errors);

    // collect everything for the summary box at the top of the form
    var allErrors = bill.errors.concat(people.errors);
    var summary = document.getElementById("formErrors");
    var list = document.getElementById("formErrorList");

    if (allErrors.length > 0) {
        list.innerHTML = "";
        allErrors.forEach(function (message) {
            var item = document.createElement("li");
            item.textContent = message;
            list.appendChild(item);
        });
        summary.classList.add("show");
        document.getElementById("result").classList.add("hidden");
        return;
    }

    summary.classList.remove("show");

    // ---- the actual arithmetic ----
    var tipAmount = bill.value * (tipRate / 100);
    var totalWithTip = bill.value + tipAmount;
    var perPerson = totalWithTip / people.value;

    document.getElementById("outBill").textContent = money(bill.value);
    document.getElementById("outTipRate").textContent = tipRate + "%";
    document.getElementById("outTipAmount").textContent = money(tipAmount);
    document.getElementById("outTotal").textContent = money(totalWithTip);
    document.getElementById("outPeople").textContent = String(people.value);
    document.getElementById("outPerPerson").textContent = money(perPerson);

    var panel = document.getElementById("result");
    panel.classList.remove("hidden");
    panel.classList.add("show-ok");
}

/* Wire the button up on load - no inline onclick in the HTML at all. */
window.addEventListener("DOMContentLoaded", function () {
    document.getElementById("calculate").addEventListener("click", calculateBill);
    document.getElementById("reset").addEventListener("click", function () {
        ["billAmount", "numPeople"].forEach(function (id) {
            setFieldError(id, []);
        });
        document.getElementById("formErrors").classList.remove("show");
        document.getElementById("result").classList.add("hidden");
    });
});
