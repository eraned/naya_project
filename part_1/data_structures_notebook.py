#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In many cases the data we work with has to be organized. This is obvious when we talk about tables and databases, but it is not less crucial when we deal even with the simplest data objects. Every program language provides its programmers with many built-in data structrues to allow this "organization". It is up to us, though, to use the most appropriate structure for each task.
# 
# Similar to the data types, each data structure supports specific operations, which are optimized to its characteristics. Python provides several dozens of built-in data structures, and in this chapter we will learn about the most notable four:
# 
# * list
# * tuple
# * dictionary
# * set
# 
# As noted earlier, one of the most important characteristics of a data structure is its (im)mutability, therefore it is important to keep in mind which data structure is mutable and which is not.

# # Lists

# List is a sequence of elements. That's it.

# > **Reminder:** *sequence* is Python's generic term for an ordered set of elements. Strings are also sequences.

# To create a list we usually use the `[]` constructor, either with or without elements, separated by commas if present. Alternatively we can use the `list()` function, which is useful in some specific scenarios. The elements don't have to be of the same type, and they can even be of type _list_ themselves.

# In[ ]:


list0 = []

list1 = [4.2, 'House', 3, False, ['a', False, 1, 'book'], [], 'dog']


# ## Lists are sequences

# Lists are sequences, so they support all the sequences operations we already met when we learned about strings. These include indexing and slicing, the _len()_ function, the _in_ operator, concatenation with the '+' sign, the _index()_ method, etc. 

# ### Indexing and slicing

# Specific index returns the element itself (which may be a list itself)

# In[ ]:


print(list1[3])
print(list1[-3])


# Slicing returns a list

# In[ ]:


print(list1[3:5])
print(list1[2:-1])
print(list1[2:])


# In[ ]:


print(list1[2])
print(list1[2:3])


# It should be noted that when we refer to a list as an element of a list, then we should use **chained indexing** and not think of it as a two-dimensional object.

# In[ ]:


print(list1[4][3])


# > **Your turn:** For the same `list1`, calulcate the following expressions by yourself, and then check with Python (note also the data type of each answer):
# > * `list1[1][-2]`
# > * `str(list1[0])[1]`
# > * `len(list1[-1])`
# > * `list1[len(list1[1])-1][0][0]`

# ### Other illustrations

# In[ ]:


details = ['John', 'Doe', 'm', 32, 'Tel Aviv', False, 1.71]


# In[ ]:


print(len(details))


# In[ ]:


print('John' in details)
print('Jon' in details)
print(['John'] in details)


# In[ ]:


print(details[:3] + details[4:5])


# > **Note:** Why will `details[:3] + details[4]` not work?

# In[ ]:


print(details.index(32))


# ## Common operations

# > **Reference:** The full list of methods can be found in the [official docs](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types).

# ### Lists are mutable

# Unlike strings, lists are **mutable** objects, which means their value(s) can change during runtime. 

# In[ ]:


print(details)
details[3] = 33
print(details)


# As we just saw, this can be done by simply reassigning the values of the elements in the list. However, as we will see below, it is much more convenient to apply the various methods which allow to modify their content. Such methods modify the list object **in-place** and usually do **not** return the modified list itself. What they do return is `None`.
# 

# ### Adding elements - append(), insert() & extend()

# 
# * `append(x)` - adds the element `x` at the end of the list
# * `insert(i, x)` insert the element `x` at the i-th place
# * `extend(iter)` - concatenate the elements of iter` to the list

# In[ ]:


list1 = ['Aa', 'Bb']

list1.append('Dd') 
print(list1)

list1.insert(2, 'Cc')
print(list1)

list1.extend(['Ee', 'Ff'])
print(list1)


# > **Discussion:** we saw in the last lesson that we can chain functions after each other, for example:
# ```python
# full_name_string.replace('a', 'A').replace('i', 'I')...
# ```
# This will not work with lists and append:
# ```python
# my_list.append(item1).append(item2)```
# >
# > why?

# ### Removing elements - pop() & remove()

# * `pop(i)` - Remove the item at index i (and returns it)
# * `remove(x)` - Remove item x

# In[ ]:


list1 = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff']
print(list1)

list1.pop(2)
print(list1)

list1.pop()
print(list1)

list1.remove('Aa')
print(list1)


# **Discussion:** Where are the popped elements?

# ## Lists and strings - `join()` and `split()`

