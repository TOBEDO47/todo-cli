#Giovanni Khoshaba
#1221672569

import argparse  # For handling command-line arguments
import json      # To read/write task data in JSON format
import os        # To check if the JSON file exists

# Name of the file where tasks will be stored
TODO_FILE = 'todo.json'

# Load tasks from the JSON file, or return an empty list if the file doesn't exist
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            # If the JSON is malformed, start fresh with an empty list
            tasks = []
    return tasks

# Save the list of tasks back to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task to the to-do list
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,           # Assign the next available ID
        "description": description,     # The text of the task
        "completed": False              # Default to not completed
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: "{description}"')

# Display all tasks with their status (completed or not)
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for task in tasks:
            status = "✔" if task["completed"] else "✘"
            print(f'{task["id"]}. [{status}] {task["description"]}')

# Remove a task by its ID
def remove_task(task_id):
    tasks = load_tasks()
    # Filter out the task to be removed
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print(f'No task found with ID {task_id}')
        return
    # Reassign IDs to keep them consecutive
    for i, task in enumerate(new_tasks, start=1):
        task["id"] = i
    save_tasks(new_tasks)
    print(f"Task {task_id} removed.")

# Mark a specific task as completed
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"No task found with ID {task_id}")

# Handle command-line interface and parse commands
def main():
    parser = argparse.ArgumentParser(description="Simple command-line To-Do list manager")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Command: add
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    # Command: list
    subparsers.add_parser('list', help='List all tasks')

    # Command: remove
    parser_remove = subparsers.add_parser('remove', help='Remove a task by ID')
    parser_remove.add_argument('id', type=int, help='ID of the task to remove')

    # Command: complete
    parser_complete = subparsers.add_parser('complete', help='Mark a task as complete')
    parser_complete.add_argument('id', type=int, help='ID of the task to complete')

    # Parse the command-line arguments and call the appropriate function
    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'remove':
        remove_task(args.id)
    elif args.command == 'complete':
        complete_task(args.id)
    else:
        parser.print_help()

# Run the program if this script is executed directly
if __name__ == '__main__':
    main()
