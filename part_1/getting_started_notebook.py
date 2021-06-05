#!/usr/bin/env python
# coding: utf-8

# # Working environment

# We will get to know many components of our work environment, but for start we need to be familiar with the three main interfaces:
# 
# * **Python** - the engine behind the scenes
# * **Jupyter** - the IDE we will use to write our Notebooks during the course
# * **Google Colaboratory** - A free cloud service to run your Jupyter notebboks. It supports nearly all the relevant modules for our course (and many more). See [here](https://colab.research.google.com/notebooks/welcome.ipynb) for full details.
# 

# > **Discussion:** How does it really run with Google Colab? Discuss the responsibility of the data scientist regarding the availibility of necessary infrastructures.

# The closer you get to "production" the less convenient it is to work with Jupyter Notebbooks. For simplicity we will stick with Google Colaboratory for te entire course. Nevertheless, two additional environments should definitely be mentioned:
# * **Anaconda** - A scientific distribution of Python, which includes hundreds of packages (including most of the packages we will meet in our course).
# * **PyCharm** - one of the most common IDEs for python developers

# # Basic concepts

# ## Tradition first
# Traditionally, the first program you write when learning a new programming language is Hello World. So let's write it in Python now

# In[ ]:


print('Hello, Avi')


# ## Assignment and operations

# This is the most basic action in programming. The '=' sign assigns the value on the right to a variable, whose name is on the left.
# 
# A variable is like a box. You can put something in the box (thats called Assignment) and use the contents later for further operation. **Variable's name should be meaningful**.
# 
# Python variables do not need explicit declaration (nor type declarations) to reserve memory space. The declaration happens automatically when you assign a value to a variable. 

# In[ ]:


a = 3
b = a + 1
c = b * 5

my_number = 12.345
my_name = 'Liran'
is_spam = True
result = max(12, 32, 17, c)


# > **Note:** Don't use Python terms for naming your variables and files. E.g. calling your variable `list` or your file `numpy` may cause Python to not work properly.

# ## Case sensitivity

# Python is a case-sensitive language, which means that whether you use lower-case or upper-case letters makes a lot of difference.

# In[ ]:


a = 1
A = 2
print (123 + a)
print (123 + A)


# ## Comments

# If we want to add a comment to our code, we add a **#** sign, and everything after it within the same line will not be ecaluated.

# In[ ]:


y =7 # This line is a comment
# The next line is not a comment
my_age = 33


# In[ ]:


"""
If we want to add a comment to our 'code, we add a # sign, and everything after it within the same line will not be ecaluated.
"""


# ## Printing

# Very often we would like to print something to the "console", the textual interface. This is acheived by the _print_ function.

# In[ ]:


print("This will be printed.")


# In[ ]:


max = 10


# In[ ]:


max(10,120,12)


# `print()` can print several elements, and they should be separated with commas. It automatically adds a white space between them.

# In[ ]:


my_name = 'Balu'
print("My name is", my_name)


# The function `print()` automatically starts a new line (after the printing). This can be modified by the `end` argument.

# In[ ]:


for name in ['Arik', 'Bentz']:
    print("My name is", name)


# if we wish _print_ not to start a new line, we can change the `end` argument (the default is a new line)

# In[ ]:


for name in ['Arik', 'Bentz']:
    print("My name is", name, end=' ')


# ## Indentation

# While most programming languages use various syntax methods to mark a block of code (e.g. { ... }, BEGIN ... END, etc.), Python's uses indentation. This feature gives the language a very "clean" look.
# 
# A code block which represents the body of a function or a loop begins with the indentation and ends with the first unindented line.
# 
# standard indention is 4 spaces.

# In[ ]:


my_name = 'Arik'
other_name = 'Bentz'


# In[ ]:


if other_name == my_name:
    print("You are awesome!")
else:
    print("You are NOT awesome!")


# The following variations illustrate the importance of correct indentation.

# In[ ]:


for x in [1, 2, 3, 4, 5, 6]:
    if x % 2 == 0:
        print(x, "is even.")
    else:
        print(x, "is odd.")


# **Your turn**: Your first time!
# 
# 1.   Create 2 variable with value: "my_age","my_name".
# 2.   Print them with an explanation
# 
# Example for output: "My Name is Avi and I am 55 years old."
# 
# 

# # Self-explanatory examples

# > **Note:** The following examples are for illustration purposes. Every detail in them will be explained in depth throughout the course.

# ## Example 1 - Interactive Guess-My-Number game

# The following script implements a game, in which the computer randomly chooses a number between 1 and 100, and you have to guess it guided by the computer's hints.

# In[ ]:


# import necessary module
import random

# The computer "chooses" a number
my_number = random.randint(1, 100)

# The program asks you to play
print ("I have chosen a number between 1 and 100.")
print ("Please try to guess it...")

# The program reads your guess and stores it
user_guess = int(input())

# The game is on...
while my_number != user_guess:
    if user_guess > my_number:
        print ("Wrong! You are too high, please try again...")
        user_guess = int(input())
    else:
        print ("Wrong! You are too low, please try again...")
        user_guess = int(input())

print ("Finally :-)\nGAME OVER")


# ## Example 2 - Data exploration

# > **Note:** In this example we will use the `Diamonds` dataset, which can be found in the *Datasets* folder of the course ([link](https://drive.google.com/drive/folders/15J2Y2y81Uc9Wy8-ceBF7ZQj4C-uQr1dT?usp=sharing)).

# The following script reads a file from a given path and make some manipulations to its data.

# > **Note:** We are making use of the `pandas` and `seaborn` packages, which will be an important tool throughout our course.

# In[ ]:


import pandas as pd
import seaborn as sns


# In[ ]:


file_path = 'diamonds.csv'
df_diamonds = pd.read_csv(file_path)


# We can now see the actual raw data

# In[ ]:


df_diamonds.head()


# We can query the data for anything we like, e.g. how many diamonds weigh more than 2.5 carats and cost less than 10000.

# In[ ]:


len(df_diamonds[(df_diamonds.carat>2.5) & (df_diamonds.price<10000)])


# We can explore it with many manipulations, e.g. sort the diamonds `Cut` categories by their average price.

# In[ ]:


df_diamonds.groupby('cut')['price'].mean().sort_values(ascending=False)


# We can make any plot we desire, e.g. the boxplots of the prices of each `Clarity` category.

# In[ ]:


sns.boxplot(x='clarity', y='price', data=df_diamonds)

