# Initialize variables
coke_price = 50
inserted = 0

# Prompt the user for coins
while inserted < coke_price:
    coin = int(input("Insert coin: "))

    # Validate coin denomination
    if coin not in [5, 10, 25]:
        print("Amount Due: 50")
        continue

    inserted += coin

    # Print amount due if not enough
    if inserted < coke_price:
        print(f"Amount Due: {coke_price - inserted}")

# Calculate and display change
change = inserted - coke_price
print(f"Change Owed: {change}")
