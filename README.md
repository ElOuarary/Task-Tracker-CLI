# Task Tracker CLI
This is a Python console-based task tracker where the user tracks his tasks.  
The programme ofer the user the ability to add tasks, update them, and marking them.  

## Features
Creating the tasks.json file.  
Add tasks with unique properties: id, description, status, createdAT, updateAT.  
Update the description of taks based on their ids.  
Delete the tasks based on their ids.  
Mark the status of the tasks: in-progress, done.  
List tasks based on their status.  

## How to run
1) Use the command python main.py create.
2) Add the task that you want to track.
3) Update the task if you accomplish it or in progress with it.
4) Delete a task if you are no longer interested in it.
5) List the tasks that you are interseted with their comman status or all tasks.

##  Functions
-create_task_file() -> None: Create a JSON task file if it does not exists.  
-description_exists(description: str, tasks: list) -> bool: Check for the existence of the description in the tasks list.  
-id_exists(id: int, tasks: list) -> bool: Check for the existence of the id in the tasks list.  
-read_task_file() -> Optional[list]: Try to read the task.json file.  
-update_file(tasks: list) -> None: Update the task.json file.  
-add_task(description: str) -> None: Add a task to the task.json file.  
-update_task(id: int, new_description: str): Update a task in task.json file.  
-delete_task(id:int) -> None: Delete a task in task.json file.  
-list_task(status:str = None) -> None: List all task in the task.json file.  
-mark_in_progress(id:int) -> None: Mark a task as in progress.  
-mark_done(id:int) -> None: Mark a task as done.

## Requirements
Python 3.x

## How to run
1) Use the command "python main.py craete" to create the json file if it does not exits.
2) Use command "python main.py add 'description'" to add a task to the json file it will be initialize with its propretis.
3) Use command "python main.py update id 'new description'" to update the task with the specific id with a new description.
4) Use the command "python main.py mark_in_progress id" to mark the status of the task with id as in progress.
5) Use the command "python main.py mark_done id" to mark the status of thask with id as done.
6) Use the command "python main.py delete id" to delete the task with  the defiened id.
7) Use the command "python main.py list 'status'" to list the tasks with the comman status defiened, leaving status empty will result to listing all the tasks.
