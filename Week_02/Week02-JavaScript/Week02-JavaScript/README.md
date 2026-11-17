# Week 02 - JavaScript worksheet

Three tasks from the Week 02 worksheet. Every page uses an **external stylesheet**
and an **external JavaScript file**; no inline handlers are used.

## Task 1 - Bill splitter (`task1-bill-splitter.html`)

* inputs: total bill amount, tip rate (0 / 5 / 10 / 15 / 20 %), number of people
* a button calls `calculateBill()` in `js/billsplitter.js`
* output: bill, tip rate, tip amount, total with tip, number of people, **per person**
* validation: empty, non-numeric, negative, zero and out-of-range values are rejected,
  the offending input is given a red border and **each invalid item is named** in a
  summary box plus a message under the field
* the look of every message is driven by CSS (`.error`, `.show`, `#formErrors`)

Debugging evidence required by the worksheet (breakpoint, stepping through the code,
inspecting a variable) is included in the separate evidence document.

## Task 2 - Menu bill (`task2-menu-bill.html`)

* the total bill input has been **removed**
* the user adds menu items (name + cost); items can be removed individually
* the bill is the **sum of the items** (`totalBill()` uses `Array.reduce`)
* pressing *Calculate split* derives the total from the list, applies the tip rate and
  divides by the number of people

## Task 3 - To-do list (`task3-todo.html`)

* add a task, tick the checkbox to mark it complete (struck through), delete a task,
  clear all completed tasks
* a counter shows "n of m tasks completed"
* no persistence - refreshing clears the list

## Run it

No build step; open `index.html` in a browser or serve the folder:

```bash
python -m http.server 8000
```

## File layout

```
Week02-JavaScript/
  index.html                 overview page
  task1-bill-splitter.html   Task 1
  task2-menu-bill.html       Task 2
  task3-todo.html            Task 3
  css/style.css              external stylesheet shared by all pages
  js/billsplitter.js         Task 1 logic (validated, commented)
  js/menubill.js             Task 2 logic
  js/todo.js                 Task 3 logic
```
