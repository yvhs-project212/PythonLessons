#!/usr/bin/env python3

# lesson5.py: Classes, objects, and object-oriented programming in Python
#   From the PythonLessons repository:
#   https://github.com/YVHS-Project212/PythonLessons
# Created by Jon Solera, December 2024
#


# An object is a programming "thingie" that has both *data* and *behavior*.
#
# An object has DATA in the form of variables -- not just the global and local
# variables that we've seen so far, but now also instance variables and
# class variables.  (We'll see these soon.)
#
# An object has BEHAVIOR in the form of methods, which are functions associated
# with classes and objects.  (Again, we'll see these soon.)
#
# Here's a simple example:

class ProgrammingLanguageName:
  """
  This is a comment about the ProgrammingLanguageName class.

  A ProgrammingLanguageName object represents the name of a programming
  language -- and absolutely nothing else about the programming language,
  only its name.
  """
  def __init__(self, language_name):
    """
    (Almost) every class in Python has a method called __init__, also known as
    a constructor.  The constructor method provides the recipe for taking
    a soon-to-be-instance of this class called "self", and making it *actually*
    an instance of this class, based on what we want the class to do.

    In this case, we want a ProgrammingLanguageName to remember the name that
    it was initialized with, so we store it in an *instance variable*.  An
    instance variable is attached to an instance of the class, so different
    instances can hold different values in their instance variables.
    """
    self.lang_name = language_name

  def name(self):
    """
    Return the name of the programming language this instance was created with.

    name() is a method -- a function connected to an object or a class.  In
    this case, name() is an instance method, because it's connected to
    instances of the class.  (Calling name() on different instances can give
    different results.)  Because of that, we need access to a parameter for
    "whatever instance happens to be calling this method".  That's the "self"
    parameter.
    """
    return self.lang_name

lang1 = ProgrammingLanguageName("Python")
lang2 = ProgrammingLanguageName("C++")

print(f"Classes and objects in {lang1.name()}")
print(f"(I don't know anything about classes and objects in {lang2.name()})")

# lang1 and lang2 are instances of the ProgrammingLanguageName class.
# Notice that invoking the name() method on the different instances gives
# different results.
#
# Remember, the class is a recipe, like a function definition.  Defining the
# class doesn't create an object, just like defining a function doesn't
# invoke the function.  Instead, objects are created when you call the
# constructor -- which you do by writing the class name followed by
# parentheses and any constructor parameters.  You can see that above where
# we define and assign lang1 and lang2.


# Okay, so that was a simple class.  What can you actually do with classes
# and objects?  Well, we can define and create "thingies" that know how to
# do the stuff we commonly want to do with them.  Here's another example:

class Rectangle:
  def __init__(self, name, length, width):
    self.name = name
    self.L = length
    self.W = width

  def area(self):
    return self.L * self.W

  def perimeter(self):
    return self.L + self.W + self.L + self.W

rect1 = Rectangle("Rectangle #1", 3, 12)
rect2 = Rectangle("Rectangle #2", 4, 5)
rect3 = Rectangle("Rectangle #3", 7, 1)

all_rectangles = [rect1, rect2, rect3]
for r in all_rectangles:
  name = r.name    # copy the instance variable "name"
  area = r.area()  # get the result of the area() method on this instance
  perim = r.perimeter() # result of the perimeter() method on this instance
  print(f"{name} has area {area} and perimeter {perim}")

# Do you see how each instance has its own data, such as its own length?
#
# Do you see how the instance methods defined in the class can return different
# values for different instances, depending on their data?


# When we use the robotpy library, hardware components such as motors or
# sensors will be instances of specific motor classes or sensor classes.  The
# good news is that whoever wrote those classes figured out the hard stuff,
# like how to send signals to turn the motor on, and made them available to us
# through methods.
#
# The bad news is that we still have to learn about the methods that those
# people wrote, and learn how to use them.
