# Initialise the module that I will need
import json
import os
import sys
import time
from typing import Any


def create_task_file(file_name:str) -> None:
    '''Create a JSON task file if it does not exists'''

    # Check if the file ends with json
    if not file_name.endswith(".json"):
        print(f"{file_name} is not json file.")
    
    # Check if the file exists
    elif not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)
        print(f"{file_name} was created.")
    
    # print a messaget that indicate that the file already exists
    else:
        print(f"{file_name} already exists.")


def task_exists(description:str, tasks:list) -> bool:
    """Check for the existence of the task in the tasks list"""
    # Normalize task description to prevent case-sensitive duplicates
    description_list = [task['description'].lower() for task in tasks]
    return description.lower() not in description_list


def add_task(description:str, file_name:str) -> None:
    """Add a task to the task.json file"""

    # Try to read the task.json file content
    try:
        with open(file_name, 'r') as file:
            tasks:list = json.load(file)
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error: The file '{file_name}' contains invalid JSON data.")
    
    # Check if the task already exists
    if task_exists(description, tasks):

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
        with open(file_name, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        print(f"Task added succesfully.")
    else:
        print(f"Task with the description '{description}' already exists!")


def main():
    try:
        commands = sys.argv[1:]
        commands_length = len(commands)
        match commands[0]:
            case 'create':
                if commands_length > 1:
                    print(f"Commande 'create' does not support any parameter.")
                else:
                    create_task_file('task.json')
            case 'add_task':
                if commands_length > 2:
                    print(f"Commande 'add_task' supports only one parameter.")
                elif commands_length == 0:
                    print(f"Commade 'add_task' needs additional parameter.")
                else:    
                    add_task(commands[1], 'task.json')
            case _:
                print(f"Invalid Command")
    except:
        return None
        

main()