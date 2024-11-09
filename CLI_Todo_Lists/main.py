import os 

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the tasks."""
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

def add_task(task, tasks):
    """Add a task to the list."""
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def remove_task(task_number, tasks):
    """Remove a task from the list."""
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{task}' removed!")
    else:
        print("Invalid task number.")

def mark_task_completed(task_number, tasks):
    """Mark a task as completed."""
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        tasks[task_number - 1] = task + " (Completed)"
        save_tasks(tasks)
        print(f"Task '{task}' marked as completed!")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == '3':
            display_tasks(tasks)
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number, tasks)
        elif choice == '4':
            display_tasks(tasks)
            task_number = int(input("Enter task number to mark as completed: "))
            mark_task_completed(task_number, tasks)
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
