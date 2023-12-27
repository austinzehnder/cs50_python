import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if "to" not in s:
        raise ValueError

    match = re.search(r"(\d+):(\d+) (AM|PM) to (\d+):(\d+) (AM|PM)", s)
    if not match:
        match = re.search(r"(\d+) (AM|PM) to (\d+) (AM|PM)", s)
        if not match:
            raise ValueError

        groups = match.groups()
        hours1 = int(groups[0])
        minutes1 = 0
        ampm1 = groups[1]
        hours2 = int(groups[2])
        minutes2 = 0
        ampm2 = groups[3]

    else:
        groups = match.groups()
        hours1 = int(groups[0])
        minutes1 = int(groups[1])
        ampm1 = groups[2]
        hours2 = int(groups[3])
        minutes2 = int(groups[4])
        ampm2 = groups[5]

    if hours1 > 12 or minutes1 > 59:
        raise ValueError

    if hours2 > 12 or minutes2 > 59:
        raise ValueError

    if ampm1 == "PM":
        if hours1 != 12:
            hours1 += 12
    elif hours1 == 12:
        hours1 = 0

    if ampm2 == "PM":
        if hours2 != 12:
            hours2 += 12
    elif hours2 == 12:
        hours2 = 0

    return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"


if __name__ == "__main__":
    main()
