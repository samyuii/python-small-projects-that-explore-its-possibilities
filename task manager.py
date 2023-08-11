class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


tasks = []


def add_task(description, priority):
    task = Task(description, priority)
    tasks.append(task)
    print("Task added successfully!")


def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.description} - Priority: {task.priority} - {status}")

while True:
    print("Welcome to the Task Manager!")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter task priority (High/Medium/Low): ")
        add_task(description, priority)
        print("\n")
    elif choice == "2":
        display_tasks()
        print("\n")
    elif choice == "3":
        display_tasks()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index].mark_as_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
        print("\n")
    elif choice == "4":
        print("Thanks for using the Task Manager. Stay organized!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        print("\n")
