import os
import datetime
from binance.client import Client
from apscheduler.schedulers.blocking import BlockingScheduler

def buy_low_sell_high():
    asset   = "BTC"
    base    = "USDT"
    symbol  =  asset + base
    core    =  1000

    # Get environment variables
    api_key     = os.environ.get('API_KEY')
    api_secret  = os.environ.get('API_SECRET')
    client      = Client(api_key, api_secret)

    # transactions_history = "transactions-history"
    # if not os.path.exists(transactions_history):
    #     os.makedirs(transactions_history)

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

    if (current_core > core) and (abs(change_percent) >= 3.5):
        client.order_market_sell(symbol=symbol, quantity=trade_amount)
        print("Action               : SELL " + str(trade_amount) + " " + asset + "\n")
        # with open(os.path.join(transactions_history, asset + "-logs.txt"), "a") as trade_logs:
        #     trade_logs.write(str(price_response) + "\n")
        #     trade_logs.write("Created at            : " + str(datetime.datetime.now()) + "\n")
        #     trade_logs.write("Prefix Core  (" + asset + ")    : " + str(core) + " " + base + " \n")
        #     trade_logs.write("Current Core (" + asset + ")    : " + str(current_core) + " " + base + " \n")
        #     trade_logs.write("Percentage Changed    : " + str(change_percent) + " " + base + " \n")
        #     trade_logs.write("Action                : SELL " + str(trade_amount) + " " + asset + "\n\n")
    elif (current_core < core) and (abs(change_percent) >= 3.5):
        client.order_market_buy(symbol=symbol, quantity=trade_amount)
        print("Action               : BUY " + str(trade_amount) + " ETH\n")
        # with open(os.path.join(transactions_history, asset + "-logs.txt"), "a") as trade_logs:
        #     trade_logs.write(str(price_response) + "\n")
        #     trade_logs.write("Created at            : " + str(datetime.datetime.now()) + "\n")
        #     trade_logs.write("Prefix Core  (" + asset + ")    : " + str(core) + " " + base + " \n")
        #     trade_logs.write("Current Core (" + asset + ")    : " + str(current_core) + " " + base + " \n")
        #     trade_logs.write("Percentage Changed    : " + str(change_percent) + " %\n")
        #     trade_logs.write("Action                : BUY " + str(trade_amount) + " " + asset + "\n\n")
    else:
        print("Action               : Do Nothing\n")
    
# Run every 30 minutes 
scheduler = BlockingScheduler()
scheduler.add_job(buy_low_sell_high, 'cron', minute='0, 30')
scheduler.start()