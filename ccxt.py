import numpy as np
import pandas as pd
import ccxt

exchange = 'ftx'

if exchange == 'binanceUsd':
    client = ccxt.binanceusdm()
elif exchange == 'kucoin':
    client = ccxt.kucoin()
elif exchange == 'bybit':
    client = ccxt.bybit()
elif exchange == 'ftx':
    client = ccxt.ftx()

pair = 'BTC/USDT'
timeframe = '1m'

data = client.fetch_ohlcv(pair, timeframe, limit=3)

ohlcv = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
ohlcv = ohlcv.set_index('timestamp')
ohlcv.index = pd.to_datetime(ohlcv.index, unit='ms')

print(ohlcv)