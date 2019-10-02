#%% [markdown]
# # Lab 1: Programming Concept Review
# In this lab, you will practice using Python by first modifying code to achieve
# certain results. At the end of this lab, you will have written a new function
# based on a set of requirements. 

#%% [markdown]
# ## Completing Labs
# This lab is available as a Jupyter Notebook file (.ipynb). You can import it
# into Visual Studio Code and see the file as a python file. This can be done
# through the command pallette (Ctrl+Shift+P on Windows, Command+Shift+P on Mac
# and select "Python: Import Jupyter Notebook")
#
# You should complete the lab by making modifications to the code in each cell.
# Run each cell in VS Code (or in Jupyter) both before and after modifying the
# code.
#
# You can run a cell by either clicking the "Run Cell" link above the cell or by
# holding ctrl (command on bac) and pressing enter.
#
# ## Modifying Code
# Instructions to modify code is provided after the initial code, beginning with
# the phrase "ON YOUR OWN:". The expected output will be provided where it makes
# sense.

#%% [markdown]
# # Values
#
# In programming, the term "value" means a piece of data. They can be one of
# four simple types:
# ## *Numbers*
# integer (`int`, which represents a positive or negative whole number, like -1
# or 100), or a real number (`float`, which is a representation of a fractional
# number with a decimal part, such as `1.2`). 
#
# Strings are also simple values in python, and are given the type identifier
# `str`. 
# The four types are:
# - *String*: (`str`): A sequence of characters using single quotes ('')
# - *Integer*: (`int`): integer
# - *Float*: (`float`): floating point number
# - *Boolean*: (`bool`): Either `True` or `False`, useful for conditional expressions.

#%% [markdown]
# ON YOUR OWN: Type an example value for each of the four types of values in this cell below each comment: 
# string
# int
# float
# bool

#%%
print("Hello World, I'm a string!")
print("'3' an integer")
print("'2.5' is a float")
print("'true' is a boolean")

#%% [markdown]
# # Types
# You can discover the type of any value by using the method "type." Methods are
# "invoked" or "called" by use of parens: 

#%%
type(5) # Will print the "int" to the console. 

#%% [markdown]
# # Variables
# In programming, variables are names that specify a location for values. For
# instance, this statement creates a place with the name `a` and *assigns* or
# *initializes* it to the value 5

#%%
a = 5
#%% [markdown]
# If you enter a variable without first defining it, you will receive a NameError:

#%%
# *ON YOUR OWN:* Assign an integer to the variable `b` above so that no error
# will result and re-run this cell.
b=6
try:
    if(type(b)==type(0)):
        print("Well done.")
    else:
        print("b is not assigned a value of an integer type")
except:
    print("Make sure to initialize b to a value in the session")

#%% [markdown] 
#
# The variable `a` can be assigned another value later, as each instruction is
# executed one after the next. The "=" symbol, which in math denotes equality,
# is used in the "assignment" statement. When you read the following line, read
# it as "a is assigned the value 6"
a = 6
print(a)

#%% [markdown]
# *ON YOUR OWN:* Add additional lines of code below that assign and then print the value of a with the following values:
# - "Hello World"
# - 42.0 
# - True
#%%
x="Hello World"
y=42.0
z="true"
print(x, y, z)

#%% [markdown]
# # Expressions
# Expressions are instructions to combine one or more variables or values.
# Simple expressions include arithmetic expressions that produce the result:
# The following expression will produce the value 8 using the "+" (integer addition) operator
3+5
# # Parentheses
# You can also force the program to evaluate expressions in a particular order
# using parentheses. For instance, the following two lines result in different
# orders of execution:
print(10/2+3)
print(10/(2+3))

#%% [markdown] 
# # Operators
# Operators are one or more characters that designate a particular operation.
# These include "+", "-", "/" and "*", but also include the function call
# operator `()` and the member operator
#

#%% [markdown]
# # Functions
# Functions are bundles of code that can be executed multiple times. They are
# "called" using a list of *arguments*. For instance, `print()` takes one or
# more arguments and prints the values to the output
print("This is the result of a function call")
# The function `print()` does not return a value. Instead, it causes the
# argument to appear in the output of the program. This is an important
# distinction, as you will not be able to combine functions with no output in
# the same way as you can combine those that return a value.

#%% [markdown]
# ## Defining a function
# The function below, `my_print`, will execute the single instruction when it is called.
# To define a function, use the following syntax:
def my_print():
    print("Function called")

#%% [markdown]
# ## Calling a function
# To call a function that has previously been defined, you use the name of the function:
my_print()

#%% [markdown]
# ## Return values
# A function can *return* a value. This means that where the function was
# called, the value is substituted. For a simple example, the function below, `return_four`
# returns the integer 4. Its return value can be used in arithmetic expressions.
def return_four():
    return 4
return_four()

