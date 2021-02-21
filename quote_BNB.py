round_off = 3
recommended_core = 1
recommended_margin = 5

print()
print("Here are the supported Pairs : ")
print("1. BURGER 🍔")
print("2. CAKE 🎂")
print("3. SUSHI 🍣")
print("4. AAVE")
print("5. ADA")
print("6. DOT")
print("7. MATIC")
print("8. XRP")
print("9. YFI")
print("0. Others (Required more input)")
asset_input = input("\nChoose your Pair : ")

if asset_input == '0': asset = input("Enter your COIN SYMBOL (Ex: SUSHI): ").upper()
elif (asset_input == '1') or (asset_input == 'BURGER')  : asset = "BURGER"
elif (asset_input == '2') or (asset_input == 'CAKE')    : asset = "CAKE"
elif (asset_input == '3') or (asset_input == 'SUSHI')   : asset = "SUSHI"
elif (asset_input == '4') or (asset_input == 'AAVE')    : asset = "AAVE"
elif (asset_input == '5') or (asset_input == 'ADA')     : asset = "ADA"
elif (asset_input == '6') or (asset_input == 'DOT')     : asset = "DOT"
elif (asset_input == '7') or (asset_input == 'MATIC')   : asset = "MATIC"
elif (asset_input == '8') or (asset_input == 'XRP')     : asset = "XRP"
elif (asset_input == '9') or (asset_input == 'YFI')     : asset = "YFI"
else: asset = "SUSHI"
