def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        break
    else:
        print("Invalid choice!")