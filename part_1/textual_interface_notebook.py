#!/usr/bin/env python
# coding: utf-8

# The textual interface with the user is done through the **console**, and we already met the `print()` function for printing data to the console. In this chapter we will learn about receiving input with the `input()` function and formatting output with the `format()` string method (or the equivalent f-string).

# # The `input()` function

# The function `input([prompt])` allows the user to type data in the console, so that the program reads it. This is executed in three steps:
# 
# * The string `prompt` is presented to the user
# * The program waits until the Enter key is pressed
# * The user's input is returned by the function **as a string**

# In[ ]:


name = input("Please enter your name:\n")
print("Hi,", name)


# In[ ]:


answer = input("Would you like to continue? (Y\\N)\n")
print("Your answer was", answer)


# In[ ]:


age = input("What is your age?\n")
if age.isnumeric():
    print("You are", int(age), "years old.")
else:
    print("No jokes please")


# > **Your turn:** Write a script that asks the user for two numbers and prints their sum.

# ### Grand example (The Hangman Game)

# Implement the game [Hangman][1], where the computer simulates the side chosing the word. Ignore the drawing as well as the limit of guesses.
# 
# [1]: https://en.wikipedia.org/wiki/Hangman_(game) "Hangman"

# In[ ]:


word = 'abracadabra'
length = len(word)

print ("I've chosen a word of", length, "letters.")
ans = input("Do you want to guess it? (Y \ N)\n")

# Make sure you understand the user's answer
while ans not in ['Y', 'N', 'y', 'n']:
    ans = input("Please choose Y or N.\n")

if ans in ['Y', 'y']:
    print ("Great!")

    # Initializing
    checked = []  # letters the user already tried to guess
    revealed = '*' * length

    # Game iterations
    while revealed != word:
        # Contact the user
        print ("Until now you have " + revealed + ".")
        letter = input("What is your next guess?\n")

        # Check and update history
        if letter in checked:
            print ("You've already tried this one. Try again.")
            continue
        else:
            checked.append(letter)

        # Update revealed status
        if letter in word:
            new_revealed = ''
            for i in range(length):
                if revealed[i] != '*' or word[i] == letter:
                    new_revealed += word[i]
                else:
                    new_revealed += '*'
            revealed = new_revealed
            print ("Nice guess!")
        else:
            print ("Sorry... This letter is not part of my word.")

    print ("Excellent! You have guessed my word :-)")
    print (word.upper())
else:
    print ("Too bad. My word was " + word + ". Bye!")


# # String formatting - *format()*

# _format()_ is a **string method** that makes is easy to edit text with the help of "replacement fields" surrounded by curly braces. Let's see a simple example that demonstrates the use of _format()_ and then discuss some details.

# In[ ]:


num1, num2 = 1.23456, 2.34567
prod = num1 * num2


# Without any formatting we can't control spacing and numeric formats, so we have:

# In[ ]:


print (num1, '*', num2, '=', prod)


# One advantage of _format()_ is the intuitive insertion of variables within the sentence.

# In[ ]:


print ("{}*{}={}\n".format(num1, num2, prod))
print ("{} * {} = {}\n".format(num1, num2, prod))
print ("{}\t*\n{}\t=\n{}".format(num1, num2, prod))


# Another advantage of _format()_ is the accuracy of float numbers.

# In[ ]:


print ("{} * {} = {:.3f}".format(num1, num2, prod))
print ("{:.3f} * {:.3f} = {:2.4f}".format(num1, num2, prod))


# ### Example

# Create a dictionary with elements of the form {_name: (birth, death)_} (_death_ is _None_ if the the dude is alive), and for each element in the dictionary write the sentence "_name_ was born on _birth_ and died on _death_" (or "is still alive"). 

# In[ ]:


band = {'John': (1940, 1980),
        'Paul': (1942, None),
        'George': (1943, 2001),
        'Ringo': (1940, None)}


# In[ ]:


