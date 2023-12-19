from emoji import emojize

phrase = input("Input: ")
emoji_phrase = emojize(phrase, language='alias')

print(f"Output {emoji_phrase}")
