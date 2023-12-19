menu = [
    {"Baja Taco": 4.25},
    {"Burrito": 7.50},
    {"Bowl": 8.50},
    {"Nachos": 11.00},
    {"Quesadilla": 8.50},
    {"Super Burrito": 8.50},
    {"Super Quesadilla": 9.50},
    {"Taco": 3.00},
    {"Tortilla Salad": 8.00}
]

def display_total(order):
    total = sum(order.values())
    print(f"${total:.2f}")

def main():
    order = {}

    try:
        while True:
            item = input("Item: ").strip()

            found = False
            for menu_item in menu:
                for key, value in menu_item.items():
                    if item.lower() == key.lower():
                        order[key] = order.get(key, 0) + value
                        found = True
                if found:
                    break

            if found:
                display_total(order)
            else:
                print("Invalid item. Please choose from the menu.")

    except EOFError:
        print("\nOrder complete.")
        display_total(order)

if __name__ == "__main__":
    main()
