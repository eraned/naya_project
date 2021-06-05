'''
create hangman game
'''

import telebot
from telebot import types
import time
import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Get Token from bot Father
test1_token = '1594806170:AAEyMsEgCJjE2BenxGzO_7Viuh44w81VMrQ'
# chat_id = 865138792

bot = telebot.TeleBot(test1_token)

word = 'abracadabra'
length = len(word)
global revealed
revealed = '*' * length

checked = []  # letters the user already tried to guess


@bot.message_handler(commands=['start'])
def greetings(message):
    global revealed
    word = "abracadabra"
    length = len(word)
    revealed = '*' * length
    bot.send_message(message.chat.id, "I've chosen a word for you :-)\nLet's go!")


@bot.message_handler(commands=['guess'])
def turn(message):
    global revealed
    letter = message.text[-1]
    if letter in checked:
        bot.send_message(message.chat.id, "You've already tried this one. Try again.")
    else:
        checked.append(letter)
        if letter in word:
            new_revealed = ''
            for i in range(length):
                if revealed[i] != '*' or word[i] == letter:
                    new_revealed += word[i]
                else:
                    new_revealed += '*'
            revealed = new_revealed
            if revealed == word:
                bot.send_message(message.chat.id, f'You got it :-)\n{revealed.upper()}')
            else:
                bot.send_message(message.chat.id, f'Nice guess!\n{revealed}')
        else:
            bot.send_message(message.chat.id, "Sorry... This letter is not part of my word.")


@bot.message_handler(commands=['hint'])
def hint(message):
    global revealed
    suggestion = list(set(word) - set(revealed))[0]
    bot.send_message(message.chat.id, f"Don't worry, Be happy!\nTry {suggestion}...")


bot.polling()