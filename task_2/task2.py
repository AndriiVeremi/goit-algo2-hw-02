from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера,
    використовуючи жадібний алгоритм.

    Args:
        print_jobs: Список завдань на друк у форматі словників.
        constraints: Обмеження принтера у форматі словника.

    Returns:
        Dict з оптимальним порядком друку та загальним часом.
    """
    # Крок 1: Перетворюємо вхідні словники на об'єкти dataclass 
    jobs = [PrintJob(**job) for job in print_jobs]
    printer_cons = PrinterConstraints(**constraints)

    # Крок 2: Сортуємо завдання за пріоритетом жадібний вибір
    jobs.sort(key=lambda job: job.priority)

    print_order = []
    total_time = 0
    
    remaining_jobs = list(jobs)

    # Крок 3: Формуємо партії, доки є невиконані завдання
    while remaining_jobs:
        current_batch = []
        current_volume = 0
        
        jobs_to_remove = []

        # Крок 4: Жадібно наповнюємо партію
        for job in remaining_jobs:
            
            if (current_volume + job.volume <= printer_cons.max_volume and
                    len(current_batch) < printer_cons.max_items):
                
                
                current_batch.append(job)
                current_volume += job.volume
                jobs_to_remove.append(job)

        if not current_batch and remaining_jobs:
            job = remaining_jobs[0]
        
            if job.volume > printer_cons.max_volume or printer_cons.max_items < 1:
                 print(f"Попередження: Завдання {job.id} не може бути надруковане, оскільки перевищує обмеження принтера.")
                 jobs_to_remove.append(job) 
            else:
                current_batch.append(job)
                jobs_to_remove.append(job)


        # Крок 5: Обробляємо сформовану партію
        if current_batch:
            
            batch_time = max(job.print_time for job in current_batch)
            total_time += batch_time

            for job in current_batch:
                print_order.append(job.id)

            remaining_jobs = [job for job in remaining_jobs if job not in jobs_to_remove]

        elif remaining_jobs:
            print("Помилка: Не вдалося обробити решту завдань. Можливо, вони завеликі.")
            break


    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")

if __name__ == "__main__":
    test_printing_optimization()
