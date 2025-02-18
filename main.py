import time
from plyer import notification

def countdown(seconds):
    for i in range(seconds):
        percent = (i + 1) / seconds * 100  # Процент выполнения
        elapsed = i + 1                    # Прошедшее время в секундах
        remaining = seconds - (i + 1)      # Оставшееся время в секундах
        print(f"\rПрогресс: {percent:5.1f}% | Прошло (сек): {elapsed:3d} | Осталось (сек): {remaining:3d}", end="")
        time.sleep(1)
    print()  # Переходим на новую строку после завершения

def pomodoro_timer(work_minutes=0.1, break_minutes=0.1, cycles=2):
    for cycle in range(1, cycles + 1):
        print(f"\nЦикл {cycle}: Начинаем работу!")
        countdown(int(work_minutes * 60))
        notification.notify(
            title="Пора отдохнуть!",
            message=f"Цикл {cycle} завершен. Отдохните {break_minutes} минут.",
            timeout=10
        )
        if cycle == cycles:
            continue
        print(f"\nЦикл {cycle}: Пора отдохнуть!")
        countdown(int(break_minutes * 60))
        notification.notify(
            title="Время работать!",
            message="Отдых окончен. Время вернуться к работе.",
            timeout=10
        )
    print("\nВсе циклы завершены!")

if __name__ == "__main__":
    pomodoro_timer()