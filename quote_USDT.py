from termcolor import colored
round_off = 2

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

print("Here are the Recommended Pairs : ")
# AAVE, ADA, DOT, EOS, FIL, SXP, XLM, XTZ, YFI
print("1. BTC 🔥")
print("2. ETH 🔥")
print("3. BNB 🔥")
# print("4. DOT ")
# print("5. LTC ")
# print("6. LINK ")
# print("7. SUSHI 🍣")
# print("8. UNI 🦄")
# print("9. XRP ")
print("0. Others (Required more input)")

asset_input = input("\nChoose your Pair (Default BTC) : ").upper()

if asset_input == '0': asset = input("Enter your COIN NAME (Ex: BTC): ").upper()
elif (asset_input == '2') : asset = "ETH"   + direction
elif (asset_input == '3') : asset = "BNB"   + direction
elif (asset_input == '4') : asset = "DOT"   + direction
elif (asset_input == '5') : asset = "LTC"   + direction
elif (asset_input == '6') : asset = "LINK"  + direction
elif (asset_input == '7') : asset = "SUSHI" + direction
elif (asset_input == '8') : asset = "UNI"   + direction
elif (asset_input == '9') : asset = "XRP"   + direction
else: asset = "BTC" + direction
print(colored("The chosen coin is " + asset + "\n", "green"))
