# Initialise the module that I will need
import json
import os
import sys
import time


def create_task_file() -> None:
    '''Create a JSON task file if it does not exists'''
    file_name = "task.json"
    
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)
        print(f"{file_name} was created.")
    else:
        print(f"{file_name} already exists.")


def add_task(description:str) -> None:
    """Add a task to the task.json file"""

    # Try to read the task.json file content
    try:
        with open('task.json', 'r') as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error: The file 'task.json' contains invalid JSON data.")
    
    # # Normalize task description to prevent case-sensitive duplicates
    description_list = [task['description'].lower() for task in tasks]
    
    # Check if the task already exists
    if description.lower() not in description_list:
        # Create a dictionary that contain all the task information
        task = {
            'id': len(tasks) + 1,
            'description': description,
            'status': 'todo',
            'createdAT': time.asctime(),
            'updatedAT': None
        }
        
        # Apped new task and update the task.json file
        tasks.append(task)
        with open('task.json', 'w') as file:
            json.dump(tasks, file, indent=4)
        
        print(f"Task added succesfully.")
    else:
        print(f"Task with the description '{description}' already exists!")