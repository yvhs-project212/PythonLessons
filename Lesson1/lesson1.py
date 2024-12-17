#!/usr/bin/env python3

# Python ignores everything after a pound sign (#) on a line.
# These are "comments" -- useful for humans, ignored by computers.
#
# You can use comments to help other people understand your code, or to add
# information such as the purpose of the program or who wrote it, like this:
#
# lesson1.py: Introductory Python script from the PythonLessons repository
#   https://github.com/YVHS-Project212/PythonLessons
# Created by Jon Solera, December 2024
#

print("Python Lesson 1")  # I bet you can guess what this does!

# You can create variables and assign values to them, like this:
my_name = "Ebenezer"

# my_name is now a "string" variable, meaning that it contains text (as opposed
# to containing numbers, or logic values like True or False, or anything else).
# A string is a bunch of text, from a single keystroke up to pages and pages.
# The value of my_name does NOT include the quote marks.  You can even have an
# empty string, like this: ""

# You can perform operations on variables.  For integer variables or
# floating-point (decimal) variables, you can perform arithmetic on them, for
# example.  For string variables, you can do things like concatenate them (i.e.
# glue them together to make a longer string).

greeting = "Hello, " + my_name   # What value do you think greeting contains?

# Look at the print command below.  There are no quote marks.  Do you think
# it will print the word "greeting", or the value of the variable that is
# named greeting?

print(greeting)

# Let's look at some string variables and numeric variables
num1 = 3
num2 = 4
num3 = num1 + num2
num4 = num1 * num2   # "*" means "times"

# You can just print out a bunch of things separated by commas
print("The numbers are:", num1, num2, num3, num4)

# What do you think this program will print out?  Run the program to find out
# if you're correct.  Use "cd" to change into the Lesson1/ directory, and then
# run the following (if you're on Windows):
#
# py -3 lesson1.py
#
# (Don't type a pound sign at the command line -- that is only here to create
# a comment!)
