#!/usr/bin/env python3

# lesson2.py: Python control flow
#   From the PythonLessons repository:
#   https://github.com/YVHS-Project212/PythonLessons
# Created by Jon Solera, December 2024
#

# Many types of Python statements are simply executed one after the other:
print("This is lesson ", end="")
lesson_number = 1 + 1
print(lesson_number)

# However, things get much more interesting when code can be run or skipped
# depending on whether a condition is met, or if we can create a loop that
# runs code a certain number of times instead of writing the code out that many
# times.

# Here is an example of an "if statement", also known as a conditional.  It
# has a condition, which might be true or false.  If the condition is true,
# the code inside the if statement will be executed.  If the condition is
# false, the code inside will be skipped.
#
# Note that the code inside the if statement is all *indented* -- and in
# particular, it is all indented the same amount.

test_number = 3
if test_number < 10:
  print("the condition is true")
  print("the code inside the if statement will be executed")
  print("the value of test_number is less than 10")


# If statements can have an "else" clause in addition to their "if" clause.
# Recall that the code in the "if" clause is only executed if the condition
# is true.  The "else" clause is only executed if the same condition is false.

if test_number < 5:
  print("the value of test_number is less than 5")
else:
  print("the value of test_number is NOT less than 5")
  print("...but it might be equal to 5, for all I know...")


# Try changing the value of test_number and re-running the program.  What do
# you think it will print?


# "If" statements are one kind of control flow.  Loops, including "for" loops
# and "while" loops, are another.
#
# A "for" loop executes its code once for each item.

for number in (17, 25, -3, 1000, 2.222):
  print("Here's a number:", number)

for word in ("purple", "giraffe", "angst"):
  print("Here's a word:", word)

data = [100, "Cheez Whiz (TM)", False]
for item in data:
  print("Here's some assorted data:", item)

# The range() function returns a range of integers from the start number
# (default 0) up to BUT NOT INCLUDING the end number.  What do you think the
# following examples will print?

for number in range(5):
  print(number, "is in the first range")

for number in range(1, 11):
  print(number, "is in the second range")

for number in range(10):
  if number < 3 or number > 7:
    print(number, "is toward one end of the range")
  # There is no "else" clause
  # If the condition is false, nothing will happen (nothing will be printed)


# A "while" loop has a condition which can be true or false, and it executes
# the code in its loop until the condition is false.

total = 0
current_number = 0
while total < 30:
  current_number += 1      # shorthand for "total = total + current_number"
  total += current_number

  # Let's use formatted strings...
  print(f"adding {current_number} to the total, which is now {total}...")

print(f"The total finally went over 30 when we added {current_number}")

# Use a for loop when you know exactly what list you're iterating over, or
# exactly how many times you'll be doing it.  (Even if the number of times
# is a variable.)
#
# Use a while loop when you don't know how many times, so you have to keep
# going until some condition is met.
#

# You can break out of loop before it's finished, by using the "break"
# command.  You can skip the rest of this iteration using the "continue"
# command.  What do you think the next loop will print?

for i in range(1000):
  if i == 3:
    continue
  if i == 5:
    break
  print(f"Iteration number {i} was normal")


# Let's try the adding-numbers-to-total-100 problem again, but stop just before
# we get over 100...
total = 0
current_number = 0
while total < 30:
  current_number += 1
  if (total + current_number > 30):
    break
  total += current_number
  print(f"adding {current_number} to the total, which is now {total}...")

print(f"The total would go over 30 if we added {current_number}")
