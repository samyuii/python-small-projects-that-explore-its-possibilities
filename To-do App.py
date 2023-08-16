tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    else:
        break
