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


# 2. Функція get_numbers_ticket
import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (min_val <= quantity <= (max_val - min_val + 1)):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_val, max_val))
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



# 3.Функція normalize_phone(необов’язкове)

import re

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if phone_number.startswith("+"):
        if not phone_number.startswith("+38"):
            if phone_number.startswith("+380"):
                pass
            else:
                phone_number = "+38" + phone_number[1:]
    else:
        if phone_number.startswith("380"):
            phone_number = "+" + phone_number
        else:
            phone_number = "+38" + phone_number
    return phone_number
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)