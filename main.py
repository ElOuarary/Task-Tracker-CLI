# Initialise the module that I will need
import json
import os
import sys
import time


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


def add_task(description: str) -> None:
    """Add a task to the task.json file"""

    # Try to read the task.json file
    try:
        with open("task.json", 'r') as file:
            tasks: list = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file 'task.json' does not exists.")
        return None
    
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
        with open("task.json", 'w') as file:
            json.dump(tasks, file, indent=4)
        
        print(f"Task added succesfully.")
    else:
        print(f"Error: Task with the description '{description}' already exists!")


def update_task(id: int, new_description: str):
    """Update a task in task.json file"""

    # Try to read the task.json file
    try:
        with open("task.json", 'r') as file:
            tasks: list = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file 'task.json' does not exists.")

    if id_exists(id, tasks):
        tasks[id-1]["description"] = new_description
        tasks[id-1]["updatedAT"] = time.asctime()
    
        # Apped new task and update the task.json file
        with open("task.json", 'w') as file:
           json.dump(tasks, file, indent=4)
        print(f"Task with the id:{id} updated succefully.")
    else:
        print(f"Error: No task with the id:{id} exists!") 
    

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

            # Command 'add-task' workflow        
            case 'add-task':
                if commands_length > 2:
                    print(f"Commande 'add-task' supports only one parameter.")
                elif commands_length == 1:
                    print(f"1 missing parameter.")
                else:    
                    add_task(commands[1])
                    sys.exit()

            # Command 'update-task workflow
            case "update-task":
                if commands_length > 3:
                    print(f"Commande 'update-task' only supports 2 parametrs.")
                elif commands_length == 2:
                    print(f"1 missing parameter!")
                elif commands_length == 1:
                    print(f"2 missing parametes!")
                else:
                    if not commands[1].isdigit():
                        print(f"Value Error: first parameter is not an integer!")
                        sys.exit()    
                    update_task(int(commands[1]), commands[2])
                    sys.exit()

            # Handle a non existing command
            case _:
                print(f"Invalid Command!")
    
    except:
        return None
        

main()