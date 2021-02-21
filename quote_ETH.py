base = "ETH"
round_off = 5
recommended_core = 0.1
recommended_margin = 5

print()
print("Here are the supported Pairs : ")
print("1. ETH 🔥")
print("2. BNB 🔥")
print("3. DOGE 🚀")
print("4. LINK")
print("5. 1INCH 🦄")
print("6. SUSHI 🍣")
# print("7. ")
print("8. MATIC")
print("9. XRP")
print("0. Others (Required more input)")
asset_input = input("\nChoose your Pair : ")

if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: ETH): ").upper()
elif (asset_input == '1') or (asset_input == 'ETH')  : asset = "ETH"
elif (asset_input == '2') or (asset_input == 'BNB')  : asset = "BNB"
elif (asset_input == '3') or (asset_input == 'DOGE') : asset = "DOGE"
elif (asset_input == '4') or (asset_input == 'LINK') : asset = "LINK"
elif (asset_input == '5') or (asset_input == '1INCH'): asset = "1INCH"
elif (asset_input == '6') or (asset_input == 'SUSHI'): asset = "SUSHI"
# elif (asset_input == '7') or (asset_input == ''): asset = ""
elif (asset_input == '8') or (asset_input == 'MATIC'): asset = "MATIC"
elif (asset_input == '9') or (asset_input == 'XRP')  : asset = "XRP"
else: asset = "ETH"

core_input = input("Set BTC Amount for " + asset + "-" + base + " (Default " + str(recommended_core) + ") : ").upper() or recommended_core