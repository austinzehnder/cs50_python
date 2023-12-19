def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

def main():
    # Define the meal time ranges
    breakfast_start = convert("7:00")
    breakfast_end = convert("9:00")
    lunch_start = convert("12:00")
    lunch_end = convert("13:00")
    dinner_start = convert("18:00")
    dinner_end = convert("20:00")

    # Prompt user for input
    user_input = input("What time is it? ")

    try:
        # Convert user input into hours as a float
        user_time = convert(user_input)

        # Check if it's breakfast, lunch, or dinner time
        if breakfast_start <= user_time <= breakfast_end:
            print("breakfast time")
        elif lunch_start <= user_time <= lunch_end:
            print("lunch time")
        elif dinner_start <= user_time <= dinner_end:
            print("dinner time")

    except ValueError:
        print("Invalid time format. Please use 24-hour format like '07:30'.")

if __name__ == "__main__":
    main()
