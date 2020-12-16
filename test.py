import datetime
import keys
import sys
import time
from binance.client import Client

client = Client(keys.api_key, keys.api_secret)
symbol = "ETHUSDT"
amount = "0.02"

candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_30MINUTE)
print(candles)