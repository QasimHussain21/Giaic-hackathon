# Research: In-Memory Console Todo Application

**Date**: 2026-02-06
**Phase**: 0 (Research & Technical Decisions)
**Feature**: 001-console-todo

## Purpose

Document technical research findings, technology decisions, and best practices for implementing the in-memory console todo application. This research informs the architecture and implementation approach for Phase I of the multi-phase todo application project.

## Research Questions Addressed

1. **Python Project Structure Best Practices**: How to organize a Python console application for maintainability and future extensibility?
2. **Testing Strategy**: What testing frameworks and patterns are recommended for Python CLI applications?
3. **Package Management**: UV vs pip/poetry - which package manager aligns with modern Python development?
4. **In-Memory Storage Patterns**: What data structures and patterns work best for in-memory task management?
5. **CLI Design Patterns**: What are the industry standards for building user-friendly console interfaces?
6. **PEP-8 and Code Quality**: What tools and practices ensure code quality and style compliance?

---

## Decision 1: Three-Layer Architecture

### Decision
Implement a three-layer architecture separating CLI, Business Logic, and Data concerns.

### Rationale
- **Separation of Concerns**: Each layer has a single, well-defined responsibility
- **Testability**: Business logic can be tested independently of CLI interaction
- **Future Migration**: Services and models layers can be reused in Phase II (FastAPI backend)
- **Maintainability**: Changes to one layer minimize impact on others

### Alternatives Considered
1. **Monolithic single-file approach**: Rejected - not maintainable or extensible
2. **Two-layer (CLI + Logic combined)**: Rejected - makes testing difficult and couples UI to logic
3. **MVC pattern**: Rejected - overkill for Phase I, though services layer serves similar purpose as controller

### Implementation
```
src/models/      → Data structures (Task dataclass)
src/services/    → Business logic (TaskManager)
src/cli/         → User interaction (menu, commands)
src/utils/       → Cross-cutting concerns (validation, formatting)
```

---

## Decision 2: UV for Package Management

### Decision
Use UV (ultra-fast Python package manager) for dependency management and virtual environment handling.

### Rationale
- **Modern Tool**: UV is the latest generation Python package manager (2024+)
- **Speed**: 10-100x faster than pip for dependency resolution and installation
- **All-in-One**: Combines pip, venv, and poetry functionality in single tool
- **Constitution Alignment**: User requirements explicitly specify UV
- **Future-Proof**: Designed for modern Python (3.8+), excellent Python 3.13 support

### Alternatives Considered
1. **pip + venv**: Rejected - slower, manual venv management, no lock files
2. **Poetry**: Rejected - slower than UV, more complex for simple projects
3. **pipenv**: Rejected - largely superseded by UV and Poetry

### Configuration
```toml
# pyproject.toml
[project]
name = "console-todo"
version = "1.0.0"
description = "In-memory console-based todo application"
requires-python = ">=3.13"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8.0.0", "pytest-cov>=4.1.0", "ruff>=0.1.0"]
```

---

## Decision 3: Python Dataclasses for Task Model

### Decision
Use Python 3.13 `dataclass` (not Pydantic, attrs, or plain classes) for the Task model.

### Rationale
- **Standard Library**: No external dependencies required
- **Type Safety**: Built-in type hints with runtime checks (Python 3.13+)
- **Immutability Options**: Supports `frozen=True` for immutable fields (task ID)
- **Default Values**: Clean syntax for defaults (timestamps, status)
- **Phase II Ready**: Dataclasses are compatible with Pydantic (Phase II requirement)

### Alternatives Considered
1. **Plain classes**: Rejected - verbose, no automatic `__init__`, `__repr__`, `__eq__`
2. **Pydantic BaseModel**: Rejected - unnecessary dependency for Phase I, but will use in Phase II
3. **attrs library**: Rejected - external dependency, dataclasses are sufficient
4. **TypedDict**: Rejected - no methods, less object-oriented

### Implementation Pattern
```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
```

---

## Decision 4: pytest for Testing Framework

