from threading import Timer
from datetime import datetime, timedelta
from catgirl import email_random_catgirl

def calculate_secs():
    '''Calculates number of seconds until action'''

    now = datetime.today()
    tomorrow = now + timedelta(days=1)
    today_morning = datetime(
        now.year,
        now.month,
        now.day,
        hour=8
    )
    today_evening = datetime(
        now.year,
        now.month,
        now.day,
        hour=22
    )
    tomorrow_morning = datetime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        hour=8
    )
    tomorrow_evening = datetime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        hour=22
    )
    possible_dates = [today_morning, today_evening, tomorrow_morning, tomorrow_evening]
    filtered_dates = [date for date in possible_dates if date > now]
    if len(filtered_dates) == 0: return print('No dates?')
    earliest_date = filtered_dates[0]
    for date in filtered_dates:
        if date < earliest_date: earliest_date = date
    time_diff_until_earliest = earliest_date - now
    return time_diff_until_earliest.seconds

def init():
    '''Starts off the process by waiting to email until the next desired time'''
    
    secs = calculate_secs()
    print(f'{secs/(60*60)} hours until next run')
    Timer(secs, scheduler).start()

def scheduler():
    '''Performs the scheduled action then sets up the timer for the next time'''

    email_random_catgirl()
    secs = calculate_secs()
    print(f'{secs/(60*60)} hours until next run')
    Timer(secs, scheduler).start()

init()

