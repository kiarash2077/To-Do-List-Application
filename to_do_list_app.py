def add_task(task_list):
    pass


def remove_task(task_list: list[str]) -> None:
    task = input("Enter the task to remove: ")
    if task == "":
        print("Invalid input.")

        return

    if task in task_list:
        task_list.remove(task)
        print(f"'{task}' has been removed from the list.")
    else:
        print(f"No task found '{task}'.")


def view_tasks(task_list):
    pass


def main():
    task_list = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            remove_task(task_list)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