for player, (birth, death) in band.items():
    if death:
        print ("{} was born on {} and died on {}."            .format(player, birth, death))
    else:
        print ("{} was born on {} and he is still alive."            .format(player, birth))


# > **Your turn:** Ask the user to enter two words, find the number of common letters between the words (excluding repetitions), and print the sentence "The words _word1_ and _word2_ have \_\_\_ common letters".

# ## String formatting - f-string

# new string format in python 3.6.<br>
# we put the variable name inside the curly brackets. <br>
# 
# `f'new string formating {variable}'`
# 
# * examples and perfomance comperison is taken from [here][1]
# 
# 
# * you can read on old format strings and comperison to the new ones [here][2]
# 
# 
# [1]: https://cito.github.io/blog/f-strings/
# [2]: https://realpython.com/python-f-strings/

# 
# syntax: f ' <text> { <expression> <optional : format specifier> } <text>

# In[ ]:


name = 'Fred'
age = 42


# In[ ]:


print ('He said his name is {name} and he is {age} years old.'.format(name=name, age=age))


# In[ ]:


print(f'He said his name is {name} and he is {age} years old.')


# ### Formatting specifications

# The _format()_ method has a wide range details and use-cases (all documented [here][format documentation]), but we will focus our attention on a single aspect called "format specifications". Format specifications are used within replacement fields contained within a format string to define how individual values are presented. The full description of optional specifications are documented under the section [Format Specification Mini-Language][specification documentation] of the string methods documentation, but its main features are listed and demonstrated below.
# 
# The specifications are always preceded by a colon (:), and their general form is **\[\[fill\]align\]\[sign\]\[#\]\[0\]\[width\]\[,\]\[.precision\]\[type\]**. Adhering to this general form guarantees consistency and no ambiguity. This is a short explanation of the most useful parts:
# 
# * _align_ - left (<), right (\>) or center (^) alignment of the text
# * _width_ - decimal integer defining the minimum field width. If not specified, then the field width will be determined by the content.
# * _precision_ - decimal number indicating how many digits should be displayed after the decimal point.
# * _type_ - determines how the data should be presented
#     * _'s'_ - (default) string
#     * _'f', 'b', 'd', 'o', 'x'_ - float, binary, decimal, octal or hexagonal numeric representation
#     * _'e'_ - exponential form
#     * _'%'_ - percentage
# 
# 
# [format documentation]: https://docs.python.org/3/library/string.html#format-string-syntax "format() Python documentation"
# [specification documentation]: https://docs.python.org/3/library/string.html#format-specification-mini-language "Format Specification Mini-Language"

# ### Example 1

# Print the multiplication table.

# #### Without formatting

# In[ ]:


n = 10
for i in range(1, n+1):
    row = ""
    for j in range(1, 11):
        row = row + " " + str(i*j)
    print (row)


# #### With formatting

# In[ ]:


n = 10
for i in range(1, n+1):
    row = ''
    for j in range(1, n+1):
        row = row + f'{i*j:>4}'
    print (row)


# ## Example 2

# You have a dictionary of names and phone numbers, and you want to print its content as rows of the form `key: value`, where the `:` sign is aligned by the longest name.

# In[ ]:


d = {'Short N. ame': '555-1234', 'Longe R. Name': '555-2345', 'Longes T. N. Ame': '555-3456'}


# ### Solution

# In[ ]:


l = max(map(len, d))
print('\n'.join([f'{k:{l}}:{d[k]}' for k in d]))


# Given a dictionary, print out its content in the form

# > **Your turn:** Put the code of the previous exercise in a loop **without printouts**, and repeatedly ask the user for pairs of words until the user chooses words with no common letters. Only when this occurs, the entire “history” of the interaction should be printed, and in an organized fashion, such that the words themselves are centrally aligned.

# # Exercises

# ## Exercise 1

