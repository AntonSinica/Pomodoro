import time
from plyer import notification
from tqdm import tqdm

def countdown(seconds):
    with tqdm(total=seconds) as pbar:  # Используем менеджер контекста
        for _ in range(seconds):
            time.sleep(1)
            pbar.update(1)

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
