#!/usr/bin/env python
# coding: utf-8

# The default behavior of the interpreter is to execute the lines of code one after the other. However, the tools we will see in this chapter provide means for manipulating this behavior and control the "flow" of the code.
# 
# The two main categories of flow control are:
# 
# * **conditioning** the execution of specific code parts by some preliminary test
# * Repeated execution of specific code parts in **loops**

# # The *if* statement (and friends)

# The code block within an _if_ statement will be executed only if the specified condition is fulfilled.

# In[ ]:


word = 'Schwarzenegger'
if len(word) > 10:
    print ('This is a long word...!')
if len(word) <= 10:
    print ('This word is not so long.')
print("Done!")


# > **Note:** The `print("Done!")` is added to illustrate the indentation.

# It should be noted that the term after the word _if_ is not necessarily a "test", but is actually a **variable**. Usually it is a Boolean variable, but we will see later that this is not necessarily the case.

# In[ ]:


word = 'Schwarzenegger'
is_long_word = len(word) > 10
if is_long_word:
    print ('This is a long word...!')
if not is_long_word:
    print ('This word is not so long.')
print ("Done!")


# #### Example

# Print the largest number from a list of three numbers.

# In[ ]:


numbers = [200, 123, 63]

# Initializing
largest = numbers[0]

# Update
if numbers[1] > largest:
    largest = numbers[1]
if numbers[2] > largest:
    largest = numbers[2]

print (largest)


# ## _elif_ and _else_

# A series of conditions may be tested in order to choose the relevant code block, and to do that we use the _elif_ and _else_ statements. _elif_ is a short for "else if", which is used when we wish to make another optional testing. The _else_ statement does not make any more tests, but rather execute the code block it holds if no other test was True
# 
# The key point for understanding the logic of an _if...elif...else_ section is that **only the code block of the first fulfilled condition is executed**.

# In[ ]:


age = 14
if age < 6:
    print ('I can\'t believe how much you\'ve grown.')
elif age < 18:
    print ('How\'s school?')
elif age < 90:
    print ('Let\'s have a beer!')
else:
    print ('Sooo... no teeth, ha?')


# To understand the importance of the order between the conditions, consider the implications of this order:

# In[ ]:


age = 14
if age < 90:
    print ('Let\'s have a beer!')
elif age < 18:
    print ('How\'s school?')
elif age < 6:
    print ('I can\'t believe how much you\'ve grown.')
else:
    print ('Sooo... no teeth, ha?')


# > **Your turn:** 
# > * Part 1 - Write a short script that defines a string variable `word` and prints whether `word` contains more than 2 vowels or not
# > * Part 2 - Write a short script that defines a string variable `my_string` and prints whether `my_string` starts with an upper-case letter, a lower-case letter or neither.

# ## Nested `if`

# _if_ statements can be **nested** as long as we **keep our indentations correctly**.

# #### Example

# Given a `world_dict` dictionary (see below), write a script that receives a location of type `list` and is of the form `[continet, country, city]`, and prints whether this location is already in the dictionary or not.

# In[ ]:


world_dict = {'Europe':
                  {'Spain': ['Madrid', 'Barcelona'],
                   'France': ['Paris', 'Lyon']},
              'Asia':
                  {'Japan': ['Tokyo', 'Hiroshima'],
                   'China': ['Beijing', 'Shanghai']}}


# > **Note:** The indentation above is not mandatory, but it makes it easier to read.

# In[ ]:


location = ['Europe', 'France', 'Paris']
# location = ['Europe', 'France', 'Marseille']
# location = ['Europe', 'Germany', 'Berlin']
# location = ['Africa', 'Egypt', 'Alexandria']
# location = ['Europe', 'Germany', '']


# In[ ]:


continent = location[0]
if continent in world_dict:
    country = location[1]
    if country in world_dict[continent]:
        city = location[2]
        if city in world_dict[continent][country]:
            print ("Your city is already in the dictionary")
        else:
            print ("Your city is not in the dictionary")
    else:
        print ("Your country is not in the dictionary")
