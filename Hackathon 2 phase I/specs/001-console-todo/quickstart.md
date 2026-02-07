# Quickstart Guide: Console Todo Application

**Last Updated**: 2026-02-06
**Phase**: I (Console Application)
**Prerequisites**: Python 3.13+, UV package manager

## Overview

This guide will help you set up and run the In-Memory Console Todo Application in under 5 minutes. The application is a command-line tool for managing todo tasks during a single session.

---

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.13 or later** installed
   ```bash
   python --version
   # Should show: Python 3.13.x or higher
   ```

2. **UV package manager** installed
   ```bash
   # Install UV (one-time setup)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Or on Windows (PowerShell):
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Verify installation
   uv --version
   ```

3. **Git** (for cloning the repository)

---

## Step 1: Clone the Repository

```bash
# Clone the project
git clone <repository-url>
cd <repository-name>

# Checkout the feature branch
git checkout 001-console-todo
```

---

## Step 2: Set Up the Project

UV will automatically create a virtual environment and install dependencies:

```bash
# Initialize the project (first time only)
uv sync

# This command:
# - Creates a virtual environment in .venv/
# - Installs all dependencies from pyproject.toml
# - Creates uv.lock file for reproducible installs
```

**Expected output**:
```
Resolved X packages in XXXms
Installed X packages in XXXms
```

---

## Step 3: Run the Application

```bash
# Run the application
uv run main.py
```

**You should see**:
```
╔══════════════════════════════════════════════════════════════╗
║         Welcome to Console Todo Application v1.0             ║
║      Your tasks live here (until you close the app)         ║
╚══════════════════════════════════════════════════════════════╝

Main Menu:
  1. Add new task
  2. View all tasks
  3. Mark task as complete
  4. Update task description
  5. Delete task
  6. Exit

Enter command (1-6 or name): _
```

---

## Step 4: Try Basic Operations

### Add Your First Task

1. Enter `1` or `add`
2. When prompted, type: `Buy groceries`
3. Press Enter

**Expected**:
```
✓ Task added successfully!
  ID: 1
  Description: Buy groceries
  Status: Todo
```

### View Your Tasks

1. Enter `2` or `list`

**Expected**:
```
Your Tasks:
┌──────┬──────────────────────────────────────────────────────┬───────────┐
│  ID  │ Description                                          │  Status   │
├──────┼──────────────────────────────────────────────────────┼───────────┤
│  1   │ Buy groceries                                        │ ○ Todo    │
└──────┴──────────────────────────────────────────────────────┴───────────┘

Total: 1 tasks (0 completed, 1 pending)
```

### Mark Task as Complete

1. Enter `3` or `complete`
2. When prompted for ID, type: `1`

**Expected**:
```
✓ Task marked as complete!
  ID: 1
  Description: Buy groceries
  Status: ✓ Done
```

### Exit the Application

1. Enter `6` or `exit`

**Expected**:
```
Goodbye! Your tasks will be lost when the application closes.

Thank you for using Console Todo Application.
```

---

## Common Commands Reference

| Command          | Number | What It Does                              |
|------------------|--------|-------------------------------------------|
| `add`, `new`     | 1      | Create a new todo task                    |
| `list`, `view`   | 2      | Show all tasks                            |
| `complete`       | 3      | Mark a task as done                       |
| `update`, `edit` | 4      | Change a task's description               |
| `delete`, `rm`   | 5      | Remove a task permanently                 |
| `exit`, `quit`   | 6      | Close the application                     |
| `help`, `?`      | -      | Show available commands                   |

---

## Running Tests

### Run All Tests

```bash
# Run all tests with coverage
uv run pytest --cov=src tests/

# Expected output shows test results and coverage percentage
```

### Run Specific Test Files

```bash
# Unit tests only
uv run pytest tests/unit/

# Integration tests only
uv run pytest tests/integration/

# Specific test file
uv run pytest tests/unit/test_task_manager.py
```

### View Detailed Coverage Report

```bash
# Generate HTML coverage report
uv run pytest --cov=src --cov-report=html tests/

# Open coverage report in browser
# Report is in htmlcov/index.html
```

---

## Development Workflow

### Code Quality Checks

```bash
# Lint and format code with Ruff
uv run ruff check src/ tests/

# Auto-fix issues
uv run ruff check --fix src/ tests/

# Format code
uv run ruff format src/ tests/
```

### Project Structure

```
.
├── src/
│   ├── models/          # Data structures (Task)
│   ├── services/        # Business logic (TaskManager)
│   ├── cli/             # User interface (menu, commands)
│   └── utils/           # Helpers (validators, formatters)
├── tests/
│   ├── unit/            # Unit tests for individual components
│   └── integration/     # End-to-end flow tests
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration
└── README.md            # Project documentation
```

---

## Troubleshooting

### Issue: "python: command not found"

**Solution**: Install Python 3.13+ from [python.org](https://www.python.org/downloads/)

---

### Issue: "uv: command not found"

**Solution**: Install UV package manager:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### Issue: "Module not found" errors

**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
uv sync
uv run main.py  # Always use 'uv run' prefix
```

---

### Issue: Tests failing

**Solution**: Check if you're in the correct directory and environment:
```bash
# Verify you're in project root
pwd

# Re-sync dependencies
uv sync

# Run tests
uv run pytest
```

---

### Issue: Application won't start

**Solution**: Check Python version compatibility:
```bash
python --version
# Must be 3.13 or higher

# If using older Python, upgrade:
# - Download from python.org
# - Or use pyenv: pyenv install 3.13
```

---

## Tips & Best Practices

### For Beginners

1. **Start with "View all tasks"** to see the empty state
2. **Add 2-3 tasks** to practice
3. **Try invalid inputs** (empty description, wrong ID) to see error handling
4. **Use command aliases** - type `add` instead of `1` if it's easier to remember

### For Development

1. **Run tests before committing**:
   ```bash
   uv run pytest --cov=src tests/
   ```

2. **Format code before committing**:
   ```bash
   uv run ruff format src/ tests/
   ```

3. **Check code quality**:
   ```bash
   uv run ruff check src/ tests/
   ```

4. **Use type hints** - the codebase uses Python type hints for better IDE support

---

## What's Next?

After getting comfortable with the console application:

1. **Explore the code**: Start with `src/models/task.py` and `src/services/task_manager.py`
2. **Read the tests**: `tests/unit/` shows how each component works
3. **Try modifications**: Add new features like task priorities or categories
4. **Phase II Preview**: The architecture is designed for easy migration to a web application

---

## Getting Help

### Documentation

- **Feature Spec**: `specs/001-console-todo/spec.md` - User requirements
- **Implementation Plan**: `specs/001-console-todo/plan.md` - Architecture decisions
- **Data Model**: `specs/001-console-todo/data-model.md` - Entity definitions
- **CLI Contracts**: `specs/001-console-todo/contracts/cli-commands.md` - Command reference

### Interactive Help

Type `help` or `?` in the application menu to see available commands.

### Issues

If you encounter bugs or have questions, check:
1. Are you on the correct branch? (`git branch` should show `001-console-todo`)
2. Is Python 3.13+ installed? (`python --version`)
3. Are dependencies installed? (`uv sync`)

---

## Success Checklist

After completing this quickstart, you should be able to:

- ✅ Launch the console application
- ✅ Add a new task
- ✅ View all tasks
- ✅ Mark a task as complete
- ✅ Update a task description
- ✅ Delete a task
- ✅ Exit the application
- ✅ Run the test suite
- ✅ Check code quality with Ruff

**Congratulations! You're ready to use and develop the Console Todo Application.** 🎉
