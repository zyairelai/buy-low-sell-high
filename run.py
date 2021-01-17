import os
import config
import datetime
from binance.client import Client
from apscheduler.schedulers.blocking import BlockingScheduler

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
    print("Created at           : " + str(datetime.datetime.now()))
    print("Prefix Core  (" + config.asset + ")   : " + str(config.core) + " " + config.base)
    print("Current Core (" + config.asset + ")   : " + str(current_core) + " " + config.base)
    print("Percentage Changed   : " + str(change_percent) + " %")

    if (current_core > config.core) and (abs(change_percent) >= 3.5):
        if config.live_trade: client.order_market_sell(symbol=config.pair, quantity=trade_amount)
        print("Action               : SELL " + str(trade_amount) + " " + config.asset + "\n")

    elif (current_core < config.core) and (abs(change_percent) >= 3.5):
        if config.live_trade: client.order_market_buy(symbol=config.pair, quantity=trade_amount)
        print("Action               : BUY " + str(trade_amount) + " ETH\n")

    else: print("Action               : Do Nothing\n")

# Run every 30 minutes
scheduler = BlockingScheduler()
scheduler.add_job(buy_low_sell_high, 'cron', minute='0, 30')
scheduler.start()
