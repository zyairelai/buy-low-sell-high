try:
    import os
    import config
    import socket
    import requests
    import urllib3
    from datetime import datetime
    from termcolor import colored
    from binance.client import Client
    from binance.exceptions import BinanceAPIException
    from apscheduler.schedulers.blocking import BlockingScheduler

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

        if (current_core > config.core) and (abs(change_percent) > config.margin_percentage):
            if config.live_trade: client.order_market_sell(symbol=config.pair, quoteOrderQty=trade_amount)
            print(colored(asset_info, "green"))
            print(colored("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")), "green"))
            print(colored("Prefix Core          : " + str(config.core) + " " + config.base, "green"))
            print(colored("Current Core         : " + str(current_core) + " " + config.base, "green"))
            print(colored("Percentage Changed   : " + str(change_percent) + " %", "green"))
            print(colored("Action               : SELL " + str(trade_amount) + " " + config.base + "\n", "green"))
        
        elif (current_core < config.core) and (abs(change_percent) > config.margin_percentage):
            if config.live_trade: client.order_market_buy(symbol=config.pair, quoteOrderQty=trade_amount)
            print(colored(asset_info, "red"))
            print(colored("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")), "red"))
            print(colored("Prefix Core          : " + str(config.core) + " " + config.base, "red"))
            print(colored("Current Core         : " + str(current_core) + " " + config.base, "red"))
            print(colored("Percentage Changed   : " + str(change_percent) + " %", "red"))
            print(colored("Action               : BUY " + str(trade_amount) + " " + config.base + "\n", "red"))
        
        else:
            print(asset_info)
            print("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")))
            print("Prefix Core          : " + str(config.core) + " " + config.base)
            print("Current Core         : " + str(current_core) + " " + config.base)
            print("Percentage Changed   : " + str(change_percent) + " %")
            print("Action               : Do Nothing\n")

    try:
        scheduler = BlockingScheduler()
        scheduler.add_job(buy_low_sell_high, 'cron', minute='0, 30')
        scheduler.start()

    except (BinanceAPIException,
            ConnectionResetError,
            socket.timeout,
            urllib3.exceptions.ProtocolError,
            urllib3.exceptions.ReadTimeoutError,
            requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout) as e:

        if not os.path.exists("Error_Message"): os.makedirs("Error_Message")
        with open((os.path.join("Error_Message", config.pair + ".txt")), "a") as error_message:
            error_message.write("[!] " + config.pair + " - " + "Created at : " + datetime.today().strftime("%d-%m-%Y @ %H:%M:%S") + "\n")
            error_message.write(str(e) + "\n\n")

except KeyboardInterrupt: print("\n\nAborted.\n")
