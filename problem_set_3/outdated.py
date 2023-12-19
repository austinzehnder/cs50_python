months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        try:
            m, d, y = date.split("/")
            month = int(m)
            day = int(d)
            year = int(y)
        except ValueError:
            print("Invalid date format")
            continue
    else:
        try:
            month_str, day_str, year_str = date.replace(",", "").split()
            day = int(day_str)
            year = int(year_str)
            month = months.index(month_str) + 1
        except ValueError:
            print("Invalid date format")
            continue

    if "," not in date and "/" not in date:
        print("Invalid date format")
        continue

    if 1 <= month <= 12 and 1 <= day <= 31:
        print(f"{year:04}-{month:02}-{day:02}")
        break
    else:
        print("Invalid date")
