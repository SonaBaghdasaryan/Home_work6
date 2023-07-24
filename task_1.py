# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from datetime import datetime

date_st = input('Введите дату в формате DD.MM.YYYY: ')
def leap_year(year):
    return year % 4 == 0 or year % 100 == 0 and year % 400 != 0

def valis_date(date_str):
    try:
        value = datetime.strptime(date_str, "%d.%m.%Y").date()
        day, month, year = map(int, date_str.split('.'))
        if leap_year(year) == 1:
            return True
        return True
    except:
        return False

print(valis_date(date_st))
if __name__ == '__main__':
    _, date_str = sys.argv
    print(valis_date(date_str))