# Task Tracker CLI

This is a Python console-based task tracker where you can easily track your tasks through the command line. The program offers capabilities to add tasks, update them, and mark their status.

## Features

- **Create `tasks.json`**: Initializes a JSON file to store tasks.
- **Add Tasks**: Each task has unique properties such as `id`, `description`, `status`, `createdAT`, and `updateAT`.
- **Update Tasks**: Modify task descriptions by ID.
- **Delete Tasks**: Remove tasks by ID.
- **Status Tracking**: Mark tasks as “in-progress” or “done.”
- **Task Listing**: List tasks by their status or show all tasks.

## Requirements
- Python 3.7+

## Usage

- **Initialize the Task File**: Run `python main.py create` to create `tasks.json` if it doesn't already exist.
- **Add a Task**: Use `python main.py add 'description'` to add a task with a description.
- **Update a Task**: Update the description of a task by ID: `python main.py update <id> 'new description'`.
- **Delete a Task**: Delete a task by ID: `python main.py delete <id>`.
- **Mark Task in Progress**: Use `python main.py mark_in_progress <id>` to set a task's status to "in-progress".
- **Mark Task as Done**: Use `python main.py mark_done <id>` to set a task's status to "done".
- **List Tasks**: List tasks by status using `python main.py list <status>`. Use `list` alone to show all tasks.

## Functions

- `create_task_file() -> None`: Creates a JSON task file if it does not exist.
- `description_exists(description: str, tasks: list) -> bool`: Checks if the description is already in tasks.
- `id_exists(id: int, tasks: list) -> bool`: Checks if a task with the given ID exists.
- `file_readable() -> Optional[list]`: Reads and returns the contents of `tasks.json`.
- `update_file(tasks: list) -> None`: Updates `tasks.json`.
- `add_task(description: str) -> None`: Adds a new task.
- `update_task(id: int, new_description: str)`: Updates the task description by ID.
- `delete_task(id: int) -> None`: Deletes a task by ID.
- `list_task(status: str = None) -> None`: Lists all tasks, filtered by status if provided.
- `mark_in_progress(id: int) -> None`: Marks a task as "in-progress".
- `mark_done(id: int) -> None`: Marks a task as "done".

