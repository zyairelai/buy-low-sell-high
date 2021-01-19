recommended_margin = 3.5

while True:
    print("Which currency do you want to stack up?")
    print("1. BTC 💰")
    print("2. USD 💵")

    based_input = input("Choose your currency (Default = BTC) : ").upper() or 'BTC'
    print()

    if (based_input == '1') or (based_input == 'BTC') or (based_input == 'BITCOIN'):
        base = "BTC"
        round_off = 6
        recommended_core = 0.003

        while True:
            print("Here are the supported Pairs: ")
            print("1. DOGE-BTC 🚀")
            print("2. LINK-BTC")
            print("3. SUSHI-BTC 🍣")
            print("4. 1INCH-BTC 🦄")
            print("5. TRX-BTC")
            print("6. XRP-BTC")
            print("0. Others (Required more input)")

            asset_input = input("Choose your Pair (Default = LINK) : ") or 'LINK'

            if asset_input == '0':
                asset = input("Enter your COIN NAME: ").upper()
                recommended_core = 0.005
                break
            elif (asset_input == '1') or (asset_input == 'DOGE'):
                asset = "DOGE"
                recommended_margin = 6
                recommended_core   = 0.002
                break
            elif (asset_input == '2') or (asset_input == 'LINK'):
                asset = "LINK"
                break
            elif (asset_input == '3') or (asset_input == 'SUSHI'):
                asset = "SUSHI"
                break
            elif (asset_input == '4') or (asset_input == '1INCH'):
                asset = "1INCH"
                break
            elif (asset_input == '5') or (asset_input == 'TRX'):
                asset = "TRX"
                break
            elif (asset_input == '6') or (asset_input == 'XRP'):
                asset = "XRP"
                break
            else: print("❗Invalid Number❗Try again❗\n")

        pair = asset + base
        core_input = input("\nSet your Core for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ").upper() or recommended_core
        break

    elif (based_input == '2') or (based_input == 'USDT') or (based_input == 'USD'):
        base = "USDT"
        round_off = 4
        recommended_core = 300

        while True:
            print("Here are the supported Pairs: ")
            print("1. BTC-USDT")
            print("2. ETH-USDT 🔥")
            print("3. BNB-USDT")
            print("4. LINK-USDT")
            print("5. SUSHI-USDT 🍣")
            print("6. 1INCH-USDT 🦄")
            print("7. UNI-USDT")
            print("8. TRX-USDT")
            print("9. XRP-USDT")
            print("0. Others (Required more input)")

            asset_input = input("Choose your Pair (Default = ETH) : ").upper() or 'ETH'
            
            if asset_input == '0':
                asset = input("Enter your COIN NAME: ").upper()
                break
            elif (asset_input == '1') or (asset_input == 'BTC'):
                asset = "BTC"
                break
            elif (asset_input == '2') or (asset_input == 'ETH'):
                asset = "ETH"
                break
            elif (asset_input == '3') or (asset_input == 'BNB'):
                asset = "BNB"
                break
            elif (asset_input == '4') or (asset_input == 'LINK'):
                asset = "LINK"
                break
            elif (asset_input == '5') or (asset_input == 'SUSHI'):
                asset = "SUSHI"
                break
            elif (asset_input == '6') or (asset_input == '1INCH'):
                asset = "1INCH"
                break
            elif (asset_input == '7') or (asset_input == 'UNI'):
                asset = "UNI"
                break
            elif (asset_input == '8') or (asset_input == 'TRX'):
                asset = "TRX"
                break
            elif (asset_input == '9') or (asset_input == 'XRP'):
                asset = "XRP"
                break
            else: print("❗Invalid Number❗Try again❗\n")

        pair =  asset + base
        core_input = input("\nSet your Core for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ") or recommended_core
        break

    else: print("❗Invalid Number❗Try again❗\n")

margin_input = input("Enter Margin Percentage (Recommended 3.5%) : ") or recommended_margin
real_trade_input = input("Enable Live Trade? [Y/n] ") or 'n'

if real_trade_input == 'Y': 
    live_trade = True
    print("✅ Live Trade Enabled ✅")
else: 
    live_trade = False
    print("❌ This is a Demo ❌")

core = float(core_input)
margin_percentage = float(margin_input)

print("Pair :   " + asset + "-" + base)
print("Core :   " + str(core) + "\n")
