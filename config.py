from termcolor import colored

while True:
    print("Which currency do you want to stack up?")
    print("1. BTC 💰")
    print("2. USD 💵")

    based_input = input("Choose your currency (Default BTC) : ").upper() or 'BTC'
    print()

    if (based_input == '1') or (based_input == 'BTC') or (based_input == 'BITCOIN'):
        base = "BTC"
        round_off = 6
        recommended_core = 0.005
        recommended_margin = 5

        print("Here are the supported Pairs: ")
        print("1. DOGE 🚀")
        print("2. 1INCH")
        print("0. Others (Required more input)")

        asset_input = input("Choose your Pair (Default DOGE) : ") or 'DOGE'

        if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: ETH): ").upper()
        elif (asset_input == '2') or (asset_input == '1INCH'): asset = "1INCH"
        else: asset = "DOGE"

        pair = asset + base
        core_input = input("\nSet your BTC Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ").upper() or recommended_core
        break

    elif (based_input == '2') or (based_input == 'USDT') or (based_input == 'USD'):
        base = "USDT"
        round_off = 4
        recommended_core = 200
        recommended_margin = 10

        print("You want to bet going UP or DOWN? [Up/Down] ")
        print("1. UP")
        print("2. DOWN")
        direction_input = input("Enter your number: ")
        if direction_input == '2': 
            print(colored("You choose DOWN\n", "red"))
            direction = 'DOWN'
        else:
            print(colored("You choose UP\n", "green"))
            direction = 'UP'

        print("Here are the supported Pairs: ")
        # AAVE, ADA, DOT, EOS, FIL, SXP, XLM, XTZ, YFI
        print("1. BTC 🔥")
        print("2. ETH 🔥")
        print("3. BNB")
        print("4. LTC")
        print("5. LINK")
        print("6. SUSHI 🍣")
        print("7. UNI 🦄")
        print("8. TRX")
        print("9. XRP")
        print("0. Others (Required more input)")

        asset_input = input("Choose your Pair (Default BTC) : ").upper() or 'BTC'
        
        if asset_input == '0': asset = input("Enter your COIN NAME (Ex: BTC): ").upper()

        elif (asset_input == '1') or (asset_input == 'BTC'): asset = "BTC" + direction
        elif (asset_input == '2') or (asset_input == 'ETH'): asset = "ETH" + direction
        elif (asset_input == '3') or (asset_input == 'BNB'): asset = "BNB" + direction
        elif (asset_input == '4') or (asset_input == 'LTC'): asset = "LTC" + direction
        elif (asset_input == '5') or (asset_input == 'LINK'): asset = "LINK" + direction
        elif (asset_input == '6') or (asset_input == 'SUSHI'): asset = "SUSHI" + direction
        elif (asset_input == '7') or (asset_input == 'UNI'): asset = "UNI" + direction
        elif (asset_input == '8') or (asset_input == 'TRX'): asset = "TRX" + direction
        elif (asset_input == '9') or (asset_input == 'XRP'): asset = "XRP" + direction
        else: print(colored("Invalid Number. Please try again.\n", "red")) 

        pair =  asset + base
        core_input = input("\nSet your USD Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ") or recommended_core
        break

    else: print(colored("Invalid Number. Please try again.\n", "red")) 

margin_input = input("Enter Margin Percentage (Recommended " + str(recommended_margin) + "%) : ") or recommended_margin
real_trade_input = input("Enable Live Trade? [Y/n] ") or 'n'

if real_trade_input == 'Y': 
    live_trade = True
    print(colored("Live Trade Enabled", "green"))
else: 
    live_trade = False
    print(colored("Live Trade NOT Enabled", "red"))

core = float(core_input)
margin_percentage = float(margin_input)

print("Pair :   " + asset + "-" + base)
print("Core :   " + str(core) + "\n")
