import sys

def main():
    fraction = input("Fraction: ")
    try:
        print(gauge(convert(fraction)))
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Invalid input")


def convert(fraction):
    try:
        X, Y = map(int, fraction.split('/'))
        if Y == 0:
            raise ZeroDivisionError("Invalid input")
        if X > Y:
            raise ValueError("Invalid input")

        return round(X / Y * 100)

    except ValueError:
        raise ValueError("Invalid input")
    except ZeroDivisionError:
        raise ZeroDivisionError("Invalid input")

def gauge(percentage):
    # Check for empty or full tank
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
      main()
