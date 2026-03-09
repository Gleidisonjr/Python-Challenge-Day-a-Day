"""
Day 10 — break and continue

What to study and practice in this file:
----------------------------------------
1. break
   - Exits the loop immediately. No more iterations.
   - Used when you find what you were looking for, or hit a "stop" condition.
   - Works in both for and while loops.

2. continue
   - Skips the rest of the current iteration and goes to the next one.
   - Used when you want to ignore certain values (e.g. skip even numbers, skip empty input).
   - The loop keeps running; only this turn is skipped.

3. Typical use of break
   - Search: loop until you find something, then break.
   - "Exit when user types 'quit'": if word == "quit": break

4. Typical use of continue
   - Filter: if condition: continue  then do something with the rest.
   - Skip invalid input and ask again.

You can combine with for, while, if, and everything from previous days.

---

PROBLEM — break and continue challenge
-------------------------------------
Using break and/or continue (with for or while), do the following:

1. Use a for loop over range(10). Print each number, but use break to stop when
   you reach 5 (so you print 0, 1, 2, 3, 4 and then exit). Don't print 5.

2. Use a for loop over range(10). Use continue to skip printing when the number is
   even (so you only print 1, 3, 5, 7, 9). Hint: if n % 2 == 0: continue

3. Ask the user for numbers one by one in a while loop. Keep asking until they
   type 0 (then break and print "Done."). For each non-zero number, print "You entered: ...".

4. (Optional) Use a for loop over range(1, 11). Print each number, but use continue
   to skip 3 and 7 (so you print 1, 2, 4, 5, 6, 8, 9, 10).
"""

# My solution below:

#1
for i in range(10):
   if i == 5:
      break
   print(i)

#2
for i in range(10):
   if i % 2 == 0:
      continue
   print(i)

#3
while True:
   number = int(input("Enter a number (0 to stop): "))
   if number == 0:
      break
   print("You entered:", number)
print("Done.")

#4
for i in range(1, 11):
   if i == 3 or i == 7:
      continue
   print(i)