# It is a very common task to switch from strings to lists and vice versa, so it is useful to be proficient with the relevant methods:
# 
# * **String $\longrightarrow$ List**: `s.split([sep])` splits the string `s` by `sep` occurrences and returns a list of strings from the splitted parts
# * **List $\longrightarrow$ String**: `sep.join(lst)` concatenates the elements of `lst` (assuming they are all strings), and separates them by `sep`

# In[ ]:


sentence = 'I love you'


# In[ ]:


print(sentence.split())
print(20*'~')
print(sentence.split('o'))


# In[ ]:


print('#'.join(sentence.split()))
print(20*'~')
print(' ~ O ~ '.join(sentence.split()))


# > **Note:** Many students are confused how `join()` works. Try to beat the statistics...

# ## Exercises

# ### Exercise 1

# 1.	Create two lists of strings:
#     * _boys_ with 3 names of boys
#     * _girls_ with 3 names of girls.
# 2.	Do the following with list methods:
#     * Use _append()_ to add _boys_ a 4th name at the end.
#     * Use _insert()_ to add _girls_ a 4th name at the beginning.
#     * Use _pop()_ to remove from _girls_ the last name and assign it to a variable called _bride_.
#     * Use _pop()_ to remove from _boys_ the first name and assign it to a variable called _groom_.
#     * Use _remove()_ to remove the last name from boys.
#         * Can you do it without knowing the actual name of the last boy.
#     * Create a **new** list called _names_, which is the concatenation of _boys_ and _girls_.
#         * Why will _extend()_ not do the job?

# #### Solution

# In[ ]:


boys = ['Hagai', 'Binyamin', 'Itamar']
girls = ['Shoshana', 'Noga', 'Reut']


# In[ ]:


boys.append('Iddo')
print (boys)


# In[ ]:


girls.insert(0, 'Ahuva')
print (girls)


# In[ ]:


bride = girls.pop()
print (girls)
print (bride)


# In[ ]:


groom = boys.pop(0)
print (boys)
print (groom)


# In[ ]:


boys.remove(boys[-1])
print (boys)


# In[ ]:


names = boys + girls
names


# _boys.extend(girls)_ will change the list _boys_ itself and will not return a new list.

# ### Exercise 2

# 1. Create three variables of type list representing three guys. Each list should be of the form [name (string), age (int), married (Boolean)]. Give the lists proper variable names.
# 2. Modify the age of one of the guys. Note that lists are mutable, so you can do that using direct assignment and there is no need to recreate the entire list.
# 3. Create a **new** list called _guys_, whose elements are the three lists you’ve created. Note that you've created a list of lists.
# 4. Create a list for another "guy" and append it to _guys_.
# 5. Modify the age of one of the guys in _guys_. Again - remember that _guys_ is mutable, so you can "access" its elements and modify them directly.
# 6. Remove one of the elements of _guys_ with two different methods:
#     * using pop()
#     * using remove()

# #### Solution

# In[ ]:


person1 = ['Harry', 16, False]
person2 = ['Ron', 15, False]
person3 = ['Hermione', 16, False]


# In[ ]:


person2[1] = 17


# In[ ]:


guys = [person1, person2, person3]
print (guys)


# In[ ]:


person4 = ['Hagrid', 68, True]
guys.append(person4)
print (guys)


# In[ ]:


guys[3][1] = 67
print (guys)


# In[ ]:


guys.pop(2)


# ### Exercise 3

# 1. Write a sentence (string) and assign it to a variable called _sentence_. 
# 2. Print your sentence, so that every word is printed in a new line.
# 3. Count how many times the letter ‘m’ appears in _sentence_ in two differnt ways:
#     * by using the string method count().
#     * without using the string method count().

# #### Solution

# In[ ]:


sentence = 'This is my magnificent example'


# In[ ]:


sentence_list = sentence.split()
print(sentence_list)


# In[ ]:


sentence_in_lines = '\n'.join(sentence_list)
print(sentence_in_lines)


# In[ ]:


# Solution 1
num_of_m_1 = sentence.count('m')
print (num_of_m_1)

# Solution 2
num_of_m2 = len(sentence) - len(sentence.replace('m', ''))
print(num_of_m2)

# Solution 3
num_of_m_3 = len(sentence.split('m')) - 1
print (num_of_m_3)


# # Tuples

# [Tuples](https://docs.python.org/3/library/stdtypes.html#tuples) are the **immutable** version of lists.
# 
# To create a tuple we use the `()` constructor with elements separated with commas. Alternatively we can use the `tuple()` function.
# The elements don't have to be of the same type, but they do have to be immutable themselves (see *Further reading* below).
# 
# _tuple_ is also a sequencial data type, and as such it support all the related methods, but none of the in-place methods is valid.
# 
# 

