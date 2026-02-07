"""Pytest configuration and fixtures for console-todo tests."""

import pytest
from datetime import datetime
from src.models.task import Task
from src.services.task_manager import TaskManager


@pytest.fixture
def sample_task():
    """Create a sample task for testing."""
    return Task(
        id=1,
        description="Buy groceries",
        completed=False,
        created_at=datetime(2026, 2, 6, 10, 0, 0)
    )


@pytest.fixture
def completed_task():
    """Create a completed task for testing."""
    task = Task(
        id=2,
        description="Write documentation",
        completed=False,
        created_at=datetime(2026, 2, 6, 11, 0, 0)
    )
    task.mark_complete()
    return task


@pytest.fixture
def task_manager():
    """Create a fresh TaskManager instance for testing."""
    return TaskManager()


@pytest.fixture
def task_manager_with_tasks(task_manager):
    """Create a TaskManager with some pre-populated tasks."""
    task_manager.add_task("Buy groceries")
    task_manager.add_task("Write documentation")
    task_manager.add_task("Review pull requests")
    return task_manager
