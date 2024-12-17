# Lesson 3: Python variables and data types

## Look at the sample program

Load up the sample program using a text editor.  Read through the comments,
and the code.  What do you understand about the program?  What still isn't
clear?

See if you can predict *exactly* what the program will print.

## Run the sample program

1. Use `cd` to change into the `Lesson3/` directory.
1. From a terminal window (such as a Git Bash window), run `py -3 ./lesson3.py`

How close was your guess to what the computer actually printed?

## Exercises

1. Normally `print("Hello")` prints a new line at the end, so that the next
   thing that gets printed appears on the next line.  However, you can add
   an optional parameter `end` to the function call that will override this
   behavior.  `print("Hello ", end="")` doesn't print the new line, and if
   you follow that with `print("Ebenezer")`, then your program will print
   `Hello Ebenezer`.  (Note the space in `print("Hello ", end="")`!  Without
   that space, you'll see `HelloEbenezer`.)

   With that knowledge, write a program that uses a `for` loop to print
   the numbers from 1 to 50, ten to a line.  In other words, your program
   should print
   ```
   1 2 3 4 5 6 7 8 9 10
   11 12 13 14 15 16 17 18 19 20
   21 22 23 24 25 26 27 28 29 30
   31 32 33 34 35 36 37 38 39 40
   41 42 43 44 45 46 47 48 49 50
   ```


2. Write a program to construct a dictionary that maps the first 100
   integers to their squares.  Sure, you *could* write
   ```
   my_map = {}    # you have to define my_map to be a dictionary first!
   my_map[1] = 1
   my_map[2] = 4
   my_map[3] = 9
   ...
   ```
   But that would get really boring.  Use loops instead.


3. Let's say you had a list of integers, such as
   ```
   [ 3, 0, 10, -2, 0, 1, 1, 0, 5, 0 ]
   ```
   You want to produce a list of boolean values, which will each be `False`
   if the corresponding integer is zero, and `True` if the corresponding
   integer is non-zero.  In this case, you're hoping to produce the list
   ```
   [ True, False, True, True, False, True, True, False, True, False ]
   ```
   ... but in an automated way.  Write a program that starts with
   ```
   integer_list = [ 3, 0, 10, -2, 0, 1, 1, 0, 5, 0 ]
   ```
   and then constructs a variable called `boolean_list`, which should end up
   having the value above.

3. Write a program to construct a dictionary that maps the first 100
   integers to their squares.  Sure, you *could* write
   ```
   my_map = {}    # you have to define my_map to be a dictionary first!
   my_map[1] = 1
   my_map[2] = 4
   my_map[3] = 9
   ...
   ```
   But that would get really boring.  Use loops instead.

