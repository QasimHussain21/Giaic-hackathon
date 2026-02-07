"""Task model for the console todo application."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique identifier for the task.
        description: What needs to be done.
        completed: Whether the task is marked as complete.
        created_at: When the task was created.
    """

    id: int
    description: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validate task data after initialization.

        Raises:
            ValueError: If task data is invalid.
        """
        if self.id < 1:
            raise ValueError("Task ID must be a positive integer")
        if not self.description or not self.description.strip():
            raise ValueError("Task description cannot be empty")
        if len(self.description) > 500:
            raise ValueError("Task description must be 500 characters or less")

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.completed = True

    def update_description(self, new_description: str) -> None:
        """Update the task description with validation.

        Args:
            new_description: The new description text.

        Raises:
            ValueError: If the new description is invalid.
        """
        if not new_description or not new_description.strip():
            raise ValueError("Task description cannot be empty")
        if len(new_description) > 500:
            raise ValueError("Task description must be 500 characters or less")
        self.description = new_description

    def __str__(self) -> str:
        """Human-readable string representation."""
        status = "Done" if self.completed else "Todo"
        return f"[{self.id}] {self.description} ({status})"
