#!/usr/bin/env python3

# lesson3.py: Python variables and data types
#   From the PythonLessons repository:
#   https://github.com/YVHS-Project212/PythonLessons
# Created by Jon Solera, December 2024
#

# Python has many different data types, and sometimes we need to know
# exactly what type of data we're dealing with.  Python data types include:
#
# * integers, like 3 or 1000000 or -78 or 0
# * "floats", which are decimal numbers like 1.234 or -17.0 or 0.0000008
# * strings, like "Hi" or "This is a string" or "" (the empty string)
# * booleans, which are either True or False
# * lists, such as [1, 11, 111, 234]
#
# There are also some others that you haven't seen yet, including dictionaries,
# objects, functions, the special "None" data type, and more.  We'll get there.

print("Some things about integers...")

# You know you can do arithmetic with integers, like adding and multiplying.
# You know that "*" means "times", and "/" means "divided by".
# Here's something that's probably new:
#   "%" means "modulo", which means "the remainder after you divide by"
#
# Here's how it works:
#   503 % 100 == 3
#     ... because when you divide 503 by 100, the quotient is 5 (we don't care)
#         and the remainder is 3
#   38 % 10 == 8
#   28 % 10 == 8
#   18 % 10 == 8
#    8 % 10 == 8   ... you might see a pattern here...

# What do you think the following loop will print?

for i in range(16):
  print(f"{i} % 3 is {i % 3}")


# You can use % to do something once every however-many times
for i in range(10):
  if i % 5 == 0:
    print("--- NEW GROUP OF 5 ---")
  print(f"Iteration #{i}")


# You can use an integer to get a specific element of a list.  A float won't
# work, even if its value is an integer!
#
# The first element in a list is element number 0.  That means that the last
# element in a 10-element list is number 9, and there is no element number 10!
# Hmm, maybe that's why the range() function works the way it does...

my_list = ["red", "orange", "yellow", "green", "blue", "violet"]
print(f"Element number 0 in the list is: {my_list[0]}")
print(f"Element number 2 in the list is: {my_list[2]}")

# Unexpected situations called "exceptions" can cause programs to stop running.
# If you know you might have an exception, you can use a try/except block
# to "catch" the exception.  There are many kinds of exceptions, and it's best
# to specify exactly what kind of exception you're expecting.

try:
  # This should bomb, because the index to my_list isn't an integer!
  bad_result = my_list[1.0]
  print("The program should never get here!")
except TypeError as e:
  # We know we might get a TypeError.  If we do, catch it, and save the
  # exception in a variable we'll name "e".  We can look at the exception
  # later if we want.
  print("Indexing a list with a float generated an exception, as we expect.")


print("Some things about strings...")

# You can index strings (get the Nth element) just like lists
s = "hi there"
print(f"The first letter of the string is {s[0]}")
print(f"The second letter of the string is {s[1]}")

# You can concatenate strings (glue them together) using the + operator
print(f"The string s is: {s}")
s = s + ", everyone"
print(f"Now the string s is: {s}")


print("Some things about booleans...")

# Boolean values are logic values: True or False.  (You need to use the capital
# letter!)  Conditions in "if" and "while" statements have boolean values.
# You can assign boolean values to a variable and use that variable in
# conditions, if you want.

boolean1 = True
boolean2 = (1 < 3)   # is this True or False?
boolean3 = (1 > 3)   # is this True or False?

if boolean1:
  print("boolean1's condition evaluated to True")

if boolean2:
  print("boolean2's condition evaluated to True")

if boolean3:
  print("Wait, somehow 1 is greater than 3?!")
else:
  print("boolean3's condition evaluated to False")

# You can perform logic operations on Boolean values

boolean4 = boolean1 and boolean2

if ((boolean1 and boolean2) or boolean3):
  print("The complicated condition was True.")
  print(f"The value of boolean4 is {boolean4}")
  print(f"The value of 'not boolean1' is {not boolean1}")
else:
  print("The complicated condition was False, which it shouldn't be!")


print("Some things about lists, tuples, and dictionaries...")

# A list can hold any type of data, but usually it makes sense for it to hold
# the same type in each element.

my_list = [False, 17, "poodle"]   # Allowed, but usually not helpful
print(f"my_list is {my_list}")

# Lists are *mutable* -- they can be changed in place
my_list[1] = -5
print(f"now my_list is {my_list}")

# In addition to using an index to pick out a specific element in a list,
# you can also grab a range of elements.  my_list[10:15] grabs elements number
# 10 through 14 (!!!) from my_list.

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
print(f"The middle two colors are: {colors[2:4]}")



# A tuple is like a list, but immutable.  Tuples have (parentheses), instead
# of [brackets] like a list.

my_tuple = (False, 17, "poodle")
print(f"my_list is {my_list}")

try:
  my_tuple[1] = -5
  print("The program should never print this, since tuples are immutable!")
except TypeError as e:
  print("Trying to change a tuple raised a TypeError, which it should")


# You can still "change" a tuple by using it to construct a different one

my_new_tuple = ("new", "tuple") + my_tuple
print(f"my_new_tuple is {my_new_tuple}")

# You can reassign a tuple variable to point to a different tuple.  The rule is
# just that you can't modify a tuple in place.

my_new_tuple = my_new_tuple[0:2]
print(f"now my_new_tuple has been reassigned to be {my_new_tuple}")


# A dictionary maps one set of stuff, called "keys", to another set of stuff,
# called "values".  Keys must be immutable, so they can't be lists.
# Dictionaries are defined in place with braces, but indexed with brackets
# just like lists or tuples.

acronyms = {
  "AAA": "American Automobile Association",
  "CD": "Compact Disc",
  "USA": "United States of America",
  "YVHS": "Ygnacio Valley High School",
}

for key in acronyms:
  long_name = acronyms[key]
  print(f"'{key}' stands for {long_name}")
