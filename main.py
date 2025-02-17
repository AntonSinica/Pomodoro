import time
from plyer import notification
from tqdm import tqdm

def countdown(minutes):
    for _ in tqdm(range(minutes * 60)):  # Прогресс-бар на minutes * 60 секунд
        time.sleep(1)  # Ждем 1 секунду

def pomodoro_timer(work_minutes=1, break_minutes=1, cycles=2):
    for cycle in range(1, cycles + 1):
        print(f"Цикл {cycle}: Начинаем работу!")
        countdown(work_minutes)  # Заменяем time.sleep на countdown
        notification.notify(
            title="Пора отдохнуть!",
            message=f"Цикл {cycle} завершен. Отдохните {break_minutes} минут.",
            timeout=10
        )
        print(f"Цикл {cycle}: Пора отдохнуть!")
        countdown(break_minutes)  # Заменяем time.sleep на countdown
        notification.notify(
            title="Время работать!",
            message="Отдых окончен. Время вернуться к работе.",
            timeout=10
        )
    print("Все циклы завершены!")

if __name__ == "__main__":
    pomodoro_timer()