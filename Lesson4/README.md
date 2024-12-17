# Lesson 4: Functions in Python

## Look at the sample program

Load up the sample program using a text editor.  Read through the comments,
and the code.  What do you understand about the program?  What still isn't
clear?

See if you can predict *exactly* what the program will print.

## Run the sample program

1. Use `cd` to change into the `Lesson4/` directory.
1. From a terminal window (such as a Git Bash window), run `py -3 ./lesson4.py`

How close was your guess to what the computer actually printed?

## Exercises

1. If `mystr` is a string, you can get its length with `len(mystr)`.  Try it
   in the interactive Python environment:
   ```
   py -3
   >>> mystr = "Hi there"
   >>> len(mystr)
   8
   ```
   (Note that the space counts as part of the string length!)

   Now let's shout a bunch of words near a wall that causes an echo only for
   long words.  So if you shout "Hi", you'll hear "Hi"  But if you shout
   "Salutations", you'll hear "SalutationsSalutations".  Words echo if their
   length is at least 8.

   Here's a good chunk of a program:
   ```
   words = ["Hi", "Hello", "Greetings", "Robotics", "Program"]
   for word in words:
     if requires_echo(word):
       print(repeated(word))
     else:
       print(word)
   ```
   You'll notice that there are two functions that aren't defined anywhere,
   so that little program won't currently work.  (Those functions are
   `requires_echo()` and `repeated()`.  They don't exist.)

   Copy that code and write the missing functions.  That means that above
   the code you copy, you'll need to define a function named `requires_echo`
   that takes one string parameter and returns a boolean which will be `True`
   if the word requires an echo (if its length is at least 8) and `False`
   if not.  And you'll need to define a function named `repeated` that also
   takes one string parameter, and returns a string containing that parameter
   repeated.

   Test your program!  Its output should be
   ```
   Hi
   Hello
   GreetingsGreetings
   RoboticsRobotics
   Program
   ```
