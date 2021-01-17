while True:
    print("Which currency do you want to stack up?")
    print("1. USDT 🔥")
    print("2. BTC")

    based_input = input("Choose your currency (Default 1) : ") or '1'
    print()

    if based_input == '1':
        base = "USDT"
        while True:
            print("Here are the supported Pairs: ")
            print("1. BTC-USDT 🔥")
            print("2. ETH-USDT 🔥")
            print("3. BNB-USDT")
            print("4. LINK-USDT")
            print("5. SUSHI-USDT")
            print("6. 1INCH-USDT")
            print("7. UNI-USDT")
            print("8. TRX-USDT")
            print("9. XRP-USDT")

            asset_input = input("Choose your Pair (Default 1) : ") or '1'
            if asset_input == '1':
                asset = "BTC"
                break
            elif asset_input == '2':
                asset = "ETH"
                break
            elif asset_input == '3':
                asset = "BNB"
                break
            elif asset_input == '4':
                asset = "LINK"
                break
            elif asset_input == '5':
                asset = "SUSHI"
                break
            elif asset_input == '6':
                asset = "1INCH"
                break
            elif asset_input == '7':
                asset = "UNI"
                break
            elif asset_input == '8':
                asset = "TRX"
                break
            elif asset_input == '9':
                asset = "XRP"
                break
            else: print("[!] Invalid Number. Try again.\n")

        pair =  asset + base
        core_input = input("\nSet your Core Number for " + asset + "-" + base + " (Default 300) : ") or 300
        break

    elif based_input == '2':
        base = "BTC"
        while True:
            print("Here are the supported Pairs: ")
            print("1. LINK-BTC")
            print("2. SUSHI-BTC")
            print("3. 1INCH-BTC")
            print("4. UNI-BTC")
            print("5. TRX-BTC")
            print("6. XRP-BTC")

            asset_input = input("Choose your Pair (Default SUSHI) : ") or '2'
            if asset_input == '1':
                asset = "LINK"
                break
            elif asset_input == '2':
                asset = "SUSHI"
                break
            elif asset_input == '3':
                asset = "1INCH"
                break
            elif asset_input == '4':
                asset = "UNI"
                break
            elif asset_input == '5':
                asset = "TRX"
                break
            elif asset_input == '6':
                asset = "XRP"
                break
            else: print("[!] Invalid Number. Try again.\n")

        pair = asset + base
        core_input = input("\nSet your Core Number for " + asset + "-" + base + " (Default 0.01) : ") or 0.01
        break

    # ADD ON GOES HERE
    else: print("[!] Invalid Number. Try again.\n")

core = float(core_input)
real_trade_input = input("Trade For Real? [Y/n] ") or 'n'
if real_trade_input == 'Y': live_trade = True
else: live_trade = False

print(" > " + str(live_trade))
print("Pair :   " + asset + "-" + base)
print("Core :   " + str(core) + "\n")
