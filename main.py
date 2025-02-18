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

def work_timer(work_minutes, cycle):
    print(f"Цикл {cycle}: Начинаем работу!")
    countdown(int(work_minutes * 60))
    notification.notify(
        title="Пора отдохнуть!",
        message=f"Цикл {cycle} завершен. Отдохните.",
        timeout=10
    )

def break_timer(break_minutes, cycle):
    print(f"Цикл {cycle}: Пора отдохнуть!")
    countdown(int(break_minutes * 60))
    notification.notify(
        title="Время работать!",
        message="Отдых окончен. Время вернуться к работе.",
        timeout=10
    )

def pomodoro_timer(work_minutes=0.05, break_minutes=0.05, cycles=2):
    for cycle in range(1, cycles + 1):
        work_timer(work_minutes, cycle)
        print()
        if cycle == cycles:
            continue
        break_timer(break_minutes, cycle)
        print()

    print("Все циклы завершены!")

if __name__ == "__main__":
    pomodoro_timer()