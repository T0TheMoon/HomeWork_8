from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    today = date.today()  # Отримуємо поточну дату
    next_week = today + timedelta(days=7)  # Обчислюємо дату через тиждень
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }  # Словник з номерацією днів тижня та відповідними назвами днів
    birthday_week = {day: [] for day in
                     weekdays.values()}  # Створюємо словник для зберігання днів народження за днями тижня

    for user in users:
        # Встановлюємо поточний рік для дня народження користувача
        birthday = user["birthday"].replace(year=today.year)
        if birthday < today:  # Якщо день народження вже минув у поточному році
            # Встановлюємо наступний рік
            birthday = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження потрапляє у вікно наступного тижня і не впадає на вихідні
        if today <= birthday <= next_week:
            # 0-4 відповідають пн-пт (робочі дні)
            day_name = weekdays[birthday.weekday()]
            if day_name in ["Saturday", "Sunday"]:
                day_name = "Monday"  # Отримуємо назву дня тижня для дня народження
            birthday_week[day_name].append(
                user["name"])  # Додаємо ім'я користувача до списку імен відповідного дня тижня

    return {day: names for day, names in birthday_week.items() if names}


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")