### Decision
Use pytest with pytest-cov for testing and coverage reporting.

### Rationale
- **Industry Standard**: Most widely used Python testing framework
- **Simple Syntax**: No boilerplate, straightforward assertions
- **Powerful Fixtures**: Excellent test data and setup management
- **Coverage Integration**: pytest-cov provides detailed coverage reports
- **Constitution Compliance**: Testing is non-negotiable (Principle III)

### Alternatives Considered
1. **unittest (stdlib)**: Rejected - verbose, class-based, less Pythonic
2. **nose/nose2**: Rejected - less maintained, pytest is more popular
3. **No testing framework**: Rejected - violates constitution Principle III

### Testing Structure
```
tests/
├── unit/               # Fast, isolated tests for individual functions/classes
├── integration/        # Tests for multi-component interactions
└── conftest.py         # Shared fixtures and configuration
```

### Coverage Target
- **Minimum**: 80% (per constitution Phase I success criteria)
- **Focus**: Business logic (services/) and models/ should have near 100% coverage
- **Lower Priority**: CLI (menu.py, commands.py) can have lower coverage due to I/O mocking complexity

---

## Decision 5: In-Memory Storage Using Dictionary

### Decision
Store tasks in a Python dictionary with integer keys (task IDs) and Task objects as values.

### Rationale
- **O(1) Lookup**: Fast access by task ID
- **Natural Key-Value Mapping**: ID → Task is intuitive
- **Easy Iteration**: Can iterate over `.values()` for listing all tasks
- **Simple ID Generation**: `max(keys) + 1` or maintain counter

### Alternatives Considered
1. **List of tasks**: Rejected - O(n) lookup, ID management more complex
2. **OrderedDict**: Rejected - not needed, Python 3.7+ dicts maintain insertion order
3. **SQLite in-memory**: Rejected - violates "no database" constraint, overkill
4. **Class attribute storage**: Rejected - less flexible, harder to test

### Implementation Pattern
```python
class TaskManager:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
```

---

## Decision 6: Interactive Menu CLI (Not Command-Line Arguments)

### Decision
Implement an interactive REPL-style menu system instead of command-line arguments.

### Rationale
- **User Story 5 (P5)**: Specification explicitly requests interactive menu
- **Beginner-Friendly**: Easier for beginners than remembering CLI flags
- **Error Recovery**: Users can retry commands without restarting application
- **Clear Options**: Menu displays all available commands at once

### Alternatives Considered
1. **Command-line arguments** (`python main.py add "task"`): Rejected - less user-friendly, doesn't meet US5
2. **Mixed mode** (args or interactive): Rejected - adds complexity without clear benefit
3. **TUI framework** (Rich, Textual): Rejected - external dependency, overkill for Phase I

### Implementation Approach
```python
while True:
    display_menu()
    choice = input("Enter command: ").strip().lower()
    if choice == "1" or choice == "add":
        # Add task flow
    elif choice == "2" or choice == "list":
        # List tasks flow
    # etc.
```

---

## Decision 7: Ruff for Linting and Formatting

### Decision
Use Ruff for code quality checks (linting and formatting) to ensure PEP-8 compliance.

### Rationale
- **Unified Tool**: Combines functionality of flake8, black, isort, pydocstyle
- **Extremely Fast**: 10-100x faster than individual tools
- **PEP-8 Compliance**: Enforces Python style guide automatically
- **Constitution Requirement**: Phase I success criteria requires PEP-8 compliance

### Alternatives Considered
1. **Black + flake8 + isort**: Rejected - multiple tools, slower, configuration complexity
2. **Pylint**: Rejected - slower, more opinionated, less focused on PEP-8
3. **autopep8**: Rejected - only formatting, no linting

### Configuration
```toml
[tool.ruff]
line-length = 100
target-version = "py313"
select = ["E", "F", "W", "I", "N", "D"]  # PEP-8 errors, warnings, docstrings
```

---

## Decision 8: Input Validation Strategy

