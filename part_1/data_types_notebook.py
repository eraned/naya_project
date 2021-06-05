#!/usr/bin/env python
# coding: utf-8

# # General

# The program must know the data type of each variable. It has a significant influence on many techanical aspects:
# 
# * Every data type "supports" different operations.
# * The same "function" may have different meaning for different data types.
# * Every data type is stored differently in the machine memory.

# In[ ]:


num1 = 1.2
num2 = 2.3
str1 = 'micro'
str2 = 'phone'

# print(num1 + num2)
# print(num1 * num2)
# print(str1 + str2)
# print (str1 * str2)  # ERROR!!!
# print (num1 + str1)  # ERROR!!!


# The type of the variable can be retrieved by the `type()` function.

# > **Note:** Python is a dynamic language, which means you don't have to specify the type of a variable.

# In[ ]:


print(type(num1))
print(type(str1))


# At this stage we will discuss four basic data types, but later in the course we will see many more data types and even create some new ones by ourselves.

# # Numbers

# We will work with two types of numbers:
# 
# * integers - round numbers, which are very useful for enumeration.
# * float numbers - numbers with decimal point, which are used for accuracy.

# In[ ]:


print(type(3))
print(type(3.55454554545454554541))


# Python assumes that if a number is given as a round number then it is an integer. If a float is needed, then there are two ways to "force" it:
# * add a "fictive" decimal point
# * use the conversion function _float()_

# In[ ]:


# print(type(3.0))
print(type(float(3)))


# Obviously, numbers support all the mathematical functions we expect them them to support. Note, however, that the basic Python includes only the most basic arithmetical operations, so things like trigonometric functions, exponential functions, etc. are not readily available.

# In[ ]:


a = 3
b = 17

print("a =", a, ", b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b = ", a * b)
print("b / a =", b / a)
print("b mod a =", b % a)
print("b^a =", b**a)
print("max(a, b, 12) =", max(a, b, 12))


# > **Your turn:** Evaluate $\frac{3^{4}-4^{3}}{2^{5}-5^{2}}$

# # Strings

# String is a **sequence** of **characters**, and they are defined by one of two methods:
# 
# * wrapping them with either single-quotes or double-quotes (it doesn't matter)
# * Applying the _str()_ function on an object.

# In[ ]:


str1 = 'This is a string'
str2 = "This is also a string"
str3 = str(12.34)

print(type(str1), type(str2), type(str3))


# Being a sequence, the characters of a string have **index**, that gives direct access to any part of the string. The indexing system is not intuitive at first, but I you'll get it very fast. The picture below explains the indexation.
# 
# <center><img src="https://developers.google.com/edu/python/images/hello.png" alt="Python sequence indexation" style="width: 200px;"/></center>
# 
# Two things to note:
# 
# * The concept of **negative indexing** is very useful when you want to deal with the end of the string, but you don't know its length. This is the case, for example, when you want to know the type of a file bsed on the file name.
# * The indexing system also supports **slicing** using the '**:**' sign. The slicing excludes the last specified index.

# In[ ]:


str1 = 'This is a string'
str2 = "This is also a string"
str3 = str(12.34)

print(str1[0])   
print(str3[2])      
print(str1[6:11])    
print(str2[-4:-1])   # Take all BUT the lase character
print(str3[-4:])     # Take all INCLUDING the lase character
print(str1[:6])  
print(str1[5:2])     # Backwards indexing returns an empty string


# In[ ]:


len(str1)


# ## Common operations

# Like any data type, strings support several operations. Being sequences as well, strings support also sequence operations.
# 
# * Sequence types:
#     * the `len()` function - returns the length of the sequence
#     * the `in` operator - test whether an element is within the sequence
#     * the `+` operator - concatenation of two sequences of the same type
#     * the `index()` method - returns the index of an element within the sequence
#     * the `count()` method - counts the number of occurrences of an element within the sequence
# * Strings
#     * the method `replace(old, new)` - returns a new string in which all the occurrences of `old` are replaced with `new`
#     * the method `find(sub)` - returns the index of sub within a given string. Returns -1 if `sub` is not in the calling string.
#     * the methods `upper()` and `lower()` - return a new string with the same letters as the original, but with all the letters in uppercase or lowercase
# 

