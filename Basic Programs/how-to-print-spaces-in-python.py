# While writing the code, sometimes we need to print the space. For example, print space between the message and the values, print space between two values, etc. In the Python programming language, it's easy to print the space.

# Following are the examples demonstrating how to print the spaces in Python?

# Printing spaces in Python
# There are multiple ways to print space in Python. They are:

# Give space between the messages
# Separate multiple values by commas
# Declare a variable for space and use its multiple
# 1) Give space between the messages
# The simple way is to give the space between the message wherever we need to print space in the output.

# Example 1: A simple way to print spaces

print(' ')
print(" ")
print("Hello world!")
print("Hello         world")

# Output
# Hello world!
# Hello         world


# 2) Separate multiple values by commas
# When we print multiple values separated by the commas (,) using the print statement – Python default print a between them.

# Example 2: Printing spaces between two values while printing in a single print statement
x = 10
y = 20

print("x:",x)
print("y:",y)

# Output
# x: 10
# y: 20


# 3) Declare a variable for space and use its multiple
# To give multiple spaces between two values, we can assign space in a variable, and using the variable by multiplying the value with the required spaces. For example, there is a variable space assigned with space and we need to print 5 spaces - we can use space*5 and it will print the 5 spaces.

# Example 3: Give multiple spaces between two values
x = 10
y = 20

space = ' '

'''
  2 spaces would be here
  1 space after first parameter,
  1 space by using space variable
  1 space after second parameter
'''
print("Hello",space,"world")

'''
  7 spaces would be here
  1 space after first parameter,
  5 space by using space*5
  1 space after second parameter
'''
print("Hello",space*5,"world")

'''
  12 spaces would be here
  1 space after first parameter,
  10 space by using space*10
  1 space after second parameter
'''
print("Hello",space*10,"world")

# for better better understanding
# assign space by any other character
# Here, I am assigning '#'
space = '#'
print("Hello",space,"world")
print("Hello",space*5,"world")
print("Hello",space*10,"world")

# printing values of x and y with spaces
space = ' '
print("x:",space*10,x)
print("y:",space*10,y)

# Output
# Hello   world
# Hello       world
# Hello            world
# Hello # world
# Hello ##### world
# Hello ########## world
# x:            10
# y:            20