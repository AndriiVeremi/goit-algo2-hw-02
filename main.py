import os
import sys

def main():

    tasks = {
        '1': 'task_1/task1.py',
        '2': 'task_2/task2.py'
    }

    while True:
        print("\n==============================")
        print("Головне меню:")
        print("1. Пошук min/max")
        print("2. Оптимізація 3D-принтера")
        print("Введіть 'q' або 'exit' для виходу.")
        print("==============================")
        
        choice = input("Ваш вибір: ")

        if choice.lower() in ['q', 'exit']:
            print("Завершення роботи.")
            break
        
        script_to_run = tasks.get(choice)

        if script_to_run:
            print(f"\n--- Запуск {script_to_run} ---")
            try:
                os.system(f"{sys.executable} {script_to_run}")
            except Exception as e:
                print(f"Помилка під час виконання {script_to_run}: {e}")
            print(f"--- {script_to_run} завершив роботу ---\n")
        else:
            print("\n*** Неправильний вибір. Спробуйте ще раз. ***")

if __name__ == "__main__":
    main()
