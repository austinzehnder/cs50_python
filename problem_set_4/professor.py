import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        print(f"{x} + {y} = ", end="")

        correct_answer = x + y
        try_count = 0

        while try_count < 3:
            try:
                ans = int(input())
                if ans == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    print(f"{x} + {y} = ", end="")
                try_count += 1
            except ValueError:
                print("EEE")
                print(f"{x} + {y} = ", end="")
                try_count += 1

            if try_count == 3:
                print(f"{correct_answer}\n")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    return random.randint(10**(level -1)-int(level == 1), 10**level-1)


if __name__ == "__main__":
    main()
