import time
from plyer import notification

def countdown(seconds: int) -> None:
    """
    Выполняет обратный отсчет в секундах с отображением прогресса в процентах.

    Args:
        seconds (int): Количество секунд для обратного отсчета.

    Returns:
        None
    """
    for i in range(seconds):
        percent: float = (i + 1) / seconds * 100  # Процент выполнения
        elapsed: int = i + 1                       # Прошедшее время в секундах
        remaining: int = seconds - (i + 1)         # Оставшееся время в секундах
        # Выводим прогресс в процентах, прошедшее и оставшееся время
        print(f"\rПрогресс: {percent:5.1f}% | Прошло (сек): {elapsed:3d} | Осталось (сек): {remaining:3d}", end="")
        time.sleep(1)  # Задержка в 1 секунду
    print()  # Переходим на новую строку после завершения

def work_timer(work_minutes: float, cycle: int) -> None:
    """
    Запускает таймер рабочего цикла и уведомляет о необходимости отдыха.

    Args:
        work_minutes (float): Длительность рабочего цикла в минутах.
        cycle (int): Номер текущего цикла.

    Returns:
        None
    """
    print(f"Цикл {cycle}: Начинаем работу!")
    countdown(int(work_minutes * 60))  # Конвертируем минуты в секунды и запускаем отсчет
    # Отправляем уведомление о завершении рабочего цикла
    notification.notify(
        title="Пора отдохнуть!",
        message=f"Цикл {cycle} завершен. Отдохните.",
        timeout=10  # Уведомление отображается 10 секунд
    )

def break_timer(break_minutes: float, cycle: int) -> None:
    """
    Запускает таймер перерыва и уведомляет о необходимости вернуться к работе.

    Args:
        break_minutes (float): Длительность перерыва в минутах.
        cycle (int): Номер текущего цикла.

    Returns:
        None
    """
    print(f"Цикл {cycle}: Пора отдохнуть!")
    countdown(int(break_minutes * 60))  # Конвертируем минуты в секунды и запускаем отсчет
    # Отправляем уведомление о завершении перерыва
    notification.notify(
        title="Время работать!",
        message="Отдых окончен. Время вернуться к работе.",
        timeout=10  # Уведомление отображается 10 секунд
    )

def pomodoro_timer(work_minutes: float = 0.05, break_minutes: float = 0.05, cycles: int = 2) -> None:
    """
    Запускает цикл техники Помодоро с рабочими и перерывными интервалами.

    Args:
        work_minutes (float, optional): Длительность рабочего интервала в минутах. По умолчанию 0.05 (3 секунды для теста).
        break_minutes (float, optional): Длительность перерыва в минутах. По умолчанию 0.05 (3 секунды для теста).
        cycles (int, optional): Количество циклов. По умолчанию 2.

    Returns:
        None
    """
    for cycle in range(1, cycles + 1):
        work_timer(work_minutes, cycle)  # Запускаем рабочий цикл
        print()  # Пустая строка для разделения вывода
        if cycle == cycles:
            continue  # Пропускаем перерыв для последнего цикла
        break_timer(break_minutes, cycle)  # Запускаем перерыв
        print()  # Пустая строка для разделения вывода

    print("Все циклы завершены!")

if __name__ == "__main__":
    # Запускаем таймер Помодоро с тестовыми значениями
    pomodoro_timer()