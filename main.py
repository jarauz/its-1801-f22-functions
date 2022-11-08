"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

# Since casper is not inside a function
# it is a global variable
casper = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)

# When you want to use functions, you need to
# define them first in Python
# We will create a function called redTriangle
# Now we will add an argument to our function to
# change the length of the side
def redTriangle(side):
  casper.color('red')
  casper.forward(side)
  casper.left(120)
  casper.forward(side)
  casper.left(120)
  casper.forward(side)
  casper.left(120)

# A function does not do anything until you call it
# So let's call our function

redTriangle(50)
casper.goto(20,0)
redTriangle(75)
casper.goto(40,0)
redTriangle(45)
  