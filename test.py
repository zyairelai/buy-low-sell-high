import os
import datetime
from binance.client import Client
from apscheduler.schedulers.blocking import BlockingScheduler

def buy_low_sell_high():
    asset   = "ETH"
    base    = "USDT"
    symbol  =  asset + base
    core    =  500

    # Get environment variables
    api_key     = os.environ.get('API_KEY')
    api_secret  = os.environ.get('API_SECRET')
    client      = Client(api_key, api_secret)

    price_response = client.get_symbol_ticker(symbol=symbol)
    price = float(list(list(price_response.items())[1])[1])

    balance_response = client.get_asset_balance(asset=asset)
    balance = float(list(list(balance_response.items())[1])[1])

    current_core    = round((balance * price), 4)
    change_percent  = round((((float(current_core)-core)/core)*100), 4)
    trade_amount    = round((abs(core - current_core) / price), 4)
    
    print(price_response)
    print("Created at           : " + str(datetime.datetime.now()))
    print("Prefix Core  (" + asset + ")   : " + str(core) + " " + base)
    print("Current Core (" + asset + ")   : " + str(current_core) + " " + base)
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > core) and (abs(change_percent) > 3.5):
        print("Action               : SELL " + str(trade_amount) + " " + asset + "\n")
    elif (current_core < core) and (abs(change_percent) > 3.5):
        print("Action               : BUY " + str(trade_amount) + " " + asset + "\n")
    else:
        print("Action               : Do Nothing\n")

scheduler = BlockingScheduler()
scheduler.add_job(buy_low_sell_high, 'cron', second='0,5,10,15,20,25,30,35,40,45,50,55')
scheduler.start()