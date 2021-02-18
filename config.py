from termcolor import colored

print("Which currency do you want to stack up?")
print("1. BTC 💰")
print("2. USD 💵")
# print("3. BNB ")
# print("4. ETH ")

based_input = input("Choose your currency : ").upper()

if (based_input == '1'):
    base = "BTC"
    round_off = 6
    recommended_core = 0.005
    recommended_margin = 5

    print("Here are the supported Pairs : ")
    print("1. ETH 🔥")
    print("2. BNB")
    print("3. DOGE 🚀")
    print("4. LINK")
    print("5. 1INCH 🦄")
    print("6. SUSHI 🍣")
    print("7. XRP")
    print("0. Others (Required more input)")
    asset_input = input("\nChoose your Pair : ")

    if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: ETH): ").upper()
    elif (asset_input == '1') or (asset_input == 'ETH'): asset = "ETH"
    elif (asset_input == '2') or (asset_input == 'BNB'): asset = "BNB"
    elif (asset_input == '3') or (asset_input == 'DOGE'): asset = "DOGE"
    elif (asset_input == '4') or (asset_input == 'LINK'): asset = "LINK"
    elif (asset_input == '5') or (asset_input == '1INCH'): asset = "1INCH"
    elif (asset_input == '6') or (asset_input == 'SUSHI'): asset = "SUSHI"
    elif (asset_input == '7') or (asset_input == 'XRP'): asset = "XRP"
    else: asset = "ETH"

    pair = asset + base
    core_input = input("Set BTC Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ").upper() or recommended_core

else:
    base = "USDT"
    round_off = 4

    print("Which token do you want to trade?")
    print("1. NORMAL TOKEN")
    print("2. LEVERAGE TOKEN")

    direction_input = input("Enter your number : ")
    if direction_input == '2':
        print(colored("You choose: LEVERAGE TOKEN\n", "red"))
        direction = 'UP'
        recommended_core = 200
        recommended_margin = 5
    else:
        print(colored("You choose: NORMAL TOKEN\n", "green"))
        direction = ''
        recommended_core = 300
        recommended_margin = 4

    print("Here are the supported Pairs : ")
    # AAVE, ADA, DOT, EOS, FIL, SXP, XLM, XTZ, YFI
    print("1. BTC 🔥")
    print("2. ETH 🔥")
    print("3. BNB")
    print("4. LTC")
    print("5. LINK")
    print("6. SUSHI 🍣")
    print("7. UNI 🦄")
    print("8. XRP")
    print("9. 1INCH")
    print("0. Others (Required more input)")

    asset_input = input("\nChoose your Pair (Default BTC) : ").upper()

    if asset_input == '0': asset = input("Enter your COIN NAME (Ex: BTC): ").upper()
    elif (asset_input == '2') or (asset_input == 'ETH'): asset = "ETH" + direction
    elif (asset_input == '3') or (asset_input == 'BNB'): asset = "BNB" + direction
    elif (asset_input == '4') or (asset_input == 'LTC'): asset = "LTC" + direction
    elif (asset_input == '5') or (asset_input == 'LINK'): asset = "LINK" + direction
    elif (asset_input == '6') or (asset_input == 'SUSHI'): asset = "SUSHI" + direction
    elif (asset_input == '7') or (asset_input == 'UNI'): asset = "UNI" + direction
    elif (asset_input == '8') or (asset_input == 'TRX'): asset = "XRP" + direction
    elif (asset_input == '9') or (asset_input == 'XRP'): asset = "1INCH"
    else: asset = "BTC" + direction

    pair =  asset + base
    core_input = input("Set USD Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ") or recommended_core

margin_input = input("Set Margin Percentage (Default " + str(recommended_margin) + "%) : ") or recommended_margin
real_trade_input = input("Enable Live Trade? [Y/n] ") or 'n'

if real_trade_input == 'Y':
    live_trade = True
    print(colored("Live Trade Enabled", "green"))
else:
    live_trade = False
    print(colored("Live Trade NOT Enabled", "red"))

core = float(core_input)
margin_percentage = float(margin_input)

print("Pair   :   " + asset + "-" + base)
print("Core   :   " + str(core))
print("Margin :   " + str(margin_input) + "\n")
