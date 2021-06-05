'''
This bot gets  𝑓(𝑥)  and returns its graph in the range (-3, 3).
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
chat_id = 865138792

bot = telebot.TeleBot(test1_token)


@bot.message_handler(commands=['plot'])
def handle_function(message):
    x = pd.Series(np.linspace(-3, 3, 100))
    plt.figure()
    funcs = message.text[6:].split()
    for f in funcs:
        plt.plot(x, eval(f))
    plt.savefig(fname='ppp.png')

    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('ppp.png', 'rb')
    bot.send_photo(chat_id, img)
    img.close()


bot.polling()