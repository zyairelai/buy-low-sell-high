# ONLY WORKS FOR BINANCE
If you are using KuCoin, there is a similar bot called "Infinity Grid" which introduced 6 months after I created this bot.  
Me stress feeling stress feeling betrayed as my open source idea being taken without credits anyway, I prefer using KuCoin now because its easier and I don't have to host my ec2 instance to host this bot on the cloud 😂  
Use my referral code for KuCoin https://www.kucoin.com/ucenter/signup?rcode=rJZ6M1C

## TABLE OF CONTENTS

1. [BUY-LOW-SELL-HIGH](#buy_low_sell_high)
2. [DISCLAIMER](#hello_disclaimer)
3. [HOW-IT-WORKS](#how_it_works)
4. [HOW-TO-USE](#how_to_use)
    1. [ENVIRONMENT SETUP](#environment_setup)
    2. [PIP3 REQUIREMENTS](#pip3_requirements)
    3. [CONFIGURATIONS](#configurations)
    4. [RUN](#run)
5. [SCREENSHOTS](#hello_screenshots)
    - [SAMPLE-OUTPUT](#sample_output)
    - [PROFIT-AND-LOSS](#profit_and_loss)

<a name="buy_low_sell_high"></a>
## BUY-LOW-SELL-HIGH
This is a trading bot that trades on Binance SPOT WALLET

A Trading Bot that perfectly illustrate the art of "**buy low, sell high**" strategy.

Inspired by [THE 3 % SIGNAL STRATEGY](https://medium.com/@Grandecoffee/how-to-never-lose-money-in-the-stock-market-again-2a1f48c86c45)  

It is always a good idea if you know [HOW THIS STRATEGY WORKS](https://louiszhenyean.medium.com/buy-low-sell-high-a-practical-way-205661d30632) before you use this script.

**This bot is stable therefore no new changes is made until new bugs been spotted.**  
**I use this bot personally and it works fine for me with stable profits.**  
**Maybe you might like to checkout my other bots that uses leverage:**  
- https://github.com/zyairelai/long-term-low-leverage (I am actively using this)
- https://github.com/zyairelai/futures-hero/ (I do not use this personally)

<a name="hello_disclaimer"></a>
## DISCLAIMER
I have no responsibility for any loss or hardship incurred directly or indirectly by using this code.

PLEASE MANAGE YOUR RISK LEVEL BEFORE USING MY SCRIPT.

USE IT AT YOUR OWN RISK!

<a name="how_it_works"></a>
## HOW-IT-WORKS

**NOTE** For example, for BTCUSDT, BTC is the base asset, USDT is the quote asset.

1. This script is a very simple implementation of "**buy low, sell high**" strategy.

2. Assuming you want to hold 500 USDT worth of BTC.

3. Make sure you have more than 500 USDT in your `SPOT WALLET`, ideally at least 20-30% more than the amount you want to hold.

4. When you run the script, the program will purchase BTC using 500 USDT from your `SPOT WALLET`.

5. If you use the default scheduler in the script, the script will execute every `00:00`, `06:00`, `12:00` and `18:00`.

6. For every 6 hours, if your BTC amount, the $500 is increased more than the `margin_percentage`, which by default is 4%, it will trigger a sell order. 

7. The sell amount will be the amount on top of the value 500. Which will bring your BTC balance back to 500 USDT. **(Sell the profit into the pump)**

8. Vice versa, if your BTC amount, the $500 is decresed more than the `margin_percentage`, which by default is 4%, it will trigger a buy order.

9. The buy amount will be the amount to top up your BTC balance back to 500 USDT. **(Buy the dip with proper wallet management)**

10. Always make sure you have enough ammo quote asset to allow this script to buy low and sell high at its full potential. 

11. My recommendation for the `base : quote` ratio is `80 : 20`, 80% for your overall base assets, 20% is the ammo quote asset.

<a name="how_to_use"></a>
## HOW-TO-USE
<a name="environment_setup"></a>
### 1. ENVIRONMENT SETUP
Setup your environment API key on the Terminal:
```
export BINANCE_KEY="your_binance_api_key"
export BINANCE_SECRET="your_binance_secret_key"
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
| `base`              | You can put your coin list here                                                                            |
| `core`              | Amount of the quote asset you want to maintain                                                             |
| `quote`             | Optimal is `USDT`                                                                                          |
| `margin_percentage` | The percentage that will trigger buy or sell. <br /> Optimal is 4 , minimum should not be lower than 3.5   |

The following code means the program will help you to maintain:  
- 500 USDT worth of BTC
- 300 USDT worth of ETH
```
base = ["BTC", "ETH"]
core = [500, 300]
quote = ["USDT]
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

### Screenshot PnL on 31st May 2021
<p align="center">
  <img src="screenshots/May 2021.png">
</p>

### Screenshot PnL on 30th June 2021
<p align="center">
  <img src="screenshots/June 2021.png">
</p>
