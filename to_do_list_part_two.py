import re


def is_valid_date_format(date_str):

    pattern = r'^\d{4}-\d{2}-\d{2}$'

    return bool(re.match(pattern, date_str))


def add_task(task_list):
    name = input("Enter the task: ")

    priority = input("Enter the priority(high, medium, low): ")
    if priority not in ["high", "medium", "low"]:
        print("Enter the correct word in high, medium, low")
        return

    deadline = input("Enter the deadline (YYYY-MM-DD): ")

    if not is_valid_date_format(deadline):

        print("Please enter the deadline in the correct format (YYYY-MM-DD).")
        return

    if name and priority and deadline:
        task_list.append({"name":name, "priority":priority, "deadline":deadline})

        print(f"{name} with priority '{priority}' and deadline '{deadline}'has been added to the list.")

    else:
        print("Enter the your task details.")


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
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        sorted_tasks = sorted(task_list, key=lambda x: (priority_order[x['priority']], x['deadline']))
        for idx, task in enumerate(sorted_tasks, start=1):
            print(f"{idx}. {task['task']} - {task['priority']} - {task['deadline'].strftime('%Y-%m-%d')}")


def suggest_tasks(task_list):
    if not task_list:
        print("No tasks to suggest. Consider adding a new!")
    else:
        print("Greetings! Here are some taskes you might want to work on:")
        priority_order = {'high': 1, 'medium'': 2, "low': 3}
        sorted_tasks = sorted(task_list, key=lambda x: (priority_order[x['priority']], x['deadline']))
        for task in sorted_tasks:
            print(f"{task['task']} - {task['priority']} - {task['deadline'].strftime('%Y-%m-%d')}")

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
