"""Task management service for CRUD operations."""

from typing import Optional
from src.models.task import Task


class TaskManager:
    """Manages a collection of tasks in memory.

    This class provides CRUD operations for tasks and maintains
    the in-memory storage of all tasks during the application session.
    """

    def __init__(self) -> None:
        """Initialize an empty task manager."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """Add a new task.

        Args:
            description: The task description.

        Returns:
            The newly created task.

        Raises:
            ValueError: If description is invalid.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks.

        Returns:
            List of all tasks (may be empty).
        """
        return list(self._tasks.values())

    def task_count(self) -> int:
        """Return the number of tasks.

        Returns:
            The total number of tasks.
        """
        return len(self._tasks)

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update a task's description.

        Args:
            task_id: The ID of the task to update.
            new_description: The new description text.

        Returns:
            True if updated successfully, False if task not found.

        Raises:
            ValueError: If new_description is invalid.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.update_description(new_description)
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete.

        Returns:
            True if marked successfully, False if task not found.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.mark_complete()
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            True if deleted successfully, False if task not found.
        """
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True
