import sys
import random
from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1:
        font = random.choice(Figlet().getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            font = sys.argv[2]
            if font not in Figlet().getFonts():
                print("Invalid usage")
                sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

    figlet = Figlet(font=font)
    text = input("Input: ")

    print ("Output: ", end="\n")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
