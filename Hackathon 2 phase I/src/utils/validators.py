"""Input validation functions."""

from typing import Tuple


def validate_description(description: str) -> Tuple[bool, str]:
    """Validate task description.

    Args:
        description: The description to validate.

    Returns:
        Tuple of (is_valid, error_message_if_invalid).
        If valid, error_message is empty string.
    """
    if not description or not description.strip():
        return False, "Task description cannot be empty"
    if len(description) > 500:
        return False, f"Task description must be 500 characters or less (current: {len(description)})"
    return True, ""


def validate_task_id(task_id_str: str) -> Tuple[bool, int, str]:
    """Validate and parse task ID input.

    Args:
        task_id_str: The task ID string from user input.

    Returns:
        Tuple of (is_valid, parsed_id, error_message_if_invalid).
        If valid, parsed_id is the integer ID and error_message is empty.
        If invalid, parsed_id is -1.
    """
    try:
        task_id = int(task_id_str)
        if task_id < 1:
            return False, -1, "Task ID must be a positive number"
        return True, task_id, ""
    except ValueError:
        return False, -1, "Invalid task ID. Please enter a number"


def validate_yes_no(response: str) -> Tuple[bool, bool]:
    """Validate yes/no response.

    Args:
        response: User input string.

    Returns:
        Tuple of (is_valid, is_yes).
        is_yes is True if response is yes/y, False if no/n.
        is_valid is False if response is neither.
    """
    response_lower = response.strip().lower()
    if response_lower in ('y', 'yes'):
        return True, True
    if response_lower in ('n', 'no'):
        return True, False
    return False, False
