round_off = 5
recommended_core = 0.1
recommended_margin = 5

print("\nHere are the supported Pairs : ")
print("1. BNB 🔥")
print("2. AAVE")
print("3. ADA")
print("4. DASH")
print("5. EOS")
print("6. LTC")
print("7. LINK")
print("8. TRX")
print("9. XRP")
print("0. Others (Required more input)")
asset_input = input("\nChoose your Pair : ")

if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: BNB): ").upper()
elif (asset_input == '1') : asset = "BNB"
elif (asset_input == '2') : asset = "AAVE"
elif (asset_input == '3') : asset = "ADA"
elif (asset_input == '4') : asset = "DASH"
elif (asset_input == '5') : asset = "EOS"
elif (asset_input == '6') : asset = "LTC"
elif (asset_input == '7') : asset = "LINK"
elif (asset_input == '8') : asset = "TRX"
elif (asset_input == '9') : asset = "XRP"
else: asset = "BNB"

from termcolor import colored
print(colored("The chosen coin is " + asset + "\n", "green"))