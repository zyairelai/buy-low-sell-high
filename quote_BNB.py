round_off = 3
recommended_core = 1
recommended_margin = 5

print("\nHere are the supported Pairs : ")
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
elif (asset_input == '1') : asset = "BURGER"
elif (asset_input == '2') : asset = "CAKE"
elif (asset_input == '3') : asset = "SUSHI"
elif (asset_input == '4') : asset = "AAVE"
elif (asset_input == '5') : asset = "ADA"
elif (asset_input == '6') : asset = "DOT"
elif (asset_input == '7') : asset = "MATIC"
elif (asset_input == '8') : asset = "XRP"
elif (asset_input == '9') : asset = "YFI"
else: asset = "SUSHI"