else:
    print ("Your continent is not in the dictionary")
print ("Done!")


# ## Exercises

# ### Exercise 1

# Choose a number and assign it to a variable called `n`. Then write a code to check whether `n` is divisible by 2, 3 and 5 (all of them). Is your code efficient?

# > **Reminder:** `n` is divisible by `d` if  `n % d == 0`

# In[ ]:


num = 120


# ### Solution

# #### Solution 1 - `if...else`

# In[ ]:


if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print (str(num) + " is divisible by 2, 3 and 5!")
else:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")


# #### Solution 2 - nested `if`

# In[ ]:


if num % 2 == 0:
    if num % 3 == 0:
        if num % 5 == 0:
            print (str(num) + " is divisible by 2, 3 and 5!")
        else:
            print (str(num) + " is NOT divisible by 2, 3 and 5!")
    else:
        print (str(num) + " is NOT divisible by 2, 3 and 5!")
else:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")


# #### Solution 3 - `if...elif...else`

# In[ ]:


if num % 2 != 0:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")
elif num % 3 != 0:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")
elif num % 5 != 0:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")
else:
    print (str(num) + " is divisible by 2, 3 and 5!")


# #### Solution 4 - yet another approach

# In[ ]:


if num % 30 == 0:
    print (str(num) + " is divisible by 2, 3 and 5!")
else:
    print (str(num) + " is NOT divisible by 2, 3 and 5!")


# ### Exercise 2

# Create a list with 3 words of different lengths, and write a code that prints the longest word in the list.

# #### Solution

# In[ ]:


x = ['I', 'am', 'bad']
#x = ['Python', 'is', 'cool']

longest = x[0]
if len(x[1]) > len(longest):
    longest = x[1]
if len(x[2]) > len(longest):
    longest = x[2]

print (longest)


# ### Exercise 3

# Create a dictionary with 3 items of the form `{name, age}`, and write a code that prints the sentence “**name** is the oldest one, and his age is **age**”.

# #### Solution

# In[ ]:


my_dict = {'Arthur': 34, 'Benjamin': 57, 'Carl': 42}

my_keys = list(my_dict.keys())
oldest = my_keys[0]
if my_dict[my_keys[1]] > my_dict[oldest]:
    oldest = my_keys[1]
if my_dict[my_keys[2]] > my_dict[oldest]:
    oldest = my_keys[2]

print ("The oldest guy is " + oldest + " and his age is " + str(my_dict[oldest]))


# # The `for` loop

# The _for_ loop enables to exeucte a specific block of code a predefined number of times, dictated by the **iterable** object on which the loop is running. Every repetition of the block of code is called **iteration**, and with each iteration the **iteration variable** is assigned a new value from the loop iterable.

# ## Basic Examples

# In[ ]:


for i in [1, 2, 3, 4, 5]:
    print(i)


# In[ ]:


for num in [2.2, -0.6, 7.03]:
    print(int(num**2), end=' ')


# > **Note:** It is a convention that we call the iterable `i` if and only if it iterates integers. Otherwise we must use a different name!

# In[ ]:


for name in ['Averbuch', 'Blumenfeld', 'Clementine']:
    print(name, end=' ')


# In[ ]:


for name, age in [('Alexandra', 23), ('Belle', 28), ('Craig', 15)]:
    print(name, "is", age, "years old")


# > **Your turn:** Create a list of words called `words`, and then iterate it and for each word print the sentence "The word _'word'_ has _x_ letters". Do it in 2 ways: by iterating the words themselves and by iterating the index of the list.

# ## The `range()` function

# [`range()`](https://docs.python.org/3/library/stdtypes.html#range) is a utility function which generates an iterable sequence of integers. The full syntax allows three inputs - `start`, `stop` & `step`, where the resulted iterable iterates from `start` to `stop` (not including) in steps of `step`.

# In[ ]:


for i in range(9):
    print(i, end=' ')


# In[ ]:


