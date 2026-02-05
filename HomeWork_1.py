# 1. Функція get_days_from_today
from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
    today = date.today()
    delta = today - given_date
    return delta.days
print(get_days_from_today("2021-10-09"))




