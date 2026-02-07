"""Interactive CLI menu system."""

import signal
import sys
from typing import Callable, Optional
from src.services.task_manager import TaskManager
from src.cli.commands import (
    add_task_command,
    view_tasks_command,
    complete_task_command,
    update_task_command,
    delete_task_command,
    help_command
)


def display_welcome_banner() -> None:
    """Display welcome banner with ASCII art."""
    print("=" * 64)
    print("         Welcome to Console Todo Application v1.0             ")
    print("      Your tasks live here (until you close the app)         ")
    print("=" * 64)
    print()


def display_main_menu() -> None:
    """Display the main menu options."""
    print("Main Menu:")
    print("  1. Add new task")
    print("  2. View all tasks")
    print("  3. Mark task as complete")
    print("  4. Update task description")
    print("  5. Delete task")
    print("  6. Exit")
    print()


def get_user_command() -> str:
    """Get command input from user.

    Returns:
        User input string (lowercased and stripped).
    """
    return input("Enter command (1-6 or name): ").strip().lower()


def map_command_to_handler(
    command: str,
    task_manager: TaskManager
) -> Optional[Callable[[], None]]:
    """Map user input to command handler.

    Args:
        command: User input command.
        task_manager: TaskManager instance.

    Returns:
        Command handler function or None if invalid command.
    """
    # Command aliases mapping
    command_map = {
        '1': lambda: add_task_command(task_manager),
        'add': lambda: add_task_command(task_manager),
        'new': lambda: add_task_command(task_manager),
        'create': lambda: add_task_command(task_manager),
        '2': lambda: view_tasks_command(task_manager),
        'list': lambda: view_tasks_command(task_manager),
        'view': lambda: view_tasks_command(task_manager),
        'show': lambda: view_tasks_command(task_manager),
        'all': lambda: view_tasks_command(task_manager),
        '3': lambda: complete_task_command(task_manager),
        'complete': lambda: complete_task_command(task_manager),
        'done': lambda: complete_task_command(task_manager),
        'finish': lambda: complete_task_command(task_manager),
        '4': lambda: update_task_command(task_manager),
        'update': lambda: update_task_command(task_manager),
        'edit': lambda: update_task_command(task_manager),
        'modify': lambda: update_task_command(task_manager),
        '5': lambda: delete_task_command(task_manager),
        'delete': lambda: delete_task_command(task_manager),
        'remove': lambda: delete_task_command(task_manager),
        'rm': lambda: delete_task_command(task_manager),
        '6': lambda: exit_application(),
        'exit': lambda: exit_application(),
        'quit': lambda: exit_application(),
        'q': lambda: exit_application(),
        'help': lambda: help_command(),
        '?': lambda: help_command(),
        'h': lambda: help_command(),
    }

    return command_map.get(command)


def handle_invalid_command(command: str) -> None:
    """Handle invalid command input.

    Args:
        command: The invalid command entered.
    """
    print(f"\n[ERROR] Invalid command: \"{command}\"")
    print("\nPlease enter a number (1-6) or command name.")
    print("Type \"help\" to see available commands.\n")


def pause_for_user() -> None:
    """Pause and wait for user to press Enter."""
    input("\nPress Enter to continue...")
    print()


def exit_application() -> None:
    """Display goodbye message and exit."""
    print("\nGoodbye! Your tasks will be lost when the application closes.")
    print("\nThank you for using Console Todo Application.")
    sys.exit(0)


def handle_interrupt(signum, frame) -> None:
    """Handle Ctrl+C interrupt gracefully.

    Args:
        signum: Signal number.
        frame: Current stack frame.
    """
    print("\n\nInterrupt detected. Exiting gracefully...")
    exit_application()


def run_application_loop() -> None:
    """Run the main application loop."""
    # Setup interrupt handler
    signal.signal(signal.SIGINT, handle_interrupt)

    # Initialize task manager
    task_manager = TaskManager()

    # Display welcome banner
    display_welcome_banner()

    # Main loop
    while True:
        display_main_menu()
        command = get_user_command()

        # Map command to handler
        handler = map_command_to_handler(command, task_manager)

        if handler:
            handler()
            # Don't pause for exit or help commands
            if command not in ['6', 'exit', 'quit', 'q', 'help', '?', 'h']:
                pause_for_user()
        else:
            handle_invalid_command(command)
            pause_for_user()
