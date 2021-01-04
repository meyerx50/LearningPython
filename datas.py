import datetime
birthday = datetime.date(2011, 2, 22)
today = datetime.date(2020, 1, 4)
delta = today - birthday
print(f'You were born {delta.days} days ago')