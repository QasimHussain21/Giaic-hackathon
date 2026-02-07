"""Console output formatting functions."""

from typing import List
from src.models.task import Task


def format_task_list(tasks: List[Task]) -> str:
    """Format a list of tasks as a table.

    Args:
        tasks: List of tasks to format.

    Returns:
        Formatted table string.
    """
    if not tasks:
        return "\n  No tasks yet! Use \"Add new task\" to create your first task.\n"

    # Calculate column widths
    id_width = 6
    desc_width = max(50, max(len(task.description) for task in tasks) + 2)
    status_width = 11

    # Build table
    lines = []
    lines.append("\nYour Tasks:")

    # Header
    lines.append("+" + "-" * id_width + "+" + "-" * desc_width + "+" + "-" * status_width + "+")
    lines.append("|" + "  ID  " + "|" + " Description".ljust(desc_width) + "|" + "  Status   " + "|")
    lines.append("+" + "-" * id_width + "+" + "-" * desc_width + "+" + "-" * status_width + "+")

    # Rows
    for task in tasks:
        status = "[DONE]" if task.completed else "[TODO]"
        desc = task.description[:desc_width-2] if len(task.description) > desc_width-2 else task.description
        lines.append(
            f"|  {task.id:<4}| {desc.ljust(desc_width-1)}| {status.ljust(status_width-1)}|"
        )

    # Footer
    lines.append("+" + "-" * id_width + "+" + "-" * desc_width + "+" + "-" * status_width + "+")

    # Summary
    completed = sum(1 for task in tasks if task.completed)
    pending = len(tasks) - completed
    lines.append(f"\nTotal: {len(tasks)} tasks ({completed} completed, {pending} pending)")

    return "\n".join(lines)


def format_success(message: str, task: Task = None) -> str:
    """Format a success message.

    Args:
        message: The success message.
        task: Optional task to include details.

    Returns:
        Formatted success message.
    """
    lines = [f"[SUCCESS] {message}"]
    if task:
        status = "Done" if task.completed else "Todo"
        lines.append(f"  ID: {task.id}")
        lines.append(f"  Description: {task.description}")
        lines.append(f"  Status: {status}")
    return "\n".join(lines)


def format_error(message: str, suggestion: str = None) -> str:
    """Format an error message.

    Args:
        message: The error message.
        suggestion: Optional suggestion for fixing the error.

    Returns:
        Formatted error message.
    """
    lines = [f"[ERROR] {message}"]
    if suggestion:
        lines.append(suggestion)
    return "\n".join(lines)


def format_info(message: str) -> str:
    """Format an informational message.

    Args:
        message: The info message.

    Returns:
        Formatted info message.
    """
    return f"[INFO] {message}"
