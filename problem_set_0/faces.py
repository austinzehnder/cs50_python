def convert(input_str):
    # Replace :) with 🙂 and :( with 🙁
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")

    return input_str

def main():
    user_input = input("Enter a text with emoticons: ")
    converted_text = convert(user_input)
    print("Converted text:")
    print(converted_text)

if __name__ == "__main__":
    main()
