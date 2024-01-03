from datetime import date, timedelta
import inflect, sys

p = inflect.engine()

def get_birthdate():
    birthdate_str = input("Date of Birth: ")
    try:
        return date.fromisoformat(birthdate_str)
    except ValueError:
        sys.exit("Invalid date")

def get_age_in_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days * 24 * 60

def format_age(minutes):
    words = p.number_to_words(minutes).replace(" and ", " ")
    return words.capitalize()

def main():
    birthdate = get_birthdate()
    minutes = get_age_in_minutes(birthdate)

    print(f"{format_age(minutes)} minutes")

if __name__ == "__main__":
    main()
