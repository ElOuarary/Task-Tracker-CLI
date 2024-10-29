# Initialise the module that I will need
import json
import os
import sys
import time
from typing import Optional


def create_task_file() -> None:
    '''Create a JSON task file if it does not exists'''

    # Check if the file exists
    if not os.path.exists("task.json"):
        with open("task.json", 'w') as file:
            json.dump([], file)
        print(f"task.json file was created.")
    
    # print a messaget that indicate that the file already exists
    else:
        print(f"task.json file already exists.")


def description_exists(description: str, tasks: list) -> bool:
    """Check for the existence of the description in the tasks list"""
    # Normalize task description to prevent case-sensitive duplicates
    description_list = [task['description'].lower() for task in tasks]
    return description.lower() in description_list


def id_exists(id: int, tasks: list) -> bool:
    """Check for the existence of the id in the tasks list"""
    id_list = [task["id"] for task in tasks]
    return id in id_list


def file_readble() -> Optional[list]:
    """Try to read the task.json file"""
    try:
        with open("task.json", 'r') as file:
            tasks: list = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"Error: The file 'task.json' does not exists.")
        sys.exit

def upadate_file(tasks: list) -> None:
    with open("task.json", 'w') as file:
            json.dump(tasks, file, indent=4)


def add_task(description: str) -> None:
    """Add a task to the task.json file"""
    tasks = file_readble()

    # Check if the task does not exist
    if not description_exists(description, tasks):

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
        upadate_file(tasks)
        
        print(f"Task added succesfully.")
    else:
        print(f"Error: Task with the description '{description}' already exists!")


def update_task(id: int, new_description: str):
    """Update a task in task.json file"""
    tasks = file_readble()

    if id_exists(id, tasks):
        tasks[id-1]["description"] = new_description
        tasks[id-1]["updatedAT"] = time.asctime()
    
        # Update the tasks in task.json file
        upadate_file(tasks)
        print(f"Task with the id:{id} updated succefully.")
    else:
        print(f"Error: No task with the id:{id} exists!") 


def delete_task(id:int) -> None:
    """Delete a task in task.json file"""
    tasks = file_readble()
    
    if id_exists(id, tasks):
        tasks.pop(id - 1)
        upadate_file(tasks)
        print(f"Task with the id:{id} deleted succefully.")
    else:
        print(f"Error: No task with the id:{id} exists!")


def list_task(status:str = None) -> None:
    """List all task in the task.json file"""
    tasks = file_readble()
    if status == None:
       tasks_to_get = tasks
    else:
        tasks_to_get = [task for task in tasks if task["status"] == status]
    for task in tasks_to_get:
        print(f"{task["id"]}: {task["description"]}.")


def main():
    try:
        commands = sys.argv[1:]
        commands_length = len(commands)
        
        # Handle different commandes
        match commands[0]:

            # Command 'create' workflow
            case 'create':
                if commands_length > 1:
                    print(f"Commande 'create' does not support any parameter.")
                else:
                    create_task_file()
                    sys.exit()

            # Command 'add' workflow        
            case 'add':
                if commands_length > 2:
                    print(f"Commande 'add-task' supports only one parameter.")
                elif commands_length == 1:
                    print(f"1 missing parameter.")
                else:    
                    add_task(commands[1])
                    sys.exit()

            # Command 'update' workflow
            case "update":
                if commands_length > 3:
                    print(f"Commande 'update' only supports 2 parametrs.")
                elif commands_length == 2:
                    print(f"1 missing parameter!")
                elif commands_length == 1:
                    print(f"2 missing parametes!")
                else:
                    if not commands[1].isdigit():
                        print(f"Value Error: first parameter is not an integer!")
                        sys.exit()    
                    update_task(int(commands[1]), commands[2])

            # Command 'delete' workflow
            case "delete":
                if commands_length > 2:
                    print(f"Commande 'delete' only supports 1 parameters!")
                elif commands_length == 1:
                    print(f"1 missing parameter!")
                else:
                    if not commands[1].isdigit():
                        print(f"Value Error: first parameter is not an integer!")
                        sys.exit()
                    delete_task(int(commands[1]))

            # Command 'list' workflow
            case "list":
                if commands_length > 2:
                    print(f"Commande 'list' only support one parameter!")
                elif commands_length == 1:
                    list_task(None)
                elif commands[1] in ("todo", "in-progress", "done"):
                    list_task(commands[1])
                else:
                    print(f"Invalid parameter!")
                

            # Handle a non existing command
            case _:
                print(f"Invalid Command!")
    
    except:
        return None
        

main()