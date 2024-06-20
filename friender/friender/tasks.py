from celery import shared_task
from datetime import date, timedelta

@shared_task
def get_today_date():
    print(f'Today is {date.today()}') 


@shared_task
def get_tomorrow_date():
    tomorrow = date.today() + timedelta(days=1)
    print(f'Tommorow will be {tomorrow}') 

@shared_task
def task_every_3m40s():
    print("Task running every 3 minutes 40 seconds")


@shared_task
def task_three_times_hourly():
    print("Task running every hour from 19 to 21, for a total of 3 times")