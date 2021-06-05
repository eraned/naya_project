'''
This example repeats the message of the user.
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

bot = telebot.TeleBot(test1_token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()