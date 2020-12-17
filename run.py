import keys
import sys
import time
from binance.client import Client

# start = time.time()
# print(f"{time.time() - start} seconds\n")

client = Client(keys.api_key, keys.api_secret)
symbol = "ETHUSDT"
core   = 500

# Get Average Price Per 5 minute
avg_price = client.get_avg_price(symbol=symbol)
current = avg_price

# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol      = 'ETHUSDT',
    side        = 'BUY',
    type        = 'MARKET',
    quantity    =  100)
