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
print("3. BNB 🔥")
print("4. DOT ")
print("5. LTC ")
print("6. LINK ")
print("7. SUSHI 🍣")
print("8. UNI 🦄")
print("9. XRP ")
print("0. Others (Required more input)")

asset_input = input("\nChoose your Pair (Default BTC) : ").upper()

if asset_input == '0': asset = input("Enter your COIN NAME (Ex: BTC): ").upper()
elif (asset_input == '2') or (asset_input == 'ETH')  : asset = "ETH"   + direction
elif (asset_input == '3') or (asset_input == 'BNB')  : asset = "BNB"   + direction
elif (asset_input == '4') or (asset_input == 'DOT')  : asset = "DOT"   + direction
elif (asset_input == '5') or (asset_input == 'LTC')  : asset = "LTC"   + direction
elif (asset_input == '6') or (asset_input == 'LINK') : asset = "LINK"  + direction
elif (asset_input == '7') or (asset_input == 'SUSHI'): asset = "SUSHI" + direction
elif (asset_input == '8') or (asset_input == 'UNI')  : asset = "UNI"   + direction
elif (asset_input == '9') or (asset_input == 'XRP')  : asset = "XRP"   + direction
else: asset = "BTC" + direction

pair =  asset + base
core_input = input("Set USD Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ") or recommended_core