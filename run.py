#!/bin/python3

live_trade = True

# You can select the coins that you want to trade here
base = ["BTC", "ETH", "BNB", "SOL", "DOGE"]
core = [1000, 1000, 800, 500, 500]

# Optimal value, do not change these
quote = ["USDT"]
margin_percentage = 5

import os
from datetime import datetime
from binance.client import Client

# Get environment variables
api_key    = os.environ.get('BINANCE_KEY')
api_secret = os.environ.get('BINANCE_SECRET')
client     = Client(api_key, api_secret)

# Trading Setup
pair,round_off = [], []
for i in range(len(base)):
    if len(quote) > 1 : my_quote_asset = quote[i]
    else: my_quote_asset = quote[0]
    pair.append(base[i] + quote[0])

for coin in quote:
    if coin == "USDT": decimal = 2
    elif coin == "BTC": decimal = 6
    elif coin == "ETH": decimal = 5
    elif coin == "BNB": decimal = 3
    else: decimal == 4
    round_off.append(decimal)

def buy_low_sell_high():
    for i in range(len(pair)):

        # Auto Adjust FIXED or DYNAMIC variable
        if len(quote) > 1 : my_quote_asset = quote[i]
        else: my_quote_asset = quote[0]
        if len(core) > 1 : my_core_number = core[i]
        else: my_core_number = core[0]
        if len(round_off) > 1 : my_round_off = round_off[i]
        else: my_round_off = round_off[0]

        # Retrieve Current Asset INFO
        asset_info      = client.get_symbol_ticker(symbol=pair[i])
        asset_price     = float(asset_info.get("price"))
        asset_balance   = float(client.get_asset_balance(asset=base[i]).get("free"))

        # Computing for Trade Quantity
        current_holding = round(asset_balance * asset_price, my_round_off)
        change_percent  = round(((current_holding - my_core_number) / my_core_number * 100), 4)
        trade_amount    = round(abs(current_holding - my_core_number), my_round_off)

        # Output Console and Placing Order
        if (current_holding > my_core_number) and (abs(change_percent) > margin_percentage):
            if live_trade: client.order_market_sell(symbol=pair[i], quoteOrderQty=trade_amount)
            print(asset_info)
            print("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")))
            print("Prefix Core          : " + str(my_core_number) + " " + my_quote_asset)
            print("Current Core         : " + str(current_holding) + " " + my_quote_asset)
            print("Percentage Changed   : " + str(change_percent) + " %")
            print("Action               : SELL " + str(trade_amount) + " " + my_quote_asset + "\n")

        elif (current_holding < my_core_number) and (abs(change_percent) > margin_percentage):
            if live_trade: client.order_market_buy(symbol=pair[i], quoteOrderQty=trade_amount)
            print(asset_info)
            print("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")))
            print("Prefix Core          : " + str(my_core_number) + " " + my_quote_asset)
            print("Current Core         : " + str(current_holding) + " " + my_quote_asset)
            print("Percentage Changed   : " + str(change_percent) + " %")
            print("Action               : BUY " + str(trade_amount) + " " + my_quote_asset + "\n")

        else:
            print(asset_info)
            print("Created at           : " + str(datetime.today().strftime("%d-%m-%Y @ %H:%M:%S")))
            print("Prefix Core          : " + str(my_core_number) + " " + my_quote_asset)
            print("Current Core         : " + str(current_holding) + " " + my_quote_asset)
            print("Percentage Changed   : " + str(change_percent) + " %")
            print("Action               : Do Nothing\n")

buy_low_sell_high()