# > **Further reading:** You can read [here](https://stackoverflow.com/questions/9755990/why-can-tuples-contain-mutable-items) more about why we can assign mutable objects (variables) to tuples
# 
# 
# 

# > **Note:** Since `tuple` is the default data structure in Python, elements separated by commas will automatically be assigned to a tuple. This is pretty conventional with the `return` statement which we will meet in the [chapter about functions](https://drive.google.com/drive/folders/1k_wyAY5tvc6_A834DesEhry62v_-AUSa?usp=sharing).

# In[ ]:


tup0 = ()
print(type(tup0))


# In[ ]:


tup1a = ('a', )
tup1b = 'a',


# In[ ]:


tup2a = ('a', 'b')
tup2b = 'a', 'b'


# ## Tuples are sequences

# Tuples, being sequences themselves, behave much like lists.
# 

# In[ ]:


tuple1 = (1, 4.2, 'House', 2.8,
          False, ('a', False, 1, 'book'),
          5.331, 'dog')


# In[ ]:


print (len(tuple1))
print (tuple1[3:6])
print ('dog' in tuple1)
print (tuple1.index(2.8))


# ## Tuples are immutable

# Tuples are immutable, so their content cannot be altered. This means they do not support assignment and that many methods do not apply to them.

# In[ ]:


# tuple1[5] = 3.2


# In[ ]:


# tuple1.append(3.2)


# ## Unpacking
# 
# Tuple unpacking (aka mutiple assignment) allows us to extract (unpack) values in tuple to different variables.

# In[ ]:


person_details = 'Shealtiel', 33, False  # (name, age, Married)
name, age, married = person_details


# In[ ]:


print(name)
print(age)
print(married)


# Actually, we already saw this tuple-unpacking feature before. Last lesson we saw that we can assign multiple variables at the same time in one line of code.

# In[ ]:


num1, num2 = 1234, 4321

print('num1 =', num1)
print('num2 =', num2)


# ## Lists vs. tuples

# Even though you might not understand the big difference between the two data structures right now, it will become very intuitive later, when the concept of mutability will be fully understood.
# 
# Lists are used when the data itself is constantly changing during the execution. Some example are guests in a party, records in a database, dates when something happened, etc. Tuples are used when the data cannot be changed, which is frequently the case for meta-data. Some examples are personal details, coordinates, etc.
# 
# Thumb rule (as noted in [Python core developer's tweet][1]): usually lists will contain homogeneous items (i.e. items with the same type) while tuples will contain more heterogeneous items (although its also common to see homogeneous tuples in some cases, such as coordinates). Tuples can be seen as Python's way of collecting related heterogeneous pieces of information under one roof. 
# 
# Also, since tuples are immtuables, they have simpler objects and fixed size so they are faster to work with
# 
# [1]: https://twitter.com/raymondh/status/324664257004322817

# In[ ]:


get_ipython().run_line_magic('timeit', 'x=(1,2,3,4,5,6,7)')
get_ipython().run_line_magic('timeit', 'x=[1,2,3,4,5,6,7]')


# > **Reference:** More about IPython's [Magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

# ### Exercise 1

# 
# 
# 1.   create 2 variables with value in **one sentence**
# 2.   replace between the variables value
# 3. print the replaced variables
# 

# #### Solution

# In[ ]:


num1,num2=5,7
num3=num2
num2 = num1
num1=num3

print("the first num is", num1,"the second num is" , num2)


# # Dictionaries

# [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) is a mapping object made of **items**, each of which is made of a **key** and a **value**.
# 
# To create a dictionary we usually use the `{}` constructor, either with or without elements (if elements are specified, they are separated by commas, and each of them is separated with a colon (e.g., `{key1: value1, key2: value2}`)). Alternatively we can use the `dict()` function, which is useful in some specific scenarios.
# 
# 
# 

# In[ ]:


my_dict = {1: 'two', 2: 'three', 4: 'five'}
print(my_dict)


# ## Fundamentals

# Let's create some dictionaries to work with.

# In[ ]:


dict0 = {}

dict1 = {1879: 'Albert Einstein was born',
         1914: 'World-War 1'}

dict2 = {1939: 'World-War 2',
         1948: 'Israel declaration of independence'}

