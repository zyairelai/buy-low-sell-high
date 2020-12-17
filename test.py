import keys
import sys
from binance.client import Client
import datetime
import time

client = Client(keys.api_key, keys.api_secret)
symbol = "ETHUSDT"
amount = "0.02"

candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_30MINUTE)
print(candles)

order = client.create_test_order(
    symbol      = 'ETHUSDT',
    side        = 'BUY',
    type        = 'MARKET',
    quantity    =  100)
