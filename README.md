## TABLE OF CONTENTS

1. [BUY-LOW-SELL-HIGH](#buy_low_sell_high)
2. [DISCLAIMER](#hello_disclaimer)
3. [HOW-IT-WORKS](#how_it_works)
    - [](#)
4. [HOW-TO-USE](#how_to_use)
    1. [ENVIRONMENT SETUP](#environment_setup)
    2. [PIP3 REQUIREMENTS](#pip3_requirements)
    3. [CONFIGURATIONS](#configurations)
    4. [RUN](#run)
5. [SCREENSHOTS](#hello_screenshots)
    - [SAMPLE-OUTPUT](#sample_output)
    - [PROFIT-AND-LOSS](#profit_and_loss)
6. [JOIN-MY-DISCORD](#discord)
    - [QUICK ACCESS TO THE DARK DIMENSION](https://discord.gg/r4TnhcdqmT)

<a name="buy_low_sell_high"></a>
## BUY-LOW-SELL-HIGH
Inspired by [THE 3 % SIGNAL STRATEGY](https://medium.com/@Grandecoffee/how-to-never-lose-money-in-the-stock-market-again-2a1f48c86c45)  

You can check my daily PnL [HERE ON MY GOOGLE SHEET](https://docs.google.com/spreadsheets/d/1VsOY7B7WWT0D67ifggpbsdHrQEegl0DaXHfWhsx--tY/edit#gid=103443936)  

<a name="hello_disclaimer"></a>
## DISCLAIMER
I have no responsibility for any loss or hardship incurred directly or indirectly by using this code.

PLEASE MANAGE YOUR RISK LEVEL BEFORE USING MY SCRIPT.

USE IT AT YOUR OWN RISK!

<a name="how_it_works"></a>
## HOW-IT-WORKS
# WORK IN PROGRESS WORK IN PROGRESS 

<a name="how_to_use"></a>
## HOW-TO-USE
<a name="environment_setup"></a>
### 1. ENVIRONMENT SETUP
Setup your environment key on the Terminal:
```
export API_KEY="your_binance_api_key"
export API_SECRET="your_binance_secret_key"
```

Or as an alternative, you can change `line 9-11` in `run.py` to following: 
```
api_key     = "your_binance_api_key"
api_secret  = "your_binance_secret_key"
client      = Client(api_key, api_secret)
```

<a name="pip3_requirements"></a>
### 2. PIP3 REQUIREMENTS
You need to have these libraries installed:
```
pip3 install apscheduler==3.6.3
pip3 install cryptography==3.2 
pip3 install python-binance==0.7.5
pip3 install termcolor==1.1.0
```

<a name="configurations"></a>
### 3. CONFIGURATIONS
Before running, maybe you want to see how the output looks like.  
The settings can be configured in `config.py`.

| Variables           | Description                                                                                                |
| --------------------| -----------------------------------------------------------------------------------------------------------|
| `live_trade`        |`True` to place actual order <br /> `False` to see sample output                                            |
| `enable_scheduler`  |`True` to run the code at every `00:00`, `06:00`, `12:00`, `18:00` <br /> `False` to run the code only once |
| `asset`             | You can put your coin list here                                                                            |
| `core`              | The amount of the quote asset. <br />  For `BTC/USDT`, the quote asset is `USDT`                           |
| `base`              | The Quote asset. The optimal is `USDT`                                                                     |
| `margin_percentage` | The percentage that will trigger buy or sell. <br /> Optimal is 4 , minimum should not be lower than 3.5   |

The following code means the program will help you to maintain:  
- 500 USDT worth of BTC
- 300 USDT worth of ETH
```
asset = ["BTC", "ETH"]
core  = [500, 300]
base  = ["USDT]
```
**IMPORTANT NOTE:**  
- **The minimum core amount for quote USDT is 300 USDT**
- **Make sure you have enough USDT in your `SPOT WALLET` to unleash this program at its full potential**

<a name="run"></a>
### 4. RUN
If you want to time this script by your own, set `enable_scheduler = False` then you can make your own scheduler

Else, you can set `enable_scheduler = True` and the script will loop the program for you every 6 hours.

Now if you are all ready, set `live_trade = True` and ...

Let's make the magic happens!
```
python3 run.py
```

<a name="hello_screenshots"></a>
## SCREENSHOTS

<a name="sample_output"></a>
### SAMPLE OUTPUT
<p align="center">
  <img src="screenshots/sample_output.png">
</p>

<a name="profit_and_loss"></a>
### PROFIT AND LOSS

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

<a name="discord"></a>
## JOIN MY DISCORD HERE
- [QUICK ACCESS TO THE DARK DIMENSION](https://discord.gg/r4TnhcdqmT)
