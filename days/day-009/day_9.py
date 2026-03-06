"""
Day 9 — Loop: while

What to study and practice in this file:
----------------------------------------
1. while loop
   - Repeat a block of code as long as a condition is True.
   - while condition:
         # code here
   - Before each repetition, Python checks the condition. If False, the loop stops.

2. Condition to stop the loop
   - The condition must eventually become False, or the loop runs forever (infinite loop).
   - Usually you change a variable inside the loop so the condition becomes False (e.g. increment a counter).

3. Typical pattern: counter
   - count = 0
   - while count < 5:
         print(count)
         count = count + 1   # or count += 1
   - Same idea as for i in range(5):, but with while you control the condition.

4. When to use while vs for
   - for: when you know how many times to repeat or you're iterating over a sequence.
   - while: when you repeat until a condition is met (e.g. "keep asking until user types 'quit'").

You can combine with input(), if, variables, and everything from previous days.

---

PROBLEM — while loop challenge
------------------------------
Using while (and optionally input), do the following:

1. Use a while loop to print the numbers 0, 1, 2, 3, 4 (one per line). Use a variable
   (e.g. i) that starts at 0 and add 1 each time until it reaches 5.

2. Ask the user for a number n. Use a while loop to print "Hello" n times (each on a
   new line). Use a counter that goes from 0 to n-1 (or 1 to n).

3. Use a while loop to print the numbers from 5 down to 1 (5, 4, 3, 2, 1). Start at 5
   and subtract 1 each time until you reach 0.

4. (Optional) Ask the user to type a word. Use a while loop to keep asking until they
   type "quit" (then stop). Each time they type something else, print "You said: ..."
   and ask again. Use a variable to store the input and make the condition something
   like while word != "quit".
"""

# My solution below:

#1 
i = 0 
while i < 5: 
   print(i)
   i += 1

#2
n = int(input("Enter a number by 1 between 100:"))
if n > 0 and n <= 100:
   i = 0
   while i < n:
      print("Hello")
      i += 1
else:
   print("Number is not between 1 and 100")

#3
i = 5
while i > 0:
   print(i)
   i -= 1

#4 
word = input("Enter a word:")
while word != "quit":
   print("You said: ", word)
   word = input("Enter a word:")
else:
   print("You typed quit")