dict3 = {'Fruits': ['Apple', 'Banana', 'Orange'],
         'Vegetables': ['Tomato', 'Cucumber', 'Onion'],
         'Other': ['Meat', 'Bread', 'Rice']}


# ### Getting and setting
# 
# Like for lists (and actually all over Python...), the `[]` syntax is used for getting and setting values of the dictionary. Dictionaries differ from lists primarily in how elements are accessed. in lists we use the position of items in the list (i.e. their indcies) while in dictionaries we use user-defined keys.

# In[ ]:


print(dict1[1879])
print(dict3['Fruits'])
print(dict3['Fruits'][1])


# In[ ]:


dict1[1492] = 'Christopher Columbus finds the new world'
print(dict1)


# Calling a non-existent key raises an error.

# In[ ]:


print(dict2[1])


# > **Note**: in previous version of Python (3.5 or earlier) Dictionaries were unordered data structure, and one could not rely on such order when writing a code (and therefore there is additional built-in [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) data structure. In Python 3.6, a new implementation of the dict data structure was introduced, which is keeping the items order. This is relevant for iterations and print-outs, but less to the practical use.

# Dictionaries are mutable. Moreover, you can modify its "inner" elements (if they are mutable...).

# In[ ]:


dict3['Fruits'].append('Peach')
print (dict3)


# > **Further reading:** By definition, the keys of a dictionary must be unique and immutable (the actual requirement is called **hashable**, but we will not get into it in this course). There are no limitations about the values. we can use any type of object as value (including values, another dict, custom object etc.). More about hashable objects and why they are useful can be found in the [Python glossary](https://docs.python.org/3/glossary.html) and in this nice intro from [Programiz](https://www.programiz.com/python-programming/methods/built-in/hash).

# ### Limitations

# The keys must be unique

# > **Note:** Python will not raise an error, but simply replace the existing value with a new value.

# In[ ]:


bad_dict_1 = {'Boris': 'Metula', 'Alex': 'Jerusalem', 'Genadi': 'Rehovot', 'Alex': 'Yeruham'}
print(bad_dict_1)


# The keys must be hashable

# In[ ]:


# bad_dict_2 = {['pen', 'pencil', 'brush']: 'writing',
#               ['piano', 'trumpet', 'drum']: 'playing',
#               ['dog', 'cat', 'mouse']: 'animals'}


# ### _keys()_, _values()_ & _items()_

# The three most important methods of dictionaries are `keys()`, `values()` and `items()`, which all return sequence (set-like) **view** objects containing the relevant data.

# In[ ]:


customers = {62896715: 'Tel-Aviv', 82631105: 'Jerusalem',
             77290611: 'Tel-Aviv', 48801272: 'Tel-Aviv'}


# In[ ]:


print (type(customers.keys()))
print (type(customers.values()))
print (type(customers.items()))


# In[ ]:


print (list(customers.keys()))
print (customers.values())
print (customers.items())


# > **Furtehr reading:** In Python2, `keys()`, `values()` and `items()` returned lists. This changed to view objects in Python3. views are **dynamic** objects reflects the underlying dictionary. any change in the dictionary will be reflected in the view. Dictionary views are sequences. they can be iterated over to yield their respective data and support membership tests (e.g. `X in dict.keys()`). We can convert these view objects to lists by using list() function (i.e. `list(dict.keys)`) but these are static lists which will not be updated if the dictionay is changed. You can read more about it in the [official docs](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects) and in [this SO answer](https://stackoverflow.com/a/8960727/3121900).
# 

# see the how view change with changes in the dictionary:

# In[ ]:


dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

keys = dishes.keys()
values = dishes.values()
keys_list = list(dishes.keys())
values_list = list(dishes.values())

print('before delete:')
print("Keys in view: ", keys)
print("values in view: ", values)
print("Keys in list: ", keys_list)
print("values in list: ", values_list)

del dishes['eggs']

print('after delete')
print("Keys in view: ", keys)
print("values in view: ", values)
print("Keys in list: ", keys_list)
print("values in list: ", values_list)


# > **Your turn:** We want to create a dictionary of the form `{subject: [grade1, grade2]}` to hold our grades (note that the grades in each subject should be a list). <br>
# Start with an empty dictionary called `grades` and do the following tasks:
# > * Add the following grades to the dictionary *one by one*:
# >     * Math - 78
# >     * English - 92
# >     * History - 88
# >     * English - 79
# >     * Math - 90
# > * Find the average score of each subject

# ## Common operations

# ### `pop(key)`

# The method _pop(key)_ removes from and return the dictionary the **item** whose **key** is _key_.

