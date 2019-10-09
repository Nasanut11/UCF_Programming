#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Week_6_InClass'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # In-Class Notes 10/9
# This Jupyter notebook provides examples that correspond to the topics covered so far in this course. These correspond to the slides in the presentation. For additional practice, try to answer the practice questions by applying the concepts. You may need to reference the documentation.
# 

#%%
import os
# This will return the current directory. Notice this is the root of your VS Code project.
os.getcwd()

#%% [markdown]
# The "os" package provides a number of variables that pertain to interacting with the operating system. For instance, to access the list of environmental variables, you can access the environ dictionary:
# 

#%%
os.environ

# PRACTICE: How do you find your home directory?

#%% [markdown]
# ## Paths and Separators
# A path is a sequence of folder names that can end in a file name. Each folder name is separated by a path separator, which is different for Windows and Unix/Mac. 
# 
# You can find out the separator and use it by referencing the path submodule of the os package:

#%%
print(os.path.sep)

#%% [markdown]
# For instance, to specify a path based on the current working directory that specifies the "week-6" subdirectory of the "in-class" subdirectory of the current project, you can use the `os.path.jos`:
# 

#%%
os.path.join(os.getcwd(),'in-class','week-6')

# PRACTICE: Specify other folders relative to other locations on your computer.

#%% [markdown]
# # Working with Files and Folders
# In programming, there are times when the data you are interested in working with is not stored in the script itself. This could be a dataset, or it could be images or other files you want to process.
# 
# There are four main ways to acquire and store data (values):
# 
# 1. Directly through a *networking protocol*. This means locating a remote computer and sending a request that identifies the information needed, using HTTP or another method.
# 2. Using a program called a *database*, which may be on the same computer. The database handles persisting, sorting, and organizing the data.
# 3. You can directly access and store information as files on the operating system. These can either be *text* or *binary* files. 
# 4. Through a special-purpose library that encapsulates the lower-level network access to a data source. This includes online content sources such as project Gutenberg, Twitter, OpenWeather, or others. 
# 
#%% [markdown]
# # Directly downloading web resources
# 
# You can load files that are publicly available on the internet using the `urllib` package and the `request` module:

#%%
import urllib.request
page = urllib.request.urlopen('http://www.gutenberg.org/files/1342/1342-0.txt')
# The return value of page.read() is bytes, which could be an image, or it could be text. 
text = page.read().decode('utf-8')
print(text[716:1000])

# utf-8 is an encoding that maps bytes to specific characters for rendering. It handles a wider range of characters than ascii, but fewer than utf-16.

#%% [markdown]
# You can save the file using the python "open" builtin. There are two ways to do so:
# 
# 1. By assigning the file (which is relative to the current working directory) to a variable:

#%%
# open takes several arguments: the path of the file to open, whether to open it in read-only or write-only mode, and the encoding to open it with. Files can also be opened as binary (b).
source = open('janeausten.txt','w',encoding="utf-8",newline='\n')
# This writes the contents of the the variable (text, from above) to the file. The newline specifies which character to use for the newline, which may default to \n\r on Windows.

source.write(text)
# This closes the file pointer, which is important as it allows you to see the results. 
source.close()

# PRACTICE: Try downloading other text from the internet this way and saving them as files. You can delete the files using the explorer on the left, or by using the bash command "rm"

#%% [markdown]
# 2. Using the `with` keyword to create a context for the file's use. 
# 
# This method creates a context where at the end, the file is closed, and within the block, the variable name designated by "as <var>" is available:

#%%
with open('janeausten.txt','r',encoding="utf-8",newline='\n') as file:
    print(text[0:400])

#%% [markdown]
# ## Iteration and Recursion
# The next part will involve looking at two different implementations of a simple math quiz:
# 
#  - input_for.py
#  - input_infinite.py
# 
#  These should be run in the terminal using the appropriate anaconda shell (command prompt, if you are on windows)
#  python in-class/week-6/input_for.py
#  python in-class/week-6/input_infinite.py
# 
#  The first makes use of data stored in a file (problems.txt) and the second demonstrates an infinite loop as well as exception handling.
# 
#  *PRACTICE:*
#  Modify these programs to handle different types of data or input. What about multiple choice questions?
#%% [markdown]
# # In-Class Exercise: Collaborative Gutenberg Analysis
# The final part of today's class will require you to make use of project gutenberg through a partner-programming activity.
# 
# Start by looking at the gutenberg Jupyter notebook in this directory for a short tutorial on TextBlob and Natural Language Processing, then select between 2 and 3 books on Project Gutenberg to analyze. You may use Live Share or you may simply collaborate by programming in parallel, but you should 
# 
# Some ideas for analysis:
# 
#  - Use Montfort's method to analyze the ratio of adjectives to the total number of words.
#  - Find the average length of sentences in each work. What does this tell you about the work?
#  - Break the work down into smaller segments (Chapters) and compare the frequency of character names or terms in each. 
#  - Find the top used words 
#  - Find out the average sentiment of the work, including the most positive and most negative sentences. Do these correlate to parts of the story? 
# 
# Use this information to form a hypotheses about the two works based on exploring the work using natural language processing. You can use works you are familiar with, or you could compare Jane Austen's Pride and Prejudice (1813) to Herman Melville's Moby Dick (1851). You could also compare two works by the same author -- the choice is yours.
# 
# I recommend keeping a copy of the work in the same directory.
# 
# Please turn in a url to a Google doc in WebCourses with the following:
#   - Location of the code in your repository
#   - What questions you decided to pursue
#   - What information you decided to collect and compare
#   - Results, if any, from running your scripts against the two books
#   - Any conclusions or future work that this exercise would lead to, given additional experience with Python.

