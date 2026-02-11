"""
Day 1 — Data types

What to study and practice in this file:
----------------------------------------
1. int (integer)
   - Whole numbers: 0, 42, -7
   - Create variables and use them in expressions.

2. float (floating-point)
   - Numbers with decimals: 3.14, -0.5, 2.0
   - Try arithmetic: division often gives float.

3. str (string)
   - Text in quotes: "hello", 'world', 
   - You already used these in Day 0.

4. bool (boolean)
   - True or False (capital T and F).
   - Often come from comparisons: 5 > 3  →  True

5. list
   - Ordered, mutable sequence: [1, 2, 3], ["a", "b"], []
   - Create lists, index them, check type.

6. tuple
   - Ordered, immutable sequence: (1, 2), ("x",), ()
   - Often used for fixed pairs or multiple return values.

7. range
   - range(stop), range(start, stop), range(start, stop, step)
   - Used in for loops; use list(range(...)) to see the numbers.

8. dict (dictionary)
   - Key/value mapping: {"name": "Gleidison", "age": 26}
   - Access by key: my_dict["name"], check type.

9. type()
   - type(value) tells you the type: type(42)  →  <class 'int'>
   - Use it to check your variables.

Practice: create variables of each type, print them, and use type() to show their types.
"""

# My code below:

x = 1  #integers
z = 1.1  #floats
meu_nome = "Gleidison" #string
true_or_false = True #boolean
my_list = [1, 2, 3] #list
my_tuple = (1,2,3) #tuple
my_range = range(10) #range
my_dictionary = {"name": "Gleidison", "age": 26, "job": "Data Scientist and Data Analyst"} #dictionary
type_x = type(x) #type of x

#printing the variables and their types
print("My integer is: ", x)
print("My type is: ", type(x))
print("My float is: ", z)
print("My type is: ", type(z))
print("My string is: ", meu_nome)
print("My type is: ", type(meu_nome))
print("My boolean is: ", true_or_false)
print("My type is: ", type(true_or_false))
print("My list is: ", my_list)
print("My type is: ", type[int](my_list))
print("My tuple is: ", my_tuple)   
print("My type is: ", type[tuple](my_tuple))
print("My range is: ", my_range)   
print("My type is: ", type[range](my_range))
print("My dictionary is: ", my_dictionary)
print("My type is: ", type[dict](my_dictionary))