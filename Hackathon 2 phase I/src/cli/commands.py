"""CLI command handlers for todo operations."""

from src.services.task_manager import TaskManager
from src.utils.validators import validate_description, validate_task_id, validate_yes_no
from src.utils.formatters import (
    format_task_list,
    format_success,
    format_error,
    format_info
)


def add_task_command(task_manager: TaskManager) -> None:
    """Handle the add task command.

    Args:
        task_manager: The TaskManager instance.
    """
    print("\nYou selected: Add new task")
    description = input("Enter task description: ").strip()

    # Validate description
    is_valid, error_msg = validate_description(description)
    if not is_valid:
        print(f"\n{format_error(error_msg)}")
        print("Please try again.\n")
        return

    try:
        task = task_manager.add_task(description)
        print(f"\n{format_success('Task added successfully!', task)}\n")
    except ValueError as e:
        print(f"\n{format_error(str(e))}\n")


def view_tasks_command(task_manager: TaskManager) -> None:
    """Handle the view tasks command.

    Args:
        task_manager: The TaskManager instance.
    """
    print("\nYou selected: View all tasks")
    tasks = task_manager.get_all_tasks()
    print(format_task_list(tasks))
    print()


def complete_task_command(task_manager: TaskManager) -> None:
    """Handle the mark task complete command.

    Args:
        task_manager: The TaskManager instance.
    """
    print("\nYou selected: Mark task as complete")
    task_id_str = input("Enter task ID: ").strip()

    # Validate task ID
    is_valid, task_id, error_msg = validate_task_id(task_id_str)
    if not is_valid:
        print(f"\n{format_error(error_msg)}\n")
        return

    # Check if task exists
    task = task_manager.get_task(task_id)
    if task is None:
        print(f"\n{format_error(f'Task with ID {task_id} not found.')}")
        print("Use \"View all tasks\" to see available task IDs.\n")
        return

    # Check if already complete
    if task.completed:
        print(f"\n{format_info('Task is already marked as complete.')}")
        print(f"  ID: {task.id}")
        print(f"  Description: {task.description}")
        print(f"  Status: Done\n")
        return

    # Mark complete
    task_manager.mark_task_complete(task_id)
    print(f"\n{format_success('Task marked as complete!', task)}\n")


def update_task_command(task_manager: TaskManager) -> None:
    """Handle the update task command.

    Args:
        task_manager: The TaskManager instance.
    """
    print("\nYou selected: Update task description")
    task_id_str = input("Enter task ID: ").strip()

    # Validate task ID
    is_valid, task_id, error_msg = validate_task_id(task_id_str)
    if not is_valid:
        print(f"\n{format_error(error_msg)}\n")
        return

    # Check if task exists
    task = task_manager.get_task(task_id)
    if task is None:
        print(f"\n{format_error(f'Task with ID {task_id} not found.')}")
        print("Use \"View all tasks\" to see available task IDs.\n")
        return

    # Show current description
    print(f"Current description: {task.description}")
    new_description = input("Enter new description: ").strip()

    # Validate new description
    is_valid, error_msg = validate_description(new_description)
    if not is_valid:
        print(f"\n{format_error(error_msg)}")
        print("Please try again.\n")
        return

    # Update task
    try:
        task_manager.update_task(task_id, new_description)
        print(f"\n[SUCCESS] Task updated successfully!")
        print(f"  ID: {task_id}")
        print(f"  Old: {task.description}")
        print(f"  New: {new_description}\n")
    except ValueError as e:
        print(f"\n{format_error(str(e))}\n")


def delete_task_command(task_manager: TaskManager) -> None:
    """Handle the delete task command.

    Args:
        task_manager: The TaskManager instance.
    """
    print("\nYou selected: Delete task")
    task_id_str = input("Enter task ID: ").strip()

    # Validate task ID
    is_valid, task_id, error_msg = validate_task_id(task_id_str)
    if not is_valid:
        print(f"\n{format_error(error_msg)}\n")
        return

    # Check if task exists
    task = task_manager.get_task(task_id)
    if task is None:
        print(f"\n{format_error(f'Task with ID {task_id} not found.')}")
        print("Use \"View all tasks\" to see available task IDs.\n")
        return

    # Show task and confirm
    status = "Done" if task.completed else "Todo"
    print(f"Current task: {task.description} ({status})")
    confirmation = input("Are you sure you want to delete this task? (y/n): ").strip()

    is_valid, is_yes = validate_yes_no(confirmation)
    if not is_valid:
        print(f"\n{format_error('Invalid input. Please enter y or n')}\n")
        return

    if not is_yes:
        print(f"\n{format_info('Delete cancelled. Task not removed.')}\n")
        return

    # Delete task
    task_manager.delete_task(task_id)
    print(f"\n[SUCCESS] Task deleted successfully!")
    print(f"  ID: {task_id}")
    print(f"  Description: {task.description}\n")


def help_command() -> None:
    """Display help information about available commands."""
    print("\nHelp - Available Commands:")
    print("  1 / add      - Add a new task")
    print("  2 / list     - View all tasks")
    print("  3 / complete - Mark a task as done")
    print("  4 / update   - Update task description")
    print("  5 / delete   - Remove a task")
    print("  6 / exit     - Quit the application")
    print("\nTips:")
    print("  - Task IDs are shown in the \"View all tasks\" list")
    print("  - Use ID numbers to reference specific tasks")
    print("  - All tasks are stored in memory only\n")
