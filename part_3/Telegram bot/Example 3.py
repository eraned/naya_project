'''
Send message to chat id
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

# Create bot class
bot = telebot.TeleBot(test1_token)

# using this object we can use the API more easily, e.g.:
msg = bot.send_message(chat_id=865138792, text='This is my message')

print(msg)

