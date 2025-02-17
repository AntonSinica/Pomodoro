import time
from plyer import notification
from tqdm import tqdm

def countdown(seconds):
    for _ in tqdm(range(seconds)):  # Прогресс-бар
        time.sleep(1)

def pomodoro_timer(work_minutes=0.1, break_minutes=0.1, cycles=2):
    for cycle in range(1, cycles + 1):
        print(f"Цикл {cycle}: Начинаем работу!")
        countdown(int(work_minutes * 60))
        notification.notify(
            title="Пора отдохнуть!",
            message=f"Цикл {cycle} завершен. Отдохните {break_minutes} минут.",
            timeout=10
        )
        if cycle == cycles:  # на последнем цикле пропускаем цикл отдыха
            continue

        print(f"Цикл {cycle}: Пора отдохнуть!")
        countdown(int(work_minutes * 60))  # Заменяем time.sleep на countdown
        notification.notify(
            title="Время работать!",
            message="Отдых окончен. Время вернуться к работе.",
            timeout=10
        )
    print("Все циклы завершены!")

if __name__ == "__main__":
    pomodoro_timer()