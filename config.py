from termcolor import colored

print("Which currency do you want to stack up?")
print("1. BNB 🔥")
print("2. BTC 💰")
print("3. ETH 💰")
print("4. USD 💵")
based_input = input("Choose your currency : ") or '1'

if (based_input == '2'):
    base = "BTC"
    print(colored(base + " is the quote asset", "green"))
    import quote_BTC
    asset               = quote_BTC.asset
    round_off           = quote_BTC.round_off
    recommended_core    = quote_BTC.recommended_core
    recommended_margin  = quote_BTC.recommended_margin

elif (based_input == '3'):
    base = "ETH"
    print(colored(base + " is the quote asset", "green"))
    import quote_ETH
    asset               = quote_ETH.asset
    round_off           = quote_ETH.round_off
    recommended_core    = quote_ETH.recommended_core
    recommended_margin  = quote_ETH.recommended_margin

elif (based_input == '4'):
    base = "USDT"
    print(colored(base + " is the quote asset", "green"))
    import quote_USDT
    asset               = quote_USDT.asset
    round_off           = quote_USDT.round_off
    recommended_core    = quote_USDT.recommended_core
    recommended_margin  = quote_USDT.recommended_margin

else:
    base = "BNB"
    print(colored(base + " is the quote asset", "green"))
    import quote_BNB
    asset               = quote_BNB.asset
    round_off           = quote_BNB.round_off
    recommended_core    = quote_BNB.recommended_core
    recommended_margin  = quote_BNB.recommended_margin

core_input       = input("Set " + base + " Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ").upper() or recommended_core
margin_input     = input("Set Margin Percentage (Default " + str(recommended_margin) + "%) : ") or recommended_margin
real_trade_input = input("Enable Live Trade? [Y/n] ") or 'n'

if real_trade_input == 'Y':
    live_trade = True
    print(colored("Live Trade Enabled", "green"))
else:
    live_trade = False
    print(colored("Live Trade NOT Enabled", "red"))

core = float(core_input)
margin_percentage = float(margin_input)

pair = asset + base
print("Pair   :   " + asset + "-" + base)
print("Core   :   " + str(core) + " " + base)
print("Margin :   " + str(margin_input) + " %\n")
