"""
Day 3 — User input

What to study and practice in this file:
----------------------------------------
1. input()
   - input("Prompt: ") waits for the user to type and press Enter.
   - Always returns a string: result = input("Your name? ")
   - The string can be empty if user presses Enter without typing.

2. Converting input to numbers
   - int(input("Number: ")) — converts to integer (whole number).
   - float(input("Number: ")) — converts to decimal number.
   - If user types text that isn't a number, you'll get an error (we'll handle that later with try/except).

3. Storing input in variables
   - name = input("What is your name? ")
   - age = int(input("How old are you? "))
   - Then use the variables in expressions and print.

You already know: variables, data types, operators, print(). Use them together with input().

---

PROBLEM — Interactive progress report
------------------------------------
Using input(), variables, and the concepts from Day 0–2, create a short interactive script:

1. Ask the user for their name and store it in a variable.

2. Ask how many steps they have completed so far in the challenge (e.g. 3).
   Convert the answer to int and store it.

3. Ask how many minutes they studied today.
   Convert the answer to int (or float if you prefer decimals) and store it.

4. If steps_completed > 0, calculate minutes_per_step = minutes_studied / steps_completed.

5. Print a personalized message using the variables, for example:
   - "Hello, [name]! You've completed [X] steps."
   - "You studied [Y] minutes today."
   - If steps_completed > 0: "That's about [Z] minutes per step so far."
   Use f-strings or concatenation for the output.

6. (Optional) Ask for total steps in Stage 0 (e.g. 20), convert to int, compute steps_remaining and percentage_done, and print them.
"""

# My solution below:

name = input("Whats your name?")
steps_completed = int(input("How many steps you have completed so far in the challenge?"))
minutes_studied = int(input("How many minutes you studied today?"))

if steps_completed > 0:
   minutes_per_step = minutes_studied / steps_completed
   print(f"Hello, {name}! You've completed {steps_completed} steps.")
   print(f"You studied {minutes_studied} minutes today.")
   print(f"That's about {minutes_per_step} minutes per step so far.")
else:
   print(f"Hello, {name}! You haven't completed any steps yet.")
   print(f"You studied {minutes_studied} minutes today.")

#optional:
total_steps_stage0 = 20
steps_remaining = total_steps_stage0 - steps_completed
percentage_done = (steps_completed / total_steps_stage0) * 100
print(f"You have {steps_remaining} steps remaining.")
print(f"You have completed {percentage_done}% of the challenge.")