# In[ ]:


friends = {'Avi': ('Eilat', 35),
           'Ben': ('Haifa', 28),
           'Gil': ('Ashdod', 32)}


# In[ ]:


val = friends.pop('Ben')
print (friends)
print(val)


# Trying to pop by the item or value will not work.

# In[ ]:


# friends.pop(('Eilat', 35))


# ### The function `len()`

# The function _len()_ returns the number of items in the dictionary.

# In[ ]:


print(len(friends))


# ### The operator `in`

# The operator _in_, like all the other _dict_ operations, works through the keys, and return _True_ if the element is a key in the dictionary.

# In[ ]:


legs = {'Zebra': 4, 'Spider': 8, 'ant': 6, 'lion': 4,
        'chicken': 2, 'man': 2, 'millipede': 'Infinity'}


# In[ ]:


print('ant' in legs)
print(6 in legs)
print(('ant', 6) in legs)


# To compare, the following tests are perform on the corresponding .

# In[ ]:


print('ant' in legs.keys())
print(6 in legs.values())
print(('ant', 6) in legs.items())


# Since lists are mutable, they can't be keys of a dictionary. This is so fundamental, that an error is raised even before the lookup is performed.

# ## Exercises

# ### Exercise 1

# 1. Create a dictionary with 3 items of the following form:
#     * key – a letter
#     * value – a list of words starting with the key letter
# 2. Use the mutability of the dictionary to add a new word to each of the dictionary items without recreating its values.
# 3. Add a new item to the dictionary.
# 4. Remove an item from the dictionary.
# 5. Create a list, whose elements are the lists of words from the dictionary.

# #### Solution

# In[ ]:


my_dict = {'p': ['pizza', 'problem'],
           'b': ['building', 'brain'],
           'f': ['fight', 'flag']}
print (my_dict)


# In[ ]:


my_dict['p'].append('play')
my_dict['b'].append('ball')
my_dict['f'].append('fire')
print (my_dict)


# In[ ]:


my_dict['g'] = ['gold', 'glory', 'goat']
print (my_dict)


# In[ ]:


my_dict.pop('b')
print (my_dict)


# In[ ]:


all_lists = my_dict.values()
print (all_lists)


# # Sets

# ## Fundamentals

# _set_ is a collection object with **no order** and **no repetitions**.
# 
# To create a set we usually use the set() constructor, either with or without elements (if elements are specified, they are separated by commas). After creation, all duplications are removed, and the remaining elements are conventionally called **keys**.

# In[ ]:


tour = ['Jerusalem', 'Tel-Aviv', 'Haifa', 'Tel-Aviv', 'Jerusalem']
cities = set(tour)
print (cities)


# In[ ]:


word = 'abracadabra'
letters = set(word)
print (letters)


# Sets support different operations than what we've seen so far. The full list of operations is listed [here][sets operations], but we will discuss the main ones.
# 
# [sets operations]:https://docs.python.org/2/library/stdtypes.html#set "Python documentation for set methods"

# ## Common operations

# #### _add(x)_ and _remove(x)_

# The method _add(x)_ adds the element _x_ to the calling set, ignoring the call if _x_ is already in the set.

# In[ ]:


cities.add('Eilat')
print (cities)


# In[ ]:


cities.add('Jerusalem')
print (cities)


# The method _remove(x)_ deletes the element from the calling set, raising an error if _x_ is not in the set.

# In[ ]:


cities.remove('Eilat')
print (cities)


# In[ ]:


# cities.remove('Eilat')


# #### The function _len()_

# The function _len()_ returns the number of items in the set.

# In[ ]:


print (len(cities))


# #### The operator _in_

# The operator _in_ returns _True_ if the element is in the set.

# In[ ]:


print ('Tel Aviv' in cities)
print ('Tel-Aviv' in cities)


# ## Special operations

# Sets support several unique operations, which are very useful. They are described below and summarized in the image.
# 
# 
# <center><img src=https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Set_Theory_Operations.svg/1024px-Set_Theory_Operations.svg.png alt="symmetric_difference" width=350>

# ### Inclusion

# We say that a set _A_ is _included_ in a set _B_, or alternatively that _A_ is a subset of _B_ (marked mathematically as $A \subseteq B$) if all the elements of _A_ are also elements of _B_. This is illustrated below (this kind of visualization is called Venn diagram). The Python implementation of this test is with the same old intuitive less-than ($\lt$) or less-or-equal-than ($\le$).