# > **Note:** Later in the course, in the [chapter about object-oriented programming](https://drive.google.com/drive/folders/1tvtiiU0hd5kgkCzIHx0xFK78g7wzJDys?usp=sharing), we will understand the exact differene between operators, functions and methods. In the meantime we just need to pay attention to the "dot" syntax, where `obj.app(arg)` means that the object `obj` applies the method `app()` on the argument `arg`.

# ### Illustration

# In[2]:


str1 = 'Made in Israel'


# In[ ]:


print(len(str1))


# In[ ]:


print('a' in str1)
print('in' in str1)
print('In' in str1)


# In[ ]:


str2 = str1[0:8] + "China"
print(str2)


# In[4]:


print(str1.count('a'))
print(str1.index('In'))
print(str1.find('in'))


# In[5]:


print(str1.upper())


# ## Immutability

# A string cannot be changed after its creation, and the only way to produce new strings objects from it is by ceating new ones. This is a very important feature of the string data type, and we say that strings are **immutable**. During the course we will see the importance of this characteristic and compare it to other data types. 
# 
# What happens when we execute the _replace()_ method on the string _str1_?

# In[ ]:


str1 = str1.replace('Israel', 'China')
print(str1)


# **Nothing!** Since strings are immutable, _str1_ cannot be modified, and therefore the result of the _replace_ method actually creates a new string, which can be assigned to a new variable, e.g. _str2_.

# In[ ]:


str2 = str1.replace('Israel', 'China')
print(str1)
print(str2)


# The immutability of strings can be also demonstrated by the error raised when we try to use the indexation for assignment.

# In[ ]:


str1[8:] = 'China'


# > **Reference:** More about the mutability concept and other related functionalities can be found [in Ventsislav Yordanov's Medium article](https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a).

# ## String literals

# String literals are auxiliary strings that allow to use characters which are either invisible or raise technical issues when used. To symbolize these characters, you havee to use  the backslash **escape character** (\\). The full list of string literals can be found [here][String literals], and the following are the most common:
# 
# * \\n - New line
# * \\t - Tab
# * \\' - Single quote
# * \\" - Double quote
# * \\\\ - Backslash
# 
# [String literals]: https://docs.python.org/3/reference/lexical_analysis.html#literals "Python documentation for string literals"

# > **Note:** The escape character is part of the string.

# ### Illustrations

# In[ ]:


print('First line.\nSecond line.')


# In[ ]:


print('Israel\t:\tJerusalem\nSpain\t:\t?\n')
print('(a) Paris\t(b) Rome\t(c) Madrid\t(d) Berlin')


# In[ ]:


print('He is John') 
print('He\'s John') 


# The existance of two string wrappers enables the following trick...

# In[ ]:


print('And god said: There was light')
print('And god said: \"There was light\"')
#print ("And god said: "There was light"")  # This raises an error
print('And god said: "There was light"')


# String literals are characters like any other.

# In[ ]:


len('a\nb')


# > **Your turn:** Print the following text in a more readable fashion with proper newlines and tabs.

# In[ ]:


s = 'Sunday: visitors: 20, unique: 13, Monday: visitors: 25, unique: 14, Tuesday: visitors: 31, unique: 19'
print(s)


# ## multi-lines string
# 
# String can also be wrapped with three characters, using either single-quote or double-quote, allowing to write text with quotes and new lines as you normally do:

# In[ ]:


text = '''A String warpped with triple quotes can extend over
multiple lines like this one, and can contain 'single'
and "double" quotes without using string literals.'''

print(text)


# ## Conversions

# Strings can be concatenated, but this may get a little bit tricky when combined with other data types.

# In[ ]:


num1, num2 = 1234, 4321
the_sum = num1 + num2


# In[ ]:


print('The sum of', num1, 'and', num2, 'is', the_sum)


# > **Note:** The `print()` function does not concatenate strings, but rather print them one by one, adding a white space between them.

# In[ ]:


# sentence = 'The sum of ' + num1 + ' and ' + num2 + ' is ' + the_sum


# In[ ]:


sentence = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(the_sum)
print(sentence)


# # Booleans

# Boolean variables can have only _True_ and _False_ values, and they are also called "binary" and "logical" variables. Boolean variables can be created directly by assigning `True` or `False` to them, however it is much more common to create them with comparisons and tests.

# In[ ]:


is_connected = False
type(is_connected)


# In[ ]:


num1, num2 = 12, 27

# print(num1 == num2)
# print(num1 != num2)
# print(num1 < num2)
# print(num1 >= num2)


# In[ ]:


