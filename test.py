import os
import sys
import time
import datetime
import json
from binance.client import Client

symbol  = "ETHUSDT"
core    =  500

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

# while True:
# price_response = client.get_symbol_ticker(symbol=symbol)
# price = float(list(list(price_response.items())[1])[1]) # Get Price Value

# balance_response = client.get_asset_balance(asset='ETH')
# balance = float(list(list(balance_response.items())[1])[1])

# current_core = balance * price 
# print("Current Core: " + current_core)

# change_percent = abs(((float(current_core)-core)/core)*100)
# print("Percentage Changed: " + change_percent)

# if (current_core > core) and (change_percent > 3.5):
#     print("SELL")
# elif (current_core < core) and (change_percent > 3.5):
#     print("BUY")
# else:
#     print("Do Nothing")

# time.sleep(5)         # Every x hours * minutes * seconds -> time.sleep(4 * 60 * 60)