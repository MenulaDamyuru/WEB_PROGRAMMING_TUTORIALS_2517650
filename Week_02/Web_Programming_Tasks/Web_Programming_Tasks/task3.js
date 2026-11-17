const todoForm = document.getElementById("todoForm");
const todoInput = document.getElementById("todoInput");
const todoList = document.getElementById("todoList");
const todoError = document.getElementById("todoError");

todoForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const taskText = todoInput.value.trim();

    if (taskText === "") {
        todoError.textContent = "Please enter a task before adding it.";
        return;
    }

    todoError.textContent = "";

    const listItem = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", function () {
        taskLabel.classList.toggle("completed", checkbox.checked);
    });

    const taskLabel = document.createElement("span");
    taskLabel.textContent = taskText;

    const deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.className = "remove-button";
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function () {
        listItem.remove();
    });

    listItem.appendChild(checkbox);
    listItem.appendChild(taskLabel);
    listItem.appendChild(deleteButton);
    todoList.appendChild(listItem);

    todoInput.value = "";
    todoInput.focus();
});
