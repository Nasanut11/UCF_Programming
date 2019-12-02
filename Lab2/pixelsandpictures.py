#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Lab2'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Pixels and Pictures
# Lab 2: Part 2
# 
# In this notebook, you will complete 5 coding tasks involving content from Chapter 10 and 11 of Montfort's Exploratory Programming from the Humanities.
# 
# Like previous labs, the instructions for each of the exercises (labeled 2-6 through 2-10) will be prefixed with "ON YOUR OWN". Add or modify the necessary code to the cell to satisfy the requirements.
#%% [markdown]
# ## Tuples and Pixels
# A `tuple` is a special sequence data type that is *immutable*. You can define a tuple by using a list of values separated by commas enclosed by parentheses:

#%%
myTuple = (1,2,3)

#%% [markdown]
# 
# Like other sequences, you can access different parts of the tuple using indices:
# ```python
# myTuple[1] # Prints 2, being the second elements
# print(myTuple[-1]) # Prints 3, being the last element

#%%
print(myTuple[1])
print(myTuple[-1])

#%% [markdown]
# Tuples are immutable, meaning you cannot assign a value to a member. You must instead create a new tuple. This is useful for making assumptions about the data, and to make assumptions about the meaning of certain values exlicit:

#%%
# The following will produce a TypeError:
myTuple[1] = 0


#%%
from PIL import Image
mode = 'RGBA' # This states that each pixel will have four components
size = (100, 100) # This tuple refers to the dimensions of the image (100 pixels by 100 pixels)
color = 'black' # The default color for a pixel
ourimage = Image.new(mode, size, color)
# ourimage now contains a set of pixels that have the color 'black' and is 100 by 100 pixels in size.


#%%
# We can display the image using Jupyter notebook:
ourimage


#%%
# This will save the image to the root of our project in VS Code. 
# You can specify a different directory as well.
ourimage.save('allblack.png')


#%%
# You can find out more about many methods by using the "help" function in addition to looking up the function on the web.
help(Image.new)

#%% [markdown]
# # Setting Pixels
# You can change a pixel to a new value using the `putpixel()` method. For instance, the following line will set the centermost pixel of our image to white:

#%%
ourimage.putpixel((50,50),(255,255,255,255))
ourimage


#%%
# Often objects (and ourimage is an Image object) have properties that are useful. 
#For instance, the size can be obtained by the attribute 'size':
ourimage.size


#%%
# [2-4] ON YOUR OWN: 
# Using code, create a new function that accepts three arguments: (1) an image created by Image.new, and (2) a x value, and (3) a color specified as a 4-tuple. 
# The function should return the image that has a vertical line drawn across it in the color provided.

# For instance, if it were named vert_line:
# image = Image.new(100,100)
# vert_line(image, 50, (10,30,50,255))

# You must create the vertical line on an image of any size.
 
# WRITE YOUR CODE HERE

#%% [markdown]
# # Gradients
# Montfort describes the following technique for creating a *linear* gradient, or one where the color changes smoothly across an image.

#%%
from PIL import Image
rectangle = Image.new('RGB', (150, 100))
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (x, x, x))
        rectangle.save('gradient.png')
rectangle


#%%
# [2-5] ON YOUR OWN:
# Write a function that generates a radial gradient in an image given a particular coordinate. Your function should take in an image of any size and create a radial gradient from the coordinate provided in the form of a tuple.

# For instance, if the function were called "gradient", and "image" contained a 100 x 100 image, you could call the function like so:

# gradient(image, (25,25))

# This would return the same image with the gradient starting at 25, 25. You may either specify the color in the function or accept two quadtuples as arguments:
# gradient(image, (25,25), (100,100,100,255),(200,200,200,255)
# or, with each argument given its own variable:
# location = (25,25)
# color_1 = (100,100,100,255)
# color_2 = (200,200,200,255)
# gradient(image,location,color_1,color_2)

#%% [markdown]
# ### Opening existing images
# You can open an existing image by using the Image.open method:
# ```python
# Image.open('cat.png')
# ```
# Note that you will have to have the image file accessible by the version of Python.

#%%
cat = Image.open('cat.png')
cat


#%%
# [2-6] ON YOUR OWN:
# Write a function that takes as an input an image. 
# Create a "Thumbnail" image of the provided image that is 1/3 of the size of the original image, and return it. The new image should have the same color space as the original, and work with either RGB or RGBA color schemes.


#%%
# [2-7] ON YOUR OWN:
# Given a formula to calculate the "luminance" of a pixel as:
#  L  =  0.2126 × R   +   0.7152 × G   +   0.0722 × B 
# Write a function that accepts an image and returns a new image that is in grayscale that is the same dimensions.


#%%
# [2-8] ON YOUR OWN:
# Write a function that applies the grayscale method to all of the image files in a directory.
# Use the Glob library. Make sure the new images have "_gray" appended to their name. This means "img1.png" would be written as "img1_gray.png". Guidance for doing this can be found in Montfort's Chapter 11. 


