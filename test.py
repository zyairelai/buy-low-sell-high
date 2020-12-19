import os
import time
import datetime
from binance.client import Client

symbol  = "ETHUSDT"
core    =  500

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

while True:
    price_response = client.get_symbol_ticker(symbol=symbol)
    price = float(list(list(price_response.items())[1])[1])

    balance_response = client.get_asset_balance(asset='ETH')
    balance = float(list(list(balance_response.items())[1])[1])

    current_core    = round((balance * price), 4)
    change_percent  = round((((float(current_core)-core)/core)*100), 4)
    trade_amount    = round((abs(core - current_core) / price), 4)
    
    print(price_response)
    print("Prefix Core          : " + str(core) + " USDT")
    print("Current Core         : " + str(current_core) + " USDT")
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > core) and (abs(change_percent) > 3.5):
        print("Action               : SELL " + str(trade_amount) + "\n")
        with open("logs.txt", "a") as trade_logs:
            trade_logs.write(str(price_response) + "\n")
            trade_logs.write("Created at            : " + str(datetime.datetime.now()) + "\n")
            trade_logs.write("Prefix Core           : " + str(core) + " USDT\n")
            trade_logs.write("Current Core          : " + str(current_core) + " USDT\n")
            trade_logs.write("Percentage Changed    : " + str(change_percent) + " %\n")
            trade_logs.write("Action                : SELL " + str(trade_amount) + "\n\n")
    elif (current_core < core) and (abs(change_percent) > 3.5):
        print("Action               : BUY " + str(trade_amount) + "\n")
        with open("logs.txt", "a") as trade_logs:
            trade_logs.write(str(price_response) + "\n")
            trade_logs.write("Created at            : " + str(datetime.datetime.now()) + "\n")
            trade_logs.write("Prefix Core           : " + str(core) + " USDT\n")
            trade_logs.write("Current Core          : " + str(current_core) + " USDT\n")
            trade_logs.write("Percentage Changed    : " + str(change_percent) + " %\n")
            trade_logs.write("Action                : BUY " + str(trade_amount) + "\n\n")
    else:
        print("Action               : Do Nothing\n")

    time.sleep(3)