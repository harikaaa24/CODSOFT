# To-Do List Application

import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{index}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting To-Do List Application.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
