"""
Day 5 — Strings (methods)

What to study and practice in this file:
----------------------------------------
1. .strip()
   - Removes whitespace (spaces, tabs, newlines) from both ends.
   - "  hello  ".strip()  →  "hello"
   - .lstrip() and .rstrip() for left or right only.

2. .split()
   - Splits a string into a list of substrings.
   - "a b c".split()  →  ["a", "b", "c"]  (default: split on whitespace)
   - "a,b,c".split(",")  →  ["a", "b", "c"]  (split on comma)

3. .upper() and .lower()
   - "Hello".upper()  →  "HELLO"
   - "Hello".lower()  →  "hello"
   - Useful for comparing text without caring about case.

4. .replace(old, new)
   - Replaces all occurrences of old with new.
   - "hello world".replace("world", "Python")  →  "hello Python"

5. Other useful methods (optional)
   - .startswith("x"), .endswith("x"), .count("x"), .find("x")

You can combine with input(), indexing, slicing, and f-strings from previous days.

---

PROBLEM — String methods challenge
---------------------------------
Using .strip(), .split(), .upper(), .lower(), and .replace(), do the following:

1. Ask the user to type a sentence (with possible extra spaces at the start or end).
   Store it in a variable. Use .strip() to get a cleaned version and print it.

2. Using .split(), split the sentence into a list of words. Print the list and the number of words (use len()).

3. Using .upper() and .lower(), print:
   - The sentence in all uppercase.
   - The sentence in all lowercase.

4. Ask the user for a word to replace and a replacement word (two inputs).
   Use .replace() to replace the first word with the second in the sentence, and print the result.

5. (Optional) Using .split() and indexing, print the first word and the last word of the sentence.
   Use .strip() when reading input so extra spaces don't create empty "words".
"""

# My solution below:    

#1 Using .strip()
sentence = input("Whats your sentence?")
cleaned_sentence = sentence.strip()
print(cleaned_sentence)

#2 — Using .split()
list_of_words = cleaned_sentence.split()
print(list_of_words)
print(len(list_of_words))

#3 Using .upper() and .lower()
print(sentence.upper())
print(sentence.lower())

#4 Using .replace() — .replace() returns a new string; assign it to see the result
word_to_replace = input("Whats the word to replace?").strip()
replacement_word = input("Whats the replacement word?").strip()
sentence = sentence.replace(word_to_replace, replacement_word)
print(sentence)

#5 First and last word (use the list from .split(), not sentence[0]/[-1] which are characters)
print(list_of_words[0])
print(list_of_words[-1])