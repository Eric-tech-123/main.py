from todolist import TodoList

# Prints the main menu options
def print_menu():
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View List")
    print("4. Remove Task")
    print("5. Exit")

# Gets the user's choice
def get_user_choice():
    choice = input("Enter your choice (1-5): ")
    return choice

# Adds a task to the to-do list
def add_task(todo_list):
    task = input("Enter a task: ")
    todo_list.add_task(task)
    print("Task added successfully.")

# Marks a task as completed
def mark_completed(todo_list):
    task_id = int(input("Enter the task ID to mark as completed: "))
    if todo_list.mark_completed(task_id):
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")

# Views the list of tasks
def view_list(todo_list):
    tasks = todo_list.get_tasks()
    if tasks:
        print("To-Do List:")
        for task in tasks:
            print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}")
    else:
        print("No tasks found.")

# Removes a task from the to-do list
def remove_task(todo_list):
    task_id = int(input("Enter the task ID to remove: "))
    if todo_list.remove_task(task_id):
        print("Task removed successfully.")
    else:
        print("Invalid task ID.")

# Main function to run the To-Do List application
def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            view_list(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()