import inflect

def bid_adieu(names):
    p = inflect.engine()

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        adieu_str = "Adieu, adieu, to " + ", ".join(names[:-1]) + f", and {names[-1]}"
        print(adieu_str)

def main():
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()

    bid_adieu(names)

if __name__ == "__main__":
    main()
