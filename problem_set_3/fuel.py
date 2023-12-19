def main():
    while True:
        try:
            # Prompt user for input
            fraction = input("Fraction: ")
            # Extract x (numerator) and y (denominator)
            x, y = fraction.split("/")
            x, y = int(x), int(y)

            # Validate input
            if not isinstance(x, int) or not isinstance(y, int):
                raise ValueError()
            if x > y:
                raise ValueError()
            if y == 0:
                raise ZeroDivisionError()

            # Calculate fuel percentage
            percentage = round(100 * (x / y))

            # Check for empty or full tank
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except ValueError:
            print("Invalid input.")
        except ZeroDivisionError:
            print("Invalid input.")


main()