for i in range(3, 9):
    print(i**2, end=' ')


# #### Example

# Find all the numbers from 11 to 999 which are made only from a single digit.

# In[ ]:


for i in range(10, 1000):
    if len(set(str(i))) == 1:
        print(i, end=' ')


# #### Example

# Find all the multiples of 7 from 1 to 100.

# In[ ]:


for i in range(7, 100, 7):
    print(i, end=' ')


# > **Discussion:** In Python we have **Iterables**, **Iterators** & **Generators**. `range()` does not return a simple list, but a generator, which is out of the scope of this course. For now, all we need to know about iterators and generators is that we can (1) iterate over them, and (2) see their content with `list()` (e.g. `nums = list(range(10))`.

# > **Further reading:** More about generators can be found in [Python's Wiki page about generators](https://wiki.python.org/moin/Generators) and in [Programiz](https://www.programiz.com/python-programming/generator). If you are new to Python, I would wait until learning about functions... 

# ## Initialization

# Many times, each iteration will modify a common object, until finally the object will get its final form. If this is the case, then usually an initialization of the object and the relevant variables is necessary.

# #### Example

# Choose a number _n_ and find: <Br>
# * Part A - the sum of the numbers from 1 to n <br>
# * Part B - the sum of the numbers from 1 to n that are divisible by 3. <br>

# In[ ]:


n = 100


# ##### Part A

# In[ ]:


# Initialization
sum_all = 0
# Iteration
for i in range(1, n+1):
    sum_all += i  # equivalent to "sum_all = sum_all + i"
print (sum_all)


# ##### Part B

# In[ ]:


# %%timeit
# Initialization
sum_by_3 = 0
# Iteration
for i in range(1, n+1):
    if i % 3 == 0:
        sum_by_3 += i
print (sum_by_3)


# > **Your turn:** Improve the solution to part B by iterating only the relevant numbers.

# ## Everyting (almost) is iterable

# The fact that `for`-loops in Python can iterate the actual elements of objects is very useful. In the examples below we see that nearly all the data types and data structures we know are actually iterables.

# #### Strings

# The iteration is done on the characters.

# In[ ]:


my_string = 'Beautiful'
for ch in my_string:  # "ch" for "character"
    print (ch, end= ' ')


# #### Lists

# The iteration is done on the elements in their native order.

# In[ ]:


my_list = ['Apple', 'Banana', 'Carrot', 'Fig']
for el in my_list:  # "el" for "element"
    print (el, end= ' ')


# These, of course, can be combined...

# In[ ]:


my_list = ['Apple', 'Banana', 'Carrot', 'Fig']
for el in my_list:  # "el" for "element"
    for ch in el:
        print (ch, end=' ')
    print ('-->', end=' ')


# #### Tuples

# Like all sequences before, the iteration is done on the elements in their native order.

# In[ ]:


my_tuple = tuple(my_list)
for el in my_tuple:  # "el" for "element"
    print (el, end=' ')


# #### Sets

# The iteration is done on the elements, and is **unordered**.

# In[ ]:


my_set = set('Sets have no order and no duplication')
for el in my_set:
    print (el, end=' ')


# #### Dictionaries

# The default iteration is through the keys

# In[ ]:


my_dict = {'Avi': '12-Oct-1982', 'Betty': '7-Jun-1979',
           'Carl': '31-Jan-1977', 'David': '15-Mar-1968'}


# In[ ]:


for name in my_dict:
    print (name)


# The iteration can also be performed through the **views** `keys()`,  `values()` and `items()`.

# In[ ]:


for key in my_dict.keys():
    print (key)


# In[ ]:


for val in my_dict.values():
    print (val)


# In[ ]:


for item in my_dict.items():
    print(item)


# In[ ]:


for item in my_dict.items():
    print (item[0], '\t', item[1])


# `dictionary.items()` generate a sequence of *tuples* in the form of (key, value). we can iterate over these tuples as in the example above, or we can **unpack** the tuples to different varaibles. This is another use-case where using unpacking make our code cleaner and easier to read.