# In this exercise, we will implement a [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) competition.
# * Part I – Reception
#     * Ask each of the two players to print his name
# * Part II – A single round
#     * Ask one of the players (use his name) to enter his choice. Make sure it is a legitimate choice (Rock, Paper or Scissors). Then, ask the second player for his choice. Then print the winner’s name.
# * Part III – Full competition
#     * Implement a loop that asks the players whether they would like to have another round, and if so (a single “agreed” answer is enough) a new round is initiated. Make sure you record the results in order to satisfy the next part of the exercise.
# * Part IV – Results
#     * At the end of the competition (when the players have answered they ae not interested in another round), print out an informative and clear report of the results.

# ### Solution

# #### Part I

# In[ ]:


name1 = input("Player 1, please enter your name.\n")
name2 = input("Player 2, please enter your name.\n")


# #### Part II

# Player #1 choses a weapon

# In[ ]:


weapon1 = 'X'
while weapon1.upper() not in 'RPS':
    weapon1 = input(f'{name1}, please enter your weapon... (R / P / S)\n')
    if weapon1.upper() in 'RPS':
        break
    else:
        print("This is not a legitimate weapon...")


# Player #2 choses a weapon

# In[ ]:


weapon2 = 'X'
while weapon2.upper() not in 'RPS':
    weapon2 = input(f"{name2}, please enter your weapon... (R / P / S)\n")
    if weapon2.upper() in 'RPS':
        break
    else:
        print("This is not a legitimate weapon...")


# The result is evaluated.

# In[ ]:


if weapon1 == weapon2:
    print("It's a tie. No one wins this round.")
elif (weapon1 == 'R' and weapon2 == 'S') or (weapon1 == 'S' and weapon2 == 'P') or (weapon1 == 'P' and weapon2 == 'R'):
    print(name1, "wins this round.")
else:
    print(name2, "wins this round.")


# #### Part III

# In[ ]:


records = {}

want_again = True
i_round = 0
while want_again:
    i_round = i_round + 1

    ### Choosing weapons ###

    weapon1 = 'X'
    while weapon1.upper() not in 'RPS':
        weapon1 = input(f'{name1}, please enter your weapon... (R / P / S)\n').upper()
        if weapon1 in 'RPS':
            break
        else:
            print("This is not a legitimate weapon...")

    weapon2 = 'X'
    while weapon2.upper() not in 'RPS':
        weapon2 = input(f"{name2}, please enter your weapon... (R / P / S)\n").upper()
        if weapon2 in 'RPS':
            break
        else:
            print("This is not a legitimate weapon...")

    ### Results ###

    if weapon1 == weapon2:
        print("It's a tie. No one wins this round.")
        res = 'No one'
    elif (weapon1 == 'R' and weapon2 == 'S') or (weapon1 == 'S' and weapon2 == 'P') or (weapon1 == 'P' and weapon2 == 'R'):
        print(name1, "wins this round.")
        res = name1
    else:
        print(name2, "wins this round.")
        res = name2

    ### Records ###

    records[i_round] = [res, weapon1, weapon2]

    ### Continue? ###

    want_again = input("\nDo you want to play again? (Y / N)\n").upper() == 'Y'


# #### Part IV

# In[ ]:


num_of_rounds = len(records)
winners = [x[0] for x in records.values()]
name1_weapons = [x[1] for x in records.values()]
name2_weapons = [x[2] for x in records.values()]

if winners.count(name1) > winners.count(name2):
    winner = name1
elif winners.count(name1) < winners.count(name2):
    winner = name2
else:
    winner = 'No one'

print(f"The winner is {winner.upper()} !!!")
print(f"All in all there were {num_of_rounds} rounds.")
print(f"{name1} won {winners.count(name1)} rounds,     and {name2} won {winners.count(name2)} rounds.")

for round, details in records.items():
    print(f"Round {round:^3}: {details[0]:^10} won\t-\t{name1} had {details[1]}     and {name2} had {details[2]}.")

weapons_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
for initial, full in weapons_dict.items():
    print(f"The weapon {full:^10} was used {name1_weapons.count(initial):^3} times by {name1:^10}     and {name2_weapons.count(initial):^3} times by {name2:^10}")

