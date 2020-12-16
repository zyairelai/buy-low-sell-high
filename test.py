import os
import sys
import time
from binance.client import Client

# Get environment variables
api_owner = os.getenv('API_OWNER')
api_key = os.getenv('API_KEY')
api_secret = os.environ.get('API_SECRET')
client = Client(api_key, api_secret)


# Test your algorithm here
print(client.get_account())
print(client.get_account().values(1))
