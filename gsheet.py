import os
from datetime import datetime
from binance.client import Client
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Access Google Sheet API
SERVICE_ACCOUNT_FILE = 'gsheet-key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Define Google Sheet Info
spreadsheet_id = "1VsOY7B7WWT0D67ifggpbsdHrQEegl0DaXHfWhsx--tY"
range_name = 'buy-low-sell-high!A1:E1'
service = build('sheets', 'v4', credentials=creds)

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

def append_to_sheet():
    # Retrieve Data from Binance
    date = datetime.today().strftime("%d-%m-%Y")

    # Append to Google Sheet
    values = [[date, "BTC_Overview", "USD_Overview","SPOT_BTC", "SPOT_USD"]]
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption="USER_ENTERED", body={"values":values}).execute()

append_to_sheet()