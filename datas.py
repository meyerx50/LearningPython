from datetime import date, timedelta, datetime
life_expectancy_male_germany = 81

def date_info(past_date):
    past_date = datetime.strptime(past_date, '%Y-%m-%d').date()
    today = date.today()
    delta = today - past_date
    print(f'You were born on a {past_date.strftime("%A")}')
    print(f'You were born {delta.days} days ago')
    print(f'You were born on the calendar week {past_date.isocalendar()[1]}')
    print(f'You have {life_expectancy_male_germany - round(delta.days/365)} years left in your life')

my_birthday = "1980-5-5"
date_info(my_birthday)