#%% [markdown] We can show that calling the function `return_four` can be used
# in expressions by printing an expression that adds 3 to the returned value.
print(3+return_four())

#%% [markdown] 
#
# *ON YOUR OWN:* Write a function that returns the string "!" (exclamation),
# called "exclaim", and use it to concatenate the returned value to the string
# "Hello World" in a print statement.

#%% [markdown]
# ## Parameters and Arguments
# A *parameter* is the local variable that is associated with a function. The
# function `f1` below has a single parameter, and it adds 1 to the value passed
# in as an argument.
def f1(parameter1):
    return parameter1+1
f1(1) # 1 is passed in as an argument to the function, and is bound to the local variable `parameter1

#%% [markdown] 
#
# *ON YOUR OWN:* In this cell, Modify the function `multiply_2` to accept two
# arguments and returns the result of multiplying them together. You may name
# the arguments anything you want

#%% [markdown]
# # Conditionals and Tests
# One of the advantages of having a computer execute instructions is that it can
# also change its execution based on the values. You can conditionally execute
# code by using the "if" statement that uses the keyword `if` The keyword is
# followed by an expression that evaluates to a Boolean value, `True` or
# `False,` followed by a colon and a body of code. 
#
# Conventionally, you place the "conditional" expresison inside parentheses.
if True:
    print("Test is true") 
if 5 > 3:
    print("5 is greater than 3")

#%% [markdown]
# ## elif and else
# You can handle alternative cases by using the `elif` and `else` keywords,
# followed by colons. Like before, the statements that are indented below are
# executed. The expression "str(input)" casts the value of input (which is
# expected to be an integer) into a string in order to concatenate it with
# another string.
#
def compare_with_3(input):
    if input < 3:
        print(str(input) + " is less than 3")
    elif input > 3:
        print(str(input) + " is greater than 3")
    else:
        print(str(input) + " is equal to 3")
compare_with_3(2)
compare_with_3(3)
compare_with_3(4)

#%% [markdown]
#
# *ON YOUR OWN*: Write a new version of the function that compares the input
# with a second argument and name it "compare":
# For instance, calling it with the following arguments should result in the following printed output:
# compare(3,3)
# 3 is equal to 3
# compare(10,3) 
# 10 is greater than 3

#%% [markdown]
# # Scope
# The last topic covered in this part of the lab is the concept of scope. Scope
# refers to the fact that at each point in a code's execution, certain variables
# may be available. Parameters, for instance, are only available within the body of a function.
# Any variable declared in the outer scope may be available inside of a function. 
# For example:
x = 5
def out_of_scope():
    print(x)
out_of_scope()

#%% [markdown]
# If a variable is declared inside of a function has the same name as the outer variable, it will "shadow" it:
x = 10
def inside():
    # This will set the local variable x to 20, but not change the above variable x.
    x = 20
    print(x)
inside()
print(x)

#%% [markdown] 
# 
# This is intended to isolate the world of the function from the
# rest of the program. A function should not depend (in general) on anything
# except the arguments that are passed in as an argument. 
# 
# This way, the function can be reused in multiple contexts.
# If the function changes the value passed in, the new value can be assigned to the previosu variable:
def add_one(x):
    return x + 1
x = 10
x = add_one(x)
print(x) 
x = add_one(x)
print(x)

#%% [markdown]
# # Iteration
# The keyword `for` is used to iterate over a sequence. A sequence can be
# defined using brackets. For instance, [1,2] is a sequence that contains the
# integer 1 in the 0 index, and the integere 2 in the 1 location. The first
# location of a sequence is 0. 
#
sequence = [1,2]
sequence

#%% [markdown] The syntax for a for loop is the keyword `for` followed by the
# name of a local variable that each value will be bound to, then  the keyword
# `in` followed by the sequence to iterate over:
for value in [1,2]:
    print(value)

#%% [markdown] 
# 
# You can generate a sequence to iterate a specified number of
# times using the `range` method:
for value in range(1,10):
    print(value)  

#%% [markdown]
# # While loop
# The while loop will continue executing until the expression after it is true.
# This is useful if you don't know when the loop will end, whereas the `for`
# loop is often called "definite iteration" for this reason. 
x = 10
while x > 1:
    print(x)
    x = x -1

#%% [markdown] 
# # Random
# `random` is a module that contains useful functions. You import modules using
# the 'import' keyword, and call methods using the '.' operator. One useful
# method in the random function is the randint, which returns a random integere
# between the two arguments. 
import random
print(random.randint(2,100))
print(random.randint(2,100))

#%% [markdown] *ON YOUR OWN*: 
#
# Write a function, `sum_random`, that returns the sum of x random numbers
# between 1 and 100. 
#
# The function should accept a single argument. For instance, sum_random(2)
# would sum two numbers between 1 and 100: 34 and 16 and return the value 50.