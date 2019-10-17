# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
# Change directory to VSCode workspace root so that relative path loads work correctly. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..'))
	print(os.getcwd())
except:
	pass

#%% [markdown]
# Here are a set of exercises and challenges that will ensure you have a solid understanding of variables, functions and iteration.
# 
# A *factorial* is defined as the product of an integer and all of the integers below it.
# 
# If the argument is not a float, then throw a value error.
#%% [markdown]
# # 1: factorial()
# Calculate the factorial of any number provided as an argument.

#%%
# Write your code here
def factorial(input):
    if(type(input)==type(3.0)):
        raise ValueError("Bad Input")
    if(input==0):
        return 1
    else:
        return input*factorial(input-1)

factorial(10)

#%% [markdown]
# # 2: print_times()
# Create a function accepts a single string argument, and a number. If the first argument isn't a string, have it throw a ValueError. Then, print out the string to the console the number of times provided in the second argument.
# 
# Return an integer that represents the number of times printed.

#%%
# Write your code here

#%% [markdown]
# # 3: concat_strings()
# Write a function that concatenates two strings together, with a space in between, and returns the result.

#%%
# Modify this function:
def concat_strings(a,b):
    raise RuntimeError("Unimplemented")

#%% [markdown]
# ## Test your code by running this cell:

#%%
import random
for value in range(100):
    ran_num = random.randint(0,100)
    if(concat_strings("Test"+str(value),"Test"+str(ran_num)) == 
        "Test"+(str(value)) +"Test"+str(ran_num)):
        print("Success")
    else:
        print("Fail")

#%% [markdown]
# # 4: calc_mean
# Write a function that calculates the mean of a list of numbers and returns that value 
# 
# The average (or mean) of a set of numbers is sum divided by the number of items in the list

#%%
# Write your code here

#%% [markdown]
# # 5: find_max():
# Write a function that finds the largest number in a list of numbers and returns that number. You must use a for loop and you may only use simple comparisons (E.g. > or <)

#%%
# Write your code here

#%% [markdown]
# # 6: sort_list_ints()
# 
# Write a function that sorts a list of integers. You can assume the input is a single sequence of 0 or more integers. You may not use any of the existing sorting functions or methods.

#%%
# Write your code here
# Example Input: [1,100,3,50,2]
# Example Output: [1,2,3,50,100]

