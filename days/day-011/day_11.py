"""
Day 11 — Lists: create and access

What to study and practice in this file:
----------------------------------------
1. Creating lists
   - A list stores multiple values in order.
   - Example: numbers = [10, 20, 30]
   - Lists can store strings, numbers, booleans, and even mixed types.

2. Accessing items by index
   - Index starts at 0.
   - list[0] is the first item, list[1] the second, and so on.
   - Negative index: list[-1] is the last item.

3. Slicing lists
   - list[a:b] returns items from index a up to (not including) b.
   - list[:3] first 3 items, list[2:] from index 2 to the end.

4. len() with lists
   - len(my_list) returns how many items are in the list.

You can combine with input(), for loops, and everything from previous days.

---

PROBLEM — lists (create and access) challenge
----------------------------------------------
Using list creation, indexing, slicing, and len(), do the following:

1. Create a list with 5 favorite fruits (strings). Print the whole list.

2. Print:
   - First fruit (index 0)
   - Last fruit (index -1)

3. Print how many fruits are in the list using len().

4. Print a slice with the first 3 fruits.

5. (Optional) Ask the user for 3 numbers, store them in a list, and print:
   - The full list
   - First number
   - Last number
"""

# My solution below:

# 1
favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(favorite_fruits)

# 2
print(favorite_fruits[0])
print(favorite_fruits[-1])

# 3
print(len(favorite_fruits))

# 4
print(favorite_fruits[:3])

# 5
numbers = []
for i in range(3):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(numbers)
print(numbers[0])
print(numbers[-1])