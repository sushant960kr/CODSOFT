import json

class ToDoList:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. {task['task']} [{status}]")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                todo_list.mark_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
