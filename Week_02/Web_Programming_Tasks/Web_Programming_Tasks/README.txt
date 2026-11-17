WEB PROGRAMMING TASKS

Files:
- task1.html and task1.js: Task 1 manual bill amount, tip percentage and people split.
- task2.html and task2.js: Task 2 add menu items; the bill total is calculated from the item costs.
- task3.html and task3.js: Task 3 temporary ToDo list with completion checkboxes.
- style.css: External CSS shared by all three pages.

HOW TO RUN
1. Keep all files in the same folder.
2. Open task1.html, task2.html or task3.html in a browser.
3. No frameworks or libraries are used.

DEBUGGER EVIDENCE FOR TASK 1
Use Chrome or Edge:
1. Open task1.html in the browser.
2. Press F12 and open the Sources tab.
3. Open task1.js.
4. Click the line number beside:
   const tipAmount = billAmount * tipRate / 100;
   This creates a breakpoint.
5. Enter a bill amount, choose a tip rate, enter the number of people,
   then click Calculate.
6. The debugger should pause at the breakpoint.
7. Take a screenshot showing the highlighted paused line (breakpoint evidence).
8. Click the Step over button (right-facing curved arrow) to execute the
   next line one at a time (stepping evidence).
9. In the Scope panel, inspect billAmount, tipRate, people, tipAmount,
   totalAmount and amountPerPerson. Take a screenshot with a variable selected
   or visible (variable inspection evidence).
10. Press the Resume button to finish.

Suggested test:
Bill amount: 2000
Tip: 10%
People: 4
Expected tip: Rs. 200.00
Expected total: Rs. 2200.00
Expected per person: Rs. 550.00

Validation tests:
- Leave bill amount empty.
- Enter 0 or a negative bill amount.
- Leave people empty.
- Enter 0, a negative number, or a decimal for people.
The page displays a message identifying the invalid input.

NOTE
The ToDo list is not saved. Refreshing task3.html clears the tasks, as
required by the assignment.
