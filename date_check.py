import datetime


def parse_date(date_str):
    # Определение разделителя и разбиение строки на части
    if '.' in date_str:
        parts = date_str.split('.')
    elif '/' in date_str:
        parts = date_str.split('/')
    else:
        raise ValueError("Неправильный формат даты. Ожидается 'дд.мм.гггг' или 'дд/мм/гггг'.")

    # Преобразование частей в целые числа
    day, month, year = map(int, parts)
    return day, month, year


def check_date(day, month, year, current_day, current_month, current_year):
    if year < 1 or year > current_year:
        return False

    days_in_month = {1: 31, 2: 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
                     3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month[month]:
        return False

    if year == current_year:
        if month > current_month or (month == current_month and day > current_day):
            return False

    return True


def main():
    today = datetime.date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year

    print(f"Сегодня {current_day}.{current_month}.{current_year}")

    flag = True
    while flag:
        date = input("Введите дату для проверки (дд.мм.гггг или дд/мм/гггг): ")

        try:
            day, month, year = parse_date(date)

            if check_date(day, month, year, current_day, current_month, current_year):
                print("Дата корректна.")
            else:
                print("Дата некорректна.")
        except ValueError as e:
            print(e)

        while True:
            flag_str = input("Проверить другую дату (Y/N)? ").strip().upper()
            if flag_str in ['Y', 'N']:
                break
            print("Введите 'Y' для продолжения или 'N' для выхода.")

        if flag_str == 'N':
            flag = False


if __name__ == '__main__':
    main()
