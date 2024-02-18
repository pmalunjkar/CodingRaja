import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task_name, priority, due_date):
        self.tasks.append({
            'name': task_name,
            'priority': priority,
            'due_date': due_date,
            'completed': False
        })
        self.save_tasks()

    def remove_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()

    def mark_completed(self, task_index):
        self.tasks[task_index]['completed'] = True
        self.save_tasks()

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def main():
    filename = "tasks.json"
    task_manager = TaskManager(filename)

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            priority = input("Enter priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(task_name, priority, due_date)

        elif choice == '2':
            task_manager.display_tasks()
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            task_manager.remove_task(task_index)

        elif choice == '3':
            task_manager.display_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            task_manager.mark_completed(task_index)

        elif choice == '4':
            task_manager.display_tasks()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