# In[ ]:


for item in my_dict.items():
    name, birthday = item
    print (name, '\t', birthday)


# but we can also perform the unpacking inside the `for` loop and avoid unnecessary extra assignment

# In[ ]:


for name, birthday in my_dict.items():
    print (name, '\t', birthday)


# > **Further reading:** Although this technique is called "tuple unpacking", we can perform unpacking to any iterable object (such as lists). you can read more about tuple-unpacking in this [link][1]
# 
# [1]: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/ "tuple unpacking blog post"

# #### Example

# Write a sentence, and create a dictionary `d_counter` of the form `{letter: count}`, where `count` is the number of times `letter` appears in the sentence.
# 
# Notes:
# * Only letters that appear in the sentence should appear in the dictionary
# * Do not make a distinction between upper-case and lower-case letters (e.g. 'a' and 'A' should be "grouped").
# * Use the string method `isalpha()` to decide whether a character is a letter or not.

# In[4]:


sentence = "God will forgive me. That's his job. (Heinrich Heine, 1797 - 1856)"


# In[ ]:


d_counter = {}
lower_sentence = sentence.lower()
characters = set(lower_sentence)
for ch in characters:
    if ch.isalpha():
        d_counter[ch] = lower_sentence.count(ch)
print(d_counter)


# > **Your turn:** Iterate the dictionary `d_counter` and answer the question which letter is the most frequent.

# > **Discussion:** It is not advised to change mutable object while iterating them. Consider what should be printed by the following script:
# >
# > ```python
# > lst = ['a', 'b', 'c', 'd', 'e', 'f']
# > for letter in lst:
# >     print(lst.pop())
# ```

# ## Exercises

# ### Exercise 1

# Write a sentence and count the number of times the letter ‘m’ appears in it using a for-loop.

# #### Solution

# In[ ]:


sentence = "This is my magnificent example."
my_letter = 'm'


# In[ ]:


counter = 0
for letter in sentence:
    if letter == my_letter:
        counter += 1
print(counter)


# ### Exercise 2

# Write a sentence and do the following:
# 
# 1. Count how many vowels are in it, including repetitions (e.g. ‘abracadabra’ $\rightarrow$ 5)
# 2. Count how many vowels are in it, excluding repetitions (e.g. ‘abracadabra’ $\rightarrow$ 1)
# 3. Create a dictionary with items of the form {letter: number of occurrences}. Note that letters which are not in the sentence should not appear as keys in the dictionary.

# #### Solution

# In[ ]:


pangram = "the quick brown fox jumps over the lazy dog".lower()


# > **Reference:** What is so special about the sentence [the quick brown fox jumps over the lazy dog](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog)?

# ##### Part I

# In[ ]:


counter = 0
for x in 'aeiou':
    counter += pangram.count(x)
print (counter)


# ##### Part II

# In[ ]:


counter = 0
for x in 'aeiou':
    counter += x in pangram
print (counter)


# > **Note:** The fact that Booleans can be summed as 0 and 1 saves an _if_ statement.

# ##### Part III

# In[ ]:


counter_dict = {}
for ch in set(pangram):
    if ch.isalpha():
        counter_dict[ch] = pangram.count(ch)
print(counter_dict)


# ### Exercise 3

# Write a code that reverses a given list, where…
# 1.	the flipped list is a new list.
# 2.	the flipping is done in-place. **(difficult)**

# #### Solution

# ##### Part I

# In[ ]:


my_list = ['a', 'b', 'c', [], 1, 2, 3, {}, True, False]


# ###### Solution 1

# In[ ]:


flipped = []
for el in my_list:
    flipped.insert(0, el)
#     print flipped
print (flipped)


# ###### Solution 2

# In[ ]:


flipped = []
for i in range(len(my_list)):
    flipped.append(my_list[len(my_list)-1-i])
#     print flipped
print (flipped)


# ##### Part II

