"""
Day 2 — Operators

What to study and practice in this file:
----------------------------------------
1. Arithmetic operators
   - + (add), - (subtract), * (multiply), / (divide)
   - // (floor division), % (remainder)
   - Example: 17 // 5  →  3,  17 % 5  →  2

2. Comparison operators
   - == (equal), != (not equal)
   - < (less than), > (greater than), <= (less or equal), >= (greater or equal)
   - Result is bool: True or False

3. Assignment operators
   - = (assign), += (add and assign), -= (subtract and assign)
   - Example: x = 10; x += 3  →  x is 13

You can use variables, data types, and print() from Day 0 and Day 1.
(You will study user input in Day 3 — for now use fixed values in variables.)

---

PROBLEM — Python Challenge Day a Day: progress calculator
---------------------------------------------------------
Using only variables, data types, operators, and print(), solve this:

1. Define variables for your challenge:
   - steps_completed = number of steps you have done so far (e.g. 2 for day-0 and day-1)
   - total_steps_stage0 = total steps in Stage 0 (see ROADMAP: steps 0 to 19)
   - minutes_studied_today = how many minutes you studied today (e.g. 30)

2. Using arithmetic operators, compute and store in new variables:
   - steps_remaining = how many steps are left in Stage 0
   - percentage_done = percent of Stage 0 completed (steps_completed / total * 100)
   - minutes_per_step = average minutes per step so far (minutes_studied_today / steps_completed)
   Use the operators you need: -, /, *, etc.

3. Using comparison operators, create booleans (store in variables or use in print):
   - is_started = you have started (steps_completed is greater than 0)
   - is_not_finished = Stage 0 is not complete (steps_remaining is greater than 0)
   - studied_today = you studied at least 1 minute today

4. Print a short report, for example:
   - Steps completed, steps remaining, percentage done
   - Whether you have started and whether Stage 0 is finished
   - Minutes studied today and (if steps_completed > 0) minutes per step

5. (Optional) Use an assignment operator: e.g. add 1 to steps_completed with += and print again.

Try to use at least: +, -, *, /, one of (// or %), == or != or < or >, and = (assignment).
"""

# My solution below:

#Task 1: Define variables for your challenge:
steps_completed = 2
total_steps_stage0 = 19
minutes_studied_today = 15

#Task 2: Using arithmetic operators, compute and store in new variables:
steps_remaining = total_steps_stage0 - steps_completed
percentage_done = (steps_completed / total_steps_stage0) * 100
minutes_per_step = minutes_studied_today / steps_completed

#Task 3: Using comparison operators, create booleans (store in variables or use in print):
is_started = steps_completed > 0
is_not_finished = steps_remaining > 0
studied_today = minutes_studied_today >= 1

#Task 4: Print a short report, for example:
print(f"Steps completed: {steps_completed}")
print(f"Steps remaining: {steps_remaining}")
print(f"Percentage done: {percentage_done}%")
print(f"Minutes per step: {minutes_per_step}")
print(f"Is started: {is_started}")
print(f"Is not finished: {is_not_finished}")
print(f"Studied today: {studied_today}")

