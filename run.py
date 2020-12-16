import os
import sys
import time
from binance.client import Client

# Get environment variables
api_key = os.getenv('API_KEY')
api_secret = os.environ.get('API_SECRET')
client = Client(api_key, api_secret)

# start = time.time()
# print(f"{time.time() - start} seconds\n")

# Get Average Price Per 5 minute
avg_price = client.get_avg_price(symbol='ETHUSDT')
current = avg_price



# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol      =   'ETHUSDT',
    side        =   Client.SIDE_BUY,
    type        =   Client.ORDER_TYPE_MARKET,
    quantity    =   100)
