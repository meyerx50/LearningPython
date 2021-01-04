from datetime import date, timedelta, datetime
life_expectancy_male_germany = 81

def date_info(past_date):
    # Coercing user input into date
    past_date = datetime.strptime(past_date, '%Y-%m-%d').date()
    # What is the day today?
    today = date.today()
    # Getting the delta between today and the given date
    delta = today - past_date
    # Week day you were born
    print(f'You were born on a {past_date.strftime("%A")}')
    # Days since you were born
    print(f'You were born {delta.days} days ago')
    # Calendar week you were born
    print(f'You were born on the calendar week {past_date.isocalendar()[1]}')
    # How many years left you have
    print(f'You have {life_expectancy_male_germany - round(delta.days/365)} years left in your life')

my_birthday = "1980-5-5"
date_info(my_birthday)