# In[ ]:


letters1 = set('pasta')
letters2 = set('tractor')
letters3 = set('catastrophe')


# In[ ]:


print (letters1)
print (letters2)
print (letters1 < letters2)


# In[ ]:


print (letters1)
print (letters3)
print (letters1 < letters3)


# In[ ]:


print (letters2)
print (letters3)
print (letters2 < letters3)


# ### Union

# The union of _A_ and _B_, the equivalent of the Boolean "or", and mathematically signed as $A \cup B$, is a new set that contains all the elements of _A_ and _B_, removing duplicates of course. In Python it is implemented with a pipeline ('|').

# In[ ]:


print (letters1)
print (letters2)
print (letters1 | letters2)


# In[ ]:


(letters1 | letters2) < letters3


# ### Intersection

# The intersection of _A_ and _B_, the equivalent of the Boolean "and", and mathematically signed as $A \cap B$, is a new set that contains only the elements that are common to _A_ and _B_. In Python it is implemented with an ampersand ('&').

# In[ ]:


print (letters1)
print (letters2)
print (letters1 & letters2)


# ### Subtraction

# The subtraction of _B_ from _A_ (mathematically signed as $A \setminus B$) is a new set that contains only the elements of _A_ that are **not** in _B_. This is also called sometimes the "difference" between _A_ and _B_, but this terminology is confusing because of the symmetry. In Python it is implemented with the standard minus sign.

# In[ ]:


print (letters1)
print (letters2)
print (letters2 - letters1)
print (letters1 - letters2)


# ### Symmetric difference

# The symmetric difference of _A_ and _B_, the equivalent of the Boolean "exclusive or" (xor), and mathematically signed as $A \oplus B$), is a new set that contains only the elements of _A_ that are not in _B_ **and** the elements of _B_ that are not in _A_. In Python it is implemented with a caret (' ^ ').
# 

# In[ ]:


print (letters1)
print (letters2)
print (letters1 ^ letters2)


# ## Exercises

# ### Exercise 1

# Create two strings and write a code that prints the number of their common letters (excluding duplicates).
# 
# > For example the result for 'abracadabra' and 'barbarian' is 3 ('a', 'b' & 'r').

# #### Solution

# In[ ]:


word1 = 'abracadabra'
word2 = 'barbarian'
print (len(set(word1) & set(word2)))


# ### Exercise 2

# You are given three lists, recording the visitors of the museum on Sunday, Monday and Tuesday. Note that a visitor might appear more than once even on thhe same day. Answer the following questions:
# 
# 1. Create sets for the unique visitors for each day and for the entire three days (4 sets in total).
# 2. Is there a day, that every visitor of that day, had also visited on another day?
# 3. Which visitors visited the museum on more than a single day? Which visitors visited every day??
# 4. Which visitors visited the museum **only** on Tuesday?
# 5. Which visitors visited **exactly** on one of the days Sunday and Monday?

# In[ ]:


sunday_visitors = ['abe', 'bob', 'carl', 'dave', 'ed',
                   'heinrich', 'isabel', 'abe', 'fred']
monday_visitors = ['abe', 'gale', 'ed', 'fred']
tuesday_visitors = ['ed', 'bob', 'jack', 'fred', 'abe',
                    'abe', 'jack', 'kent', 'gale']


# #### Solution

# In[ ]:


sunday_unique_visitors = set(sunday_visitors)
monday_unique_visitors = set(monday_visitors)
tuesday_unique_visitors = set(tuesday_visitors)
unique_visitors = sunday_unique_visitors | monday_unique_visitors | tuesday_unique_visitors


# In[ ]:


print (sunday_unique_visitors < monday_unique_visitors | tuesday_unique_visitors)
print (monday_unique_visitors < sunday_unique_visitors | tuesday_unique_visitors)
print (tuesday_unique_visitors < sunday_unique_visitors | monday_unique_visitors)


# In[ ]:


persistent_visitors = (sunday_unique_visitors & monday_unique_visitors) |                       (monday_unique_visitors & tuesday_unique_visitors) |                       (sunday_unique_visitors & tuesday_unique_visitors)


# In[ ]:


very_persistent_visitors = sunday_unique_visitors &                            monday_unique_visitors &                            tuesday_unique_visitors


# In[ ]:


only_tuesday_visitors = tuesday_unique_visitors -                         (sunday_unique_visitors | monday_unique_visitors)


# In[ ]:


single_day_visitors = sunday_unique_visitors ^ monday_unique_visitors

