"""
Author - Philip Favour Boluwatife
Date - 9th December, 2025
Pset Name - Outdated
Pset Detail - implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
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
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""
def main():
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
    update = outdated(months)
    print(update)

def outdated(months):
    max_month = 12
    max_day = 31
    updated = ""
    while True:
        date = input("Enter the date: ")
        try:
            if "/" in date:
                month, day, year = map(int, date.strip().split("/"))
                if day <= max_day and month <= max_month:
                    return f"{year}-{month:02}-{day:02}"
            else:
                day_with_month, year = date.strip().split(",")
                month, day = day_with_month.split()
                if month.title() in months:
                    new_month = months.index(month.title()) + 1
                    day = int(day)
                    if day <= max_day and new_month <= max_month:
                        return f"{year.strip()}-{new_month:02}-{day:02}"
        except Exception as e:
            print(f"Invalid. Here is your error message:\n {e}")

if __name__ == "__main__":
    main()
