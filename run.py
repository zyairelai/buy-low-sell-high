import os
import sys
import time
from binance.client import Client

symbol  = "ETHUSDT"
core    =  500

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      =  Client(api_key, api_secret)

# Get lastest price every second
while True:
    price_response = client.get_symbol_ticker(symbol=symbol)
    price = float(list(list(price_response.items())[1])[1]) # Get Price Value
    print(price_response)
    print(price)
    time.sleep(1)


# buy   = client.order_market_buy(symbol=symbol, quantity=100)
# sell  = client.order_market_sell(symbol=symbol, quantity=100)