# Note that this solution changes _my_\__list_ during iterations, which is not advised.

# In[ ]:


for i in range(len(my_list)):
    my_list.insert(0, my_list.pop(i))
print (my_list)


# ### Exercise 4

# 1. Create a dictionary with 10 items of the form {name: age}.
# 2. Calculate the average age of the guys on the dictionary.
# 3. Remove from the dictionary all the guys below the average age.

# #### Solution

# In[ ]:


tribes = {'Reuven': 23, 'Simeon': 34, 'Levi': 51, 'Judah': 36,
          'Dan': 36, 'Naphtali': 25, 'Gad': 36, 'Asher': 27,
          'Issachar': 41, 'Zebulun': 19, 'Joseph': 24, 'Benjamin': 28}


# ##### Part I

# In[ ]:


sum_of_ages = 0.0 
for age in tribes.values():
    sum_of_ages += age
average_age = sum_of_ages / len(tribes)
print (average_age)


# ##### Part II

# In[ ]:


to_remove = []
for tribe, age in tribes.items():
    if age < average_age:
        to_remove.append(tribe)
        
for item in to_remove:
    tribes.pop(item)

print (tribes)


# ### Exercise 5

# Summing the integers from 1 (1, 2, 3...), at which integer the sum will exceed 1000?
# 
# > Can you answer the question without unnecessary printouts. **(difficult)**

# #### Solution

# ##### Part I

# In[ ]:


sum_of_nums = 0
for i in range(1, 50):
    sum_of_nums += i
    if sum_of_nums > 1000:
        print ("The number is", i)


# ##### Part II

# We can use a Boolean **flag** to indicate when there is no need for further printing.

# In[ ]:


sum_of_nums = 0
reached = False
for i in range(1, 100):
    if sum_of_nums < 1000:
        sum_of_nums += i
    elif sum_of_nums > 1000 and not reached:
        print ("The number is", i-1)
        reached = True


# ### Exercise 6

# There are $n<200$ houses in the street, and the sum of the numbers below the $k$-th house is equal to the sum of numbers above it. How many houses are in the street? Can you find it without Python?

# #### Solution

# In[ ]:


for n_houses in range(2, 200):
    for k in range(1, n_houses):
        if sum(range(1, k)) == sum(range(k+1, n_houses)):
            print(k, n_houses)


# # List comprehension

# The combined utilization of lists and _for_ loops is so common, that there is a special syntax for it called **list comprehension**. This syntax is never mandatory, but it is so simple and clean, that it became a standard for Python code writing, and it is definitely a sign of coding maturity.

# ### Basic approach

# In short - list comprehension is a compact way for creating a list from another list. It aimes to save some of the standard syntax and some of the lines and to yield a one-liner readible code. The syntax for creating _list2_ from _list1_ is `list2 = [ f(x) for x in list1 ]`, and the proper way to "read" this line is: **"For every element *x* in _list1_, apply the function *f* to _x_ and append the result to *list2*"**.

# #### Illustration

# We wish to make a list of all the squares (1, 4, 9, 16...) up to $10^{2}=100$. We are talking about making a new list of values from the list `range(1, 11)`, so list comprehension is very suitable here. Let's compare the standard syntax with the syntax of list comprehension.

# In[ ]:


squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)


# While the iterating is still visible (`for...in`), The initialization and appending are done internally.

# In[ ]:


squares = [i**2 for i in range(1,11)]
print(squares)


# ### Adding conditioning

# Another feature of the list comprehension syntax is the conditioning, which allows to apply the function `f()` and to append the result to `list2` only if a specific condition `cond()` is fulfilled. The syntax for this is an extension of the syntax above: `list2 = [f(x) for x in list1 if cond(x)]`

# #### Illustration

# Repeat example 1, but include only the squares of the odd numbers. Again, we compare both syntaxes.

# In[ ]:


squares = []
for i in range(1, 11):
    if i % 2 == 1:
        squares.append(i ** 2)
print(squares)


# In[ ]:


