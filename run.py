import os
import sys
import time
import datetime
import json
from binance.client import Client
# buy   = client.order_market_buy(symbol=symbol, quantity=100)
# sell  = client.order_market_sell(symbol=symbol, quantity=100)

symbol  = "ETHUSDT"
core    =  500

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

while True:
    price_response = client.get_symbol_ticker(symbol=symbol)
    price = float(list(list(price_response.items())[1])[1]) # Get Price Value

    balance_response = client.get_asset_balance(asset='ETH')
    balance = float(list(list(balance_response.items())[1])[1])

    current_core = round((balance * price), 4)
    print("Current Core         : " + str(current_core) + " USDT")

    change_percent = round((((float(current_core)-core)/core)*100), 4)
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > core) and (abs(change_percent) > 3.5):
        print("Action               : SELL\n")
    elif (current_core < core) and (abs(change_percent) > 3.5):
        print("Action               : BUY\n")
    else:
        print("Action               : Do Nothing\n")

    time.sleep(5)         # Every x hours * minutes * seconds -> time.sleep(4 * 60 * 60)