'''
This example allows you to run calculations with Python syntax on Telegram.
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

@bot.message_handler(content_types=['voice'])
def handle_audio(message):
    bot.reply_to(message, "I can't hear you")


@bot.message_handler(commands=['calc'])
def calculator(message):
    bot.reply_to(message, eval(message.text[6:]))


bot.polling()