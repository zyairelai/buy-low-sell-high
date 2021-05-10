# BUY-LOW-SELL-HIGH
Inspired by [The 3% Signal Strategy](https://medium.com/@Grandecoffee/how-to-never-lose-money-in-the-stock-market-again-2a1f48c86c45)  
You can check my daily PnL [here](https://docs.google.com/spreadsheets/d/1VsOY7B7WWT0D67ifggpbsdHrQEegl0DaXHfWhsx--tY/edit#gid=103443936)

# DISCLAIMER

This automation software is purely handcoded by [@zyairelai](https://github.com/zyairelai) from scratch with my personal manual trading strategy.  
Kindly provide feedback through my email `zyairelai@gmail.com` if you are using my repository.  
If you had modified or improved my code feel free to share with me and we may have futher discussion on this project!  
Distribution of the software is allowed. However, SELLING is NOT allowed.  
PLEASE MANAGE YOUR RISK LEVEL BEFORE USING MY SCRIPT.

## 1. Environment Setup
Paste the following into your Default Shell
```
export API_KEY="your_binance_api_key"
export API_SECRET="your_binance_secret_key"
```

Or as an alternative, you can change `line 33-35` in `run.py` to following: 
```
api_key     = "your_binance_api_key"
api_secret  = "your_binance_secret_key"
client      = Client(api_key, api_secret)
```

## 2. Pip3 Requirements
You need to have these libraries installed:
```
pip3 install apscheduler==3.6.3
pip3 install cryptography==3.2 
pip3 install python-binance==0.7.5
pip3 install termcolor==1.1.0
```

## 3. Run
Let's make the magic happens!
```
python3 run.py
```

## 4. Donate for MORE!!
If you found this useful to generate your passive income, feel free to donate to me so I can IMPROVE MORE!
```
BTC  (BTC)   : 15VowsyMp9A5DWbKbZEVt4A4r7dQQgddtn
ETH  (ERC20) : 0x7701948f0477e629c5bb5d79f99b833133ab30d5
USDT (ERC20) : 0x7701948f0477e629c5bb5d79f99b833133ab30d5
```

## 5. Screenshot Validation
Here is my ROI with this strategy

### Screenshot PnL on 28th February 2021
<p align="center">
  <img src="screenshots/Feb 2021.png">
</p>

### Screenshot PnL on 31st March 2021
<p align="center">
  <img src="screenshots/March 2021.png">
</p>

### Screenshot PnL on 30th April 2021
<p align="center">
  <img src="screenshots/April 2021.png">
</p>
