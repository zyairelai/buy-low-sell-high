round_off = 6
recommended_core = 0.005
recommended_margin = 5

print("\nHere are the Recommended Pairs : ")
print("1. ETH 🔥")
print("2. BNB 🔥")
print("3. DOGE 🚀")
# print("4. LINK")
# print("5. 1INCH 🦄")
# print("6. SUSHI 🍣")
# print("7. UNI")
# print("8. MATIC")
# print("9. XRP")
print("0. Others (Required more input)")
asset_input = input("\nChoose your Pair : ")

if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: ETH): ").upper()
elif (asset_input == '1') : asset = "ETH"
elif (asset_input == '2') : asset = "BNB"
elif (asset_input == '3') : asset = "DOGE"
elif (asset_input == '4') : asset = "LINK"
elif (asset_input == '5') : asset = "1INCH"
elif (asset_input == '6') : asset = "SUSHI"
elif (asset_input == '7') : asset = "UNI"
elif (asset_input == '8') : asset = "MATIC"
elif (asset_input == '9') : asset = "XRP"
else: asset = "ETH"

from termcolor import colored
print(colored("The chosen coin is " + asset + "\n", "green"))