def add_task(task_list):
    pass


def remove_task(task_list):
    pass


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
