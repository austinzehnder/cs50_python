def main():
    user_input = input("Greeting: ")
    user_input = user_input.lower().strip()

    if user_input.startswith("hello") == True:
        print("$0")
    elif user_input.startswith("h") == True:
        print("$20")
    else:
        print("$100")

main()
