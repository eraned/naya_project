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

# put your chat id and send a message
bot_url = f'https://api.telegram.org/bot{test1_token}/'
chat_id = 865138792
text = 'This is my message'
url = bot_url + f'sendMessage?chat_id={chat_id}&text={text}'

# Print the get request
resp = requests.get(url)
print(resp.text)


message = json.loads(resp.text)['result']
print(message)


