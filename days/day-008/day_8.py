"""
Day 8 — Loop: for and range()

What to study and practice in this file:
----------------------------------------
1. for loop
   - Repeat a block of code for each item in a sequence.
   - for item in sequence:
         # code here (use item)

2. range()
   - range(n)        → 0, 1, 2, ..., n-1  (n numbers, starts at 0)
   - range(a, b)     → a, a+1, ..., b-1   (from a up to but not including b)
   - range(a, b, step)  → a, a+step, ...   (optional step, can be negative)
   - Often used with for:  for i in range(5):  → i is 0, 1, 2, 3, 4

3. Iterating over a sequence
   - Strings:  for char in "hello":   → char is "h", "e", "l", "l", "o"
   - Lists (you'll see more in Day 11):  for x in [1, 2, 3]:  → x is 1, then 2, then 3

4. Indentation
   - Everything you want to repeat must be indented under the for line.

You can combine with print(), variables, conditionals, and everything from previous days.

---

PROBLEM — for loop challenge
----------------------------
Using for and range() (and optionally iterating over a string), do the following:

1. Use a for loop and range(5) to print the numbers 0, 1, 2, 3, 4 (one per line).

2. Use a for loop and range(1, 6) to print the numbers 1, 2, 3, 4, 5 (one per line).

3. Ask the user for a number n. Use a for loop and range(n) to print "Hello" n times
   (each "Hello" on a new line). Remember to convert input to int.

4. Use a for loop to iterate over the string "Python" and print each character on a
   separate line (so you'll see P, then y, then t, etc.).

5. (Optional) Ask the user for a word. Use a for loop to print each character of the
   word on one line, separated by spaces (e.g. "hi" → "h i"). Use end=" " in print()
   to avoid a newline, and add a final print() for the newline at the end.
"""

# My solution below:

# 1 
for i in range(5):
   print(i)

# 2 
for i in range(1, 6):
   print(i)

# 3
n = int(input("Enter a number:"))
for i in range(n):
   print("Hello")

# 4
for i in "Python":
   print(i)

# 5 
word = input("Enter a word:")
for i in word:
   print(i)
   print()
print()