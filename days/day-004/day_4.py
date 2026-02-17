"""
Day 4 — Strings (basics)

What to study and practice in this file:
----------------------------------------
1. Concatenation
   - Join strings with +: "Hello" + " " + "world"  →  "Hello world"
   - Only works with strings; use str(42) to convert a number to string for concatenation.

2. f-strings
   - f"Text {variable} more text" — variable is inserted inside the braces.
   - f"Result: {x + y}" — expressions work inside braces.
   - You used these in Day 0.

3. Indexing
   - s[0] is the first character, s[1] the second, etc.
   - s[-1] is the last character, s[-2] the second-to-last (negative index from the end).

4. Slicing
   - s[start:stop] — characters from index start up to (but not including) stop.
   - s[:3] — from start to index 3.  s[2:] — from index 2 to end.
   - s[::2] — every 2nd character (step).  s[::-1] — reverse the string.

You can combine with input(), variables, and print() from previous days.

---

PROBLEM — String basics challenge
---------------------------------
Using concatenation, f-strings, indexing, and slicing, do the following:

1. Ask the user for their first name and last name (two input() calls). Store in variables.

2. Using concatenation (+), create full_name = first_name + " " + last_name and print it.

3. Using an f-string, print: "Welcome, [full_name]! You're on Day 4 of the Python Challenge."

4. Using indexing, print:
   - The first character of first_name.
   - The last character of last_name.

5. Using slicing, create and print:
   - The first 3 characters of first_name (e.g. "Gle" from "Gleidison").
   - The last 2 characters of last_name.
   - (Optional) full_name in reverse using a slice.

6. Using an f-string with a slice inside the braces, print something like:
   "Your initials: [first letter of first_name][first letter of last_name]."
"""

# My solution below:

#1 and 2
first_name = input("Whats your first name?")
last_name = input("Whats your last name?")
concatenation = first_name + " " + last_name
print(concatenation)

#3
print(f"Welcome, {concatenation}! You're on Day 4 of the Python Challenge.")

#4
print(f"The first character of {first_name} is {first_name[0]}")
print(f"The last character of {last_name} is {last_name[-1]}")

#5
first_3_characters = first_name[0:3] #slicing the first 3 characters
last_2_characters = last_name[-2:] #slicing the last 2 characters
reverse_full_name = concatenation[::-1] #reversing the full name  

#6
print(f"The first 3 characters of {first_name} are {first_3_characters}")	
print(f"The last 2 characters of {last_name} are {last_2_characters}")
print(f"The full name in reverse is {reverse_full_name}")