### Decision
Centralize validation logic in `src/utils/validators.py` with clear error messages.

### Rationale
- **DRY Principle**: Validation logic reused across CLI and services
- **Consistent Error Messages**: Single source of truth for validation rules
- **Testable**: Validators can be unit tested independently
- **Extensible**: Easy to add new validation rules

### Validation Rules
1. **Task Description**: Non-empty, non-whitespace-only, reasonable length (1-500 chars)
2. **Task ID**: Positive integer, exists in task list
3. **Menu Input**: Valid menu option or command alias

### Implementation Pattern
```python
def validate_description(description: str) -> tuple[bool, str]:
    """Validate task description.

    Returns:
        (is_valid, error_message_if_invalid)
    """
    if not description or not description.strip():
        return False, "Task description cannot be empty"
    if len(description) > 500:
        return False, "Task description must be 500 characters or less"
    return True, ""
```

---

## Decision 9: Console Output Formatting

### Decision
Use `src/utils/formatters.py` for consistent, readable console output without external libraries.

### Rationale
- **No Dependencies**: Use built-in string formatting
- **Consistent Look**: Centralized formatting ensures uniform output
- **Accessibility**: Plain text compatible with screen readers
- **Future Enhancement**: Easy to swap in Rich library in future if desired

### Formatting Patterns
```
Task List:
┌──────┬──────────────────────────────────────────┬──────────┐
│  ID  │ Description                              │ Status   │
├──────┼──────────────────────────────────────────┼──────────┤
│  1   │ Buy groceries                            │ ✓ Done   │
│  2   │ Write documentation                      │ ○ Todo   │
└──────┴──────────────────────────────────────────┴──────────┘
```

---

## Best Practices Summary

### Code Quality
- **PEP-8 Compliance**: Enforced by Ruff
- **Type Hints**: Use throughout codebase for clarity and type checking
- **Docstrings**: All public functions/classes must have docstrings (Google style)
- **Small Functions**: Keep functions under 50 lines, single responsibility
- **No Magic Numbers**: Use named constants

### Testing
- **Test First**: Write tests before implementation where possible (TDD for critical logic)
- **Descriptive Names**: Test function names describe what is being tested
- **Arrange-Act-Assert**: Structure tests clearly
- **Fixtures**: Use pytest fixtures for common test data

### Version Control
- **Atomic Commits**: Each commit represents one logical change
- **Conventional Commits**: Use format `type(scope): description`
- **Commit Before Refactor**: Commit working code before refactoring

### Documentation
- **README.md**: Project overview, setup instructions, usage examples
- **quickstart.md**: Step-by-step guide to get running quickly
- **Inline Comments**: Explain "why" not "what" for complex logic

---

## Phase II Migration Considerations

### What Stays the Same
- `src/models/task.py`: Task dataclass can be converted to Pydantic model
- `src/services/task_manager.py`: Business logic remains, add persistence layer
- Testing strategy and structure

### What Changes
- Replace in-memory dict with SQLModel + PostgreSQL
- CLI layer replaced/supplemented with FastAPI endpoints
- Add authentication and session management
- Add frontend (Next.js) consuming the API

### Migration-Ready Design Decisions
- Service layer isolates business logic from storage (repository pattern-like)
- Task model is storage-agnostic (only in-memory reference is in TaskManager)
- Validation and formatting utilities are reusable

---

## Tools & Dependencies Summary

### Runtime Dependencies (Phase I)
- Python 3.13+ (standard library only)

### Development Dependencies
- **pytest** ~= 8.0.0: Testing framework
- **pytest-cov** ~= 4.1.0: Coverage reporting
- **ruff** ~= 0.1.0: Linting and formatting

### Development Tools (not dependencies)
- **UV**: Package management
- **Git**: Version control
- **VS Code / PyCharm**: Recommended IDEs with Python support

---

## References

- [Python Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Ruff Linter](https://docs.astral.sh/ruff/)
- [Constitution: Phase I Requirements](./.specify/memory/constitution.md)
