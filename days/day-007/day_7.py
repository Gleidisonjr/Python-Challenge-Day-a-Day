"""
Day 7 — Conditionals: elif and multiple conditions

What to study and practice in this file:
----------------------------------------
1. elif ("else if")
   - When you have more than two cases, use elif between if and else.
   - Only one block runs: the first condition that is True.
   - if condition1:
         # case 1
     elif condition2:
         # case 2
     elif condition3:
         # case 3
     else:
         # default

2. Order of conditions
   - Check the most specific cases first, then broader ones.
   - Once a condition is True, the rest are skipped.

3. Nested if
   - You can put an if (or if/elif/else) inside another if block.
   - Useful when the second condition only matters when the first is True.

4. Combining conditions
   - and: both must be True   →  if age >= 18 and has_id:
   - or:  at least one True   →  if day == "Sat" or day == "Sun":

You can combine with input(), comparison operators, and everything from previous days.

---

PROBLEM — elif and multiple conditions challenge
------------------------------------------------
Using if, elif, else (and optionally nested if), do the following:

1. Ask the user for a number. Print:
   - "Positive" if the number is greater than 0
   - "Zero" if it is 0
   - "Negative" if it is less than 0
   Use if / elif / else (no nested if needed for this one).

2. Ask the user for their age. Print a message based on age ranges, for example:
   - Under 13: "Child"
   - 13 to 17: "Teenager"
   - 18 to 64: "Adult"
   - 65 or over: "Senior"
   Use if / elif / else.

3. (Optional) Ask for a day of the week (e.g. "Monday", "Tuesday"). Print "Weekday" or "Weekend"
   (Saturday and Sunday = weekend). Use if / elif / else or a single condition with or.

4. (Optional) Nested if: ask for age and whether they have an ID (yes/no). Only print
   "You can enter" if they are 18+ and have an ID. Otherwise print an appropriate message.
"""

# My solution below:

