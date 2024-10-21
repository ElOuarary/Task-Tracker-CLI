# Initialise the module that I will need
import json
import os
import sys


def create_task_file() -> None:
    '''Create a JSON task file if it does not exists'''
    file_name = "task.json"
    
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)
        print(f"{file_name} was created.")
        return None
    
    print(f"{file_name} already exists.")