import os
import config
import socket
import requests
import urllib3
from datetime import datetime
from binance.client import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from binance.exceptions import BinanceAPIException

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

def buy_low_sell_high():
    price_response = client.get_symbol_ticker(symbol=config.pair)
    price = float(list(list(price_response.items())[1])[1])

    balance_response = client.get_asset_balance(asset=config.asset)
    balance = float(list(list(balance_response.items())[1])[1])

    current_core    = round((balance * price), 4)
    change_percent  = round((((float(current_core)-config.core)/config.core)*100), 4)
    trade_amount    = round((abs(config.core - current_core) / price), 4)

    print(price_response)
    print("Created at           : " + str(datetime.now()))
    print("Prefix Core  (" + config.asset + ")   : " + str(config.core) + " " + config.base)
    print("Current Core (" + config.asset + ")   : " + str(current_core) + " " + config.base)
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > config.core) and (abs(change_percent) > 3.5):
        print("Action               : SELL " + str(trade_amount) + " " + config.asset + "\n")
    elif (current_core < config.core) and (abs(change_percent) > 3.5):
        print("Action               : BUY " + str(trade_amount) + " " + config.asset + "\n")
    else: print("Action               : Do Nothing\n")

try:
    scheduler = BlockingScheduler()
    scheduler.add_job(buy_low_sell_high, 'cron', second='0,5,10,15,20,25,30,35,40,45,50,55')
    scheduler.start()

except (BinanceAPIException,
        ConnectionResetError,
        socket.timeout,
        urllib3.exceptions.ProtocolError,
        urllib3.exceptions.ReadTimeoutError,
        requests.exceptions.ConnectionError,
        requests.exceptions.ReadTimeout) as e:

    if not os.path.exists("Error_Message"): os.makedirs("Error_Message")
    with open((os.path.join("Error_Message", config.pair + ".txt")), "a") as error_message:
        error_message.write("[!] " + config.pair + " - " + "Created at : " + datetime.today().strftime("%d-%m-%Y @ %H:%M:%S") + "\n")
        error_message.write(str(e) + "\n\n")
