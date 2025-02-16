import time
from plyer import notification

def pomodoro_timer(work_minutes=1, break_minutes=1):
    print("Начинаем работу!")
    time.sleep(work_minutes * 60)  # Работа
    notification.notify(
        title="Пора отдохнуть!",
        message="Вы хорошо поработали. Отдохните 5 минут.",
        timeout=10
    )
    print("Пора отдохнуть!")
    time.sleep(break_minutes * 60)  # Отдых
    notification.notify(
        title="Время работать!",
        message="Отдых окончен. Время вернуться к работе.",
        timeout=10
    )
    print("Время работать!")

if __name__ == "__main__":
    pomodoro_timer()
