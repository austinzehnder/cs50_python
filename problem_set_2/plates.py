def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # No special characters
    if any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in s):
        return False

    # Check first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check digits can only appear at the end and doesn't start with zero
    ls = list(s)
    for i in range(len(ls)):
        if ls[i].isdigit():
            if s[i] == '0':
                return False
            if i < len(s)-1 and s[i+1:].isalpha():
                return False

    # No special characters
    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()
