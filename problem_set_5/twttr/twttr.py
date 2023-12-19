def main():
    text = input("Input: ")
    text_without_vowels = shorten(text)
    print(f"Output: {text_without_vowels}")

def shorten(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char.isdigit():
            result += char
        elif char in "!,.-?":
            results += char
        elif char.upper() not in vowels:
            result += char

    return result

if __name__ == "__main__":
    main()
