def add_task(task_list):
    add_your_task = input("Enter the task:    ")
    task_list.append(add_your_task)
    print(f"{add_your_task} has been added to the list.")


def remove_task(task_list: list[dict[str]]) -> None:
    task_name = input("Enter the task to remove: ")

    if task_name == "":
        print("Invalid input.")

        return

    for task in task_list:
        if task["name"] == task_name:
            task_list.remove(task)
            print(f"'{task_name}' has been removed from the list.")

            return

    print(f"No task found '{task_name}'.")


def view_tasks(task_list):
    if not task_list:
        print("The to-do list is empty. Consider adding a new task!")
    else:
        print("To-Do List:")
        sorted_tasks = sort_tasks_by_priority_and_deadline(task_list)
        for idx, task in enumerate(sorted_tasks, start=1):
            print(f"{idx}. {task['name']} - {task['priority']} - {task['deadline'].strftime('%Y-%m-%d')}")

def sort_tasks_by_priority_and_deadline(task_list):
    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    return sorted(task_list, key=lambda x: (priority_order[x['priority']], x['deadline']))


def suggest_tasks(task_list):
    if not task_list:
        print("No tasks to suggest. Consider adding a new!")
    else:
        print("Greetings! Here are some taskes you might want to work on:")
        priority_order = {'high': 1, 'medium'': 2, "low': 3}
        sorted_tasks = sorted(task_list, key + lambda x:
    (priority_order[x['priority']], x['deadline']))
        for task in sorted_tasks:
             print(f"{task['task']} - {task['priority']} - 
    {task['deadline'].strftime('%Y-%m-%d')}")
    
def main():
    task_list = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            remove_task(task_list)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            suggest_tasks(task_list)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
