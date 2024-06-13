import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

    def mark_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as done: "))
            todo_list.mark_done(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()