print([i**2 for i in range(1, 11) if i % 2 == 1])


# #### Example

# * Part I - For a given number, create the list of its divisors.
# * Part II - Create a dictionary of the form {i, divisors} for all numbers from 1 to 10.
# * Part III - Create a list of all the numbers from 1 to 10 that have exactly 4 divisors.

# ##### Part I

# In[ ]:


N = 10
div_list = [d for d in range(1, N+1) if N % d == 0]
print (div_list)


# ##### Part II

# In[ ]:


div_dict = {}
for n in range(1, N+1):
    div_dict[n] = [d for d in range(1, n+1) if n % d == 0]
div_dict


# ##### Part III

# In[ ]:


[i for i, i_divs in div_dict.items() if len(i_divs) == 4]


# > **Your turn:** Create a list of "random" words, and then use list comprehension to create a list of all the words that contain at least one letter more than once (e.g. dad, mummy, ~car~, roar, ~israel~).

# > **Further reading:** Dictionary comprehension and Set comprehension are also supported with intuitive syntax as illustrated below. More about that can be found at the [official Python docs about data structures](https://docs.python.org/3/tutorial/datastructures.html).
# >
# > ```python
# sentence = "God will forgive me. That's his job. (Heinrich Heine)"
# counter = {ch: sentence.lower().count(ch) for ch in sentence}
# letters = {ch for ch in sentence.lower() if ch.isalpha()}
# ```

# ## Exercises

# ### Exercise 1

# Write a sentence and count the number of times the letter ‘m’ appears in it using a for-loop.

# #### Solution

# In[ ]:


sentence = "This is my magnificent example."
my_letter = 'm'


# In[ ]:


print (len([letter for letter in sentence if letter == my_letter]))


# ### Exercise 2

# Create a list of 10 words.
# 
# 1. Create a list of the lengths of the words.
# 2. Create a list of the words which have more than 4 letters.

# #### Solution

# In[ ]:


sentence_string = "An investment in knowledge pays the best interest (Benjamin Franklin)"
sentence_list = sentence_string.split()


# ##### Part I

# In[ ]:


print ([len(word) for word in sentence_list])


# ##### Part II

# In[ ]:


print ([word for word in sentence_list if len(word)>=4])


# ### Exercise 3

# Write a code that reverses a given list, where…
# 
# 1. the flipped list is a new list.
# 2. the flipping is done in-place. **(difficult)**

# #### Solution

# ##### Part I - new list

# In[ ]:


my_list = ['a', 'b', 'c', [], 1, 2, 3, {}, True, False]

N = len(my_list)
flipped = [my_list[N-i] for i in range(1, N+1)]
print (flipped)


# ##### Part II - in-place

# In[ ]:


my_list = ['a', 'b', 'c', [], 1, 2, 3, {}, True, False]

[my_list.insert(0, my_list.pop(i)) for i in range(len(my_list))]
print (my_list)


# # The _while_ loop

# The `while` statement executes a block of code as long as a specified **iteration condition** is fulfilled. Unlike the `for` loop, it does not utilize an iteration variable, but rather depends on the results during the execution of the code, which may change the truth value of the iteration condition. The `while` loop is specifically useful when the theoretical number of iterations is infinite or unknown.
# 
# It is very often a confusing matter to apply the `while` loop properly, and below are some things to consider when implementing such a loop:
# 
# * The "testing" of the iteration condition happens `before` any iteration is executed. That includes the first iteration.
# * If nothing is changed inside the loop, then the condition will never be fulfilled, and the loop will run infinitely.
# * One of the vulnerabilities of `while` loops are the **edge cases**. Deal with them carefully.

# ### Example

# Find the first number to have exactly 20 divisors.

# In[ ]:


n = 0
n_divs = 0
while n_divs != 20:
    n += 1
    n_divs = len([d for d in range(1, n+1) if n % d == 0])
print (n)


# > **Discussion:** The order of actions is very important within the `while` loop due to the edge cases. In the example above, if the two lines of the iteration block are flipped, the result is wrong.