str1 = 'Python'

# print('p' in str1)
print(str1[3:5] == 'ho')


# In[ ]:


str1[3:3]


# ## Common operations

# Booleans support less known operations, which are:
# 
# * _not_ - the negative
# * _and_ / _&_ - return _True_ if and only if both of its sides are _True_
# * _or_ / _|_ - return _False_ if and only if both of its sides are _False_
# * _^_ (xor) - return _True_ if and only if exactly one of its sides is _True_

# In[ ]:


x, y = True, False

print(x)        # True
print(not x)    # False
print(x & y)    # False
print(x and y)  # False
print(x | y)    # True
print(x or y)   # True
print(x ^ y)    # True


# ## Illustration

# In[ ]:


avg_height, avg_weight = 1.79, 75
my_height, my_weight = 1.77, 85


# In[ ]:


am_i_tall = my_height >= avg_height
print(am_i_tall)


# In[ ]:


am_i_fat = my_weight >= avg_weight
print(am_i_fat)


# In[ ]:


am_i_giant = am_i_tall and am_i_fat
print(am_i_giant)


# In[ ]:


am_i_chubby = am_i_fat and not am_i_tall
print(am_i_chubby)


# In[ ]:


am_i_abnormal_1 = (am_i_fat and not am_i_tall) or (am_i_tall and not am_i_fat)
am_i_abnormal_2 = am_i_fat ^ am_i_tall
print(am_i_abnormal_1, am_i_abnormal_2)


# > **Note:** In addition to simple Booleans, Python allows [Truth-value testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) with non-Boolean variables.

# # Exercises

# ## Exercise 1

# 1. Assign your height in meters to a variable called _height_ and your weight in kilograms to a variable called _weight_.
# 2. Calculate your BMI and assign the value to a variable called BMI. ($BMI=\frac{w}{h^2}$)
# 3. Print the sentence "My height is \_\_\_ meters, my weight is \_\_\_ Kgs, and my BMI is \_\_\_.”.
# 4. Print the sentence, so that each part of it will be in a new line.

# ### Solution

# In[ ]:


Weight, Height = 104, 1.77


# In[ ]:


BMI = Weight / Height**2


# In[ ]:


print("My height is " + str(Height) + " meters, my weight is " + str(Weight) + " Kgs, and my BMI is " + str(BMI) + ".")


# In[ ]:


print("My height is " + str(Height) + " meters,\nmy Weight is " + str(Weight) + " Kgs,\nand my BMI is " + str(BMI) + ".")


# ## Exercise 2

# 1. Assign your first name and your last name to the variables _first_\__name_ and _last_\__name_, respectively.
# 2. How many letters does your full name have?
# 3. Create your full name by concatenating _first_\__name_ and _first_\__name_ with a space in the middle, and assign the result to a variable called _full_\__name_.
# 4. Use the string method _replace()_ to change all the vowels in your full name from lower case to upper case. (Vowels are the letters 'a', 'e', 'i', 'o' & 'u')
# 
#     * Note that you are not allowed to use the _for_ syntax at the moment.

# ### Solution

# In[ ]:


first_name, last_name = 'Avi', 'Yashar'


# In[ ]:


print(len(first_name) + len(last_name))


# In[ ]:


full_name = first_name + ' ' + last_name


# In[ ]:


upper_aeiou_name = full_name.replace('a','A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
print(upper_aeiou_name)


# ## Exercise 3

# Define proper variables with the following data for yourself and for one of your imaginary friends: gender (string), age (int), city (string) and marital status (Boolean). Then create the following Boolean variables:
# 
# 1. `same_city` – do both of you live in the same city?
# 2. `is_older` – is your friend older than you?
# 3. `diff_gender` – are you from different genders?
# 4. `both_married` – are you both married?

# ### Solution

# In[ ]:


my_gender, other_gender = 'M', 'F'
my_age, other_age = 33, 29
my_city, other_city = 'Kfar-saba', 'Kfar-saba'
my_marriage, other_marriage = True, False


# In[ ]:


same_city = my_city == other_city


# In[ ]:


is_older = other_age > my_age


# In[ ]:


diff_gender1 = (my_gender == 'M' and other_gender == 'F') or                    (my_gender == 'F' and other_gender == 'M')
diff_gender2 = my_gender != other_gender
diff_gender3 = not(my_gender == other_gender)


# In[ ]:


both_married = my_marriage & other_marriage

