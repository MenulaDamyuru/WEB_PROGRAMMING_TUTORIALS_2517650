/* =====================================================================
   MOD002619 Web Programming - Week 02, Task 3
   Simple To-Do list: add tasks and tick them off when they are complete.
   Nothing is persisted - refreshing the page clears the list.
   ===================================================================== */

"use strict";

var tasks = []; // [{ text: "...", done: false }]

/** Count how many tasks are finished and refresh the counter text. */
function updateCounter() {
    var done = tasks.filter(function (task) {
        return task.done;
    }).length;
    document.getElementById("counter").textContent =
        done + " of " + tasks.length + " task" + (tasks.length === 1 ? "" : "s") + " completed";
}

/** Redraw the whole list from the tasks array (the single source of truth). */
function renderTasks() {
    var list = document.getElementById("todoList");
    list.innerHTML = "";

    if (tasks.length === 0) {
        var hint = document.createElement("li");
        hint.className = "empty";
        hint.id = "emptyHint";
        hint.textContent = "Nothing to do yet - add your first task above.";
        list.appendChild(hint);
        updateCounter();
        return;
    }

    tasks.forEach(function (task, index) {
        var item = document.createElement("li");
        if (task.done) {
            item.classList.add("done");
        }

        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.done;
        checkbox.id = "task-" + index;
        checkbox.setAttribute("aria-label", "Mark '" + task.text + "' complete");
        checkbox.addEventListener("change", function () {
            tasks[index].done = checkbox.checked;
            renderTasks();
        });

        var label = document.createElement("label");
        label.className = "task-text";
        label.setAttribute("for", checkbox.id);
        label.textContent = task.text;

        var remove = document.createElement("button");
        remove.type = "button";
        remove.className = "small remove";
        remove.textContent = "Delete";
        remove.addEventListener("click", function () {
            tasks.splice(index, 1);
            renderTasks();
        });

        item.appendChild(checkbox);
        item.appendChild(label);
        item.appendChild(remove);
        list.appendChild(item);
    });

    updateCounter();
}

function addTask() {
    var field = document.getElementById("newTask");
    var text = field.value.trim();
    var box = document.getElementById("newTask-error");

    if (text === "") {
        field.classList.add("invalid");
        box.classList.add("show");
        box.textContent = "Type a task before pressing Add.";
        return;
    }

    field.classList.remove("invalid");
    box.classList.remove("show");
    tasks.push({ text: text, done: false });
    field.value = "";
    field.focus();
    renderTasks();
}

window.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addTask").addEventListener("click", addTask);
    document.getElementById("newTask").addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            addTask();
        }
    });
    document.getElementById("clearDone").addEventListener("click", function () {
        tasks = tasks.filter(function (task) {
            return !task.done;
        });
        renderTasks();
    });
    renderTasks();
});
