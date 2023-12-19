def main():
    user_input = input.lower("Input: ")


def remove_vowels(user_input):
    vowels = "aeiouAEIOU"
    return "".join(c for c in text if c not in vowels)

text = input("Input: ")

text_without_vowels = remove_vowels(text)

print(f"Output: {text_without_vowels}")
