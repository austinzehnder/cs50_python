def main():
    print(f"${value(input("Greeting: ").lower().strip())}")

def value(greeting):
    if greeting[0:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
