#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Lab2'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Lab 2 Hints
# ## Tuples

#%%
# Tuples are values with values at specific locations
x = (0, "String")
a, b = x
print(a)
print(x[0])
print(b)
print(x[1])


#%%
# You can create arrays by appending values to them. This is particularly useful when you want to "accumulate" a value based on a set of values from a list.
def generateList(num):
    arr = []
    for x in range(num):
        arr.append(x)
values = generateList(10)

def calculateRunningTotal(input):
    runningTotals = []
    sum = 0
    for x in input:
        sum = sum+x
        runningTotals.append(sum)
    return runningTotals

# We produce a new list based on the previous list without modifying the previous list.
calculateRunningTotal(values)


#%%
# This means you can also append tuples with different components
strArray = ["a","bc","cde","def","efgy","f","g","h","i","j"]
lengths = []
for count, value in enumerate(strArray):
    lengths.append((count,value,len(value)))
lengths


#%%
# Finally, you can sort these using either the sort method (array.sort()) or sorted(array):
from operator import itemgetter 
# itemgetter produces a function that retrieves the nth value.
# For instance:
tuple = (1,2,3)
# getter is a function, as itemgetter returns a function
getter = itemgetter(2)
# This will retrieve the item at index 2 (again, 0 index)
getter(tuple)


#%%
# This is particularly useful as a function to sort on a particular location in a tuple. 

# For our list, if we wanted to sort on the 3rd item (2 when 0 indexed), then we would do the following:

sortedResult = sorted(lengths,key=itemgetter(2), reverse = True)
sortedResult


#%%



