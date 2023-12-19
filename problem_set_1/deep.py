def main():
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Convert the user's input to lowercase and remove spaces
    user_input = user_input.lower().replace(" ", "").replace("-","")

    # Check if the input matches "42", "fortytwo", or "fortytwo"
    if user_input == "42" or user_input == "fortytwo":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
