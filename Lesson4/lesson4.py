#!/usr/bin/env python3

# lesson4.py: Functions in Python
#   From the PythonLessons repository:
#   https://github.com/YVHS-Project212/PythonLessons
# Created by Jon Solera, December 2024
#

# A function is a software recipe.  It accepts inputs (called "parameters" or
# "arguments") and defines how to do something with those inputs and optionally
# produce an output and return that value.  Here's a simple example:

def add_two_numbers(first, second):
  result = first + second
  return result

# Notice that we haven't added any numbers yet -- we've just provided
# instructions for what to do if adding two numbers is requested!  In other
# words, we've only *defined* the function so far, we haven't *called* or
# *invoked* it yet.

result1 = add_two_numbers(3, 4)
print(f"The result of add_two_numbers(3, 4) is {result1}")

result2 = add_two_numbers(1, 1)
print(f"The result of add_two_numbers(1, 1) is {result2}")


# Do you see how defining the function just provides the recipe, and it can't
# actually run, because its parameters don't have values?  And how we can
# invoke the function by passing in parameters -- such as add_two_numbers(3, 4)
# -- and then it makes sense to talk about what value gets returned?



# Functions allow you to provide a string of documentation, which is a good
# idea.  Here's how that function might look with good documentation:

def add_two_numbers_with_good_documentation(first, second):
  """
  Return the result of adding two input numbers.

  Parameters:
    first (int or float): The first of the two numbers to add
    second (int or float): The second of the two numbers to add

  Returns:
    (int or float) the sum of the two input numbers

  Notes:
   * It is the responsibility of the caller to make sure that only compatible
       data types are passed in!
   * This function will use the + operator on any two inputs, but the result
       may not be addition!  For example,
       add_two_numbers_with_good_documentation("2", "3") will return "23",
       which probably isn't what you want!
  """
  result = first + second
  return result

# Note that good documentation for a function explains what kinds of parameters
# it's expecting, and what data type it will return, and any notes or gotchas
# about what the function does!
#
# Also note that function documentation is a string provided as the first
# non-comment line of the function, and multi-line strings can be created
# and terminated with triple quotes.


# Functions don't have to return anything.  A function that doesn't return
# a value typically just performs a task.  Here's an example:

def print_info_message(msg):
  print(f"***INFO*** {msg}")


print("A few things to know about SCOPE...")

# "Scope" is the issue of where a variable exists -- in what parts of the code
# does that variable have a value?  For example, we could print the variable
# called "msg" a few lines above.  Do you think it would work if we wrote
#
#   print(f"msg = {msg}")
#
# below this comment?  If you guessed "no", you were right.  But why not?  It
# was allowed just a few lines above.  The answer is that the variable "msg"
# is now out of scope.  It was only in scope for the duration of the
# print_info_message() function.
#
# As a general guideline, variables are only in scope for the rest of the
# "block" where they are defined.  (A block is a chunk of indented text.)

# Why does the code below not work?
try:
  def number_after(my_parameter):
    next_num = my_parameter + 1
    return next_num

  return_value = number_after(7)
  print(f"return_value was {return_value}")
  print(f"my_parameter was {my_parameter}")
  print(f"next_num was {next_num}")

except NameError as e:
  print("A NameError was raised!  Probably using some out-of-scope variable...")