# > **Your turn:** Find the third number to have exactly 20 divisors.

# ## Exercises

# ### Exercise 1

# Summing the integers from 1 (1, 2, 3...), at which integer the sum will exceed 1000?

# #### Solution

# In[ ]:


i = 0
sum_of_nums = 0
while sum_of_nums <= 1000:
    i += 1
    sum_of_nums += i
print ("The number is", i)


# # Skipping iterations

# There are situations in which you wish to skip an iteration or even completely terminate the loop, and this behavior can be achieved by two special words:
# 
# * **continue** will quit the current iteration and start the next one.
# * **break** will terminate the entire loop and proceed with the outer code execution.
# 
# The following should be noted for both statements:
# 
# * They are applicable only within a _for_- or a _while_-loop. Otherwise an error will be raised.
# * They refer only to the inner-most loop in which they are called.
# * They can be used within infinte loops as well

# ### Basic examples

# The following code will print the letters of the word 'Python' which are not vowels.

# In[ ]:


for letter in "Python":
    if letter in 'aeiou':
        continue
    print (letter, end=' ')


# The following code will print the letters of the word 'Python' **until** it reaches a vowel.

# In[ ]:


for letter in "Python":
    if letter in 'aeiou':
        break
    print (letter, end=' ')


# The following code will do the following for each word in the sentence:
# 
# * If the letter 'r' is in the word, it will do nothing
# * If the letter 'r' is not in the word, then letters of the word will be printed until the letter 'n' (if exists), and then it will show the original word.

# In[ ]:


sentence = "Continue and break are useful"
for word in sentence.split():
    if 'r' in word:
        continue
    for letter in word:
        if letter == 'n':
            break
        print (letter, end=' ')
    print ("-", word)


# ### Example

# Make the list of all the numbers between 1 and 1000 that are divisible by **all of** 6, 15 & 35.

# In[ ]:


good_numbers = []
for i in range(1, 1001):
    if i % 6 != 0:
        continue
    if i % 15 != 0:
        continue
    if i % 35 != 0:
        continue
    # if you made it to here,
    # then you are divisible by all the numbers
    good_numbers.append(i)
print (good_numbers)


# > **Your turn:** Find all the numbers between 1 and 100 that are divisible by **at least one of** 6, 15 & 35.

# > **Your turn (bonus):** All the numbers between 1 and 100 that are divisible by **exactly one of** 6, 15 & 35.

# ### Grand example

# Find a solution to the following verbal arithmetic puzzle, in which every letter stands for a different digit from 1 to 9:
# <center>$\frac{ABCD}{EFGHI}=\frac{1}{3}$</center>

# > **Reference:** This puzzle is puzzle #88 in [Henry Dudeney's fantastic *Amusements in Mathematics*](http://djm.cc/library/Amusements_in_Mathematics_Dudeney_edited02.pdf) from 1917. All the puzzles from this chapter (entitled Digital Puzzles) can be easily solved with Python.

# In[ ]:


frac = 1.0/3
found = False
for numerator in range(1234, 10000):
    if '0' in str(numerator):
        continue
    if len(set(str(numerator))) < 4:
        continue
    for denominator in range(12345, 98765):
        if '0' in str(denominator):
            continue
        if len(set(str(numerator) + str(denominator))) < 9:
            continue
        if float(numerator) / denominator == frac:
            found = True
            break
    if found:
        break
print (numerator, "/", denominator, "=", frac)


# ## Exercises

# ### Exercise 1

# Summing the integers from 1 (1, 2, 3...), at which integer the sum will exceed 1000?

# #### Solution

# In[ ]:


sum_of_nums = 0
for i in range(1, 100):
    sum_of_nums += i
    if sum_of_nums > 1000:
        print ("The number is", i)
        break


# ### Exercise 2

# *   Create 2 variable- lower,upper.
# *   Please calculate all the prime numbers between these 2 numbers
# 
# 

# #### Solution

# In[ ]:


lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

