import time
from plyer import notification

def pomodoro_timer(work_minutes=0.1, break_minutes=0.1, cycles=2):
    for cycle in range(1, cycles + 1):
        print(f"Цикл {cycle}: Начинаем работу!")
        time.sleep(work_minutes * 60)
        notification.notify(
            title="Пора отдохнуть!",
            message=f"Цикл {cycle} завершен. Отдохните {break_minutes} минут.",
            timeout=10
        )
        print(f"Цикл {cycle}: Пора отдохнуть!")
        time.sleep(break_minutes * 60)
        notification.notify(
            title="Время работать!",
            message="Отдых окончен. Время вернуться к работе.",
            timeout=10
        )
    print("Все циклы завершены!")

if __name__ == "__main__":
    pomodoro_timer()
