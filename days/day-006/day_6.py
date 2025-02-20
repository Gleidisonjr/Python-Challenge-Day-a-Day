"""
Day 6 — Conditionals: if and else

What to study and practice in this file:
----------------------------------------
1. if
   - Run a block of code only when a condition is True.
   - if condition:
         # code here (indented)

2. Comparison operators (you already know them from Day 2)
   - == (equal), != (not equal), <, >, <=, >=
   - Result is True or False.

3. else
   - Run a different block when the condition is False.
   - if condition:
         # when True
     else:
         # when False

4. Indentation
   - Python uses indentation (usually 4 spaces) to show which lines belong to the if or else block.
   - Wrong indentation = syntax error or wrong behavior.

5. Simple conditions
   - You can use: numbers (e.g. age >= 18), strings (e.g. name == "admin"),
     and results from input() (remember to convert to int/float when comparing numbers).

You can combine with input(), variables, and everything from previous days.

---

PROBLEM — if and else challenge
-------------------------------
Using if and else (and input), do the following:

1. Ask the user for their age (as a number). Convert the input to int.

2. If the user is 18 or older, print a message like "You are an adult."
   Otherwise, print "You are a minor."

3. Ask the user for a number. If the number is positive, print "Positive."
   If it is zero or negative, print "Zero or negative." (Use else for zero/negative.)

4. (Optional) Ask for a password (e.g. a simple string). If the password equals a secret
   you choose (e.g. "python"), print "Access granted." Otherwise print "Access denied."
"""

# My solution below:

# 1 — Age: adult or minor
age = int(input("What's your age? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2 — Number: positive or zero/negative
number = int(input("What's your number? "))
if number > 0:
    print("Positive.")
else:
    print("Zero or negative.")

# 4 — Password check (using .strip() so spaces don't block access)
password = input("What's your password? ").strip()
if password == "python":
    print("Access granted.")
else:
    print("Access denied.")