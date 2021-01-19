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
    asset_info      = client.get_symbol_ticker(symbol=config.pair)
    asset_price     = float(asset_info.get("price"))
    asset_balance   = float(client.get_asset_balance(asset=config.asset).get("free"))

    current_core    = round(asset_balance * asset_price, config.round_off)
    change_percent  = round(((current_core - config.core) / config.core * 100), 4)
    trade_amount    = round(abs(current_core - config.core), config.round_off)

    print(trade_amount)

    print(asset_info)
    print("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")))
    print("Prefix Core          : " + str(config.core) + " " + config.base)
    print("Current Core         : " + str(current_core) + " " + config.base)
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > config.core) and (abs(change_percent) > config.margin_percentage):
        if config.live_trade: client.order_market_sell(symbol=config.pair, quoteOrderQty=trade_amount)
        print("Action               : SELL " + str(trade_amount) + " " + config.base + "\n")
    
    elif (current_core < config.core) and (abs(change_percent) > config.margin_percentage):
        if config.live_trade: client.order_market_buy(symbol=config.pair, quoteOrderQty=trade_amount)
        print("Action               : BUY " + str(trade_amount) + " " + config.base + "\n")
    
    else: print("Action               : Do Nothing\n")

try:
    scheduler = BlockingScheduler()
    scheduler.add_job(buy_low_sell_high, 'cron', second='0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57')
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
