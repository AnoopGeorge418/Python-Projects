import sys
import os

all_tasks = []

def load_Tasks():
    """Load tasks from a file into the ToDo List Application"""
    if os.path.exists('./tasks.csv'):
        with open('./tasks.csv', 'r') as file:
            for line in file:
                all_tasks.append(line.strip())
    elif os.path.exists('./tasks.txt'):
        with open('./tasks.txt', 'r') as file:
            for line in file:
                all_tasks.append(line.strip())

def add_Tasks():
    """Adding 1 or more new tasks to the ToDo List Application"""
    global all_tasks
    try:
        no_of_task = int(input('Enter the number of tasks you want to add: '))
        for _ in range(no_of_task):
            task = input('Task: ').title()
            all_tasks.append(task)
        print(f'All Task added successfully!')
        view = input('Do you want to view your tasks (y/n): ').lower()
        if view == 'y':
            view_Tasks()
        else:
            todo()
    except ValueError:
        print('Error: Please enter a number')
        add_Tasks()

def view_Tasks():
    """Viewing all the tasks that are in ToDo List Application"""
    if not all_tasks:
        print('No tasks to display.')
        add = input('Want to add task? (y/n): ').lower()
        if add == 'y':
            add_Tasks()
        else:
            todo()
    else:
        for idx, task in enumerate(all_tasks, 1):
            print(f'{idx}: {task}')
        update = input('Do you want to update a task (y/n): ').lower()
        if update == 'y':
            update_Task()
        delete = input('Do you want to delete a task (y/n): ').lower()
        if delete == 'y':
            delete_Task()
        main_menu = input('Do you want to go back to the main menu (y/n): ').lower()
        if main_menu == 'y':
            todo()

def update_Task():
    """Updating a task in the ToDo List Application"""
    for idx, task in enumerate(all_tasks, 1):
        print(f'{idx}: {task}')
    try:
        task_no = int(input('Enter the task number that you want to update: '))
        if 1 <= task_no <= len(all_tasks):
            edit = input('Enter the Changes that you want to make:\n ')
            all_tasks[task_no - 1] = edit
            print(f'Task number {task_no} updated with {edit} and added to todo list successfully')
        else:
            print(f'Error: Task number - {task_no} not found!')
    except ValueError:
        print('Error: please enter a valid number.')
        update_Task()

def delete_Task():
    """Deleting a tasks in the ToDo List Application"""
    for idx, task in enumerate(all_tasks, 1):
        print(f'{idx}: {task}')
    try:
        task_no = int(input('Enter the task number that you want to delete: '))
        if 1 <= task_no <= len(all_tasks):
            removed_task = all_tasks.pop(task_no - 1)
            print(f'Task "{removed_task}" deleted successfully!')
        else:
            print(f'Error: Task number {task_no} not found!')
    except ValueError:
        print('Error: Please enter a valid task number.')
        delete_Task()
        
def save_Tasks():
    """Saving tasks to a file in ToDo List Application"""
    save = int(input('Save in 1(.Csv) or 2(.txt) format? '))
    if save == 1:
        with open('tasks.csv', 'w') as file:
            for task in all_tasks:
                file.write(task + '\n')
        print('All tasks saved successfully!')
    else:
        with open('tasks.txt', 'w') as file:
            for task in all_tasks:
                file.write(task + '\n')
        print('All tasks saved successfully!')

def exit_from_app():
    """Exiting from the Application"""
    if not all_tasks:
        print('Exiting from app...')
        sys.exit()
    else:
        save = input('Do you want to save the tasks? (y/n): ').lower()
        if save == 'y':
            save_Tasks()
        else:
            print('Your tasks are not saved... Bye!')
        sys.exit()

def todo():
    """Performs all the operations of ToDo List Application"""
    tasks = {
        1: 'Add a New Task',
        2: 'View Existing Tasks',
        3: 'Update an Existing Task',
        4: 'Delete an Existing Task',
        5: 'Exit from Application\n'
    }
    for key, value in tasks.items():
        print(f'{key}. {value}')
    try:
        choose = int(input('Enter the task number that you want to perform: '))
        if choose == 1:
            add_Tasks()
        elif choose == 2:
            view_Tasks()
        elif choose == 3:
            update_Task()
        elif choose == 4:
            delete_Task()
        elif choose == 5:
            exit_from_app()
        else:
            print('Error: Please enter a valid number.')
            todo()
    except ValueError:
        print('Error: Only enter the given numbers.')
        todo()

def main():
    """Calling the todo program to run again and again, if there is an error in user input"""
    print('Welcome to ToDo List application!')
    load_Tasks()  
    while True:
        todo()

if __name__ == '__main__':
    main()