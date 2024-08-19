from datetime import datetime
from dateutil.relativedelta import relativedelta

def parse_datetime(datetime_str):
    try:
        if len(datetime_str) == 5 and datetime_str[2] == ':':
            # Формат: чч:мм
            return datetime.strptime(datetime_str, '%H:%M')
        elif len(datetime_str) == 10 and datetime_str[2] == '.':
            # Формат: дд.мм.гггг
            return datetime.strptime(datetime_str, '%d.%m.%Y')
        elif len(datetime_str) == 16 and datetime_str[2] == '.' and datetime_str[10] == ' ':
            # Формат: дд.мм.гггг чч:мм
            return datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
        elif len(datetime_str) == 19 and datetime_str[2] == '.' and datetime_str[10] == ' ':
            # Формат: дд.мм.гггг чч:мм:сс
            return datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')
        elif len(datetime_str) == 5 and datetime_str[2] == ':':
            # Формат: чч:мм
            return datetime.strptime(datetime_str, '%H:%M')
        else:
            raise ValueError("Неверный формат даты и времени.")
    except ValueError as e:
        print(f"Ошибка при разборе даты: {e}")
        raise

def format_timedelta(delta):
    return (f"{delta.years} лет  {delta.months} месяцев {delta.days} дней "
            f"{delta.hours} часов {delta.minutes} минут {delta.seconds} секунд")

def add_time(datetime_obj, delta):
    return datetime_obj + relativedelta(years=delta.years, months=delta.months, days=delta.days,
                                        hours=delta.hours, minutes=delta.minutes, seconds=delta.seconds)

def subtract_time(datetime1, datetime2):
    return relativedelta(datetime1, datetime2)

def multiply_time(delta, factor):
    total_seconds = int((delta.years * 365 * 24 * 3600 +
                         delta.months * 30 * 24 * 3600 +
                         delta.days * 24 * 3600 +
                         delta.hours * 3600 +
                         delta.minutes * 60 +
                         delta.seconds) * factor)
    return format_seconds_to_relativedelta(total_seconds)

def divide_time(delta, divisor):
    total_seconds = int((delta.years * 365 * 24 * 3600 +
                         delta.months * 30 * 24 * 3600 +
                         delta.days * 24 * 3600 +
                         delta.hours * 3600 +
                         delta.minutes * 60 +
                         delta.seconds) / divisor)
    return format_seconds_to_relativedelta(total_seconds)

def format_seconds_to_relativedelta(seconds):
    years, remainder = divmod(seconds, 365 * 24 * 3600)
    months, remainder = divmod(remainder, 30 * 24 * 3600)
    days, remainder = divmod(remainder, 24 * 3600)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return relativedelta(years=years, months=months, days=days,
                         hours=hours, minutes=minutes, seconds=seconds)

def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение времени")
        print("2. Вычитание времени")
        print("3. Умножение времени")
        print("4. Деление времени")
        print("5. Выход")

        choice = input("Введите номер операции: ").strip()

        if choice == '1':
            datetime_str = input("Введите дату и/или время \n(дд.мм.гггг чч:мм:сс / дд.мм.гггг чч:мм / дд.мм.гггг / чч:мм:cc / чч:мм): ")
            try:
                datetime_obj = parse_datetime(datetime_str)
                years = int(input("Введите количество лет (годов): "))
                days = int(input("Введите количество дней: "))
                hours = int(input("Введите количество часов: "))
                minutes = int(input("Введите количество минут: "))
                seconds = int(input("Введите количество секунд: "))
                delta = relativedelta(years=years, days=days, hours=hours, minutes=minutes, seconds=seconds)
                result = add_time(datetime_obj, delta)
                print("Результат:", result.strftime('%d.%m.%Y %H:%M:%S'))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                datetime1_str = input("Введите первую дату и/или время \n(дд.мм.гггг чч:мм:сс / дд.мм.гггг чч:мм / дд.мм.гггг / чч:мм:cc / чч:мм): ")
                datetime1 = parse_datetime(datetime1_str)
                datetime2_str = input("Введите вторую дату и/или время \n(дд.мм.гггг чч:мм:сс / дд.мм.гггг чч:мм / дд.мм.гггг / чч:мм:cc / чч:мм): ")
                datetime2 = parse_datetime(datetime2_str)
                result = subtract_time(datetime1, datetime2)
                print("Разница:", format_timedelta(result))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            try:
                print("Введите временной интервал для умножения:")
                years = int(input("Введите количество лет (годов): "))
                days = int(input("Введите количество дней: "))
                hours = int(input("Введите количество часов: "))
                minutes = int(input("Введите количество минут: "))
                seconds = int(input("Введите количество секунд: "))
                factor = float(input("Введите множитель: "))
                delta = relativedelta(years=years, days=days, hours=hours, minutes=minutes, seconds=seconds)
                result = multiply_time(delta, factor)
                print("Результат:", format_timedelta(result))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '4':
            try:
                print("Введите временной интервал для деления:")
                years = int(input("Введите количество лет (годов): "))
                days = int(input("Введите количество дней: "))
                hours = int(input("Введите количество часов: "))
                minutes = int(input("Введите количество минут: "))
                seconds = int(input("Введите количество секунд: "))
                divisor = float(input("Введите делитель: "))
                delta = relativedelta(years=years, days=days, hours=hours, minutes=minutes, seconds=seconds)
                result = divide_time(delta, divisor)
                print("Результат:", format_timedelta(result))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неправильный выбор. Попробуйте снова.")
        print()

if __name__ == '__main__':
    main()
