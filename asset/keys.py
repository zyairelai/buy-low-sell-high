import os
from binance.client import Client

# Binance Futures Testnet API

def get_key(): 
    return "API_KEY"

def get_secret():
    return "API_SECRET"


# Paste the following into your Default Shell
"""
export API_OWNER="your_binance_username"
export API_KEY="your_binance_api_key"
export API_SECRET="your_binance_secret_key"
"""

# Check Your Environment
# api_owner   = os.environ.get('API_OWNER')
# api_key     = os.environ.get('API_KEY')
# api_secret  = os.environ.get('API_SECRET')

# print("API OWNER        :   " + api_owner)
# print("API Key          :   " + api_key)
# print("API Secret Key   :   " + api_secret)

# client = Client(keys.api_key, keys.api_secret)

