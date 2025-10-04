import os
import sys

def main():
    """
    Main function that acts as a menu to run tasks.
    """
    # Dictionary mapping user choice to the task script
    tasks = {
        '1': 'task_1/task.py',
        '2': 'task_2/task2.py'
    }

    while True:
        print("\n==============================")
        print("Main Menu:")
        print("1. Run Task 1 (Min/Max Search)")
        print("2. Run Task 2 (3D Printer Optimizer)")
        print("Enter 'q' or 'exit' to quit.")
        print("==============================")
        
        choice = input("Your choice: ")

        if choice.lower() in ['q', 'exit']:
            print("Exiting.")
            break
        
        script_to_run = tasks.get(choice)

        if script_to_run:
            print(f"\n--- Running {script_to_run} ---")
            try:
                # Use sys.executable to ensure the same Python version is used
                os.system(f"{sys.executable} {script_to_run}")
            except Exception as e:
                print(f"Error while running {script_to_run}: {e}")
            print(f"--- {script_to_run} finished ---\n")
        else:
            print("\n*** Invalid choice. Please try again. ***")

if __name__ == "__main__":
    main()