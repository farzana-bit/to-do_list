import os

def display_menu():
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Save and Exit")
    print("5. Load and View To-Do List")
    print("6. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        
def add_task(tasks):
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"\nTask '{task}' added to your To-Do List.\n")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to remove: "));
            if 1 <= task_num <= len(tasks):
                remove_task = tasks.pop(task_num - 1)
                print(f"'{remove_task}' has been removed from To-Do List.")
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

def save_tasks(tasks, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("\nTasks saved to file {filename}.\n")

def load_tasks(filename="todo_list.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
            print(f"\nTo-Do List loaded from {filename}")
    else:
        print(f"\n{filename} not found. Starting with an empty to-do list. ")
    return tasks

def todo_app():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("\nEnter your choice(1-6): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
        elif choice == '5':
            tasks = load_tasks()
        elif choice == '6':
            save_option = input(
                "Do you want to save your To-Do List before exiting? (yes/no):")
            if save_option.lower() == "yes":
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    todo_app()
